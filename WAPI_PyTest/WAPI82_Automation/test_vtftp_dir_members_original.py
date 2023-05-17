import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import os
import ib_utils.ib_NIOS as ib_NIOS
class MemberFileDistribution(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
         usually contains tests).
         """
        logging.info("SETUP METHOD")

    def simple_func(self,a):
        # do any process here and return the value
        # Return value is comparted(asserted) in test case method
        return(a+2)

    @pytest.mark.run(order=1)
    def test_1_create_tftpfiledir1_vtftp_dir_members(self):
        logging.info("Create the tftpfiledir Directory type")
        data = {"directory": "/","name": "NewDirectory","type": "DIRECTORY"}
        response1 = ib_NIOS.wapi_request('POST', object_type="tftpfiledir",fields=json.dumps(data))
        logging.info(response1)
        assert  re.search(r"tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9OZXdEaXJlY3Rvcnk:DIRECTORY/NewDirectory",response1)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=2)
    def test_2_tftp_acls_with_true_member_FD_vtftp_dir_members(self):
        logging.info("Update operation for tftp_acls fields with acl values")
        data = {"tftp_acls":[{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.36.199.8","permission": "DENY"},{"address": "10.35.0.0/16","permission": "ALLOW"},{"address": "10.37.0.0/16","permission": "DENY"},{"address": "Any","permission": "ALLOW"}] }
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_acls", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["tftp_acls"] == [{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.36.199.8","permission": "DENY"},{"address": "10.35.0.0/16","permission": "ALLOW"},{"address": "10.37.0.0/16","permission": "DENY"},{"address": "Any","permission": "ALLOW"}]
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=3)
    def test_3_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
	d = config.grid_fqdn
        data = {"vtftp_dir_members": [{"address": "10.36.199.8","ip_type": "ADDRESS","member": d}]}
        response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        res = json.loads(response1)
        print res
        i = res['vtftp_dir_members'][0]
        assert i["address"] == "10.36.199.8" and i["ip_type"] == "ADDRESS" and i["member"] == config.grid_fqdn
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=4)
    def test_4_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -Invalid IP address")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
	d =config.grid_fqdn
        data = {"vtftp_dir_members": [{"address": "a10.36.199.8","ip_type": "ADDRESS","member": d}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r'Invalid value for address: .*a10.36.199.8.*: Invalid IP address',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=5)
    def test_5_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -Invalid value for ip_type")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
	d = config.grid_fqdn
        data = {"vtftp_dir_members": [{"address": "10.36.199.8","ip_type": "ADDRESS1","member": d}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r'Invalid value for ip_type (.*ADDRESS1.*) valid values are: ADDRESS, NETWORK, RANGE',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=6)
    def test_6_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
        data = {"vtftp_dir_members": [{"address": "10.36.199.8","ip_type": "ADDRESS1","member": "infoblox.localdomain1"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 404 and re.search(r'Grid Member infoblox.localdomain1 not found',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")	
		
		
    @pytest.mark.run(order=7)
    def test_7_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -Network")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
	d = config.grid_fqdn
        data = {"vtftp_dir_members": [{"cidr": 16,"ip_type": "NETWORK","member": d,"network": "10.37.0.0"}]}
        response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        res = json.loads(response1)
        print res
        i = res['vtftp_dir_members'][0]
        assert i["cidr"] == 16 and i["ip_type"] == "NETWORK" and i["member"] == config.grid_fqdn and i["network"] == "10.37.0.0"
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")	
    @pytest.mark.run(order=8)
    def test_8_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -Network cidr with 17")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
	d = config.grid_fqdn
        data = {"vtftp_dir_members": [{"cidr": 17,"ip_type": "NETWORK","member": d,"network": "10.37.0.0"}]}
        response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        res = json.loads(response1)
        print res
        i = res['vtftp_dir_members'][0]
        assert i["cidr"] == 17 and i["ip_type"] == "NETWORK" and i["member"] == config.grid_fqdn and i["network"] == "10.37.0.0"
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=9)
    def test_9_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -Network cidr with 16")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
	d= config.grid_fqdn
        data = {"vtftp_dir_members": [{"cidr": 16,"ip_type": "NETWORK","member": d,"network": "10.37.0.0"}]}
        response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        res = json.loads(response1)
        print res
        i = res['vtftp_dir_members'][0]
        assert i["cidr"] == 16 and i["ip_type"] == "NETWORK" and i["member"] == config.grid_fqdn and i["network"] == "10.37.0.0"
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")			
    @pytest.mark.run(order=10)
    def test_10_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -1")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
	d = config.grid_fqdn
        data = {"vtftp_dir_members": [{"cidr": 16,"ip_type": "NETWORK1","member": d,"network": "10.37.0.0"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r'Invalid value for ip_type (.*NETWORK1.*) valid values are: ADDRESS, NETWORK, RANGE',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=11)
    def test_11_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -2")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
        data = {"vtftp_dir_members": [{"cidr": 16,"ip_type": "NETWORK","member": "infoblox.localdomain1","network": "10.37.0.0"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 404 and re.search(r'Grid Member infoblox.localdomain1 not found',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")	
		
    @pytest.mark.run(order=12)
    def test_12_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -Range")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
	d = config.grid_fqdn
        data = {"vtftp_dir_members": [{"end_address": "10.35.0.10","ip_type": "RANGE","member": d,"start_address":"10.35.0.2"}]}
        response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        res = json.loads(response1)
        print res
        i = res['vtftp_dir_members'][0]
        assert i["end_address"] == "10.35.0.10" and i["ip_type"] == "RANGE" and i["member"] == config.grid_fqdn and i["start_address"] == "10.35.0.2"
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")	
    @pytest.mark.run(order=13)
    def test_13_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -Range 1")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
	d = config.grid_fqdn
        data = {"vtftp_dir_members": [{"end_address": "10.35.0.100","ip_type": "RANGE","member": d,"start_address":"10.35.0.200"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Invalid range with start address '10.35.0.200' and end address '10.35.0.100'.",response1)
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")			
    @pytest.mark.run(order=14)
    def test_14_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -Range 2")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
	d = config.grid_fqdn
        data = {"vtftp_dir_members": [{"end_address": "10.35.0.255","ip_type": "RANGE","member": d,"start_address":"10.35.0.20"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Invalid range with start address '10.35.0.20' and end address '10.35.0.255'.",response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")	
		
    @pytest.mark.run(order=15)
    def test_15_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir -Range 3")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
	d = config.grid_fqdn
        data = {"vtftp_dir_members": [{"end_address": "10.35.0.10","ip_type": "RANGE1","member": d,"start_address":"10.35.0.2"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Invalid value for ip_type (.*RANGE1.*) valid values are: ADDRESS, NETWORK, RANGE",response1)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")	
    @pytest.mark.run(order=16)
    def test_16_update_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Update the vtftp_dir_members field in tftpfiledir Range")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
        data = {"vtftp_dir_members": []}
        response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=vtftp_dir_members",fields=json.dumps(data))
        logging.info(response1)
        res = json.loads(response1)
        print res
        assert res['vtftp_dir_members'] == []
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=17)
    def test_17_delete_vtftp_dir_members_field_tftpfiledir(self):
        logging.info("Delete the vtftp_dir_members field in tftpfiledir Range")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
        response1 = ib_NIOS.wapi_request('DELETE', ref=ref1)
        logging.info(response1)
        assert re.search(r"tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9OZXdEaXJlY3Rvcnk:DIRECTORY/NewDirectory",response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=18)
    def test_18_tftp_acls_with_true_member_FD_vtftp_dir_members(self):
        logging.info("Update operation for tftp_acls fields with default acl values")
        data = {"tftp_acls":[] }
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_acls", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["tftp_acls"] == []
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")
