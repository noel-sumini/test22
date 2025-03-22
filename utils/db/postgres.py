import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

load_dotenv()


def get_db_connection():
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME2"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        cursor_factory=RealDictCursor
    )
    return conn