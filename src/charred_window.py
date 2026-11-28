import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from utilities_system import on_quit

class CharredWindow(Gtk.ApplicationWindow):
	def __init__(self, **kargs):
		super().__init__(**kargs, title="Charred")

		self.label = Gtk.Label(label="Hello World")
		self.set_child(self.label)
		self.connect("close-request", on_quit)
