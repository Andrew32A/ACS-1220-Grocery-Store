from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, ValidationError
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button

    title = StringField('Store Title', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your title needs to be betweeen 3 and 80 chars")
        ])
    address = StringField('Address',
        validators=[
            DataRequired(),
            Length(min=3, max=80, message="Your Address needs to be betweeen 3 and 80 chars")
        ])
    submit = SubmitField('Submit')

    # def validate_title(form, field):
    #     if 'banana' in field.data:
    #         raise ValidationError('Title cannot contain the word banana')


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button

    name = StringField('Name', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your title needs to be betweeen 3 and 80 chars")
        ])
    price = FloatField('Price', validators=[DataRequired()])
    category = SelectField('Category', choices=ItemCategory.choices(), validators=[DataRequired()])
    photo_url = StringField('Photo', validators=[DataRequired()])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query, validators=[DataRequired()])
    submit = SubmitField('Submit')
