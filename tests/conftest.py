import pytest
from api.github_client import GitHubClient
from config.settings import settings


@pytest.fixture(scope="session")
def github_client():
    return GitHubClient()


@pytest.fixture(scope="session")
def demo_user():
    return settings.demo_username


@pytest.fixture(scope="session")
def demo_repo():
    return {
        "owner": settings.demo_owner,
        "repo": settings.demo_repo,
    }
