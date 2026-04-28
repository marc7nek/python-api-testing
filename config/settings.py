from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://api.github.com")
    api_version: str = os.getenv("GITHUB_API_VERSION", "2022-11-28")
    github_token: str = os.getenv("GITHUB_TOKEN", "")
    demo_username: str = os.getenv("DEMO_USERNAME", "octocat")
    demo_owner: str = os.getenv("DEMO_OWNER", "octocat")
    demo_repo: str = os.getenv("DEMO_REPO", "Hello-World")
    request_timeout: int = int(os.getenv("REQUEST_TIMEOUT", "15"))


settings = Settings()