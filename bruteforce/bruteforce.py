import itertools

chars = "abc123"

for password in itertools.product(chars, repeat=3):
    print("".join(password))