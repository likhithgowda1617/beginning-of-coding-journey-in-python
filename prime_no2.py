a=list()
for i in range(2,51):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag!=1:
        
        a.append(i)
print("list of prime numbers:",a)
print("length of this list:",len(a))            