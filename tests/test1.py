import sncorreopy

#parametros para la conexion
SERVIDOR_SMTP = 'smtp.gmail.com'
PUERTO_SMTP_SSL = 465 #SSL
SERVIDOR_IMAP = 'imap.gmail.com'
PUERTO_IMAP_SSL = 993 #SSL
USUARIO = input('Introduce usuario: ')
PASSWORD = input('Introduce password: ')

#test
sncorreo=SNCorreo(SERVIDOR_SMTP,PUERTO_SMTP_SSL,USUARIO,PASSWORD)
destinatario = input('Introduce destinatario: ')
mensaje=sncorreo.crearMensaje(USUARIO,destinatario,'Test','Esto es un test')
sncorreo.enviarMensaje(mensaje)
sncorreo.leerCorreos()
