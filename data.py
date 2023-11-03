import os
import json
from datetime import datetime


class DataManager:
    JSON_PATH = os.path.join(os.path.dirname(__file__), "data.json")
    MODIFY_SECRET_KEY = os.environ.get("MODIFY_SECRET_KEY")

    def __init__(
        self, status=False, date="", title="", message="", redirect="", **kwargs
    ):
        self.status = status
        self.date = date
        self.title = title
        self.message = message
        self.redirect = redirect
        for key, value in kwargs.items():
            setattr(self, key, value)

    def serialize(self):
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                self.__dict__[key] = value.strftime("%Y-%m-%d %H:%M:%S")
        return self.__dict__

    def _load_data(self):
        with open(self.JSON_PATH, "r") as f:
            return json.load(f)

    def _save_data(self):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = self._serialize()
        with open(self.JSON_PATH, "w") as f:
            json.dump(data, f, indent=4)

    def _update_data(self, key, value):
        setattr(self, key, value)
        self._save_data()

    def _delete_data(self, key):
        setattr(self, key, "")
        self._save_data()

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)

    @classmethod
    def from_file(cls):
        if not os.path.exists(cls.JSON_PATH):
            # Initialize file with default values if it doesn't exist
            instance = cls()
            instance._save_data()
        else:
            with open(cls.JSON_PATH, "r") as f:
                data = json.load(f)
            instance = cls.from_json(data)
        return instance

    def update_fields(self, **kwargs):
        for key, value in kwargs.items():
            self._update_data(key, value)
