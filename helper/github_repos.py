import requests


def github_repo(username: str) -> list:
    """ Function returns all public repos for given username """
    repos = []
    api = f"https://api.github.com/users/{username}/repos"
    data = requests.get(api).json()
    for i in data:
        repos.append(i["full_name"])
    return repos
