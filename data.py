import os
import json
from datetime import datetime


class DataManager:
    JSON_PATH = os.path.join(os.path.dirname(__file__), "data.json")
    MODIFY_SECRET_KEY = os.environ.get("MODIFY_SECRET_KEY")

    def __init__(self, status=False, date="", title="", message="", redirect=""):
        self.status = status
        self.date = date
        self.title = title
        self.message = message
        self.redirect = redirect

    def _load_data(self):
        with open(self.JSON_PATH, "r") as f:
            return json.load(f)

    def _save_data(self):
        data = {
            "status": self.status,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "title": self.title,
            "message": self.message,
            "redirect": self.redirect,
        }
        with open(self.JSON_PATH, "w") as f:
            json.dump(data, f)

    def update_data(self, key, value):
        setattr(self, key, value)
        self._save_data()

    def delete_data(self, key):
        setattr(self, key, "")
        self._save_data()

    @classmethod
    def from_json(cls, json_data):
        if cls.test_json(json_data):
            return cls(**json_data)
        else:
            raise ValueError("Invalid JSON data")

    @classmethod
    def load_from_file(cls):
        if not os.path.exists(cls.JSON_PATH):
            # Initialize file with default values if it doesn't exist
            instance = cls()
            instance._save_data()
        else:
            with open(cls.JSON_PATH, "r") as f:
                data = json.load(f)
            instance = cls.from_json(data)
        return instance

    @staticmethod
    def test_json(payload):
        required_keys = ["status", "date", "title", "message", "redirect"]
        return all(key in payload and payload[key] is not None for key in required_keys)

    def record_modified_time(self):
        self.update_data("date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
