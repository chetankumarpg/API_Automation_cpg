import xml.etree.ElementTree as ET
import subprocess
import yaml


tree = ET.parse("Configuration.xml")
root = tree.getroot()
setup_info = {}
members = []
for child in root:

    master_length=len(root[0])

    f = open('config.py','w')
    f.write("\"\"\"\nCopyright (c) Infoblox Inc., 2022\n\nDescription: This is Auto Generated config file.\n\nAuthor  : Vindya V K\n\"\"\"\n\n")
    f.write("\n#LISTING ALL THE REQUIRED VARIABLES BELOW")
    for i in range(master_length):
        f.write("\n"+(child[i].tag).lower() +"=\""+child[i].text+"\"")
#    f.write("\n")
    f.close()


path=subprocess.check_output('pwd',shell=True)
print("Current Path =" + path)

#### Fetching workspace path ####
workspace_path=""
workspace=path.split("/")
workspace.pop(0)
print(workspace)

for w in range(0,4):
    workspace_path=workspace_path+"/"+workspace[w]

print(workspace_path)

#### Writing external global server details into config.py

# converting data in yaml file to dictionary
with open(workspace_path+'/API_Automation/WAPI_PyTest/ib_utils/OPTIMISATION_SCRIPTS/global_config.yaml') as file:
    variables = yaml.load(file, Loader=yaml.FullLoader)
    #print(variables)

# pushing data from dictionary to config.py
f = open('config.py','a')
f.write("\n\n#ADDING VALUES OF EXTERNAL SERVERS BELOW\n")
f.close()

for key,value in variables.items():
    data_to_push=str(key)+"=\""+str(value)+"\""
    print(data_to_push)

    f = open('config.py','a')
    f.write(data_to_push+"\n")
    f.close()

    
#### Writing custom variable details into config.py

# converting data in custom_config.yaml file to dictionary
with open(r'custom_config.yaml') as file:
    variables = yaml.load(file, Loader=yaml.FullLoader)
    #print(variables)

# pushing data from dictionary to config.py
f = open('config.py','a')
f.write("\n\n#ADDING VALUES OF CUSTOM VARIABLES BELOW\n")
f.close()

for key,value in variables.items():
    data_to_push=str(key)+"=\""+str(value)+"\""
    print(data_to_push)

    f = open('config.py','a')
    f.write(data_to_push+"\n")
    f.close()
