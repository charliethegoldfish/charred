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

def is_platform_supported() -> bool:
	return is_platform_linux() or is_platform_macos() or is_platform_windows()

def get_platform() -> str:
	return sys.platform