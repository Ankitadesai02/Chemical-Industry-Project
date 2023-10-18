# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 03:43:25 2023

@author: Work
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my website"

app.run()