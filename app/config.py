import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

GROUPS = ["me"]
# GROUPS = [
# "crypto_signals",
# "hacking_zone"
# ]

KEYWORDS = ["hack", "crypto", "fraud"]
TARGET_USER = "target_username"
