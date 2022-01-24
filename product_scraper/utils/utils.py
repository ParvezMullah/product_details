from urllib.parse import urlparse


def get_site(url : str) -> str:
    parsed_uri = urlparse(url)
    result = f'{parsed_uri.scheme}://{parsed_uri.netloc}/'
    return result


def append_path(path : str, text: str) -> str:
    return f"{path}/{text}"
