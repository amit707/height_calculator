from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:onetwo@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__= "data"
    id = db.Column(db.Integer,primary_key=True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height = height_

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/success', methods=['GET','POST', 'Options'])
def success():
    if request.method == 'POST':
        email = request.values.get("email")
        height = request.values.get("height")
        l = [email, height]
        print(l)
        return render_template("success.html")

if __name__ == '__main__':
    app.run()
