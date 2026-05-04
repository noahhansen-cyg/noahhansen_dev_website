def test_index_contains_name(client):
    resp = client.get("/")
    assert b"Noah Hansen" in resp.data


def test_index_has_work_section(client):
    resp = client.get("/")
    assert b'id="work"' in resp.data


def test_index_has_projects_section(client):
    resp = client.get("/")
    assert b'id="projects"' in resp.data


def test_index_has_life_section(client):
    resp = client.get("/")
    assert b'id="life"' in resp.data


def test_index_has_links_section(client):
    resp = client.get("/")
    assert b'id="links"' in resp.data


def test_index_contains_github_link(client):
    resp = client.get("/")
    assert b"github.com" in resp.data


def test_index_contains_resume_link(client):
    resp = client.get("/")
    assert b"/resume" in resp.data


def test_index_contains_email(client):
    resp = client.get("/")
    assert b"noah.hansen1323@gmail.com" in resp.data
