import json
import os

SETTINGS_FILE = "settings.json"


def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as file:
            return json.load(file)

    default_settings = {
        "snake_color": [0, 255, 0],
        "grid": True
    }

    save_settings(default_settings)
    return default_settings


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)