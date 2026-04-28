from api.base_client import BaseClient


class GitHubClient(BaseClient):
    def get_user(self, username: str):
        return self.get(f"/users/{username}")

    def get_repository(self, owner: str, repo: str):
        return self.get(f"/repos/{owner}/{repo}")

    def list_repository_issues(self, owner: str, repo: str, state: str = "open"):
        return self.get(
            f"/repos/{owner}/{repo}/issues",
            params={"state": state, "per_page": 10},
        )

    def get_rate_limit(self):
        return self.get("/rate_limit")