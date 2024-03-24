import json
from unittest import TestCase

from models.student import Student


class TestStudent(TestCase):
    def test_student_to_dict(self):
        student = Student("1", "Santiago", "Bedoya")
        expected = json.dumps({"id": "1", "nombre": "Santiago", "apellido": "Bedoya"})
        result = json.dumps(student.to_dict())
        self.assertEqual(expected, result)
