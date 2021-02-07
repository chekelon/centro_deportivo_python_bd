import json
import datetime

data = {}
data['clients'] = []
data['prestamos'] = []
persona=[]
presta=[]

fecha=datetime.datetime.today()

f_prestamo=fecha.strftime("%Y-%m-%d %H:%M:%S")

def storeJson(persona=None,prestamo=None):
	

	if persona != None:
		

		data['clients'].append({
	    'nombre':persona.nombre,
	    'age': persona.age,
	    'telefono': persona.telefono})
	elif prestamo != None:
		

		data['prestamos'].append({
	    'nombre':prestamo.persona,
	    'material': prestamo.material,
	    'cantidad': prestamo.cantidad,
	    'fecha prestamo': f_prestamo,
	    'fecha entrega': prestamo.f_entrega})

def writeJson():

	with open('data.json', 'w') as file:
		json.dump(data, file, indent=4)

def readJson():
	with open('data.json') as file:
		data = json.load(file)

		for client in data['clients']:
			persona.append(client)


		for prestamo in data['prestamos']:
			presta.append(prestamo)

	return persona,presta



		

 







