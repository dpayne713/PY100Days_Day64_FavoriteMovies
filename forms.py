from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, URL, Length, InputRequired
import datetime as dt


class UpdateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message=""), Length(min=1)])
    year = IntegerField('Year (Optional)', validators=[NumberRange(min=1910, max=dt.datetime.now().year)])
    description = TextAreaField('Description', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired(), NumberRange(min=0, max=10.0)])
    ranking = IntegerField('Ranking', validators=[DataRequired(), NumberRange(min=1, max=10)])
    review = TextAreaField('Review', validators=[DataRequired()])

class AddForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(message="Movie title required")])
    year = IntegerField('Year (Optional)', validators=[NumberRange(min=1910, max=dt.datetime.now().year)])

