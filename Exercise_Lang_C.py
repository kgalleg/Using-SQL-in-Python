import sqlite3


class CSharpLanguage:

    def __init__(self, language):
        self.language = language

    def __repr__(self):
        return f'{self.language}'


class CSharpExercises():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/kgallegos/workspace/python/sql/StudentExercises/studentexercises.db"

    def CSharp_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = conn.row_factory = lambda cursor, row: CSharpLanguage(
        row[0]
        )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Language
            from Exercise e
            where e.Language = "C#"
            """)

            CSharp_exercises = db_cursor.fetchall()



        for CSharpexercise in CSharp_exercises:
            print(CSharpexercise)



list_of_CSharp_exercises = CSharpExercises()
list_of_CSharp_exercises.CSharp_exercises()



































