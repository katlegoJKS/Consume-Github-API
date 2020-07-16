from github import Github
import datetime
import urllib3
import requests
import os

UserName = os.environ.get('USERNAME')
PassWord = os.environ.get('PASSWORD')

RepositoryLogin = Github(UserName, PassWord)

def get_pull_requests(start_date, end_date, repository_name):
    repository = RepositoryLogin.get_repo(repository_name)
    pulls = repository.get_pulls(state='all', sort='created', base='master')
    for pr in pulls:
        if pr.created_at.date() == start_date and pr.closed_at.date() == end_date:
            print("\n> Date of pull requests created and closed on the same day:\n")
        else:
            print("\n> Dates of pull requests created and closed on different days:\n")
            pull_requests = {
                "Date created" : pr.created_at,
                "Date updated" :pr.updated_at,
                "Date Merged" : pr.merged_at,
                "Date Closed" : pr.closed_at,
                "Repository" : pr.review_comments,
                }
            print(pull_requests)

started_date = datetime.datetime(2020, 6, 30, 9, 33, 9)
closed_date = datetime.datetime(2020, 7, 1, 8, 1, 31)
print(get_pull_requests(started_date.date(),closed_date.date(),"Umuzi-org/Katlego-Malatjie-286-dags-with-airflow"))

