"""
INSTRUCTIONS:
1. Type in the dataclass code from the slides/video. You would have done this before class.
2. Add one more field: gpa, a float.
3. Write a main function to create some example Student objects with some example names,
college_id and GPA values.
4. Verify you can read the name, college ID and GPA for an example student.
5. Verify when you print an example student, the GPA is included.
6. Add some comments in your code to compare the dataclass version to the "traditional" version.
"""

# Student class for storing name and college ID
#
# class Student:
#
#     def __init__(self, name, college_id):
#         self.name = name
#         self.college_id = college_id
#         self.gpa = gpa
#
#     def __str__(self): # __str__ = returns a string of an object
#         return f'Student name: {self.name}, ID: {self.college_id}, GPA: {self.GPA}'
#
#
# alex = Student('Alex', 'abcdef')
# print(alex.name)
# print(alex)

from dataclasses import dataclass


@dataclass
class Student:  # dataclass version much shorter than traditional, please see above traditional sample
    name: str
    college_id: int
    gpa: float  # added additional field for GPA


def main():  # main function to create some example Student objects

    alice = Student('Alice', 12345, 3.5)
    bob = Student('Bob', 98765, 2.0)

    print(alice)
    print(bob)


main()

