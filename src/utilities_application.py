from utilities_application_linux import get_application_objects
from object_application import ObjectApplication

def get_applications() -> list[ObjectApplication]:
	# TODO: Determine when we're on a linux platform?
	apps = get_application_objects()
	return apps
