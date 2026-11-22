import sys

PLATFORM_LINUX = 'linux'
PLATFORM_WINDOWS = 'win32'
PLATFORM_MACOS = 'darwin'

def is_platform_linux() -> bool:
	return sys.platform == PLATFORM_LINUX

def is_platform_windows() -> bool:
	return sys.platform == PLATFORM_WINDOWS

def is_platform_macos() -> bool:
	return sys.platform == PLATFORM_MACOS