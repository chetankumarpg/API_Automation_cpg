
"""
Copyright (c) Infoblox Inc., 2016

Description: This is Auto Generated config file.

Author  : Manimaran.A
History : 05/27/2015
"""

#GRID INFORMATION
grid_vip="10.197.9.42"
grid_fqdn="ib-10-197-9-42.infoblox.com"
username="admin"
password="infoblox"
grid2_vip="[GRID2_VIP]"
grid2_fqdn="[GRID2_FQDN]"
CLIENT_IP="10.36.198.1"
#INDEXER_IP WILL BE 'GRID MASTER IP' IF GRID IS CONFIGURED WITH CLUSTERING 
indexer_ip="10.35.192.8"
network_id="[NETWORK_ID]"
grid_master_vip="10.197.9.42"
grid_member_fqdn="ib-10-197-9-42.infoblox.com"
grid_member1_vip="10.35.197.10"
grid_member1_fqdn="ib-10-35-197-10.infoblox.com"
grid_member2_vip="10.35.188.11"
grid_member2_fqdn="ib-10-35-188-11.infoblox.com"
grid_member3_vip="10.35.151.18"
grid_member3_fqdn="ib-10-35-151-18.infoblox.com"
grid_member4_vip="10.35.161.16"
grid_member4_fqdn="ib-10-35-161-16.infoblox.com"
grid_member5_vip="10.35.132.6"
grid_member5_fqdn="ib-10-35-132-6.infoblox.com"
grid_member6_vip="10.35.173.15"
grid_member6_fqdn="ib-10-35-173-15.infoblox.com"
reporting_member1_ip="10.35.192.8"
reporting_member1_fqdn="ib-10-35-192-8.infoblox.com"
reporting_member2_ip="[REPORTING_MEMBER2_VIP]"
reporting_member2_fqdn="[REPORTING_MEMBER2_FQDN]"
reporting_member3_ip="[REPORTING_MEMBER3_VIP]"
reporting_member3_fqdn="[REPORTING_MEMBER3_FQDN]"
reporting_member4_ip="[REPORTING_MEMBER4_VIP]"
reporting_member4_fqdn="[REPORTING_MEMBER4_FQDN]"

#CONFIG POOL INFORMATION
pool_dir="/tmp/Reporting_FR_part2"
pool_tag="GRID1"
hw_info="/tmp/Reporting_FR_part2/hws.txt"

#DNS Resolver
dns_resolver="10.103.3.10"  #which is configured for CISCO ISC

#DCVM Configuration
dcvm_ip="[DCVM_IP]"
dcvm_user="auto"
dcvm_password="auto123"

#CISCO ISC Configuraiton
cisco_ise_ip="10.36.141.15"
cisco_ise_user="qa"
cisco_ise_password="Infoblox1492"
cisco_ise_secret="secret"

#WAPI VERSION
wapi_version = "2.11.2"
splunk_port="8089"
splunk_version="7.2.6"

#CLIENT INFORMION
client_vm="vm-07-77"
client_ip="10.36.198.7"
#client_vm="vm-01-77"
#client_ip="10.36.198.1"
client_user="root"
client_passwd="infoblox"
olympic_ruleset="/import/release_archive/olympic-rule/OFFICIAL//OLYMPIC_r_414072_p_397017_NIOS_8.5.0_397898_2021-04-29-00-08-27_x86_64/ruleset-20210429-olympic-r-414072-p-397017-n-397898-2021-04-29-00-08-27.bin2"

#BELOW IP'S ARE USED FOR DNS_TOP_CLIENTs
#client_eth1_ip1="10.35.132.6"
client_eth1_ip1="10.35.132.6"
client_eth1_ip2="10.35.195.11"
#client_eth1_ip2="10.34.220.251"
client_eth1_ip3="10.34.220.252"
client_eth1_ip4="10.34.220.253"
client_eth1_ip5="10.34.220.254"
client_netmask="255.255.252.0"

#BELOW IP'S ARE USED FOR DNS_TOP_REQUESTED DOMAIN
client_eth1_ip6="10.34.220.240"
client_eth1_ip7="10.34.220.241"
client_eth1_ip8="10.34.220.242"

#BELOW IP'S ARE USED FOR DNS Query Trend per IP Block Group
client_eth1_ip9 ="10.36.198.8"
client_eth1_ip10="10.36.198.7"
client_eth1_ip11="10.120.22.146"
client_eth1_ip12="10.120.21.51"
client_eth1_ip13="10.120.20.92"


#REPORTING BACKUP & RESTORE DEFAULT PATH
backup_path="/tmp/reporting_bakup"

#PY TEST ENVIRONMNET cONFIGURATION
log_path = "output.log"
search_py="/import/qaddi/API_Automation/splunk-sdk-python/examples/search.py"
json_file="report.json"
dns_resolver="10.0.2.35"  #which is configured for CISCO ISC
dns_forwarder="10.36.6.80"



#GLOBAL VARIABLE
scal_test1=""
scal_test2=""
scal_test3=""
scal_test4=""
scal_test5=""
list_test1=[]
list_test2=[]
list_test3=[]
list_test4=[]
list_test5=[]
dict_test1={}
dict_test2={}
dict_test3={}
dict_test4={}
dict_test5={}


dns_forwarder="10.39.16.160"
cisco_ise_server_ip="vm-25.neo.com"
dns_resolver="10.34.98.39"
host_name="infoblox.neo.com"
MS_user="test1"

