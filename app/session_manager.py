from telethon import TelegramClient
from app.config import API_ID, API_HASH

def create_client(session_name):
    return TelegramClient(session_name, API_ID, API_HASH)
