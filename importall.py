import os
import re


os.system("$env:PATH=$env:PATH+';C:\\Program Files\\Oracle\\VirtualBox'")  

fileno = os.listdir("ova-files")  # number of Files

for i in range(len(fileno)):
    os.system(f"VBoxManage import ova-files/{fileno[i]} --vsys 0 --vmname {fileno[i]} --cpus 1 --memory 1024")

allvms = os.popen('vboxmanage list vms').read() # List down all the created VMs 
vmnamelist = re.findall(r'"(.*?)"', allvms)  # Stores all VMs name in a list


for s in range(len(vmnamelist)): 
    os.system(f"vboxmanage startvm {vmnamelist[s]}")