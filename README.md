# Python Learning Journal

A living record of my journey learning Python. Code under `src/learning/`,
narrative notes under `docs/notes/`, and an auto-generated reference site
published at **https://samirinux.github.io/python-learning-docs/**.

## Project layout

```
.
├── docs/
│   ├── index.md            # landing page
│   ├── notes/              # narrative learning notes (written by me)
│   ├── reference/          # API reference (auto-generated at build time)
│   └── gen_ref_pages.py    # script that generates reference/ at build time
├── src/learning/           # Python code I'm studying / writing
├── tests/                  # pytest tests
├── properdocs.yml          # docs site config (read by ProperDocs)
├── pyproject.toml          # package metadata
└── .github/workflows/      # CI: auto-deploys docs on push to main
```

## Local development (ProperDocs)

This project uses [ProperDocs](https://properdocs.org/) — a continuation of
MkDocs 1.x — to build the docs site, and [uv](https://docs.astral.sh/uv/)
for Python and dependency management.

```bash
# one-time setup
uv venv
uv sync

# day-to-day: start the live-reloading docs server
uv run properdocs serve
# then open http://127.0.0.1:8000

# one-off full build into ./site
uv run properdocs build

# manual deploy to GitHub Pages (the CI does this automatically on push)
uv run properdocs gh-deploy --force --clean
```

Run tests with:

```bash
uv run pytest
```

### How the docs are built

Two layers on the same site:

- **Learning Notes** (`docs/notes/`): prose. My own voice, my own mistakes.
- **API Reference** (`docs/reference/`): generated from docstrings by
  [mkdocstrings](https://mkdocstrings.github.io/). Don't edit these files
  directly — edit the docstrings in `src/learning/` and they regenerate.

The site is built by ProperDocs with the
[Material theme](https://squidfunk.github.io/mkdocs-material/) (still
compatible) and published to GitHub Pages by a workflow in
`.github/workflows/docs.yml`. Every push to `main` rebuilds and redeploys.

## Legacy: MkDocs instructions (obsolete)

> [!WARNING]
> **These instructions are obsolete.** The project migrated from MkDocs to
> ProperDocs. The commands below are kept for historical reference only —
> do not use them. The config file has been renamed from `mkdocs.yml` to
> `properdocs.yml`, and the `mkdocs` CLI is no longer a project dependency.
> Use the [ProperDocs instructions above](#local-development-properdocs).

<details>
<summary>Show obsolete MkDocs commands</summary>

```bash
# OBSOLETE — do not use
uv venv
uv pip install -r requirements-docs.txt
uv pip install -e .

uv run mkdocs serve          # replaced by: uv run properdocs serve
uv run mkdocs build          # replaced by: uv run properdocs build
uv run mkdocs gh-deploy      # replaced by: uv run properdocs gh-deploy
```

The old config file `mkdocs.yml` has been renamed to `properdocs.yml`.
ProperDocs still reads `mkdocs.yml` as a legacy fallback but prints a
deprecation notice, and that fallback is slated for removal.

</details>

## License

MIT — see `LICENSE` if present, or add your own.
