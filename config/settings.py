from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://api.github.com")
    api_version: str = os.getenv("GITHUB_API_VERSION", "2026-03-10")
    github_token: str = os.getenv("GITHUB_TOKEN", "")
    demo_username: str = os.getenv("DEMO_USERNAME", "octocat")
    demo_owner: str = os.getenv("DEMO_OWNER", "octocat")
    demo_repo: str = os.getenv("DEMO_REPO", "Hello-World")
    request_timeout: int = int(os.getenv("REQUEST_TIMEOUT", "15"))
    retry_total: int = int(os.getenv("RETRY_TOTAL", "2"))
    retry_backoff_factor: float = float(os.getenv("RETRY_BACKOFF_FACTOR", "0.3"))
    api_debug: bool = os.getenv("API_DEBUG", "false").lower() == "true"


settings = Settings()
