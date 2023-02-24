'''
#running total/value called ans
ans = 0
'''
''' gnb5 implemented on 2/24/23 
#function for addition
def add(num1,num2):
    ans = num1 + num2
    print(num1, "+", num2, '=', ans)
    return ans
'''
#test
#print(add(1,2))

''' gnb5 implemented on 2/24/23 
#function for subtraction
def sub(num1,num2):
    ans = num1 - num2
    print(num1, "-", num2, '=', ans)
    return ans
'''
#test
#print(sub(1,2))

''' gnb5 implemented on 2/24/23 
#function for multiplication
def mult(num1,num2):
    ans = num1 * num2
    print(num1, "x", num2, '=', ans)
    return ans
'''
#test
#print(mult(1,2))

''' gnb5 implemented on 2/24/23 
#function for division
def div(num1,num2):
    ans = num1 / num2
    print(num1, "/", num2, '=', ans)
    return ans
'''
#test
#print(div(1,2))

''' gnb5 implemented on 2/24/23 
#Define a "main" logic to run when the program runs
#Ask for user input
while True:
    calc = input("Enter a calculation or exit to quit: ")

    #User can input exit to stop using the calculator 
    #use calc.lower in case they input 'Exit or EXIT'
    if calc.lower() == 'exit':
        print("Bye now, exiting program.")
        break

    #if the user inputs text 'ans' need to convert that to a string of the ans variable
    if 'ans' in calc:
        calc = calc.replace('ans', str(ans))

    #If/elif/else look for +,-,*,/ 
    #if they find an operand they split at the operand to distinguish num1 and num2 
    #the numbers are then passed through the respective functions
    if '+' in calc:
        print('Calculating addition')
        num1, num2 = calc.split('+')
        ans = add(float(num1),float(num2))
    
    elif '-' in calc:
        print('Calculating subtraction')
        num1, num2 = calc.split('-')
        ans = sub(float(num1),float(num2))

    elif '*' in calc:
        print('Calculating multiplication')
        num1, num2 = calc.split('*')
        ans = mult(float(num1),float(num2))

    elif '/' in calc:
        print('Calculating division')
        num1, num2 = calc.split('/')
        ans = div(float(num1),float(num2))

    #if no valid oeprand is found
    else:
        print('Sorry, not a valid operation.')



Notes
Issue 1:  
    If input is 'ans + 2' it does not realize 'ans' is a variable just 
    considers it as a string -->
    ValueError: could not convert string to float: 'ans'

Issue 2: had everything as else statements instead of elif, which was causing the else statement to execute each time
W3 schools: 'Use else if to specify a new condition to test, if the first condition is false'
Now the single else statment will only execture if all other coditions are false
'''