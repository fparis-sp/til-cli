from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Entry:
    id: int
    content: str
    tags: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "content": self.content,
            "tags": self.tags,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Entry":
        return cls(
            id=data["id"],
            content=data["content"],
            tags=data.get("tags", []),
            created_at=datetime.fromisoformat(data["created_at"])
        )
