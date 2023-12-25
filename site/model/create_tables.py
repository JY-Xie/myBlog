from sqlalchemy import create_engine
from tables import Base

engine = create_engine("sqlite:///database.db", echo=True)

Base.metadata.create_all(engine)
