from config import State

class StateController:
	def __init__(self):
		self._current_state = State.IDLE
		self._current_focused_app = None

	def get_state(self) -> State:
		return self._current_state

	def update_focused_app(self, focused_app: str|None):
		self._current_focused_app = focused_app
		self.update_state()

	def update_state(self):
		if self._current_focused_app != None:
			if self.is_focused_app():
				self._current_state = State.CONFIGURE
			else:
				self._current_state = State.DISPLAY
		else:
			self._current_state = State.IDLE

	def is_focused_app(self):
		# TODO: Implement check to see if we are the focused app
		return False