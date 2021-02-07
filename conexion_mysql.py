import mysql.connector 
import datetime

mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="centro deportivo"
	)


mycursor=mydb.cursor()
fecha=datetime.datetime.today()

f_prestamo=fecha.strftime("%Y-%m-%d %H:%M:%S")


def RegistrarPersonaMYSQL(persona):
	sql="INSERT INTO personas (nombre,edad,telefono) VALUES (%s,%s,%s)"
	val=(persona.nombre,persona.age,persona.telefono)

	mycursor.execute(sql,val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted Persona.")



def updatePersonaMYSQL(nombre,edadNew,telefonoNew):
	sql="UPDATE personas SET edad=%s,telefono=%s WHERE nombre=%s"
	val=(edadNew,telefonoNew,nombre)

	mycursor.execute(sql,val)
	mydb.commit()
	print(mycursor.rowcount, "record(s) affected")


def deletePersonaMYSQL(nombre):
	sql = "DELETE FROM personas WHERE nombre=%s "
	val=(nombre,)
	mycursor.execute(sql,val)
	mydb.commit()
	print(mycursor.rowcount, "record(s) deleted")



def RegistrarPrestamoMYSQL(prestamo):
	sql="INSERT INTO prestamos (nombre,material,cantidad,fecha_prestamo) VALUES (%s,%s,%s,%s)"
	val=(prestamo.persona,prestamo.material,prestamo.cantidad,f_prestamo)
	
	mycursor.execute(sql,val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted Prestamo.")

def updatePrestamosMYSQL(nombreOLD,nombre,material,cantidad):
	sql="UPDATE prestamos SET nombre=%s,material=%s,cantidad=%s WHERE nombre=%s"
	val=(nombre,material,cantidad,nombreOLD)

	mycursor.execute(sql,val)
	mydb.commit()
	print(mycursor.rowcount, "record(s) affected")


def deletePrestamosMYSQL(nombre):
	sql = "DELETE FROM prestamos WHERE nombre=%s "
	val=(nombre,)
	mycursor.execute(sql,val)
	mydb.commit()
	print(mycursor.rowcount, "record(s) deleted")

def entregaMYSQL(nombre):
	sql="UPDATE prestamos SET fecha_entrega=%s WHERE nombre=%s"
	val=(f_prestamo,nombre)

	mycursor.execute(sql,val)
	mydb.commit()
	print(mycursor.rowcount, "record(s) affected")




