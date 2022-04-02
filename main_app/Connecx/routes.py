from Connecx import app
from flask import render_template,redirect,url_for,flash,request

from Connecx.forms import register,User_register
from Connecx import db
from Connecx.models import user



@app.route('/login',methods=['GET','POST'])
def home():
	form=register()
	if(request.method=='POST'):
		r_n=form.roll_no.data
		pwrd=form.password1.data
		for i in user.query.all():
			if(r_n==i.rollno):
				if(pwrd==i.password1):
					return redirect(url_for('front_page'))
				else:
					pass
			else:
				pass


			

	return render_template('login.html',form=form)

@app.route('/signup')
def signup_user():

	return render_template('selection.html')

@app.route('/student',methods=['GET','POST'])
def student_signup():
	form=User_register()	
	if form.validate_on_submit():
		dept_select=request.form.get('Department')
		gender_type=request.form.get('gender')
		hstl=request.form.get('place')
		user_create=user(username=form.username.data,rollno=form.rollno.data,dept=dept_select,
			batch=form.batch.data,gender=gender_type,hostelers=hstl,password1=form.password1.data)
		db.session.add(user_create)
		db.session.commit()
		return redirect(url_for('home'))

	return render_template('student_signup.html',form=form)


@app.route('/faculty',methods=['GET','POST'])
def faculty_signup():
	form=User_register()
	if form.validate_on_submit():
		
		gender_type=request.form.get('gender')
		hstl=request.form.get('place')
		user_create=user(username=form.username.data,rollno=form.rollno.data,dept='',
			batch='',gender=gender_type,hostelers=hstl,password1=form.password1.data)
		db.session.add(user_create)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('faculty_signup.html',form=form)


@app.route('/Home')
def front_page():
	return render_template('front_page.html')
