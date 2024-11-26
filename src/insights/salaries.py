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
            if not salary.isdigit():
                raise ValueError("O parâmetro salary deve ser um número.")
            salary = int(salary)

        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError("As chaves min_salary e max_salary devem estar presentes no dicionário job.")

        min_salary = job['min_salary']
        max_salary = job['max_salary']

        for value in (min_salary, max_salary):
            if isinstance(value, str):
                if not value.isdigit():
                    raise ValueError("Os valores de min_salary e max_salary devem ser numéricos.")
                value = int(value)

        if int(min_salary) > int(max_salary):
            raise ValueError("O valor de min_salary não pode ser maior que o valor de max_salary.")

        return int(min_salary) <= salary <= int(max_salary)


    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
