from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from tables import Admin
engine = create_engine("sqlite:///database.db", echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
to_add = Admin(
    name="xiejiye",
    password="scrypt:32768:8:1$rEdIagz3X1S8MPVO$94defbc99fc3aeddecd06125b3cbab25d6ca4054685e8e4a4f47ac037ac70e3c809e0c544209635d2a0249b27a2ab54d3c70724bcffe079696d069bf8ff36aad"
)
db_session.add(to_add)
db_session.commit()
db_session.close()
