import json
from pathlib import Path
from src.models import Entry


DATA_DIR = Path.home() / ".til"
DATA_FILE = DATA_DIR / "entries.json"


def ensure_data_dir():
    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_entries():
    ensure_data_dir()
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return [Entry.from_dict(e) for e in data]


def save_entries(entries):
    ensure_data_dir()
    data = [e.to_dict() for e in entries]
    DATA_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def get_next_id():
    entries = load_entries()
    if not entries:
        return 1
    return max(e.id for e in entries) + 1
