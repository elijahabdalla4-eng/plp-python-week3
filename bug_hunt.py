count = 1
total = 0

# BUG: Missing colon at the end of the while loop statement. Fixed by adding ':'.
# BUG: The condition 'count < 5' excludes 5, producing a total of 10 instead of 15. Fixed by changing to 'count <= 5'.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: String and integer cannot be concatenated directly with '+'. Fixed by converting total to string using str().
print("Sum of 1 to 5 is: " + str(total))