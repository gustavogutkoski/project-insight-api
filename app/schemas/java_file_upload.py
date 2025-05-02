from pydantic import BaseModel
from datetime import datetime

class JavaFileUpload(BaseModel):
    filename: str
    content_type: str
    upload_date: datetime
    file_data: bytes
    size_bytes: float
    content_hash: str
