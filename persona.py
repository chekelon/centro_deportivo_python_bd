

class Persona:

	def __init__(self,nombre='',age='',telefono=''):
		self.nombre=nombre
		self.age=age
		self.telefono=telefono
		self.list=[]


	def setData(self,nombre=None,age=None,telefono=None):
		if (nombre != None):
			self.nombre=nombre
		if (age != None):
			self.age=age
		if (telefono != None):
			self.telefono=telefono


	def get(self):
		return self.nombre,self.age,self.telefono

	def addObject(self,persona):
		self.list.append(persona)

	def removeObject(self,indice=None,nombre=None):
		if indice != None:
			self.list.pop(indice)
			return True
		elif nombre !=None:
			c=0
			for element in self.list:
				if element.nombre==nombre:
					self.list.pop(c)
					return True
			c+=1
		return False


	def searchObject(self,nombre=None):
		if nombre != None:
			for element in self.list:
				if element.nombre==nombre:
					return element
		return None


	def getList(self):
		return self.list


	def updatePersona(self,indice,persona):
		self.list[indice]=persona			
		


	def __str__(self):
		
		return self.nombre 

	









