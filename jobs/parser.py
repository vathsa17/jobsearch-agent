"""
Converts Jobsuche API responses into Job objects.
"""

from jobs.models import Job


class JobParser:

    @staticmethod
    def parse(item: dict) -> Job:

        locations = item.get("stellenlokationen", [])

        if locations:
            address = locations[0].get("adresse", {})
            location = address.get("ort", "")
        else:
            location = ""

        salary = ""

        salary_from = item.get("gehaltsspanneVon")
        salary_to = item.get("gehaltsspanneBis")

        if salary_from and salary_to:
            salary = f"{int(salary_from)} - {int(salary_to)} €"

        return Job(
            reference=item.get("referenznummer", ""),
            title=item.get("stellenangebotsTitel", ""),
            company=item.get("firma", ""),
            location=location,
            profession=item.get("hauptberuf", ""),
            salary=salary,
            remote=item.get("homeofficemoeglich", False),
            url=item.get("externeURL"),
        )