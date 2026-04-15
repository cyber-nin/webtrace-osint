def extract_group_info(event):
    try:
        chat = event.chat
        return {
            "id": chat.id,
            "title": getattr(chat, "title", "unknown")
        }
    except:
        return None
    