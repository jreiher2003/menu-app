# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from models import Place, MenuItem
from menu import db, models
 
# engine = create_engine('sqlite:///menu.db')
# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)

# session = DBSession()


#Menu for UrbanBurger
restaurant1 = models.Place(name = "Beef O' Brady's")
db.session.add(restaurant1)
db.session.commit()

restaurant2 = models.Place(name = "Johnny Leverocks")
db.session.add(restaurant2)
db.session.commit()

restaurant3 = models.Place(name = "Lock and Key")
db.session.add(restaurant3)
db.session.commit()

print "3 restaurants were added"