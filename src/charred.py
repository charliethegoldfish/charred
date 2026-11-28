import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from utilities_system import initialise_systems
# from utilities_application import get_applications
from charred_window import CharredWindow

def on_activate(app):
	window = CharredWindow(application=app)
	window.present()

def main():
	print("Charred app here!")

	app = Gtk.Application(application_id="com.charliethegoldfish.Charred")
	app.connect("activate", on_activate)

	try:
		initialise_systems()

		# apps = get_applications()
		# for app in apps:
		# 	print(f"{app.name} is running!")

		app.run(None)

	except Exception as e:
		# app.quit()
		print(f"Error running Charred: {e}")

	# focused_app = None
	# old_focused_app = None

	# while(True):
	# 	check_apps = get_applications()
	# 	for app in check_apps:
	# 		if app.has_focused_window():
	# 			focused_app = app

	# 	if focused_app == None:
	# 		continue

	# 	if old_focused_app == None or old_focused_app.name != focused_app.name:
	# 		old_focused_app = focused_app
	# 		print(f"{focused_app.name} has a focused window!")

if __name__ == "__main__":
	main()