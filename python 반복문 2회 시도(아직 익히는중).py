Python 3.7.1 (default, Dec 10 2018, 22:09:34) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print('*',end='')

	
*****
>>> i
4
>>> for i in range(4):
	for j in range(5):
		print('*','end='')
		      
SyntaxError: EOL while scanning string literal
>>> for i in range(4):
	for j in range(5):
		      print('*',end="")
		print(end='')
		      
SyntaxError: unindent does not match any outer indentation level
>>> 
		      
>>> for i in range(4):
	for j in range(5):
		      print('*',end="")

		      
********************
>>> for i in range(4):
	for j in range(5):
		      print('*',end="")
	print('')

		      
*****
*****
*****
*****
>>> for i in range(4):
	for j in range(5):
		      print('*',end="")
	        print('')
		      
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(4):
	for j in range(5):
		      print('*',end="")
		      print('')

		      
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
>>> for i in range(5):
	print('*',end="")
		      for j in range(4):
		      
SyntaxError: unexpected indent
>>> for i in range(4):
		      for j in range(5):
			print('*',end="")
		      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for i in range(4):
	for j in range(5):
		print('*',end="")
	print('')

		      
*****
*****
*****
*****
>>> for i in range(5):
	for j in range(j+1)
		      
SyntaxError: invalid syntax
>>> for i in range(5):
	for j in range(j+1):
		print('*',end="")
	print('')

		      
*****
*****
*****
*****
*****
>>> for i in range(5):
	for j in range(j+1):
		print('*',end="")
	print('j+1')

		      
*****j+1
*****j+1
*****j+1
*****j+1
*****j+1
>>> for i in range(5):
	for j in range(i+1):
		print('*',end="")
	print('')

		      
*
**
***
****
*****
>>> for i in range(5):
	for j in range(i):
		print('*',end="")
	print('')

		      

*
**
***
****
>>> range(4)
		      
range(0, 4)
>>> print(range(4))
		      
range(0, 4)
>>> list(range(4))
		      
[0, 1, 2, 3]
>>> for i in range(5):
	for j in range(4-i):
		print("*",end="")
	print('')

		      
****
***
**
*

>>> for i in range(5):
	for j in range(3-i):
		print("*",end="")
	print('')

		      
***
**
*


>>> for i in range(5):
	for j in range(5-i):
		print("*",end="")
	print('')

		      
*****
****
***
**
*
>>> for i in ragne(5):
	for j in range(4-i,"i",end="")
		      
SyntaxError: invalid syntax
>>> for i in range(5):
	for j in range(4-i,"i",end=""):
		print("")

		      
Traceback (most recent call last):
  File "<pyshell#61>", line 2, in <module>
    for j in range(4-i,"i",end=""):
TypeError: range() takes no keyword arguments
>>> for j in range(5):
        print(' '*j + '*' * (2 * (5 - j) - 1), end='\n')

		      
*********
 *******
  *****
   ***
    *
>>> for j in range(5):
        print(' '*j + '*' * (2 * (5 - j) - 1), end='n')

		      
*********n *******n  *****n   ***n    *n
>>> for i in apart:
	for j in i:
		l = 0
		for k in arrears:
			if ( j == k ):
				l += 1
		if ( l == 0 ):
			print(j)

		      
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    for i in apart:
NameError: name 'apart' is not defined
>>> apart=[[101,102,103,104],[201,202,203,204],[301,302,303,304],[401,402,403,404]]
		      
>>> aprat
		      
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    aprat
NameError: name 'aprat' is not defined
>>> apart
		      
[[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
>>> arrears=[101,203,301,404]
		      
>>> for floor in apart:
	for ben in floor:
		if ben in arrears:
		      continue
		else:
		      print("Newspaper delivery: ", house)

		      
Traceback (most recent call last):
  File "<pyshell#78>", line 6, in <module>
    print("Newspaper delivery: ", house)
NameError: name 'house' is not defined
>>> for floor in apart:
        for house in floor:
                if house in arrears:
                        continue
                else:
                        print("Newspaper delivery: ", house)

		      
Newspaper delivery:  102
Newspaper delivery:  103
Newspaper delivery:  104
Newspaper delivery:  201
Newspaper delivery:  202
Newspaper delivery:  204
Newspaper delivery:  302
Newspaper delivery:  303
Newspaper delivery:  304
Newspaper delivery:  401
Newspaper delivery:  402
Newspaper delivery:  403
>>> apart
		      
[[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
>>> for floor in apart:
	for bad in floor:
		if bad in arreares:
		       continue
		else:
		       print("newspaper delivery: ",house)

		      
Traceback (most recent call last):
  File "<pyshell#88>", line 3, in <module>
    if bad in arreares:
NameError: name 'arreares' is not defined
>>> for floor in apart:
	for bad in floor:
		if bad in arreares:
		        continue
		else:
		        print("newspaper delivery: ",house)

		      
Traceback (most recent call last):
  File "<pyshell#90>", line 3, in <module>
    if bad in arreares:
NameError: name 'arreares' is not defined
>>> for floor in apart:
	for bad in floor:
		if bad in arreares:
		         continue
		else:
		         print("newspaper delivery: ",house)

		      
Traceback (most recent call last):
  File "<pyshell#92>", line 3, in <module>
    if bad in arreares:
NameError: name 'arreares' is not defined
>>> for floor in apart:
	for bad in floor:
		if bad in arrears:
		         continue
		else:
		         print("newspaper delivery: ",house)

		      
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
>>> arrears
		      
[101, 203, 301, 404]
>>> apart
		      
[[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
>>> for floor in apart:
        for house in floor:
                if house in arrears:
                        continue
                else:
                        print("Newspaper delivery: ", house)

		      
Newspaper delivery:  102
Newspaper delivery:  103
Newspaper delivery:  104
Newspaper delivery:  201
Newspaper delivery:  202
Newspaper delivery:  204
Newspaper delivery:  302
Newspaper delivery:  303
Newspaper delivery:  304
Newspaper delivery:  401
Newspaper delivery:  402
Newspaper delivery:  403
>>> for floor in apart:
	for bad in floor:
		if bad in arrears:
		          continue
		else:
		          print("newspaper delivery: ",house)

		      
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
newspaper delivery:  404
>>> for floor in apart:
        for a in floor:
                if a in arrears:
                        continue
                else:
                        print("Newspaper delivery: ", house)

		      
Newspaper delivery:  404
Newspaper delivery:  404
Newspaper delivery:  404
Newspaper delivery:  404
Newspaper delivery:  404
Newspaper delivery:  404
Newspaper delivery:  404
Newspaper delivery:  404
Newspaper delivery:  404
Newspaper delivery:  404
Newspaper delivery:  404
Newspaper delivery:  404
>>> for floor in apart:
        for a in floor:
                if a in arrears:
                        continue
                else:
                        print("Newspaper delivery: ", a)

		      
Newspaper delivery:  102
Newspaper delivery:  103
Newspaper delivery:  104
Newspaper delivery:  201
Newspaper delivery:  202
Newspaper delivery:  204
Newspaper delivery:  302
Newspaper delivery:  303
Newspaper delivery:  304
Newspaper delivery:  401
Newspaper delivery:  402
Newspaper delivery:  403
>>> for i in range(3):
		      print("대신증권")

		      
대신증권
대신증권
대신증권
>>> def print_ntimes():
		      print("대신증권")

		      
>>> print_ntimes
		      
<function print_ntimes at 0x01F666A8>
>>> print(print_ntimes)
		      
<function print_ntimes at 0x01F666A8>
>>> print_ntimes()
		      
대신증권
>>> print
		      
<built-in function print>
>>> def myaverage(a,b):
		      average(a,b)

		      
>>> myaverage
		      
<function myaverage at 0x01F66660>
>>> myaverage(1,5)
		      
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    myaverage(1,5)
  File "<pyshell#117>", line 2, in myaverage
    average(a,b)
NameError: name 'average' is not defined
>>> average(1,4)
		      
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    average(1,4)
NameError: name 'average' is not defined
>>> 
		      
>>> average
		      
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    average
NameError: name 'average' is not defined
>>> 
