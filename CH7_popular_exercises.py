import sqlite3
#joint tables
# Output a report in your terminal that lists all students and the exerices each is assigned. Use a dictionary to track each exercise. Remember that the key should be the exercise id and the value should be the entire exercise object.

class Popular_Exercises:

    def __init__(self):
        self.db_path = "/Users/kgallegos/workspace/python/sql/StudentExercises/studentexercises.db"

    def multi_join(self):


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

        x = dict()
        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'

            if exercise_name not in x:
                x[exercise_name] = [student_name]
            else:
                x[exercise_name].append(student_name)

# print(exercises)

        for exercise_name, students in x.items():
            print(f'{exercise_name} is being worked on by:')
            for student in students:
                print(f'\t* {student}')

exercise = Popular_Exercises()
exercise.multi_join()


















