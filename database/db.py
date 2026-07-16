"""
SQLite database helper.
"""

import sqlite3

from config import DATABASE_FILE
from jobs.models import Job
import json

class Database:

    def __init__(self):

        self.connection = sqlite3.connect(DATABASE_FILE)

        self.connection.row_factory = sqlite3.Row

        self.create_tables()

    # -------------------------------------------------

    def create_tables(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS job_matches (

                reference TEXT PRIMARY KEY,

                score INTEGER,

                recommendation TEXT,

                summary TEXT,

                strengths TEXT,

                missing_skills TEXT,

                suggested_cv_changes TEXT,

                interview_difficulty TEXT,

                preparation_topics TEXT,

                preparation_hours INTEGER,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY(reference)
                    REFERENCES jobs(reference)

            )
            """)

        self.connection.commit()

    # -------------------------------------------------

    def insert_job(self, job: Job) -> bool:

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT OR IGNORE INTO jobs
            (
                reference,
                title,
                company,
                location,
                profession,
                salary,
                remote,
                url
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                job.reference,
                job.title,
                job.company,
                job.location,
                job.profession,
                job.salary,
                int(job.remote),
                job.url,
            )
        )

        self.connection.commit()

        return cursor.rowcount == 1

    # -------------------------------------------------

    def get_all_jobs(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM jobs
            ORDER BY company
            """
        )

        return cursor.fetchall()

    # -------------------------------------------------

    def job_exists(self, reference):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM jobs
            WHERE reference = ?
            """,
            (reference,)
        )

        return cursor.fetchone() is not None

    # -------------------------------------------------

    def close(self):

        self.connection.close()
    # -------------------------------------------------

    def get_new_jobs(self, jobs: list[Job]) -> list[Job]:

        """
        Returns only jobs that do not already exist in the database.
        """

        new_jobs = []

        for job in jobs:

            if not self.job_exists(job.reference):
                new_jobs.append(job)

        return new_jobs
    # -------------------------------------------------

    def insert_jobs(self, jobs: list[Job]):

        cursor = self.connection.cursor()

        rows = []

        for job in jobs:

            rows.append(
                (
                    job.reference,
                    job.title,
                    job.company,
                    job.location,
                    job.profession,
                    job.salary,
                    int(job.remote),
                    job.url,
                )
            )

        cursor.executemany(
            """
            INSERT OR IGNORE INTO jobs
            (
                reference,
                title,
                company,
                location,
                profession,
                salary,
                remote,
                url
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
        )

        self.connection.commit()
    def save_match(self, reference: str, match):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO job_matches
            (
                reference,
                score,
                recommendation,
                summary,
                strengths,
                missing_skills,
                suggested_cv_changes,
                interview_difficulty,
                preparation_topics,
                preparation_hours
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                reference,
                match.score,
                match.recommendation.value,
                match.summary,
                json.dumps(match.strengths),
                json.dumps(match.missing_skills),
                json.dumps(match.suggested_cv_changes),
                match.estimated_interview_difficulty,
                json.dumps(match.preparation_topics),
                match.estimated_preparation_hours,
            )
        )

        self.connection.commit()