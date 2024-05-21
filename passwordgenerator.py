import string
import random
import array 

# maximum length of password needed 
# this can be changed to suit your password length 
MAX_LEN = int(input("Enter password length: "))


# declare arrays of the character that we need in out password 
# Represented as chars to enable easy string concatenation 
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
					'z'] 

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
					'Z'] 

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

temp_pass = ("")

 
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 


for x in range(MAX_LEN): 
	temp_pass = temp_pass + random.choice(COMBINED_LIST) 

	# convert temporary password into array and shuffle to 
	# prevent it from having a consistent pattern 
	# where the beginning of the password is predictable 
	temp_pass_list = array.array('u', temp_pass) 
	random.shuffle(temp_pass_list) 

# traverse the temporary password array and append the chars 
# to form the password 
password = "" 
for x in temp_pass_list: 
		password = password + x 
		
# print out password 
print(password)
