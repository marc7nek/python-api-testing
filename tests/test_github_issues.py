import pytest
from utils.assertions import (
    assert_json_schema,
    assert_response_time_under,
    assert_status_code,
)
from utils.schemas import ISSUE_SCHEMA


@pytest.mark.live
@pytest.mark.regression
def test_list_repository_issues(github_client, demo_repo):
    response = github_client.list_repository_issues(
        demo_repo["owner"],
        demo_repo["repo"],
        state="all",
        per_page=10,
    )

    assert_status_code(response, 200)
    assert_response_time_under(response, 5)

    body = response.json()
    assert isinstance(body, list)

    if body:
        assert_json_schema(body[0], ISSUE_SCHEMA)
