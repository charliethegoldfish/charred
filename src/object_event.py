from enum import Enum

class EventType(Enum):
	IGNORE = "ignore"
	WINDOW_FOCUS_CHANGED = "window_focus_changed"

class ObjectEvent:
	def __init__(self, event_type: EventType):
		self.event_type = event_type