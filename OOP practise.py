print("hell")

class Pet:
    number_of_pets = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.add_number_pets() # or use Pet.number_of_pets += 1

    def intro(self):
        print(f'I am {self.name} and I am {self.age} years old')
    def speak(self):
        print("bark")
    
    @classmethod
    def get_number_pets(cls):
        return cls.number_of_pets
    
    @classmethod
    def add_number_pets(cls):
        cls.number_of_pets += 1


class Dog(Pet):
    #number_of_pets += 1
    def speak(self):
        print("bark")
class Cat(Pet):
    def __init__(self, name, age, colour):
        super().__init__(name, age)                             #IMP to add extra attribute
        self.colour = colour
    def intro(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.colour}') 
    def speak(self):
        print("Meow")

d1 = Dog("tim",23)
d1.intro()
d1.speak()
print(Pet.number_of_pets)
print(f'Pet.get_number_pets(){Pet.get_number_pets()}')
p1 = Pet("Lil", 12)
p1.speak()
print(Pet.number_of_pets)
c1 = Cat("bob", 5, "white")
c1.intro()
c1.speak()
print(f'Pet.get_number_pets(){Pet.get_number_pets()}')


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade      #0-100
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students) :
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        sum = 0
        for student in self.students:
            sum += student.get_grade()
        
        return sum/len(self.students)

s1 = Student("RJ", 22, 56)
s2 = Student("NJ", 25, 75)
s3 = Student("HJ", 27, 35)

c1 = Course("OOP", 2)
c1.add_student(s1)
c1.add_student(s2)
print(c1.students[0].get_name())
print(c1.get_average_grade())
d = Dog("Tim",22)
d.speak()
d2 = Dog("bill",12)
print(c1.add_student(s3))

class StaticFunctions:

    @staticmethod
    def add(x,y):
        return x+y

print(StaticFunctions.add(7,3))


