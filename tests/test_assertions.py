from datetime import timedelta
from types import SimpleNamespace

import pytest

from utils.assertions import assert_status_code


class FakeResponse:
    status_code = 500
    text = "Internal Server Error"
    url = "https://api.example.test/users/octocat"
    elapsed = timedelta(seconds=1.25)
    request = SimpleNamespace(method="GET")


def test_assert_status_code_includes_request_context_on_failure():
    with pytest.raises(AssertionError) as error:
        assert_status_code(FakeResponse(), 200)

    message = str(error.value)
    assert "Expected 200, got 500" in message
    assert "Request: GET https://api.example.test/users/octocat" in message
    assert "Elapsed: 1.25s" in message
    assert "Internal Server Error" in message
