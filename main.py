def dictionary():
    print("Dictionary Generator")

def analyzer():
    print("Password Analyzer")

def simulation():
    print("Simulation Module")

def report():
    print("Report Generator")

print("\nPassword Cracking Toolkit\n")

print("1. Generate Dictionary")
print("2. Analyze Password")
print("3. Run Simulation")
print("4. Generate Report")

choice = input("\nEnter choice: ")

if choice == "1":
    dictionary()

elif choice == "2":
    analyzer()

elif choice == "3":
    simulation()

elif choice == "4":
    report()

else:
    print("Invalid option")
