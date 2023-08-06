from __future__ import annotations

import json
import typing as t
import urllib.parse

if t.TYPE_CHECKING:
    from .typings import JSON


def extract_cookies(headers: dict[str, str]) -> dict[str, str]:
    """:returns: a dict of cookies based off the 'cookie' header"""
    cookie_header = headers.pop("cookie", None)
    if not cookie_header:
        return {}
    cookie_dict = {}
    for cookie in cookie_header.split("; "):
        try:
            key, value = cookie.split("=", maxsplit=1)
            cookie_dict[key] = value
        except ValueError:
            continue
    return cookie_dict


def parse_url(url: str) -> tuple[str, dict[str, str] | None]:
    parsed_url = urllib.parse.urlparse(url)
    query = parse_url_encoded(parsed_url.query) or None

    without_query = urllib.parse.ParseResult(
        parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, "", parsed_url.fragment
    )

    return without_query.geturl(), query


def format_json_like(data: JSON, indent: int | None = 4) -> str:
    # I'm not sure it's possible to pretty-format this with something like
    # pprint, but if it is possible LMK!
    formatted = json.dumps(data, indent=indent)
    # parse bools and none
    # leading space allows us to only match literal false and not "false" string
    formatted = formatted.replace(" null", " None")
    formatted = formatted.replace(" true", " True")
    formatted = formatted.replace(" false", " False")
    # replace lists with tuples
    # (json doesn't support tuples)
    formatted = formatted.replace("[", "(")
    formatted = formatted.replace("]", ")")
    # replace binary with actual bytes of binary
    formatted = formatted.replace('"(binary)"', 'b"(binary)"')
    return formatted


def format_string(text: str) -> str:
    """formats a string"""
    if "'" in text or '"' in text:
        # text contains a quote, so let python escape it optimally
        return repr(text)
    # double quotes by default
    return f'"{text}"'


def parse_url_encoded(x: str) -> dict[str, str]:
    """parses application/x-www-form-urlencoded and query string params"""
    return dict(urllib.parse.parse_qsl(x, keep_blank_values=True))


def fix_escape_chars(body: str) -> str:
    """
    replaces escaped \\ followed by a letter to the appropriate char
    (ex. "\\t" --> "\t")
    (ex. "\\n" --> "\n")
    """
    return body.encode(encoding="utf8", errors="ignore").decode(encoding="unicode_escape", errors="ignore")
