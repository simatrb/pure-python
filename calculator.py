num1 = float(input( 'Enter a number :'))

operator= input ( 'select ( + , - ,* , /) :')

num2 = float ( input(' Enter a number :'))

if operator == '+' :
    print (num1 + num2)
elif operator == '-' :
    print (num1 - num2) 
elif operator == '*' :
    print (num1 * num2)
elif operator == '/' :
    print (num1 / num2)
else :
    print ('Error')
