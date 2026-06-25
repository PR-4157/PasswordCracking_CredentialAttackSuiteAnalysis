import itertools

chars = "abc123"

count = 0

for password in itertools.product(chars, repeat=3):
    count += 1

print("Total combinations:", count)