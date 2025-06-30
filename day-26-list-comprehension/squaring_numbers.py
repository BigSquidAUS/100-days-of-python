numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# A list of integers — these happen to be part of the Fibonacci sequence.

squared_numbers = [n * n for n in numbers]
# A list comprehension that loops through each number `n` in `numbers`
# and appends `n * n` (n squared) to the new list `squared_numbers`.

print(squared_numbers)
# Outputs the new list of squared values.
# Expected output: [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
