#!/bin/sh

UNAME=$(uname)

if [ "$UNAME" == "Darwin" ] ; then
	python3.14 src/charred.py
else
	python3 src/charred.py
fi