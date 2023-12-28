import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from .tables import Base


if __name__ == '__main__':
    from tables import Base
    engine = create_engine("sqlite:///mysite/model/database.db", echo=True)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.metadata.create_all(engine)
