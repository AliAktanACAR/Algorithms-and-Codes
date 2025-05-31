# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print("Number:", i)

print("-" * 30)

# 2. Print even numbers from 0 to 20
for i in range(0, 21, 2):
    print("Even number:", i)

print("-" * 30)

# 3. Countdown from 10 to 1
for i in range(10, 0, -1):
    print("Countdown:", i)

print("-" * 30)

# 4. Print each character in a string
word = "Python"
for letter in word:
    print("Letter:", letter)

print("-" * 30)

# 5. Print elements of a list
fruits = ["Apple", "Pear", "Cherry", "Banana"]
for fruit in fruits:
    print("Fruit:", fruit)

print("-" * 30)

# 6. Print list elements with index numbers
for i in range(len(fruits)):
    print(f"{i + 1}. fruit: {fruits[i]}")

print("-" * 30)

# 7. Print squares of numbers from 1 to 5
for i in range(1, 6):
    print(f"{i}^2 =", i**2)

print("-" * 30)

# 8. Nested for loop (multiplication table 1–3)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# 9. Create a triangle using "*" characters
for i in range(1, 6):
    print("*" * i)

print("-" * 30)

# 10. Ask the user to enter 5 numbers and calculate the average
numbers = []
for i in range(5):
    n = int(input(f"Enter number {i+1}: "))
    numbers.append(n)

total = 0
for num in numbers:
    total += num

print("Average:", total / len(numbers))

print("-" * 30)

# 11. Check if a number is prime
number = int(input("Enter a number (to check if it's prime): "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime and number > 1:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
