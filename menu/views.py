from flask import render_template
from menu import app


# from sqlachemy import create_engine 
# from sqlalchemy.orm import sessionmaker
# from models import Base, Place

# engine = create_engine('sqlite:///menu.db')
# Base.metadata.bind = engine 


@app.route('/')
@app.route('/hello')
def index():
    user = {'nickname': 'Jeffaroni'}  
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template('base.html', title="Jeff's boom boom room",
    									user=user,
    									posts=posts)
