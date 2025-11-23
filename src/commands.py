"""Command implementations for til-cli."""
from datetime import datetime
from src.models import Entry
from src.storage import load_entries, save_entries, get_next_id


def add_entry(content: str, tags: list[str] | None = None) -> Entry:
    """Add a new TIL entry.

    Args:
        content: The learning note to save.
        tags: Optional list of category tags.

    Returns:
        The newly created Entry with assigned ID.
    """
    if tags is None:
        tags = []
    entry = Entry(
        id=get_next_id(),
        content=content,
        tags=tags,
        created_at=datetime.now()
    )
    entries = load_entries()
    entries.append(entry)
    save_entries(entries)
    return entry


def list_entries(filter_today: bool = False, filter_tag: str | None = None) -> list[Entry]:
    """List TIL entries with optional filters.

    Args:
        filter_today: If True, show only today's entries.
        filter_tag: If provided, filter by this tag.

    Returns:
        List of Entry objects matching the filters.
    """
    entries = load_entries()
    result = []
    for entry in entries:
        if filter_today:
            if entry.created_at.date() == datetime.now().date():
                if filter_tag:
                    if filter_tag in entry.tags:
                        result.append(entry)
                else:
                    result.append(entry)
        else:
            if filter_tag:
                if filter_tag in entry.tags:
                    result.append(entry)
            else:
                result.append(entry)
    return result


def search_entries(query: str) -> list[Entry]:
    """Search entries by content.

    Args:
        query: Text to search for (case-insensitive).

    Returns:
        List of Entry objects containing the query string.
    """
    entries = load_entries()
    result = []
    for entry in entries:
        if query.lower() in entry.content.lower():
            result.append(entry)
    return result


def delete_entry(entry_id: int) -> bool:
    """Delete an entry by ID.

    Args:
        entry_id: The ID of the entry to delete.

    Returns:
        True if the entry was found and deleted, False otherwise.
    """
    entries = load_entries()
    new_entries = []
    deleted = False
    for entry in entries:
        if entry.id == entry_id:
            deleted = True
        else:
            new_entries.append(entry)
    if deleted:
        save_entries(new_entries)
    return deleted
