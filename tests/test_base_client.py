from api import base_client
from api.base_client import BaseClient


class DummySession:
    def __init__(self):
        self.headers = {}
        self.request_calls = []

    def request(self, **kwargs):
        self.request_calls.append(kwargs)
        return {"ok": True}


def test_base_client_builds_url_and_sets_default_timeout(monkeypatch):
    session = DummySession()
    monkeypatch.setattr(base_client.requests, "Session", lambda: session)

    client = BaseClient(base_url="https://api.example.test/")
    response = client.get("/users/octocat")

    assert response == {"ok": True}
    assert session.request_calls == [
        {
            "method": "GET",
            "url": "https://api.example.test/users/octocat",
            "timeout": base_client.settings.request_timeout,
        }
    ]


def test_base_client_sets_expected_github_headers(monkeypatch):
    session = DummySession()
    monkeypatch.setattr(base_client.requests, "Session", lambda: session)

    BaseClient()

    assert session.headers["Accept"] == "application/vnd.github+json"
    assert session.headers["X-GitHub-Api-Version"] == base_client.settings.api_version
    assert session.headers["User-Agent"] == "python-api-automation-framework"
