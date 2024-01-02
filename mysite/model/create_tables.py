from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


if __name__ == '__main__':
    from tables import Base
    engine = create_engine("sqlite:///database.db", echo=True)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.metadata.create_all(engine)
