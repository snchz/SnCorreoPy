import smtplib, ssl, imaplib
from email.mime.text import MIMEText

__version__='1.0.2.dev0'
__author__='Snchz'
__license__='BDD'
__doc__='Doc'


class SNCorreo:
	def __init__(self,direccionServidorSMTP,puertoSMTP,direccionServidorIMAP,puertoIMAP,usuario,password):
		contextoSSL1=ssl.create_default_context()
		self.servidorOUT=smtplib.SMTP_SSL(direccionServidorSMTP,puertoSMTP,context=contextoSSL1)
		self.servidorOUT.login(usuario,password)
		
		contextoSSL2=ssl.create_default_context()
		self.servidorIN=imaplib.IMAP4_SSL(direccionServidorIMAP,puertoIMAP)#,context=contextoSSL2)
		self.servidorIN.login(usuario,password)
		self.servidorIN.select('INBOX')
	def crearMensaje(self,emisor, destinatario, asunto, textoMensaje):
		mensaje=MIMEText(textoMensaje)
		mensaje['to']=destinatario
		mensaje['from']=emisor
		mensaje['subject']=asunto
		return mensaje
	def enviarMensaje(self,mensajeMIME):
		self.servidorOUT.sendmail(mensajeMIME['from'],mensajeMIME['to'],mensajeMIME.as_string())
	def leerCorreos(self):
		estado, respuesta=self.servidorIN.search(None,'UNSEEN')
		msg_sin_leer=respuesta[0].split()
		print(len(msg_sin_leer))

		for eid in msg_sin_leer:
                        _, respuesta = self.servidorIN.fetch(eid,'(UID BODY[TEXT])')
                        print(respuesta[0][1])

		#Marcar como leidos
		for eid in msg_sin_leer:
                        self.servidorIN.store(eid,'+FLAGS','\Seen')
		
	def cerrarSesion(self):
		self.servidorOUT.quit()
		self.servidorIN.quit()

