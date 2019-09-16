CREATE TABLE Cohort (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL UNIQUE
);

SELECT * FROM Cohort


CREATE TABLE Student (
	Id	   	  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL UNIQUE,
	LastName  TEXT NOT NULL UNIQUE,
	SlackHandle TEXT NOT NULL UNIQUE,
	CohortId 	  INTEGER NOT NULL,
	FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
	);

SELECT * FROM Student


CREATE TABLE Instructor (
	Id	   	  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL UNIQUE,
	LastName  TEXT NOT NULL UNIQUE,
	SlackHandle TEXT NOT NULL UNIQUE,
	CohortId INTEGER NOT NULL,
	Specialty TEXT NOT NULL UNIQUE,
	FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
	);

Select * From Instructor


CREATE TABLE Exercise (
	Id	   	  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL UNIQUE,
	Language  TEXT NOT NULL UNIQUE
	);

Select * From Exercise;


-- Drop table deletes table and you can create it again, just in case you made an error on the original table
DROP Table Instructor;

-- here we create the table again
CREATE TABLE Instructor (
	Id	   	  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL UNIQUE,
	LastName  TEXT NOT NULL UNIQUE,
	SlackHandle TEXT NOT NULL UNIQUE,
	CohortId INTEGER NOT NULL,
	Specialty TEXT NOT NULL UNIQUE,
	FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
	);

DROP TABLE Student;

CREATE TABLE Student (
	Id	   	  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL UNIQUE,
	LastName  TEXT NOT NULL UNIQUE,
	SlackHandle TEXT NOT NULL UNIQUE,
	CohortId 	  INTEGER NOT NULL,
	FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
	);


INSERT INTO Exercise (Name, Language)
VALUES 
('Kandy Korner', 'JavaScript'),
('Farmer Farm', 'HTML'),
('Color Rainbow', 'CSS'),
('Snakes in the Zoo', 'PYTHON'),
('Baking a Cake', 'C#');


INSERT INTO Cohort (Name)
VALUES 
('Day Cohort 33'),
('Day Cohort 34'),
('Day Cohort 35');


INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty)
VALUES 
('Steve', 'Brownlee', 'Coach', 1, "dancing"),
('Joe', 'Shepherd', 'Joes', 2, "dad jokes"),
('Leah', 'Hoefling', 'Leah', 3, "teaching");


Select * From Instructor;

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
VALUES 
('Karla', 'Gallegos', 'Kag', 1),
('Jayce', 'Wygard', 'JayceW', 2),
('Misty', 'DeRamus', 'Mdera', 3),
('Mike', 'Lopez', 'Llp', 1),
('Jenn', 'Flemm', 'Jenny', 2),
('Caleb', 'Mcmillen', 'Mcmmilen', 3),
('Melissa', 'Brown', 'Mbb', 1);


-- #joint table
CREATE TABLE StudentExercises (
	Id	   	  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	StudentId INTEGER NOT NULL,
	ExerciseId INTEGER NOT NULL,
	FOREIGN KEY(StudentId) REFERENCES Student(Id),
	FOREIGN KEY(ExerciseId) REFERENCES Exercise(Id)
	);

Drop Table StudentExercises;


INSERT INTO StudentExercises (StudentId, ExerciseId)
VALUES 
(1, 1),
(1, 2),
(2, 2),
(2, 3),
(3, 4),
(3, 5),
(4, 1),
(4, 2),
(5, 2),
(5, 1),
(6, 3),
(6, 4),
(7, 1),
(7, 3);
