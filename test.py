import telnetlib
import paramiko
import getpass
import telnetlib
start_time = time.time()



# target = open("target") # IP Address file

hostname = "192.168.1.101"
username = input("Etner Username")
password = getpass.getpass()

command = "python importall.py"


# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()


# execute the commands
print("="*50, command, "="*50)
stdin, stdout, stderr = client.exec_command(command)
print(stdout.read().decode())
err = stderr.read().decode()
if err:
     print(err)