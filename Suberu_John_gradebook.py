class EmptyRosterError(Exception):
    pass

class StudentNotFoundError(Exception):
    def __init__(self, student_id):
        super().__init__(f"Exception: Student ({student_id}) not found")

class GradeItemNotFoundError(Exception):
    def __init__(self, grade_item_name):
        super().__init__(f"Exception: Grade Item ({grade_item_name}) not found")

class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

class GradeItem:
    def __init__(self, name, total_points):
        self.name = name
        self.total_points = total_points
        self.grades = {}

    def add_student_grade(self, student_id, grade):
        self.grades[student_id] = grade

    def get_name(self):
        return self.name

    def get_total_points(self):
        return self.total_points

    def get_student_grade(self, student_id):
        return self.grades.get(student_id, "N/A")

class Course:
    def __init__(self):
        self.roster = []
        self.grade_items = []

    def add_student(self, student):
        self.roster.append(student)

    def add_grade_item(self, grade_item):
        self.grade_items.append(grade_item)

    def add_student_grade(self, grade_item_name, student_id, grade):
        student_exists = any(student.get_student_id() == student_id for student in self.roster)
        if not student_exists:
            raise StudentNotFoundError(student_id)

        grade_item = next((gi for gi in self.grade_items if gi.get_name() == grade_item_name), None)
        if grade_item is None:
            raise GradeItemNotFoundError(grade_item_name)

        grade_item.add_student_grade(student_id, grade)

    def print_student_grades(self, student_id):
        student = next((s for s in self.roster if s.get_student_id() == student_id), None)
        if student is None:
            raise StudentNotFoundError(student_id)

        print(f"Grades for {student.get_first_name()} {student.get_last_name()} ({student_id}):")
        for grade_item in self.grade_items:
            grade = grade_item.get_student_grade(student_id)
            print(f"  {grade_item.get_name()}: {grade}")

    def print_roster(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty.")

        print("Class Roster:")
        for student in self.roster:
            print(f"  {student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()})")

    def print_class_grades(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty.")

        print("Class Grades:")
        for student in self.roster:
            print(f"{student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()}):")
            for grade_item in self.grade_items:
                grade = grade_item.get_student_grade(student.get_student_id())
                print(f"  {grade_item.get_name()}: {grade}")


course = Course()

while True:
    print("\nGradebook Menu:")
    print("1. Add Student")
    print("2. Add Grade Item")
    print("3. Add Student Grade")
    print("4. Print Student Grades")
    print("5. Print Class Roster")
    print("6. Print Class Grades")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            try:
                student_id = int(input("Enter student ID: "))
            except ValueError:
                print("Error: Enter a Interger Student ID")
                continue
            student = Student(first_name, last_name, student_id)
            course.add_student(student)
            print("Student added.")

        elif choice == 2:
            name = input("Enter grade item name: ")
            try:
                total_points = int(input("Enter total points: "))
            except ValueError:
                print("Invalid input: Total points must be numeric.")
                continue
            grade_item = GradeItem(name, total_points)
            course.add_grade_item(grade_item)
            print("Grade item added.")

        elif choice == 3:
            grade_item_name = input("Enter grade item name: ")
            try:
                student_id = int(input("Enter student ID: "))
                grade = int(input("Enter grade: "))
            except ValueError:
                print("Invalid input: Student ID and grade must be numeric.")
                continue
            try:
                course.add_student_grade(grade_item_name, student_id, grade)
                print("Grade added.")
            except (StudentNotFoundError, GradeItemNotFoundError) as e:
                print(e)

        elif choice == 4:
            try:
                student_id = int(input("Enter student ID: "))
            except ValueError:
                print("Invalid input: Student ID must be numeric.")
                continue
            try:
                course.print_student_grades(student_id)
            except StudentNotFoundError as e:
                print(e)

        elif choice == 5:
            try:
                course.print_roster()
            except EmptyRosterError as e:
                print(e)

        elif choice == 6:
            try:
                course.print_class_grades()
            except EmptyRosterError as e:
                print(e)

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input: Please enter a numeric choice.")