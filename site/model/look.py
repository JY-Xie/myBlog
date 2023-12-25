import sqlite3


con = sqlite3.connect("database.db")
cur = con.cursor()
sql1 = 'select * from article'
cur.execute(sql1)
all_person = cur.fetchall()
print(all_person)


