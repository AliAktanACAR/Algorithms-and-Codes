# Take a number n from the user and calculate the sum of the numbers from 1 to n

# Get a number from the user
n = int(input("Bir sayı girin: "))

# Calculate sum
toplam = 0
for i in range(1, n + 1):
    toplam += i

# Print result
print("1'den", n, "e kadar olan sayıların toplamı:", toplam)
