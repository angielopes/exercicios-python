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

grade_system = []

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

    try:
        option = int(input("\nChoose an option: "))
    except ValueError:
        print("Please choose a valid number: ")
        continue

    # Exit the program
    if option == 5:
        print("\nProgram closed...")
        break

    # Adding student
    elif option == 1:
        student_name = input("Enter the student's name: ").title().strip()
        # Adding three grades for the student
        student_grades = []
        for i in range(1, 4):
            while True:
                try:
                    grade = float(input(f"{i}ª grade of the student: "))
                    if 0 <= grade <= 10:
                        student_grades.append(grade)
                        break
                    else:
                        print("The grade must be between 0 and 10.")
                except ValueError:
                    print("Enter a valid numeric value.")
        grade_system.append([student_name, student_grades])
        print(f"{student_name} added.")

    # Remove student
    elif option == 2:
        remove_student = input("Which student do you want to remove? ").title().strip()
        for student in grade_system:
            if student[0] == remove_student:
                grade_system.remove(student)
                print(f"{remove_student} removed successfully!")
                break
        else:
            print(f"Student {remove_student} not found.")

    # Calculate and view a student's average
    elif option == 3:
        query_student_average = (
            input("Enter the student's name to view their average: ").title().strip()
        )
        for student in grade_system:
            if student[0] == query_student_average:
                average = sum(student[1]) / len(student[1])
                print(f"\n{query_student_average} has an average of {average:.2f}.")
                break
        else:
            print(f"Student {query_student_average} not found.")

    # List all students and their averages
    elif option == 4:
        if grade_system:
            print("\nList of students and their averages:")
            for student in grade_system:
                average = sum(student[1]) / len(student[1])
                print(f"{student[0]} - Average: {average:.2f}")
        else:
            print("No students registered.")
    else:
        (print("Invalid option! Try again."))
