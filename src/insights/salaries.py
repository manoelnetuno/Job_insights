from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = [
            int(job["max_salary"])
            for job in self.jobs_list
            if job.get("max_salary") and job["max_salary"].isdigit()
        ]

        return max(max_salary) if max_salary else 0

    def get_min_salary(self) -> int:
        min_salary = [
            int(job["min_salary"])
            for job in self.jobs_list
            if job.get("min_salary") and job["min_salary"].isdigit()
        ]

        return min(min_salary) if min_salary else 0

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if isinstance(salary, str):
            salary = int(salary)

        min_salary = job.get("min_salary")
        max_salary = job.get("max_salary")

        if min_salary is None or max_salary is None:
            return False
        if not (isinstance(min_salary, int) and isinstance(max_salary, int)):
            return False

        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
