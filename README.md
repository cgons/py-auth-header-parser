Python Auth. Header Parser
==========================
A small and simple library to parse JWT tokens embedded in Authorization or Authentication HTTP headers.

_Note: This library does not decode the JWT token. It simply extracts the JWT token string from the header string._  


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
When a refresh token is no present in the header, the `refresh_token` key will be `None`.
