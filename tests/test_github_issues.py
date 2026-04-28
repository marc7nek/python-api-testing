import pytest
from utils.assertions import assert_status_code, assert_response_time_under


@pytest.mark.regression
def test_list_repository_issues(github_client, demo_repo):
    response = github_client.list_repository_issues(
        demo_repo["owner"],
        demo_repo["repo"],
        state="all",
    )

    assert_status_code(response, 200)
    assert_response_time_under(response, 5)

    body = response.json()
    assert isinstance(body, list)

    if body:
        assert "id" in body[0]
        assert "state" in body[0]
        assert "html_url" in body[0]
