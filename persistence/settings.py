import json
import os

import platformdirs

__file_path = platformdirs.user_data_dir("WorldTopicSearch", "settings.json")
__settings = None

if __settings is None:
    if os.path.exists(__file_path):
        with open(__file_path) as file:
            __settings = json.load(file)
    __settings = {}

def topic():
    return __settings.get("topic", "")

def topic(value: str):
    __settings["topic"] = value

def save():
    with open(__file_path, "w") as file:
        json.dumps(__settings, fp=file, indent=4)
