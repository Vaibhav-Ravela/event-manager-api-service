from os import getenv
from dotenv import load_dotenv

try:
    load_dotenv("../.env")
except:
    raise Exception

POSTGRES_USER = getenv("POSTGRES_USER", "admin")
POSTGRES_PASS = getenv("POSTGRES_PASSWORD", "admin@123")
POSTGRES_HOST = getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = getenv("POSTGRES_DB", "event_db")