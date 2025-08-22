class ConversionError(Exception):
    def __init__(self, from_unit, to_unit, message="Those two units are not convertible"):
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Got {self.from_unit} & {self.to_unit}"