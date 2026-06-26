from fastapi import FastAPI, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

from api.app.core.db import check_database_connection

from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Code Judge API", version="0.1.0")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/database")
def database_health_check() -> dict[str, str]:
    try:
        check_database_connection()
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unavailable",
        ) from error

    return {"status": "ok"}
