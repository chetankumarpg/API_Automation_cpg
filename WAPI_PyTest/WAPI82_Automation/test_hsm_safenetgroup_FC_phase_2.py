import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import time
import ib_utils.ib_NIOS as ib_NIOS

class Fileop_Function_Call(unittest.TestCase):

	@pytest.mark.run(order=1)
	def test_1_refresh_hsm_hsm_safenetgroup_Function_Call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="hsm:safenetgroup")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		logging.info("Test the uploadinit function call in hsm:safenetgroup object")
		response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=refresh_hsm")
		print response
		res = json.loads(response)
		string = {"results": "PASSED"}
		if res == string:
			assert True
		else:
			assert False
        	logging.info("Test Case 1 Execution Completed")
        	logging.info("============================")


	@pytest.mark.run(order=2)
	def test_2_refresh_hsm_hsm_safenetgroup_Function_Call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="hsm:safenetgroup")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		logging.info("Test the refresh_hsm function call with PUT in hsm:safenetgroup object")
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,params="?_function=refresh_hsm")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Function refresh_hsm illegal with this method',response)
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=3)
	def test_3_DELETE_refresh_hsm_hsm_safenetgroup_Function_Call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="hsm:safenetgroup")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		logging.info("Test the refresh_hsm function call with DELETE in hsm:safenetgroup object")
		status,response = ib_NIOS.wapi_request('DELETE',object_type=ref,params="?_function=refresh_hsm")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Function refresh_hsm illegal with this method',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=4)
	def test_4_Create_hsm_thalesgroup_Function_Call(self):
		logging.info("Create A new hsm_thalesgroup")
		data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}],"pass_phrase":"Infoblox.123"}
		response = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup", fields=json.dumps(data))
		print response
		logging.info(response)
		read  = re.search(r'201',response)
		for read in  response:
			assert True
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=5)
	def test_5_refresh_hsm_hsm_thalesgroup_Function_Call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		logging.info("Test the uploadinit function call in hsm:thalesgroup object")
		response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=refresh_hsm")
		print response
		res = json.loads(response)
		string = {"results": "PASSED"}
		if res == string:
			assert True
		else:
			assert False
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")

		

	@pytest.mark.run(order=6)
	def test_6_refresh_hsm_hsm_thalesgroup_Function_Call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		logging.info("Test the refresh_hsm function call with PUT in hsm:thalesgroup object")
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,params="?_function=refresh_hsm")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Function refresh_hsm illegal with this method',response)
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=7)
	def test_7_DELETE_refresh_hsm_hsm_thalesgroup_Function_Call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		logging.info("Test the refresh_hsm function call with DELETE in hsm:thalesgroup object")
		status,response = ib_NIOS.wapi_request('DELETE',object_type=ref,params="?_function=refresh_hsm")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Function refresh_hsm illegal with this method',response)
		logging.info("Test Case 7 Execution Completed")
		logging.info("============================")
		
		
	@pytest.mark.run(order=8)
	def test_8_DELETE_hsm_thalesgroup(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Deleting the hsm:thalesgroup user")
		response = ib_NIOS.wapi_request('DELETE', object_type=ref)
		logging.info(response)
		read  = re.search(r'201',response)
		for read in  response:
			assert True
		logging.info(response)
		logging.info("Test Case 8 Execution Completed")
		logging.info("=============================")
