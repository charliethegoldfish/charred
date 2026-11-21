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

if __name__ == "__main__":
	main()