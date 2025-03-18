"""Create a program that allows managing the grades of a class of students.
It must offer the following options:
1. Add student:
    The user must provide the student's name and a list of 3 grades
    (using input and conversion to numbers).
    The student will be added to the list in the format
    ["Name", [grade1, grade2, grade3]].
2. Remove student:
    The user must provide the student's name to remove them from the list.
    If the student does not exist, display an informative message.
3. View a student's average:
    The user must provide the student's name, and the program calculates
    and displays the average of the grades.
4. List all students and their averages:
    The program displays all students in the list, showing their averages.
5. Exit the program."""

from utils import confirm_action, get_valid_float, get_valid_int, get_valid_string


class Student:
    """
    A class used to represent a Student.

    Attributes
    ----------
    name : str
        the name of the student
    grades : list
        a list of grades for the student

    Methods
    -------
    add_grade(grade)
        Adds a grade to the student's list of grades if it is between 0 and 10.
    calculate_average()
        Calculates and returns the average of the student's grades.
    """

    def __init__(self, name):
        """
        Initializes a new instance of the class.
        Args:
            name (str): The name of the student.
        Attributes:
            name (str): The name of the student.
            grades (list): A list to store the grades of the student.
        """
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """
        Adds a grade to the list of grades if it is within the valid range.
        Parameters:
            grade (float): The grade to be added. Must be between 0 and 10 inclusive.
        Raises:
            ValueError: If the grade is not between 0 and 10.
        """
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            raise ValueError("The grade must be between 0 and 10.")

    def calculate_average(self):
        """
        Calculate the average of the grades.
        Returns:
            float: The average of the grades. If there are no grades, returns 0.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


class GradeSystem:
    """
    GradeSystem class for managing student grades.

    Methods:
    -------
        __init__():
            Initializes the GradeSystem with an empty list of students.
        add_student(student_name: str):
            Adds a new student to the system.
        remove_student(student_name: str):
            Removes a student from the system by their name.
        view_student_average(student_name: str):
            Prints the average grade of a specified student.
        list_all_students():
            Lists all students and their average grades.
    """

    def __init__(self):
        """
        Initializes a new instance of the class.
        Attributes:
            students (list): A list to store student information.
        """
        self.students = []

    def add_student(self, student_name):
        """
        Adds a new student to the list of students.
        Args:
            student_name (str): The name of the student to be added.
        Returns:
            None
        """
        new_student = Student(student_name)
        self.students.append(new_student)

    def remove_student(self, student_name):
        """
        Removes a student from the list of students by their name.
        Args:
            student_name (str): The name of the student to be removed.
        Returns:
            None
        Prints:
            A message indicating whether the student was successfully removed or not found.
        """
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                print(f"{student_name} removed successfully!")
                return
        print(f"Student {student_name} not found.")

    def view_student_average(self, student_name):
        """
        Display the average grade of a specified student.
        Args:
            student_name (str): The name of the student whose average grade is to be displayed.
        Returns:
            None: This function prints the average grade of the student if found,
              otherwise it prints a message indicating the student was not found.
        """
        for student in self.students:
            if student.name == student_name:
                average = student.calculate_average()
                print(f"\n{student_name} has an average of {average:.2f}")
                return
        print(f"Syudent {student_name} not found.")

    def list_all_students(self):
        """
        Lists all registered students and their average grades.
        If no students are registered, it prints a message indicating that.
        Otherwise, it prints the name and average grade of each student.
        Returns:
            None
        """
        if not self.students:
            print("No students registered.")
            return
        print("\nList of students and their averages:")
        for student in self.students:
            average = student.calculate_average()
            print(f"{student.name} - Average: {average:.2f}")


# Start the program

grade_system = GradeSystem()

while True:
    print(
        """
          OPTIONS:
    [1] Add student
    [2] Remove student
    [3] View a student's average
    [4] List all students and their averages
    [5] Exit"""
    )

    option = get_valid_int("\nChoose an option: ")

    # Exit the program
    if option == 5:
        if confirm_action("Are you sure you want to exit?"):
            print("\nProgram closed...")
            break

    # Adding student
    elif option == 1:
        student_name = get_valid_string("Enter the student's name: ")
        grade_system.add_student(student_name)
        for i in range(1, 4):
            grade = get_valid_float(f"{i}ª grade of the student: ")
            grade_system.students[-1].add_grade(grade)  # Last student added to the list
        print(f"{student_name} added.")

    # Remove student
    elif option == 2:
        remove_student = get_valid_string("Which student do you want to remove? ")
        grade_system.remove_student(remove_student)

    # Calculate and view a student's average
    elif option == 3:
        query_student_average = get_valid_string(
            "Enter the student's name to view their average: "
        )
        grade_system.view_student_average(query_student_average)

    # List all students and their averages
    elif option == 4:
        grade_system.list_all_students()
    else:
        print("Invalid option! Try again.")
