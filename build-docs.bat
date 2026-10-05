@echo off
rem Windows: double-click this file in File Explorer to rebuild the documentation and open it
rem in the browser. On macOS or Linux, use build-docs.command instead.
rem Requires Python 3 (https://www.python.org/downloads/), with "Add python.exe to PATH" ticked.
rem The first run installs Sphinx and its extensions, which can take several minutes.

setlocal
set PORT=8765
if defined DOCS_PORT set PORT=%DOCS_PORT%
rem Page to open, e.g. rUWWTD2024/SpatialPoints/ ; empty opens the home page
set PAGE=
set URL=http://127.0.0.1:%PORT%/%PAGE%

cd /d "%~dp0"

set PY=python
where python >nul 2>&1 || set PY=py -3

if not exist ".venv\Scripts\sphinx-build.exe" (
  echo First run: installing Sphinx and its extensions...
  %PY% -m venv .venv || goto install_failed
  ".venv\Scripts\python.exe" -m pip install -q -r docs\requirements.txt || goto install_failed
)

echo Building the documentation...
".venv\Scripts\sphinx-build.exe" -q -b html docs _build\html || goto build_failed

rem Never stop another program: if the port is taken, say so and stop here
".venv\Scripts\python.exe" -c "import socket,sys; s=socket.socket(); sys.exit(s.connect_ex(('127.0.0.1', int(sys.argv[1]))) == 0)" %PORT% 2>nul
if errorlevel 1 goto port_in_use

rem Serve the build in a minimised window; closing that window stops the server
start "Documentation server" /min ".venv\Scripts\python.exe" -m http.server %PORT% --bind 127.0.0.1 --directory _build\html

rem Wait up to ten seconds for the server to answer
".venv\Scripts\python.exe" -c "exec('import sys,time,urllib.request as u\nfor i in range(20):\n try:\n  u.urlopen(sys.argv[1], timeout=1); sys.exit(0)\n except u.HTTPError:\n  sys.exit(0)\n except OSError:\n  time.sleep(0.5)\nsys.exit(1)')" http://127.0.0.1:%PORT%/
if errorlevel 1 goto server_failed

start "" "%URL%"
echo Done. The documentation is at %URL%
echo Close the "Documentation server" window to stop the server.
timeout /t 5 >nul
exit /b 0

:install_failed
echo Installation failed. Check that Python 3 is installed and on the PATH.
pause
exit /b 1

:build_failed
echo The build failed; see the messages above.
pause
exit /b 1

:port_in_use
echo The build is in _build\html, but port %PORT% is already in use, so no server was started.
echo If the documentation server from an earlier run is still open, reload %URL% in the browser.
echo Otherwise, close the program using port %PORT%, or set DOCS_PORT to a free port and run again.
pause
exit /b 1

:server_failed
echo The documentation server did not start on port %PORT%.
pause
exit /b 1
