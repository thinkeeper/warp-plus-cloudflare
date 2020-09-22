import os

class Config:
    CLIENT_ID = os.environ.get("CLIENT_ID")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    LOG_CHAT_ID = os.environ.get("LOG_CHAT_ID")
    MESSAGE_ID = os.environ.get("LOG_CHAT_ID")