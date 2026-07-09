from jsonschema import validate


def _response_debug_context(response) -> str:
    request = getattr(response, "request", None)
    method = getattr(request, "method", "UNKNOWN")
    url = getattr(response, "url", getattr(request, "url", "UNKNOWN"))

    body = response.text
    if len(body) > 1000:
        body = f"{body[:1000]}... [truncated]"

    return (
        f"Request: {method} {url}\n"
        f"Status: {response.status_code}\n"
        f"Elapsed: {response.elapsed.total_seconds():.2f}s\n"
        f"Response body: {body}"
    )


def assert_status_code(response, expected_status_code: int):
    assert response.status_code == expected_status_code, (
        f"Expected {expected_status_code}, got {response.status_code}.\n"
        f"{_response_debug_context(response)}"
    )


def assert_json_schema(response_json: dict, schema: dict):
    validate(instance=response_json, schema=schema)


def assert_response_time_under(response, max_seconds: float):
    elapsed = response.elapsed.total_seconds()
    assert elapsed < max_seconds, f"Response took {elapsed:.2f}s, expected under {max_seconds}s"
