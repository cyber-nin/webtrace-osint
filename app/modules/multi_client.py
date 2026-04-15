from telethon import TelegramClient
from app.config import API_ID, API_HASH

def load_clients(session_list):
    clients = []
    for session in session_list:
        client = TelegramClient(session, API_ID, API_HASH)
    client.start()
    clients.append(client)
    return clients
