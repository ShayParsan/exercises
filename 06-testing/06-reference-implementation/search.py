class Student:
    def __init__(self, id):
        self.id = id


def linear_search(students, target_id):
    for student in students:
        if student.id == target_id:
            return student.id


def binary_search(students, target_id):
    left = 0
    right = len(students) - 1

    while left <= right:
        mid = (left + right) // 2
        if students[mid].id == target_id:
            return mid
        elif students[mid].id < target_id:
            left = mid + 1
        else:
            right = mid - 1

    return -1
