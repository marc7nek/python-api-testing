import requests
from requests import Response
from config.settings import settings


class BaseClient:
    def __init__(self, base_url: str = settings.base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": settings.api_version,
                "User-Agent": "python-api-automation-framework",
            }
        )

        if settings.github_token:
            self.session.headers.update(
                {"Authorization": f"Bearer {settings.github_token}"}
            )

    def request(self, method: str, endpoint: str, **kwargs) -> Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        kwargs.setdefault("timeout", settings.request_timeout)
        response = self.session.request(method=method, url=url, **kwargs)
        return response

    def get(self, endpoint: str, **kwargs) -> Response:
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> Response:
        return self.request("POST", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs) -> Response:
        return self.request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> Response:
        return self.request("DELETE", endpoint, **kwargs)