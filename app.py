from flask import Flask,render_template,request

app = flask(__name__)

@app.route("/",methods=["GET","POST"])