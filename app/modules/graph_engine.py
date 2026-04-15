import networkx as nx
from app.database import cursor

def build_user_group_graph():
    G = nx.Graph()
    cursor.execute("SELECT user_id, username, group_name FROM messages")
    rows = cursor.fetchall()

    for uid, uname, group in rows:
        user_label = uname if uname else str(uid)

        if user_label and group:
            G.add_node(user_label, type="user")
            G.add_node(group, type="group")

            G.add_edge(user_label, group)

    return G

