from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired

class FileForm(FlaskForm):
    file = FileField("Select Document here:", validators=[FileRequired()])
    submit = SubmitField("Upload")

class TextForm(FlaskForm):
    text = TextAreaField("Enter your question here:", validators=[DataRequired()])
    submit = SubmitField("Send")