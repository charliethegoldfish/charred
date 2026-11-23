from object_event import EventType, ObjectEvent



def event_is_focus_change(event: ObjectEvent):
	return event.event_type == EventType.WINDOW_FOCUS_CHANGED

def event_is_ignorable(event: ObjectEvent):
	return event.event_type == EventType.IGNORE

def handle_event(event: ObjectEvent):
	pass

def setup_event_listener():
	pass