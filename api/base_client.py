import logging

import requests
from requests import Response
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config.settings import settings

logger = logging.getLogger(__name__)


class BaseClient:
    def __init__(self, base_url: str = settings.base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self._configure_retries()
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

    def _configure_retries(self) -> None:
        retry = Retry(
            total=settings.retry_total,
            backoff_factor=settings.retry_backoff_factor,
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=("GET", "HEAD", "OPTIONS"),
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def request(self, method: str, endpoint: str, **kwargs) -> Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        kwargs.setdefault("timeout", settings.request_timeout)

        if settings.api_debug:
            logger.info("API request: %s %s", method, url)

        response = self.session.request(method=method, url=url, **kwargs)

        if settings.api_debug:
            logger.info(
                "API response: %s %s in %.3fs",
                response.status_code,
                response.url,
                response.elapsed.total_seconds(),
            )

        return response

    def get(self, endpoint: str, **kwargs) -> Response:
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> Response:
        return self.request("POST", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs) -> Response:
        return self.request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> Response:
        return self.request("DELETE", endpoint, **kwargs)
