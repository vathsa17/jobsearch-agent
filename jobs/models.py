"""
Data models used throughout the application.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Job:
    """Represents a single job posting."""

    reference: str

    title: str

    company: str

    location: str

    profession: str = ""

    description: str = ""

    salary: str = ""

    employment_type: str = ""

    remote: bool = False

    url: Optional[str] = None

    score: Optional[int] = None

    summary: Optional[str] = None

    strengths: list[str] = field(default_factory=list)

    missing_skills: list[str] = field(default_factory=list)

    first_seen: datetime = field(default_factory=datetime.utcnow)

    last_seen: datetime = field(default_factory=datetime.utcnow)

    emailed: bool = False

    def __str__(self):

        return (
            f"{self.title} | "
            f"{self.company} | "
            f"{self.location}"
        )

    def to_dict(self):

        return {
            "reference": self.reference,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "profession": self.profession,
            "description": self.description,
            "salary": self.salary,
            "employment_type": self.employment_type,
            "remote": self.remote,
            "url": self.url,
            "score": self.score,
            "summary": self.summary,
            "strengths": self.strengths,
            "missing_skills": self.missing_skills,
            "emailed": self.emailed,
        }