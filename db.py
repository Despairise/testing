import databases
import sqlalchemy
from sqlalchemy.schema import ForeignKey

DATABASE_URL = "postgresql://postgres:12131415ee@localhost:5432/ab_db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('full_name', sqlalchemy.String),
    sqlalchemy.Column('gender', sqlalchemy.String),
    sqlalchemy.Column('b_day', sqlalchemy.String),
    sqlalchemy.Column('address', sqlalchemy.String)
)
phones = sqlalchemy.Table(
    'phones',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('type', sqlalchemy.String),
    sqlalchemy.Column('number_phone', sqlalchemy.String),
    sqlalchemy.Column('owner_id', sqlalchemy.Integer, ForeignKey("users.id"))

)

mails = sqlalchemy.Table(
    'mails',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('type', sqlalchemy.String),
    sqlalchemy.Column('mail_address', sqlalchemy.String),
    sqlalchemy.Column('owner_id', sqlalchemy.Integer, ForeignKey("users.id"))
)


engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
