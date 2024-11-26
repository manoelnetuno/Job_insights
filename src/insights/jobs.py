from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self) -> List[Dict]:
        with open(path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            self.jobs_list = [row for row in csv_reader]
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
