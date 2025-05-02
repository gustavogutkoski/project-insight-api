from pydantic import BaseModel
from datetime import datetime

class JavaFileRead(BaseModel):
    id: int
    filename: str
    content_type: str
    upload_date: datetime
    size_bytes: float
    content_hash: str
