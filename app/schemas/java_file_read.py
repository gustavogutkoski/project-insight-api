from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class JavaFileRead(BaseModel):
    uuid: UUID
    filename: str
    content_type: str
    upload_date: datetime
    size_bytes: float
    content_hash: str
