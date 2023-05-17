import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class Diagnostic_Function_Call(unittest.TestCase):

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
	def test_1_diagnostic_FC_discovery_gridproperties(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:gridproperties")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the diagnostic function call in discovery:gridproperties object")
		data ={"address":"10.40.16.3","community_string":"qasnmp","force_test": False,"network_view":"default"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=diagnostic",fields=json.dumps(data))
		print response
		logging.info(response)
		assert status == 400 and re.search(r'IP address is excluded from the discovery',response)
		logging.info("Test Case 1 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=2)
	def test_2_diagnostic_FC_discovery_gridproperties(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:gridproperties")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the diagnostic function call in discovery:gridproperties object")
		data ={"community_string":"qasnmp","discovery_member": "nd.member.com","force_test": False,"network_view":"default"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=diagnostic",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: required function parameter missing: address',response)
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=3)
	def test_3_address_diagnostic_FC_discovery_gridproperties(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:gridproperties")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the address field with diagnostic function call in discovery:gridproperties object")
		data ={"address":True,"community_string":"qasnmp","discovery_member": "nd.member.com","force_test": False,"network_view":"default"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=diagnostic",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for address: true: Must be string type',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=4)
	def test_4_community_string_diagnostic_FC_discovery_gridproperties(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:gridproperties")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the community_string field with diagnostic function call in discovery:gridproperties object")
		data ={"address":"10.40.16.10","community_string":True,"discovery_member": "nd.member.com","force_test": False,"network_view":"default"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=diagnostic",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for community_string: true: Must be string type',response)
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=5)
	def test_5_discovery_member_diagnostic_FC_discovery_gridproperties(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:gridproperties")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the discovery_member field with diagnostic function call in discovery:gridproperties object")
		data ={"address":"10.40.16.10","community_string":"qasnmp","discovery_member": True,"force_test": False,"network_view":"default"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=diagnostic",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for discovery_member: true: Must be string type',response)
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=6)
	def test_6_force_test_diagnostic_FC_discovery_gridproperties(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:gridproperties")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the force_test field with diagnostic function call in discovery:gridproperties object")
		data ={"address":"10.40.16.10","community_string":"qasnmp","discovery_member": "nd.member.com","force_test": 1,"network_view":"default"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=diagnostic",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for force_test: 1: Must be boolean type',response)
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=7)
	def test_7_diagnostic_status_FC_discovery_gridproperties(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:gridproperties")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the diagnostic_status function call in discovery:gridproperties object")
		data ={"session_id": "6caf4dbb-5aaf-4a9e-90fc-8128234ba08c"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=diagnostic_status",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: required function parameter missing: start',response)
		logging.info("Test Case 7 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=8)
	def test_8_start_diagnostic_status_FC_discovery_gridproperties(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:gridproperties")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the start field with diagnostic_status function call in discovery:gridproperties object")
		data ={"session_id": "6caf4dbb-5aaf-4a9e-90fc-8128234ba08c","start":True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=diagnostic_status",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for start: true: Must be integer type',response)
		logging.info("Test Case 8 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=9)
	def test_9_diagnostic_status_FC_discovery_gridproperties(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:gridproperties")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the diagnostic_status function call in discovery:gridproperties object")
		data ={"start":True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=diagnostic_status",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: required function parameter missing: session_id',response)
		logging.info("Test Case 9 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=10)
	def test_8_session_id_diagnostic_status_FC_discovery_gridproperties(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:gridproperties")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the session_id field with diagnostic_status function call in discovery:gridproperties object")
		data ={"session_id": True,"start":1}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=diagnostic_status",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for session_id: true: Must be string type',response)
		logging.info("Test Case 8 Execution Completed")
		logging.info("============================")
