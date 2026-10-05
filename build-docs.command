#!/bin/bash
# Double-click in Finder to rebuild the documentation and open it in the browser.
# The first run installs Sphinx and its extensions, which can take several minutes.

PORT=8765
PAGE=""   # page to open, e.g. "rUWWTD2024/SpatialPoints/"; empty opens the home page

cd "$(dirname "$0")" || exit 1

if [ ! -x .venv/bin/sphinx-build ]; then
  echo "First run: installing Sphinx and its extensions..."
  python3 -m venv .venv && .venv/bin/pip install -q -r docs/requirements.txt || {
    echo "Installation failed."; read -r -p "Press Enter to close."; exit 1; }
fi

echo "Building the documentation..."
if ! .venv/bin/sphinx-build -q -b html docs _build/html; then
  echo "The build failed; see the messages above."
  read -r -p "Press Enter to close."
  exit 1
fi

# Restart the local web server so it serves this build
lsof -ti:"$PORT" | xargs kill 2>/dev/null
(cd _build/html && nohup python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 &)
sleep 1

open "http://127.0.0.1:$PORT/$PAGE"
echo "Done. The documentation is at http://127.0.0.1:$PORT/$PAGE"
