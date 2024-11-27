from enum import Enum


class TodoStatus(str, Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    DONE = "Done"
    CLOSED = "Closed"
    CANCELLED = "Cancelled"
