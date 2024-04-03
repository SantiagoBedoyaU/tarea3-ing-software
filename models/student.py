class Student:
    """Encargada de la estructura de la informacion de un estudiante"""
    def __init__(self, id: str, name: str, lastname: str) -> None:
        self.id = id
        self.name = name
        self.lastname = lastname

    def to_dict(self) -> dict[str, str]:
        """Retorna la informacion de un estudiante en forma de un diccionario"""
        return {
            "id": self.id,
            "nombre": self.name,
            "apellido": self.lastname,
        }
