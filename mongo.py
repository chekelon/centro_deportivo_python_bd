from pymongo import MongoClient
import datetime

client = MongoClient('localhost')

db=client['personas']


personas=db['personas']
prestamos=db['prestamos']

fecha=datetime.datetime.today()

f_prestamo=fecha.strftime("%Y-%m-%d %H:%M:%S")
	

print(db.list_collection_names())

def RegistrarPersona(persona):
	
	personas.insert_one({
		'nombre':persona.nombre,
		'edad':persona.age,
		'telefono':persona.telefono
		})


def RegistrarPrestamo(prestamo):
	prestamos.insert_one({
		'nombre':prestamo.persona,
		'material':prestamo.material,
		'cantidad':prestamo.cantidad,
		'fecha prestamo':f_prestamo,
		'fecha entrega':prestamo.f_entrega
		})

def Personas():
	pass

def deletePrestamosMongo(nombre):
	myquery = { "nombre": nombre }
	prestamos.delete_one(myquery)

def deletePersonaMongo(persona):
	personas.delete_one({'nombre':persona})


def updatePersonaMongo(persona,edad,telefono):
	myquery = { "nombre": persona }
	newvalues = { "$set": { "edad": edad,"telefono":telefono}}
	personas.update_one(myquery,newvalues)

def entregaMongo(nombre):
	myquery = { "nombre": nombre }
	newvalues = { "$set": { "fecha entrega":f_prestamo}}
	prestamos.update_one(myquery,newvalues)

