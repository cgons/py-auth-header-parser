Python Auth. Header Parser
==========================
A small and simple library to parse JWT tokens embedded in Authorization or Authentication HTTP headers.

_Note: This library does not decode the JWT token. It simply extracts the JWT token string from the header string._  

## Installation
```
pip install py-auth-header-parser
```
https://pypi.org/project/py-auth-header-parser/


## Usage

```
from py_auth_header_parser import parse_auth_header

header = "Authorization: Bearer AAA, Refresh BBB"
parsed = parse_auth_header(header)

# 'parsed' will then contain:
{
  "access_token": "AAA",
  "refresh_token": "BBB",
}
```

`parse_auth_header()` will always return a dict with two keys: `access_token` and `refresh_token`.

When a token is not present in the header or, cannot be parsed, the key's value will be `None`.

For example, given the following headers:  
1. `Authorization: Bearer AAA`   
2. `Authorization: Bearer AAA, RefreshG1bb3r1sh`

The parsed result will be:
```
{"access_token": "AAA", "refresh_token": None}
```
