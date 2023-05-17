import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS


class Radius_Authservice(unittest.TestCase):

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
	def test_1_Create_Radius_Authservice(self):
		logging.info("Create A new radius Authservice")
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
	def test_2_Format_Radius_Authservice(self):
        	logging.info("Test the format of radius:authservice object")
        	get_radius = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
        	logging.info(get_radius)
        	res = json.loads(get_radius)
        	print res
        	for i in res:
        		print i
            		logging.info("found")
            		assert i["name"] == "admin" and i["comment"] == "QA_Testing"
        	logging.info("Test Case 2 Execution Completed")
        	logging.info("============================")

	@pytest.mark.run(order=3)
	def test_3_Schedule_Radius_Authservice(self):
        	logging.info("Perform schedule operation for radius:authservice")
        	status,response = ib_NIOS.wapi_request('POST', object_type="radius:authservice",params="?_schedinfo.scheduled_time=1924223800")
        	print status
        	print response
        	logging.info(response)
        	assert  status == 400 and re.search(r'(IBDataConflictError: IB.Data.Conflict:radius:authservice does not support scheduling.)',response)
        	logging.info("Test Case 3 Execution Completed")
        	logging.info("============================")

		
	@pytest.mark.run(order=4)
	def test_4_Csv_Export_Radius_Authservice(self):
		logging.info("Test the restriction for the radius:authservice object - CSV Export")
		data = {"_object":"radius:authservice"}
		status,response = ib_NIOS.wapi_request('POST', object_type="radius:authservice",params="?_function=csv_export",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Function csv_export is not valid for this object',response)
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")
		
	@pytest.mark.run(order=5)
	def test_5_return_fields_Radius_Authservice(self):
		logging.info("Test the _return_fields for default values in radius:authservice object")
		get_return_fields = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_return_fields)
		res = json.loads(get_return_fields)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["comment"] == "QA_Testing" and i["disable"] == False and i["name"] == "admin"
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=6)
	def test_6_Req_Fields_1_Create_Radius_Authservice(self):
		logging.info("Test the fields are required to create this object -1")
		data = {"comment" : "QA_Testing","servers": [{"address": "10.39.39.45","shared_secret":"hello"}]}
		status,response = ib_NIOS.wapi_request('POST', object_type="radius:authservice", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: field for create missing: name',response)
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=7)
	def test_7_Req_Fields_2_Create_Radius_Authservice(self):
		logging.info("Test the fields are required to create this object -2")
		data = {"name" : "admin","comment" : "QA_Testing"}
		status,response = ib_NIOS.wapi_request('POST', object_type="radius:authservice", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: field for create missing: servers',response)
		logging.info("Test Case 7 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=8)
	def test_8_acct_retries_Radius_Authservice(self):
		logging.info("Test the acct_retries fileld in radius:authservice object")
		data = {"acct_retries": 1000}
		acct_retries = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=acct_retries")
		logging.info(acct_retries)
		res = json.loads(acct_retries)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["acct_retries"] == 1000
		logging.info("Test Case 8 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=9)
	def test_9_Serach_acct_Retries_exact_equality(self):
		logging.info("perform Search with =  for acct_retries field in radius:authservice ")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?acct_retries=1000")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: acct_retries',response)
		logging.info("Test Case 9 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=10)
	def test_10_Serach_acct_Retries_case_insensitive(self):
		logging.info("perform Search with :=  for acct_retries field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?acct_retries:=1000")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: acct_retries',response)
		logging.info("Test Case 10 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=11)
	def test_11_Serach_acct_Retries_case_regular_expression(self):
		logging.info("perform Search with ~=  for acct_retries field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?acct_retries~=1000")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: acct_retries',response)
		logging.info("Test Case 11 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=12)
	def test_12_acct_timeout_Radius_Authservice(self):
		logging.info("Test the acct_timeout fileld in radius:authservice object")
		data = {"acct_timeout": 5000}
		acct_timeout = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=acct_timeout")
		logging.info(acct_timeout)
		res = json.loads(acct_timeout)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["acct_timeout"] == 5000
		logging.info("Test Case 12 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=13)
	def test_13_Serach_acct_timeout_exact_equality(self):
		logging.info("perform Search with =  for acct_timeout field in radius:authservice ")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?acct_timeout=5000")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: acct_timeout',response)
		logging.info("Test Case 13 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=14)
	def test_14_Serach_acct_timeout_case_insensitive(self):
		logging.info("perform Search with :=  for acct_timeout field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?acct_timeout:=5000")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: acct_timeout',response)
		logging.info("Test Case 14 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=15)
	def test_15_Serach_acct_timeout_case_regular_expression(self):
		logging.info("perform Search with ~=  for acct_timeout field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?acct_timeout~=5000")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: acct_timeout',response)
		logging.info("Test Case 15 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=16)
	def test_16_auth_retries_Radius_Authservice(self):
		logging.info("Test the auth_retries fileld in radius:authservice object")
		data = {"auth_retries": 6}
		auth_retries = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=auth_retries")
		logging.info(auth_retries)
		res = json.loads(auth_retries)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["auth_retries"] == 6
		logging.info("Test Case 16 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=17)
	def test_17_Serach_auth_Retries_exact_equality(self):
		logging.info("perform Search with =  for auth_retries field in radius:authservice ")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?auth_retries=6")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: auth_retries',response)
		logging.info("Test Case 17 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=18)
	def test_18_Serach_auth_Retries_case_insensitive(self):
		logging.info("perform Search with :=  for auth_retries field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?auth_retries:=6")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: auth_retries',response)
		logging.info("Test Case 18 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=19)
	def test_19_Serach_auth_Retries_case_regular_expression(self):
		logging.info("perform Search with ~=  for auth_retries field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?auth_retries~=6")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: auth_retries',response)
		logging.info("Test Case 19 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=20)
	def test_20_auth_timeout_Radius_Authservice(self):
		logging.info("Test the auth_timeout fileld in radius:authservice object")
		data = {"auth_timeout": 5000}
		auth_timeout = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=auth_timeout")
		logging.info(auth_timeout)
		res = json.loads(auth_timeout)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["auth_timeout"] == 5000
		logging.info("Test Case 20 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=21)
	def test_21_Serach_auth_timeout_exact_equality(self):
		logging.info("perform Search with =  for auth_timeout field in radius:authservice ")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?auth_timeout=5000")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: auth_timeout',response)
		logging.info("Test Case 21 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=22)
	def test_22_Serach_auth_timeout_case_insensitive(self):
		logging.info("perform Search with :=  for auth_timeout field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?auth_timeout:=5000")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: auth_timeout',response)
		logging.info("Test Case 22 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=23)
	def test_23_Serach_auth_timeout_case_regular_expression(self):
		logging.info("perform Search with ~=  for auth_timeout field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?auth_timeout~=5000")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: auth_timeout',response)
		logging.info("Test Case 23 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=24)
	def test_24_comment_Radius_Authservice(self):
		logging.info("Test the comment fileld in radius:authservice object")
		data = {"comment": "QA_Testing"}
		comment = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=comment")
		logging.info(comment)
		res = json.loads(comment)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["comment"] == "QA_Testing"
		logging.info("Test Case 24 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=25)
	def test_25_Serach_comment_exact_equality(self):
		logging.info("perform Search with =  for comment field in radius:authservice ")
		response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?comment=QA_Testing")
		print response
		logging.info(response)
		assert re.search(r'QA_Testing',response)
		logging.info("Test Case 25 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=26)
	def test_26_Serach_comment_case_insensitive(self):
		logging.info("perform Search with :=  for comment field in radius:authservice ")
		response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?comment:=qA_testing")
		print response
		logging.info(response)
		assert re.search(r'qA_testing',response,re.I)
		logging.info("Test Case 25 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=27)
	def test_27_Serach_comment_regular_expression(self):
		logging.info("perform Search with ~=  for comment field in radius:authservice ")
		response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?comment~=QA_Tes*")
		print response
		logging.info(response)
		assert re.search(r'QA_Tes*',response)
		logging.info("Test Case 27 Execution Completed")
		logging.info("=============================")

		
		
        @pytest.mark.run(order=28)
        def test_28_disable_Radius_Authservice(self):
                logging.info("Test the disable fileld in radius:authservice object")
                data = {"disable": False}
                disable = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=disable")
                logging.info(disable)
                res = json.loads(disable)
                print res
                for i in res:
                        print i
                        logging.info("found")
                        assert i["disable"] == False
                logging.info("Test Case 28 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=29)
        def test_29_Serach_disable_exact_equality(self):
                logging.info("perform Search with =  for disable field in radius:authservice ")
                status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?disable=False")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: disable',response)
                logging.info("Test Case 29 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=30)
        def test_30_Serach_disable_case_insensitive(self):
                logging.info("perform Search with :=  for disable field in radius:authservice")
                status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?disable:=fAlse")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: disable',response)
                logging.info("Test Case 30 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=31)
        def test_31_Serach_disable_regular_expression(self):
                logging.info("perform Search with ~=  for disable field in radius:authservice")
                status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?disable~=Fal*")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: disable',response)
                logging.info("Test Case 31 Execution Completed")
                logging.info("=============================")

        @pytest.mark.run(order=32)
        def test_32_name_Radius_Authservice(self):
                logging.info("Test the name fileld in radius:authservice object")
                data = {"name": "admin"}
                name = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=name")
                logging.info(name)
                res = json.loads(name)
                print res
                for i in res:
                        print i
                        logging.info("found")
                        assert i["name"] == "admin"
                logging.info("Test Case 32 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=33)
        def test_33_Serach_name_exact_equality(self):
                logging.info("perform Search with =  for name field in radius:authservice ")
                response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?name=admin")
                print response
                logging.info(response)
                assert re.search(r'admin',response)
                logging.info("Test Case 33 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=34)
        def test_34_Serach_name_case_insensitive(self):
                logging.info("perform Search with :=  for name field in radius:authservice ")
                response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?name:=ADmin")
                print response
                logging.info(response)
                assert re.search(r'ADmin',response,re.I)
                logging.info("Test Case 34 Execution Completed")
                logging.info("=============================")

        @pytest.mark.run(order=35)
        def test_35_Serach_name_regular_expression(self):
                logging.info("perform Search with ~=  for name field in radius:authservice ")
                response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?name~=adm*")
                print response
                logging.info(response)
                assert re.search(r'adm*',response)
                logging.info("Test Case 35 Execution Completed")
                logging.info("=============================")


	@pytest.mark.run(order=36)
	def test_36_servers_Radius_Authservice(self):
		logging.info("Test the servers fileld in radius:authservice object")
		data = {"servers": "QA_Testing"}
		servers = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(servers)
		res = json.loads(servers)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.39.45","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 36 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=37)
	def test_37_Serach_servers_exact_equality(self):
		logging.info("perform Search with =  for servers field in radius:authservice ")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?servers=10.39.39.45")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: servers',response)
		logging.info("Test Case 37 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=38)
	def test_38_Serach_servers_case_insensitive(self):
		logging.info("perform Search with :=  for servers field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?servers:=10.39.39.45")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: servers',response)
		logging.info("Test Case 38 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=39)
	def test_39_Serach_servers_regular_expression(self):
		logging.info("perform Search with ~=  for servers field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?servers~=10.39.39.45")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: servers',response)
		logging.info("Test Case 39 Execution Completed")
		logging.info("=============================")



	@pytest.mark.run(order=40)
	def test_40_cache_ttl_Radius_Authservice(self):
		logging.info("Test the cache_ttl fileld in radius:authservice object")
		data = {"cache_ttl": "QA_Testing"}
		cache_ttl = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=cache_ttl")
		logging.info(cache_ttl)
		res = json.loads(cache_ttl)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["cache_ttl"] == 3600
		logging.info("Test Case 40 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=41)
	def test_41_Serach_cache_ttl_exact_equality(self):
		logging.info("perform Search with =  for cache_ttl field in radius:authservice ")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?cache_ttl=10.39.39.45")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: cache_ttl',response)
		logging.info("Test Case 41 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=42)
	def test_42_Serach_cache_ttl_case_insensitive(self):
		logging.info("perform Search with :=  for cache_ttl field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?cache_ttl:=10.39.39.45")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: cache_ttl',response)
		logging.info("Test Case 42 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=43)
	def test_43_Serach_cache_ttl_regular_expression(self):
		logging.info("perform Search with ~=  for cache_ttl field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?cache_ttl~=10.39.39.45")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: cache_ttl',response)
		logging.info("Test Case 43 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=44)
	def test_44_enable_cache_Radius_Authservice(self):
		logging.info("Test the enable_cache fileld in radius:authservice object")
		data = {"enable_cache": "QA_Testing"}
		enable_cache = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=enable_cache")
		logging.info(enable_cache)
		res = json.loads(enable_cache)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["enable_cache"] == False
		logging.info("Test Case 44 excution Completed")
		logging.info("============================")

	@pytest.mark.run(order=45)
	def test_45_Serach_enable_cache_exact_equality(self):
		logging.info("perform Search with =  for enable_cache field in radius:authservice ")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?enable_cache=false")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: enable_cache',response)
		logging.info("Test Case 45 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=46)
	def test_46_Serach_enable_cache_case_insensitive(self):
		logging.info("perform Search with :=  for enable_cache field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?enable_cache:=false")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: enable_cache',response)
		logging.info("Test Case 46 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=47)
	def test_47_Serach_enable_cache_regular_expression(self):
		logging.info("perform Search with ~=  for enable_cache field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?enable_cache~=fal*")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: enable_cache',response)
		logging.info("Test Case 47 Execution Completed")
		logging.info("=============================")


		
		
	@pytest.mark.run(order=48)
	def test_48_mode_Radius_Authservice(self):
		logging.info("Test the mode fileld in radius:authservice object")
		data = {"mode": "HUNT_GROUP"}
		mode = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=mode")
		logging.info(mode)
		res = json.loads(mode)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["mode"] == "HUNT_GROUP"
		logging.info("Test Case 48 Execution Completed")
		logging.info("============================")
				
	

	@pytest.mark.run(order=49)
	def test_49_Serach_mode_exact_equality(self):
		logging.info("perform Search with =  for mode field in radius:authservice ")
		response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?mode=HUNT_GROUP")
		print response
		logging.info(response)
		assert re.search(r'admin',response)
		logging.info("Test Case 49 Execution Completed")
		logging.info("=============================")



	@pytest.mark.run(order=50)
	def test_50_Serach_mode_case_insensitive(self):
		logging.info("perform Search with :=  for mode field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?mode:=hunt_GROUP")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Search modifier ',response)
		logging.info("Test Case 50 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=51)
	def test_51_Serach_mode_regular_expression(self):
		logging.info("perform Search with ~=  for mode field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?mode~=HUNT_GR*")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Search modifier ',response)
		logging.info("Test Case 51 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=52)
	def test_52_recovery_interval_Radius_Authservice(self):
		logging.info("Test the recovery_interval fileld in radius:authservice object")
		data = {"recovery_interval": "QA_Testing"}
		recovery_interval = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=recovery_interval")
		logging.info(recovery_interval)
		res = json.loads(recovery_interval)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["recovery_interval"] == 30
		logging.info("Test Case 52 excution Completed")
		logging.info("============================")

	@pytest.mark.run(order=53)
	def test_53_Serach_recovery_interval_exact_equality(self):
		logging.info("perform Search with =  for recovery_interval field in radius:authservice ")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?recovery_interval=30")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: recovery_interval',response)
		logging.info("Test Case 53 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=54)
	def test_54_Serach_recovery_interval_case_insensitive(self):
		logging.info("perform Search with :=  for recovery_interval field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?recovery_interval:=30")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: recovery_interval',response)
		logging.info("Test Case 54 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=55)
	def test_55_Serach_recovery_interval_regular_expression(self):
		logging.info("perform Search with ~=  for recovery_interval field in radius:authservice")
		status,response = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?recovery_interval~=30")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: recovery_interval',response)
		logging.info("Test Case 55 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=56)
	#Updating name field in radius:authservice object-1
	def test_Update_On_name_1_Radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for usage_type field in radius:authservice")
		data ={"name": "user"}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		name = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=name")
		logging.info(name)
		res = json.loads(name)
		print res
		for i in res:
			print i
			logging.info("found")
		assert i["name"] == "user"
		logging.info("Test Case 56 Execution Completed")
		logging.info("============================")
		

	@pytest.mark.run(order=57)
	#Updating servers field in radius:authservice object-1
	def test_Update_On_servers_1_Radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for usage_type field in radius:authservice")
		data ={"servers": [{"address": "10.39.38.40","shared_secret":"hello"}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		servers = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=servers")
		logging.info(servers)
		res = json.loads(servers)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["servers"] == [{"acct_port": 1813,"address": "10.39.38.40","auth_port": 1812,"auth_type": "PAP","disable": False,"use_accounting": True,"use_mgmt_port": False}]
		logging.info("Test Case 57 Execution Completed")
		logging.info("============================")
		
		
		
	@pytest.mark.run(order=58)
	#Updating mode field in radius:authservice object-1
	def test_Update_On_mode_1_Radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for usage_type field in radius:authservice") 
		data = {"mode": "ROUND_ROBIN"}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		mode = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=mode")
		logging.info(mode)
		res = json.loads(mode)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["mode"] == "ROUND_ROBIN"
		logging.info("Test Case 58 Execution Completed")
		logging.info("============================")		

		
	@pytest.mark.run(order=59)
	#Updating recovery_interval field in radius:authservice object-1
	def test_Update_On_recovery_interval_1_Radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for usage_type field in radius:authservice") 
		data = {"recovery_interval": 25}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		recovery_interval = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=recovery_interval")
		logging.info(recovery_interval)
		res = json.loads(recovery_interval)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["recovery_interval"] == 25
		logging.info("Test Case 59 Execution Completed")
		logging.info("============================")	

		
	@pytest.mark.run(order=60)
	#Updating enable_cache field in radius:authservice object-1
	def test_Update_On_enable_cache_1_Radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for usage_type field in radius:authservice") 
		data = {"enable_cache": True}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		enable_cache = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=enable_cache")
		logging.info(enable_cache)
		res = json.loads(enable_cache)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["enable_cache"] == True
		logging.info("Test Case 60 Execution Completed")
		logging.info("============================")
		
		
	@pytest.mark.run(order=61)
	#Updating disable field in radius:authservice object-1
	def test_Update_On_disable_1_Radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for usage_type field in radius:authservice") 
		data = {"disable": True}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		disable = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=disable")
		logging.info(disable)
		res = json.loads(disable)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["disable"] == True
		logging.info("Test Case 61 Execution Completed")
		logging.info("============================")
		
	@pytest.mark.run(order=62)
	#Updating cache_ttl field in radius:authservice object-1
	def test_Update_On_cache_ttl_1_Radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for usage_type field in radius:authservice") 
		data = {"cache_ttl": 3500}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		cache_ttl = ib_NIOS.wapi_request('GET',object_type="radius:authservice",params="?_return_fields=cache_ttl")
		logging.info(cache_ttl)
		res = json.loads(cache_ttl)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["cache_ttl"] == 3500
		logging.info("Test Case 62 Execution Completed")
		logging.info("============================")	
		
	@pytest.mark.run(order=63)
	def test_45_DELETE_radius_Authservice(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="radius:authservice")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref

		logging.info("Deleting the radius:authservice user")
		data ={"name": "user"}
		get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
		print get_status
		logging.info(get_status)
		logging.info("Test Case 63 Execution Completed")
		logging.info("=============================")


        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

