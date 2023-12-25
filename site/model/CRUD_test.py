from sqlalchemy.orm import Session
from tables import Admin, Article
from create_tables import engine
from datetime import datetime


with Session(engine) as session:
    spongebob = Admin(
        name="spongebob",
        password="Spongebob Squarepants"
    )
    sandy = Article(
        article_head="sandy",
        article_body="Sandy Cheeks",
        article_time=datetime.now()
    )
    session.add_all([spongebob, sandy])
    session.commit()


from sqlalchemy import select

session = Session(engine)

stmt = select(Admin).where(Admin.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)

stmt1 = select(Article).where(Article.article_head.in_(["sandy"]))

for user in session.scalars(stmt1):
    print(user)
