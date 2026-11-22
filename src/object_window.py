from enum import Enum

class WindowState(Enum):
	DEFAULT = "default"
	FOCUSED = "focused"

class ObjectWindow:
	def __init__(self, name: str):
		self.name = name
		self.state = WindowState.DEFAULT

	def set_state_focused(self):
		self.state = WindowState.FOCUSED

	def set_state_lose_focus(self):
		self.state = WindowState.DEFAULT

	def is_focused(self):
		return self.state == WindowState.FOCUSED