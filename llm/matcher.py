"""
Matches a Job against a candidate CV using an LLM.
"""

from llm.client import LLMClient
from llm.prompts import (
    SYSTEM_PROMPT,
    build_prompt,
)

from llm.models import (
    JobMatch,
    Recommendation,
)

from jobs.models import Job

from utils.logger import setup_logger

logger = setup_logger()


class JobMatcher:

    def __init__(self):

        self.client = LLMClient()

    # ----------------------------------------------------------

    def match(
        self,
        job: Job,
        cv: str,
    ) -> JobMatch:

        logger.info(
            "Matching job: %s",
            job.title,
        )

        prompt = build_prompt(job, cv)

        response = self.client.ask_json(
            SYSTEM_PROMPT,
            prompt,
        )

        match = JobMatch(

            score=response["score"],

            recommendation=Recommendation(
                response["recommendation"]
            ),

            summary=response["summary"],

            strengths=response.get(
                "strengths",
                [],
            ),

            missing_skills=response.get(
                "missing_skills",
                [],
            ),

            suggested_cv_changes=response.get(
                "suggested_cv_changes",
                [],
            ),

            estimated_interview_difficulty=response.get(
                "estimated_interview_difficulty",
                "",
            ),

            preparation_topics=response.get(
                "preparation_topics",
                [],
            ),

            estimated_preparation_hours=response.get(
                "estimated_preparation_hours",
                0,
            ),
        )

        logger.info(
            "Match score: %d",
            match.score,
        )

        return match