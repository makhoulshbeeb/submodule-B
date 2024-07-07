import os
import yaml 
with open(os.chdir("../Instructions.yaml"),'r') as file:
    data=yaml.load(file, Loader=yaml.SafeLoader)

print(data)