class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks.values())

    def average(self):
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("\nRoll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Average:", round(self.average(), 2))
        print("Grade:", self.grade())


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.filename = "students.txt"
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    if len(data) == 5:
                        roll_no = int(data[0])
                        name = data[1]

                        marks = {
                            "Python": int(data[2]),
                            "SQL": int(data[3]),
                            "Java": int(data[4])
                        }

                        student = Student(roll_no, name, marks)
                        self.students.append(student)

        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.filename, "w") as file:
            for student in self.students:
                file.write(
                    f"{student.roll_no},{student.name},"
                    f"{student.marks['Python']},"
                    f"{student.marks['SQL']},"
                    f"{student.marks['Java']}\n"
                )

    def add_student(self):
        roll_no = int(input("Enter Roll No: "))

        for student in self.students:
            if student.roll_no == roll_no:
                print("Student already exists!")
                return

        name = input("Enter Name: ")

        python = int(input("Enter Python Marks: "))
        sql = int(input("Enter SQL Marks: "))
        java = int(input("Enter Java Marks: "))

        marks = {
            "Python": python,
            "SQL": sql,
            "Java": java
        }

        student = Student(roll_no, name, marks)
        self.students.append(student)
        self.save_data()

        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No students found!")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        roll_no = int(input("Enter Roll No to search: "))

        for student in self.students:
            if student.roll_no == roll_no:
                student.display()
                return

        print("Student not found!")

    def update_student(self):
        roll_no = int(input("Enter Roll No to update: "))

        for student in self.students:
            if student.roll_no == roll_no:
                student.name = input("Enter New Name: ")
                student.marks["Python"] = int(input("Enter New Python Marks: "))
                student.marks["SQL"] = int(input("Enter New SQL Marks: "))
                student.marks["Java"] = int(input("Enter New Java Marks: "))

                self.save_data()

                print("Student updated successfully!")
                return

        print("Student not found!")

    def delete_student(self):
        roll_no = int(input("Enter Roll No to delete: "))

        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                self.save_data()

                print("Student deleted successfully!")
                return

        print("Student not found!")

    def menu(self):
        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.display_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                print("Thank you!")
                break

            else:
                print("Invalid choice!")


system = StudentManagementSystem()
system.menu()