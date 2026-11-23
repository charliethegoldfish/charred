#!/bin/sh

UNAME=$(uname)

if [ "$UNAME" == "Darwin" ] ; then
	python3.14 -m venv .venv --system-site-packages --prompt charred-venv
	./.venv/bin/pip install -r requirements_macOS.txt
else
	python3 -m venv .venv --system-site-packages --prompt charred-venv
	./.venv/bin/pip install -r requirements.txt
fi