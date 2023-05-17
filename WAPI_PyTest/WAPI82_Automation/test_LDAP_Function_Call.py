import re
import os
import config
import pytest
import unittest
import logging
import subprocess
import json
import time
import ib_utils.ib_NIOS as ib_NIOS


class LDAP_Auth_Service_Function_Call(unittest.TestCase):


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
        def test_1_POST_On_check_ldap_server_settings_FC_LDAP_Auth_Service(self):
                logging.info("Test Create a New LDAP auth Service object")
                data = {"name":"LDAP","servers": [{"address": "test.com", "authentication_type": "ANONYMOUS","base_dn": "o=edirectory", "disable": False, "encryption": "SSL", "port": 636, "use_mgmt_port": False, "version": "V3"}],"ldap_user_attribute":"admin","recovery_interval":30,"retries":5,"timeout":5}
                response = ib_NIOS.wapi_request('POST',object_type="ldap_auth_service",fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")



	@pytest.mark.run(order=2)
	def test_2_GET_On_check_ldap_server_settings_FC_LDAP_Auth_Service(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ldap_auth_service")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test GET On check_ldap_server_settings function call in LDAP auth Service object")
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,params="?_function=check_ldap_server_settings")
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Function check_ldap_server_settings illegal with this method',response)
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")

		
		
	@pytest.mark.run(order=3)
	def test_3_DELETE_On_check_ldap_server_settings_FC_LDAP_Auth_Service(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ldap_auth_service")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test DELETE On check_ldap_server_settings function call in LDAP auth Service object")
		status,response = ib_NIOS.wapi_request('DELETE',object_type=ref,params="?_function=check_ldap_server_settings")
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Function check_ldap_server_settings illegal with this method',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=4)
	def test_4_PUT_On_check_ldap_server_settings_FC_LDAP_Auth_Service(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ldap_auth_service")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test PUT On check_ldap_server_settings function call in LDAP auth Service object")
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,params="?_function=check_ldap_server_settings")
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Function check_ldap_server_settings illegal with this method',response)
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")
		
		

	@pytest.mark.run(order=5)
	def test_5_Req_field_check_ldap_server_settings_FC_LDAP_Auth_Service(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ldap_auth_service")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test required field wih check_ldap_server_settings function call in LDAP auth Service object")
		data = {}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=check_ldap_server_settings",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: required function parameter missing: ldap_server',response)
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=6)
	def test_6_version_check_ldap_server_settings_FC_LDAP_Auth_Service(self):
		logging.info("Test required field wih check_ldap_server_settings function call in LDAP auth Service object")
		data = {"ldap_server": {"address": "10.39.39.150","authentication_type": "AUTHENTICATED","base_dn": "o=edirectory","bind_user_dn": "cn=Admin,o=edirectory","bind_password": "infoblox","comment": "for the purpose of qa testing","disable": True,"encryption": "NONE","port": 390,"use_mgmt_port": True,"version": "V1"}}
		status,response = ib_NIOS.wapi_request('POST',object_type="ldap_auth_service",params="?_function=check_ldap_server_settings",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for version',response)
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=7)
	def test_7_version_check_ldap_server_settings_FC_LDAP_Auth_Service(self):
		logging.info("Test required field wih check_ldap_server_settings function call in LDAP auth Service object")
		data = {"ldap_server": {"address": "10.39.39.150","authentication_type": "AUTHENTICATED","base_dn": "o=edirectory","bind_user_dn": "cn=Admin,o=edirectory","bind_password": "infoblox","comment": "for the purpose of qa testing","disable": False,"encryption": "NONE","use_mgmt_port": False,"version": "V3"}}
		status,response = ib_NIOS.wapi_request('POST',object_type="ldap_auth_service",params="?_function=check_ldap_server_settings",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Required field missing: port',response)
		logging.info("Test Case 7 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=8)
	def test_8_conection_time_out_check_ldap_server_settings_FC_LDAP_Auth_Service(self):
		logging.info("Test required field wih check_ldap_server_settings function call in LDAP auth Service object")
		data = {"ldap_server": {"address": "10.39.40.150","authentication_type": "AUTHENTICATED","base_dn": "o=edirectory","bind_user_dn": "cn=Admin,o=edirectory","bind_password": "infoblox","comment": "for the purpose of qa testing","disable": False,"encryption": "NONE","port": 390,"use_mgmt_port": False,"version": "V3"}}
		response = ib_NIOS.wapi_request('POST',object_type="ldap_auth_service",params="?_function=check_ldap_server_settings",fields=json.dumps(data))
		print response
		logging.info(response)
		read = re.search(r'200',response)
		for read in response:
			assert True
		logging.info("Test Case 8 Execution Completed")
		logging.info("============================")

        @pytest.mark.run(order=9)
        def test_9_error_message_check_ldap_server_settings_FC_LDAP_Auth_Service(self):
                logging.info("Test required field wih check_ldap_server_settings function call in LDAP auth Service object")
                data = {"ldap_server": {"address": "10.39.39.150","authentication_type": "AUTHENTICATED","base_dn": "o=edirectory","bind_user_dn": "cn=Admin,o=edirectory","bind_password": "infoblox","comment": "for the purpose of qa testing","disable": True,"encryption": "SSL","port": 636,"use_mgmt_port": True,"version": "V3"}}
                response = ib_NIOS.wapi_request('POST',object_type="ldap_auth_service",params="?_function=check_ldap_server_settings",fields=json.dumps(data))
                print response
                logging.info(response)
                read = re.search(r'200',response)
                for read in response:
                        assert True
                logging.info("Test Case 9 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=10)
	def test_10_authentication_type_check_ldap_server_settings_FC_LDAP_Auth_Service(self):
		logging.info("Test required field wih check_ldap_server_settings function call in LDAP auth Service object")
		data = {"ldap_server": {"address": "10.39.39.150","authentication_type": "AUTHENTICATED","base_dn": "o=edirectory","bind_password": "infoblox","comment": "for the purpose of qa testing","disable": False,"encryption": "NONE","port": 390,"use_mgmt_port": False,"version": "V3"}}
		status,response = ib_NIOS.wapi_request('POST',object_type="ldap_auth_service",params="?_function=check_ldap_server_settings",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: You must specify bind_user_dn when authentication type is set to',response)
		logging.info("Test Case 10 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=11)
        def test_11_DELETE_On_check_ldap_server_settings_FC_LDAP_Auth_Service(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ldap_auth_service")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test DELETE On check_ldap_server_settings function call in LDAP auth Service object")
                response = ib_NIOS.wapi_request('DELETE',object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 11 Execution Completed")
                logging.info("============================")

        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

