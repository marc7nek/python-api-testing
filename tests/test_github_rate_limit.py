import pytest
from utils.assertions import assert_status_code, assert_json_schema
from utils.schemas import RATE_LIMIT_SCHEMA


@pytest.mark.smoke
def test_get_rate_limit_status(github_client):
    response = github_client.get_rate_limit()

    assert_status_code(response, 200)

    body = response.json()
    assert_json_schema(body, RATE_LIMIT_SCHEMA)
    assert "core" in body["resources"]
    assert "remaining" in body["resources"]["core"]
