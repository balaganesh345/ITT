Loyalty point – Given a customer and his purchased amount, find his
points.
Example: customer reference
A - B, X, Y, Z
B – C, P, Q, R
C – D, M, N, O
that is, customer A refers B, X, Y, Z and customer B refers C,P, Q, R and
customer C refers D, M, N, O. For every 1000 rupees, 2 points to the
customer who purchases, 3 points to the one who referred him and 1 point
to the refferees in the next level.
Input : D 3000
ouput : D 6 C 9 B 3


code:
#python code to solve this problem
n = int(input("Enter the no.of customers : "))
customers = {}
for i in range(n):
    customer_name = input("Enter the customer name : ")
    n_c = int(input("Enter the no.of referred customer : "))
    l = []
    for i in range(n_c):
        r_name = input("Enter the name of the referred customer :")
        l.append(r_name)
    customers[customer_name]=l
print(customers)

point_current = 2
point_refer = 3
point_next = 1

#input 
c = input("Enter the customer name : ")
amount = int(input("Enter the Amount : "))

result_amount = amount / 1000
flag =0
for key,value in customers.items():
       if c in value:
            print(f"{c} {result_amount*point_current}")
            key_refer = key
            print(f"{key_refer} {result_amount*point_refer}")
            for key1,value1 in customers.items():
                 if key_refer in value1:
                      print(f"{key1} {result_amount}")
                      flag = 1
if flag == 0:
     print("No next level customer is present")

output:
PS C:\Users\GBL\Documents\itt> python .\cost.py
Enter the no.of customers : 3
Enter the customer name : A
Enter the no.of referred customer : 4
Enter the name of the referred customer :B
Enter the name of the referred customer :X
Enter the name of the referred customer :Y
Enter the name of the referred customer :Z
Enter the customer name : B
Enter the no.of referred customer : 4
Enter the name of the referred customer :C
Enter the name of the referred customer :P
Enter the name of the referred customer :Q
Enter the name of the referred customer :R
Enter the customer name : C
Enter the no.of referred customer : 4
Enter the name of the referred customer :D
Enter the name of the referred customer :M
Enter the name of the referred customer :N
Enter the name of the referred customer :O
{'A': ['B', 'X', 'Y', 'Z'], 'B': ['C', 'P', 'Q', 'R'], 'C': ['D', 'M', 'N', 'O']}
Enter the customer name : D
Enter the Amount : 3000
D 6.0
C 9.0
No next level customer is present
B 3.0
No next level customer is present
PS C:\Users\GBL\Documents\itt> python .\cost.py
Enter the no.of customers : 3
Enter the customer name : A
Enter the no.of referred customer : 4
Enter the name of the referred customer :B
Enter the name of the referred customer :X
Enter the name of the referred customer :Y
Enter the name of the referred customer :Z
Enter the customer name : B
Enter the no.of referred customer : 4
Enter the name of the referred customer :C
Enter the name of the referred customer :P
Enter the name of the referred customer :Q
Enter the name of the referred customer :R
Enter the customer name : C
Enter the no.of referred customer : 4
Enter the name of the referred customer :D
Enter the name of the referred customer :M
Enter the name of the referred customer :N
Enter the name of the referred customer :O
{'A': ['B', 'X', 'Y', 'Z'], 'B': ['C', 'P', 'Q', 'R'], 'C': ['D', 'M', 'N', 'O']}
Enter the customer name : B
Enter the Amount : 2000
B 4.0
A 6.0
No next level customer is present

