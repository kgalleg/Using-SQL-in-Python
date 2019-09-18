import sqlite3
#joint tables

class DatasetToDict:

    def __init__(self):
        self.db_path = "/Users/kgallegos/workspace/python/sql/StudentExercises/studentexercises.db"

    def multi_join(self):

        exercises = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    s.Id,
                    s.FirstName,
                    s.LastName
                from Exercise e
                join StudentExercises se on se.ExerciseId = e.Id
                join Student s on s.Id = se.StudentId
            """)

        dataset = db_cursor.fetchall()


        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'

            if exercise_name not in exercises:
                exercises[exercise_name] = [student_name]
            else:
                exercises[exercise_name].append(student_name)

# print(exercises)

        for exercise_name, students in exercises.items():
            print(exercise_name)
            for student in students:
                print(f'\t* {student}')

exercise = DatasetToDict()
exercise.multi_join()















