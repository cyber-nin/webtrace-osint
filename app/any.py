import sqlite3

conn = sqlite3.connect("osint.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM messages LIMIT 5")
print(cursor.fetchall())
cursor.execute("SELECT * FROM messages")
print(cursor.fetchall())