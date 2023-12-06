a=[1,2,3,10,34]
print(10 in a)
print(10 not in a)

b={"Apple":"fruit",1:"Number",35:"Float"}
print(1 not in b)

a,b=36.5,36.5
c=a is b 
print(c)
a=(id(a))
b=(id(b))
c= a is b 
print(c)

a =[1,2,3,1]
b =[1,2,3,1]
c= a is b
print(c)

a =(1,2,3,1)
b =(1,2,3,1)
c= a is b
print(c)

a ={1:"2",3:"2"}
b ={1:"2",3:"2"}
c= a is b
print(c)