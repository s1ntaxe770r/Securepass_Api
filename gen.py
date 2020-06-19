from string import *
import random

class Password:
 	@classmethod
 	def generate(cls,size=16):
 		characters = ascii_letters + punctuation +  digits + ascii_lowercase
 		choice = random.SystemRandom()
 		password =  "".join(choice.choice(characters)
                    for i in range(size))
 		return str(password)
