import os
import databases
import sqlalchemy
from sqlalchemy.schema import ForeignKey

DATABASE_URL = os.environ.get('DATABASE_URL')
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('full_name', sqlalchemy.String),
    sqlalchemy.Column('gender', sqlalchemy.String),
    sqlalchemy.Column('b_day', sqlalchemy.Date),
    sqlalchemy.Column('address', sqlalchemy.String)
)

phones = sqlalchemy.Table(
    'phones',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('phone_type', sqlalchemy.String),
    sqlalchemy.Column('number_phone', sqlalchemy.String),
    sqlalchemy.Column('owner_id', sqlalchemy.Integer, ForeignKey("users.id", ondelete="CASCADE"))
)

mails = sqlalchemy.Table(
    'mails',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('mail_type', sqlalchemy.String),
    sqlalchemy.Column('mail_address', sqlalchemy.String),
    sqlalchemy.Column('owner_id', sqlalchemy.Integer, ForeignKey("users.id", ondelete="CASCADE"))
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
