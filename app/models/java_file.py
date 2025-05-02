from dataclasses import dataclass
from datetime import datetime


@dataclass
class JavaFile:
    id: int
    file_name: str
    content_type: str
    upload_date: datetime
    file_data: bytes
    size_bytes: float
    content_hash: str