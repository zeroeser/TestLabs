from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, Table
from sqlalchemy.orm import  sessionmaker
from sqlalchemy_utils import database_exists, create_database
from config import URL

engine = create_engine(URL)

if not database_exists(engine.url):
    create_database(engine.url)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()


users = Table('users',
    metadata,
    Column('id', Integer, primary_key=True, unique=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('patronymic', String, nullable=True),
    Column('surname', String, nullable=False),
    Column('email', String, unique=True),
    Column('password', String),
    Column('when', DateTime),
    Column('update', DateTime))


metadata.create_all(engine)


