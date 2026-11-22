from object_window import ObjectWindow

class ObjectApplication:
	def __init__(self, name: str, windows: list[ObjectWindow]):
		self.name = name
		self.windows = windows

	def has_focused_window(self):
		for window in self.windows:
			if window.is_focused():
				return True
		return False