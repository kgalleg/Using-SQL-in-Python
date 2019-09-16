import sqlite3

#trying to display all cohorts
class Cohort():

    def __init__(self, name):
        self.name = name


class cohortnames():

    """Methods for reports on the cohorts database"""

    def create_cohort(self, cursor, row):
        return Cohort(row[1])


    def __init__(self):
        self.db_path = "/Users/kgallegos/workspace/python/sql/StudentExercises/studentexercises.db"

    def all_cohorts(self):

        """Retrieve list of all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_cohort

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name
            from Cohort c
            """)

            all_cohorts = db_cursor.fetchall()


            for cohort in all_cohorts:
                print(f'Name: {cohort.name}')


cohorts = cohortnames()
cohorts.all_cohorts()
