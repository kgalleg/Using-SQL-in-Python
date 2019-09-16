import sqlite3


class ExerciseLanguage:

    def __init__(self, language):
        self.language = language

    def __repr__(self):
        return f'{self.language}'


class PythonExercises():

    """Methods for reports on the Student Exercises database"""

    def create_py_exercise(self, cursor, row):
        return ExerciseLanguage(row[0])


    def __init__(self):
        self.db_path = "/Users/kgallegos/workspace/python/sql/StudentExercises/studentexercises.db"

    def py_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_py_exercise

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Language
            from Exercise e
            where e.Language = "PYTHON"
            """)

            py_exercises = db_cursor.fetchall()



        for pyexercise in py_exercises:
            print(pyexercise)



list_of_python_exercises = PythonExercises()
list_of_python_exercises.py_exercises()
































