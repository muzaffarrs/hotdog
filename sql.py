import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv('DATABASE_NAME')
db_user = os.getenv('DATABASE_USER')
db_pass = os.getenv('DATABASE_PASSWORD')
db_host = os.getenv('DATABASE_HOST')
db_port = int(os.getenv('DATABASE_PORT'))


def connect_psql():
    DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}?sslmode=require"
    return psycopg2.connect(DATABASE_URL)

"""Yangi taom qo'shish"""
def add_menu(name, price):
    conn = connect_psql()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM products WHERE name = %s;", (name,))
        if cursor.fetchone():
            return "Bu nomdagi taom allaqachon mavjud!"

        cursor.execute(
            "INSERT INTO products (name, price) VALUES (%s, %s);",
            (name, price)
        )
        conn.commit()
        return "✅ Yangi taom qo‘shildi!"
    except Exception as e:
        return f"Xatolik taom qo'shishda: {e}"
    finally:
        cursor.close()
        conn.close()
