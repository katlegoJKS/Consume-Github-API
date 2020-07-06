import requests

from datetime import timedelta, date

def pull_requests(repository_name, start_date, end_date):
      git_info = {
        'created_at':2020-4-1,
        'updated_at': 2020-6-20,
        'merged_at': {
            'start_ddate': start_date,
            'end_date': end_date
            }
        }

      repo_pull_requests = requests.get(repository_name, data=git_info)
      return repo_pull_requests.json()

pull_requests('https://api.github.com/repos/Umuzi-org/tech-department/pulls', 2020-4-1, 2020-6-1)