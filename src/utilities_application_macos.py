# TODO: Implement MacOS specific app grabbing logic

from AppKit import NSWorkspace
from object_application import ObjectApplication

def get_application_objects() -> list[ObjectApplication]:
	app_objects = []
	running_apps = NSWorkspace.sharedWorkspace().runningApplications()

	for app in running_apps:
		app_object = ObjectApplication(app.localizedName(), [])
		app_objects.append(app_object)
	
	return app_objects