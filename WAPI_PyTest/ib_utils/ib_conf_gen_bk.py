import os
import re
import sys
import string
import logging
from time import sleep
from logger import logger

"""
 Following 'splunk_conf' variable is used to dynamically generate splunkd config file. 
 NOTE: DONT MODIFY FOLLOWING VARIABLE.
"""


"""
Following 'config' variable is used to generate config.py dinamically.
NOTE: DONT MODIFY FOLLOWING VARIABLE.
"""

CONFIG_VAR="""
\"\"\"
Copyright (c) Infoblox Inc., 2016

Description: This is Auto Generated config file.

Author  : Manimaran .A
History : 12/11/2015
\"\"\"

#GRID INFORMATION
grid_vip="[GRID_MASTER_VIP]"
grid_fqdn="[GRID_MASTER_FQDN]"
username="admin"
password="infoblox"

#INDEXER_IP WILL BE 'GRID MASTER IP' IF GRID IS CONFIGURED WITH CLUSTERING 
indexer_ip="[INDEXER_IP]"
network_id="[NETWORK_ID]"
grid_master_vip="[GRID_MASTER_VIP]"
grid_member_fqdn="[GRID_MASTER_FQDN]"
grid_member1_vip="[GRID_MEMBER1_VIP]"
grid_member1_fqdn="[GRID_MEMBER1_FQDN]"
grid_member2_vip="[GRID_MEMBER2_VIP]"
grid_member2_fqdn="[GRID_MEMBER2_FQDN]"
grid_member3_vip="[GRID_MEMBER3_VIP]"
grid_member3_fqdn="[GRID_MEMBER3_FQDN]"
grid_member4_vip="[GRID_MEMBER4_VIP]"
grid_member4_fqdn="[GRID_MEMBER4_FQDN]"
grid_member5_vip="[GRID_MEMBER5_VIP]"
grid_member5_fqdn="[GRID_MEMBER5_FQDN]"

#CONFIG POOL INFORMATION
pool_dir="[POOL_DIR]"
pool_tag="[POOL_TAG]"
hw_info="[POOL_DIR]/hws.txt"



#WAPI VERSION
wapi_version = "[WAPI_VERSION]"
splunk_port="[SPLUNK_PORT]"
splunk_version="[SPLUNK_VERSION]"

#CLIENT INFORMION
client_vm="[CLIENT_HWID]"
client_ip="[CLIENT_IP]"
client_user="[CLIENT_USER]"
client_passwd="[CLIENT_PASSWD]"


#PY TEST ENVIRONMNET cONFIGURATION
log_path = "output.log"
search_py="../splunk-sdk-python/examples/search.py"
json_file="report.json"



"""

"""
Search and replace
"""
def  generate_conf(x,k):
    for stext in k.keys():
        x=string.replace(x,"["+stext+"]",k[stext])
    return x

def config(**k):
    conf=generate_conf(CONFIG_VAR,k)
    fout=open('config.py','w')
    fout.write(conf)
    logger.info(conf)
    fout.close
