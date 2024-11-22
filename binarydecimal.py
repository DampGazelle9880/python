bin = int(input("Enter a binary number: "))
result = 0
i = 0
while bin !=0:
    digit = bin % 10
    result = result + 2**i
    i = i + 1
    bin = bin//10
print(result)

    