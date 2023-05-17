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

class Networkview(unittest.TestCase):

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
	def test_1_The_Networkview_Object(self):
		
		logging.info("Test the format of networkview object")
		get_tacacsplus = ib_NIOS.wapi_request('GET', object_type="networkview")
		logging.info(get_tacacsplus)
		res = json.loads(get_tacacsplus)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["name"] == "default" and i["is_default"] == True
		logging.info("Test Case 1 Execution Completed")
		logging.info("============================")

		
	@pytest.mark.run(order=2)
	def test_Create_Networkview(self):
        	logging.info("Create A new networkview")
        	data = {"name": "Testing","comment" : "QA_Testing"}
        	response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
        	print response
        	logging.info(response)
        	read  = re.search(r'201',response)
        	for read in  response:
        	    assert True
        	logging.info("Test Case 1 Execution Completed")
        	logging.info("============================")

	@pytest.mark.run(order=3)
	def test__Schedule_Networkview(self):
       		logging.info("Perform schedule operation for networkview")
        	status,response = ib_NIOS.wapi_request('POST', object_type="networkview",params="?_schedinfo.scheduled_time=1924223800")
        	print status
        	print response
        	logging.info(response)
        	assert  status == 400 and re.search(r'(IBDataConflictError: IB.Data.Conflict:networkview does not support scheduling.)',response)
        	logging.info("Test Case 3 Execution Completed")
        	logging.info("============================")


	@pytest.mark.run(order=4)
	def test_Csv_Export_Networkview(self):
		logging.info("Test the restriction for the networkview object - CSV Export")
		data = {"name":"Test"}
		status,response = ib_NIOS.wapi_request('POST', object_type="networkview",params="?_function=csv_export",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Function csv_export is not valid for this object',response)
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=5)
	def test_5_Req_Fields_1_Create_networkview(self):
       		logging.info("Test the fields are required to create this object -1")
       		data = {"comment" : "QA_Testing"}
        	status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
        	print status
        	print response
        	logging.info(response)
        	assert status == 400 and re.search(r'AdmConProtoError: field for create missing: name',response)
        	logging.info("Test Case 5 Execution Completed")
        	logging.info("============================")

	@pytest.mark.run(order=6)
	def test_6_name_Tacacsplus_networkview(self):
		logging.info("Test the data type name fileld in networkview object")
		data = {"name": 10}
        	status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
        	print status
        	print response
        	logging.info(response)
        	assert status == 400 and re.search(r'AdmConProtoError: Invalid value for name: 10: Must be string type',response)
        	logging.info("Test Case 6 Execution Completed")
        	logging.info("============================")


		
	@pytest.mark.run(order=7)
	def test_7_Serach_name_networkview_exact_equality(self):
		logging.info("perform Search with =  for name field in networkview ")
		response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?name=Testing")
		print response
		logging.info(response)
		assert re.search(r'Testing',response)
		logging.info("Test Case 7 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=8)
	def test_8_Serach_name_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for name field in networkview ")
		response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?name:=teSTINg")
		print response
		logging.info(response)
		assert re.search(r'teSTINg',response,re.I)
		logging.info("Test Case 8 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=9)
	def test_9_Serach_name_networkview_regular_expression(self):
		logging.info("perform Search with ~=  for name field in networkview ")
		response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?name~=Test*")
		print response
		logging.info(response)
		assert re.search(r'Test*',response)
		logging.info("Test Case 9 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=10)
	def test_10_associated_dns_views_Tacacsplus_networkview(self):
		logging.info("Test the data type associated_dns_views fileld in networkview object")
		data = {"name" : "Test","associated_dns_views": True}
        	status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
        	print status
        	print response
        	logging.info(response)
        	assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: associated_dns_views',response)
        	logging.info("Test Case 10 Execution Completed")
        	logging.info("============================")

	@pytest.mark.run(order=11)
	def test_11_Serach_associated_dns_views_networkview_exact_equality(self):
		logging.info("perform Search with =  for associated_dns_views field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?associated_dns_views=default")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: associated_dns_views',response)
		logging.info("Test Case 11 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=12)
	def test_12_Serach_associated_dns_views_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for associated_dns_views field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?associated_dns_views:=DEfaUlt")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: associated_dns_views',response)
		logging.info("Test Case 12 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=13)
	def test_13_Serach_associated_dns_views_networkview_regular_expression(self):
		logging.info("perform Search with ~=  for associated_dns_views field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?associated_dns_views~=defa*")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: associated_dns_views',response)
		logging.info("Test Case 13 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=14)
	def test_14_associated_members_networkview(self):
		logging.info("Test the data type associated_members fileld in networkview object")
		data = {"name": "Test","associated_members": True}
		status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: associated_members',response)
		logging.info("Test Case 14 Execution Completed")
		logging.info("============================")


		
	@pytest.mark.run(order=15)
	def test_15_Serach_associated_members_networkview_exact_equality(self):
		logging.info("perform Search with =  for associated_members field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?associated_members=default")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: associated_members',response)
		logging.info("Test Case 15 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=16)
	def test_16_Serach_associated_members_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for associated_members field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?associated_members:=DEfaUlt")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: associated_members',response)
		logging.info("Test Case 16 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=17)
	def test_17_Serach_associated_members_networkview_regular_expression(self):
		logging.info("perform Search with ~=  for associated_members field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?associated_members~=defa*")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: associated_members',response)
		logging.info("Test Case 17 Execution Completed")
		logging.info("=============================")

        @pytest.mark.run(order=18)
        def test_18_cloud_info_networkview(self):
                logging.info("Test the data type cloud_info fileld in networkview object")
                data = {"name" : "Test","cloud_info": True}
                status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert status == 400 and re.search(r'AdmConProtoError: Structure expected in cloud_info',response)
                logging.info("Test Case 18 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=19)
        def test_19_Serach_cloud_info_networkview_exact_equality(self):
                logging.info("perform Search with =  for cloud_info field in networkview ")
                status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?cloud_info=[]")
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: cloud_info',response)
                logging.info("Test Case 19 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=20)
        def test_20_Serach_cloud_info_networkview_case_insensitive(self):
                logging.info("perform Search with :=  for cloud_info field in networkview ")
                status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?cloud_info:=[]")
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: cloud_info',response)
                logging.info("Test Case 20 Execution Completed")
                logging.info("=============================")

				
        @pytest.mark.run(order=21)
        def test_21_Serach_cloud_info_networkview_regular_expression(self):
                logging.info("perform Search with ~=  for cloud_info field in networkview ")
                status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?cloud_info~=[]")
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: cloud_info',response)
                logging.info("Test Case 21 Execution Completed")
		logging.info("=============================")


        @pytest.mark.run(order=22)
        def test_22_comment_Tacacsplus_networkview(self):
                logging.info("Test the data type comment fileld in networkview object")
                data = {"name": "Test","comment": True}
                status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert status == 400 and re.search(r'AdmConProtoError: Invalid value for comment:',response)
                logging.info("Test Case 22 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=23)
        def test_23_Serach_comment_networkview_exact_equality(self):
                logging.info("perform Search with =  for comment field in networkview ")
                response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?comment=QA_Testing")
                print response
                logging.info(response)
                assert re.search(r'QA_Testing',response)
                logging.info("Test Case 23 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=24)
        def test_24_Serach_comment_networkview_case_insensitive(self):
                logging.info("perform Search with :=  for comment field in networkview ")
                response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?comment:=qa_TEsting")
                print response
                logging.info(response)
                assert re.search(r'qa_TEsting',response,re.I)
                logging.info("Test Case 24 Execution Completed")
                logging.info("=============================")

        @pytest.mark.run(order=25)
        def test_25_Serach_comment_networkview_regular_expression(self):
                logging.info("perform Search with ~=  for comment field in networkview ")
                response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?comment~=QA_Test*")
                print response
                logging.info(response)
                assert re.search(r'QA_Test*',response)
                logging.info("Test Case 25 Execution Completed")
                logging.info("=============================")

	@pytest.mark.run(order=26)
	def test_26_ddns_dns_view_networkview(self):
		logging.info("Test the data type ddns_dns_view fileld in networkview object")
		data = {"name": "Test","ddns_dns_view": True}
		status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for ddns_dns_view:',response)
		logging.info("Test Case 26 Execution Completed")
		logging.info("============================")


		
	@pytest.mark.run(order=27)
	def test_27_Serach_ddns_dns_view_networkview_exact_equality(self):
		logging.info("perform Search with =  for ddns_dns_view field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?ddns_dns_view=default")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: ddns_dns_view',response)
		logging.info("Test Case 27 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=28)
	def test_28_Serach_ddns_dns_view_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for ddns_dns_view field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?ddns_dns_view:=DEfaUlt")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: ddns_dns_view',response)
		logging.info("Test Case 16 Execution Completed")
		logging.info("=============================")

			
	@pytest.mark.run(order=29)
	def test_29_Serach_ddns_dns_view_networkview_regular_expression(self):
		logging.info("perform Search with ~=  for ddns_dns_view field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?ddns_dns_view~=defa*")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: ddns_dns_view',response)
		logging.info("Test Case 29 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=30)
	def test_30_ddns_zone_primaries_networkview(self):
		logging.info("Test the data type ddns_zone_primaries fileld in networkview object")
		data = {"name": "Test","ddns_zone_primaries": True}
		status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: List value expected for field: ddns_zone_primaries',response)
		logging.info("Test Case 30 Execution Completed")
		logging.info("============================")


		
	@pytest.mark.run(order=31)
	def test_31_Serach_ddns_zone_primaries_networkview_exact_equality(self):
		logging.info("perform Search with =  for ddns_zone_primaries field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?ddns_zone_primaries=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: ddns_zone_primaries',response)
		logging.info("Test Case 31 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=32)
	def test_32_Serach_ddns_zone_primaries_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for ddns_zone_primaries field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?ddns_zone_primaries:=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: ddns_zone_primaries',response)
		logging.info("Test Case 32 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=33)
	def test_33_internal_forward_zones_networkview(self):
		logging.info("Test the data type internal_forward_zones fileld in networkview object")
		data = {"name": "Test","internal_forward_zones": True}
		status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: List value expected for field: internal_forward_zones',response)
		logging.info("Test Case 33 Execution Completed")
		logging.info("============================")


		
	@pytest.mark.run(order=33)
	def test_33_Serach_internal_forward_zones_networkview_exact_equality(self):
		logging.info("perform Search with =  for internal_forward_zones field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?internal_forward_zones=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: internal_forward_zones',response)
		logging.info("Test Case 33 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=34)
	def test_34_Serach_internal_forward_zones_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for internal_forward_zones field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?internal_forward_zones:=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: internal_forward_zones',response)
		logging.info("Test Case 34 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=35)
	def test_35_Serach_internal_forward_zones_networkview_regular_expression(self):
		logging.info("perform Search with ~=  for internal_forward_zones field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?internal_forward_zones~=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: internal_forward_zones',response)
		logging.info("Test Case 35 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=36)
	def test_37_is_default_networkview(self):
		logging.info("Test the data type is_default fileld in networkview object")
		data = {"name": "Test","is_default": "yes"}
		status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: is_default"',response)
		logging.info("Test Case 37 Execution Completed")
		logging.info("============================")


		
	@pytest.mark.run(order=38)
	def test_38_Serach_is_default_networkview_exact_equality(self):
		logging.info("perform Search with =  for is_default field in networkview ")
		response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?is_default=true")
		print response
		logging.info(response)
		res = json.loads(response)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["is_default"] ==  True and i["name"] ==  "default"
		logging.info("Test Case 38 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=39)
	def test_39_Serach_is_default_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for is_default field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?is_default:=trUE")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Search modifier \':\' not allowed for field: is_default"',response)
		logging.info("Test Case 39 Execution Completed")
		logging.info("=============================")

			
	@pytest.mark.run(order=40)
	def test_40_Serach_is_default_networkview_regular_expression(self):
		logging.info("perform Search with ~=  for is_default field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?is_default~=tru*")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Search modifier \'~\' not allowed for field: is_default"',response)
		logging.info("Test Case 40 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=41)
	def test_41_mgm_privatet_networkview(self):
		logging.info("Test the data type mgm_privatet fileld in networkview object")
		data = {"name": "Test","mgm_private": "yes"}
		status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for mgm_private:',response)
		logging.info("Test Case 41 Execution Completed")
		logging.info("============================")


		
	@pytest.mark.run(order=42)
	def test_42_Serach_mgm_privatet_networkview_exact_equality(self):
		logging.info("perform Search with =  for mgm_privatet field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?mgm_private")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: mgm_private',response)
		logging.info("Test Case 42 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=43)
	def test_43_Serach_mgm_privatet_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for mgm_privatet field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?mgm_private")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: mgm_private',response)
		logging.info("Test Case 43 Execution Completed")
		logging.info("=============================")

			
	@pytest.mark.run(order=44)
	def test_44_Serach_mgm_privatet_networkview_regular_expression(self):
		logging.info("perform Search with ~=  for mgm_privatet field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?mgm_private~=tru*")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: mgm_private',response)
		logging.info("Test Case 44 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=45)
	def test_45_ms_ad_user_data_networkview(self):
		logging.info("Test the data type ms_ad_user_data fileld in networkview object")
		data = {"name": "Test","ms_ad_user_data": "yes"}
		status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: ms_ad_user_data',response)
		logging.info("Test Case 45 Execution Completed")
		logging.info("============================")


		
	@pytest.mark.run(order=46)
	def test_46_Serach_ms_ad_user_data_networkview_exact_equality(self):
		logging.info("perform Search with =  for ms_ad_user_data field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?ms_ad_user_data=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: ms_ad_user_data',response)
		logging.info("Test Case 46 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=47)
	def test_47_Serach_ms_ad_user_data_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for ms_ad_user_data field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?ms_ad_user_data:=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: ms_ad_user_data',response)
		logging.info("Test Case 47 Execution Completed")
		logging.info("=============================")

			
	@pytest.mark.run(order=48)
	def test_48_Serach_ms_ad_user_data_networkview_regular_expression(self):
		logging.info("perform Search with ~=  for ms_ad_user_data field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?ms_ad_user_data~=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: ms_ad_user_data',response)
		logging.info("Test Case 48 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=49)
	def test_49_remote_forward_zones_networkview(self):
		logging.info("Test the data type remote_forward_zones fileld in networkview object")
		data = {"name": "Test","remote_forward_zones": "yes"}
		status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: List value expected for field: remote_forward_zones',response)
		logging.info("Test Case 49 Execution Completed")
		logging.info("============================")


		
	@pytest.mark.run(order=50)
	def test_50_Serach_remote_forward_zones_networkview_exact_equality(self):
		logging.info("perform Search with =  for remote_forward_zones field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?remote_forward_zones=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: remote_forward_zones',response)
		logging.info("Test Case 50 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=51)
	def test_51_Serach_remote_forward_zones_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for remote_forward_zones field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?remote_forward_zones:=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: remote_forward_zones',response)
		logging.info("Test Case 51 Execution Completed")
		logging.info("=============================")

			
	@pytest.mark.run(order=52)
	def test_52_Serach_remote_forward_zones_networkview_regular_expression(self):
		logging.info("perform Search with ~=  for remote_forward_zones field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?remote_forward_zones~=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: remote_forward_zones',response)
		logging.info("Test Case 52 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=53)
	def test_53_remote_reverse_zones_networkview(self):
		logging.info("Test the data type remote_reverse_zones fileld in networkview object")
		data = {"name": "Test","remote_reverse_zones": "yes"}
		status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: List value expected for field: remote_reverse_zones',response)
		logging.info("Test Case 53 Execution Completed")
		logging.info("============================")


		
	@pytest.mark.run(order=54)
	def test_54_Serach_remote_reverse_zones_networkview_exact_equality(self):
		logging.info("perform Search with =  for remote_reverse_zones field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?remote_reverse_zones=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: remote_reverse_zones',response)
		logging.info("Test Case 54 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=55)
	def test_55_Serach_remote_reverse_zones_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for remote_reverse_zones field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?remote_reverse_zones:=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: remote_reverse_zones',response)
		logging.info("Test Case 55 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=56)
	def test_56_Serach_remote_reverse_zones_networkview_regular_expression(self):
		logging.info("perform Search with ~=  for remote_reverse_zones field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?remote_reverse_zones~=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: remote_reverse_zones',response)
		logging.info("Test Case 56 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=57)
	def test_57_extattrs_networkview(self):
		logging.info("Test the data type extattrs fileld in networkview object")
		data = {"name": "Test","extattrs": "yes"}
		status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Field',response)
		logging.info("Test Case 57 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=58)
	def test_58_Serach_extattrs_networkview_exact_equality(self):
		logging.info("perform Search with =  for extattrs field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?extattrs=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: extattrs',response)
		logging.info("Test Case 58 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=59)
	def test_59_Serach_extattrs_networkview_case_insensitive(self):
		logging.info("perform Search with :=  for extattrs field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?extattrs:=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: extattrs',response)
		logging.info("Test Case 59 Execution Completed")
		logging.info("=============================")

			
	@pytest.mark.run(order=60)
	def test_60_Serach_extattrs_networkview_regular_expression(self):
		logging.info("perform Search with ~=  for extattrs field in networkview ")
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?extattrs~=[]")
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: extattrs',response)
		logging.info("Test Case 60 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=61)
	def test_61_Try_DELETE_default_networkview(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="networkview")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref

		logging.info("Deleting the networkview Testing")
		data ={"name": "default"}
		status,get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
		print get_status
		logging.info(get_status)
		assert  status == 400 and re.search(r'AdmConDataError: None',get_status)
		logging.info("Test Case 61 Execution Completed")
		logging.info("=============================")



	@pytest.mark.run(order=62)
	def test_62_DELETE_networkview(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="networkview")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[1]['_ref']
		print ref

		logging.info("Deleting the networkview Testing")
		data ={"name": "Testing"}
		get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
		print get_status
		logging.info(get_status)
		logging.info("Test Case 62 Execution Completed")
		logging.info("=============================")


        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

