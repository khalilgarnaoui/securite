import base64 ,hashlib
import string
import re
import pyfiglet
import pyinputplus as pyip

class Encoding:
	'''
		1- encode my message
		2- decode my message
	'''

	@classmethod
	def encode(cls,data, method):
		if(method in ['utf8','ascii']):
			encoded_text = str.encode(data,encoding=method)
			print('Votre message code est : ' + encoded_text)
			return(encoded_text)
		
		elif(method == 'base64'):
			message_bytes = data.encode('ascii')
			base64_bytes = base64.b64encode(message_bytes)
			base64_message = base64_bytes.decode('ascii')
			print('Votre message code est : ' + base64_message)
			return(base64_message)
		
		elif(method == 'base32'):
			message_bytes = data.encode('ascii')
			base32_bytes = base64.b32encode(message_bytes)
			base32_message = base32_bytes.decode('ascii')
			print('Votre message code est : ' + base32_message)
			return(base32_message)
			
		elif(method=='base16'):
			message_bytes = data.encode('ascii')
			base16_bytes = base64.b32encode(message_bytes)
			base16_message = base16_bytes.decode('ascii')
			print('Votre message code est : ' + base16_message)
			return(base16_message)

	@classmethod
	def decode(cls, encoded_data, method):
		if(method in ['utf8','ascii']):
			data = str.decode(encoded_data,encoding=method)
			print('Votre message decode est : ' + data)
			return(data)
		
		elif(method == 'base64'):
			message_bytes = encoded_data.encode('ascii')
			base64_bytes = base64.b64decode(message_bytes)
			base64_message = base64_bytes.decode('ascii')
			print('Votre message decode est : ' + base64_message)
			return(base64_message)
		
		elif(method == 'base32'):
			message_bytes = encoded_data.encode('ascii')
			base32_bytes = base64.b32decode(message_bytes)
			base32_message = base32_bytes.decode('ascii')
			print('Votre message decode est : ' + base32_message)
			return(base32_message)
			
		elif(method=='base16'):
			message_bytes = encoded_data.encode('ascii')
			base16_bytes = base64.b32decode(message_bytes)
			base16_message = base16_bytes.decode('ascii')
			print('Votre message decode est : ' + base16_message)
			return(base16_message)


	

	@classmethod
	def menu(cls):
		ascii_banner = pyfiglet.figlet_format("CODAGE")
		print(ascii_banner)

		while(True):
			print('\n')
			choice = pyip.inputMenu(['Coder un message', 'quitter'])
			if(choice=='Coder un message'):
				data = pyip.inputStr('Entrez le message a coder : \n')
				method = pyip.inputMenu(['utf8', 'ascii', 'base16', 'base32', 'base64'])
				encoded_data = Encoding.encode(data,method)

				print('\nVoulez vous decoder votre message ? : ')
				decode = pyip.inputMenu(['oui','non'])
				if(decode=='non'):
					continue
				else :
					Encoding.decode(encoded_data , method)
			
			else:
				return

