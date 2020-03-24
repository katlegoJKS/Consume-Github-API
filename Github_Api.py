from datetime import datetime
from datetime import timedelta, date

import github

git_client = github.Github("username", "key-here")
pull_counts ={}

def github_pull_requests(repo_name, start_date, end_date):
    pulls = []
    count = 0
    # i = 1
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

    for i in git_client.get_user().get_repos():
        pulls.append(i.get_pulls('all'))
        pull_counts[count] = 0
        count += 1
    return pulls

github_pull_requests()

if __name__ == "__main__":
    labs.github_pull_requests()
    while True:
        if not labs.check_counts():
            labs.pull_counts = {}
            labs.github_pull_requests()
            labs.set_pull_counts()


start_date = date(2019, 12, 1)
end_date = date(2020, 3, 5)

for single_date in daterange(start_date, end_date):
    date_obj = datetime.combine(single_date, datetime.min.time()
    print(single_date.strftime('%Y-%m-%d:'), "pull request")