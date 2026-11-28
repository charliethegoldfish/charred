from event_manager import EventManager

class EventManagerLinux(EventManager):
	def __init__(self):
		super().__init__()

	def register_window_focus_event(self):
		pass

	def window_focus_callback(self):
		pass