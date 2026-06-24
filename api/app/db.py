import os

from sqlalchemy import create_engine, text


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://code_judge:code_judge@localhost:5432/code_judge",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def check_database_connection() -> None:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
