import os

from flask import Flask,render_template,request,redirect,url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

app = Flask(__name__)

engine = create_engine("postgres://lkghylsqhggivp:d827f6dc5637928e95e060761de590b7d9514e9463c5241ed3d652d777a4a3a9@ec2-52-200-16-99.compute-1.amazonaws.com:5432/d6d65s4otfm5cr")
db = scoped_session(sessionmaker(bind=engine))
@app.route("/")
def index():
    return render_template("a.html")
@app.route("/insert",methods=['POST'])
def insert():
    firstname=request.form.get('firstname')
    lastname=request.form.get('lastname')
    dob=request.form.get('dob')
    gender=request.form.get('gender')
    aadharno=request.form.get('aadharno')
    address=request.form.get('address')
    db.execute("insert into aadhar (firstname,lastname,dob,gender,aadharno,address) values (:firstname,:lastname,:dob,:gender,:aadharno,:address)",{"firstname":firstname ,"lastname":lastname,"dob":dob,"gender":gender,"aadharno":aadharno,"address" : address})
    db.commit()
    return redirect(url_for('index'))
