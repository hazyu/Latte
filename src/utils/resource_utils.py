import sys
import os

def resource_path(path: str) -> str:
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("resources/")
    return os.path.join(base_path, path)