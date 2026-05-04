import pytest
from app.routes import get_slideshow_images


def test_returns_empty_for_missing_directory():
    assert get_slideshow_images("/nonexistent/path/abc") == []


def test_filters_to_image_extensions_only(tmp_path):
    for name in ("photo.jpg", "photo.png", "photo.webp", "photo.jpeg", "photo.gif"):
        (tmp_path / name).touch()
    for name in ("document.pdf", "script.js", "data.yaml", ".gitkeep"):
        (tmp_path / name).touch()

    result = get_slideshow_images(str(tmp_path))

    assert set(result) == {"photo.jpg", "photo.png", "photo.webp", "photo.jpeg", "photo.gif"}


def test_returns_sorted_alphabetically(tmp_path):
    for name in ("charlie.jpg", "alpha.jpg", "bravo.png"):
        (tmp_path / name).touch()

    assert get_slideshow_images(str(tmp_path)) == ["alpha.jpg", "bravo.png", "charlie.jpg"]


def test_case_insensitive_extension_matching(tmp_path):
    for name in ("photo.JPG", "photo.PNG", "photo.Jpeg"):
        (tmp_path / name).touch()

    result = get_slideshow_images(str(tmp_path))
    assert len(result) == 3


def test_empty_directory_returns_empty_list(tmp_path):
    assert get_slideshow_images(str(tmp_path)) == []


def test_index_renders_without_slideshow_images(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"slideshow" not in resp.data
