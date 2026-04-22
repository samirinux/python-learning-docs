"""Getting started: my first documented module.

Why I wrote this:
    I wanted a throwaway module to prove the whole pipeline works -
    from writing a docstring here all the way through to seeing it
    rendered on the published docs site. If you are reading this on
    the website, the pipeline works.

What I learned setting this up:
    - Module docstrings go at the very top of a .py file, before any
      imports. They are the first string literal in the file.
    - Function docstrings live inside the function, right after the
      def line. mkdocstrings picks them up via the identifier
      `learning.example.<function_name>`.
    - Google-style docstrings use section headers like `Args:` and
      `Returns:`. They render as nicely formatted tables on the site.
    - Type hints (int, str, list[int]) appear in the rendered signature
      and save me from having to repeat types in the docstring.

Open questions:
    - What is the cleanest way to document a function that raises
      several different exceptions conditionally?
    - How do I cross-reference another function from inside a docstring?
"""
from __future__ import annotations


def greet(name: str) -> str:
    """Return a friendly greeting for the given name.

    This is the "hello world" of my learning journal - deliberately
    trivial so I can verify the whole toolchain without worrying about
    whether the code itself makes sense.

    Args:
        name: The person (or thing) to greet. Must be non-empty.

    Returns:
        A greeting of the form `"Hello, <name>!"`.

    Raises:
        ValueError: If `name` is empty or whitespace-only.

    Example:
        >>> greet("Ada")
        'Hello, Ada!'
    """
    if not name.strip():
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"


def chunked(items: list[int], size: int) -> list[list[int]]:
    """Split a list into consecutive chunks of a given size.

    The final chunk may be shorter if `len(items)` is not a multiple
    of `size`. I wrote this to practice slicing and to see how
    mkdocstrings renders a slightly more realistic docstring.

    Args:
        items: The list to split. Can be empty.
        size: Number of items per chunk. Must be positive.

    Returns:
        A list of lists. Empty if `items` is empty.

    Raises:
        ValueError: If `size` is not a positive integer.

    Example:
        >>> chunked([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> chunked([], 3)
        []
    """
    if size <= 0:
        raise ValueError("size must be positive")
    return [items[i : i + size] for i in range(0, len(items), size)]
