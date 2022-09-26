class User:
    """python class user that stores data."""

    def __init__(self, person_id, name, address, phone, email):
        self.person_id = person_id
        self.name = name
        self.adress = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return self.short_string()

    def short_string(self) -> str:
        """function to return name as string"""
        return f" name {self.name}"
