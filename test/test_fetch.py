from unittest.mock import patch
from fetch import fetch_github_repositories, fetch_nasa_apod, fetch_color_palette


@patch("requests.get")
def test_fetch_github_repositories(mock_get):
    # Mock response data for two repositories
    mock_response = [
        {"name": "example_repo_1", "created_at": "2023-01-01"},
        {"name": "example_repo_2", "created_at": "2023-01-02"},
    ]
    mock_get.return_value.json.return_value = mock_response

    result = fetch_github_repositories()

    # Assert that we have two repositories
    assert len(result) == 2

    # Check the order of the repositories by creation date
    assert result[0]["name"] == "example_repo_2"
    assert result[1]["name"] == "example_repo_1"


@patch("requests.get")
def test_fetch_nasa_apod(mock_get):
    # Mock response data
    mock_response = {
        "title": "Astronomy Picture of the Day",
        "url": "http://example.com/apod.jpg",
        "explanation": "This is an explanation.",
    }
    mock_get.return_value.json.return_value = mock_response

    result = fetch_nasa_apod()

    assert result["title"] == "Astronomy Picture of the Day"
    assert result["url"] == "http://example.com/apod.jpg"
    assert result["explanation"] == "This is an explanation."


@patch("requests.post")
def test_fetch_color_palette(mock_post):
    # Mock response data
    mock_response = {"result": [[255, 0, 0]]}
    mock_post.return_value.json.return_value = mock_response

    result = fetch_color_palette()

    assert result == "#ff0000"