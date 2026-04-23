"""Generate a reference page for every module under src/.

This runs automatically at build time via the mkdocs-gen-files plugin.
You should not need to edit or run this by hand.
"""
from pathlib import Path

import mkdocs_gen_files

SRC = Path("src")

nav = mkdocs_gen_files.Nav()

for path in sorted(SRC.rglob("*.py")):
    module_path = path.relative_to(SRC).with_suffix("")
    doc_path = path.relative_to(SRC).with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = tuple(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
        if not parts:
            continue
    elif parts[-1].startswith("_"):
        # Skip private modules like _internal.py
        continue

    nav[parts] = doc_path.as_posix()

    identifier = ".".join(parts)
    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        fd.write(f"# `{identifier}`\n\n::: {identifier}\n")

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
