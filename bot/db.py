import aiosqlite

DB_FILE = "db.sqlite"

CREATE_USERS = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    balance INTEGER DEFAULT 100,
    farm_img_url TEXT
);
"""

async def init_db():
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute(CREATE_USERS)
        await db.commit()

async def get_user(user_id):
    async with aiosqlite.connect(DB_FILE) as db:
        cur = await db.execute("SELECT user_id, username, balance, farm_img_url FROM users WHERE user_id=?", (user_id,))
        return await cur.fetchone()

async def create_user(user_id, username, farm_img_url):
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, username, balance, farm_img_url) VALUES (?, ?, ?, ?)",
            (user_id, username, 100, farm_img_url)
        )
        await db.commit()

async def update_balance(user_id, amount):
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
        await db.commit()

async def update_farm_img(user_id, url):
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute("UPDATE users SET farm_img_url = ? WHERE user_id = ?", (url, user_id))
        await db.commit()
