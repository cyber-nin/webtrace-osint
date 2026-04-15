import sqlite3
import os

conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "..", "osint.db"), check_same_thread=False)
cursor = conn.cursor()

# Create tables

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
msg_id INTEGER PRIMARY KEY,
user_id INTEGER,
username TEXT,
group_name TEXT,
message TEXT,
time TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
user_id INTEGER PRIMARY KEY,
username TEXT
)
""")

conn.commit()
cursor.execute("""
CREATE TABLE IF NOT EXISTS groups (
group_id INTEGER PRIMARY KEY,
group_name TEXT
)
""")
conn.commit()
