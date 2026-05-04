def test_index_returns_200(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_resume_returns_200(client):
    resp = client.get("/resume")
    assert resp.status_code == 200


def test_resume_contains_pdf_embed(client):
    resp = client.get("/resume")
    assert b"resume.pdf" in resp.data


def test_health_returns_200(client):
    resp = client.get("/health")
    assert resp.status_code == 200


def test_health_returns_json(client):
    resp = client.get("/health")
    assert resp.is_json


def test_health_body(client):
    resp = client.get("/health")
    assert resp.get_json() == {"status": "ok"}


def test_unknown_route_returns_404(client):
    resp = client.get("/nonexistent")
    assert resp.status_code == 404
