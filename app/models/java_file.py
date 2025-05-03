from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class JavaFile:
    id: int
    file_name: str
    content_type: str
    upload_date: datetime
    file_data: bytes
    size_bytes: float
    content_hash: str
    uuid: UUID = field(default_factory=uuid4)
