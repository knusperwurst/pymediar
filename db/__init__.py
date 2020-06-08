from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///sqlite.db", echo=True)
Base = declarative_base()


def get_session():
    session = sessionmaker(bind=engine)
    return session()


def create_db():
    Base.metadata.create_all(engine)


