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

    def __init__(self, *name):  # polymorphism No.1
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