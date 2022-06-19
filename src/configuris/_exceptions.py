class IncorrectFiletypeError(Exception):
    """Exception class that should be raised when Configuris class was given an incorrect filetype property."""

    def __init__(self, filetype: str):
        self.message = (
            f'Incorrect file type given. Got {filetype}, need "json", "yml" or "toml".'
        )
        super().__init__(self.message)
