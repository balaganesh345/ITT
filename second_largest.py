l = []
print("Enter the no.of element in the array")
n = int(input("  "))
for i in range(n):
    t = int(input(f"Enter the element {i+1} : "))
    l.append(t)
print(l)

m = -1
prev = -1
for i in l:
    if i > m:
        prev = m
        m = i
    elif i > prev and m != i:
        prev = i

print(f"Largest Element in the Array {m}")
print(f"Second Largest Element in the Array {prev}")
