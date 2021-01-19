import base64 ,hashlib
import pyinputplus as pyip
import string
import pyfiglet

class Hashing:
	'''
		1- string to base_64
		2- string to multidigest(MD5, SHA1, SHA256, SHA384, SHA512, RIPEMD-160)
		3- Hash Password Cracker (MD5, SHA1, SHA256, SHA384, SHA512, RIPEMD-160)
		4- secure password generator
	'''

	@classmethod
	def choose_method(cls):
		method = pyip.inputMenu(list(hashlib.algorithms_guaranteed))
		return method

	def base64_encoder(self,text):
		text_bytes = text.encode("ascii")
		base64_bytes = base64.b64encode(text_bytes)
		return base64_bytes

	@classmethod
	def text_to_hash(cls,text,method):
		encoded_text = text.encode()
		if(method.upper() == 'MD5'):
			return hashlib.md5(encoded_text).hexdigest()
		if(method.upper() == 'SHA1'):
			return hashlib.sha1(encoded_text).hexdigest()
		if(method.upper() == 'SHA256'):
			return hashlib.sha256(encoded_text).hexdigest()
		if(method.upper() == 'SHA384'):
			return hashlib.sha384(encoded_text).hexdigest()
		if(method.upper() == 'SHA512'):
			return hashlib.sha512(encoded_text).hexdigest()

	@classmethod
	def multidigest(cls , text):
		method = Hashing.choose_method()
		hash = Hashing.text_to_hash(text,method)
		return hash
	
	@classmethod
	def password_cracker(cls, hash):
		methods = list(hashlib.algorithms_guaranteed)
		with open('pentbox-wlist.txt', 'r+') as f:
			passwords = f.read().splitlines()
		for password in passwords: 
			for method in methods:
				if( Hashing.text_to_hash(password,method) == hash ):
					return password

		return 'Desole, on n\'a pas trouve le mot de passe'


	@classmethod
	def hash_menu(cls):
		ascii_banner = pyfiglet.figlet_format("HACHAGE")
		print(ascii_banner)

		while(True):
			print('\n')
			choice = pyip.inputMenu(['Hacher un message','Quitter'])
			if(choice=='Hacher un message'):
				text = pyip.inputStr('Entrer le message a hacher : \n')
				hashed_text = Hashing.multidigest(text)
				print('Le message hache est : ' + hashed_text)
			else:
				return

	@classmethod
	def crack_menu(cls):
		ascii_banner = pyfiglet.figlet_format("CRACKER MOT DE PASSE")
		print(ascii_banner)

		while(True):
			print('\n')
			choice = pyip.inputMenu(['Cracker','Quitter'])
			if(choice=='Cracker'):
				hash = pyip.inputStr('Entrer le message a cracker : \n')
				cracked_hash = Hashing.password_cracker(hash)
				print('Le message cracke est :  ' + cracked_hash)
			else:
				return