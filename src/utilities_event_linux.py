import gi

gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

def handle_event_linux(event: Atspi.Event) -> None:
	pass

def setup_event_listener_platform(handle_func: callable):
	pass