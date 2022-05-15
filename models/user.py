from sqlalchemy import Integer, String, Table, Column
from config.db import metadata, engine

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('phone', String(255))
)

metadata.create_all(engine)