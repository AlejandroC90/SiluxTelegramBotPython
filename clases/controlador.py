# -*- coding: utf-8 -*-
#Se acomoda la codificón utf-8 para poder poner tildes y que no sea solo unicode

#Se importan las librerías necesarias
import sys
import time
import random
import datetime
import profesor
import informacion
import canal
import eliza
import fechas
from eliza import eliza

therapist = eliza();

#Clase controladora del Bot
def asesoriaProfesor(nombre):
	return profesor.asesoriaPro(nombre)

def correoProfesor(nombre):
	return profesor.correoPro(nombre)
    
def paginaProfesor(nombre):
	return profesor.paginaPro(nombre)

def enviarMensajeCanal():
	return canal.info()

def enviarFechas(nombre):
        return fechas.fecha(nombre)
  
def elizam(mensaje):
	return therapist.respond(mensaje)
	  	

