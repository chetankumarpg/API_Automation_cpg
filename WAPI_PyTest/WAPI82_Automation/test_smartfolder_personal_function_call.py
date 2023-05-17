import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class smartfolder_personal_Function_Call(unittest.TestCase):

 


        @pytest.mark.run(order=1)
        def test_1_create_the_smartfolder_personal_object_with_all_required_fields(self):
                logging.info("create_the_smartfolder_personal_object_with_all_required_fields")
                data = { "comment": "Smart_personal_folder_wapi","group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"name": "Smart_personal_folder_wapi7","query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": "default"},"value_type": "ENUM"}]}
                response = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
                logging.info("============================")
                print response


	@pytest.mark.run(order=2)
	def test_2_Adding_smartfolder_personal_object_with_name_and_is_shortcut_in_function_call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:personal")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Adding_smartfolder_personal_object_with_name_in_function_call")
                data ={"name":"Smart_child_personal","is_shortcut":False}
                response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=save_as",fields=json.dumps(data))
                print response
                logging.info(response)
                res = json.loads(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 2 Execution Completed")
                logging.info("============================")



	@pytest.mark.run(order=3)
	def test_3_Adding_smartfolder_personal_object_with_name_in_function_call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:personal")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Adding_smartfolder_personal_object_with_name_in_function_call")
                data ={"name":"Smart_child_personal_11"}
                response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=save_as",fields=json.dumps(data))
                print response
                logging.info(response)
                res = json.loads(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 3 Execution Completed")
                logging.info("============================")



	@pytest.mark.run(order=4)
	def test_3_Adding_smartfolder_personal_object_with_is_shortcut_in_function_call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:personal")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Adding_smartfolder_personal_object_with_is_shortcut_in_function_call")
                data ={"is_shortcut":False}
                response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=save_as",fields=json.dumps(data))
                print response
                logging.info(response)
                res = json.loads(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 4 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=5)
	def test_5_Create_smartfolder_personal_object_with_function_call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:personal")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test create operation for Function Calls smartfolder:personal object")
		data ={"global_flag":False}
		response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=save_as",fields=json.dumps(data))
		print response
		logging.info(response)
		res = json.loads(response)
		read  = re.search(r'200',response)
		for read in  response:
			assert True
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")

		
	@pytest.mark.run(order=6)
	def test_6_Put_smartfolder_personal_object_with_function_call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:personal")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test PUT for operation smartfolder:groupbyvalue object")
		data ={"global_flag":False}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,params="?_function=save_as",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Function save_as illegal with this method',response)
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")
		
		
        @pytest.mark.run(order=7)
        def test_7_DELETE_smartfolder_personal_object_with_function_call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:personal")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref

                logging.info("Deleting smartfolder_personal ")
                data = {"is_shortcut":False,"global_flag":"fdgk"}
                status,get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,params="?_function=check_radius_server_settings",fields=json.dumps(data))
                print get_status
                print status
                logging.info(get_status)
                assert status == 400 and re.search(r'AdmConProtoError: Function check_radius_server_settings illegal with this method',get_status)
                logging.info("Test Case 7 Execution Completed")
                logging.info("=============================")


                
        @pytest.mark.run(order=8)
        def test_8_DELETE_the_smartfolder_personal(self):
                logging.info("DELETE_the_smartfolder_personal")
                data = {"name": "Smart_child_personal/false"}
                response = ib_NIOS.wapi_request('DELETE',ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9jaGlsZF9wZXJzb25hbA:Smart_child_personal/false", fields=json.dumps(data))
                logging.info("Test Case 8 Execution Completed")
                logging.info("============================")
	


        @pytest.mark.run(order=9)
        def test_9_DELETE_the_smartfolder_personal(self):
                logging.info("DELETE_the_smartfolder_personal")
                data = {"name": "Smart_child_personal_11/false"}
                response = ib_NIOS.wapi_request('DELETE', ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9jaGlsZF9wZXJzb25hbF8xMQ:Smart_child_personal_11/false", fields=json.dumps(data))
                logging.info("Test Case 9 Execution Completed")
                logging.info("============================")
		
			
	@pytest.mark.run(order=10)
        def test_10_DELETE_the_smartfolder_personal(self):
                logging.info("DELETE_the_smartfolder_personal")
                data = {"name": "Smart_child_personal%20Copy/false"}
                response = ib_NIOS.wapi_request('DELETE', ref="smartfolder:personal/Li5teV9wZXJzb25hbFzbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9jaGlsZF9wZXJzb25hbCBDb3B5:Smart_child_personal%20Copy/false", fields=json.dumps(data))
                logging.info("Test Case 10 Execution Completed")
                logging.info("============================")
		

		
        @pytest.mark.run(order=11)
        def test_11_DELETE_the_smartfolder_personal(self):
                logging.info("DELETE_the_smartfolder_personal")
                data = {"name": "Smart_child_personal%20Copy1/false"}
                response = ib_NIOS.wapi_request('DELETE', ref="smartfolder:personal/Li5teV9wZXJzb25hbFzbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9jaGlsZF9wZXJzb25hbCBDb3B5MQ:Smart_child_personal%20Copy1/false", fields=json.dumps(data))
                logging.info("Test Case 11 Execution Completed")
                logging.info("============================")
	

 		
        @pytest.mark.run(order=12)
        def test_12_DELETE_the_smartfolder_personal(self):
                logging.info("DELETE_the_smartfolder_personal")
                data = {"name": "Smart_personal_folder_wapi7/false"}
                response = ib_NIOS.wapi_request('DELETE', ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9wZXJzb25hbF9mb2xkZXJfd2FwaTc:Smart_personal_folder_wapi7/false", fields=json.dumps(data))
                logging.info("Test Case 12 Execution Completed")
                logging.info("============================")
		
		
