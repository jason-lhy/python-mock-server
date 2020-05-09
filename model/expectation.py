from enum import Enum
import json


class Expectation:
    def __init__(self, path: str, method: str, arguments: dict, response: dict = {}):
        self.path = path
        self.method = method
        self.arguments = arguments
        self.response = response

    def toJson(self):
        return json.dumps(self.__dict__)
