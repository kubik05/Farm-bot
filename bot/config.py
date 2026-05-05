import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_IDS = [int(x) for x in os.environ.get("ADMIN_IDS", "").split(",") if x]
DB_PATH = os.environ.get("DB_PATH", "db.sqlite")
FARMGEN_BASE = "https://image.pollinations.ai/prompt/"
