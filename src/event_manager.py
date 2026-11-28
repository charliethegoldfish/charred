
class EventManager:
	def __init__(self):
		pass

	# TODO: Implement this for platform specific functionality
	def register_window_focus_event(self):
		raise NotImplementedError("Requires platform specific implementation")

	# TODO: Implement this for platform specific functionality
	def window_focus_callback(self):
		raise NotImplementedError("Requires platform specific implementation")

	# TODO: Implement this for general functionality
	def window_focus_changed(self):
		pass