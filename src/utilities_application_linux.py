import gi

gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

from object_application import ObjectApplication
from object_window import ObjectWindow

def get_all_applications() -> list[Atspi.Accessible]:
	desktop = Atspi.get_desktop(0)

	apps = []

	for i in range(desktop.get_child_count()):
		app = desktop.get_child_at_index(i)
		if not app:
			continue
		apps.append(app)
	
	return apps

def get_all_windows_for_app(app) -> list:
	windows = []

	for i in range(app.get_child_count()):
		window = app.get_child_at_index(i)
		if not window:
			continue

		windows.append(window)

	return windows

def get_application_objects() -> list[ObjectApplication]:
	app_objects = []
	
	apps = get_all_applications()

	for app in apps:
		name = app.get_name()
		windows = get_all_windows_for_app(app)
		window_objects = []

		for window in windows:
			window_name = window.get_name()
			window_object = ObjectWindow(window_name)
			window_objects.append(window_object)

		app_object = ObjectApplication(name, window_objects)
		app_objects.append(app_object)
	
	return app_objects