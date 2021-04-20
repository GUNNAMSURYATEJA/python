if 2 > 5:
	print("Five is greater than two")

print(9>11) 
print(700==(5*5*28))

#no prints
x=float(5)
print(x)


 
#casting
psp2k= "pawan kalyan" 
print(type(psp2k))

hero1, hero2, hero3= "rock ", "mahesh ", "rajni "
print(hero1 + hero2 + hero3)
print(hero2)
print(hero3)

#list 
bill=['groceries', 'electricity', 'tickets', 'recharge']
p2500, p700,p500, p300 = bill
print(p2500)
print(p500)
print(p700)



#local variable : executes only under a function
#global variable: exceultes globally
#Global variables


y = "institute"
y = "university"


def function(): # this is a fucntion
 global y
 y = "college"  
 print("Bharath "+ y ) #1

function() # execute this function : 

print("Bharath "+ y) #2

# add two variable q=2, q=5, q=7  add u=14
def function2 ():
  q=7
  q=5
  q=2
  u=q+q
  print(u)
 
function2()



#int double float byte short boolean long
#tuple list dictionary range set



x3=5.9 #float
x4=int(x3)
print(x4)



value=str(44)
print(value)