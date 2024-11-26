from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industries = set()

    for job in self.jobs_list:
        current_industry = job.get("industry")

        if current_industry:
            unique_industries.add(current_industry)

        return list(unique_industries)
