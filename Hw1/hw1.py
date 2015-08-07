import random

class Portfolio(object):
	def __init__(self):
		self.cash = 0
		self.stock = {}
		self.MF={}
		self.history=[]
	
	def buyStock(self,number, name):
		try: int(number)
		except ValueError: print "This is not a number"
		if number<1: raise NotImplementedError("Introduce positive number")
		if name in self.stock: self.stock[name]+=number
		else: self.stock[name]=number
        else: self.db[student_grade] = {name} #if the key doesn't exist, create it and put kid in
			
			
class Stock(object):
	def __init__(self, price, name):
		self.price = price
		self.name = name
		


