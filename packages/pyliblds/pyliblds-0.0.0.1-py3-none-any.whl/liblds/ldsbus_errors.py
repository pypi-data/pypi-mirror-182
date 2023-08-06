class LDSBusResponseError(ValueError):
    """
    Class for LDSBus Response Error
    """

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self) -> str:
        return self.message
