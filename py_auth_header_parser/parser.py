import re
from typing import Optional


def parse_auth_header(
    auth_header: str, 
    access_token_title: str = "Bearer",
    refresh_token_title: str = "Refresh",
) -> dict:
    """Parses a Authorization/Authentication http header and extracts the access + request 
    tokens if present.

    Example header:
    "Authorization: Bearer AAA, Refresh BBB"
    """
    def _match_token(token_title: str) -> Optional[str]:
        expression = re.escape(token_title) + r" ([^\s,]+)"
        match = re.search(expression, auth_header)
        try:
            return match.group(1)
        except (AttributeError, IndexError):
            return None
            
    tokens = {
        "access_token": _match_token(access_token_title),
        "refresh_token": _match_token(refresh_token_title)
    }
    return tokens