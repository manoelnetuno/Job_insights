from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        all_industries = self.get_unique_industries()  

        unique_industries = set(industry for industry in all_industries if industry)

        return list(unique_industries)