import sqlite3
#joint tables
# List all exercises assigned by each instructor. Display each instructor name and the exercises s/he has assigned beneath their name. Use a dictionary to track each instructor. Remember that the key should be the instructor id and the value should be the entire instructor object.

class Instructor_Workload:

    def __init__(self):
        self.db_path = "/Users/kgallegos/workspace/python/sql/StudentExercises/studentexercises.db"

    def multi_join(self):


        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    i.Id,
                    i.FirstName,
                    i.LastName
                from Exercise e
                join StudentExercises se on se.ExerciseId = e.Id
                join Instructor i on i.Id = se.StudentId
            """)

        dataset = db_cursor.fetchall()

        x = dict()
        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            instructor_id = row[2]
            instructor_name = f'{row[3]} {row[4]}'

            if instructor_name not in x:
                x[instructor_name] = [exercise_name]
            else:
                x[instructor_name].append(exercise_name)

# print(exercises)

        for instructor_name, exercises in x.items():
            print(f'{instructor_name} has assigned:')
            for exercise in exercises:
                print(f'\t* {exercise}')

exercise = Instructor_Workload()
exercise.multi_join()


















