from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
menuItem = Table('menuItem', post_meta,
    Column('name', String(length=80), nullable=False),
    Column('id', Integer, primary_key=True, nullable=False),
    Column('course', String(length=250)),
    Column('description', String(length=250)),
    Column('price', String(length=8)),
    Column('place_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['menuItem'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['menuItem'].drop()
