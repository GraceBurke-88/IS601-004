a = [1,2,5,63,3,23,6,7,6,8,5,34,7,8]
c = {}

for i in a:
    if i in c.keys():
        c[i] += 1
    else:
        c[i] = 1


print(f"{c}")
print(c) #confused about the f




