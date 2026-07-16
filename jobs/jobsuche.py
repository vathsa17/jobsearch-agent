"""
Jobsuche API Client

https://jobsuche.api.bund.dev/
"""

from __future__ import annotations

import requests

from config import JOBSUCHE_API_KEY
from config import JOBSUCHE_URL
from config import SEARCH_LOCATION

from jobs.models import Job


class JobsucheClient:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update(
            {
                "X-API-Key": JOBSUCHE_API_KEY
            }
        )

    # --------------------------------------------------

    def search(
        self,
        keyword: str,
        page: int = 1,
        size: int = 25,
    ) -> list[Job]:

        params = {
            "was": keyword,
            "wo": SEARCH_LOCATION,
            "page": page,
            "size": size,
        }

        response = self.session.get(
            JOBSUCHE_URL,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        jobs = []

        for item in data.get("ergebnisliste", []):

            jobs.append(
                self._parse_job(item)
            )

        return jobs

    # --------------------------------------------------

    def search_multiple(
        self,
        keywords: list[str],
    ) -> list[Job]:

        found = {}

        for keyword in keywords:

            print(f"Searching: {keyword}")

            jobs = self.search(keyword)

            for job in jobs:

                found[job.reference] = job

        return list(found.values())

    # --------------------------------------------------

    def _parse_job(
        self,
        item: dict,
    ) -> Job:

        location = ""

        if item.get("stellenlokationen"):

            try:

                location = (
                    item["stellenlokationen"][0]
                    ["adresse"]["ort"]
                )

            except Exception:

                pass

        salary = ""

        if (
            item.get("gehaltsspanneVon")
            and
            item.get("gehaltsspanneBis")
        ):

            salary = (
                f"{int(item['gehaltsspanneVon'])}"
                " - "
                f"{int(item['gehaltsspanneBis'])}"
                " €"
            )

        remote = item.get(
            "homeofficemoeglich",
            False,
        )

        return Job(

            reference=item.get(
                "referenznummer",
                ""
            ),

            title=item.get(
                "stellenangebotsTitel",
                ""
            ),

            company=item.get(
                "firma",
                ""
            ),

            location=location,

            profession=item.get(
                "hauptberuf",
                ""
            ),

            salary=salary,

            remote=remote,

            url=item.get(
                "externeURL"
            ),
        )