import sqlite3

# this is same as cohorts.py but using lamda

#trying to display all cohorts
class Cohort():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class Cohort_Names():

    def __init__(self):
        self.db_path = "/Users/kgallegos/workspace/python/sql/StudentExercises/studentexercises.db"

    def all_cohorts(self):

        """Retrieve list of all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name
            from Cohort c
            """)

            all_cohorts = db_cursor.fetchall()


            for cohort in all_cohorts:
                print(cohort)

                # print("\nCohorts: \n")
                # [print(f'  * {c}') for c in all_cohorts]


cohorts = Cohort_Names()
cohorts.all_cohorts()

