from datetime import datetime
from src.models import Entry
from src.storage import load_entries, save_entries, get_next_id


def add_entry(content, tags=None):
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


def list_entries(filter_today=False, filter_tag=None):
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


def search_entries(query):
    entries = load_entries()
    result = []
    for entry in entries:
        if query.lower() in entry.content.lower():
            result.append(entry)
    return result


def delete_entry(entry_id):
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
