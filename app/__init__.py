import os
from flask import Flask, render_template, request, abort
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

STAR_USER_INFO = {
    'hobbies':{
        'hobby 1': ['logo.jpg'],
        'hobby 2': ['smallcats.png'],
        'hobby 3': ['logo.jpg'],
        'hobby 4': ['smallcats.png']
     },
    'experiences':{
        'Software Developer Intern @ RBC': ['Currently working on improving IAM processes with a security team of 10'],
        'Meta x MLH Production Engineer Fellow': ['Creating a flask website using Jinja with a portfolio', 'Learning how to use Python and Flask to create a webpage!']
    },
    'education':{
        'University of Waterloo': ['waterloo.jpg'],
        'Pierre Elliott Trudeau High School': ['peths.jpg']
    },
    'images':[
        'waterloo.jpg',
        'peths.jpg'
    ]
}

ELAINE_USER_INFO = {
    'hobbies':['Blogging','Reading Books','Playing chess'],
    'experiences': ['lorem ipsum', 'xxx', 'more description about work experiences'],
    'education':{
        'XX College': ['logo.jpg'],
        'XX University': ['smallcats.png']
    },
    'images':[
        'logo.jpg',
        'smallcats.png'
    ]
}

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
    return render_template('education.html', user = USER_INFO)

@app.route('/star_about')
def star_about():
    return render_template('star_about.html', user = STAR_USER_INFO)

@app.route('/countries')
def countries():
    return render_template('countries.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', user = STAR_USER_INFO)
