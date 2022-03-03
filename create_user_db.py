from sqlalchemy import Column, String, Boolean, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    username = Column(String(20), primary_key=True)
    password = Column(String(40), nullable=False)
    v1 = Column(Boolean, nullable=False)
    v2 = Column(Boolean, nullable=False)


def create_user_db():

    engine = create_engine('sqlite:///data.db', echo=True)

    if not inspect(engine).has_table('users'):

        Base.metadata.create_all(engine)

        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        session = db_session()

        users = pd.read_csv('/Users/donor/PycharmProjects/Sentiment_Analysis_API/credentials.csv')

        for i in range(len(users)):

            username = users.loc[i, 'username']
            password = str(users.loc[i, 'password'])
            v1 = users.loc[i, 'v1']
            v2 = users.loc[i, 'v2']

            session.add(User(username=username, password=password, v1=v1, v2=v2))
            session.commit()

