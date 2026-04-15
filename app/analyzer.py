from app.database import cursor
from collections import Counter

def get_user_stats(username):
    cursor.execute("SELECT * FROM messages WHERE username=?", (username,))
    data = cursor.fetchall()

    total = len(data)
    groups = list(set([d[3] for d in data]))
    hours = [int(d[5][11:13]) for d in data]

    return {
        "total_messages": total,
        "groups": groups,
        "active_hours": dict(Counter(hours))
    }
