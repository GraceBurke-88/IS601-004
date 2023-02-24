#running total/value called ans
ans = 0

''' gnb5 implemented on 2/24/23 '''
#function for addition
def add(num1,num2):
    ans = num1 + num2
    print(num1, "+", num2, '=', ans)
    return ans

#test
print(add(1,2))

''' gnb5 implemented on 2/24/23 '''
#function for subtraction
def sub(num1,num2):
    ans = num1 - num2
    print(num1, "-", num2, '=', ans)
    return ans

#test
print(sub(1,2))

''' gnb5 implemented on 2/24/23 '''
#function for multiplication
def mult(num1,num2):
    ans = num1 * num2
    print(num1, "x", num2, '=', ans)
    return ans

#test
print(mult(1,2))

''' gnb5 implemented on 2/24/23 '''
#function for division
def div(num1,num2):
    ans = num1 / num2
    print(num1, "/", num2, '=', ans)
    return ans

#test
print(div(1,2))

#Define a "main" logic to run when the program runs
#Ask for user input

#operator = input("Enter math:")
#ans = 0

print(type(ans))

while True:
    calc = input("Enter the your calculation or exit to quit: ")

    #User can input exit to stop using the calculator 
    #use calc.lower in case they input 'Exit or EXIT'
    if calc.lower() == 'exit':
        print("Bye now, exiting program.")
        break

    #If input is 'ans + 2' it does not realize 'ans' is a variable just 
    #considers it as a string -->
    #ValueError: could not convert string to float: 'ans'
    if 'ans' in calc:
        calc = calc.replace('ans', str(ans))

    if '+' in calc:
        print('Calculating addition')
        num1, num2 = calc.split('+')
        ans = add(float(num1),float(num2))
        print(ans)

    else:
        print('The calculation is not a valid operation.')


