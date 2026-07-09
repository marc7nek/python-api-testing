from api.github_client import GitHubClient


class DummyGitHubClient(GitHubClient):
    def __init__(self):
        self.calls = []

    def get(self, endpoint: str, **kwargs):
        self.calls.append((endpoint, kwargs))
        return {"ok": True}


def test_get_user_builds_expected_endpoint():
    client = DummyGitHubClient()

    response = client.get_user("octocat")

    assert response == {"ok": True}
    assert client.calls == [("/users/octocat", {})]


def test_get_repository_builds_expected_endpoint():
    client = DummyGitHubClient()

    response = client.get_repository("octocat", "Hello-World")

    assert response == {"ok": True}
    assert client.calls == [("/repos/octocat/Hello-World", {})]


def test_list_repository_issues_passes_state_and_page_size():
    client = DummyGitHubClient()

    response = client.list_repository_issues(
        "octocat",
        "Hello-World",
        state="all",
        per_page=25,
    )

    assert response == {"ok": True}
    assert client.calls == [
        (
            "/repos/octocat/Hello-World/issues",
            {"params": {"state": "all", "per_page": 25}},
        )
    ]


def test_get_rate_limit_builds_expected_endpoint():
    client = DummyGitHubClient()

    response = client.get_rate_limit()

    assert response == {"ok": True}
    assert client.calls == [("/rate_limit", {})]
