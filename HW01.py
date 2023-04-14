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

