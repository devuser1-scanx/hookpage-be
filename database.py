from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Provide a database host/IP, e.g. 35.192.117.171 or 35.192.117.171:5432")

def _create_connection():
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    db_sslmode = os.getenv("DB_SSLMODE")

    if not db_user or not db_password or not db_name:
        raise RuntimeError(
            "DATABASE_URL is set to a host/IP (no scheme). "
            "To use this mode, also set DB_USER, DB_PASSWORD, and DB_NAME."
        )

    # Default port if not specified
    host = DATABASE_URL
    port = "5432"
    
    # Extract port from DATABASE_URL if present (format: host:port)
    if ":" in DATABASE_URL and "/" not in DATABASE_URL.split(":")[1]:
        host, port = DATABASE_URL.split(":", 1)

    return psycopg2.connect(
        host=host,
        port=int(port) if port.isdigit() else 5432,
        dbname=db_name,
        user=db_user,
        password=db_password,
        # sslmode=db_sslmode or "require",
    )

def get_db():
    db = _create_connection()
    try:
        yield db
    finally:
        db.close()
