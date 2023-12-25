from sqlalchemy import create_engine
from DC import Base

engine = create_engine("sqlite:///demo.db", echo=True)

Base.metadata.create_all(engine)