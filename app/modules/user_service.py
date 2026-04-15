from app.database import cursor

def get_all_users():
    # unique users from messages table
    cursor.execute("""
    SELECT DISTINCT user_id, username
    FROM messages
    WHERE user_id IS NOT NULL
    """)
    rows = cursor.fetchall()
    users = []
    for uid, uname in rows:
        label = f"{uname} ({uid})" if uname else f"{uid}"
        users.append({
            "label": label,
            "user_id": str(uid),
            "username": uname if uname else ""
        })
    return users

