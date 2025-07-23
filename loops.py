# 1 for loop over list

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# 2 for loop with range

for i in range(1, 5):
    print(i * 2)

# range(1, 5) generates numbers from 1 to 4 (stop is exclusive)

# 3 while loop
count = 1
while count <= 3:
    print(f"Count: {count}")
    count += 1
"""
Count: 1
Count: 2
Count: 3
"""
# while loop is useful when the number of iterations depends on a condition
# break and continue

for num in range(1, 6):
    if num == 3:
        continue
    if num == 5:
        break
    print(num)

"""
continue skips the iteration when n == 3, so 3 isn't printed.
break stops the loop when num == 5, so 5 isn't printed.
controls loop flow for specific conditions
"""

# 5 loop with else

numbers = [1, 2, 3]
for num in numbers:
    print(num)
else:
    print("Loop completed")

print("==============================================================")

# 1: sum of numbers on a list

numbers = [1, 2, 3, 4, 5, 6, 7]
total = 0

for num in numbers:
    total += num # add each number to total
print(f"Sum: {total}")

print("==============================================================")

# 2 : print even numbers
for i in range(1, 11):
    if i % 2 == 0:
        print(f"Evens: {i}")

print("==============================================================")

# 3 countdown timer

count = 5

while count > 0:
    print(f"Countdown: {count}")
    count -= 1 # decrease count
print("Blast Off!")

print("==============================================================")

numbers =  [10, 20, -5, 30, -10]

for num in numbers:
    if num < 0:
        print(f"First Negative: {num}")  # First Negative: -5
        break

print("==============================================================")

# 5 generate random scores and average
import random
scores = []

while len(scores) < 5:
    scores.append(random.randint(50, 100)) # Add random score
average = sum(scores) / len(scores)
print(f"Scores: {scores}, Average: {average:.2f}")

print("==============================================================")

nums = [2,7,11,15]

target = 9

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] ==  target:
                return [i, j]
    return []
twoSum(nums = [2,7,11,15], target = 9)
print("==============================================================")