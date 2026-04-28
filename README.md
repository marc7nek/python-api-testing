# Python API Testing

A demo Python API automation framework for testing GitHub REST API endpoints.

## Stack

- Python 3.10+
- pytest
- requests
- pytest-html
- python-dotenv
- jsonschema
- PyGithub

## What this framework covers

- Reusable API client
- Environment-based configuration
- Optional GitHub token support
- Positive and negative API tests
- JSON schema validation
- Pytest markers
- HTML reports
- GitHub Actions CI workflow

## Demo endpoints used

The framework uses safe public `GET` endpoints:

- `GET /users/{username}`
- `GET /repos/{owner}/{repo}`
- `GET /repos/{owner}/{repo}/issues`
- `GET /rate_limit`

## Project structure

```text
github_api_testing_framework/
├── api/
│   ├── base_client.py
│   └── github_client.py
├── config/
│   └── settings.py
├── tests/
│   ├── conftest.py
│   ├── test_github_users.py
│   ├── test_github_repos.py
│   ├── test_github_issues.py
│   └── test_github_rate_limit.py
├── utils/
│   ├── assertions.py
│   └── schemas.py
├── pytest.ini
└── requirements.txt
```

## Setup

```bash
python -m venv .venv
```

Activate it:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your local `.env` file:

```bash
cp .env.example .env
```

Optional: add a GitHub token to avoid low unauthenticated rate limits.

```env
GITHUB_TOKEN=your_token_here
```

## Run tests

Run all tests:

```bash
pytest
```

Run smoke tests only:

```bash
pytest -m smoke
```

Run tests and generate HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Configuration

Edit `.env`:

```env
BASE_URL=https://api.github.com
GITHUB_API_VERSION=2022-11-28
GITHUB_TOKEN=
DEMO_USERNAME=octocat
DEMO_OWNER=octocat
DEMO_REPO=Hello-World
REQUEST_TIMEOUT=15
```

## Notes

This demo uses read-only public endpoints, so it is safe to run without creating, editing, or deleting GitHub data.
