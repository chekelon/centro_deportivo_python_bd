


class Prestamo:

	def __init__(self,persona=None,material='',cantidad=0,f_prestamo='',f_entrega=''):
		self.persona=persona
		self.material=material
		self.cantidad=cantidad
		self.f_prestamo=f_prestamo
		self.f_entrega=f_entrega
		self.list=[]



	def setFechaPrestamo(self,f_prestamo=None):
		if f_prestamo != None:
			self.f_prestamo=f_prestamo
			return True
		else:
			print("Favor de escribir la fecha...")
			return False


	def setFechaEntrega(self,f_entrega=None):
		if f_entrega != None:
			self.f_entrega=f_entrega
			return True
		else:
			print("Favor de escribir la fecha...")
			return False

	def addPrestamo(self,prestamo):
		self.list.append(prestamo)


	def getList(self):
		return self.list

	def removePrestamo(self,indice=None,nombre=None):
		if indice != None:
			self.list.pop(indice)
			return True
		elif nombre !=None:
			c=0
			for element in self.list:
				if element.persona==nombre:
					self.list.pop(c)
					return True
			c+=1
		return False


