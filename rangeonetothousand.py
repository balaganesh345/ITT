#find between the words between 1 1000

words_map = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
n=int(input("Enter the number to convert into word : "))
t=n
count = 0
h = []
while n > 0:
    r= n % 10
    count = count + 1
    h.append(r)
    n = n //10   
#print(count)
f = 0
if count == 0:
    print("Zero")
    f = 1
if count == 1:
    print(words_map[t-1])
elif count == 2:
    z = t % 10
    z1 = t // 10
    if z == 0:
        print(tens[z1-1])
    elif t > 10 and t < 20:
        print(teens[t-11])
    else:
        print(f"{tens[z1-1]} {words_map[z-1]}")
elif count == 3:
   if h[1] == 0 and h[0] == 0:
        print(f"{words_map[h[2]-1]} Hundred")     
   elif h[0] == 0:
      print(f"{words_map[h[2]-1]} Hundred {tens[h[1]-1]}")
   elif h[1] == 1:
        # t % 100 extracts the last two digits cleanly (e.g., 12, 15)
        print(f"{words_map[h[2]-1]} Hundred {teens[(t % 100) - 11]}")
   elif h[1] == 0:
       print(f"{words_map[h[2]-1]} Hundred {words_map[h[0]-1]}")
        
   else:
      print(f"{words_map[h[2]-1]} Hundred {tens[h[1]-1]} {words_map[h[0]-1]}")

else:
    if f == 0:
       print("One Thousand")
   

       



