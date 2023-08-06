from __future__ import annotations

import json
import typing as t

from requests_toolbelt.multipart import decoder  # type: ignore[import]

from ..commons import fix_escape_chars, parse_url_encoded

if t.TYPE_CHECKING:
    from ..typings import JSON, Data, Files


def parse_body(body: str | None, content_type: str | None) -> tuple[Data | None, JSON | None, Files | None]:
    data: Data | None = None
    json_: JSON | None = None
    files: Files | None = None

    if not body:
        return data, json_, files
    else:
        body = fix_escape_chars(body)

    def is_multipart_form_data(body: str) -> bool:
        return "------WebKitFormBoundary" in body

    def is_urlencoded(body: str) -> bool:
        if not body or "=" not in body:
            return False
        return all(item.count("=") > 0 for item in body.split("&"))

    def is_json(body: str) -> bool:
        if not body:
            return False
        try:
            json.loads(body, strict=False)
        except json.JSONDecodeError:
            return False
        else:
            return True

    if is_multipart_form_data(body) and content_type:
        data, files = parse_multipart_form_data(body, content_type)
    elif is_urlencoded(body):
        data = parse_url_encoded(body)
    elif is_json(body):
        json_ = parse_json(body)
    return data, json_, files


def standardize_newlines(body: str) -> str:
    """
    standardize newlines to \n
    (ex. "\r\n" --> "\n")
    """
    return "\n".join(body.splitlines())


def parse_json(body: str) -> JSON | None:
    return json.loads(body, strict=False)


def parse_multipart_form_data(body: str, content_type: str) -> tuple[Data | None, Files | None]:
    data: Data = {}
    files: Files = {}

    decoded = decoder.MultipartDecoder(body.encode(), content_type=content_type)

    data = {}
    files = {}

    for part in decoded.parts:
        disposition = part.headers.get(b"Content-Disposition")  # type: ignore

        if not disposition:
            continue

        disposition = disposition.decode()
        disposition = disposition.lstrip("form-data; ")

        values: dict[str, str] = {}

        for item in disposition.split("; "):
            key, value = item.split("=", maxsplit=1)
            values[key] = value.strip('"')

        name = values.get("name")
        filename = values.get("filename")

        if not name:
            continue
        elif filename:
            files[name] = (filename, "(binary)")  # type: ignore
        else:
            data[name] = part.text

    return data, files
