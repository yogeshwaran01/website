import requests


def github_repo() -> list:
    repos = []
    api = "https://api.github.com/users/yogeshwaran01/repos"
    data = requests.get(api).json()
    for i in data:
        repos.append(i["full_name"])
    return repos
