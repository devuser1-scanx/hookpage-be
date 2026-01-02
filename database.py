import os
import psycopg2
from dotenv import load_dotenv

# Load .env only for local dev
if os.getenv("ENV") != "production":
    load_dotenv()

def _create_connection():
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT", "5432")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    dbname = os.getenv("DB_NAME")

    if not all([host, user, password, dbname]):
        raise RuntimeError("Database environment variables are not fully set")

    return psycopg2.connect(
        host=host,
        port=int(port),
        dbname=dbname,
        user=user,
        password=password,
    )

def get_db():
    db = _create_connection()
    try:
        yield db
    finally:
        db.close()
