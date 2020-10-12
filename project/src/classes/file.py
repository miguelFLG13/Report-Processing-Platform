from dataclasses import dataclass
from typing import Literal

PDF_CONTENT_TYPE = 'application/pdf'
TXT_CONTENT_TYPE = 'text/plain'

@dataclass
class File:
    title: str
    content_type: Literal[PDF_CONTENT_TYPE, TXT_CONTENT_TYPE]
    content: str
