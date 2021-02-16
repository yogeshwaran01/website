import requests

skipable_repos = [
    "yogeshwaran01/yogeshwaran01.github.io",
    "yogeshwaran01/yogeshwaran01"
]


def github_repo(username: str) -> list:
    """ Function returns all public repos for given username """
    repos = []
    api = f"https://api.github.com/users/{username}/repos"
    data = requests.get(api).json()
    for i in data:
        name = i["full_name"]
        if name in skipable_repos:
            pass
        else:
            url = "https://github-readme-stats.vercel.app/api/pin/?username={}&repo={}&theme=chartreuse-dark".format(
                name.split("/")[0], name.split("/")[1]
            )
            data = {
                "image": url,
                "link": "https://github.com/" + name
            }
            repos.append(data)
    return repos
