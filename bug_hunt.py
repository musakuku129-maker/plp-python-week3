count = 1
total = 0

# BUG: The while loop was missing a colon after the condition, so Python would not recognize the loop body.
# BUG: The loop was stopping too early because it never included 5; I changed the condition to <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The print statement tried to concatenate a string and an integer; I converted total to a string before printing.
print("Sum of 1 to 5 is: " + str(total))
