# User information
name = "rahul"
dob = "05041996"

# Basic passwords
passwords = [
    name,
    name + dob,
    name + "123",
    name.capitalize(),
    name + "@123"
]

# Mutation rules
mutations = [
    name.upper(),
    name.replace("a", "@"),
    name.replace("a", "4"),
    name + "2026"
]

# Combine lists
all_passwords = passwords + mutations

# Remove duplicates
all_passwords = list(set(all_passwords))

# Display passwords
print("\nGenerated Passwords:\n")

for p in all_passwords:
    print(p)

# Save to file
with open("wordlists/list.txt", "w") as file:
    for p in all_passwords:
        file.write(p + "\n")

print("\nWordlist saved to wordlists/list.txt")