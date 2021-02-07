
from persona import *
from prestamos import *
from saveJson import *
from mongo import *
from conexion_mysql import *
import datetime

fecha=datetime.datetime.today()

f_prestamo=fecha.strftime("%Y-%m-%d %H:%M:%S")


lista= Persona()
prestamo= Prestamo()
bd_mysql=False
bd_mongo=False


def WhatBD(BasedeDatos):
	if BasedeDatos==1:
		bd_mysql=True
		print("Elegiste trabajar con MYSQL....")
	elif BasedeDatos==2:
		bd_mongo=True
		print("Elegiste trabajar con Mongo")




def fullListPerson():
	personasList,prestamosList=readJson()
	listadp=[]
	 
	for person in personasList:
		for value in person.values():
			listadp.append(value)

		usuario=Persona(listadp[0],listadp[1],listadp[2])
		lista.addObject(usuario)
		listadp=[]

	for person in prestamosList:
		for value in person.values():
			listadp.append(value)

		presta=Prestamo(listadp[0],listadp[1],listadp[2],listadp[3],listadp[4])
		prestamo.addPrestamo(presta)
		listadp=[]



def writeBeforeExit():
	for persona in lista.getList():
		storeJson(persona,None)

	for presta in prestamo.getList():
		storeJson(None,presta)

	writeJson()


def Mostrar():
	listaPrestamos=[]
	listaSinPrestamos=[]

	if(len(prestamo.getList())==0 and len(lista.getList())==0):
		print("Sin Registros...\n")
	else:
		for elemento in prestamo.getList():
			if elemento.f_entrega != "":
				listaPrestamos.append(elemento)

			else:
				listaSinPrestamos.append(elemento)
	print("\n\n::Usuarios::\n")
	for elemento in lista.getList():
		print("Nombre: "+elemento.nombre)

	print("\n\n::Listado de Prestamos::")
	for elemento in prestamo.getList():
		if elemento.f_entrega =='':
			print("Nombre: "+elemento.persona+"  Material: "
				+elemento.material+"  Cantidad: "+str(elemento.cantidad))




def Registrar():
	
	nombre=input("Nombre:  ")
	edad=input("Edad:  ")
	telefono=input("Telefono:  ")
	
	usuario=Persona(nombre,edad,telefono)
	lista.addObject(usuario)

	RegistrarPersonaMYSQL(usuario)
	RegistrarPersona(usuario)


	
	

def Verificar(nombre):
	
	for usuario in lista.getList():
		if usuario.nombre == nombre:
			return True
			break
		
	return False


def Prestar():
	print("PRESTAMOS DE MATERIAL")
	nombre=input("Nombre de persona:  ")
	if Verificar(nombre):
		material=input("Material: ")
		cantidad=int(input("cantidad: "))
		

		presta=Prestamo(nombre,material,cantidad)
		prestamo.addPrestamo(presta)

		
		RegistrarPrestamoMYSQL(presta)
		RegistrarPrestamo(presta)
		
		print("Prestamo registrado.....")
				
	else:
		print("Persona no registrada...")

def Entrega():
	print("ENTREGA DE MATERIAL")
	nombre=input("Nombre de persona:  ")
	cantidad=int(input("cantidad: "))
	encontrado=True

	for usuario in prestamo.getList():
		if usuario.persona == nombre:
			usuario.cantidad-=cantidad
			usuario.f_entrega=f_prestamo
			if usuario.f_entrega != "" and usuario.cantidad==0:
				
				entregaMYSQL(usuario.persona)
				entregaMongo(usuario.persona)
				print("Entrega registrada exitosamente.....")
				encontrado=False
				break
	
	if encontrado:
		print("Persona no registrada en prestamos!!!...")	



def modificarPersona():
	print("Datos de la Persona a modificar....\n")
	nombre=input("Nombre de la persona:")
	
	

	if Verificar(nombre):
		for client in lista.getList():
			if client.nombre==nombre:
				print("Nombre: "+client.nombre)
				print("Edad: "+str(client.age))
				print("Telefono: "+client.telefono)
				print("\n\n")
				print(":::Nuevo Datos:::\n")
				edad=int(input("Edad: "))
				telefono=input("Telefono: ")
				client.age=edad
				client.telefono=telefono
				
				updatePersonaMYSQL(client.nombre,edad,telefono)
				updatePersonaMongo(client.nombre,edad,telefono)
				print("Persona modificada satisfactoriamente!!...")
				break
	else:
		print("Persona no registrada!!!...")


def eliminarPersona():
	print(":::Eliminar Persona:::\n")

	nombre=input("Nombre: ")
	
	if lista.removeObject(None,nombre):
		deletePersonaMYSQL(nombre)
		deletePersonaMongo(nombre)
		print("Persona eliminada...")
	else:
		print(nombre+" no registrada!!!...")


def eliminarPrestamo():
	print(":::Eliminar Prestamo:::\n")
	nombre=input("Nombre de la Persona: ")

	if prestamo.removePrestamo(None,nombre):
		deletePrestamosMYSQL(nombre)
		deletePrestamosMongo(nombre)
		print("Prestamo Eliminado!!....")
	else:
		print("Prestamo con nombre "+nombre+" no registrado....")


def modificarPrestamo():
	print(":::Modificar Prestamo:::")

	nombre=input("Nombre: ")
	
	for client in prestamo.getList():
		if client.persona==nombre:
			print("Nombre: "+client.persona)
			print("Material: "+client.material)
			print("Cantidad: "+client.cantidad)
			print("\n\n")
			print(":::Nuevo Datos:::\n")
			nombre=input("Nombre: ")
			material=input("Material: ")
			cantidad=int(input("Cantidad: "))
			client.persona=nombre
			client.material=material
			client.cantidad=cantidad
			updatePrestamosMYSQL(client.persona,nombre,material,cantidad)
			updatePrestamoMongo(client.persona,nombre,material,cantidad)
			print("Prestamo modificada satisfactoriamente!!...")
			break
	







