from models.file_manager import FileManager

if __name__ == "__main__":
    try:
        filemanager = FileManager("xyz.csv")
        students = filemanager.read_csv()
        filemanager.write_json(students)

        print(f"Estudiantes obtenidos: {len(students)}")
    except Exception as error:
        print(error)
