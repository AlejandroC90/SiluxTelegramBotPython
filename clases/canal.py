# -*- coding: utf-8 -*-
#Se acomoda la codificón utf-8 para poder poner tildes y que no sea solo unicode

#Se importan las librerías necesarias
import sys
import time
import random
import datetime
import telepot
import MySQLdb #para la conexión a la base de datos de datos mysql, recuerde tener instalado el paquete python-mysqldb



#db = MySQLdb.connect(host="", # tu host, generalmente localhost
 #                    user="", # nombre de usuario para la conexion a la base de datos
  #                    passwd="", # contraseña para conectar a la base de datos
   #                   db="", charset="utf8") # nombre de la base de datos, se define codificacion utf-8
#db.names="uft8" #Se vuelinve a definir codificación utf-8 para los nombres
#cur = db.cursor()  #se inicializa el objetor cur el cual será nuestra manera de hacer consultas, más abajo se ve
foo = ['Tu puedes Ing!',
'Haz tu mejor esfuerzo','Si quieres triunfar, no te quedes mirando la escalera, empieza a subir, escalón por escalón, hasta que llegues arriba.','El que lucha siempre puede equivocarse, el que no, ya está equivocado.', 'Cuando pierdes, no te fijes en lo que has perdido, sino en lo que te queda por ganar.',
'Para triunfar en la vida, no es importante llegar el primero, para triunfar simplemente hay que llegar, levantándose cada vez que se cae en el camino.',
'No es verdaderamente grande aquel que nunca falla, si no el que nunca se da por vencido.',
' La VIDA no es fácil, pero si nos ESFORZAMOS y TRABAJAMOS DURO podemos conseguir TODO aquello que nos PROPONGAMOS','Lo único IMPOSIBLE en la vida, es aquello que no INTENTAS.']

def info():
 return random.choice(foo)
#	print "estoy aquí"
#	if random.randint(1,2) == 1:
	#	return "El Programa de Ingeniería de Sistemas de la UFPS está comprometido en la formación integral de profesionales competentes en el Desarrollo y Gestión de Sistemas de Información, caracterizados por una sólida fundamentación en las áreas de las ciencias de la computación e informática, enmarcado en un Proyecto Educativo fundamentado en el mejoramiento continuo de los procesos de docencia, investigación y extensión; basados en los principios de excelencia académica, con responsabilidad y compromiso con los procesos de transformación de la región y del país; contando con docentes de calidad con altas cualidades personales y profesionales, con una adecuada infraestructura física y tecnológica."
#	return "El Programa de Ingeniería de Sistemas proyecta para el 2017 continuar siendo un programa acreditado de alta calidad, manteniendo los procesos de mejoramiento continuo, líder en la formación de Ingenieros de Sistemas competentes en el desarrollo y Gestión de Sistemas de Información, comprometidos con el desarrollo tecnológico de la región y del país, afrontando las situaciones cambiantes del medio, respondiendo a los retos que presenta el uso masivo de las Tecnologías de Información y Comunicación. Apoyados en una estructura curricular flexible, con un equipo administrativo idóneo, con docentes de calidad con altas cualidades personales y profesionales, con una adecuada infraestructura física y tecnológica."	
	
