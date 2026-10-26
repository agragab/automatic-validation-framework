from pydantic import BaseModel, TypeAdapter
from typing import TypedDict

class ReadingUnit(TypedDict):
    m_id: str 
    timestamp: str
    temperature: str
    exposure: str
    focus_error: str

class Readings(BaseModel):
    Readings: list[ReadingUnit]
            
