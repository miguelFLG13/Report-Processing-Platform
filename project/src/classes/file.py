from dataclasses import dataclass


@dataclass
class File:
    title: str
    content_type: str
    content: str

