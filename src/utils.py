from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def most_frequent(list):
    return max(set(list), key=list.count)