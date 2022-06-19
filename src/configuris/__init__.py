import sys
from ._exceptions import IncorrectFiletypeError


class Configuris:
    _possible_filetypes = {"json", "yml", "toml"}
    data = {}

    def __init__(self, name="config", filepath="", filetype: str = "json"):
        self.name = name
        if filetype in self._possible_filetypes:
            self.filetype = filetype
        else:
            raise IncorrectFiletypeError(filetype)
        self.full_filename = f"{filepath}{self.name}.{self.filetype}"

        try:
            open(self.full_filename, "x")
        except FileExistsError:
            pass

    def init_file(self):
        try:
            open(self.full_filename, "x")
        except FileExistsError:
            pass

    def read_file(self):
        """Reads file and saves result into data property."""
        result = {}
        try:
            f = open(self.full_filename, "r")
            if self.filetype == "json":
                import json

                result = json.loads(f.read())
            elif self.filetype == "yml":
                import yaml

                result = yaml.safe_load(f)
            elif self.filetype == "toml":
                import tomli

                result = tomli.loads(f.read())
            f.close()
        except OSError as e:
            print(e, file=sys.stderr)

        self.data = result

    def write_file(self):
        """Writes data to a file specified by a property in object."""
        try:
            f = open(self.full_filename, "w")
            if self.filetype == "json":
                import json

                f.write(json.dumps(self.data))
            elif self.filetype == "yml":
                import yaml

                yaml.dump(self.data, f)
            elif self.filetype == "toml":
                import tomli_w

                f.write(tomli_w.dumps(self.data))

            f.close()
        except OSError as e:
            print(e, file=sys.stderr)
