from weakref import WeakKeyDictionary

'''
Exam 클래스를 처음 정의할 때, 한번만 생성
class Grade(object):
    def __init__(self):
        self._value = 0

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value

    def __get__(self, instance, owner):
        return self._value
'''

class Grade(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


class Exam(object):
    math_grade = Grade()
    write_grade = Grade()
    science_grade = Grade()

exam1 = Exam()
exam1.math_grade = 100

exam2 = Exam()
exam2.math_grade = 90

print(id(exam1.math_grade))
print(id(exam2.math_grade))
print(id(exam1.write_grade))
print(id(exam2.write_grade))

print(exam1.math_grade)
print(exam2.math_grade)

print(exam1.write_grade)
print(exam2.write_grade)