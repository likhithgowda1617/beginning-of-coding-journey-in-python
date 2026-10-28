#a=[10,15,34]
#a.append(5)
#print(a)
#a.sort()
#print(a) 
#a.sort(reverse=True)
#print(a)
#a.insert(0,24)
#print(a)
#a.pop(2)
#print(a)



#b=["map","India","Usa"]
#b.sort()
#print(b)
#b.reverse()
#print(b)
#b.remove("map")
#print(b)

#example for the list operations


#a=list()
#for i in range(3):
#    movie=input("please enter your favourite movie :")
#    a.append(movie)
#print(a)

a=[1,2,3,2,1]
b=[1,2,3,4,5]
copy_list=a.copy()
copy_list.reverse()
if copy_list==a:
    print("palindrome")
else:
    print("not palindrome")

