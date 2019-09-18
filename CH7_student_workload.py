import sqlite3
#joint tables
# List the exercises assigned to each student. Display each student name and the exercises s/he has been assigned beneath their name. Use a dictionary to track each student. Remember that the key should be the student id and the value should be the entire student object.

class Student_Workload:

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

            if student_name not in x:
                x[student_name] = [exercise_name]
            else:
                x[student_name].append(exercise_name)

# print(exercises)

        for student_name, exercises in x.items():
            print(f'{student_name} is working on:')
            for exercise in exercises:
                print(f'\t* {exercise}')

exercise = Student_Workload()
exercise.multi_join()

















