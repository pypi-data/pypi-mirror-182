import json

from remotemanager.serialisation.serial import serial


class serialjson(serial):
    """
    subclass of serial, implementing json methods
    """

    def dumps(self, obj):
        return json.dumps(obj)

    def loads(self, string):
        return json.loads(string)

    @property
    def callstring(self):
        return "json"
