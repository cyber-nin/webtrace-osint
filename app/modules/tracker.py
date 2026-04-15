from app.database import cursor
from collections import Counter
import re

def analyze_user(query):
    # query can be username OR user_id (string)
    cursor.execute("""
    SELECT * FROM messages
    WHERE username=? OR user_id=?
    """, (query, query))
    data = cursor.fetchall()


    if not data:
        return {"error": "No data found"}

    total_msgs = len(data)
    groups = list(set([d[3] for d in data]))

    hours = [int(d[5][11:13]) for d in data]
    hour_dist = dict(Counter(hours))

    dates = [d[5][:10] for d in data]
    date_dist = dict(Counter(dates))

    links = []
    for d in data:
        links.extend(re.findall(r'https?://\S+', d[4]))

    keywords = ["hack", "fraud", "carding", "crypto"]
    keyword_hits = sum(1 for d in data if any(k in d[4].lower() for k in keywords))

    risk_score = min(100, keyword_hits * 10 + len(links) * 2)

    return {
        "total_messages": total_msgs,
        "groups": groups,
        "active_hours": hour_dist,
        "daily_activity": date_dist,
        "links_shared": len(links),
        "keyword_hits": keyword_hits,
        "risk_score": risk_score
    }

