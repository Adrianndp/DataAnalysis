import datetime
from sqlalchemy import create_engine, Column, Integer, DATETIME, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', convert_unicode=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.datetime.utcnow)
    username = Column(String, unique=True, nullable=False)
    language = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def __init__(self, created_at=None, username=None, language=None, age=None):
        self.created_at = created_at
        self.username = username
        self.language = language
        self.age = age


tables_dict = {table.__tablename__: table for table in db.Model.__subclasses__()}


def get_table_object(table_name):
    return tables_dict.get(table_name)


def init_db():
    # Base.metadata.drop_all(engine)  # "DROP TABLES IF EXISTS "
    Base.metadata.create_all(bind=engine)  # CREATE TABLE


# Creates a new session to the database by using the engine we described.
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base.query = db_session.query_property()
