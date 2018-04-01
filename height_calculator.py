from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy import  func

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:onetwo@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://aqbjbwfiyjtlma:9e738585fb625276256d274cc6b59c5fd82091df7fd078e8110fa51e6638adbb@ec2-54-243-63-13.compute-1.amazonaws.com:5432/d6enf5pfd9f88v?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__= "data"
    id = db.Column(db.Integer,primary_key=True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_,height_):
        self.email_ = email_
        self.height_ = height_

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/success', methods=['GET','POST', 'Options'])
def success():
    if request.method == 'POST':
        email = request.values.get("email")
        height = request.values.get("height")
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            avg_height=db.session.query(func.avg(Data.height_)).scalar()
            avg_height=round(avg_height,1)
            count = db.session.query(Data.height_).count()
            send_email(email, height, avg_height,count)
            print (avg_height)
            return render_template("success.html")
    return render_template("index.html",
                           text="seems like we have got that email already")

if __name__ == '__main__':
    app.run()
