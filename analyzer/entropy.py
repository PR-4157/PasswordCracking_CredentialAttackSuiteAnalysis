import math

password = "R@hul#2026"

length = len(password)
charset = 94

entropy = length * math.log2(charset)

print("Password:", password)
print("Entropy:", round(entropy, 2), "bits")