USER_SCHEMA = {
    "type": "object",
    "required": ["login", "id", "html_url", "type"],
    "properties": {
        "login": {"type": "string"},
        "id": {"type": "integer"},
        "html_url": {"type": "string"},
        "type": {"type": "string"},
    },
}

REPOSITORY_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "full_name", "owner", "private"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "full_name": {"type": "string"},
        "owner": {"type": "object"},
        "private": {"type": "boolean"},
    },
}

RATE_LIMIT_SCHEMA = {
    "type": "object",
    "required": ["resources", "rate"],
    "properties": {
        "resources": {"type": "object"},
        "rate": {"type": "object"},
    },
}
