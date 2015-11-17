# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine


# Base = declarative_base()
from menu import db
#### class code #######
class Place(db.Model):
    __tablename__ = 'place' # names table
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Place %r>' % (self.name)


class MenuItem(db.Model):
	__tablename__ = 'menuItem'
	name = db.Column(db.String(80), nullable=False)
	id = db.Column(db.Integer, primary_key=True)
	course = db.Column(db.String(250))
	description = db.Column(db.String(250))
	price = db.Column(db.String(8))
	place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
	place = db.relationship(Place)

	def __repr__(self):
		return '<MenuItem %r>' % (self.name)


########## insert at end of file ########
# engine = create_engine('sqlite:///menu.db')
# Base.metadata.create_all(engine)