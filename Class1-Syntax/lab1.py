def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  else:
	max=int(num**(0.5))
	maxi=max+1
	digits = []
	for  i in range(1,maxi):
		number=int(num/(2**(max)))
		digits.append(str(number))
		if number<1: num=num
		else: num=num%(2**(max))
		max-=1
		
  return ''.join(digits)

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0' 
  else:
	max=int(num**(1/base))
	maxi=max+1
	digits = []
	for  i in range(0,maxi)[::-1]:
		number=int(num/(base**(i)))
		digits.append(str(number))
		num%=(base**(i))	
  return ''.join(digits)
  
def base_to_int(string, base):
	"""take a string-formatted number and its base and return the base-10 integer"""
	if string=="0" or base <= 0 : return 0 
	number= 0
	length=len(string)-1
	for letters in string:
		num=int(letters)*base**(length)
		length-=1
		number+=num
	return number

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  number1=base_to_int(str1,base1)
  number2=base_to_int(str2,base2)
  result = number1+number2
  return result 

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  number1=base_to_int(str1,base1)
  number2=base_to_int(str2,base2)
  result = number1*number2
  return result 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  digit=10**(len(str(num))-1)
  digitM='M'*(int(digit/1000))
  if digitM!='': num=num-digit
  
  
  number=num/digit
  
  
  result = ""
  return result
  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.