import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS


class Tacacsplus_Server(unittest.TestCase):

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
	def test_1_Create_Tacacsplus_server(self):
		logging.info("Create A new Tacacsplus Server")
		data = {"name": "admin","comment" : "QA_Testing","servers": [{"address": "10.39.39.45","shared_secret":"hello"}]}
		response = ib_NIOS.wapi_request('POST', object_type="tacacsplus:authservice", fields=json.dumps(data))
		print response
		logging.info(response)
		read  = re.search(r'201',response)
		for read in  response:
			assert True
		logging.info("Test Case 1 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=2)
	def test_2_servers_Tacacsplus_server(self):
		logging.info("Test the servers fileld in tacacsplus:server object")
		data = {"servers": "QA_Testing"}
		servers = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(servers)
		res = json.loads(servers)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "CHAP","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=3)
	def test_3_Req_Fields_1_Create_Tacacsplus_server(self):
		logging.info("Test that address field is required on creation of tacacsplus:server struct.")
		data = {"name": "admin","comment" : "QA_Testing","servers": [{"shared_secret":"hello"}]}
		status,response = ib_NIOS.wapi_request('POST', object_type="tacacsplus:authservice", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Required field missing: address',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=4)
	def test_4_Create_Tacacsplus_server(self):
		logging.info("Test the address field with different values in tacacsplus:server struct")
		data = {"name": "admin","comment" : "QA_Testing","servers": [{"address": " 10.39.39.45","shared_secret":"hello"}]}
		status,response = ib_NIOS.wapi_request('POST', object_type="tacacsplus:authservice", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for address:',response)
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=5)
	#Updating address field with fqdn from IP tacacsplus:authservice object
	def test_5_Update_address_1_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for address field in tacacsplus:authservice")
		data ={"name": "admin","servers": [{"address": "asm.com","shared_secret":"hello"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		address = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(address)
		res = json.loads(address)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "asm.com","auth_type": "CHAP","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")
		
	@pytest.mark.run(order=6)
	#Updating address field with IP from fqdn tacacsplus:authservice object
	def test_6_Update_address_2_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for address field in tacacsplus:authservice")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret":"hello"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		address = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(address)
		res = json.loads(address)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "CHAP","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")	

		
	@pytest.mark.run(order=7)
	def test_7_auth_type_1_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test auth_type field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","auth_type": "ASCII"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		auth_type = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(auth_type)
		res = json.loads(auth_type)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "ASCII","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 7 Execution Completed")
		logging.info("============================")
		
	@pytest.mark.run(order=8)
	def test_8_auth_type_2_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test auth_type field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","auth_type": "PAP"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		auth_type = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(auth_type)
		res = json.loads(auth_type)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "PAP","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 8 Execution Completed")
		logging.info("============================")
		
		
	@pytest.mark.run(order=9)
	def test_9_auth_type_3_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test auth_type field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","auth_type": "CHAP"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		auth_type = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(auth_type)
		res = json.loads(auth_type)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "CHAP","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 8 Execution Completed")
		logging.info("============================")
		
		
	@pytest.mark.run(order=10)
	def test_10_comment_1_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test comment field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","comment": "For_QA_Testing"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		comment = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(comment)
		res = json.loads(comment)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","comment": "For_QA_Testing","auth_type": "CHAP","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 10 Execution Completed")
		logging.info("============================") 
		

	@pytest.mark.run(order=11)
	def test_11__comment_2_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test comment field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		comment = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(comment)
		res = json.loads(comment)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "CHAP","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 11 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=12)
	def test_12_disable_1_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test disable field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","disable": False}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		disable = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(disable)
		res = json.loads(disable)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "CHAP","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 12 Execution Completed")
		logging.info("============================")

		
	@pytest.mark.run(order=13)
	def test_13_disable_2_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test disable field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","disable": True}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		disable = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(disable)
		res = json.loads(disable)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "CHAP","disable": True,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 13 Execution Completed")
		logging.info("============================")
		


	@pytest.mark.run(order=14)
	def test_14_disable_3_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		logging.info("Test disable field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","disable": "test"}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for disable:',response)
		logging.info("Test Case 14 Execution Completed")
		logging.info("============================")

		
		
	@pytest.mark.run(order=15)
	def test_15_Port_1_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test Port field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","port": 50}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		port = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(port)
		res = json.loads(port)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "CHAP","disable": False,"port": 50,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 15 Execution Completed")
		logging.info("============================")

		
		
		
	@pytest.mark.run(order=16)
	def test_16_Port_2_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		logging.info("Test disable field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","port": "test"}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for port:',response)
		logging.info("Test Case 16 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=17)
	def test_16_Port_3_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		logging.info("Test disable field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","port": 65536}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConDataError: Value must be between 1 and 65535',response)
		logging.info("Test Case 17 Execution Completed")
		logging.info("============================")
		
		
	@pytest.mark.run(order=18)
	def test_18_Shared_Secret_1_Tacacsplus_server(self):
		logging.info("Test the Shared_Secret field in tacacsplus:server struct")
		data = {"name": "admin","servers": [{"address": " 10.39.39.45"}]}
		status,response = ib_NIOS.wapi_request('POST', object_type="tacacsplus:authservice", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Required field missing: shared_secret',response)
		logging.info("Test Case 18 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=19)
	def test_19_Shared_Secret_2_Tacacsplus_server(self):
		logging.info("Test the Shared_Secret field in tacacsplus:server struct")
		data = {"name": "admin","servers": [{"address": " 10.39.39.45","shared_secret":" test"}]}
		status,response = ib_NIOS.wapi_request('POST', object_type="tacacsplus:authservice", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for address:',response)
		logging.info("Test Case 19 Execution Completed")
		logging.info("============================")

		
		
	@pytest.mark.run(order=20)
	def test_20_use_accounting_1_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test use_accounting field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","use_accounting": True}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_accounting = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(use_accounting)
		res = json.loads(use_accounting)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "CHAP","disable": False,"port": 49,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 20 Execution Completed")
		logging.info("============================")
		

	@pytest.mark.run(order=21)
	def test_21_use_accounting_2_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test use_accounting field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","use_accounting": False}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_accounting = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(use_accounting)
		res = json.loads(use_accounting)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "CHAP","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 21 Execution Completed")
		logging.info("============================")

		
		

	@pytest.mark.run(order=22)
	def test_22_use_accounting_3_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		logging.info("Test disable field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","use_accounting": "test"}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for use_accounting:',response)
		logging.info("Test Case 22 Execution Completed")
		logging.info("============================")
		
		
	@pytest.mark.run(order=23)
	def test_23_use_mgmt_port_1_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test use_mgmt_port field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","use_mgmt_port": True}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_mgmt_port = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(use_mgmt_port)
		res = json.loads(use_mgmt_port)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "CHAP","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": True}]
		logging.info("Test Case 23 Execution Completed")
		logging.info("============================")
		
		
	@pytest.mark.run(order=24)
	def test_24_use_mgmt_port_2_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test use_mgmt_port field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","use_mgmt_port": False}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_mgmt_port = ib_NIOS.wapi_request('GET',object_type="tacacsplus:authservice",params="?_return_fields=servers")
		logging.info(use_mgmt_port)
		res = json.loads(use_mgmt_port)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"address": "10.39.39.45","auth_type": "CHAP","disable": False,"port": 49,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 24 Execution Completed")
		logging.info("============================")
		
		
	@pytest.mark.run(order=25)
	def test_25_use_mgmt_port_3_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		logging.info("Test use_mgmt_port field in tacacsplus:server")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","use_accounting": "test"}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for use_accounting:',response)
		logging.info("Test Case 25 Execution Completed")
		logging.info("============================")
		
		
	@pytest.mark.run(order=26)
	def test_26_DELETE_Tacacsplus_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="tacacsplus:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Deleting the tacacsplus:authservice admin")
		data ={"servers": "10.39.39.45"}
		get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
		print get_status
		logging.info(get_status)
		logging.info("Test Case 26 Execution Completed")
		logging.info("=============================")

        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

