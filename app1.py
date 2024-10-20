import os
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')
@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect (url_for('User',usr=user))
    else:
     return render_template('login.html')
@app.route("/<usr>")
def User(usr):
    return f"<h1>hi {usr}!</h1>"
if __name__ == '__main__' :
   app.run(debug = True)
     