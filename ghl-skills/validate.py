#!/usr/bin/env python3
"""Check that every skill file in this tree will import into GoHighLevel.

GHL takes one self-contained Markdown file per skill, with a single YAML
frontmatter block carrying name and description. The checks below are the
failure modes actually observed in the wild: a byte-order mark ahead of the
opening delimiter, CRLF endings, a second frontmatter block that pushes the
required fields into the body, and pointers to sibling files that do not
survive the import.

Exits non-zero if anything fails, so it can gate a release.
"""

import glob
import os
import re
import sys

DOCS = {"README.md", "_TEMPLATE.md", "PROVISIONING-SCHEMA.md"}
MAX_BYTES = 50 * 1024
ROOT = os.path.dirname(os.path.abspath(__file__))


def problems_with(raw: bytes) -> list[str]:
    found = []

    if raw[:3] == b"\xef\xbb\xbf":
        found.append("byte-order mark before opening ---")
    if b"\r\n" in raw:
        found.append("CRLF line endings")
    if len(raw) > MAX_BYTES:
        found.append(f"{len(raw)} bytes, over the {MAX_BYTES} limit")

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return found + ["not valid UTF-8"]

    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        found.append("no frontmatter block at the start of the file")
    else:
        block, body = match.group(1), text[match.end():]
        for field in ("name", "description"):
            if re.search(rf"^{field}:", block, re.M):
                continue
            if re.search(rf"^{field}:", body, re.M):
                # The field exists, just not in the block a parser reads. This is
                # the signature of a file with two frontmatter blocks stacked.
                found.append(
                    f"{field} appears in the body, not the first frontmatter block"
                    " - a parser only reads the first block, so this field is invisible"
                )
            else:
                found.append(f"frontmatter missing {field}")

    if re.search(r"\breferences/|\bscripts/|\.\./", text):
        found.append("points at a sibling file or directory")

    return found


def main() -> int:
    failures = 0
    paths = sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))

    for path in paths:
        if os.path.basename(path) in DOCS:
            continue
        raw = open(path, "rb").read()
        found = problems_with(raw)
        rel = os.path.relpath(path, ROOT)
        if found:
            failures += 1
            print(f"FAIL  {rel}")
            for problem in found:
                print(f"        {problem}")
        else:
            print(f"ok    {rel} ({len(raw)} bytes)")

    checked = len(paths) - sum(1 for p in paths if os.path.basename(p) in DOCS)
    print(f"\n{checked - failures}/{checked} ready to import")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
