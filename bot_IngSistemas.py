# -*- coding: utf-8 -*-
import sys
import telepot
from telepot.delegate import per_chat_id, create_open

import clases.profesor
import clases.informacion
import clases.controlador as controlador
import threading

def canal():
        threading.Timer(3600, canal).start()
        print "Enviando mensaje a canal"
      #  self.sender.sendMessage("@IngSistemasUFPSCanal" + controlador.enviarmensajecanal())
      #  bot.sendMessage('@IngSistemasUFPSCanal', controlador.enviarMensajeCanal())

class botSistemas(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        super(botSistemas, self).__init__(seed_tuple, timeout)
        self._variable = 0
        self._mensaje = ""
        self._clave = ""
        
  
        

    def on_chat_message(self, msg):
        #Tomamos el mensaje que llega
        self._mensaje = msg['text'].encode('utf-8')
        #El nombre de la persona que envia el mensaje
        nombre = (msg['from']['first_name']).encode('utf-8')
        
        if self._mensaje == "/start":
            self.sender.sendMessage ("Hola! \nBienvenido al Bot de Ingeniería de Sistemas de la UFPS creado por el Semillero de Desarrollo de Software Libre y Linux. \n\nTengo disponibles los siguientes comandos: \n\n/correo Muestro correo de un profesor \n/asesoria Muestro los días de asesorias de un profesor \n/fecha Muestro la fecha de un evento (ej: primeros previos) \n/paginaWeb Muestro la página web de un profesor \n")
            
        #LISTO LO REFERENTE A PROFESOR
        elif self._mensaje == "/profesor":
            show_keyboard = {'keyboard': [['Correo'],['Horario de Asesoría'],['Página Web']],'one_time_keyboard':True}
            self.sender.sendMessage("¿Qué información desea saber del profesor?",reply_markup=show_keyboard)
            self._variable = 1
        
             
        elif self._mensaje == "/fechas":
            show_keyboard = {'keyboard': [['Primeros Previos'],['Segundos Previos'],['Exámenes Finales'],['Habilitaciones']],'one_time_keyboard':True}
            self.sender.sendMessage(nombre + ", ¿De qué evento desea saber su fecha?",reply_markup=show_keyboard)
            self._variable = 2
            
      
        elif self._mensaje == "/recursos":
            show_keyboard = {'keyboard': [['Formato Carta del Programa'],['Formato Oficio del Programa'],['Formato Presentación']],'one_time_keyboard':True}
            self.sender.sendMessage("Escoge la información que quieres saber",reply_markup=show_keyboard)
            self._variable = 4
            
        elif self._mensaje == "/informacion":
            show_keyboard = {'keyboard': [['Misión'],['Visión']],'one_time_keyboard':True}
            self.sender.sendMessage("Escoge la información del Programa que quieres saber",reply_markup=show_keyboard)
            self._variable = 5
            
        elif self._mensaje == "/canal":
            print "Enviando mensaje a canal"
            bot.sendMessage('@IngSistemasUFPSCanal', controlador.enviarmensajecanal())
            
        elif self._mensaje == "/sugerencias":
            self.sender.sendMessage("Por favor escriba la sugerencia que se le desea enviar:")
            self._variable = 6

        elif self._mensaje == "/amigosAcademicos":
            show_keyboard = {'keyboard': [['Días'],['Materias']]}
            self.sender.sendMessage("Mostrar Amigos Académicos por Días o por Materias?",reply_markup=show_keyboard)
            self._variable = 7



        
        #INFORMACION REFERENTE AL PROFESOR
        elif self._variable == 1:
            
            respuesta = ""
            print self._clave

            if self._clave == "":
                print "entré por aquí"
                self._clave = self._mensaje
                hide_keyboard = {'hide_keyboard': True}
                self.sender.sendMessage("Escriba el nombre del profesor de cual desea obtener su " + self._clave,reply_markup=hide_keyboard) 
                
                      
            elif self._clave == "Correo":
                self.sender.sendChatAction('typing')
                try: 
                    respuesta = clases.profesor.correoPro(self._mensaje)
                except Exception:
                    self.sender.sendMessage("No encontré el " + self._clave + " del profesor solicitado")
                self.sender.sendMessage("El correo del Ing " + respuesta)
                self._variable = 0
                self._clave = ""
            
            elif self._clave == "Horario de Asesoría":
                self.sender.sendChatAction('typing')
                try: 
                    respuesta = controlador.asesoriaProfesor(self._mensaje) 
                except Exception:
                    self.sender.sendMessage("No encontré el " + self._clave + " del profesor solicitado")
                self.sender.sendMessage("La asesoria del Ing " + respuesta)
                self._variable = 0
                self._clave = ""
            
            elif self._clave == "Página Web":
                self.sender.sendChatAction('typing')
                try: 
                    respuesta = controlador.paginaProfesor(self._mensaje)
                except Exception:
                    self.sender.sendMessage("No encontré la " + self._clave + " del profesor solicitado")
                self.sender.sendMessage("La página Web del Ing " + respuesta)
                self._variable = 0
                self._clave = ""
            
           
       # CONDICIONES DE CONSULTA DE FECHAS DE PRIMEROS, SEGUNDOS PREVIOS ETC 
        elif self._variable == 2:       
                       
            if self._mensaje == "Primeros Previos":
                self.sender.sendChatAction('typing')
                respuesta = controlador.enviarFechas(self._mensaje) 
                self.sender.sendMessage("Los " + self._mensaje + " son desde " + respuesta)
                self._variable = 0
                self._clave = ""

            elif self._mensaje == "Segundos Previos":
                self.sender.sendChatAction('typing')
                respuesta = controlador.enviarFechas(self._mensaje) 
                self.sender.sendMessage("Los " + self._mensaje + " son desde " + respuesta)
                self._variable = 0
                self._clave = ""
                
            elif self._mensaje == "Habilitaciones":
                self.sender.sendChatAction('typing')
                respuesta = controlador.enviarFechas(self._mensaje) 
                self.sender.sendMessage("Las " + self._mensaje + " son desde " + respuesta)
                self._variable = 0
                self._clave = ""
                
            elif self._clave == "Exámenes Finales":
                self.sender.sendChatAction('typing')
                respuesta = controlador.enviarFechas(self._mensaje) 
                self.sender.sendMessage("Los " + self._mensaje + " son desde " + respuesta)
                self._variable = 0
                self._clave = ""

               
        elif self._variable == 3:
            self.sender.sendChatAction('typing')
            try: 
                respuesta = clases.profesor.paginaPro(self._mensaje)
            except Exception:
                self.sender.sendMessage("Escriba bien, no encontré nada")
            self.sender.sendMessage("La Página Web del Ing " + respuesta)
            self._variable = 0
            
        elif self._variable == 4:
            self.sender.sendChatAction('typing')
            try: 
                respuesta = clases.profesor.paginaPro(self._mensaje)
            except Exception:
                self.sender.sendMessage("Escriba bien, no encontré nada")
            self.sender.sendMessage("La Página Web del Ing " + respuesta)
            self._variable = 0
            
        elif self._variable == 5:
            self.sender.sendChatAction('typing')
            respuesta = clases.informacion.info(self._mensaje)
            hide_keyboard = {'hide_keyboard': True}
            self.sender.sendMessage(respuesta,reply_markup=hide_keyboard)
            self._variable = 0
            
        elif self._variable == 6:
            controlador.feedback(self._mensaje)
            self.sender.sendMessage("Gracias por ayudarnos a mejorar")
            self._variable = 0
            
        
	# self.sender.sendMessage(controlador.elizam(self._mensaje))    
print "En ejecucion"
            
TOKEN = ""

bot = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(botSistemas, timeout=30)),
])
canal()
bot.message_loop(run_forever=True)
time.sleep(10)

