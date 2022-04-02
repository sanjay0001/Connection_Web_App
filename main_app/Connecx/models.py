from Connecx import db


class user(db.Model):
	username=db.Column(db.String(length=50),nullable=False)
	rollno=db.Column(db.String(),nullable=False,unique=True)
	dept=db.Column(db.String(length=30))
	batch=db.Column(db.Integer())
	gender=db.Column(db.String(),nullable=False)
	hostelers=db.Column(db.String(),nullable=False)
	password1=db.Column(db.String(length=50),nullable=False)
	ID=db.Column(db.Integer(),nullable=False,unique=True,primary_key=True)
	score=db.Column(db.Float(),default=0.0)
		





	


    