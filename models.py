from pydantic import BaseModel, TypeAdapter
from typing_extensions import TypedDict, List

class jsonnaya(TypedDict):
    m_id: str 
    timestamp: str
    temperature: str
    exposure: str
    focus_error: str

class jsonnat(BaseModel):
    listaya: list[jsonnaya]
