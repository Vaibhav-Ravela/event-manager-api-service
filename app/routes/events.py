from fastapi import APIRouter, Depends, HTTPException
from app.schemas.events import EventRequest, EventResponse
from fastapi.security import OAuth2PasswordBearer
from app.core.database import get_db
from psycopg2.extensions import connection

# oauth2_token = OAuth2PasswordBearer(tokenUrl="auth/login")

router = APIRouter(prefix="/events", tags=["events"])

@router.get(path="/", response_model=list[EventResponse])
def get_all_events(db: connection=Depends(get_db)):
    cur = db.cursor()
    cur.execute("SELECT * FROM Events")
    rows = cur.fetchall()
    res = list()
    print(rows)
    for row in rows:
        res.append(
            EventResponse(id=row[0], time=row[2], title=row[1])
        )
    return res

@router.post(path="/", response_model=EventResponse)
def add_event(new_event: EventRequest, db: connection=Depends(get_db)):
    try:
        cur = db.cursor()
        cur.execute("INSERT INTO Events (title, time) VALUES (%s, %s) RETURNING id, title, time;", (new_event.title, new_event.time))
        event = cur.fetchone()
        db.commit()
        return EventResponse(id=event[0], title=event[1], time=event[2])
    except:
        raise HTTPException(status_code=500, detail="server exception")