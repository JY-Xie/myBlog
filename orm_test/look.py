import sqlite3


con = sqlite3.connect("demo.db")
cur = con.cursor()
sql1 = 'select * from user_account'
cur.execute(sql1)
all_person = cur.fetchall()
print(all_person)


