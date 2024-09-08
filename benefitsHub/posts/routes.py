from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from benefitsHub import db
from benefitsHub.models.base_model import Post
from benefitsHub.posts.forms import MakePostForm
import os


posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=["GET", "POST"])
@login_required
def new_post():
    """Function to create a new post"""
    form = MakePostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data,
                    author=current_user.username,
                    user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash(f'Post {form.title.data} has been created!', 'success')
        return redirect(url_for('posts.view_posts'))
    return render_template('create_post.html', title='New Post', form=form)


@posts.route("/view_posts", methods=['GET', 'POST'])
def view_posts():
    """Flask route to view posts made by users"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('view_posts.html', posts=posts, title='View Posts')
