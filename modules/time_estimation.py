characters = 26
length = 6

total = characters ** length

guesses_per_second = 1000000

seconds = total / guesses_per_second

minutes = seconds / 60

print("Total combinations:", total)
print("Seconds:", round(seconds, 2))
print("Minutes:", round(minutes, 2))