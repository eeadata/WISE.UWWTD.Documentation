#!/bin/bash
# macOS and Linux: rebuilds the documentation and opens it in the browser.
#   macOS: double-click this file in Finder.
#   Linux: run ./build-docs.command in a terminal.
# On Windows, use build-docs.bat instead.
# The first run installs Sphinx and its extensions, which can take several minutes.

PORT="${DOCS_PORT:-8765}"   # set DOCS_PORT to use another port
PAGE=""   # page to open, e.g. "rUWWTD2024/SpatialPoints/"; empty opens the home page
URL="http://127.0.0.1:$PORT/$PAGE"

cd "$(dirname "$0")" || exit 1

fail() {
  echo "$1"
  read -r -p "Press Enter to close."
  exit 1
}

if [ ! -x .venv/bin/sphinx-build ]; then
  echo "First run: installing Sphinx and its extensions..."
  python3 -m venv .venv && .venv/bin/pip install -q -r docs/requirements.txt ||
    fail "Installation failed."
fi

echo "Building the documentation..."
.venv/bin/sphinx-build -q -b html docs _build/html ||
  fail "The build failed; see the messages above."

# Never stop another program: if the port is taken, say so and stop here
if .venv/bin/python -c "import socket,sys; s=socket.socket(); sys.exit(s.connect_ex(('127.0.0.1', int(sys.argv[1]))) != 0)" "$PORT" 2>/dev/null; then
  fail "The build is in _build/html, but port $PORT is already in use, so no server was started.
If the documentation server from an earlier run is still open, reload $URL in the browser.
Otherwise, close the program using port $PORT, or run again with DOCS_PORT set to a free port."
fi

nohup .venv/bin/python -m http.server "$PORT" --bind 127.0.0.1 --directory _build/html \
  >/dev/null 2>&1 &
SERVER_PID=$!

# Wait up to ten seconds for this server to answer
if ! .venv/bin/python -c "exec('import sys,time,urllib.request as u\nfor i in range(20):\n try:\n  u.urlopen(sys.argv[1], timeout=1); sys.exit(0)\n except u.HTTPError:\n  sys.exit(0)\n except OSError:\n  time.sleep(0.5)\nsys.exit(1)')" "http://127.0.0.1:$PORT/" ||
   ! kill -0 "$SERVER_PID" 2>/dev/null; then
  kill "$SERVER_PID" 2>/dev/null
  fail "The documentation server did not start on port $PORT."
fi

if command -v open >/dev/null; then
  open "$URL"      # macOS
elif command -v xdg-open >/dev/null; then
  xdg-open "$URL"  # Linux
fi
echo "Done. The documentation is at $URL"
echo "The server keeps running in the background (process $SERVER_PID)."
