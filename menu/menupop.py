from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Place
 
engine = create_engine('sqlite:///menu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

#Menu for UrbanBurger
restaurant1 = Place(name = "Beef O' Brady's")
session.add(restaurant1)
session.commit()

restaurant2 = Place(name = "Johnny Leverocks")
session.add(restaurant2)
session.commit()

restaurant3 = Place(name = "Lock and Key")
session.add(restaurant3)
session.commit()

print "3 restaurants were added"