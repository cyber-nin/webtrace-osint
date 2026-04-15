from app.database import cursor, conn

def process(data):
    cursor.execute("""
    INSERT OR REPLACE INTO messages
    (msg_id, user_id, username, group_name, message, time)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
    data["msg_id"],
    data["user_id"],
    data["username"],
    data["group"],
    data["message"],
    data["time"]
    ))

   
    # Save group
    cursor.execute("""
    INSERT OR IGNORE INTO groups (group_name)
    VALUES (?)
    """, (data["group"],))

    conn.commit()
    
