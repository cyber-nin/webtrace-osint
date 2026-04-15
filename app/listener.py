from telethon import events
from app.session_manager import create_client
from app.processor import process
from app.alerts import check
from app.logger import logger

def run_listener():
    client = create_client("main_session")

    @client.on(events.NewMessage)
    async def handler(event):
        try:
            sender = await event.get_sender()

            print("🔥 EVENT RECEIVED:", event.raw_text)

            data = {
                "msg_id": event.id,
                "user_id": sender.id if sender else None,
                "username": (sender.username if sender and sender.username else str(sender.id)) if sender else "unknown",
                "group": event.chat.title if event.chat and hasattr(event.chat, "title") else "private",
                "message": event.raw_text,
                "time": str(event.date)
            }

            process(data)
            check(data)

            logger.info(f"{data['username']} → {data['group']}")

        except Exception as e:
            logger.error(f"Error: {e}")

    logger.info("🚀 Listener started... Waiting for messages...")

    client.start()
    client.run_until_disconnected()
# from telethon import events
# from app.session_manager import create_client
# from app.processor import process
# from app.alerts import check
# from app.logger import logger

def run_listener():
    client = create_client("main_session")


    @client.on(events.NewMessage)
    async def handler(event):
        try:
            if event.is_private:
                return  # ❌ ignore private chats

            sender = await event.get_sender()
            chat = await event.get_chat()

            print("🔥 GROUP EVENT:", event.raw_text)

            data = {
                "msg_id": event.id,
                "user_id": sender.id if sender else None,
                "username": sender.username or str(sender.id) if sender else "unknown",
                "group": chat.title if hasattr(chat, "title") else "unknown",
                "message": event.raw_text,
                "time": str(event.date)
            }

            process(data)
            check(data)

            logger.info(f"{data['username']} → {data['group']}")

        except Exception as e:
            logger.error(f"Error: {e}")

    logger.info("🚀 Group Listener Active...")
    client.start()
    client.run_until_disconnected()

