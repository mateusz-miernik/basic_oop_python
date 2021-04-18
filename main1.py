"""
    Title: Basic examples of OOP in Python.

    Description: Inheritance, instance & class attributes/methods, properties etc.

    Date:        Version:     Author:              Comment:
    April 2021  1.0.0       Mateusz Miernik     Initial release

"""

from typing import List, Any
from abc import ABC, abstractmethod


class Bird(ABC):
    """
        This is parent class for Bird objects
    """

    total_objects = 0   # This is attribute defined in parent class, it count number of all object instances

    def __init__(self, species: str, speed: int, skills: List[Any], isCute):
        self.species = species      # Instance's public attribute
        self.speed = speed          # Instance's public attribute
        self.skills = skills        # Instance's public attribute
        self.__isCute = isCute      # Instance's private attribute
        Bird.total_objects += 1     # After invoking a parent class we increasing value of total_objects

    def say_hello(self):
        print(f"Hello there! I am {self.species}! My speed is {self.speed} km/h")

    # @abstractmethod     # This instance method need to be included in child classes because of this decorator
    def yell(self):
        print("This is general yell for all birds: aa a aaa a!")

    @property
    def IsCute(self):
        return self.__isCute

    @IsCute.setter
    def IsCute(self, new_value):
        print(f"Changing value of isCute from {self.__isCute} to {new_value}")
        self.__isCute = new_value

    @IsCute.deleter
    def IsCute(self):
        self.__isCute = None
        print("Value of isCute was deleted!")

    @property
    def Skills(self):
        print(f"My skills are: {self.skills}")
        return self.skills

    @Skills.setter
    def Skills(self, new_skills: List[Any]):
        print(f"Changing skills {self.skills} to {new_skills}!")
        self.skills = new_skills

    @Skills.deleter
    def Skills(self):
        self.skills = []

    @classmethod
    def ReadClassFromLine(cls, text):
        new_obj = Bird(*text.split(':'))
        return new_obj


class Hawk(Bird):
    """
        This is child class of Bird class. It describes Hawk.
    """
    def __init__(self, speed: int, skills: List[Any]):
        super().__init__("Hawk", speed, skills, False)

    def yell(self):
        print("Yell of a Hawk: <hard to describe by text..>!")


class Owl(Bird):
    """
        This is child class of Bird class. It describes Owl.
    """

    def __init__(self, speed: int, skills: List[Any]):
        super().__init__("Owl", speed, skills, True)

    def yell(self):
        print("Yell of a Hawk: hu hu hu huuu!")


if __name__ == "__main__":
    # Initializing objects
    hawk = Hawk(120, ["fast", "danger appearance"])
    owl = Owl(70, ["smart"])

    # Initializing object by class method - ReadClassFromLine
    parrot = Bird("Parrot", 50, ["colorful", "talking", "friendly"], True)

    # Get attributes of an instance
    print(f"Skills of hawk object: {hawk.skills}")
    print(f"Speed of owl object: {owl.speed} km/h\n")

    # Invoking instance's methods
    hawk.say_hello()
    owl.say_hello()
    parrot.say_hello()
    hawk.yell()

    # Invoking property of object
    print(hawk.IsCute)

    # Assigning new value to property
    hawk.IsCute = "False. Hawk is terrifing!"
    print(hawk.IsCute)

    # Show class attribute - parent class
    print(f"\nWe have {Bird.total_objects} birds on the sky!")