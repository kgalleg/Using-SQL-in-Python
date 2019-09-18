import sqlite3


class Exercise:

    def __init__(self, id, name, language):
        self.id = id
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.id}. {self.name} - {self.language}'


class ExerciseNames():

    """Methods for reports on the Student Exercises database"""

    def create_exercise(self, cursor, row):
        return Exercise(row[0], row[1], row[2])


    def __init__(self):
        self.db_path = "/Users/kgallegos/workspace/python/sql/StudentExercises/studentexercises.db"

    def all_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_exercise

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.Language
            from Exercise e
            """)

            all_exercises = db_cursor.fetchall()



        for exercise in all_exercises:
            print(exercise)



list_of_exercises = ExerciseNames()
list_of_exercises.all_exercises()

























