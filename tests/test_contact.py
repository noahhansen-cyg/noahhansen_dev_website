from unittest.mock import patch


def test_contact_success(client):
    with patch("app.routes.mail.send"):
        resp = client.post("/contact", data={
            "name": "Test User",
            "email": "test@example.com",
            "message": "Hello there",
        })
    assert resp.status_code == 200
    assert resp.get_json()["success"] is True


def test_contact_missing_name(client):
    resp = client.post("/contact", data={
        "email": "test@example.com",
        "message": "Hello",
    })
    assert resp.status_code == 400


def test_contact_missing_email(client):
    resp = client.post("/contact", data={
        "name": "Test",
        "message": "Hello",
    })
    assert resp.status_code == 400


def test_contact_missing_message(client):
    resp = client.post("/contact", data={
        "name": "Test",
        "email": "test@example.com",
    })
    assert resp.status_code == 400


def test_contact_all_empty(client):
    resp = client.post("/contact", data={"name": "", "email": "", "message": ""})
    assert resp.status_code == 400


def test_contact_get_not_allowed(client):
    resp = client.get("/contact")
    assert resp.status_code == 405
