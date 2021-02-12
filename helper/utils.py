def make_url_from_title(string: str) -> str:
    return "-".join(string.split())


def make_title_from_url(string: str) -> str:
    return " ".join(string.split('-'))
