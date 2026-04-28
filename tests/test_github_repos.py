import pytest
from utils.assertions import (
    assert_status_code,
    assert_json_schema,
    assert_response_time_under,
)
from utils.schemas import REPOSITORY_SCHEMA


@pytest.mark.smoke
def test_get_existing_repository(github_client, demo_repo):
    response = github_client.get_repository(demo_repo["owner"], demo_repo["repo"])

    assert_status_code(response, 200)
    assert_response_time_under(response, 5)

    body = response.json()
    assert_json_schema(body, REPOSITORY_SCHEMA)
    assert body["owner"]["login"].lower() == demo_repo["owner"].lower()
    assert body["name"].lower() == demo_repo["repo"].lower()


@pytest.mark.negative
def test_get_non_existing_repository_returns_404(github_client):
    response = github_client.get_repository("octocat", "repo-that-does-not-exist-987654321")

    assert_status_code(response, 404)
    assert "message" in response.json()
