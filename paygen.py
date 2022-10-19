#!/bin/python3.10
import os
import time

print("This payload generator turns commands into")
print("\nMalicious payloads.")
print("\nDo not use if on anyone unless you have permission.")

payload = input("\nEnter command: ")

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
if cont == "y":
    os.system("pyinstaller --onefile payload.py")
elif cont == "n":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Closing in 3... 2... 1...")
time.sleep(3)

exit()
