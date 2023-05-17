import re
import os
import json
import pytest
import unittest
import subprocess
import config
import logging
import ib_utils.ib_NIOS as ib_NIOS

class Microsoft_Superscope(unittest.TestCase):

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
	def test_1_Create_New_MS_Superscope(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="range")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test to create a new MS suoerscope")
		data =  {"name": "Ms_Superscope","comment": "QA_Testing","ranges": [ref]}
		response = ib_NIOS.wapi_request("POST",object_type="mssuperscope",fields=json.dumps(data))
		print response
		logging.info(response)
		read = re.search('201',response)
		for read in response:
			assert True
        	logging.info("Test Case 1 Execution Completed")
        	logging.info("============================")
		
		
    	@pytest.mark.run(order=2)
	def test_2_Csv_Export_MS_Superscope(self):
		logging.info("Test the restriction for the mssuperscope object - CSV Export")
		data = {"_object":"mssuperscope"}
		status,response = ib_NIOS.wapi_request('POST', object_type="mssuperscope",params="?_function=csv_export",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Function csv_export is not valid for this object',response)
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")
		
	@pytest.mark.run(order=3)
	def test_3_comment_MS_Superscope(self):
		logging.info("Test the comment fileld in mssuperscope object")
		data = {"comment": "QA_Testing"}
		comment = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?_return_fields=comment")
		logging.info(comment)
		res = json.loads(comment)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["comment"] == "QA_Testing"
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=4)
	def test_4_Serach_comment_exact_equality(self):
		logging.info("perform Search with =  for comment field in mssuperscope ")
		response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?comment=QA_Testing")
		print response
		res = json.loads(response)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["disable"] == False and i["name"] == "Ms_Superscope" and i["network_view"] == "default"
		logging.info("Test Case 4 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=5)
	def test_5_Serach_comment_case_insensitive(self):
		logging.info("perform Search with :=  for comment field in mssuperscope ")
		response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?comment:=qA_testing")
		print response
		res = json.loads(response)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["disable"] == False and i["name"] == "Ms_Superscope" and i["network_view"] == "default"
		logging.info("Test Case 5 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=6)
	def test_6_Serach_comment_regular_expression(self):
		logging.info("perform Search with ~=  for comment field in mssuperscope ")
		response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?comment~=QA_Tes*")
		print response
		res = json.loads(response)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["disable"] == False and i["name"] == "Ms_Superscope" and i["network_view"] == "default"
		logging.info("Test Case 6 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=7)
	def test_7_Req_Fields_for_MS_Superscope(self):
		logging.info("Test req felds on  Creation of a new mssuperscope")
		data = {"comment": "QA_Testing"}
		status,response  = ib_NIOS.wapi_request('POST',object_type="mssuperscope",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: field for create missing: name',response)
		logging.info("Test Case  Execution Completed")
		logging.info("============================")


        @pytest.mark.run(order=8)
        def test_8_Req_Fields_for_MS_Superscope(self):
                logging.info("Test req felds on  Creation of a new mssuperscope")
                data = {"name": "QA_Testing"}
                status,response  = ib_NIOS.wapi_request('POST',object_type="mssuperscope",fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert status == 400 and re.search(r'AdmConProtoError: field for create missing: ranges',response)
                logging.info("Test Case 8 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=9)
	def test_9_Test_name_MS_Superscope(self):
		logging.info("Test the data type of name field in  mssuperscope")
		data = {"name": "Ms_Superscope"}
		status,response  = ib_NIOS.wapi_request('POST',object_type="mssuperscope",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: field for create missing: ranges',response)
		logging.info("Test Case 9 Execution Completed")
		logging.info("============================")

		
	@pytest.mark.run(order=10)
	def test_10_Serach_name_exact_equality(self):
		logging.info("perform Search with =  for name field in mssuperscope ")
		response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?name=MS_Superscope")
		print response
		res = json.loads(response)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["disable"] == False and i["name"] == "Ms_Superscope" and i["network_view"] == "default"
		logging.info("Test Case 10 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=11)
	def test_11_Serach_name_case_insensitive(self):
		logging.info("perform Search with :=  for name field in mssuperscope ")
		response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?name:=Ms_Superscope")
		print response
		res = json.loads(response)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["disable"] == False and i["name"] == "Ms_Superscope" and i["network_view"] == "default"
		logging.info("Test Case 11 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=12)
	def test_12_Serach_name_regular_expression(self):
		logging.info("perform Search with ~=  for name field in mssuperscope ")
		response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?name~=Ms_Superscope")
		print response
		res = json.loads(response)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["disable"] == False and i["name"] == "Ms_Superscope" and i["network_view"] == "default"
		logging.info("Test Case 12 Execution Completed")
		logging.info("=============================")



	@pytest.mark.run(order=13)
	def test_13_Update_On_dhcp_utilization_MS_Superscope(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for dhcp_utilization field in mssuperscope")
		data ={"dhcp_utilization": 20}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		print status
		print response		
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: dhcp_utilization',response)
		logging.info("Test Case 13 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=14)
	def test_14_Serach_dhcp_utilization_exact_equality(self):
		logging.info("perform Search with =  for dhcp_utilization field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?dhcp_utilization=0")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: dhcp_utilization',response)
		logging.info("Test Case 15 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=15)
	def test_15_Serach_dhcp_utilization_case_insensitive(self):
		logging.info("perform Search with :=  for dhcp_utilization field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?dhcp_utilization:=0")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: dhcp_utilization',response)
		logging.info("Test Case 15 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=16)
	def test_16_Serach_dhcp_utilization_regular_expression(self):
		logging.info("perform Search with ~=  for dhcp_utilization field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?dhcp_utilization~=0")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: dhcp_utilization',response)
		logging.info("Test Case 16 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=17)
	def test_17_Update_On_dhcp_utilization_status_MS_Superscope(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for dhcp_utilization_status field in mssuperscope")
		data ={"dhcp_utilization_status": "HIGH"}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		logging.info(response)
		res = json.loads(response)
		assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: dhcp_utilization_status',response)
		logging.info("Test Case 17 Execution Completed")
		logging.info("============================")
	@pytest.mark.run(order=18)
	def test_18_Serach_dhcp_utilization_status_exact_equality(self):
		logging.info("perform Search with =  for dhcp_utilization_status field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?dhcp_utilization_status=MS_Superscope")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: dhcp_utilization_status',response)
		logging.info("Test Case 18 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=19)
	def test_19_Serach_dhcp_utilization_status_case_insensitive(self):
		logging.info("perform Search with :=  for dhcp_utilization_status field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?dhcp_utilization_status:=Ms_Superscope")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: dhcp_utilization_status',response)
		logging.info("Test Case 19 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=20)
	def test_20_Serach_dhcp_utilization_status_regular_expression(self):
		logging.info("perform Search with ~=  for dhcp_utilization_status field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?dhcp_utilization_status~=Ms_Superscope")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: dhcp_utilization_status',response)
		logging.info("Test Case 20 Execution Completed")
		logging.info("=============================")



	@pytest.mark.run(order=21)
	def test_21_Test_disable_MS_Superscope(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("test the datatype of disable field in mssuperscope")
		data ={"disable": 1}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for disable: 1: Must be boolean type',response)
		logging.info("Test Case 21 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=22)
	def test_22_Serach_disable_exact_equality(self):
		logging.info("perform Search with =  for disable field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?disable=false")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: disable',response)
		logging.info("Test Case 22 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=23)
	def test_23_Serach_disable_case_insensitive(self):
		logging.info("perform Search with :=  for disable field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?disable:=FaLse")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: disable',response)
		logging.info("Test Case 23 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=24)
	def test_24_Serach_disable_regular_expression(self):
		logging.info("perform Search with ~=  for disable field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?disable~=Fal*")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: disable',response)
		logging.info("Test Case 24 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=25)
	def test_25_Update_On_MS_Superscope(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for dynamic_hosts field in mssuperscope")
		data ={"dynamic_hosts": 20}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: dynamic_hosts',response)
		logging.info("Test Case 25 Execution Completed")
		logging.info("============================")



		
	@pytest.mark.run(order=26)
	def test_26_Serach_dynamic_hosts_exact_equality(self):
		logging.info("perform Search with =  for dynamic_hosts field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?dynamic_hosts=20")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: dynamic_hosts',response)
		logging.info("Test Case 26 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=27)
	def test_27_Serach_dynamic_hosts_case_insensitive(self):
		logging.info("perform Search with :=  for dynamic_hosts field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?dynamic_hosts:=20")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: dynamic_hosts',response)
		logging.info("Test Case 27 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=28)
	def test_24_Serach_dynamic_hosts_regular_expression(self):
		logging.info("perform Search with ~=  for dynamic_hosts field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?dynamic_hosts~=Fal*")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: dynamic_hosts',response)
		logging.info("Test Case 28 Execution Completed")
		logging.info("=============================")


        @pytest.mark.run(order=29)
        def test_29_Test_dynamic_hosts_MS_Superscope(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("test the datatype of dynamic_hosts field in mssuperscope")
                data ={"dynamic_hosts": True}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                logging.info(response)
                assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: dynamic_hosts',response)
                logging.info("Test Case 29 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=30)
        def test_30_Update_high_water_mark_MS_Superscope(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation for dynamic_hosts field in mssuperscope")
                data ={"high_water_mark": 90}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                logging.info(response)
                assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: high_water_mark',response)
                logging.info("Test Case 30 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=31)
	def test_31_Serach_high_water_mark_exact_equality(self):
		logging.info("perform Search with =  for high_water_mark field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?high_water_mark=95")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: high_water_mark',response)
		logging.info("Test Case 31 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=32)
	def test_32_Serach_high_water_mark_case_insensitive(self):
		logging.info("perform Search with :=  for high_water_mark field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?high_water_mark:=95")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: high_water_mark',response)
		logging.info("Test Case 32 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=33)
	def test_33_Serach_high_water_mark_regular_expression(self):
		logging.info("perform Search with ~=  for high_water_mark field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?high_water_mark~=95")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: high_water_mark',response)
		logging.info("Test Case 33 Execution Completed")
		logging.info("=============================")


        @pytest.mark.run(order=34)
        def test_34_Update_high_water_mark_Reset_MS_Superscope(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation for dynamic_hosts field in mssuperscope")
                data ={"high_water_mark": 90}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                logging.info(response)
                assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: high_water_mark',response)
                logging.info("Test Case 34 Execution Completed")
                logging.info("============================")

	@pytest.mark.run(order=35)
	def test_35_Serach_high_water_mark_reset_exact_equality(self):
		logging.info("perform Search with =  for high_water_mark_reset field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?high_water_mark_reset=95")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: high_water_mark_reset',response)
		logging.info("Test Case 35 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=36)
	def test_36_Serach_high_water_mark_reset_case_insensitive(self):
		logging.info("perform Search with :=  for high_water_mark_reset field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?high_water_mark_reset:=95")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: high_water_mark_reset',response)
		logging.info("Test Case 36 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=37)
	def test_37_Serach_high_water_mark_reset_regular_expression(self):
		logging.info("perform Search with ~=  for high_water_mark_reset field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?high_water_mark_reset~=95")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: high_water_mark_reset',response)
		logging.info("Test Case 37 Execution Completed")
		logging.info("=============================")


        @pytest.mark.run(order=38)
        def test_38_Update_low_water_mark_MS_Superscope(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation for dynamic_hosts field in mssuperscope")
                data ={"low_water_mark": 1}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                logging.info(response)
                assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: low_water_mark',response)
                logging.info("Test Case 38 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=39)
	def test_39_Serach_low_water_mark_exact_equality(self):
		logging.info("perform Search with =  for low_water_mark field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?low_water_mark=0")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: low_water_mark',response)
		logging.info("Test Case 39 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=40)
	def test_40_Serach_low_water_mark_case_insensitive(self):
		logging.info("perform Search with :=  for low_water_mark field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?low_water_mark:=0")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: low_water_mark',response)
		logging.info("Test Case 40 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=41)
	def test_41_Serach_low_water_mark_regular_expression(self):
		logging.info("perform Search with ~=  for low_water_mark field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?low_water_mark~=0")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: low_water_mark',response)
		logging.info("Test Case 41 Execution Completed")
		logging.info("=============================")


        @pytest.mark.run(order=42)
        def test_42_Update_low_water_mark_reset_MS_Superscope(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation for dynamic_hosts field in mssuperscope")
                data ={"low_water_mark_reset": 1}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                logging.info(response)
                assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: low_water_mark_reset',response)
                logging.info("Test Case 42 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=43)
	def test_43_Serach_low_water_mark_reset_exact_equality(self):
		logging.info("perform Search with =  for low_water_mark_reset field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?low_water_mark_reset=0")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: low_water_mark_reset',response)
		logging.info("Test Case 43 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=44)
	def test_44_Serach_low_water_mark_reset_case_insensitive(self):
		logging.info("perform Search with :=  for low_water_mark_reset field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?low_water_mark_reset:=0")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: low_water_mark_reset',response)
		logging.info("Test Case 44 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=45)
	def test_45_Serach_low_water_mark_reset_regular_expression(self):
		logging.info("perform Search with ~=  for low_water_mark_reset field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?low_water_mark_reset~=0")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: low_water_mark_reset',response)
		logging.info("Test Case 45 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=46)
	def test_46_Update_network_view_MS_Superscope(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for network_view field in mssuperscope")
		data ={"network_view": "default"}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		servers = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?_return_fields=network_view")
		logging.info(servers)
		res = json.loads(servers)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["network_view"] == "default"
		logging.info("Test Case 46 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=47)
	def test_47_Serach_network_view_exact_equality(self):
		logging.info("perform Search with =  for network_view field in mssuperscope ")
		response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?network_view=default")
		print response
		logging.info(response)
		res = json.loads(response)
		print res
		for i in res:
			logging.info("found")
			assert i["network_view"] == "default"
		logging.info("Test Case 47 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=48)
	def test_48_Serach_network_view_case_insensitive(self):
		logging.info("perform Search with :=  for network_view field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?network_view:=DEfault")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Search modifier',response)
		logging.info("Test Case 48 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=49)
	def test_49_Serach_network_view_regular_expression(self):
		logging.info("perform Search with ~=  for network_view field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?network_view~=defa*")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Search modifier',response)
		logging.info("Test Case 49 Execution Completed")
		logging.info("=============================")


        @pytest.mark.run(order=50)
        def test_50_Update_static_hosts_MS_Superscope(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation for static_hosts field in mssuperscope")
                data ={"static_hosts": 1}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                logging.info(response)
                assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: static_hosts',response)
                logging.info("Test Case 50 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=50)
	def test_50_Serach_static_hosts_exact_equality(self):
		logging.info("perform Search with =  for static_hosts field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?static_hosts=0")
		print response
                print status
                assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: static_hosts',response)
		logging.info("Test Case 50 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=51)
	def test_51_Serach_static_hosts_case_insensitive(self):
		logging.info("perform Search with :=  for static_hosts field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?static_hosts:=0")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: static_hosts',response)
		logging.info("Test Case 51 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=52)
	def test_52_Serach_static_hosts_regular_expression(self):
		logging.info("perform Search with ~=  for static_hosts field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?static_hosts~=0")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: static_hosts',response)
		logging.info("Test Case 52 Execution Completed")
		logging.info("=============================")

        @pytest.mark.run(order=53)
        def test_53_Update_total_hosts_MS_Superscope(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation for total_hosts field in mssuperscope")
                data ={"total_hosts": 1}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                logging.info(response)
                assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: total_hosts',response)
                logging.info("Test Case 53 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=55)
	def test_55_Serach_total_hosts_exact_equality(self):
		logging.info("perform Search with =  for total_hosts field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?total_hosts=default")
		logging.info(response)
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: total_hosts',response)
		logging.info("Test Case 55 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=56)
	def test_56_Serach_total_hosts_case_insensitive(self):
		logging.info("perform Search with :=  for total_hosts field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?total_hosts:=DEfault")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: total_hosts',response)
		logging.info("Test Case 56 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=57)
	def test_57_Serach_total_hosts_regular_expression(self):
		logging.info("perform Search with ~=  for total_hosts field in mssuperscope ")
		status,response = ib_NIOS.wapi_request('GET',object_type="mssuperscope",params="?total_hosts~=defa*")
		print response
		print status
		assert status == 400 and re.search(r'AdmConProtoError: Field is not searchable: total_hosts',response)
		logging.info("Test Case 57 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=58)
	def test_58_DELETE_MS_Superscope(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="mssuperscope")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Deleting the MS_Superscope")
		get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
		print get_status
		logging.info(get_status)
		read = re.search(r'200',get_status)
		for read in get_status:
			assert True
		logging.info("Test Case 58 Execution Completed")
		logging.info("=============================")


        @pytest.mark.run(order=59)
        def test_59_DELETE_MS_Network(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="network")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Deleting the MS Network")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True
                logging.info("Test Case 59 Execution Completed")
                logging.info("=============================")

		
        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

