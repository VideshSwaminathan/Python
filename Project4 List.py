e=list(map(int,input().split(',')))
even=[]
odd=[]
print(e)
for i in e:
    if (i%2 == 0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)