import pytest
from app.data.loader import load_all


@pytest.fixture(scope="module")
def data():
    return load_all()


# --- loader ---

def test_load_all_returns_all_keys(data):
    assert set(data.keys()) == {"work", "projects", "life", "links"}


def test_no_section_is_empty(data):
    for key, value in data.items():
        assert value, f"'{key}' section is empty"


# --- work.yaml ---

def test_work_has_required_keys(data):
    work = data["work"]
    for key in ("title", "summary", "skills", "experience"):
        assert key in work, f"work.yaml missing key: '{key}'"


def test_work_skills_have_category_and_technologies(data):
    for skill in data["work"]["skills"]:
        assert "category" in skill
        assert "technologies" in skill
        assert isinstance(skill["technologies"], list)


def test_work_experience_has_required_keys(data):
    for job in data["work"]["experience"]:
        for key in ("company", "role", "dates", "bullets"):
            assert key in job, f"experience entry missing key: '{key}'"


# --- projects.yaml ---

def test_projects_is_a_list(data):
    assert isinstance(data["projects"], list)


def test_each_project_has_required_keys(data):
    for project in data["projects"]:
        for key in ("name", "description", "tech", "url", "status"):
            assert key in project, f"project '{project.get('name', '?')}' missing key: '{key}'"


def test_project_status_is_valid(data):
    valid_statuses = {"active", "archived", "wip"}
    for project in data["projects"]:
        assert project["status"] in valid_statuses, (
            f"project '{project['name']}' has invalid status: '{project['status']}'"
        )


# --- life.yaml ---

def test_life_is_a_list(data):
    assert isinstance(data["life"], list)


def test_each_life_entry_has_required_keys(data):
    for entry in data["life"]:
        for key in ("category", "blurb"):
            assert key in entry, f"life entry missing key: '{key}'"


# --- links.yaml ---

def test_links_has_required_keys(data):
    for key in ("name", "github", "linkedin", "email", "resume_filename"):
        assert key in data["links"], f"links.yaml missing key: '{key}'"


def test_links_values_are_non_empty_strings(data):
    for key, value in data["links"].items():
        assert isinstance(value, str) and value.strip(), (
            f"links.yaml value for '{key}' is empty or not a string"
        )
