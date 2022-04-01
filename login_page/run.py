from flask import Flask,render_template
from forms import register
app = Flask(__name__)
app.config['SECRET_KEY']='265ace69ca3210b6295e4b3f'


@app.route('/')
@app.route('/login')
def home():
	form=register()
	return render_template('login.html',form=form)

