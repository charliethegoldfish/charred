from utilities_config import is_platform_linux, is_platform_macos, is_platform_windows, is_platform_supported, get_platform

if is_platform_linux:
	from utilities_system_linux import shutdown, initialise
elif is_platform_macos:
	from utilities_system_macos import shutdown, initialise
elif is_platform_windows:
	from utilities_system_windows import shutdown, initialise

def check_platform() -> bool:
	if not is_platform_supported():
		raise RuntimeError(f"Platform {get_platform()} is unsupported")
	return True

def initialise_systems():
	if check_platform():
		initialise()

def on_quit(window):
	if check_platform():
		shutdown()

