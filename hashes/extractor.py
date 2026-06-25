hash_value = input("Enter hash: ")

if hash_value.startswith("$1$"):
    print("MD5")

elif hash_value.startswith("$5$"):
    print("SHA256")

elif hash_value.startswith("$6$"):
    print("SHA512")

elif len(hash_value) == 32:
    print("Possible NTLM or MD5 hash")

else:
    print("Unknown hash type")

with open("hashes/sample_ntlm.txt", "r") as file:
    for line in file:
        username, hash_value = line.strip().split(":")

        print("User:", username)
        print("Hash:", hash_value)

        if len(hash_value) == 32:
            print("Type: Possible NTLM")
            print()