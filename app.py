# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:41:17 2021

@author: Aditi Devgan
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
#    return "Hello World!"

if __name__ == "__main__":
    app.run()