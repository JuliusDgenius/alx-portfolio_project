"""
This module contains the routes for the posts blueprint.
"""
from flask import (render_template, url_for, flash,
                   redirect, request, Blueprint, abort)
from flask_login import current_user, login_required
from benefitsHub import db
from benefitsHub.models.base_model import Post
from benefitsHub.posts.forms import MakePostForm
import os
from benefitsHub.posts.utils import save_picture


posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=["GET", "POST"])
@login_required
def new_post():
    """Function to create a new post"""
    form = MakePostForm()
    picture_file = None
    if form.validate_on_submit():
        # Save the post image if provided
        if form.post_image.data:
            picture_file = save_picture(form.post_image.data)
            post_image = picture_file
        post = Post(title=form.title.data,
                    content=form.content.data,
                    author=current_user.username,
                    user_id=current_user.id,
                    post_image = picture_file)
        db.session.add(post)
        db.session.commit()
        flash(f'Post {form.title.data} has been created!', 'success')
        return redirect(url_for('posts.view_posts'))
    image_file = url_for('static', filename='post_uploads/' + (picture_file if picture_file else 'default.jpeg'))
    return render_template('create_post.html', title='New Post', form=form, image_file=image_file)


@posts.route("/view_posts", methods=['GET', 'POST'])
def view_posts():
    """Flask route to view posts made by users"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('view_posts.html', posts=posts, title='View Posts')


@posts.route("/post/<int:post_id>")
def post(post_id):
    """View a single post by its id"""
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=f'post {post.id}', post=post)


@posts.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    """Updates a post"""
    post = Post.query.get_or_404(post_id)
    if post.author != current_user.username:
        abort(403)
    form = MakePostForm()
    if form.validate_on_submit():
        if form.post_image.data:
            picture_file = save_picture(form.post_image.data)
            post.post_image = picture_file
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.post_image.data = post.post_image
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html',
                           title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    """Deletes a post"""
    post = Post.query.get_or_404(post_id)
    if post.author != current_user.username:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('posts.view_post'))
