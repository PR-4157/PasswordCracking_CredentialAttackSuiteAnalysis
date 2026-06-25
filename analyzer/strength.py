password = input("Enter password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(not c.isalnum() for c in password):
    score += 1

levels = {
    1: "Weak",
    2: "Fair",
    3: "Good",
    4: "Strong"
}

print("Score:", score)
print("Strength:", levels.get(score, "Very Weak"))