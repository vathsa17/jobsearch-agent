"""
Main application orchestrator.
"""

from database.db import Database
from jobs.filter import is_relevant
from jobs.jobsuche import JobsucheClient
from config import SEARCH_TERMS
from utils.logger import setup_logger


class JobAgent:

    def __init__(self):

        self.logger = setup_logger()

        self.db = Database()

        self.client = JobsucheClient()

    # -------------------------------------------------------

    def run(self):

        jobs = self.search_jobs()

        jobs = self.filter_jobs(jobs)

        new_jobs = self.db.get_new_jobs(jobs)

        self.logger.info(
            "Found %d new jobs",
            len(new_jobs)
        )

        self.save_jobs(new_jobs)

        self.print_summary(new_jobs)

    # -------------------------------------------------------

    def search_jobs(self):

        self.logger.info("Searching Jobsuche...")

        jobs = self.client.search_multiple(
            SEARCH_TERMS
        )

        self.logger.info(
            "Retrieved %d jobs",
            len(jobs)
        )

        return jobs

    # -------------------------------------------------------

    def filter_jobs(self, jobs):

        filtered = [
            job
            for job in jobs
            if is_relevant(job)
        ]

        self.logger.info(
            "Filtered to %d relevant jobs",
            len(filtered)
        )

        return filtered

    # -------------------------------------------------------

    def save_jobs(self, jobs):

        self.db.insert_jobs(jobs)

        self.logger.info(
            "Saved %d jobs",
            len(jobs)
        )

    # -------------------------------------------------------

    def print_summary(self, jobs):

        self.logger.info("")

        self.logger.info("=" * 60)

        for job in jobs:

            self.logger.info(
                "%s | %s | %s",
                job.company,
                job.title,
                job.location,
            )

        self.logger.info("=" * 60)

        self.logger.info(
            "Total relevant jobs: %d",
            len(jobs),
        )