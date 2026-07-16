"""
Prompt templates for the AI job matcher.
"""

from jobs.models import Job


SYSTEM_PROMPT = """
You are an experienced technical recruiter with over 15 years of experience
hiring software engineers.

Your task is to compare a candidate's CV against a job description.

Evaluate:

- Technical skills
- Years of experience
- Domain knowledge
- Industry experience
- Soft skills
- Language requirements
- Overall suitability

Return ONLY valid JSON.

Do NOT wrap the JSON inside markdown.

Do NOT explain your answer.

Do NOT include any additional text.
"""


def build_prompt(job: Job, cv: str) -> str:
    """
    Build the user prompt for the LLM.
    """

    return f"""
Candidate CV
============

{cv}


Job Information
===============

Title:
{job.title}

Company:
{job.company}

Location:
{job.location}

Profession:
{job.profession}

Description:
{job.description}

Requirements:
{job.requirements}

Benefits:
{job.benefits}

Remote:
{"Yes" if job.remote else "No"}

Salary:
{job.salary}


Instructions
============

Compare the candidate's CV with this job.

Give an objective evaluation.

Return ONLY this JSON.

{{
    "score": 0,
    "recommendation": "Apply | Maybe | Skip",
    "summary": "",
    "strengths": [],
    "missing_skills": [],
    "suggested_cv_changes": [],
    "estimated_interview_difficulty": "",
    "preparation_topics": [],
    "estimated_preparation_hours": 0
}}
"""