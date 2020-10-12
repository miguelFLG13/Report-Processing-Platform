from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Report:
    created_at: Optional[datetime]
    patient_id: str
    document_text: str
