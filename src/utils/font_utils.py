import PyQt6.QtGui
import utils.resource_utils

font_utils_data: dict[str, str] = {}

def load_fonts():
    font_id = PyQt6.QtGui.QFontDatabase.addApplicationFont(utils.resource_utils.get_resource_path("Inter.ttf"))

    if font_id != -1:
        families = PyQt6.QtGui.QFontDatabase.applicationFontFamilies(font_id)
        font_family = families[0]

        font_utils_data["inter"] = font_family

def get_inter_font() -> str:
    return font_utils_data["inter"]