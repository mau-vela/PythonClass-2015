#Write a function that takes an integer as an input and returns a script with the ordinal number
#For example, for 1, it should give "1st"
#Write a test for your function

def ordinal(number):
	try:
		if number %1==0:
			pass
		else:
			raise Exception	
	except TypeError:
		raise TypeError, "Enter a number!"
	except:
		raise TypeError, "No decimals!"			
	
	last=number%10
	last2=number%100
	if last==1 and last2!=11: string="st"
	elif last==2 and last2!=12: string="nd"
	elif last==3 and last2!=13: string="rd"
	else: string="th"
	return str(number)+string
	

