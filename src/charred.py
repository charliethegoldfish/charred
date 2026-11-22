import gi

gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

from utilities_application import get_applications

def main():
	print("Charred app here!")

	# TODO: Only do this on linux platforms?
	if Atspi.init() != 0:
		print("Atspi was not initialised")

	apps = get_applications()
	for app in apps:
		print(f"{app.name} is running!")

	focused_app = None
	old_focused_app = None

	while(True):
		check_apps = get_applications()
		for app in check_apps:
			if app.has_focused_window():
				focused_app = app

		if focused_app == None:
			continue

		if old_focused_app == None or old_focused_app.name != focused_app.name:
			old_focused_app = focused_app
			print(f"{focused_app.name} has a focused window!")

if __name__ == "__main__":
	main()