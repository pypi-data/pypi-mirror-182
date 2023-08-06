import yaml

from remotemanager.utils import ensure_filetype
from remotemanager.serialisation.serial import serial


class serialyaml(serial):
    """
    subclass of serial, implementing yaml methods
    """

    def dumps(self, obj):
        return yaml.dump(obj)

    def loads(self, string):
        return yaml.safe_load(string)

    @property
    def callstring(self):
        return "yaml"

    @property
    def loadstring(self) -> str:
        return "safe_load"

    def dumpfunc(self) -> str:
        lines = ['\ndef dump(obj, file):',
                 f'\t{self.importstring}',
                 f'\tif isinstance(obj, (set, tuple)):',
                 f'\t\tobj = list(obj)',
                 f'\tif not file.endswith("{self.extension}"):',
                 f'\t\tfile = file + "{self.extension}"',
                 f'\twith open(file, "{self.write_mode}") as o:',
                 f'\t\t{self.callstring}.{self.dumpstring}(obj, o)']

        return '\n'.join(lines)
