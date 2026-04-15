import sys, os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

import streamlit as st
from app.modules.tracker import analyze_user
from app.modules.user_service import get_all_users

st.set_page_config(layout="wide")
st.title("🔥 Telegram OSINT Dashboard (Pro)")

# Load users

users = get_all_users()

if not users:
    st.warning("No users found yet. Let the listener collect some data first.")
else:
    labels = [u["label"] for u in users]


selected_label = st.selectbox("Select User", labels)

selected_user = next(u for u in users if u["label"] == selected_label)

colA, colB = st.columns([2, 1])

with colA:
    st.caption(f"Selected: {selected_user['label']}")

with colB:
    run_btn = st.button("Analyze")

if run_btn:
    # prefer user_id (more reliable)
    query = selected_user["user_id"] or selected_user["username"]

    result = analyze_user(query)

    if "error" in result:
        st.error(result["error"])
    else:
        c1, c2, c3 = st.columns(3)
        c1.metric("Messages", result["total_messages"])
        c2.metric("Links", result["links_shared"])
        c3.metric("Risk", result["risk_score"])

        st.subheader("🌐 Groups")
        st.write(result["groups"])

        st.subheader("⏱ Active Hours")
        st.bar_chart(result["active_hours"])

        st.subheader("📅 Daily Activity")
        st.bar_chart(result["daily_activity"])

