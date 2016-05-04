# -*- coding: utf-8 -*-
#Se acomoda la codificón utf-8 para poder poner tildes y que no sea solo unicode

#Se importan las librerías necesarias
import sys
import time
import random
import datetime
import telepot
import MySQLdb #para la conexión a la base de datos de datos mysql, recuerde tener instalado el paquete python-mysqldb



db = MySQLdb.connect(host="sandbox2.ufps.edu.co", # tu host, generalmente localhost
                     user="ufps_79", # nombre de usuario para la conexion a la base de datos
                      passwd="", # contraseña para conectar a la base de datos
                      db="ufps_79", charset="utf8") # nombre de la base de datos, se define codificacion utf-8
db.names="uft8" #Se vuelve a definir codificación utf-8 para los nombres

cur = db.cursor()  #se inicializa el objetor cur el cual será nuestra manera de hacer consultas, más abajo se ve

def fecha(nombre):
    	cur.execute('SELECT inicio, fin FROM fechas where nombre like "%'+ nombre + '%"')
	row = ""
	fechasS = ""
        correo = ""
        for row in cur.fetchall():
            correo += str(row[1].encode('utf-8'))
        return str(row[0].encode('utf-8')) + " hasta " + str(row[1])

def listarFechas():
        cur.execute('SELECT nombre FROM fechas')
        row = ""
        fechasS = ""
        for row in cur.fetchall():
            fechasS += str(row[0].encode('utf-8')) + " "
        return fechasS    
            