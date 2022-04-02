from flask_wtf import FlaskForm
from Connecx.models import user
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import length,EqualTo,DataRequired


class register(FlaskForm):
	roll_no=StringField(label='Roll.no')
	password1=PasswordField(label='Password')
	login=SubmitField(label='Login')
	
class User_register(FlaskForm):
	username=StringField(label="Username")
	password1=PasswordField(label="Password")
	password2=PasswordField(label="Confirm Password")
	rollno=StringField(label="Roll.No")
	dept=StringField(label="Department")
	gender=StringField(label="Gender")
	hosteler=StringField(label="Mode of Access")
	batch=StringField(label="Batch(Year of Finishing)")
	submit=SubmitField(label="Submit")
