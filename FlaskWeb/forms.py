from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length

class PostForm(FlaskForm):
    name = StringField(label="name", validators=[Length(min=8, max=120), DataRequired()])
    title = StringField(lable="title", validators=[Length(min=20, max=2000), DataRequired()])
    detail = StringField(label="detail", validators=[Length(min=20, max=2000), DataRequired()])
    submit = SubmitField(label="Post")





class MessageForm(FlaskForm):
    name = StringField(label="name", validators=[Length(max=120, min=8), DataRequired()])
    email = StringField(label="email", validators=[Length(min=25, max=200), DataRequired()])
    phone = IntegerField(label="phone", validators=[Length(min=10, max=15), DataRequired()])
    message = StringField(label="message", validators=[Length(min=10, max=2000), DataRequired()])
    submit = SubmitField(label="Send")
