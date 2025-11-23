"""Storage functions for til-cli entries."""
import json
from pathlib import Path
from src.models import Entry


DATA_DIR = Path.home() / ".til"
DATA_FILE = DATA_DIR / "entries.json"


def ensure_data_dir():
    """Create the data directory if it doesn't exist.

    Creates ~/.til/ directory and initializes an empty entries.json
    file if they don't already exist.
    """
    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_entries() -> list[Entry]:
    """Load all entries from the JSON file.

    Returns:
        List of Entry objects. Empty list if no entries exist.
    """
    ensure_data_dir()
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return [Entry.from_dict(e) for e in data]


def save_entries(entries: list[Entry]):
    """Save all entries to the JSON file.

    Args:
        entries: List of Entry objects to persist.
    """
    ensure_data_dir()
    data = [e.to_dict() for e in entries]
    DATA_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def get_next_id() -> int:
    """Calculate the next available entry ID.

    Returns:
        The next sequential ID (max existing ID + 1, or 1 if no entries).
    """
    entries = load_entries()
    if not entries:
        return 1
    return max(e.id for e in entries) + 1
