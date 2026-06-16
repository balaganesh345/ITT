l=[]
#print("Enter the no.of element : ")
n = int(input("Enter the no.of element :"))
print("Enter no:\t")
for i in range(n):
    t=int(input(" "))
    l.append(t)
print(l)

x = int(input("Enter insert no "))
l1 = len(l)
if l[0] > x:
    print(f" NULL , {l[0]}")
elif l[l1-1] < x:
    print(f"{l[l1-1]} , NULL")
else:
   for i in range(n):
       if x < l[i] and x > l[i-1]:
           print(f"{l[i-1]},{l[i]}")
       elif x == l[i]:
           print(f"{x} is already present")
       
