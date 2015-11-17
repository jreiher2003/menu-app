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
    # return render_template('base.html')
    return 'Hello Jeffrey'
    # place = session.query(Place).all()
    # for p in place:
    # 	output += p.name
    # 	output += '<br>'
    # return output
