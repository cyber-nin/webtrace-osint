from app.config import TARGET_USER
from app.logger import logger

def check(data):
 if data["username"] == TARGET_USER:
    logger.warning(f"🚨 Target active in {data['group']}")
