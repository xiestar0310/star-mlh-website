import os
from flask import Flask, render_template, request, abort
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')
 
@app.route('/education')
def education():
    user_info = {
        'hobbies':['Blogging','Reading Books','Playing chess'],
        'education':{
            'XX College',
            'XX University'
        }
    }
    return render_template('education.html', user = user_info)
