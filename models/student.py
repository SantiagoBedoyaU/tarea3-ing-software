class Student:
    def __init__(self, id: str, name: str, lastname: str) -> None:
        self.id = id
        self.name = name
        self.lastname = lastname

    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "nombre": self.name,
            "apellido": self.lastname,
        }
