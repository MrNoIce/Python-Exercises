import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in cohort {self.cohort}, slack handle is {self.slack_handle}'


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/jakescott/workspace/python/exercises/music-history/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)


class Cohort():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'This is the {self.name} best to be'


class CohortReport():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/jakescott/workspace/python/exercises/music-history/studentexercises.db"

    def all_cohorts(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select cohort.Id,
                Name
            from cohort
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)


class Exercises():
    def __init__(self, exName, exLanguage):
        self.exerciseName = exName
        self.exerciseLanguage = exLanguage

    def __repr__(self):
        return f'{self.exerciseName} is done in {self.exerciseLanguage}'

class ExerciseExersise():

    def __init__(self):
        self.db_path = "/Users/jakescott/workspace/python/exercises/music-history/studentexercises.db"

    def all_exercises(self):
        """GOing to get all the exercises"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercises(
                row[0], row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Name,
                e.Language
            from Exercise e
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    def only_javascript(self):
        """GOing to get all the exercises"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercises(
                row[0], row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select Name, Language
                FROM Exercise e
                WHERE e.Language="JavaScript"
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    def only_python(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercises(
                row[0], row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select Name, Language
            From Exercise e
            Where e.Language="python"
            """)
            all_exercises = db_cursor.fetchall()

            for python in all_exercises:
                print(python)

class Instructors():

    '''the form in which we use to initalize the data to be used'''

    def __init__(self, first, last, handle, cohort, skill):
        self.first_name = first
        self.last_name = last
        self.handle = handle
        self.cohort = cohort
        self.skill = skill

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is {self.handle} on Slack, and teaching Cohort {self.cohort} with {self.skill}'

class InstructorExercise():

    '''The file path to where were getting the data from'''

    def __init__(self):
        self.db_path = "/Users/jakescott/workspace/python/exercises/music-history/studentexercises.db"

    def all_instructors(self):

        '''Retrieving all instructors info from the sql database'''

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructors(
                row[1], row[2], row[3], row[4], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT i.Id,
                i.FirstName,
                i.LastName,
                i.SlackHandle,
                i.Cohort,
                i.Speciality
            FROM Instructor i
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)




exerciseInstructors = InstructorExercise()
exerciseInstructors.all_instructors()



# exerciseDisplay = ExerciseExersise()
# exerciseDisplay.all_exercises()
# exerciseDisplay.only_javascript()
# exerciseDisplay.only_python()


# cohortDisplay = CohortReport()
# cohortDisplay.all_cohorts()


# reports = StudentExerciseReports()
# reports.all_students()
