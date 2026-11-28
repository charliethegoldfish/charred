import gi

gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

def initialise():
	if Atspi.init() != 0:
		raise RuntimeError("Atspi was not intialised!")

def shutdown():
	print("Shutting down atspi!")
	Atspi.exit()

