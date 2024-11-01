n = int(input("Enter a number : "))
sum = (n*(n + 1))/2
print(sum)
print("Using for loop")
total = 0
for i in range(1,n + 1):
    total = total + i
    print("Iteration  number",i)
print(total)
