from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            self.jobs_list = [row for row in csv_reader]
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = {
            job['job_type'] for job in self.jobs_list
            if 'job_type' in job
        }
        return list(job_types)

    def filter_by_multiple_criteria(
        self, filter_criteria: Dict[str, str], jobs: List[Dict]
    ) -> List[Dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("O filtro fornecido deve ser um dicionário.")

        filtered_jobs = jobs

        for key, value in filter_criteria.items():
            filtered_jobs = [
                job for job in filtered_jobs if job.get(key) == value
            ]

        return filtered_jobs
