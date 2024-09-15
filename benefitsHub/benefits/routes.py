from flask import (render_template, url_for, flash, redirect,
                   request, Blueprint, current_app, abort)
from flask_login import login_user, current_user, logout_user, login_required
from benefitsHub import db, bcrypt, email
from benefitsHub.models.base_model import Benefit, User, Post
from benefitsHub.benefits.forms import BenefitForm
from benefitsHub.benefits.utils import linkify, save_picture
import os
from werkzeug.utils import secure_filename


benefits = Blueprint('benefits', __name__)


@benefits.route('/benefit/new', methods=["GET", "POST"])
@login_required
def new_benefit():
    """Flask route to create a new benefit"""
    form = BenefitForm()
    picture_file = None
    if form.validate_on_submit():
       if form.benefit_image.data:
        picture_file = save_picture(form.benefit_image.data)
        benefit_image = picture_file
        print(f"picture_file: {picture_file}")

       # Apply linkify and debug output
        description_linkified = linkify(form.description.data)
        requirement_linkified = linkify(form.benefit_requirement.data)

        benefit = Benefit(name=form.name.data,
                          description=description_linkified,
                          benefit_image=str(picture_file),
                          benefit_requirement=requirement_linkified,
                          benefit_link=form.benefit_link.data,
                          benefit_start_date=form.benefit_start_date.data,
                          benefit_end_date=form.benefit_end_date.data,
                          benefit_status=form.benefit_status.data,
                          benefit_created_by=current_user.username,
                          user_id=current_user.id)
        db.session.add(benefit)
        db.session.commit()
        print(f"Image: {picture_file}")
        flash(f'Benefit {form.name.data} has been created!', 'success')
        return redirect(url_for('benefits.user_benefits', username=current_user.username))
    image_file = url_for('static', filename='uploads/' + str(picture_file))
    return render_template('create_benefit.html', title='New Benefit', image_file=image_file, form=form)


@benefits.route("/user_benefit/<string:username>")
def user_benefits(username):
    """View a user's posted benefits"""
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    Benefit.query.filter_by(user=user)\
                            .order_by(Benefit.benefit_created_on\
                            .desc()).paginate(page=1)
    benefits = Benefit.query.filter_by(user=user)\
            .order_by(Benefit.benefit_created_on.desc())\
            .paginate(page=page, per_page=10)
    return render_template('user_benefits.html', title='user benefits', benefits=benefits, user=user)


@benefits.route("/explore_benefits")
def explore_benefits():
    """Route tp view all benefits"""
    page = request.args.get('page', type=int)
    benefits = Benefit.query\
               .order_by(Benefit.benefit_created_on\
               .desc()).paginate(page=page, per_page=10)
    return render_template('explore_benefits.html',
                           benefits=benefits, title='Explore Benefits')


@benefits.route("/benefit/<int:benefit_id>")
def benefit(benefit_id):
    """View a single benefit by its id"""
    benefit = Benefit.query.get_or_404(benefit_id)
    return render_template('benefit.html', title=f'benefit {benefit.id}', benefit=benefit)


@benefits.route("/benefit/<int:benefit_id>/update", methods=["GET", "POST"])
@login_required
def update_benefit(benefit_id):
    """Updates a benefit"""
    benefit = Benefit.query.get_or_404(benefit_id)
    if benefit.benefit_created_by != current_user.username:
        abort(403)
    form = BenefitForm()
    if form.validate_on_submit():
        benefit.name = form.name.data
        benefit.benefit_image = form.benefit_image.data
        benefit.benefit_requirement = form.benefit_requirement.data
        benefit.description = form.description.data
        benefit.benefit_link = form.benefit_link.data
        benefit.benefit_start_date = form.benefit_start_date.data
        benefit.benefit_end_date = form.benefit_end_date.data
        benefit.benefit_created_by = form.benefit_created_by.data
        benefit.benefit_updated_on = form.benefit_updated_on.data
        db.session.commit()
        flash('Your benefit has been updated!', 'success')
        return redirect(url_for('benefits.benefit', benefit_id=benefit.id))
    elif request.method == 'GET':
        form.name.data = benefit.name
        form.benefit_requirement.data = benefit.benefit_requirement
        form.description.data = benefit.description
        form.benefit_link.data = benefit.benefit_link
        form.benefit_start_date.data = benefit.benefit_start_date
        form.benefit_end_date.data = benefit.benefit_end_date
        form.benefit_created_by.data = benefit.benefit_created_by
        form.benefit_updated_on.data = benefit.benefit_updated_on
    return render_template('create_benefit.html', title='Update Benefit', form=form, legend='Update Benefit')


@benefits.route("/benefit/<int:benefit_id>/delete", methods=["POST"])
@login_required
def delete_benefit(benefit_id):
    """Updates a benefit"""
    benefit = Benefit.query.get_or_404(benefit_id)
    if benefit.benefit_created_by != current_user.username:
        abort(403)
    db.session.delete(benefit)
    db.session.commit()
    flash('Your benefit has been deleted!', 'success')
    return redirect(url_for('benefits.explore_benefit'))
