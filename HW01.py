from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age, gender, height, weight):
        self._name = name
        self.__age = age
        self._gender = gender
        self.__height = height
        self.__weight = weight

    def introduce(self):
        print(f"Hi, my name is {self._name}. I am {self.__age} years old.")

    def eat(self, food):
        print(f"{self._name} is eating {food}.")

    def sleep(self):
        print(f"{self._name} is sleeping.")

    def exercise(self):
        print(f"{self._name} is exercising.")

    @abstractmethod
    def talk(self):    # abstraction No.1
        pass

class Friend:

    def __init__(self, *name):  
        self._name = name

    def greeting(self):
        for Name in self._name:
            print(f'Hello {Name}! how are you?')


class Student(Person):

    def __init__(self, name, age, gender, height, weight, school_name, friend_name):
        super().__init__(name, age, gender, height, weight)  # inheritance No.1
        self.__school_name = school_name
        self._friend = Friend(friend_name)    # composition No.1

    def study(self):
        print(f"{self._name} is studying at {self.__school_name}.")

    def Group_study(self):
        print(f"{self._friend.greeting} \n Shall we study together?")

    def talk(self):     # abstraction No.1
        print(f"{self._name} is talking with {self._friend._name}")

    def perpose():  #polumorphism No.1
        print("student's perpose is graduating")    


class Teacher(Person):

    def __init__(self, name, age, gender, height, weight, subject):
        super().__init__(name, age, gender, height, weight)  # inheritance No.2
        self.__subject = subject

    def teach(self):
        print(f"{self._name} is teaching {self.__subject}.")

    def talk(self):    # abstraction No.1
        if self._gender == 'male':
            print(f"Mr.{self._name} is talking")
        elif self._gender == 'female':
            print(f"Mrs.{self._name} is talking")

    def perpose():  #polumorphism No.1
        print("teacher's perpose is to graduate good students")    

class Course:
    def __init__(self, name, description, teacher):
        self._name = name
        self.__description = description
        self._teacher = teacher

    def get_teacher(self):
        print(f"The teacher for {self._name} is {self._teacher.name}.") #aggrigation

class Door:

    def knock():
        print('knock knock!')


class Classroom:

    def __init__(self, teacher, *student):

        self.student = student
        self.teacher = teacher
        self.door = Door()  # compositon No.2

    def start_class(self):

        print(f"{self.teacher.name} starts the class.")  # aggregatin No.1

        for student in self.student:  # polymorphism No.2 & aggregatin No.2 by student
            student.study()

    def Knock(self):
        self.door.knock()


class School:
    def __init__(self, name, location, classrooms):
        self._name = name
        self._location = location
        self._classrooms = classrooms

    def start_school_day(self):
        print(f"{self._name} starts the school day.")

        for classroom in self._classrooms: 
            classroom.start_class()  # aggregation No.3

class Department:
    def __init__(self, name, head_teacher):
        self._name = name
        self.head_teacher = head_teacher

    def get_head_teacher(self):
        print(
            f"The head teacher of {self._name} department is {self.head_teacher.name}.") #aggrigation No.4 from person


class University:
    def __init__(self, name, location, departments):
        self._name = name
        self.location = location
        self.departments = departments

    def get_departments(self):
        print(f"The {self._name} university has the following departments:")

        for department in self.departments:
            print(department.name) #aggrigation No.5


class Building:
    def __init__(self, name, address, number, color, other):
        self._name = name
        self.address = address
        self.number = number
        self.color = color
        self.otherstupidthingforthelovelyta = other

    def Lost(self):
        print(f"OH , I'm lost, come to {self.address}")

    def artist(self):
        print(f"what a nice color , i love {self.color}")

    def massage(self):
        print(f"I have a question from who first said that we should make fifteen classes with 5 method and else ... 'why'? ")


class Lab(Building):
    def __init__(self, name, address, department, number, color, other):
        super().__init__(name, address, number, color, other)  # inheritace No.3
        self.department = department

class Library(Building):
    def __init__(self, name, address, floor, number, color, other):
        super().__init__(name, address, number, color, other)  # inheritance No.4
        self.libname = name
        self.floor = floor

    @abstractmethod  # abbstraction
    def borrow_book(self):
        pass


class Book(Library):
    def __init__(self,name, address, floor, number, color, other, title, *author):
        super().__init__(name, address, floor, number, color, other)  # inheritance No.5
        self.title = title
        self.author = author

    def borrow_book(self, stu_name):
        self.stu_name = stu_name
        print(f"{self.stu_name} borrow {self.title} book from {self._name} library.")

#sample aggrigation and polymorphism
student1 = Student("Eliza", 18, "female", 170, 60, "ABC High School", "Thomas")
student2 = Student("Thomas", 18, "male", 170, 60, "ABC High School", "Eliza")
teacher1 = Teacher("Bob", 35, "male", 180, 80, "Math")
classroom1 = Classroom(teacher1, student1, student2)
classroom2 = Classroom(teacher1, student2)
