import pygame

class Human:
	def __init__(self,first_name, last_name, Class, age, health):
		self.first_name =  first_name
		self.last_name = last_name
		self.name = f"{self.first} {self.last_name}"
		self.Class = Class
		self.age = age
		self.health = health
		self.alive = True
		self.immunity = 0
		self.set_immun()

	def inc_age(self):
		if self.age < 30 and self.immunity<10:
			self.immunity += 1
		if self.age > 30 :
			self.immunity -= 0.2
		self.age += 1
		return self.age

	def kill(self):
		self.alive = False
		return self.alive

	def set_immun(self):
		if self.age <= 10:
			self.immunity = 0
		if self.age>10 and self.age<=20:
			self.immunity = 1
		if 20>self.age<=35:
			self.immunity = 5
		else:
			self.immunity = 4

		return self.immunity

	def damage(self,amt):
		self.health -= amt
		return self.health
