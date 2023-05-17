import re
import json
import pytest
import unittest
import subprocess
import config
import logging
import ib_utils.ib_NIOS as ib_NIOS

class IPv6_Fixed_Address_Template(unittest.TestCase):


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
	def test_1_Create_New_ipv6fixedaddresstemplate(self):
	
		logging.info("Test to Create a new ipv6fixedaddresstemplate")
		data = {"name": "Template1","comment": "QA_Testing"}
		run  = ib_NIOS.wapi_request('POST',object_type="ipv6fixedaddresstemplate",fields=json.dumps(data))
		print run
		logging.info(run)
		read = re.search(r'201',run)
		for read in run:
			assert True
		logging.info("Test Case 1 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=2)
	def test_2_Restriction_for_Scheduling_ipv6fixedaddresstemplate(self):
	
		logging.info("Test restriction for scheduling of ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('POST',object_type="ipv6fixedaddresstemplate",params="?_schedinfo.scheduled_time=1924223800")
		print status
		print response
		logging.info(response)
		assert status ==400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=3)
	def test_3_Restriction_for_CSV_Export_ipv6fixedaddresstemplate(self):
	
		logging.info("Test restriction for CSV Expost of ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('POST',object_type="ipv6fixedaddresstemplate",params="?_function=csv_export")
		print status
		print response
		logging.info(response)
		assert status ==400 and re.search(r'AdmConProtoError: Function csv_export is not valid for this object',response)
		logging.info("Test Case 3 Execution Completed")



	@pytest.mark.run(order=4)
	def test_4_Test_Fields_ipv6fixedaddresstemplate(self):
	
		logging.info("Test the fields of ipv6fixedaddresstemplate")
		response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate")
		print response
		logging.info(response)
		res = json.loads(response)
		for i in res:
			print i
			logging.info("found")
			assert i["name"] == "Template1" and i["comment"] =="QA_Testing"
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=5)
	def test_5_Req_Fields_for_ipv6fixedaddresstemplate(self):
	
		logging.info("Test req felds on  Creation of a new ipv6fixedaddresstemplate")
		data = {"comment": "QA_Testing"}
		status,response  = ib_NIOS.wapi_request('POST',object_type="ipv6fixedaddresstemplate",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: field for create missing: name',response)
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=6)
	def test_6_comment_ipv6fixedaddresstemplate(self):
		logging.info("Test the comment fileld in ipv6fixedaddresstemplate object")
		data = {"comment": "QA_Testing"}
		comment = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=comment")
		logging.info(comment)
		res = json.loads(comment)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["comment"] == "QA_Testing"
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=7)
	def test_7_Serach_comment_exact_equality(self):
		logging.info("perform Search with =  for comment field in ipv6fixedaddresstemplate ")
		response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?comment=QA_Testing")
		print response
		logging.info(response)
		assert re.search(r'QA_Testing',response)
		logging.info("Test Case 7 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=8)
	def test_8_Serach_comment_case_insensitive(self):
		logging.info("perform Search with :=  for comment field in ipv6fixedaddresstemplate ")
		response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?comment:=qA_testing")
		print response
		logging.info(response)
		assert re.search(r'qA_testing',response,re.I)
		logging.info("Test Case 8 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=9)
	def test_9_Serach_comment_regular_expression(self):
		logging.info("perform Search with ~=  for comment field in ipv6fixedaddresstemplate ")
		response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?comment~=QA_Tes*")
		print response
		logging.info(response)
		assert re.search(r'QA_Tes*',response)
		logging.info("Test Case 9 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=10)
	def test_10_comment_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  comment field ipv6fixedaddresstemplate object")
		data ={"name": "Template1","comment": True}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for comment: true: Must be string type',response)
		logging.info("Test Case 10 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=11)
	def test_11_domain_name_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  domain_name field ipv6fixedaddresstemplate object")
		data ={"name": "Template1","domain_name": True}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for domain_name: true: Must be string type',response)
		logging.info("Test Case 11 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=12)
	def test_12_Update_domain_name_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for domain_name field in ipv6fixedaddresstemplate")
		data ={"domain_name": "asm.com"}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		domain_name = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=domain_name")
		logging.info(domain_name)
		res = json.loads(domain_name)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["domain_name"] == "asm.com"
		logging.info("Test Case 12 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=13)
	def test_13_Serach_domain_name_exact_equality(self):
		logging.info("perform Search with =  for domain_name field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?domain_name=0")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: domain_name',response)
		logging.info("Test Case 13 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=14)
	def test_14_Serach_domain_name_case_insensitive(self):
		logging.info("perform Search with :=  for domain_name field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?domain_name:=0")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: domain_name',response)
		logging.info("Test Case 14 Execution Completed")
		logging.info("=============================")

		
	@pytest.mark.run(order=15)
	def test_15_Serach_domain_name_case_regular_expression(self):
		logging.info("perform Search with ~=  for domain_name field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?domain_name~=0")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: domain_name',response)
		logging.info("Test Case 15 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=16)
	def test_16_Update_domain_name_servers_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for domain_name_servers field in ipv6fixedaddresstemplate")
		data ={"domain_name_servers": ["2001:db8:a0b:12f0::1"]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		domain_name_servers = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=domain_name_servers")
		logging.info(domain_name_servers)
		res = json.loads(domain_name_servers)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["domain_name_servers"] == ["2001:db8:a0b:12f0::1"]
		logging.info("Test Case 16 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=17)
	def test_17_Serach_domain_name_servers_exact_equality(self):
		logging.info("perform Search with =  for domain_name_servers field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?domain_name_servers=2001:db8:a0b:12f0::1")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: domain_name_servers',response)
		logging.info("Test Case 17 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=18)
	def test_18_Serach_domain_name_servers_case_insensitive(self):
		logging.info("perform Search with :=  for domain_name_servers field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?domain_name_servers:=2001:db8:a0b:12f0::1")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: domain_name_servers',response)
		logging.info("Test Case 18 Execution Completed")
		logging.info("=============================")

		
	@pytest.mark.run(order=19)
	def test_19_Serach_domain_name_servers_case_regular_expression(self):
		logging.info("perform Search with ~=  for domain_name_servers field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?domain_name_servers~=2001:db8:a0b:12f0::1")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: domain_name_servers',response)
		logging.info("Test Case 19 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=20)
	def test_20_Update_name_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for name field in ipv6fixedaddresstemplate")
		data ={"name": "template"}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		name = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=name")
		logging.info(name)
		res = json.loads(name)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["name"] == "template"
		logging.info("Test Case 20 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=21)
	def test_21_Serach_name_exact_equality(self):
		logging.info("perform Search with =  for name field in ipv6fixedaddresstemplate ")
		response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?name=template")
		print response
		logging.info(response)
		assert re.search(r'template',response)
		logging.info("Test Case 21 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=22)
	def test_22_Serach_name_case_insensitive(self):
		logging.info("perform Search with :=  for name field in ipv6fixedaddresstemplate ")
		response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?name:=TeMplate")
		print response
		logging.info(response)
		assert re.search(r'TeMplate',response,re.I)
		logging.info("Test Case 22 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=23)
	def test_23_Serach_name_regular_expression(self):
		logging.info("perform Search with ~=  for name field in ipv6fixedaddresstemplate ")
		response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?name~=templ*")
		print response
		logging.info(response)
		assert re.search(r'templ*',response)
		logging.info("Test Case 23 Execution Completed")
		logging.info("=============================")
		


	@pytest.mark.run(order=24)
	def test_24_name_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  name field ipv6fixedaddresstemplate object")
		data ={"name": True}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for name: true: Must be string type',response)
		logging.info("Test Case 24 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=25)
	def test_25_number_of_addresses_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  name field ipv6fixedaddresstemplate object")
		data ={"name": "template","number_of_addresses": True}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for number_of_addresses: true: Must be integer type',response)
		logging.info("Test Case 25 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=26)
	def test_26_Update_number_of_addresses_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for number_of_addresses field in ipv6fixedaddresstemplate")
		data ={"name": "template","number_of_addresses": 3}
		status,get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		number_of_addresses = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=number_of_addresses")
		logging.info(number_of_addresses)
		print status
		print get_status
		assert status == 400 and re.search(r'AdmConDataError: None ',get_status)
		logging.info("Test Case 26 Execution Completed")
		logging.info("============================")
		
	@pytest.mark.run(order=27)
	def test_27_Serach_number_of_addresses_exact_equality(self):
		logging.info("perform Search with =  for number_of_addresses field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?number_of_addresses=3")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: number_of_addresses',response)
		logging.info("Test Case 27 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=28)
	def test_28_Serach_number_of_addresses_case_insensitive(self):
		logging.info("perform Search with :=  for number_of_addresses field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?number_of_addresses:=3")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: number_of_addresses',response)
		logging.info("Test Case 28 Execution Completed")
		logging.info("=============================")

		
	@pytest.mark.run(order=29)
	def test_29_Serach_number_of_addresses_case_regular_expression(self):
		logging.info("perform Search with ~=  for number_of_addresses field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?number_of_addresses~=3")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: number_of_addresses',response)
		logging.info("Test Case 29 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=30)
	def test_30_offset_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  name field ipv6fixedaddresstemplate object")
		data ={"name": "template","offset": True}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for offset: true: Must be integer type',response)
		logging.info("Test Case 30 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=31)
	def test_31_Update_offset_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for offset field in ipv6fixedaddresstemplate")
		data ={"name": "template","offset": 3}
		status,get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		offset = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=offset")
		logging.info(offset)
		print status
		print get_status
		assert status == 400 and re.search(r'AdmConDataError: None ',get_status)
		logging.info("Test Case 31 Execution Completed")
		logging.info("============================")

		
	@pytest.mark.run(order=32)
	def test_32_Serach_offset_exact_equality(self):
		logging.info("perform Search with =  for offset field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?offset=3")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: offset',response)
		logging.info("Test Case 32 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=33)
	def test_33_Serach_offset_case_insensitive(self):
		logging.info("perform Search with :=  for offset field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?offset:=3")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: offset',response)
		logging.info("Test Case 33 Execution Completed")
		logging.info("=============================")

		
	@pytest.mark.run(order=34)
	def test_34_Serach_offset_case_regular_expression(self):
		logging.info("perform Search with ~=  for offset field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?offset~=3")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: offset',response)
		logging.info("Test Case 34 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=35)
	def test_35_options_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  name field ipv6fixedaddresstemplate object")
		data ={"name": "template","options": True}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: List value expected for field: options',response)
		logging.info("Test Case 35 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=36)
	def test_36_Update_options_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for options field in ipv6fixedaddresstemplate")
		data ={"name": "template","options": [{ 'name': 'dhcp-lease-time','num': 51,'use_option': False,'value': '43200','vendor_class': 'DHCP'}]}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		options = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=options")
		logging.info(options)
		read= re.search(r'200',options)
		for read in options:
			assert True 
		logging.info("Test Case 36 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=37)
	def test_37_Serach_options_exact_equality(self):
		logging.info("perform Search with =  for options field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?options=name")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: options',response)
		logging.info("Test Case 37 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=38)
	def test_38_Serach_options_case_insensitive(self):
		logging.info("perform Search with :=  for options field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?options:=Name")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: options',response)
		logging.info("Test Case 38 Execution Completed")
		logging.info("=============================")

		
	@pytest.mark.run(order=39)
	def test_39_Serach_options_case_regular_expression(self):
		logging.info("perform Search with ~=  for options field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?options~=nam*")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: options',response)
		logging.info("Test Case 39 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=40)
	def test_40_preferred_lifetime_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  name field ipv6fixedaddresstemplate object")
		data ={"name": "template","preferred_lifetime": True}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for preferred_lifetime: true: Must be integer type',response)
		logging.info("Test Case 40 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=41)
	def test_41_Update_preferred_lifetime_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for preferred_lifetime field in ipv6fixedaddresstemplate")
		data ={"name": "template","preferred_lifetime": 2500}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		preferred_lifetime = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=preferred_lifetime")
		logging.info(preferred_lifetime)
		res = json.loads(preferred_lifetime)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["preferred_lifetime"] == 2500
		logging.info("Test Case 41 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=42)
	def test_42_Serach_preferred_lifetime_exact_equality(self):
		logging.info("perform Search with =  for preferred_lifetime field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?preferred_lifetime=2500")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: preferred_lifetime',response)
		logging.info("Test Case 42 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=43)
	def test_43_Serach_preferred_lifetime_case_insensitive(self):
		logging.info("perform Search with :=  for preferred_lifetime field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?preferred_lifetime:=2500")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: preferred_lifetime',response)
		logging.info("Test Case 43 Execution Completed")
		logging.info("=============================")

		
	@pytest.mark.run(order=44)
	def test_44_Serach_preferred_lifetime_case_regular_expression(self):
		logging.info("perform Search with ~=  for preferred_lifetime field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?preferred_lifetime~=2500")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: preferred_lifetime',response)
		logging.info("Test Case 44 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=45)
	def test_45_use_domain_name_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  name field ipv6fixedaddresstemplate object")
		data ={"name": "template","use_domain_name": "yes"}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for use_domain_name: ',response)
		logging.info("Test Case 45 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=46)
	def test_46_Update_use_domain_name_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for use_domain_name field in ipv6fixedaddresstemplate")
		data ={"name": "template","use_domain_name": True}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_domain_name = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=use_domain_name")
		logging.info(use_domain_name)
		res = json.loads(use_domain_name)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["use_domain_name"] == True
		logging.info("Test Case 46 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=47)
	def test_47_Serach_use_domain_name_exact_equality(self):
		logging.info("perform Search with =  for use_domain_name field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_domain_name=true")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_domain_name',response)
		logging.info("Test Case 47 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=48)
	def test_48_Serach_use_domain_name_case_insensitive(self):
		logging.info("perform Search with :=  for use_domain_name field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_domain_name:=TRue")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_domain_name',response)
		logging.info("Test Case 48 Execution Completed")
		logging.info("=============================")

		
	@pytest.mark.run(order=49)
	def test_49_Serach_use_domain_name_case_regular_expression(self):
		logging.info("perform Search with ~=  for use_domain_name field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_domain_name~=tru*")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_domain_name',response)
		logging.info("Test Case 49 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=50)
	def test_50_use_domain_name_servers_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  name field ipv6fixedaddresstemplate object")
		data ={"name": "template","use_domain_name_servers": "Yes"}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for use_domain_name_servers:',response)
		logging.info("Test Case 50 Execution Completed")
		logging.info("============================")

		

	@pytest.mark.run(order=51)
	def test_51_Update_use_domain_name_servers_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for use_domain_name_servers field in ipv6fixedaddresstemplate")
		data ={"name": "template","use_domain_name_servers": True}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_domain_name_servers = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=use_domain_name_servers")
		logging.info(use_domain_name_servers)
		res = json.loads(use_domain_name_servers)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["use_domain_name_servers"] == True
		logging.info("Test Case 51 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=52)
	def test_52_Serach_use_domain_name_servers_exact_equality(self):
		logging.info("perform Search with =  for use_domain_name_servers field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_domain_name_servers=true")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_domain_name_servers',response)
		logging.info("Test Case 52 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=53)
	def test_53_Serach_use_domain_name_servers_case_insensitive(self):
		logging.info("perform Search with :=  for use_domain_name_servers field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_domain_name_servers:=TRue")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_domain_name_servers',response)
		logging.info("Test Case 53 Execution Completed")
		logging.info("=============================")

		
	@pytest.mark.run(order=54)
	def test_54_Serach_use_domain_name_servers_case_regular_expression(self):
		logging.info("perform Search with ~=  for use_domain_name_servers field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_domain_name_servers~=tru*")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_domain_name_servers',response)
		logging.info("Test Case 54 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=55)
	def test_55_use_options_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  name field ipv6fixedaddresstemplate object")
		data ={"name": "template","use_options": "Yes"}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for use_options:',response)
		logging.info("Test Case 55 Execution Completed")
		logging.info("============================")

		

	@pytest.mark.run(order=56)
	def test_56_Update_use_options_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for use_options field in ipv6fixedaddresstemplate")
		data ={"name": "template","use_options": True}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_options = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=use_options")
		logging.info(use_options)
		res = json.loads(use_options)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["use_options"] == True
		logging.info("Test Case 56 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=57)
	def test_57_Serach_use_options_exact_equality(self):
		logging.info("perform Search with =  for use_options field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_options=true")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_options',response)
		logging.info("Test Case 57 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=58)
	def test_58_Serach_use_options_case_insensitive(self):
		logging.info("perform Search with :=  for use_options field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_options:=TRue")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_options',response)
		logging.info("Test Case 58 Execution Completed")
		logging.info("=============================")

		
	@pytest.mark.run(order=59)
	def test_59_Serach_use_options_case_regular_expression(self):
		logging.info("perform Search with ~=  for use_options field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_options~=tru*")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_options',response)
		logging.info("Test Case 59 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=60)
	def test_60_use_preferred_lifetime_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  name field ipv6fixedaddresstemplate object")
		data ={"name": "template","use_preferred_lifetime": "Yes"}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for use_preferred_lifetime:',response)
		logging.info("Test Case 60 Execution Completed")
		logging.info("============================")

		

	@pytest.mark.run(order=61)
	def test_61_Update_use_preferred_lifetime_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for use_preferred_lifetime field in ipv6fixedaddresstemplate")
		data ={"name": "template","use_preferred_lifetime": True}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_preferred_lifetime = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=use_preferred_lifetime")
		logging.info(use_preferred_lifetime)
		res = json.loads(use_preferred_lifetime)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["use_preferred_lifetime"] == True
		logging.info("Test Case 61 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=62)
	def test_62_Serach_use_preferred_lifetime_exact_equality(self):
		logging.info("perform Search with =  for use_preferred_lifetime field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_preferred_lifetime=true")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_preferred_lifetime',response)
		logging.info("Test Case 62 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=63)
	def test_63_Serach_use_preferred_lifetime_case_insensitive(self):
		logging.info("perform Search with :=  for use_preferred_lifetime field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_preferred_lifetime:=TRue")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_preferred_lifetime',response)
		logging.info("Test Case 63 Execution Completed")
		logging.info("=============================")

		
	@pytest.mark.run(order=64)
	def test_64_Serach_use_preferred_lifetime_case_regular_expression(self):
		logging.info("perform Search with ~=  for use_preferred_lifetime field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_preferred_lifetime~=tru*")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_preferred_lifetime',response)
		logging.info("Test Case 64 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=65)
	def test_65_use_valid_lifetime_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  name field ipv6fixedaddresstemplate object")
		data ={"name": "template","use_valid_lifetime": "Yes"}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for use_valid_lifetime:',response)
		logging.info("Test Case 65 Execution Completed")
		logging.info("============================")

		

	@pytest.mark.run(order=66)
	def test_66_Update_use_valid_lifetime_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for use_valid_lifetime field in ipv6fixedaddresstemplate")
		data ={"name": "template","use_valid_lifetime": True}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		use_valid_lifetime = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=use_valid_lifetime")
		logging.info(use_valid_lifetime)
		res = json.loads(use_valid_lifetime)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["use_valid_lifetime"] == True
		logging.info("Test Case 66 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=67)
	def test_67_Serach_use_valid_lifetime_exact_equality(self):
		logging.info("perform Search with =  for use_valid_lifetime field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_valid_lifetime=true")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_valid_lifetime',response)
		logging.info("Test Case 67 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=68)
	def test_68_Serach_use_valid_lifetime_case_insensitive(self):
		logging.info("perform Search with :=  for use_valid_lifetime field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_valid_lifetime:=TRue")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_valid_lifetime',response)
		logging.info("Test Case 68 Execution Completed")
		logging.info("=============================")

		
	@pytest.mark.run(order=69)
	def test_69_Serach_use_valid_lifetime_case_regular_expression(self):
		logging.info("perform Search with ~=  for use_valid_lifetime field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?use_valid_lifetime~=tru*")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: use_valid_lifetime',response)
		logging.info("Test Case 69 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=70)
	def test_70_valid_lifetime_field_datatype_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  name field ipv6fixedaddresstemplate object")
		data ={"name": "template","valid_lifetime": True}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for valid_lifetime: true: Must be integer type',response)
		logging.info("Test Case 70 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=71)
	def test_71_Update_valid_lifetime_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation for valid_lifetime field in ipv6fixedaddresstemplate")
		data ={"name": "template","valid_lifetime": 2500}
		get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		valid_lifetime = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?_return_fields=valid_lifetime")
		logging.info(valid_lifetime)
		res = json.loads(valid_lifetime)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["valid_lifetime"] == 2500
		logging.info("Test Case 71 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=72)
	def test_72_Serach_valid_lifetime_exact_equality(self):
		logging.info("perform Search with =  for valid_lifetime field in ipv6fixedaddresstemplate ")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?valid_lifetime=2500")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: valid_lifetime',response)
		logging.info("Test Case 72 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=73)
	def test_73_Serach_valid_lifetime_case_insensitive(self):
		logging.info("perform Search with :=  for valid_lifetime field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?valid_lifetime:=2500")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: valid_lifetime',response)
		logging.info("Test Case 73 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=74)
	def test_74_Serach_valid_lifetime_case_regular_expression(self):
		logging.info("perform Search with ~=  for valid_lifetime field in ipv6fixedaddresstemplate")
		status,response = ib_NIOS.wapi_request('GET',object_type="ipv6fixedaddresstemplate",params="?valid_lifetime~=2500")
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: valid_lifetime',response)
		logging.info("Test Case 74 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=75)
	def test_75_DELETE_ipv6fixedaddresstemplate(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6fixedaddresstemplate")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Deleting the ipv6fixedaddresstemplate template")
		get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
		print get_status
		logging.info(get_status)
		logging.info("Test Case 75 Execution Completed")
		logging.info("=============================")


        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

