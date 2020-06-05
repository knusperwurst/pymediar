from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)


def get_session():
    return Session()


def create_db():
    Base.metadata.create_all(engine)


