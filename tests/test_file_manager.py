import json
from unittest import TestCase

from models.file_manager import FileManager


class TestFileManager(TestCase):
    def test_read_csv_correct_file_path(self):
        filemanager = FileManager("estudiantes.csv")
        students = filemanager.read_csv()
        self.assertEqual(len(students), 4)

    def test_write_json_correct_content(self):
        filemanager = FileManager("estudiantes.csv")
        students = filemanager.read_csv()
        expected_result = json.dumps(
            [student.to_dict() for student in students], ensure_ascii=False
        )

        filemanager.write_json(students)
        with open("estudiantes.json") as file:
            content = file.read()
            self.assertEqual(content, expected_result)

    def test_read_csv_incorrect_file_path(self):
        filemanager = FileManager("xyz.csv")
        with self.assertRaisesRegex(FileNotFoundError, "el archivo xyz.csv no existe"):
            filemanager.read_csv()
