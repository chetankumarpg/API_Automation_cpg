import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS


class radius_Server(unittest.TestCase):

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

	#Test to verifying servers field in radius servers 
	@pytest.mark.run(order=2)
	def test_2_servers_radius_server(self):
		logging.info("Test the servers fileld in radius:server object")
		data = {"servers": "10.35.39.39"}
		servers = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(servers)
		res = json.loads(servers)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=3)
	#Testing requried field for creation of radius server
	def test_3_Req_Fields_1_Create_Radius_server(self):
		logging.info("Test that address field is required on creation of radius:server struct.")
		data = {"name": "admin","comment" : "QA_Testing","servers": [{"shared_secret":"hello"}]}
		status,response = ib_NIOS.wapi_request('POST', object_type="radius:authservice", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Required field missing: address',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=4)
	#Testing requried field for creation of radius server
	def test_4_Req_Fields_2_Create_Radius_server(self):
		logging.info("Test that name field is required on creation of radius:server struct.")
		data = {"servers": [{"addresss" : "10.39.39.45","shared_secret":"hello"}]}
		status,response = ib_NIOS.wapi_request('POST', object_type="radius:authservice", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: field for create missing: name',response)
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=5)
	#Test default value of acct_port
	def test_5_default_value_of_acct_port_Radius_Server(self):
		logging.info("Test the default value of  acct_port fileld in radius:authservice object")
		data = {"acct_port": 1000}
		acct_port = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(acct_port)
		res = json.loads(acct_port)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=6)
	#Updating acct_port in radius servers
	def test_6_Update_acct_port_1_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the acct_type field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","acct_port": 1810}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		acct_port = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(acct_port)
		res = json.loads(acct_port)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1810,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")
		
		
		
	@pytest.mark.run(order=7)
	#Updating acct_port in radius servers
	def test_7_Update_acct_port_2_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the acct_type field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","acct_port": 1813}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		acct_port = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(acct_port)
		res = json.loads(acct_port)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 7 Execution Completed")
		logging.info("============================")
	
		
		
		
	@pytest.mark.run(order=8)
	#Test data type of acct_port
	def test_8_Datatype_of_acct_port_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Testing the value type of acct_port in radius:authservice")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret":"hello","acct_port": True}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		address = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(response)
		res = json.loads(response)
		print res
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for acct_port: true: Must be integer type',response)
		logging.info("Test Case 8 Execution Completed")
		logging.info("============================")

		
		
	@pytest.mark.run(order=9)
	#Updating address in radius servers
	def test_9_Update_address_1_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the acct_type field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.40","shared_secret": "test"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		address = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(address)
		res = json.loads(address)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.40","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 9 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=10)
	#Updating address in radius servers
	def test_10_Update_address_2_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the acct_type field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		address = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(address)
		res = json.loads(address)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 10 Execution Completed")
		logging.info("============================")




	@pytest.mark.run(order=11)
	#Test data type of address
	def test_11_Datatype_of_address_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Testing the value type of address in radius:authservice")
		data ={"name": "admin","servers": [{"address": True,"shared_secret":"hello"}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		address = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(response)
		res = json.loads(response)
		print res
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for address: true: Must be string type',response)
		logging.info("Test Case 11 Execution Completed")
		logging.info("============================")

		
		
		
	@pytest.mark.run(order=12)
	#Updating auth_port in radius servers
	def test_12_Update_auth_port_1_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the acct_type field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","auth_port": 100}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		auth_port = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(auth_port)
		res = json.loads(auth_port)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 100,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 12 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=13)
	#Updating auth_port in radius servers
	def test_13_Update_auth_port_2_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the acct_type field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","auth_port": 1812}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		auth_port = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(auth_port)
		res = json.loads(auth_port)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 13 Execution Completed")
		logging.info("============================")




	@pytest.mark.run(order=14)
	#Test data type of auth_port
	def test_14_Datatype_of_auth_port_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Testing the value type of auth_port in radius:authservice")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret":"hello","auth_port": True}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		auth_port = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(response)
		res = json.loads(response)
		print res
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for auth_port: true: Must be integer type',response)
		logging.info("Test Case 14 Execution Completed")
		logging.info("============================")

		

	@pytest.mark.run(order=15)
	#Test default value of auth_type
	def test_15_default_value_of_auth_type_Radius_Server(self):
		logging.info("Test the default value of  auth_type fileld in radius:authservice object")
		data = {"auth_type": "PAP"}
		auth_type = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(auth_type)
		res = json.loads(auth_type)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 15 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=16)
	#Updating auth_type in radius servers
	def test_16_Update_auth_type_1_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the auth_type field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","auth_type": "CHAP"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		auth_type = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(auth_type)
		res = json.loads(auth_type)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "CHAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 16 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=17)
	#Updating auth_type in radius servers
	def test_17_Update_auth_type_2_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the auth_type field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","auth_port": 1812}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		auth_type = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(auth_type)
		res = json.loads(auth_type)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 17 Execution Completed")
		logging.info("============================")

		

	@pytest.mark.run(order=18)
	#Test data type of auth_type
	def test_18_Datatype_of_auth_type_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Testing the value type of auth_port in radius:authservice")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret":"hello","auth_type": True}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		auth_type = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(response)
		res = json.loads(response)
		print res
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for auth_type ',response)
		logging.info("Test Case 18 Execution Completed")
		logging.info("============================")

		
	@pytest.mark.run(order=19)
	#Updating comment in radius servers
	def test_19_Update_comment_1_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the comment field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","comment": "QA_Testing"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		comment = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(comment)
		res = json.loads(comment)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False,"comment": "QA_Testing"}]
		logging.info("Test Case 19 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=20)
	#Test data type of comment
	def test_20_Datatype_of_comment_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Testing the value type of comment in radius:authservice")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret":"hello","comment": True}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		comment = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(response)
		res = json.loads(response)
		print res
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for comment: true: Must be string type',response)
		logging.info("Test Case 20 Execution Completed")
		logging.info("============================")

		
		
		
		
	@pytest.mark.run(order=21)
	#Test default value of disable
	def test_21_default_value_of_disable_Radius_Server(self):
		logging.info("Test the default value of  disable fileld in radius:authservice object")
		data = {"disable": "PAP"}
		disable = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(disable)
		res = json.loads(disable)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False,"comment": "QA_Testing"}]
		logging.info("Test Case 21 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=22)
	#Updating disable in radius servers
	def test_22_Update_disable_1_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the disable field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","disable": True}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		disable = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(disable)
		res = json.loads(disable)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": True,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 22 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=23)
	#Updating disable in radius servers
	def test_23_Update_disable_2_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the disable field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","disable": False}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		disable = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(disable)
		res = json.loads(disable)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 23 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=24)
	#Test data type of disable
	def test_24_Datatype_of_disable_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Testing the value type of auth_port in radius:authservice")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret":"hello","disable": "yes"}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		disable = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(response)
		res = json.loads(response)
		print res
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for disable: ',response)
		logging.info("Test Case 24 Execution Completed")
		logging.info("============================")

		
		
	@pytest.mark.run(order=25)
	def test_25_Shared_Secret_1_Radius_server(self):
		logging.info("Test the Shared_Secret field in radius:server struct")
		data = {"name": "admin","servers": [{"address": " 10.39.39.45"}]}
		status,response = ib_NIOS.wapi_request('POST', object_type="radius:authservice", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Required field missing: shared_secret',response)
		logging.info("Test Case 25 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=26)
	def test_26_Shared_Secret_2_Radius_server(self):
		logging.info("Test the Shared_Secret field in radius:server struct")
		data = {"name": "infoblox","servers": [{"address": "10.39.39.40","shared_secret": True}]}
		status,response = ib_NIOS.wapi_request('POST', object_type="radius:authservice", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for shared_secret: true: Must be string type',response)
		logging.info("Test Case 26 Execution Completed")
		logging.info("============================")
	
		
		
		
	@pytest.mark.run(order=27)
	#Test default value of use_accounting
	def test_27_default_value_of_use_accounting_Radius_Server(self):
		logging.info("Test the default value of  use_accounting fileld in radius:authservice object")
		data = {"use_accounting": "PAP"}
		use_accounting = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(use_accounting)
		res = json.loads(use_accounting)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 27 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=28)
	#Updating use_accounting in radius servers
	def test_28_Update_use_accounting_1_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the use_accounting field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","use_accounting": False}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_accounting = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(use_accounting)
		res = json.loads(use_accounting)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": False,"use_mgmt_port": False}]
		logging.info("Test Case 28 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=29)
	#Updating use_accounting in radius servers
	def test_29_Update_use_accounting_2_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the use_accounting field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","use_accounting": True}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_accounting = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(use_accounting)
		res = json.loads(use_accounting)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 29 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=30)
	#Test data type of use_accounting
	def test_30_Datatype_of_use_accounting_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Testing the value type of auth_port in radius:authservice")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret":"hello","use_accounting": "yes"}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_accounting = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(response)
		res = json.loads(response)
		print res
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for use_accounting: ',response)
		logging.info("Test Case 30 Execution Completed")
		logging.info("============================")

		
	@pytest.mark.run(order=31)
	#Test default value of use_mgmt_port
	def test_31_default_value_of_use_mgmt_port_Radius_Server(self):
		logging.info("Test the default value of  use_mgmt_port fileld in radius:authservice object")
		data = {"use_mgmt_port": "PAP"}
		use_mgmt_port = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(use_mgmt_port)
		res = json.loads(use_mgmt_port)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 31 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=32)
	#Updating use_mgmt_port in radius servers
	def test_32_Update_use_mgmt_port_1_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the use_mgmt_port field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","use_mgmt_port": True}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_mgmt_port = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(use_mgmt_port)
		res = json.loads(use_mgmt_port)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": True}]
		logging.info("Test Case 32 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=33)
	#Updating use_mgmt_port in radius servers
	def test_33_Update_use_mgmt_port_2_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the use_mgmt_port field in radius:server structure")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret": "test","use_mgmt_port": False}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_mgmt_port = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(use_mgmt_port)
		res = json.loads(use_mgmt_port)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 33 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=34)
	#Test data type of use_mgmt_port
	def test_34_Datatype_of_use_mgmt_port_Radius_Server(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Testing the value type of auth_port in radius:authservice")
		data ={"name": "admin","servers": [{"address": "10.39.39.45","shared_secret":"hello","use_mgmt_port": "yes"}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_mgmt_port = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(response)
		res = json.loads(response)
		print res
		assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for use_mgmt_port: ',response)
		logging.info("Test Case 34 Execution Completed")
		logging.info("============================")
	
		
	@pytest.mark.run(order=35)
	def test_35_DELETE_Radius_Server(self):
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
		logging.info("Test Case 35 Execution Completed")
		logging.info("=============================")
		
		
		
		
		
		
		
		
		
		

