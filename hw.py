n = int(input("Enter a number: "))
odd_numbers = [i for i in range(n) if i % 2 != 0]
print("Odd numbers below", n, ":", odd_numbers)