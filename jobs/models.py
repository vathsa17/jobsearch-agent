"""
Data models used throughout the application.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Job:

    reference: str

    title: str

    company: str

    location: str

    profession: str = ""

    description: str = ""

    requirements: str = ""

    benefits: str = ""

    salary: str = ""

    employment_type: str = ""

    remote: bool = False

    source: str = "Jobsuche"

    url: Optional[str] = None

    posted_date: Optional[datetime] = None

    first_seen: datetime = field(default_factory=datetime.utcnow)

    last_seen: datetime = field(default_factory=datetime.utcnow)

    status: str = "NEW"