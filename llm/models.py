"""
Models used by the LLM layer.
"""

from dataclasses import dataclass, field
from enum import Enum


class Recommendation(Enum):
    APPLY = "APPLY"
    MAYBE = "MAYBE"
    SKIP = "SKIP"



@dataclass
class JobMatch:
    """
    Result returned by the AI after comparing a CV
    against a job description.
    """

    score: int

    recommendation: str

    summary: str

    strengths: list[str] = field(default_factory=list)

    missing_skills: list[str] = field(default_factory=list)

    suggested_cv_changes: list[str] = field(default_factory=list)

    estimated_interview_difficulty: str = ""

    preparation_topics: list[str] = field(default_factory=list)

    estimated_preparation_hours: int = 0