from object_window import ObjectWindow

class ObjectApplication:
	def __init__(self, name: str, windows: list[ObjectWindow]):
		self.name = name
		self.windows = windows