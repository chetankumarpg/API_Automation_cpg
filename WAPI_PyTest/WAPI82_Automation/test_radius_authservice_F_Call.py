import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS


class radius_Authservice_Function_Call(unittest.TestCase):


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


        #Test to creating a new radius server
        @pytest.mark.run(order=1)
        def test_1_Create_radius_server(self):
                logging.info("Create A new radius Server")
                data = {"name": "admin","comment" : "QA_Testing","servers": [{"address": "10.39.39.45","shared_secret":"hello"}]}
                response = ib_NIOS.wapi_request('POST', object_type="radius:authservice", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=2)
	def test_2_check_Radius_server_settings_FC_Tacacsplus_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the check_radius_server_settings function call in tascas:authservice object")
		data ={"acct_timeout": 5000,"auth_timeout":5000,"radius_authservice": "admin","radius_server": {"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type":"PAP","disable": False,"use_accounting": True,"use_mgmt_port": False,"shared_secret":"test"}}
		response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=check_radius_server_settings",fields=json.dumps(data))
		print response
		logging.info(response)
		res = json.loads(response)
		read  = re.search(r'200',response)
		for read in  response:
			assert True
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")


		
		
	@pytest.mark.run(order=3)
	def test_3_radius_server_check_radius_server_settings_FC_radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test radius_server field in check_radius_server_settings function call of radius:authservice object")
		data ={"acct_timeout": 5000,"auth_timeout":5000,"radius_authservice": "admin"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=check_radius_server_settings",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: required function parameter missing: radius_server',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")

		


	@pytest.mark.run(order=4)
	def test_4_radius_server_check_radius_server_settings_FC_radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test radius_server field in check_radius_server_settings function call of radius:authservice object")
		data ={"acct_timeout": 4000,"auth_timeout":5000,"radius_authservice": "admin","radius_server": {"address": "10.35.20.23","auth_type": "CHAP","disable":False,"port": 49,"use_accounting": True,"use_mgmt_port": False,"shared_secret":"test"}}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,params="?_function=check_radius_server_settings",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Function check_radius_server_settings illegal with this method',response)
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=5)
	def test_5_Address_1_check_radius_server_settings_FC_radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test Address field in check_radius_server_settings function call of radius:authservice object")
		data ={"acct_timeout": 4000,"auth_timeout":5000,"radius_authservice": "admin","radius_server": {"auth_type": "CHAP","disable":False,"port": 49,"use_accounting": True,"use_mgmt_port": False,"shared_secret":"test"}}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=check_radius_server_settings",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Required field missing: address',response)
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")
		
		
		
	@pytest.mark.run(order=6)
	def test_6_Address_2_check_radius_server_settings_FC_radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test Address field type in check_radius_server_settings function call of radius:authservice object")
		data ={"acct_timeout": 4000,"auth_timeout":5000,"radius_authservice": "admin","radius_server": {"address": True,"auth_type": "CHAP","disable":False,"port": 49,"use_accounting": True,"use_mgmt_port": False,"shared_secret":"test"}}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=check_radius_server_settings",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for address: true: Must be string type',response)
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")
		

		
	@pytest.mark.run(order=7)
	def test_7_Shared_Secret_1_check_radius_server_settings_FC_radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test shared_secret field in check_radius_server_settings function call of radius:authservice object")
		data ={"acct_timeout": 4000,"auth_timeout":5000,"radius_authservice": "admin","radius_server": {"address": "10.35.20.23","auth_type": "CHAP","disable":False,"port": 49,"use_accounting": True,"use_mgmt_port": False}}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=check_radius_server_settings",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Required field missing: shared_secret',response)
		logging.info("Test Case 7 Execution Completed")
		logging.info("============================")
		
		


	@pytest.mark.run(order=8)
	def test_8_Shared_Secret_2_check_radius_server_settings_FC_radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test shared_secret field type  in check_radius_server_settings function call of radius:authservice object")
		data ={"acct_timeout": 4000,"auth_timeout":5000,"radius_authservice": "admin","radius_server": {"address": "10.35.20.23","auth_type": "CHAP","disable":False,"port": 49,"use_accounting": True,"use_mgmt_port": False,"shared_secret":True}}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=check_radius_server_settings",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for shared_secret: true: Must be string type',response)
		logging.info("Test Case 8 Execution Completed")
		logging.info("============================")
		
		
	
		
	@pytest.mark.run(order=9)
	def test_9_DELETE_check_FC_radius_server_settings_radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref

		logging.info("Deleting the radius:authservice user")
		status,get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,params="?_function=check_radius_server_settings")
		print get_status
		print status
		logging.info(get_status)
		assert status == 400 and re.search(r'AdmConProtoError: Function check_radius_server_settings illegal with this method',get_status)
		logging.info("Test Case 9 Execution Completed")
		logging.info("=============================")


        @pytest.mark.run(order=10)
        def test_10_DELETE_Radius_Server(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Deleting the radius:authservice admin")
                data ={"servers": "10.39.39.45"}
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
                print get_status
                logging.info(get_status)
                logging.info("Test Case 10 Execution Completed")
                logging.info("=============================")


        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

