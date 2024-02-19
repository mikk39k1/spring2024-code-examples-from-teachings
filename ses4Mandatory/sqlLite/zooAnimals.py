import sqlite3
con = sqlite3.connect("Zoo.db")

cur = con.cursor()

cur.execute("CREATE TABLE animal(name)")

cur.execute("INSERT INTO animal VALUES ('Tiger'), ('Giraffe'), ('Monkey')")

con.commit()

res = cur.execute("SELECT * FROM animal")

for name in res:
    print(f"Name: {name[0]}")


