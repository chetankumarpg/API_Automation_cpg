#!/usr/bin/env python
__author__ = "Chetan Kumar PG"
__email__  = "cpg@infoblox.com"

#############################################################################
#  Grid Set up required:                                                    #
#  1. GM + 3 Members                                                        #
#  2. Licenses : DNS, DHCP, Grid, NIOS                                      #
#  3. Enable DNS/DHCP services                                              #
#############################################################################

import os
import re
import sys
import time
import config
import pytest
import unittest
import logging
import json
import shlex
import pexpect
import paramiko
from time import sleep
from scp import SCPClient
from subprocess import Popen, PIPE
import ib_utils.ib_NIOS as ib_NIOS
from ib_utils.log_capture import log_action as log
from ib_utils.log_validation import log_validation as logv
from ipaddress import ip_address, IPv4Address, IPv6Address
logging.basicConfig(format='%(asctime)s - %(name)s(%(process)d) - %(levelname)s - %(message)s',filename="rfe_4753.log" ,level=logging.DEBUG,filemode='w')

global scheduled_time

def display_msg(x="",is_dict=False):
    """ 
    This function prints and logs data 'x'.
    is_dict : If this parameter is True, then print the data in easy to read format.
    """
    logging.info(x)
    if is_dict:
        print(json.dumps(x,sort_keys=False, indent=4))
    else:
        print(x)

def is_grid_alive(grid=config.grid1_master_vip):
    """
    Checks whether the grid is reachable
    """
    ping = os.popen("ping -c 2 "+grid).read()
    display_msg(ping)
    if "0 received" in ping:
        return False
    else:
        return True

def remove_known_hosts_file():
    """
    Removes known_hosts file.
    This is to avoid host key expiration issues.
    """
    cmd = "rm -rf /home/"+config.client_username+"/.ssh/known_hosts"
    ret_code = os.system(cmd)
    if ret_code == 0:
        display_msg("Cleared known hosts file")
    else:
        display_msg("Couldnt clear known hosts file")

def restart_services(grid=config.grid1_master_vip, service=['ALL']):
    """
    Restart Services
    """
    display_msg()
    display_msg("+----------------------------------------------+")
    display_msg("|           Restart Services                   |")
    display_msg("+----------------------------------------------+")
    get_ref =  ib_NIOS.wapi_request('GET', object_type="grid",grid_vip=grid)
    ref = json.loads(get_ref)[0]['_ref']
    data= {"mode" : "SIMULTANEOUS","restart_option":"FORCE_RESTART","services": service}
    restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", fields=json.dumps(data),grid_vip=grid)
    if restart != '{}':
        display_msg(restart)
        display_msg("FAIL: Restart services failed, Please debug above error message for root cause")
        assert False
    sleep(20)

    
def generate_token_from_file(filepath, filename,grid=config.grid1_master_vip):
    dir_name=filepath
    base_filename=filename
    filename= os.path.join(dir_name, base_filename)
    data = {"filename":base_filename}
    create_file = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=uploadinit",grid_vip=grid)
    logging.info(create_file)
    res = json.loads(create_file)
    token = json.loads(create_file)['token']
    url = json.loads(create_file)['url']
    print create_file
    print res
    print token
    print url
    os.system('curl -k1 -u admin:infoblox -F name=%s -F filedata=@%s %s'%(filename,filename,url))
    filename="/"+filename
    return token

def get_current_epoch_time(grid=config.grid1_master_vip):
    """
    Returns current time from the Grid IP provided
    """
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(grid, username='root', password = 'infoblox')
        stdin, stdout, stderr = client.exec_command("date +%s")
        error = stderr.read()
        if not error:
            output = stdout.read()
            return output
        else:
            display_msg("FAIL: Failed to get current epoch time")
            display_msg(error)
            assert False
    except Exception as E:
        display_msg(E)
        display_msg("FAIL: Debug above exception")
        assert False
    finally:
        client.close()

def gmc_promotion_forced_end(grid=config.grid1_master_vip):
    """
    Forcefully ends GMC Promotion and releases GMC Group Promotion Schedule wizard.
    """
    display_msg("Executing 'set gmc_promotion forced_end'")
    args = "sshpass -p 'infoblox' ssh -o StrictHostKeyChecking=no admin@"+grid
    args=shlex.split(args)
    try:
        child = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        child.stdin.write("set gmc_promotion forced_end\n")
        child.stdin.write("exit")
    except Exception as E:
        display_msg(E)
        display_msg("FAIL: Debug above exception")
        assert False
    finally:
        result = child.communicate()
    for line in result:
        display_msg(line)
        if 'Forcefully resetting the gmc_promotion flag to false' in line:
            return 1
        elif 'GMC Promotion is not in progress in this grid' in line:
            display_msg("WARNING: GMC Promotion is not in progress")
            return 2
        elif 'This command can be executed only on Master node':
            display_msg("WARNING: Executing this CLI on members is restricted")
            return 3
    display_msg("WARNING: Expected output not found. Please debug the above message.")
    return 0

def gmc_promotion_disable(grid=config.grid1_master_vip):
    """
    Disable Activate GMC Group Promotion Schedule.
    """
    display_msg("Executing 'set gmc_promotion disable'")
    args = "sshpass -p 'infoblox' ssh -o StrictHostKeyChecking=no admin@"+grid
    args=shlex.split(args)
    try:
        child = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        child.stdin.write("set gmc_promotion disable\n")
        child.stdin.write("exit")
    except Exception as E:
        display_msg(E)
        display_msg("FAIL: Debug above exception")
        assert False
    finally:
        result = child.communicate()
    flag = False
    for line in result:
        display_msg(line)
        if 'Feature is disabled' in line:
            display_msg("WARNING: Feature is already disabled")
        elif 'This command can only be executed on gmcs' in line:
            display_msg("FAIL: Please execute the above CLI on GMCs only")
            flag = True
    if flag:
        display_msg("WARNING: Expected output not found. Please debug the above message.")
        return False
    return True

def is_master(vip=config.grid1_master_vip):
    """
    Checks if this is a master.
    """
    status = is_grid_alive(vip)
    if status:
        args = "sshpass -p 'infoblox' ssh -o StrictHostKeyChecking=no admin@"+vip
        args=shlex.split(args)
        try:
            child = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            child.stdin.write("show network\n")
            child.stdin.write("exit")
        except Exception as E:
            display_msg(E)
            display_msg("FAIL: Debug above exception")
            assert False
        finally:
            result = child.communicate()
        flag = False
        for line in result:
            display_msg(line)
            if 'Master of Infoblox Grid' in line:
                flag = True
        if not flag:
            display_msg("WARNING: Expected output not found. Please debug the above message.")
            return False
        return True
    else:
        display_msg("WARNING: Device is not up and running. Please check.")
        return False

def create_gmc_promotion_group(name,scheduled_time,members=[],gmc_promotion_policy='SIMULTANEOUSLY',grid_master=config.grid1_master_vip):
    """
    Creates GMC Promotion Group with below data
    name (string)
    scheduled_time (epoch timestamp)
    members (list of members in fqdn format)
    gmc_promotion_policy (SIMULTANEOUSLY, SEQUENTIALLY)
    """
    member_data = []
    for member in members:
        member_data.append({'member': member})
    display_msg("Create a GMC Promotion Group '"+name+"'")
    data = {"name":name,
            "gmc_promotion_policy":gmc_promotion_policy,
            "members":member_data,
            "scheduled_time":scheduled_time
            }
    response = ib_NIOS.wapi_request('POST',object_type='gmcgroup',fields=json.dumps(data),grid_vip=grid_master)
    display_msg(response)
    if type(response) == tuple or 'gmcgroup' not in response:
        if 'Duplicate object' in response[-1]:
            display_msg("INFO: Updating the existing GMC Group")
            get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup?_return_fields=name",grid_vip=grid_master)
            for ref in json.loads(get_ref):
                if ref["name"] == name:
                    data = {"scheduled_time":scheduled_time}
                    if members:
                        data["members"] = member_data
                    response = ib_NIOS.wapi_request('PUT',ref=ref['_ref'],fields=json.dumps(data),grid_vip=grid_master)
                    display_msg(response)
                    if type(response) == tuple or 'gmcgroup' not in response:
                        display_msg("FAIL: GMC Promotion Group '"+name+"' not updated")
                        assert False
                    else:
                        display_msg("PASS: GMC Promotion Group '"+name+"' updated")
        else:
            display_msg("FAIL: GMC Promotion Group '"+name+"' not created")
            assert False
    else:
        display_msg("PASS: GMC Promotion Group '"+name+"' created")

def get_grid_info(grid=config.grid1_master_vip):
    """
    Returns lists of online and offline members (IP address)
    """
    output = os.Popen('grid_info '+grid).read()
    display_msg(output)
    output=output.split('\n')
    online = []
    offline = []
    for line in output:
        if 'OFFLINE' in line:
            offline.append(line.strip(' ').split(' ')[1])
        elif 'ONLINE' in line:
            online.append(line.strip(' ').split(' ')[1])
        else:
            continue
    return online,offline

def get_online_offline_members(grid=config.grid1_master_vip):
    """
    Returns lists of online and offline members (hostname)
    """
    online = []
    offline = []
    sleep(60)
    try:
        response = ib_NIOS.wapi_request('GET',object_type='member?_return_fields=host_name,node_info',grid_vip=grid)
    except Exception as E:
        if 'Connection reset by peer' in str(E):
            display_msg("INFO: Grid is not completely up. Sleeping for 60 seconds.")
            sleep(60)
            response = ib_NIOS.wapi_request('GET',object_type='member?_return_fields=host_name,node_info',grid_vip=grid)
        else:
            display_msg(E)
            assert False
    if type(response) == tuple:
        display_msg(response)
        display_msg("FAIL: Failed to get member data")
        assert False
    response = json.loads(response)
    service_status={}
    for member in response:
        if member["node_info"]:
            for service in member["node_info"][0]["service_status"]:
                if service["service"] == "NODE_STATUS":
                    service_status = service
                    break
            if service_status:
                if service_status["description"] == "Running":
                    online.append(member["host_name"])
                    flag = True
                    continue
            
        offline.append(member["host_name"])
    return online,offline

class RFE_4753(unittest.TestCase):

    @pytest.mark.run(order=1)
    def test_001_Activate_GMC_Group_Promotion_Schedule(self):
        """
        Enable Activate GMC Group Promotion Schedule.
        """
        display_msg()
        display_msg("+--------------------------------------------------+")
        display_msg("|          Test Case 1 Execution Started           |")
        display_msg("+--------------------------------------------------+")
        
        display_msg("Activate GMC Group Promotion Schedule")
        get_ref = ib_NIOS.wapi_request('GET', object_type='gmcschedule?_return_fields=activate_gmc_group_schedule')
        display_msg(get_ref)
        response = ib_NIOS.wapi_request('PUT', ref=json.loads(get_ref)[0]['_ref'], fields=json.dumps({"activate_gmc_group_schedule":True}))
        if type(response) == tuple:
            display_msg(response)
            display_msg("FAIL: Activate GMC Group Promotion Schedule")
            assert False
        display_msg("PASS: Enabled Activate GMC Group Promotion Schedule")

        display_msg("---------Test Case 1 Execution Completed----------")

    @pytest.mark.run(order=2)
    def test_002_Validate_Activate_GMC_Group_Promotion_Schedule(self):
        """
        Validate if Activate GMC Group Promotion Schedule is enabled.
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        get_ref = ib_NIOS.wapi_request('GET', object_type='gmcschedule?_return_fields=activate_gmc_group_schedule')
        display_msg(get_ref)
        if 'true' in get_ref:
            display_msg("PASS: Activate GMC Group Promotion Schedule validation")
        else:
            display_msg("FAIL: Activate GMC Group Promotion Schedule validation")
            assert False
        
        display_msg("---------Test Case 2 Execution Completed----------")
    
    @pytest.mark.run(order=3)
    def test_003_add_auth_zone(self):
        """
        Add an authoritative zone.
        """
        display_msg()
        display_msg("+--------------------------------------------------+")
        display_msg("|          Test Case 3 Execution Started           |")
        display_msg("+--------------------------------------------------+")
        
        display_msg("Add an authoritative zone test.com")
        data = {"fqdn": "test.com",
                "view":"default",
                "grid_primary": [{"name": config.grid1_master_fqdn,"stealth": False},{"name":config.grid1_member1_fqdn}]
                }
        response = ib_NIOS.wapi_request('POST',object_type="zone_auth",fields=json.dumps(data))
        display_msg(response)
        if type(response) == tuple:
            display_msg("FAIL: Create Authorative FMZ")
            assert False
        restart_services()
        display_msg("PASS: Authoritative zone test.com is added")
        
        display_msg("---------Test Case 3 Execution Completed----------")

    @pytest.mark.run(order=4)
    def test_004_validate_add_auth_zone(self):
        """
        Validate Added authoritative zone.
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        get_ref = ib_NIOS.wapi_request('GET',object_type="zone_auth?fqdn=test.com")
        display_msg(get_ref)
        if 'test.com' in get_ref:
            display_msg("PASS: Zone test.com found")
        else:
            display_msg("FAIL: Zone test.com not found")
            assert False
        
        display_msg("---------Test Case 4 Execution Completed----------")

    @pytest.mark.run(order=5)
    def test_005_add_a_record(self):
        """
        Add a record in the test.com zone.
        """
        display_msg()
        display_msg("+--------------------------------------------------+")
        display_msg("|          Test Case 5 Execution Started           |")
        display_msg("+--------------------------------------------------+")
        
        display_msg("Add a record a.test.com")
        data = {"name":"a.test.com",
                "ipv4addr":"10.1.1.1"
                }
        response = ib_NIOS.wapi_request('POST',object_type='record:a',fields=json.dumps(data))
        display_msg(response)
        if type(response) == tuple:
            display_msg("Failure: Add a record a.test.com")
            assert False
        display_msg("PASS: a record a.test.com added")
        
        display_msg("---------Test Case 5 Execution Completed----------")

    @pytest.mark.run(order=6)
    def test_006_validate_add_a_record(self):
        """
        Validated Added record in the test.com zone.
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        get_ref = ib_NIOS.wapi_request('GET',object_type="record:a?name=a.test.com")
        display_msg(get_ref)
        if 'a.test.com' in get_ref:
            display_msg("PASS: A record a.test.com found")
        else:
            display_msg("FAIL: A record a.test.com not found")
            assert False
        
        display_msg("---------Test Case 6 Execution Completed----------")

    @pytest.mark.run(order=7)
    def test_007_set_member1_as_master_candidate(self):
        """
        Set grid1_member1 as master candidate
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 7 Execution Started           |")
        display_msg("----------------------------------------------------")
        display_msg("Set grid1_member1 as master candidate")
        get_ref = ib_NIOS.wapi_request('GET', object_type='member')
        display_msg(get_ref)
        for ref in json.loads(get_ref):
            if config.grid1_member1_fqdn in ref['_ref']:
                response = ib_NIOS.wapi_request('PUT', ref=ref['_ref'], fields=json.dumps({"master_candidate":True}))
                if type(response) == tuple:
                    display_msg("FAIL: Setting member "+ref['_ref'].split(':')[-1]+" master candidate")
                    assert False
        restart_services()
        display_msg("PASS: Successfully set member "+ref['_ref'].split(':')[-1]+" as master candidate")
        
        display_msg("Sleep for 5 min for database switchover")
        sleep(300)
        
        display_msg("---------Test Case 7 Execution Completed----------")
        
    @pytest.mark.run(order=8)
    def test_008_validate_member1_as_master_candidate(self):
        """
        Validate grid1_member1 as master candidate
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        
        get_ref1 = ib_NIOS.wapi_request('GET', object_type='member?_return_fields=master_candidate')
        display_msg(get_ref1)
        for ref1 in json.loads(get_ref1):
            if config.grid1_member1_fqdn in ref1['_ref']:
                if ref1['master_candidate'] == True:
                    display_msg("PASS: Master candidate enabled on member "+ref1['_ref'].split(':')[-1])
                else:
                    display_msg("FAIL: Failed to enable master candidate on member "+ref1['_ref'].split(':')[-1])
                    assert False
        
        display_msg("---------Test Case 8 Execution Completed----------")

    @pytest.mark.run(order=9)
    def test_009_update_time_zones(self):
        """
        Keep all the members in different time zones.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 9 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Keeping Grid master in UTC+5:30 timezone")
        time_zones = ["(UTC + 5:30) Bombay, Calcutta, Madras, New Delhi",
                      "(UTC - 8:00) Pacific Time (US and Canada), Tijuana",
                      "(UTC + 1:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna",
                      "(UTC) Coordinated Universal Time"]
        member_ref = ib_NIOS.wapi_request('GET',object_type="member?_return_fields=time_zone")
        display_msg(member_ref)
        for ref in json.loads(member_ref):
            time_zone = time_zones[json.loads(member_ref).index(ref)]
            data = {"time_zone":time_zone}
            response = ib_NIOS.wapi_request('PUT',ref=ref['_ref'],fields=json.dumps(data))
            display_msg(response)
            member = ref['_ref'].split(':')[-1]
            if type(response) == tuple:
                display_msg("Failure: Update time zone of "+member+" to "+time_zone)
                assert False
            display_msg("PASS: Updated time zone of "+member+" to "+time_zone)
            
        display_msg("---------Test Case 9 Execution Completed----------")

    @pytest.mark.run(order=10)
    def test_010_validate_updated_time_zones(self):
        """
        Validate all the members are in different time zones.
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        time_zones = ["(UTC + 5:30) Bombay, Calcutta, Madras, New Delhi",
                      "(UTC - 8:00) Pacific Time (US and Canada), Tijuana",
                      "(UTC + 1:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna",
                      "(UTC) Coordinated Universal Time"]
        member_ref = ib_NIOS.wapi_request('GET',object_type="member?_return_fields=time_zone")
        display_msg(member_ref)
        for ref in json.loads(member_ref):
            time_zone = time_zones[json.loads(member_ref).index(ref)]
            member = ref['_ref'].split(':')[-1]
            if not time_zone in member_ref:
                display_msg("FAIL: Time zone "+time_zone+" for member "+member+" not updated")
                assert False
            display_msg("PASS: Time zone "+time_zone+" for member "+member+" updated")

        display_msg("---------Test Case 10 Execution Completed---------")
    
    @pytest.mark.run(order=11)
    def test_011_Create_a_GMC_Promotion_Group(self):
        """
        Create a GMC Promotion Group with all the members part of the group.
        Schedule the group for 10 minutes in future.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 11 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        global scheduled_time
        display_msg("Force end the GMC Promotion if it is in progress")
        gmc_promotion_forced_end()
        display_msg("Create a GMC Promotion Group 'group 1'")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup")
        display_msg(get_ref)
        current_epoch_time = int(get_current_epoch_time())
        scheduled_time = current_epoch_time + (10*60)
        display_msg("Current epoch time: "+str(current_epoch_time))
        display_msg("Scheduled time : "+str(scheduled_time))
        create_gmc_promotion_group('group 1',scheduled_time,members=[config.grid1_member2_fqdn,config.grid1_member3_fqdn])
        
        display_msg("---------Test Case 11 Execution Completed----------")

    @pytest.mark.run(order=12)
    def test_012_Validate_created_GMC_Promotion_Group(self):
        """
        Validate created GMC Promotion Group.
        """        
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup")
        display_msg(get_ref)
        if 'group 1' not in get_ref:
            display_msg("FAIL: GMC Promotion Group 'group 1' not found")
            assert False
        display_msg("PASS: GMC Promotion Group 'group 1' found")

        display_msg("---------Test Case 12 Execution Completed----------")

    @pytest.mark.run(order=13)
    def test_013_Perform_Master_Promotion_1(self):
        """
        Perform Master Promotion on GMC.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 13 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Perform GMC Promotion")
        args = "sshpass -p 'infoblox' ssh -o StrictHostKeyChecking=no admin@"+config.grid1_member1_vip
        args = shlex.split(args)
        try:
            child = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            child.stdin.write("set promote_master\n")
            child.stdin.write("y\n")
            child.stdin.write("y\n")
        except Exception as E:
            display_msg(E)
            display_msg("FAIL: Debug the above exception")
            assert False
        finally:
            output = child.communicate()
        flag = False
        for line in output:
            display_msg(line)
            if 'Master promotion beginning on this member' in line:
                flag = True
        if flag:
            display_msg("PASS: GMC promotion successfully started")
        else:
            display_msg("FAIL: Failed to start GMC promotion")
            assert False
        
        count = 0
        display_msg("Sleeping till Grid comes up")
        sleep(60)
        while not is_grid_alive(config.grid1_member1_vip):
            if count == 4:
                display_msg("Giving up after 5 tries")
                assert False
            display_msg("Sleeping for 1 more minute...")
            sleep(120)
            count += 1

        display_msg("---------Test Case 13 Execution Completed----------")
    
    @pytest.mark.run(order=14)
    def test_014_Validate_GMC_Promotion_1(self):
        """
        Validate GMC Promotion is complete on Master.
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        
        display_msg("Checking if Old GMC has become new Master")
        status = is_master(config.grid1_member1_vip)
        if status:
            display_msg("PASS: "+config.grid1_member1_vip+" is the new master")
        else:
            display_msg("FAIL: "+config.grid1_member1_vip+" is not a master")
            assert False

        display_msg("---------Test Case 14 Execution Completed----------")

    @pytest.mark.run(order=15)
    def test_015_Validate_Default_group_members_are_joined_1(self):
        """
        Validate if the Deafult group's members are joined to new Master
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 15 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Getting the Grid status")
        count = 0
        while count < 6:
            status = is_grid_alive(config.grid_vip)
            if status:
                break
            display_msg("GMC Member "+config.grid_vip+" is not up. Sleeping for 10s ...")
            sleep(10)
            count += 1
        online,offline = get_online_offline_members(config.grid1_member1_vip)
        display_msg("Online members: ")
        display_msg(online)
        display_msg("Offline members: ")
        display_msg(offline)
        
        display_msg("Getting the GMC Group Members")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup?_return_fields=name,members",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        
        groups = json.loads(get_ref)
        flag = False
        for group in groups:
            if group["name"] == "Default":
                for member in group["members"]:
                    if member["member"] in offline:
                        display_msg("FAIL: Grid Member '"+member["member"]+"' from the group '"+group["name"]+"' has not joined the new Master")
                        flag = True
        if flag:
            assert False
        display_msg("All the members from 'Default' group are joined to the new Master")

    @pytest.mark.run(order=16)
    def test_016_Validate_syslog_for_master_promotion_notice_1(self):
        """
        Validate syslog for below message when scheduled time is met.
        Sent master promotion notice to grid member ib-10-35-129-9.infoblox.com (10.35.129.9).
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 16 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Start capturing syslog ...")
        log("start","/var/log/messages",config.grid1_member1_vip)
        
        global scheduled_time
        current_epoch_time = get_current_epoch_time(config.grid1_member1_vip)
        sleep_time = int(scheduled_time) - int(current_epoch_time)
        display_msg("Remaining scheduled time : "+str(sleep_time))
        if sleep_time > 0:
            display_msg("Sleeping "+str(sleep_time)+" seconds for the new master to send master promotion notice")
            sleep(sleep_time+120)
            
            display_msg("Stop capturing syslog ...")
            log("stop","/var/log/messages",config.grid1_member1_vip)
            
            display_msg("Validate if the master promotion notice is sent to the group 1 members")
            try:
                logv("'Sent master promotion notice to grid member "+config.grid1_member2_fqdn+"'",'/var/log/messages',config.grid1_member1_vip)
                logv("'Sent master promotion notice to grid member "+config.grid1_member3_fqdn+"'",'/var/log/messages',config.grid1_member1_vip)
                logv("'Acknowledgement is received from the pnode "+config.grid1_member2_vip+"'",'/var/log/messages',config.grid1_member1_vip)
                logv("'Acknowledgement is received from the pnode "+config.grid1_member3_vip+"'",'/var/log/messages',config.grid1_member1_vip)
                logv("'All members of grid notified of master promotion'",'/var/log/messages',config.grid1_member1_vip)
                display_msg("PASS: Master Promotion notice is sent to the group 1 members")
                display_msg("PASS: Acknowledgement is received from the group 1 members")
            except Exception as E:
                if 'returned non-zero exit status 1' in str(E):
                    display_msg("FAIL: Above string is not found in the logs")
                    assert False
                display_msg(E)
                assert False
        else:
            display_msg("Stop capturing syslog ...")
            log("stop","/var/log/messages",config.grid1_member1_vip)
            
            display_msg("WARNING: Scheduled time has already passed")
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(config.grid1_member1_vip, username='root', password = 'infoblox')
                stdin, stdout, stderr = client.exec_command("cat /var/log/messages | grep 'Sent master promotion notice to grid member'")
                error = stderr.read()
                output = stdout.read()
            except Exception as E:
                display_msg(E)
                display_msg("FAIL: Debug the above exception")
                assert False
            finally:
                client.close()
            if error:
                display_msg("Error: "+error)
            display_msg("Output: "+output)
            assert False
        
        display_msg("---------Test Case 16 Execution Completed----------")
    
    @pytest.mark.run(order=17)
    def test_017_Create_2_GMC_Promotion_Groups(self):
        """
        Create two more GMC Promotion Groups.
        Add one member to 'group 2' and no members to 'group 3'.
        Schedule the group for 10 and 15 minutes in future respectively.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 17 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        global current_epoch_time
        global scheduled_time
        display_msg("Force end the GMC Promotion if it is in progress")
        gmc_promotion_forced_end(config.grid1_member1_vip)
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        current_epoch_time = int(get_current_epoch_time(config.grid1_member1_vip))
        
        #group 1
        scheduled_time = current_epoch_time + (15*60)
        display_msg("Current epoch time: "+str(current_epoch_time))
        display_msg("Scheduled time : "+str(scheduled_time))
        create_gmc_promotion_group('group 1',scheduled_time,members=[config.grid1_member2_fqdn],grid_master=config.grid1_member1_vip)
        
        # group 2
        scheduled_time = current_epoch_time + (10*60)
        display_msg("Current epoch time: "+str(current_epoch_time))
        display_msg("Scheduled time : "+str(scheduled_time))
        create_gmc_promotion_group('group 2',scheduled_time,members=[config.grid1_member3_fqdn],grid_master=config.grid1_member1_vip)
        
        # group 3
        scheduled_time = current_epoch_time + (15*60)
        display_msg("Current epoch time: "+str(current_epoch_time))
        display_msg("Scheduled time : "+str(scheduled_time))
        create_gmc_promotion_group('group 3',scheduled_time,grid_master=config.grid1_member1_vip)
        
        display_msg("---------Test Case 17 Execution Completed----------")

    @pytest.mark.run(order=18)
    def test_018_Validate_created_GMC_Promotion_Groups(self):
        """
        Validate created GMC Promotion Groups group 2 and group 3.
        """        
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup?_return_fields=name,members",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        if 'group 2' not in get_ref:
            display_msg("FAIL: GMC Promotion Group 'group 2' not found")
            assert False
        display_msg("PASS: GMC Promotion Group 'group 2' found")
        
        if 'group 3' not in get_ref:
            display_msg("FAIL: GMC Promotion Group 'group 3' not found")
            assert False
        display_msg("PASS: GMC Promotion Group 'group 3' found")

        display_msg("---------Test Case 18 Execution Completed----------")
    
    @pytest.mark.run(order=19)
    def test_019_Perform_Master_Promotion_2(self):
        """
        Perform Master Promotion on GMC.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 19 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Perform GMC Promotion")
        args = "sshpass -p 'infoblox' ssh -o StrictHostKeyChecking=no admin@"+config.grid1_master_vip
        args = shlex.split(args)
        try:
            child = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            child.stdin.write("set promote_master\n")
            child.stdin.write("y\n")
            child.stdin.write("y\n")
        except Exception as E:
            display_msg(E)
            display_msg("FAIL: Debug the above exception")
            assert False
        finally:
            output = child.communicate()
        flag = False
        for line in output:
            display_msg(line)
            if 'Master promotion beginning on this member' in line:
                flag = True
        if flag:
            display_msg("PASS: GMC promotion successfully started")
        else:
            display_msg("FAIL: Failed to start GMC promotion")
            assert False
        
        count = 0
        display_msg("Sleeping till Grid comes up")
        sleep(120)
        while not is_grid_alive():
            if count == 4:
                display_msg("Giving up after 5 tries")
                assert False
            display_msg("Sleeping for 1 more minute...")
            sleep(60)
            count += 1

        display_msg("---------Test Case 19 Execution Completed----------")

    @pytest.mark.run(order=20)
    def test_020_Validate_GMC_Promotion_2(self):
        """
        Validate GMC Promotion is complete on the new Master.
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        
        display_msg("Checking if Old GMC has become new Master")
        status = is_master(config.grid1_master_vip)
        if status:
            display_msg("PASS: "+config.grid1_master_vip+" is the new master")
        else:
            display_msg("FAIL: "+config.grid1_master_vip+" is not a master")
            assert False

        display_msg("---------Test Case 20 Execution Completed----------")

    @pytest.mark.run(order=21)
    def test_021_Validate_Default_group_members_are_joined_2(self):
        """
        Validate if the Deafult group's members are joined to new Master
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 21 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Getting the Grid status")
        count = 0
        while count < 6:
            status = is_grid_alive(config.grid1_member1_vip)
            if status:
                break
            display_msg("GMC Member "+config.grid1_member1_vip+" is not up. Sleeping for 10s ...")
            sleep(10)
            count += 1
        online,offline = get_online_offline_members(config.grid1_master_vip)
        display_msg("Online members: ")
        display_msg(online)
        display_msg("Offline members: ")
        display_msg(offline)
        
        display_msg("Getting the GMC Group Members")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup?_return_fields=name,members",grid_vip=config.grid1_master_vip)
        display_msg(get_ref)
        
        groups = json.loads(get_ref)
        flag = False
        for group in groups:
            if group["name"] == "Default":
                for member in group["members"]:
                    if member["member"] in offline:
                        display_msg("FAIL: Grid Member '"+member["member"]+"' from the group '"+group["name"]+"' has not joined the new Master")
                        flag = True
        if flag:
            assert False
        display_msg("All the members from 'Default' group are joined to the new Master")
        
        display_msg("---------Test Case 21 Execution Completed----------")

    @pytest.mark.run(order=22)
    def test_022_Start_capture_syslog_on_master_1(self):
        """
        Start capturing syslog on the master.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 22 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        log("start","/var/log/messages",config.grid1_master_vip)
        display_msg("Started capturing syslog ...")
        
        display_msg("---------Test Case 22 Execution Completed----------")

    @pytest.mark.run(order=23)
    def test_023_Perform_Join_Group_Now_operation_on_group_2(self):
        """
        Perform Join Group Now operation on group 2 (wih 10 minutes scheduled time).
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 23 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Performing Join Group Now operation on 'group 2'")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup?name=group%202",grid_vip=config.grid1_master_vip)
        display_msg(get_ref)
        
        if not json.loads(get_ref):
            display_msg("FAIL: GMC Group 'group 2' not found")
            assert False
        data = {"gmc_group_name":"group 2"}
        ref = json.loads(get_ref)[0]["_ref"]+"?_function=reconnect_group_now"
        response = ib_NIOS.wapi_request('POST',ref=ref,fields=json.dumps(data),grid_vip=config.grid1_master_vip)
        display_msg(response)
        if type(response) == tuple:
                display_msg("Failure: Function call reconnect_group_now failed")
                assert False
        display_msg("PASS: Successfully performed Join Group Now operation on 'group 2'")
        
        display_msg("---------Test Case 23 Execution Completed----------")

    @pytest.mark.run(order=24)
    def test_024_Validate_syslog_for_join_group_now_operation(self):
        """
        Validate syslog for below message when Join Group Now operation is performed.
        Sent master promotion notice to grid member ib-10-35-129-9.infoblox.com (10.35.129.9).
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 24 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Sleeping 60 seconds for the new master to send master promotion notice")
        sleep(100)
        
        display_msg("Stop capturing syslog ...")
        log("stop","/var/log/messages",config.grid1_master_vip)
        
        display_msg("Validate if the master promotion notice is sent to the group 2 members")
        try:
            logv("'Sent master promotion notice to grid member "+config.grid1_member3_fqdn+"'",'/var/log/messages',config.grid1_master_vip)
            logv("'Acknowledgement is received from the pnode "+config.grid1_member3_vip+"'",'/var/log/messages',config.grid1_master_vip)
            #logv("'All members of grid notified of master promotion'",'/var/log/messages',config.grid1_master_vip)
            display_msg("PASS: Master Promotion notice is sent to the group 2 members")
            display_msg("PASS: Acknowledgement is received from the group 2 members")
        except Exception as E:
            if 'returned non-zero exit status 1' in str(E):
                display_msg("FAIL: Above string is not found in the logs")
                assert False
            display_msg(E)
            assert False
        
        display_msg("---------Test Case 24 Execution Completed----------")

    @pytest.mark.run(order=25)
    def test_025_Start_capture_syslog_on_master_2(self):
        """
        Start capturing syslog on the master.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 25 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        log("start","/var/log/messages",config.grid1_master_vip)
        display_msg("Started capturing syslog ...")
        
        display_msg("---------Test Case 25 Execution Completed----------")

    @pytest.mark.run(order=26)
    def test_026_Perform_Join_Group_Now_operation_on_group_2_again(self):
        """
        Perform Join Group Now operation on group 2 again.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 26 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Performing Join Group Now operation on 'group 2' again")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup?name=group%202",grid_vip=config.grid1_master_vip)
        display_msg(get_ref)
        
        if not json.loads(get_ref):
            display_msg("FAIL: GMC Group 'group 2' not found")
            assert False
        data = {"gmc_group_name":"group 2"}
        ref = json.loads(get_ref)[0]["_ref"]+"?_function=reconnect_group_now"
        response = ib_NIOS.wapi_request('POST',ref=ref,fields=json.dumps(data),grid_vip=config.grid1_master_vip)
        display_msg(response)
        if type(response) == tuple:
                display_msg("Failure: Function call reconnect_group_now failed")
                assert False
        display_msg("PASS: Successfully performed Join Group Now operation on 'group 2'")
        
        display_msg("---------Test Case 26 Execution Completed----------")

    @pytest.mark.run(order=27)
    def test_027_Validate_syslog_for_second_join_group_now_operation(self):
        """
        Validate that master promotion notice not sent when second Join Group Now operation is performed.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 27 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Sleeping 30 seconds for the new master to send master promotion notice")
        sleep(30)
        
        display_msg("Stop capturing syslog ...")
        log("stop","/var/log/messages",config.grid1_master_vip)
        
        display_msg("Validate if the master promotion notice is sent to the group 2 members")
        flag = False
        try:
            logv("'Sent master promotion notice to grid member "+config.grid1_member3_fqdn+"'",'/var/log/messages',config.grid1_master_vip)
            flag = True
            display_msg("FAIL: Master Promotion notice is sent to the group 2 members")
            logv("'Acknowledgement is received from the pnode "+config.grid1_member3_vip+"'",'/var/log/messages',config.grid1_master_vip)
            display_msg("FAIL: Acknowledgement is received from the group 2 members")
            assert False
        except Exception as E:
            if flag:
                assert False
            elif 'returned non-zero exit status 1' in str(E):
                display_msg("PASS: Master Promotion notice are not sent to already joined members")
            else:
                display_msg(E)
                assert False
        
        display_msg("---------Test Case 27 Execution Completed----------")

    @pytest.mark.run(order=28)
    def test_028_Validate_syslog_for_master_promotion_notice_2(self):
        """
        Validate syslog for below message when scheduled time is met for group 1 and group 3.
        All members of grid notified of master promotion.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 28 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Start capturing syslog ...")
        log("start","/var/log/messages",config.grid1_master_vip)
        
        global scheduled_time
        current_epoch_time = get_current_epoch_time(config.grid1_master_vip)
        sleep_time = int(scheduled_time) - int(current_epoch_time)
        display_msg("Remaining scheduled time : "+str(sleep_time))
        if sleep_time > 0:
            display_msg("Sleeping "+str(sleep_time)+" seconds to meet the scheduled time")
            sleep(sleep_time+120)
            
            display_msg("Stop capturing syslog ...")
            log("stop","/var/log/messages",config.grid1_master_vip)
            
            display_msg("Validate if the master promotion notice is sent to the group 1 members")
            try:
                logv("'Sent master promotion notice to grid member "+config.grid1_member2_fqdn+"'",'/var/log/messages',config.grid1_master_vip)
                logv("'Acknowledgement is received from the pnode "+config.grid1_member2_vip+"'",'/var/log/messages',config.grid1_master_vip)
                logv("'All members of grid notified of master promotion'",'/var/log/messages',config.grid1_master_vip)
                display_msg("PASS: All the members of the grid notified of master promotion")
            except Exception as E:
                if 'returned non-zero exit status 1' in str(E):
                    display_msg("FAIL: Above string is not found in the logs")
                    assert False
                display_msg(E)
                assert False
        else:
            display_msg("Stop capturing syslog ...")
            log("stop","/var/log/messages",config.grid1_master_vip)
            
            display_msg("WARNING: Scheduled time has already passed")
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(config.grid1_master_vip, username='root', password = 'infoblox')
                stdin, stdout, stderr = client.exec_command("cat /var/log/messages | grep 'All the members of the grid notified of master promotion'")
                error = stderr.read()
                output = stdout.read()
            except Exception as E:
                display_msg(E)
                display_msg("FAIL: Debug the above exception")
                assert False
            finally:
                client.close()
            if error:
                display_msg("Error: "+error)
            display_msg("Output: "+output)
            assert False
        
        display_msg("---------Test Case 28 Execution Completed----------")

    @pytest.mark.run(order=29)
    def test_029_Update_scheduled_time_for_group_1(self):
        """
        Update scheduled time for 'group 1' to 6 minutes in future.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 29 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        global scheduled_time
        display_msg("Force end the GMC Promotion if it is in progress")
        gmc_promotion_forced_end(config.grid1_master_vip)
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup",grid_vip=config.grid1_master_vip)
        display_msg(get_ref)
        current_epoch_time = int(get_current_epoch_time(config.grid1_master_vip))
        
        #group 1
        scheduled_time = current_epoch_time + (6*60)
        display_msg("Current epoch time: "+str(current_epoch_time))
        display_msg("Scheduled time : "+str(scheduled_time))
        create_gmc_promotion_group('group 1',scheduled_time,members=[config.grid1_member2_fqdn],grid_master=config.grid1_master_vip)
        
        display_msg("---------Test Case 29 Execution Completed----------")

    @pytest.mark.run(order=30)
    def test_030_Perform_Master_Promotion_3(self):
        """
        Perform Master Promotion on GMC.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 30 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Perform GMC Promotion")
        args = "sshpass -p 'infoblox' ssh -o StrictHostKeyChecking=no admin@"+config.grid1_member1_vip
        args = shlex.split(args)
        try:
            child = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            child.stdin.write("set promote_master\n")
            child.stdin.write("y\n")
            child.stdin.write("y\n")
            child.stdin.write("y\n")
        except Exception as E:
            display_msg(E)
            display_msg("FAIL: Debug the above exception")
        finally:
            output = child.communicate()
        flag = False
        for line in output:
            display_msg(line)
            if 'Master promotion beginning on this member' in line:
                flag = True
        if flag:
            display_msg("PASS: GMC promotion successfully started")
        else:
            display_msg("FAIL: Failed to start GMC promotion")
            assert False
        
        count = 0
        display_msg("Sleeping till Grid comes up")
        sleep(120)
        while not is_grid_alive(config.grid1_member1_vip):
            if count == 4:
                display_msg("Giving up after 5 tries")
                assert False
            display_msg("Sleeping for 1 more minute...")
            sleep(60)
            count += 1

        display_msg("---------Test Case 30 Execution Completed----------")

    @pytest.mark.run(order=31)
    def test_031_Validate_GMC_Promotion_3(self):
        """
        Validate GMC Promotion is complete on the new Master.
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        
        display_msg("Checking if Old GMC has become new Master")
        status = is_master(config.grid1_member1_vip)
        if status:
            display_msg("PASS: "+config.grid1_member1_vip+" is the new master")
        else:
            display_msg("FAIL: "+config.grid1_member1_vip+" is not a master")
            assert False

        display_msg("---------Test Case 31 Execution Completed----------")

    @pytest.mark.run(order=32)
    def test_032_Validate_Default_group_members_are_joined_3(self):
        """
        Validate if the Deafult group's members are joined to new Master
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 32 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Getting the Grid status")
        count = 0
        while count < 6:
            status = is_grid_alive(config.grid_vip)
            if status:
                break
            display_msg("GMC Member "+config.grid_vip+" is not up. Sleeping for 10s ...")
            sleep(10)
            count += 1
        online,offline = get_online_offline_members(config.grid1_member1_vip)
        display_msg("Online members: ")
        display_msg(online)
        display_msg("Offline members: ")
        display_msg(offline)
        
        display_msg("Getting the GMC Group Members")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup?_return_fields=name,members",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        
        groups = json.loads(get_ref)
        flag = False
        for group in groups:
            if group["name"] == "Default":
                for member in group["members"]:
                    if member["member"] in offline:
                        display_msg("FAIL: Grid Member '"+member["member"]+"' from the group '"+group["name"]+"' has not joined the new Master")
                        flag = True
        if flag:
            assert False
        display_msg("All the members from 'Default' group are joined to the new Master")
        
        display_msg("---------Test Case 32 Execution Completed----------")

    @pytest.mark.run(order=33)
    def test_033_Execute_set_gmc_promotion_forced_end_CLI_on_members(self):
        """
        Execute set gmc_promotion forced_end CLI on the member grid1_member2_vip.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 33 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Execute 'set gmc_promotion forced_end' CLI on members")
        return_code = gmc_promotion_forced_end(config.grid1_member2_vip)
        if return_code == 3: 
            display_msg("PASS: Executing 'set gmc_promotion forced_end' CLI is restricted on members")
        else:
            assert False
        
        display_msg("---------Test Case 33 Execution Completed----------")

    @pytest.mark.run(order=34)
    def test_034_Validate_if_GMC_Promotion_ended_1(self):
        """
        Validate if GMC Promotion is ended (Negative).
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 34 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Validate GMC Promotion status")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        
        for ref in json.loads(get_ref):
            if 'group 1' in ref['name']:
                data = {"comment":"Updated comment in test_034"}
                response = ib_NIOS.wapi_request("PUT",ref=ref['_ref'],fields=json.dumps(data),grid_vip=config.grid1_member1_vip)
                display_msg(response)
                if 'gmc promotion is in progress' in str(response):
                    display_msg("PASS: GMC Promotion process is still in progress")
                else:
                    display_msg("FAIL: GMC Promotion process is completed")
                    assert False
        
        display_msg("---------Test Case 34 Execution Completed----------")

    @pytest.mark.run(order=35)
    def test_035_Execute_set_gmc_promotion_forced_end_CLI_on_Master(self):
        """
        Execute set gmc_promotion forced_end CLI on the Master.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 35 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Execute 'set gmc_promotion forced_end' CLI on the Master")
        return_code = gmc_promotion_forced_end(config.grid1_member1_vip)
        if return_code == 1: 
            display_msg("PASS: Executing 'set gmc_promotion forced_end' is successful on the Master")
        else:
            assert False
        
        display_msg("---------Test Case 35 Execution Completed----------")

    @pytest.mark.run(order=36)
    def test_036_Validate_if_GMC_Promotion_ended_2(self):
        """
        Validate if GMC Promotion is ended (Positive).
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 36 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Validate GMC Promotion status")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        
        for ref in json.loads(get_ref):
            if 'group 1' in ref['name']:
                data = {"comment":"Updated comment in test_036"}
                response = ib_NIOS.wapi_request("PUT",ref=ref['_ref'],fields=json.dumps(data),grid_vip=config.grid1_member1_vip)
                display_msg(response)
                if 'gmc promotion is in progress' in str(response):
                    display_msg("FAIL: GMC Promotion process is still in progress")
                    assert False
                else:
                    display_msg("PASS: GMC Promotion process is completed")
                    
        display_msg("---------Test Case 36 Execution Completed----------")

    @pytest.mark.run(order=37)
    def test_037_Execute_set_gmc_promotion_disable_CLI_on_Non_GMC_Members(self):
        """
        Execute set gmc_promotion disable CLI on the Non-GMC member.

        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 37 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Execute 'set gmc_promotion disable' CLI on members")
        return_code = gmc_promotion_disable(config.grid1_member2_vip)
        if return_code: 
            display_msg("FAIL: Executing 'set gmc_promotion disable' is successful on the Member")
            assert False
        else:
            display_msg("PASS: Executing 'set gmc_promotion disable' failed on the Member")
        
        display_msg("---------Test Case 37 Execution Completed----------")

    @pytest.mark.run(order=38)
    def test_038_Validate_if_GMC_Group_Promotion_Schedule_is_deactivated_1(self):
        """
        Validate if GMC Group Promotion Schedule is deactivated (Negative).
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 38 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Validate GMC Group Promotion Schedule is deactivated")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcschedule",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        
        if 'true' in get_ref:
            display_msg("PASS: GMC Group Promotion Schedule is still active")
        else:
            display_msg("FAIL: GMC Group Promotion Schedule is deactivated")
            assert False
                    
        display_msg("---------Test Case 38 Execution Completed----------")

    @pytest.mark.run(order=39)
    def test_039_Execute_set_gmc_promotion_disable_CLI_on_GMC_Member(self):
        """
        Execute set gmc_promotion disable CLI on the GMC member.

        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 39 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Execute 'set gmc_promotion disable' CLI on GMC members")
        return_code = gmc_promotion_disable(config.grid1_master_vip)
        if return_code: 
            display_msg("PASS: Executing 'set gmc_promotion disable' is successful on the Master")
            return_code = gmc_promotion_disable(config.grid1_master_vip)
            if return_code:
                pass
        else:
            assert False
        
        display_msg("---------Test Case 39 Execution Completed----------")

    @pytest.mark.run(order=40)
    def test_040_Validate_if_GMC_Group_Promotion_Schedule_is_deactivated_2(self):
        """
        Validate if GMC Group Promotion Schedule is deactivated (Positive).
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 40 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Validate GMC Group Promotion Schedule is deactivated")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcschedule",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        
        if 'true' in get_ref:
            display_msg("FAIL: GMC Group Promotion Schedule is still active")
            assert False
        else:
            display_msg("PASS: GMC Group Promotion Schedule is deactivated")
                    
        display_msg("---------Test Case 40 Execution Completed----------")

    @pytest.mark.run(order=41)
    def test_041_Validate_syslog_for_master_promotion_notice_3(self):
        """
        Validate syslog for below message when scheduled time is met for group 1.
        All members of grid notified of master promotion.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 41 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Start capturing syslog ...")
        log("start","/var/log/messages",config.grid1_member1_vip)
        
        global scheduled_time
        current_epoch_time = get_current_epoch_time(config.grid1_member1_vip)
        sleep_time = int(scheduled_time) - int(current_epoch_time)
        display_msg("Remaining scheduled time : "+str(sleep_time))
        if sleep_time > 0:
            display_msg("Sleeping "+str(sleep_time)+" seconds to meet the scheduled time")
            sleep(sleep_time+120)
            
            display_msg("Stop capturing syslog ...")
            log("stop","/var/log/messages",config.grid1_member1_vip)
            
            display_msg("Validate if the master promotion notice is sent to the group 1 members")
            try:
                logv("'Sent master promotion notice to grid member "+config.grid1_member2_fqdn+"'",'/var/log/messages',config.grid1_member1_vip)
                logv("'Acknowledgement is received from the pnode "+config.grid1_member2_vip+"'",'/var/log/messages',config.grid1_member1_vip)
                logv("'All members of grid notified of master promotion'",'/var/log/messages',config.grid1_member1_vip)
                display_msg("PASS: All the members of the grid notified of master promotion")
            except Exception as E:
                if 'returned non-zero exit status 1' in str(E):
                    display_msg("FAIL: Above string is not found in the logs")
                    assert False
                display_msg(E)
                assert False
        else:
            display_msg("Stop capturing syslog ...")
            log("stop","/var/log/messages",config.grid1_member1_vip)
            
            display_msg("WARNING: Scheduled time has already passed")
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(config.grid1_member1_vip, username='root', password = 'infoblox')
                stdin, stdout, stderr = client.exec_command("cat /var/log/messages | grep 'All the members of the grid notified of master promotion'")
                error = stderr.read()
                output = stdout.read()
            except Exception as E:
                display_msg(E)
                display_msg("FAIL: Debug the above exception")
                assert False
            finally:
                client.close()
            if error:
                display_msg("Error: "+error)
            display_msg("Output: "+output)
            assert False
        
        display_msg("---------Test Case 41 Execution Completed----------")

    @pytest.mark.run(order=42)
    def test_042_Add_offline_member(self):
        """
        Add Offline member to the grid.
        """
        display_msg()
        display_msg("+--------------------------------------------------+")
        display_msg("|          Test Case 42 Execution Started           |")
        display_msg("+--------------------------------------------------+")
        
        display_msg("Add Offline member")
        data = {"host_name": "offline.member",
                "vip_setting":{"address":"10.35.2.2",
                               "gateway":"10.35.0.1",
                               "subnet_mask":"255.255.0.0"}
                }
        response = ib_NIOS.wapi_request('POST',object_type="member",fields=json.dumps(data),grid_vip=config.grid1_member1_vip)
        display_msg(response)
        if type(response) == tuple:
            display_msg("FAIL: Failed to add offline member")
            assert False
        display_msg("PASS: Successfully added offline member")
        
        display_msg("---------Test Case 42 Execution Completed----------")

    @pytest.mark.run(order=43)
    def test_043_Validate_offline_member(self):
        """
        Validate if offline member is added successfully.
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        member_ref = ib_NIOS.wapi_request('GET', object_type='member', params='?host_name=offline.member',grid_vip=config.grid1_member1_vip)
        display_msg(member_ref)
        if 'offline.member' in member_ref:
            display_msg("PASS: Offline member found")
        else:
            display_msg("FAIL: Offline member not found")
            assert False

        display_msg("---------Test Case 43 Execution Completed----------")

    @pytest.mark.run(order=44)
    def test_044_Delete_all_custom_GMC_groups(self):
        """
        Delete all the custom GMC groups except Default group.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 44 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Deleting all the custom GMC groups")
        gmc_promotion_forced_end(config.grid1_member1_vip)
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        for group in json.loads(get_ref):
            if group["name"] == "Default":
                continue
            response = ib_NIOS.wapi_request("DELETE", ref=group["_ref"],grid_vip=config.grid1_member1_vip)
            if type(response) == tuple:
                display_msg(response)
                display_msg("FAIL: Failed to delete group : "+group["name"])
                assert False
        display_msg("PASS: All the custom groups are deleted")
        
        display_msg("---------Test Case 44 Execution Completed----------")

    @pytest.mark.run(order=45)
    def test_045_Validate_all_GMC_groups_deleted(self):
        """
        Validate all the custom GMC groups are deleted.
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        
        display_msg("Validate all the custom GMC groups are deleted")
        gmc_promotion_forced_end(config.grid1_member1_vip)
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        if not len(json.loads(get_ref)) == 1:
            display_msg("FAIL: Custom GMC groups are found")
            assert False
        display_msg("PASS: All the custom groups are deleted")
        
        display_msg("---------Test Case 45 Execution Completed----------")

    @pytest.mark.run(order=46)
    def test_046_Create_GMC_Group_group_1(self):
        """
        Create GMC Group 'group 1'.
        Add offline member 'offline.member' to the group.
        Schedule this group to 15 minutes in future.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 46 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        global scheduled_time
        display_msg("Force end the GMC Promotion if it is in progress")
        gmc_promotion_forced_end(config.grid1_member1_vip)
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        current_epoch_time = int(get_current_epoch_time(config.grid1_member1_vip))
        
        #group 1
        scheduled_time = current_epoch_time + (15*60)
        display_msg("Current epoch time: "+str(current_epoch_time))
        display_msg("Scheduled time : "+str(scheduled_time))
        create_gmc_promotion_group('group 1',scheduled_time,members=['offline.member'],grid_master=config.grid1_member1_vip)
        
        display_msg("---------Test Case 46 Execution Completed----------")

    @pytest.mark.run(order=47)
    def test_047_Validate_created_GMC_Promotion_Group(self):
        """
        Validate created GMC Promotion Groups 'group 1'.
        """        
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup?_return_fields=name,members",grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        if 'group 1' not in get_ref:
            display_msg("FAIL: GMC Promotion Group 'group 1' not found")
            assert False
        display_msg("PASS: GMC Promotion Group 'group 1' found")

        display_msg("---------Test Case 47 Execution Completed----------")

    @pytest.mark.run(order=48)
    def test_048_Activate_GMC_Group_Promotion_Schedule_2(self):
        """
        Enable Activate GMC Group Promotion Schedule.
        """
        display_msg()
        display_msg("+--------------------------------------------------+")
        display_msg("|          Test Case 48 Execution Started           |")
        display_msg("+--------------------------------------------------+")
        
        display_msg("Activate GMC Group Promotion Schedule")
        get_ref = ib_NIOS.wapi_request('GET', object_type='gmcschedule?_return_fields=activate_gmc_group_schedule',grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        response = ib_NIOS.wapi_request('PUT', ref=json.loads(get_ref)[0]['_ref'], fields=json.dumps({"activate_gmc_group_schedule":True}),grid_vip=config.grid1_member1_vip)
        if type(response) == tuple:
            display_msg(response)
            display_msg("FAIL: Activate GMC Group Promotion Schedule")
            assert False
        display_msg("PASS: Enabled Activate GMC Group Promotion Schedule")
        sleep(30)

        display_msg("---------Test Case 48 Execution Completed----------")

    @pytest.mark.run(order=49)
    def test_049_Validate_Activate_GMC_Group_Promotion_Schedule_2(self):
        """
        Validate if Activate GMC Group Promotion Schedule is enabled.
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        get_ref = ib_NIOS.wapi_request('GET', object_type='gmcschedule?_return_fields=activate_gmc_group_schedule',grid_vip=config.grid1_member1_vip)
        display_msg(get_ref)
        if 'true' in get_ref:
            display_msg("PASS: Activate GMC Group Promotion Schedule validation")
        else:
            display_msg("FAIL: Activate GMC Group Promotion Schedule validation")
            assert False
        
        display_msg("---------Test Case 49 Execution Completed----------")

    @pytest.mark.run(order=50)
    def test_050_Perform_Master_Promotion_4(self):
        """
        Perform Master Promotion on GMC.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 50 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Perform GMC Promotion")
        args = "sshpass -p 'infoblox' ssh -o StrictHostKeyChecking=no admin@"+config.grid1_master_vip
        args = shlex.split(args)
        try:
            child = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            child.stdin.write("set promote_master\n")
            child.stdin.write("y\n")
            child.stdin.write("y\n")
            child.stdin.write("y\n")
        except Exception as E:
            display_msg(E)
            display_msg("FAIL: Debug the above exception")
            assert False
        finally:
            output = child.communicate()
        flag = False
        for line in output:
            display_msg(line)
            if 'Master promotion beginning on this member' in line:
                flag = True
        if flag:
            display_msg("PASS: GMC promotion successfully started")
        else:
            display_msg("FAIL: Failed to start GMC promotion")
            assert False
        
        count = 0
        display_msg("Sleeping till Grid comes up")
        sleep(120)
        while not is_grid_alive(config.grid1_master_vip):
            if count == 4:
                display_msg("Giving up after 5 tries")
                assert False
            display_msg("Sleeping for 1 more minute...")
            sleep(60)
            count += 1

        display_msg("---------Test Case 50 Execution Completed----------")

    @pytest.mark.run(order=51)
    def test_051_Validate_GMC_Promotion_4(self):
        """
        Validate GMC Promotion is complete on the new Master.
        """
        display_msg()
        display_msg("+------------------------------------------+")
        display_msg("|           Validation                     |")
        display_msg("+------------------------------------------+")
        
        display_msg("Checking if Old GMC has become new Master")
        status = is_master(config.grid1_master_vip)
        if status:
            display_msg("PASS: "+config.grid1_master_vip+" is the new master")
        else:
            display_msg("FAIL: "+config.grid1_master_vip+" is not a master")
            assert False

        display_msg("---------Test Case 51 Execution Completed----------")

    @pytest.mark.run(order=52)
    def test_052_Validate_Default_group_members_are_joined_4(self):
        """
        Validate if the Deafult group's members are joined to new Master
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 52 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Getting the Grid status")
        sleep(60)
        online,offline = get_online_offline_members(config.grid1_master_vip)
        display_msg("Online members: ")
        display_msg(online)
        display_msg("Offline members: ")
        display_msg(offline)
        
        display_msg("Getting the GMC Group Members")
        get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup?_return_fields=name,members",grid_vip=config.grid1_master_vip)
        display_msg(get_ref)
        
        groups = json.loads(get_ref)
        flag = False
        for group in groups:
            if group["name"] == "Default":
                for member in group["members"]:
                    if member["member"] in offline:
                        display_msg("FAIL: Grid Member '"+member["member"]+"' from the group '"+group["name"]+"' has not joined the new Master")
                        flag = True
        if flag:
            assert False
        display_msg("All the members from 'Default' group are joined to the new Master")
        
        display_msg("---------Test Case 52 Execution Completed----------")

    @pytest.mark.run(order=53)
    def test_053_Validate_syslog_for_master_promotion_notice_4(self):
        """
        Validate syslog when scheduled time is met for offline member.
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 53 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Start capturing syslog ...")
        log("start","/var/log/messages",config.grid1_master_vip)
        
        global scheduled_time
        current_epoch_time = get_current_epoch_time(config.grid1_master_vip)
        sleep_time = int(scheduled_time) - int(current_epoch_time)
        display_msg("Remaining scheduled time : "+str(sleep_time))
        if sleep_time > 0:
            display_msg("Sleeping "+str(sleep_time)+" seconds to meet the scheduled time")
            sleep(sleep_time+30)
            
        else:
            display_msg("WARNING: Scheduled time has already passed")
        
        display_msg("Stop capturing syslog ...")
        log("stop","/var/log/messages",config.grid1_master_vip)
        
        display_msg("Validate if the master promotion notice is sent to the group 1 members")
        sleep(300)
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(config.grid1_master_vip, username='root', password = 'infoblox')
            stdin, stdout, stderr = client.exec_command("cat /var/log/messages | grep 'Sent master promotion notice to grid member offline.member'")
            error = stderr.read()
            output = stdout.read()
        except Exception as E:
            display_msg(E)
            display_msg("FAIL: Debug the above exception")
            assert False
        finally:
            client.close()
        if error:
            display_msg("Error: "+error)
            assert False
        display_msg("Output: "+output)
        if len(output.split('\n')) < 5:
            display_msg("FAIl: Periodic retries not happening for offline.member member")
            assert False
        
        display_msg("---------Test Case 52 Execution Completed----------")

    @pytest.mark.run(order=54)
    def test_054_Validate_if_GMC_Promotion_ended_3(self):
        """
        Validate if GMC Promotion is ended (Positive).
        """
        display_msg()
        display_msg("----------------------------------------------------")
        display_msg("|          Test Case 54 Execution Started          |")
        display_msg("----------------------------------------------------")
        
        display_msg("Validate GMC Promotion status")
        count = 0
        flag = False
        while count < 3:
            get_ref = ib_NIOS.wapi_request('GET',object_type="gmcgroup",grid_vip=config.grid1_member1_vip)
            display_msg(get_ref)
            
            for ref in json.loads(get_ref):
                if 'group 1' in ref['name']:
                    data = {"comment":"Updated comment in test_053"}
                    response = ib_NIOS.wapi_request("PUT",ref=ref['_ref'],fields=json.dumps(data),grid_vip=config.grid1_member1_vip)
                    display_msg(response)
                    if 'gmc promotion is in progress' in str(response):
                        display_msg("INFO: GMC Promotion process is still in progress")
                        display_msg("Sleeping for 60 seconds ...")
                    else:
                        display_msg("PASS: GMC Promotion process is completed")
                        flag = True
                        break
            count += 1
            sleep(60)
        if not flag:
            display_msg("FAIL: GMC Group Promotion Schedule wizard is still not released after 3 minutes")
            assert False
                    
        display_msg("---------Test Case 54 Execution Completed----------")