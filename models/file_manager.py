import csv
import json

from .student import Student


class FileManager:
    """Se encarga de leer y escribir los archivos que contienen a los estudiantes"""
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_csv(self) -> list[Student]:
        """
        Lee al archivo .csv, es proceso por el paquete csv
        y retorna la lista de estudiantes que encontro en este archivo
        """
        try:
            students = []
            with open(self.file_path) as file:
                csv_reader = csv.reader(file)
                for line in csv_reader:
                    id, name, lastname = line
                    students.append(Student(id, name, lastname))
            return students
        except FileNotFoundError:
            raise FileNotFoundError(f"el archivo {self.file_path} no existe")

    def write_json(self, students: list[Student]):
        """Escribe una lista de estudiantes en un archivo json"""
        try:
            data = [student.to_dict() for student in students]
            json_content = json.dumps(data, ensure_ascii=False)
            json_file_path = self.file_path.replace(".csv", ".json")
            with open(json_file_path, mode="w") as file:
                file.write(json_content)
        except Exception as error:
            print(error)
            raise error
