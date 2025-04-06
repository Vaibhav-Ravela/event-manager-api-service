from pydantic import BaseModel

class EventRequest(BaseModel):
    title: str
    time: int

class EventResponse(EventRequest):
    id: int