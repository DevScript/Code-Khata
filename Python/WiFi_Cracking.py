import subprocess
import re
import pyfiglet
print("WiFi networks scanning...")
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
print("\nAvailable Networks:\n")
users = re.findall("All User Profile     : (.*)\r", command_output)
count = 1
for profileName in users:
    print(str(count)+".", profileName)
    count += 1
wifiNo  = int(input("\nEnter wifi number for crack password:\t"))
try:
    command2_out = subprocess.run(["netsh", "wlan", "show", "profile", users[wifiNo-1], "key=clear"], capture_output=True).stdout.decode()
    password = re.search("Key Content            : (.*)\r", command2_out)
    print("*"*40)
    print("\n",users[wifiNo-1]," password is", password[1], "\n")
    print("*"*40, "\n")
    title = pyfiglet.figlet_format('Enjoy', font='stop')
    print(title)
except IndexError:
    print("Be limited, I`m not fool.")
