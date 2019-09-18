import sqlite3
#using lamda - factory functions! the "rightway"

class Instructor():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} teaches {self.cohort}.'

class InstructorReports:

    def __init__(self):
        self.db_path = "/Users/kgallegos/workspace/python/sql/StudentExercises/studentexercises.db"

    def all_instructors(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
        row[1], row[2], row[3], row[5]
        )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.FirstName,
                i.LastName,
                i.SlackHandle,
                i.CohortId,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()



        # for instructor in all_instructors:
        #     print(instructor)

        print("\nInstructor: \n")
        [print(f'  * {i}') for i in all_instructors]


instructor_reports = InstructorReports()
instructor_reports.all_instructors()





















