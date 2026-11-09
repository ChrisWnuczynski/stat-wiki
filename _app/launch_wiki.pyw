"""Open the stat wiki in its own window.

Double-click this file, or the desktop shortcut that points at it. It serves
the built site (the _site folder) on this computer only, opens it in an Edge
app window, and stops when that window is closed.
"""

from __future__ import annotations

import ctypes
import functools
import http.server
import os
import socket
import subprocess
import threading
import urllib.request
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "_site"
PORT = 4150
TITLE = "stat wiki"
EDGE_PATHS = [
    Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Microsoft/Edge/Application/msedge.exe",
    Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Microsoft/Edge/Application/msedge.exe",
]
PROFILE = Path(os.environ.get("LOCALAPPDATA", Path.home())) / "stat-wiki" / "edge-profile"


def message(text: str) -> None:
    ctypes.windll.user32.MessageBoxW(None, text, TITLE, 0x40)


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    # pythonw has no console, so the default request log would fail.
    def log_message(self, *args) -> None:
        pass


def already_running(port: int) -> bool:
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/index.html", timeout=2) as reply:
            return b"stat wiki" in reply.read(4000)
    except OSError:
        return False


def start_server() -> tuple[http.server.ThreadingHTTPServer | None, int]:
    handler = functools.partial(QuietHandler, directory=str(SITE))
    for port in (PORT, 0):
        try:
            server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
        except OSError:
            if port == PORT and already_running(PORT):
                return None, PORT
            continue
        threading.Thread(target=server.serve_forever, daemon=True).start()
        return server, server.server_address[1]
    raise OSError("No free port for the wiki")


def open_window(url: str) -> subprocess.Popen | None:
    edge = next((path for path in EDGE_PATHS if path.exists()), None)
    if edge is None:
        return None
    PROFILE.mkdir(parents=True, exist_ok=True)
    return subprocess.Popen(
        [
            str(edge),
            f"--app={url}",
            f"--user-data-dir={PROFILE}",
            "--no-first-run",
            "--no-default-browser-check",
            "--window-size=1400,900",
        ]
    )


def wait_without_edge(url: str) -> None:
    """No Edge: use the default browser, with a small window to stop the wiki."""
    import tkinter as tk
    import webbrowser

    webbrowser.open(url)
    root = tk.Tk()
    root.title(TITLE)
    tk.Label(root, text="The wiki is open in your browser.\nClose this window to stop it.", padx=24, pady=16).pack()
    tk.Button(root, text="Stop the wiki", command=root.destroy).pack(pady=(0, 14))
    root.mainloop()


def main() -> None:
    if not (SITE / "index.html").exists():
        message(
            "The wiki has not been built yet.\n\n"
            "In the wiki folder, run:\n  python build_wiki.py\n  quarto render"
        )
        return
    server, port = start_server()
    url = f"http://127.0.0.1:{port}/index.html"
    window = open_window(url)
    if server is None:
        # Another copy is already serving; it stops when its windows close.
        if window is None:
            import webbrowser

            webbrowser.open(url)
        return
    try:
        if window is None:
            wait_without_edge(url)
        else:
            # Edge keeps this process alive while any window of the wiki profile is open.
            window.wait()
    finally:
        server.shutdown()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:  # Show the reason instead of failing silently.
        message(f"The wiki could not start:\n\n{error}")
