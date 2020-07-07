# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:20:45 2019

@author: csmon
"""

# ver https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/

# creating a class:
# class is a set or category of things having some property or attribute in 
# common and differentiated from others by kind, type or quality.

# object: is one of the instances of the class, which can perform the 
# functionalities that are defined in the class.

# so with a class you can create different instances of an object? 

# self: represents the instance of the class. Using it as a keyword we can
# access the attributesand methods of the class in python.

# __init__: is a method which is called when an object is created from the 
# class and is used to initiliaze the attributes of a class.

# Let's consider that you are creating a NFS game. for that we should have a
#  car. Car can have attributes like "color", "company", "speed_limit" etc. 
# and methods like "change_gear", "start", "accelarate", "move" etc.

class Car(object):
	"""
		blueprint for car
	"""

# with def _init_ 
	def __init__(self, model, color, company, speed_limit):
		self.color = color
		self.company = company
		self.speed_limit = speed_limit
		self.model = model

	def start(self):
		print("started")

	def stop(self):
		print("stopped")

	def accelarate(self):
		print("accelarating...")
		"accelarator functionality here"

	def change_gear(self, gear_type):
		print("gear changed")
		" gear related functionality here"
        

# lets create different instances of car class
maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)

print(audi.model)

# Another example -------------------------------------------------------------
# find out the cost of a rectangular field with breadth (b=120), lenght(l=160)
# It costs x (2000) rupees per 1 square unit.

class Rectangle:
   def __init__(self, length, breadth, unit_cost=0):
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   
   def get_perimeter(self):
       return 2 * (self.length + self.breadth)
   
   def get_area(self):
       return self.length * self.breadth
   
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost
# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
r = Rectangle(160, 120, 2000)
print("Perimeter of Rectangle: %s cm" % (r.get_perimeter()))
print("Area of Rectangle: %s cm^2" % (r.get_area()))
print("Cost of rectangular field: Rs. %s " %(r.calculate_cost()))

