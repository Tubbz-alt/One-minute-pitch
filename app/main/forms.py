from flask_wtf import FlaskForm
from wtforms.validators import Required,Email
from wtforms import SubmitField, TextAreaField, StringField,ValidationError
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class GeneralForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class GeneralReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')


class SaleForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class SaleReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')


class SeductionForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class SeductionReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')


class MusicForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class MusicReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')

class ProjectForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class ProjectReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')


class InterviewForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class InterviewReviewForm(FlaskForm):
    review = StringField('Review': ', validators=[Required()])
    submit = SubmitField('Submit')


class AdvertisementForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class AdvertisementReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')
