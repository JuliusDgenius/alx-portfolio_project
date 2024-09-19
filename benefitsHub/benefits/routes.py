"""
This module defines the routes for the application.
"""
from flask import (render_template, url_for, flash, redirect,
                   request, Blueprint, abort)
from flask_login import current_user, login_required
from benefitsHub import db
from benefitsHub.models.base_model import Benefit, User
from benefitsHub.benefits.forms import BenefitForm
from benefitsHub.benefits.utils import save_picture
from markdown import markdown
from bleach.sanitizer import Cleaner
from bleach.linkifier import LinkifyFilter

cleaner = Cleaner(tags=['p', 'br', 'ul', 'ol', 'li', 'a'],
                  filters=[LinkifyFilter])

def linkify(text):
    return cleaner.clean(text)


# Create a Blueprint for benefits
benefits = Blueprint('benefits', __name__)


@benefits.route('/benefit/new', methods=["GET", "POST"])
@login_required
def new_benefit():
    """Flask route to create a new benefit"""
    form = BenefitForm()
    picture_file = None
    if form.validate_on_submit():
        # Save the benefit image if provided
        if form.benefit_image.data:
            picture_file = save_picture(form.benefit_image.data)
            benefit_image = picture_file

        # Apply linkify to description and requirement
        description_linkified = linkify(markdown(form.description.data, extensions=['extra']))
        sanitized_description = cleaner.clean(description_linkified)
        requirement_linkified = linkify(markdown(form.benefit_requirement.data, extensions=['extra']))
        sanitized_requirement = cleaner.clean(requirement_linkified)

        # Create a new Benefit object
        benefit = Benefit(name=form.name.data,
                          description=sanitized_description,
                          benefit_image=str(picture_file),
                          benefit_requirement=sanitized_requirement,
                          benefit_link=form.benefit_link.data,
                          benefit_start_date=form.benefit_start_date.data,
                          benefit_end_date=form.benefit_end_date.data,
                          benefit_status=form.benefit_status.data,
                          benefit_created_by=current_user.username,
                          user_id=current_user.id)
        # Add and commit the new benefit to the database
        db.session.add(benefit)
        db.session.commit()
        print(f"Image: {picture_file}")
        flash(f'Benefit {form.name.data} has been created!', 'success')
        return redirect(url_for('benefits.user_benefits',
                                username=current_user.username))
    # Generate URL for the benefit image
    image_file = url_for('static', filename='uploads/' + (picture_file if picture_file else 'default.jpeg'))
    return render_template('create_benefit.html', title='New Benefit',
                           image_file=image_file, form=form)


@benefits.route("/user_benefit/<string:username>")
def user_benefits(username):
    """View a user's posted benefits"""
    page = request.args.get('page', 1, type=int)
    # Get the user or return 404 if not found
    user = User.query.filter_by(username=username).first_or_404()
    # Query benefits for the user, ordered by creation date
    Benefit.query.filter_by(user=user)\
        .order_by(Benefit.benefit_created_on
                  .desc()).paginate(page=1)
    benefits = Benefit.query.filter_by(user=user)\
        .order_by(Benefit.benefit_created_on.desc())\
        .paginate(page=page, per_page=10)
    return render_template('user_benefits.html', title='user benefits',
                           benefits=benefits, user=user)


@benefits.route("/explore_benefits")
def explore_benefits():
    """Route to view all benefits"""
    page = request.args.get('page', 1,  type=int)
    # Query all benefits, ordered by creation date
    benefits = Benefit.query.order_by(Benefit.benefit_created_on.desc()).paginate(page=page, per_page=10)
    return render_template('explore_benefits.html',
                           benefits=benefits, title='Explore Benefits')


@benefits.route("/benefit/<int:benefit_id>")
def benefit(benefit_id):
    """View a single benefit by its id"""
    # Get the benefit or return 404 if not found
    benefit = Benefit.query.get_or_404(benefit_id)
    return render_template('benefit.html', title=f'benefit {benefit.id}',
                           benefit=benefit)


@benefits.route("/benefit/<int:benefit_id>/update", methods=["GET", "POST"])
@login_required
def update_benefit(benefit_id):
    """Updates a benefit"""
    # Get the benefit or return 404 if not found
    benefit = Benefit.query.get_or_404(benefit_id)
    # Check if the current user is the creator of the benefit
    if benefit.benefit_created_by != current_user.username:
        abort(403)
    form = BenefitForm()
    if form.validate_on_submit():
        # Update benefit fields with form data
        benefit.name = form.name.data
        if form.benefit_image.data:
            picture_file = save_picture(form.benefit_image.data)
            benefit.benefit_image = picture_file
        benefit.benefit_requirement = form.benefit_requirement.data
        benefit.description = form.description.data
        benefit.benefit_link = form.benefit_link.data
        benefit.benefit_start_date = form.benefit_start_date.data
        benefit.benefit_end_date = form.benefit_end_date.data
        benefit.benefit_created_by = form.benefit_created_by.data
        benefit.benefit_updated_on = form.benefit_updated_on.data
        # Commit changes to the database
        db.session.commit()
        flash('Your benefit has been updated!', 'success')
        return redirect(url_for('benefits.benefit', benefit_id=benefit.id))
    elif request.method == 'GET':
        # Populate form fields with existing benefit data
        form.name.data = benefit.name
        form.benefit_requirement.data = benefit.benefit_requirement
        form.description.data = benefit.description
        form.benefit_link.data = benefit.benefit_link
        form.benefit_start_date.data = benefit.benefit_start_date
        form.benefit_end_date.data = benefit.benefit_end_date
        form.benefit_created_by.data = benefit.benefit_created_by
        form.benefit_updated_on.data = benefit.benefit_updated_on
    return render_template('create_benefit.html', title='Update Benefit',
                           form=form, legend='Update Benefit')


@benefits.route("/benefit/<int:benefit_id>/delete", methods=["POST"])
@login_required
def delete_benefit(benefit_id):
    """Deletes a benefit"""
    # Get the benefit or return 404 if not found
    benefit = Benefit.query.get_or_404(benefit_id)
    # Check if the current user is the creator of the benefit
    if benefit.benefit_created_by != current_user.username:
        abort(403)
    # Delete the benefit from the database
    db.session.delete(benefit)
    db.session.commit()
    flash('Your benefit has been deleted!', 'success')
    return redirect(url_for('benefits.explore_benefit'))
