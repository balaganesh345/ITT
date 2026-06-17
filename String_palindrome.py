def palindrome(s):
   n=len(s)
   i=0
   j=n-1
   flag = 1
   while i < j:
      if s[i] != s[j]:
         flag = 0
         break
      i = i + 1
      j = j -1

   if flag:
      return 1
   else:
      return 0


s=input("Enter the string :")

l = []
for i in range(len(s)+1):
   for j in range(i+1,len(s)):
      l.append(s[i:j])

print(l)
r = set()
for i in l:
   if len(i) > 2 and palindrome(i):
      r.add(i)
print(list(r))
