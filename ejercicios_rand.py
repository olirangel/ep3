

#ejercicio52
import random 
n1= random.randint(1,100)
print(n1)

#ejercicio53
import random 
fruta= random.choice (['manzana', 'naranja', 'platano'])
print(fruta)

#ejercicio54
import random 
a= random.choice(["h", "t"])
r1=input("escribe h o t: ")
if a== r1: 
    print(adivinaste!!)
else: 
    print(no acertaste!!)
if a== "h": 
    print("was heads")
else: 
    print("was tails")

#ejercicio55
import random 
n1= random.randint(1,5)
r1= int(input("escriba un número: "))
if r1 < n1: 
    r1=int(input("número muy bajo, escribe otro: "))
    if r1=n1: 
        print(adivinaste!)
    else: 
        print(perdiste)
if r1 > n1: 
    r1=int(input("número muy alto, escribe otro: "))
    if r1=n1: 
        print(adivinaste!)
    else: 
        print(perdiste)
if r1=n1: 
    print(ganaste!)
    
#ejercicio56 
import random 
n1= random.randinr(1,10)
r1= false
while r1 == false:
    a = int(input("escribe un número: "))
    if a==n1:
        r1= true

#ejercicio57
import random 
num = random.randint()
c = false
while c == false: 
    a= int(input("escribe un número: "))
    if c==num: 
        c==true 
    elif a > num: 
        print("muy alto: ")
    else
    print ("muy bajo")

#ejercicio58 
import random 
a= 0
for i in range (1,6)
    n1=random.randint(1,50)
    n2=random.randint(1,50)
    r1= n1 + n2
    r2= int(input(n1, "+", n2, "= ")
    if r2==r1: 
        a=a+1
print("llevas", a, "bien")



    

