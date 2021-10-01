#!/usr/bin/python3
# SPDX-License-Identifier: GPL-3.0-or-later
# (c) TechyMinati ( Aryan Sinha ) <sinha.aryan03@gmail.com>
# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube for each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the output
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
