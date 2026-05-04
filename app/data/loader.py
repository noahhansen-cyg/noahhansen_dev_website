import os
import yaml

_DATA_DIR = os.path.dirname(__file__)


def _load(filename):
    path = os.path.join(_DATA_DIR, filename)
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_all():
    return {
        "work": _load("work.yaml"),
        "projects": _load("projects.yaml"),
        "life": _load("life.yaml"),
        "links": _load("links.yaml"),
    }
