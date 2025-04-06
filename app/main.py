from fastapi import FastAPI
from app.core.database import get_db
from app.routes.events import router

app = FastAPI()

@app.on_event("startup")
def create_all_tables():
    db = get_db()
    conn = next(db)
    try:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Events (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                time TEXT NOT NULL
        );
    """)
        conn.commit()
    finally:
        conn.close()

@app.on_event("shutdown")
def drop_all_tables():
    db = get_db()
    conn = next(db)
    try:
        conn.cursor().execute("DROP TABLE IF EXISTS Events;")
        conn.commit()
    finally:
        conn.close()

app.include_router(router)

@app.get("/")
def read_root():
    return {"event_manager_api_service": "App is Running"}