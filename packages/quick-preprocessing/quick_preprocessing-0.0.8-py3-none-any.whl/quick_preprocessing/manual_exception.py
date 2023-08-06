class InvalidListException(Exception):
    def __init__(self, message: str="invalid list exception"):
        self.message = message 
        super().__init__(self.message)
