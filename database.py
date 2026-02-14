import sqlite3

def connect():
    return sqlite3.connect("database.db")

def setup():
    conn = connect()
    c = conn.cursor()

    # Config serveur
    c.execute("""
    CREATE TABLE IF NOT EXISTS guild_config (
        guild_id INTEGER PRIMARY KEY,
        counting_enabled INTEGER DEFAULT 0,
        counting_channel INTEGER,
        tickets_enabled INTEGER DEFAULT 0,
        events_enabled INTEGER DEFAULT 0,
        giveaways_enabled INTEGER DEFAULT 0
    )
    """)

    # Giveaways
    c.execute("""
    CREATE TABLE IF NOT EXISTS giveaways (
        message_id INTEGER PRIMARY KEY,
        guild_id INTEGER,
        channel_id INTEGER,
        prize TEXT
    )
    """)

    conn.commit()
    conn.close()
