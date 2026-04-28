from jsonschema import validate


def assert_status_code(response, expected_status_code: int):
    assert response.status_code == expected_status_code, (
        f"Expected {expected_status_code}, got {response.status_code}. "
        f"Response body: {response.text}"
    )


def assert_json_schema(response_json: dict, schema: dict):
    validate(instance=response_json, schema=schema)


def assert_response_time_under(response, max_seconds: float):
    elapsed = response.elapsed.total_seconds()
    assert elapsed < max_seconds, f"Response took {elapsed:.2f}s, expected under {max_seconds}s"