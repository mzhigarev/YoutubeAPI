"""Utility functions for working with YouTube API responses."""
from typing import List, Dict, Any


def get_titles(response: Dict[str, Any]) -> List[str]:
    """Return a list of lowercase video titles from a search response.

    Parameters
    ----------
    response : dict
        Dictionary representing a YouTube search API response.

    Returns
    -------
    list of str
        Titles converted to lowercase. Missing ``nextPageToken`` keys are
        ignored gracefully.
    """
    # Ensure ``items`` key exists
    items = response.get("items", [])
    titles = []
    for item in items:
        snippet = item.get("snippet", {})
        title = snippet.get("title")
        if title is not None:
            titles.append(title.lower())

    # Access ``nextPageToken`` with ``get`` so it doesn't raise ``KeyError``
    _ = response.get("nextPageToken")

    return titles
