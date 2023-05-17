import os
import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS


class Grid_Setup(unittest.TestCase):

        @pytest.mark.run(order=1)
        def test_1_Start_Discovery_Services(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:memberproperties")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[2]['_ref']
                print ref
                logging.info("Enabling Discovery Services")
                data = {"enable_service":True}
                response = ib_NIOS.wapi_request('PUT', object_type=ref, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Started Discovery services")

        @pytest.mark.run(order=2)
        def test_2_Adding_Network_MS(self):
		logging.info("Adding_Network for MS")
		data = {"network":"19.0.0.0/8","members": [{"_struct": "msdhcpserver", "ipv4addr": "10.102.31.70"}]}
                response = ib_NIOS.wapi_request('POST', object_type="network", fields=json.dumps(data))
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Adding Network is completed")


        @pytest.mark.run(order=3)
        def test_3_Adding_Network_MS(self):
                logging.info("Adding Range for Network")
                data = {"end_addr": "19.0.0.254", "network": "19.0.0.0/8","start_addr": "19.0.0.1","ms_server": {"_struct": "msdhcpserver", "ipv4addr": "10.102.31.70"}}
                response = ib_NIOS.wapi_request('POST', object_type="range", fields=json.dumps(data))
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Adding Network is completed")


	@pytest.mark.run(order=4)
	def test_4_create_admin_group(self):
		logging.info("create_admin_group")
		data = {"name":"user"}
		response = ib_NIOS.wapi_request('POST', object_type="admingroup",fields=json.dumps(data))
		logging.info(response)
		logging.info("============================")
		print response


	@pytest.mark.run(order=5)
	def test_5_create_admin_user(self):
		logging.info("create_admin_user")
		data = {"admin_groups":["user"],"name": "user","password":"infoblox"}
		response = ib_NIOS.wapi_request('POST', object_type="adminuser",fields=json.dumps(data))
		logging.info(response)
		logging.info("============================")
		print response


	@pytest.mark.run(order=6)
	def test_6_create_admin_group(self):
		logging.info("create_admin_group")
		data = {"name":"user1"}
		response = ib_NIOS.wapi_request('POST', object_type="admingroup",fields=json.dumps(data))
		logging.info(response)
		logging.info("============================")
		print response


	@pytest.mark.run(order=7)
	def test_7_create_admin_user(self):
		logging.info("create_admin_user")
		data = {"admin_groups":["user1"],"name": "user1","password":"infoblox"}
		response = ib_NIOS.wapi_request('POST', object_type="adminuser",fields=json.dumps(data))
		logging.info(response)
		logging.info("============================")
		print response

        @pytest.mark.run(order=8)
        def test_8_create_Auth_Zone(self):
                logging.info("Create A Auth_Zone")
                data = {"fqdn":"testing.com","grid_primary": [{"name": config.grid_fqdn, "stealth": False}]}
                response = ib_NIOS.wapi_request('POST', object_type="zone_auth", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("create_for_sign_the_zone")
		data = {"operation":"SIGN"}
		response = ib_NIOS.wapi_request('POST',ref=ref,params='?_function=dnssec_operation',fields=json.dumps(data))
		logging.info(response)
		logging.info("============================")

        @pytest.mark.run(order=9)
        def test_9_Start_Threat_Protection_Services(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="member:threatprotection")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Enabling Threat protection Services")
                data = {"enable_service":True}
                response = ib_NIOS.wapi_request('PUT', object_type=ref, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Started Threat protection services")

        @pytest.mark.skip(order=10)
        def test_10_create_hsm_thalesgroup(self):
                logging.info("Test Create new hsm_thalesgroup ")
                data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}],"pass_phrase":"Infoblox.123"}
                response = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 10 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=11)
        def test_11_Creating_Zone_Rp(self):
                logging.info("Test Creating a new zone rp")
                data = {"fqdn": "rpz.com","grid_primary": [{"name": config.grid_fqdn}]}
                response = ib_NIOS.wapi_request('POST', object_type="zone_rp", fields=json.dumps(data))
                print response 
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response: 
                        assert True
                logging.info("Added new Zone_rp")
                logging.info("============================")

        @pytest.mark.run(order=12)
        def test_12_Adding_RPZ_Blacklist(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_rp")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Adding RPZ Blacklist")
                data = {"dns_tunnel_black_list_rpz_zones": [ref1]}
                response = ib_NIOS.wapi_request('PUT', object_type=ref, fields=json.dumps(data))
                print response 
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response: 
                        assert True
		os.system('sleep 60')
                logging.info("Added RPZ Blacklist")
                logging.info("============================")

        @pytest.mark.run(order=13)
        def test_13_Start_Threat_Analytics_Services(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="member:threatanalytics")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Enabling Threat protection Services")
                data = {"enable_service":True}
                response = ib_NIOS.wapi_request('PUT', object_type=ref, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Started threat analytics services")
