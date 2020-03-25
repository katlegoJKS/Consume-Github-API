from github import Github
from datetime import datetime
from datetime import timedelta, date

import git_token

from git_token import token

g = Github(token)

repos = g.get_user().get_repos()
for repo in repos:
    print(repo.name)

# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)

# start_date = date(2020, 3, 1)
# end_date = date(2020, 3, 10)

# for single_date in daterange(start_date, end_date):
#     date_obj = datetime.combine(single_date, datetime.min.time())
#     print(single_date.strftime('%Y-%m-%d:'), "pull request")