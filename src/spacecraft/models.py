from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


class TaskType(Enum):
    """Enumeration for spacecraft task types."""
    CONTACT = auto()
    OBSERVATION = auto()
    DOWNLINK = auto()


@dataclass
class Window:
    """Represents a time window for a specific task type."""
    start_time: datetime
    end_time: datetime
    window_type: TaskType

    def duration(self) -> float:
        """Returns the duration of the window in seconds."""
        return (self.end_time - self.start_time).total_seconds()


@dataclass
class Task:
    """
    Represents a scheduled spacecraft task.
    In Week 1, this maps 1:1 with a Window, but represents an assigned/locked action.
    """
    task_id: str
    target: str
    start_time: datetime
    end_time: datetime
    task_type: TaskType
    priority: int = 1  # 1 is highest priority

    def duration(self) -> float:
        return (self.end_time - self.start_time).total_seconds()


@dataclass
class ConstraintViolation:
    """Represents a schedule constraint violation."""
    constraint_name: str
    description: str
    time_of_violation: datetime | None = None
