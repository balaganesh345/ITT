s = input("Enter the input string : ")
d = {}
l = list(s)
#print("Your list of letters:", l)

for letter in l:
    if letter in d:
        d[letter] += 1 
    else:
        d[letter] = 1   # Set count to 1 if it's a new letter

#print("Letter counts dictionary:", d)
result = ""
for key,value in d.items():
     result = result + key
     result = result + str(value)
print("\nCompressed String : \t",result)

#decompress the string
decompress_string = ""
for k,v in d.items():
    for i in range(v):
       decompress_string =decompress_string + k
print("\nDecompressed String : \t",decompress_string)


     

