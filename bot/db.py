import os
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    return psycopg2.connect(
        DATABASE_URL,
        cursor_factory=RealDictCursor
    )


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT UNIQUE NOT NULL,
        username TEXT,
        first_name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS wallets (
        user_id INTEGER PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
        balance NUMERIC(18,2) DEFAULT 0
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS player_accounts (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
        player_username TEXT UNIQUE,
        player_password TEXT,
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id SERIAL PRIMARY KEY,
        trx_id TEXT UNIQUE,
        user_id INTEGER REFERENCES users(id),
        type TEXT,
        amount NUMERIC(18,2),
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS deposits (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        amount NUMERIC(18,2),
        payment_method TEXT,
        receipt_file TEXT,
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS withdrawals (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        amount NUMERIC(18,2),
        payment_method TEXT,
        wallet_address TEXT,
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS payment_methods (
        id SERIAL PRIMARY KEY,
        name TEXT,
        details TEXT,
        min_amount NUMERIC(18,2),
        max_amount NUMERIC(18,2),
        fee_percent NUMERIC(10,2) DEFAULT 0
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS notifications (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        message TEXT,
        is_read BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    cur.close()
    conn.close()


def create_user(telegram_id, username, first_name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO users
        (telegram_id, username, first_name)
        VALUES (%s, %s, %s)
        ON CONFLICT (telegram_id)
        DO NOTHING
    """, (telegram_id, username, first_name))

    conn.commit()

    cur.execute("""
        SELECT id
        FROM users
        WHERE telegram_id = %s
    """, (telegram_id,))

    user = cur.fetchone()

    cur.execute("""
        INSERT INTO wallets (user_id, balance)
        VALUES (%s, 0)
        ON CONFLICT DO NOTHING
    """, (user["id"],))

    conn.commit()

    cur.close()
    conn.close()


def get_user(telegram_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM users
        WHERE telegram_id = %s
    """, (telegram_id,))

    user = cur.fetchone()

    cur.close()
    conn.close()

    return user


def get_wallet_balance(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT balance
        FROM wallets
        WHERE user_id = %s
    """, (user_id,))

    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        return float(result["balance"])

    return 0
