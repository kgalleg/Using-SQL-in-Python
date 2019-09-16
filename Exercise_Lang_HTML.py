import sqlite3


class HTMLLanguage:

    def __init__(self, language):
        self.language = language

    def __repr__(self):
        return f'{self.language}'


class HTMLExercises():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/kgallegos/workspace/python/sql/StudentExercises/studentexercises.db"

    def HTML_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = conn.row_factory = lambda cursor, row: HTMLLanguage(
        row[0]
        )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Language
            from Exercise e
            where e.Language = "HTML"
            """)

            html_exercises = db_cursor.fetchall()



        for htmlexercise in html_exercises:
            print(htmlexercise)



list_of_HTML_exercises = HTMLExercises()
list_of_HTML_exercises.HTML_exercises()

































