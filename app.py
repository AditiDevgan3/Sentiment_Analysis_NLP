# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:41:17 2021

@author: Aditi Devgan
"""

from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/sentiment', methods = ['GET','POST'])
def sentiment():
    userid = request.form.get('userid')
    hashtag = request.form.get('hashtag')

    if userid == "" and hashtag == "":
        error = "Please Enter any one value"
        return render_template('index.html', error=error)
    
    elif userid == "" or hashtag == "":
        error = "Both entry not allowed"
        return render_template('index.html', error=error)
    
    else:
        return render_template('sentiment.html')
    


if __name__ == "__main__":
    app.run()