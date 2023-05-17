import py
import json
import os
import re
import sys
import getopt
import ib_utils.ib_NIOS as ib_NIOS
from time import sleep
#import ib_data.ib_preparation as prep
import ib_utils.ib_papi as papi
import subprocess
import ib_utils.ib_conf_gen as conf_gen
from logger import logger
os.environ["PYTHONPATH"]=os.getcwd()
"""
   -m : Members separated by ':'  (GridMaster:Member1:Member2:Member3 etc., )
   -v : wapi_version
   -s : clinet_vm:client_ip:client_user:client_user_pw (CLIENT)
"""
args=sys.argv[1:]
optlist, args = getopt.getopt(args,'m:v:')
for opt, arg in optlist:
    if opt == '-m':
        members=arg
    if opt == '-v':
       wapi_version=arg
      #splunk_version,wapi_version=arg.split(':')
#    if opt == '-s':
#       client_vm,client_ip,client_user,client_passwd=arg.split(':')

"""
Configuring Master, Member & Reporting Member Variables. 
"""
var_hash={}
L=members.split(':')
master=L[0]
var_hash["GRID_MASTER_VIP"] =master
var_hash["GRID_MASTER_FQDN"]="ib-"+'-'.join(master.split('.'))+".infoblox.com"

for i,member in enumerate(L[1:]):
    var_hash["GRID_MEMBER"+str(i+1)+"_VIP"]=member
    var_hash["GRID_MEMBER"+str(i+1)+"_FQDN"]="ib-"+'-'.join(member.split('.'))+".infoblox.com"



var_hash["WAPI_VERSION"]=wapi_version



#Generating config.py Conf file
#logger.info("Generating config.py configuraiotn file")
rc=conf_gen.config(**var_hash)

#Addkyes
logger.info("Adding SSH Keys on Grid Members")
papi.addkeys(master)

#sleep(300)
    
#logger.info("Triggered execution for Minute Group Reports")  
#args_str = "-k test_validate --tb=long --html=license_report.html --junit-xml=license_results.xml -vv"
#py.test.cmdline.main(args_str.split(" "))

WORKSPACE = os.getenv('WORKSPACE')
BUILD_USER_ID = os.getenv('BUILD_USER_ID')
Build_Path = os.getenv('Build_Path')
Master1_IP = os.getenv('Master1_IP')
REPORT_URL = os.getenv('REPORT_URL')
BUILD_URL = os.getenv('BUILD_URL')
SERVER_IP = os.getenv('SERVER_IP')
PROJECT_NAME = os.getenv('PROJECT_NAME')


#Adding MS Server
os.system("getPAPI "+master+" .")
add_server_ms = "perl add_ms_server.pl "+master+" ib-"+'-'.join(master.split('.'))+".infoblox.com"
print add_server_ms
os.system(add_server_ms)
sleep(10)

print master
#HSM Thales Group Setup
#cmd = ('''ssh root@10.39.10.39  "cd /var/www/html;  php new1.php %s lnv 07/15/2018"''') %(master)
#os.system(cmd)
#cmd = 'ssh root@10.39.10.39  "cd /var/www/html;  php new4.php"'
#os.system(cmd)


#Starting Discovery services for ND member
os.system("pytest test_start_discovery_services.py -vss")
sleep(30)


#HSM Safenet Setup
#os.system('pytest test_generate_cert.py')
#sleep(10)
#cmd = 'expect register_safenet.exp '+master
#os.system(cmd)
#sleep (60)

#os.system('pytest test_add_safenet_group.py')
#sleep(30)

file = open("files.txt",'r')
lst =[]
i =0
for line in file:
        lst.append(line)
        lst[i]=line[:-1]
        i = i+1
print lst
count = 1
for item in lst:
	feature_name = item[5:-3]
	print feature_name
	os.system("rm WAPI_Test_Reports/HTML/"+feature_name+".html")
	os.system("rm WAPI_Test_Reports/XML/"+feature_name+".xml")
	print "=============== Executing Test Suite : %d ===============" %(count)
	cmd = "py.test WAPI82_Automation/"+item+" --tb=long --html=WAPI_Test_Reports/HTML/"+feature_name+".html --junit-xml=WAPI_Test_Reports/XML/"+feature_name+".xml -vv"
	print cmd 
	rm = os.system(cmd)
	count +=1

	replace = "sed -i 's/pytest/"+feature_name+"_results/g' WAPI_Test_Reports/XML/"+feature_name+".xml"
	rm = os.system(replace)
	WORKSPACE = os.getenv('WORKSPACE')
	cp_cmd = "cp  WAPI_Test_Reports/XML/"+feature_name+".xml "+WORKSPACE
        print cp_cmd
	rm = os.system(cp_cmd)
	command = '''curl -F "uploadedfile=@%s/%s.xml" -F user=%s -F build="%s" -F tag="WAPI FR" -F product="Core DDI" -F category="NIOS" -F gridip="%s" -F report_url="%s" -F build_url="%s" "http://%s/%s/uploader.php"''' %(WORKSPACE,feature_name,BUILD_USER_ID,Build_Path,Master1_IP,REPORT_URL,BUILD_URL,SERVER_IP,PROJECT_NAME)
	print command
	os.system(command) 
