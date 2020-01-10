import pytest

from py_auth_header_parser import parse_auth_header


@pytest.mark.parametrize(
    "header,expected",
    [
        (
            "Authorization: Bearer AAA, Refresh BBB",
            {"access_token": "AAA", "refresh_token": "BBB"},
        ),
        (
            "Authorization: Bearer AAA,Refresh BBB",
            {"access_token": "AAA", "refresh_token": "BBB"},
        ),
        (
            "Authorization: BearerAAA,RefreshBBB",
            {"access_token": None, "refresh_token": None},
        ),
        (
            "Authorization: Bearer AAA       , Refresh BBB       ",
            {"access_token": "AAA", "refresh_token": "BBB"},
        ),
        (
            "Authorization: Bearer AAA , Refresh BBB,",
            {"access_token": "AAA", "refresh_token": "BBB"},
        ),
        ("Authorization: Bearer AAA", {"access_token": "AAA", "refresh_token": None}),
        ("Authorization: Refresh BBB", {"access_token": None, "refresh_token": "BBB"}),
        ("", {"access_token": None, "refresh_token": None}),
        ("Authorization:   ", {"access_token": None, "refresh_token": None}),
        ("Authorization: Bearer ,", {"access_token": None, "refresh_token": None}),
        (
            "Authorization: Bearer , Refresh ",
            {"access_token": None, "refresh_token": None},
        ),
        (
            "Authorization: Bearer , Refresh BBB",
            {"access_token": None, "refresh_token": "BBB"},
        ),
        (
            "Authorization: Bearer AAA, Refresh ",
            {"access_token": "AAA", "refresh_token": None},
        ),
        (
            "Authorization: Bearer AAA, Bearer aaa",
            {"access_token": "AAA", "refresh_token": None},
        ),
    ],
)
def test_AuthService_parse_auth_header(header, expected):
    """Ensure parse_auth_header() correctly parses and extracts access and refresh token
    values from the Authorization header.
    """
    parsed = parse_auth_header(header)
    assert parsed == expected