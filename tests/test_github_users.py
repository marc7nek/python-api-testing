import pytest
from utils.assertions import (
    assert_status_code,
    assert_json_schema,
    assert_response_time_under,
)
from utils.schemas import USER_SCHEMA


@pytest.mark.smoke
def test_get_existing_github_user(github_client, demo_user):
    response = github_client.get_user(demo_user)

    assert_status_code(response, 200)
    assert_response_time_under(response, 5)

    body = response.json()
    assert_json_schema(body, USER_SCHEMA)
    assert body["login"].lower() == demo_user.lower()


@pytest.mark.negative
def test_get_non_existing_github_user_returns_404(github_client):
    response = github_client.get_user("this-user-should-not-exist-987654321")

    assert_status_code(response, 404)
    assert "message" in response.json()
