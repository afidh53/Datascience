t=(10,"hello",3.14,True)

print("orginal tuple:",t)
print("first three elements :",t[:3])
print("first three elements :",t[-2:])
print("\n tuple elements are :")
for i in t:
    print(i)
p=(121,"python",9.6)
print("\n packed tuple is: " ,p)

a,b,c=p
print("after unpacking")
print("a= ",a)
print("b= ",b)
print("c= ",c)

