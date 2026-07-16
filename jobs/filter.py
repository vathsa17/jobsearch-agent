from jobs.models import Job

GOOD_KEYWORDS = [
    "salesforce",
    "apex",
    "lightning",
    "lwc",
]

BAD_KEYWORDS = [
    "sap",
    "google cloud",
    "azure",
    "aws",
    "microsoft cloud",
    "hubspot",
]


def is_relevant(job: Job) -> bool:

    text = f"{job.title} {job.profession}".lower()

    if any(word in text for word in BAD_KEYWORDS):
        return False

    return any(word in text for word in GOOD_KEYWORDS)