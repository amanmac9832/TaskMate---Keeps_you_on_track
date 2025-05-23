from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = 'postgresql://taskmate_database_user:T4cznTdadaAXrhg4zD6dv4FDAL9iuvv2@dpg-d0o4v03e5dus73b618e0-a.oregon-postgres.render.com/taskmate_database'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

