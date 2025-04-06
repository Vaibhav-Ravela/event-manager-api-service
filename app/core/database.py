import psycopg2
from app.core.config import POSTGRES_USER, POSTGRES_PASS, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB

def get_db():
    
    conn = psycopg2.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASS,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        dbname=POSTGRES_DB
    )
    try:
        yield conn
    finally:
        conn.close()