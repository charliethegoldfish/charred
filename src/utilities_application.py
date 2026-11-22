from utilities_system import is_platform_linux, is_platform_macos, is_platform_windows

if is_platform_linux():
	from utilities_application_linux import get_application_objects
elif is_platform_macos():
	from utilities_application_macos import get_application_objects
elif is_platform_windows():
	from utilities_application_windows import get_application_objects
else:
	raise RuntimeError("Unsupported Platform")

from object_application import ObjectApplication

def get_applications() -> list[ObjectApplication]:
	apps = get_application_objects()
	return apps
