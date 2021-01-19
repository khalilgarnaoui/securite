import pyinputplus as pyip
import pyfiglet
import stdiomask

from Crypto.Cipher import AES

class SymmetricEncryption:
	'''
		1- encrypt my message
        2- decrypt my message 
	'''
    
	@classmethod
	def encrypt(cls, method='AES'):
		plaintext = pyip.inputStr('Entrer le message a crypter :  ')
		plaintext = str.encode(plaintext)

		key = stdiomask.getpass()
		key = str.encode(key)


		if(method=='AES'):
			if(len(key)<16):
				key = key + str.encode((16-len(key))*'a')
			elif(len(key)>16):
				key = key[:16]
			cipher = AES.new(key, AES.MODE_EAX)

			nonce = cipher.nonce
			ciphertext, tag = cipher.encrypt_and_digest(plaintext)

			print('nonce: \n'+ str(nonce), '\nciphertext: \n'+ str(ciphertext), '\ntag: \n'+ str(tag))
			return (nonce,ciphertext,tag)


	@classmethod
	def decrypt(cls, nonce=None, ciphertext=None, tag=None, method='AES'):
		key = stdiomask.getpass()
		key = str.encode(key)

		if(method=='AES'):
			if(len(key)<16):
				key = key + str.encode((16-len(key))*'a')
			elif(len(key)>16):
				key = key[:16]
			cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
			plaintext = cipher.decrypt(ciphertext)
			try:
				cipher.verify(tag)
				print("\nVotre message initial:", plaintext)
			except ValueError:
				print("Cle incorrecte ou message corrompu")



	@classmethod
	def menu(cls):
		ascii_banner = pyfiglet.figlet_format("CRYPTAGE DECRYPTAGE SYMETRIQUE")
		print(ascii_banner)

		while(True):
			print('\n')
			choice = pyip.inputMenu(['Crypter un message', 'Quitter'])
			if(choice=='Crypter un message'):
				method = pyip.inputMenu(['AES'])
				print(method)
				if(method=='AES'):
					nonce,ciphertext,tag = SymmetricEncryption.encrypt(method=method)
				else: 
					ciphertext = SymmetricEncryption.encrypt(method=method)
				
				print('\nVoulez vous decrypter votre message ? ')
				decrypt = pyip.inputMenu(['oui','non'])
				if(decrypt=='non'):
					continue
				elif(method=='AES'):
					SymmetricEncryption.decrypt(nonce,ciphertext,tag,method)
				

			else:
				return
				
