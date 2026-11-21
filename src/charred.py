import gi

gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

def main():
	print("Charred app here!")

	if Atspi.init() != 0:
		print("Atspi was not initialised")

if __name__ == "__main__":
	main()