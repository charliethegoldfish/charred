#!/bin/sh
python3 -m venv .venv --system-site-packages --prompt charred-venv
./.venv/bin/pip install -r requirements.txt