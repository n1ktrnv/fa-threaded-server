import json
import os
from abc import ABC, abstractmethod


class UsersStorage(ABC):

    @abstractmethod
    def add(self, ip, username, password):
        pass

    @abstractmethod
    def exists(self, ip):
        pass

    @abstractmethod
    def get_field(self, ip, field):
        pass

    @abstractmethod
    def set_field(self, ip, field, value):
        pass

    @abstractmethod
    def clear(self):
        pass


class JSONUsersStorage(UsersStorage):

    def __init__(self, filename):
        self._filename = filename
        if not os.path.isfile(filename):
            self.clear()

    def add(self, ip, username=None, password=None):
        users = self._load()
        users[ip] = {
            'username': username,
            'password': password,
            'token': None
        }
        self._dump(users)

    def exists(self, ip):
        return ip in self._load()

    def get_field(self, ip, field):
        if self.exists(ip):
            return self._load()[ip][field]
        return None

    def set_field(self, ip, field, value):
        users = self._load()
        users[ip][field] = value
        self._dump(users)

    def clear(self):
        self._dump({})

    def _dump(self, obj):
        with open(self._filename, 'w') as file:
            json.dump(obj, file)

    def _load(self):
        with open(self._filename) as file:
            return json.load(file)
