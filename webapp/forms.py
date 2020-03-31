from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, DateTimeField, HiddenField, FileField
from wtforms.validators import DataRequired

class Input_roast(FlaskForm):
    roasting_name = StringField('Cause',validators=[DataRequired()],render_kw={"class":"form-control"})
    place_name = StringField('Place',validators=[DataRequired()],render_kw={"class":"form-control"})
    lot_name = StringField('Lot',validators=[DataRequired()],render_kw={"class":"form-control"})
    start_dttm = DateTimeField('Start time',validators=[DataRequired()],render_kw={"class":"form-control"})
    end_dttm = DateTimeField('End time',validators=[DataRequired()],render_kw={"class":"form-control"})
    initial_weight = FloatField('Initial weight',validators=[DataRequired()],render_kw={"class":"form-control"})
    acidity = FloatField('Acidity',validators=[DataRequired()],render_kw={"class":"form-control"})
    roaster = StringField('Roaster name',validators=[DataRequired()],render_kw={"class":"form-control"})
    submit = SubmitField('Submit',render_kw={"class":"btn btn-light"})

class Input_File(FlaskForm):
    filename = FileField('Click to choose file',validators=[DataRequired()],render_kw={"class":"custom-file-input"})
    submit = SubmitField('Submit', render_kw={"class":"btn btn-light"})
