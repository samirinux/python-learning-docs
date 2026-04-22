# Getting started: the setup clicked

This is the first real entry in my learning journal. The goal wasn't to
learn Python itself — it was to set up the rails on which I'll learn Python.
A deliberately boring day, so future days can be interesting.

## What I set up

A Python project with a split brain. Code lives under `src/learning/`, with
docstrings that describe what each function does. Narrative notes (like this
one) live under `docs/notes/`, where I get to use my own voice and say things
like "this confused me for an hour". A tool called MkDocs weaves both into a
website; another tool called mkdocstrings is what reads the docstrings.
GitHub Actions rebuilds and publishes the site on every push.

## What clicked

The thing that finally made sense was the *two layers*. I kept trying to
make my code comments do double duty as a learning journal, and the result
was always awful — either the code docs got chatty and useless as reference,
or the journal got sterile and useless as a journal. Keeping them physically
separate (different files, different folders, different tones) let both do
their job.

Module docstrings sit in the middle. At the top of each `.py` file I write
a short journal-style entry: why I wrote this, what I was trying to
understand, what I learned, what still confuses me. Then the functions
themselves get strict Google-style docstrings — `Args`, `Returns`, `Raises`,
maybe an `Example`. The module docstring is for me. The function docstrings
are for anyone (including me in six months) who needs to use the code.

## What confused me

Two things tripped me up.

First, the site layout feature `navigation.sections` does something different
from what its name suggests. It doesn't section off the nav by H2 headings
inside a page — it groups top-level nav entries that have children. I
wanted the former, flipped the setting, got confused, flipped it back.

Second, `mkdocstrings` couldn't find my module at first. The fix was
`pip install -e .` — installing my own package in editable mode, so that
`import learning` actually works. The `-e` means changes to the source
show up without reinstalling. This felt like magic until I realised it's
just a symlink in `site-packages`.

## What I'll do tomorrow

Write the next module. Probably something about functions and default
arguments — I have a vague sense that mutable default arguments are a
famous gotcha and I want to understand why before I get bitten. Write the
code, document it, push it, watch the site update. That's the loop now.

## See also

- [The example module](../reference/learning/example.md) — what the code
  side of this entry looks like.
- [MkDocs documentation](https://www.mkdocs.org/) — what I wish I'd read
  before Googling settings one at a time.
