"""Data models for til-cli."""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Entry:
    """A single TIL (Today I Learned) entry.

    Represents a learning note with content, optional tags,
    and automatic timestamp.

    Attributes:
        id: Unique identifier for the entry.
        content: The learning note text.
        tags: Optional list of category tags.
        created_at: Timestamp when entry was created.

    Example:
        >>> entry = Entry(
        ...     id=1,
        ...     content="Python f-strings are faster than .format()",
        ...     tags=["python", "performance"]
        ... )
    """
    id: int
    content: str
    tags: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        """Convert entry to dictionary for JSON serialization.

        Returns:
            Dictionary with all entry fields, datetime as ISO string.
        """
        return {
            "id": self.id,
            "content": self.content,
            "tags": self.tags,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Entry":
        """Create an Entry instance from a dictionary.

        Args:
            data: Dictionary containing entry fields.

        Returns:
            New Entry instance populated from the dictionary.
        """
        return cls(
            id=data["id"],
            content=data["content"],
            tags=data.get("tags", []),
            created_at=datetime.fromisoformat(data["created_at"])
        )
