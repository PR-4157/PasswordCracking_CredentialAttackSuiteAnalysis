from pyfiglet import figlet_format
from colorama import Fore, init
from tabulate import tabulate

init()

print(Fore.GREEN + figlet_format("Password"))

data = [
    ["Python", "Installed"],
    ["Colorama", "Installed"],
    ["Tabulate", "Installed"]
]

print(tabulate(data, headers=["Package", "Status"]))

