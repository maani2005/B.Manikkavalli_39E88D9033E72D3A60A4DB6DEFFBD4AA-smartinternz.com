class Student:

  def _init_(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Example usage:
students = [
    Student("Ragu", "A001", 3.8),
    Student("vijay", "B002", 3.5),
    Student("Monaj", "C003", 3.9),
    Student("Rajesh", "D004", 3.7),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print(
      f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"
  )