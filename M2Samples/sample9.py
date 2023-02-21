a = ["Bob","Bill"]
c = {}
#print sum of asci values

for i in a:
    num = 0
    #c[i] = [(num + ord(x)) for x in i]
    # in line for loop will give an array not do the math
    
    for x in i:
        num += ord(x)
    c[i] = num

    
print(f"{c}")
#print(c)

