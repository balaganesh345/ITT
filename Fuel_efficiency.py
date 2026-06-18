Write a program to calculate the maximum distance that can be covered by a car having a given
fuel amount. A set of speeds and corresponding fuel consumption are given as input.

Eg: Input : 3
Speed : 250 220 240 (km/Hr)
Consumption: 5litres 4litres 3litres
Capacity : 50litres
Output : 4000 km

code:

n = int(input("Enter the no.of input :"))
speed = []
consumption = []
for i in range(n):
    s = int(input(f"\nEnter the input for speed {i+1} : "))
    c = int(input(f"Enter the input for fuel consuption {i+1} : "))
    speed.append(s)
    consumption.append(c)
print("\n")
print("Speed \t Consumption ")
best_efficiency = []
for i in range(n):
    print(f"{speed[i]} \t {consumption[i]}")
    t = speed[i] / consumption[i]
    best_efficiency.append(t)
b = sorted(best_efficiency)
b1 = b[n-1]
print("\nResult\n ---------------------------")
print(f"Best Efficiency {b1}")
print(f"Total Distance {b1 * 50}")


Enter the no.of input :3

Enter the input for speed 1 : 250
Enter the input for fuel consuption 1 : 5

Enter the input for speed 2 : 220
Enter the input for fuel consuption 2 : 4

Enter the input for speed 3 : 240
Enter the input for fuel consuption 3 : 3


Speed    Consumption
250      5
220      4
240      3

Result
 ---------------------------
Best Efficiency 50.0
Total Distance 2500.0
PS C:\Users\GBL\Documents\itt> python .\efficiency.py
Enter the no.of input :3

Enter the input for speed 1 : 250
Enter the input for fuel consuption 1 : 5

Enter the input for speed 2 : 220 
Enter the input for fuel consuption 2 : 4

Enter the input for speed 3 : 240
Enter the input for fuel consuption 3 : 3


Speed    Consumption
250      5
220      4
240      3

Result
 ---------------------------
Best Efficiency 80.0
Total Distance 4000.0
