import sys
import os

def get_resource_path(path: str) -> str:
    try:
        base_path = sys._MEIPASS # type: ignore
    except Exception: 
        base_path = os.path.abspath("resources/")
    return os.path.join(base_path, path)