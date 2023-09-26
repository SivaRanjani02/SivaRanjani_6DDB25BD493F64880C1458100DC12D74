'''
Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.
'''


class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


student = [
    Student("Swerlin", "A126", 7.8),
    Student("Ebeena", "A125", 8.9),
    Student("Sivani", "A124", 9.1),
    Student("Aries", "A123", 9.9),
]

sorted_students = sort_students(student)

for student in sorted_students:
  print("\nName       : {}, \nRoll Number: {}, \nCGPA       : {}".format(student.name, student.roll_number,student.cgpa))
