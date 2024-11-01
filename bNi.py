a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
c = int(input("Enter your last number: "))
sum_a = (a*(a + 1))/2
sum_b = (b*(b + 1))/a
sum_c = (c*(c + 1))/b
print(sum_a)
print(sum_b)
print(sum_c)
print("Using loop:")
total = 0
for i in range(1,a + 1),(1,b + 1),(c,c+1):
    total = total + i
    print("Iteration  number",i)
print(total)

    
    

