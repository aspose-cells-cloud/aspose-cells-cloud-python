"""Type alias for multipart ``formData`` file parameters.

Request classes that upload a file accept a :data:`FileSource` instead of a bare
local path, so callers may pass any of:

* a local file path (``str`` or :class:`pathlib.Path`) -- the original behaviour,
* raw binary content (``bytes`` / ``bytearray``),
* a file-like object exposing ``.read()`` (``open(..., "rb")``,
  ``io.BytesIO``, ...),
* a ``(filename, content)`` or ``(filename, content, content_type)`` tuple (the
  ``requests`` convention), where ``content`` is ``bytes`` or file-like.

The client normalises every accepted form into a ``requests`` multipart part
(see :meth:`aspose.cells.cloud.cells_cloud_client.CellsCloudClient._file_part`).
"""

from __future__ import annotations

from pathlib import Path
from typing import BinaryIO, Tuple, Union

#: Raw binary content: ``bytes``/``bytearray`` or any file-like object.
_BinaryContent = Union[bytes, bytearray, BinaryIO]

#: A single multipart file part accepted by ``formData`` parameters.
#:
#: * ``str`` / ``Path`` -- local file path; the remote filename is the basename.
#: * ``bytes`` / ``bytearray`` -- raw content; the filename defaults to the
#:   parameter's wire name (e.g. ``"UploadFiles"``).
#: * ``BinaryIO`` -- file-like object; the filename comes from ``.name`` when
#:   present, otherwise it defaults to the wire name.
#: * ``(filename, content)`` -- ``content`` is ``bytes`` or file-like; the
#:   content type defaults to ``application/octet-stream``.
#: * ``(filename, content, content_type)`` -- explicit MIME type.
FileSource = Union[
    str,
    Path,
    bytes,
    bytearray,
    BinaryIO,
    Tuple[str, _BinaryContent],
    Tuple[str, _BinaryContent, str],
]
