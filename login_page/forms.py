from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

class register(FlaskForm):
	roll_no=StringField(label='Rollno')
	password1=StringField(label='Password')
	login=SubmitField(label='Login')
	
