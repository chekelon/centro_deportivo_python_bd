
import os 
from peticiones import *
from saveJson import *




def iniciar():
	opcion=-1
	fullListPerson()
	#eleccion=True
	
	while opcion!=9:
		# if eleccion:
		# 	print("Con que BD desea trabajar..\n"
		# 		"1) MYSQL \n"
		# 		"2) MONGO\n\n")
		# 	eleccion=False
		# 	basededatos=int(input("Escribe el numero : "))
		# 	if basededatos == 1 or basededatos == 2: 
		# 		peticion.whatDB(basededatos)
				


		print(":::::PRESTAMO DE MATERIAL DEPORTIVO::::: \n\n"
			"Elija una Opcion....\n\n"
			"1) Listado de prestamos..\n"
			"2) Prestar...\n"
			"3) Eliminar prestamo\n"
			"4) Modificar prestamo\n"
			"5) Entrega...\n"
			"6) Registrar nueva persona...\n"
			"7) Eliminar persona\n"
			"8) Modificar persona\n"
			"9) Salir.....\n")

		opcion=int(input("Escribir Opcion..."))

		if(opcion==1):
			Mostrar()
		elif(opcion==2):
		    Prestar()
		elif(opcion==3):
			eliminarPrestamo()
		elif(opcion==4):
			pass
		elif(opcion==5):
			Entrega()
		elif(opcion==6):
			Registrar()
		elif(opcion==7):
			eliminarPersona()
		elif(opcion==8):
			modificarPersona()
		elif(opcion==9):
			writeBeforeExit()
			print("Salir del programa")
		else:
			print("Ingrese una de las opciones Validas....")
		input()
		os.system ("cls")






if __name__=='__main__':
	iniciar()