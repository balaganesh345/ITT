s1 = input("Enter the first string : ")
s2 = input("Enter the second string : ")
result11 = ""
result22 = ""
if len(s1) != len(s2):
    print("The strings are not ")   
else:
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        else:
            result11 = result11 + s1[i]
            result22 = result22 + s2[i]

print("The first string is : ", result11)
print("The second string is : ", result22)
     
    
