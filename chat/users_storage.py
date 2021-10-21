import json
import os


class JSONUsersStorage:

    def __init__(self, filename):
        self._filename = filename
        if not os.path.isfile(filename):
            self.clear()

    def add(self, username, password):
        users = self._load()
        users[username] = password
        self._dump(users)

    def exists(self, username):
        return username in self._load()

    def get_password(self, username):
        if self.exists(username):
            return self._load()[username]
        return None

    def clear(self):
        self._dump({})

    def _dump(self, obj):
        with open(self._filename, 'w') as file:
            json.dump(obj, file)

    def _load(self):
        with open(self._filename) as file:
            return json.load(file)
