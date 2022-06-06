import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

STAR_USER_INFO = {
    'hobbies':['Blogging','Reading Books','Playing chess'],
    'experiences':{
        'Job 1': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit,' 
                + 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', 
                'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi' 
                + ' ut aliquip ex ea commodo consequat.'],
        'Job 2': ['did this', 'did that']
    },
    'education':{
        'XX College': ['logo.jpg'],
        'XX University': ['smallcats.png']
    },
    'images':[
        'logo.jpg',
        'smallcats.png'
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
