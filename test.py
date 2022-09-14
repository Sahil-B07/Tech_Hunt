import sqlite3

queries = []
with open('questions.csv', 'r') as f:
    data = f.read()

data = data.split('\n')
for i in data:
    d = i.strip().split(",")
    queries.append(f"INSERT INTO hunt_question VALUES ({d[0].strip()}, '{d[1].strip()}', '{d[2].strip()}', '{d[3].strip()}')")

connection = sqlite3.connect('db.sqlite3')
cur = connection.cursor()
cur.execute('DELETE FROM hunt_question')
for i in queries:
    cur.execute(i)

data = cur.execute("SELECT * from hunt_question").fetchall()

for row in data:
    print(row)


connection.commit()