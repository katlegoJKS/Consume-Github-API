import requests

from datetime import timedelta, date

def pull_requests():
      git_info = {
        'created_at':2020-4-2,
        'updated_at': 2020-5-21,
        'pushed_at': 2020-4-21
      }

      ghpull_requests = requests.get("https://api.github.com/repos/Umuzi-org/tech-department/pulls?id=1", data=git_info)
      print(ghpull_requests.json())

pull_requests()
