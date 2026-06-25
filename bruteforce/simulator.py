import hashlib

password = "rahulkumar@123"

target = hashlib.md5(password.encode()).hexdigest()

attempts = 0

with open("wordlists/list.txt") as file:
    for word in file:
        word = word.strip()
        attempts += 1

        if hashlib.md5(word.encode()).hexdigest() == target:
            print("Password found:", word)
            print("Attempts:", attempts)
            break