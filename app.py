"""
AI Job Agent

Entry point for the application.
"""

from jobs.jobsuche import JobsucheClient
from config import SEARCH_TERMS


def print_job(job):

    print("-" * 70)

    print(f"Title      : {job.title}")
    print(f"Company    : {job.company}")
    print(f"Location   : {job.location}")
    print(f"Profession : {job.profession}")

    if job.salary:
        print(f"Salary     : {job.salary}")

    print(f"Remote     : {'Yes' if job.remote else 'No'}")

    if job.url:
        print(f"URL        : {job.url}")

    print("-" * 70)


def main():

    print("=" * 70)
    print("AI Job Agent")
    print("=" * 70)

    client = JobsucheClient()

    jobs = client.search_multiple(SEARCH_TERMS)

    print(f"\nFound {len(jobs)} unique jobs\n")

    jobs = sorted(
        jobs,
        key=lambda job: job.company.lower()
    )

    for job in jobs:
        print_job(job)

    print(f"\nTotal Jobs: {len(jobs)}")


if __name__ == "__main__":
    main()