def myfunc(mystring):
   result_string = ''
   for i in range(len(mystring)):
       letter = mystring[i]
       if(i%2 == 0):
           result_string = result_string+letter.upper()
       else:
           result_string = result_string + letter.lower()
   return result_string

print(myfunc("Ramana"))