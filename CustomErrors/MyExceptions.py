class PasswordError(Exception):
    def __init__(self, message) -> None:
        self.message=message
        super().__init__(self.message)

class EmailError(Exception):
    def __init__(self, message) -> None:
        self.message=message
        super().__init__(self.message)

class PhoneNumberError(Exception):
    def __init__(self,message) -> None:
        self.message=message
        super().__init__(self.message)

class IDError(Exception):
    def __init__(self,message) -> None:
        self.message=message
        super().__init__(self.message)

class AuthenticationError(Exception):
    def __init__(self,message) -> None:
        self.message=message
        super().__init__(self.message)

class RegisterError(Exception):
    def __init__(self,message) -> None:
        self.message=message
        super().__init__(self.message)

class LoginError(Exception):
    def __init__(self,message) -> None:
        self.message=message
        super().__init__(self.message)
