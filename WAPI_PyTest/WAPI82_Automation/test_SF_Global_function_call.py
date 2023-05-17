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
        def test_1_smartfolder_global(self):
                logging.info("Create smartfolder:global with required all fields")
                data = { "comment": "samrt_global","group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"name": "global_testing_smartofolder","query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": "default"},"value_type": "ENUM"}]}
                response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
                logging.info("============================")
                print response

        @pytest.mark.run(order=2)
        def test_2_Create_smartfolder_global_object_with_function_call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test create operation for Function Calls smartfolder:global object")
                data ={"is_shortcut":False,"global_flag":True}
                response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=save_as",fields=json.dumps(data))
                print response
                logging.info(response)
                res = json.loads(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")




        @pytest.mark.run(order=2)
        def test_2_Create_smartfolder_global_object_with_name_filed_in_function_call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test create operation for Function Calls smartfolder:global object")
                data ={"name":"Smart_child_personal_44"}
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
        def test_3_Create_smartfolder_global_object_with_is_shortcut_filed_in_function_call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test create operation for Function Calls smartfolder:global object")
                data ={"is_shortcut":False}
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
        def test_4_Result_Fild_smartfolder_global_object_with_function_call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test create operation for Function Calls smartfolder:global object")
                data ={"result":False}
                status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=save_as",fields=json.dumps(data))
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not writable: result',response)
                logging.info("Test Case 4 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=5)
        def test_5_Create_smartfolder_global_object_with_function_call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test create operation for Function Calls smartfolder:global object")
                data ={"global_flag":False}
                response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=save_as",fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 5 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=6)
        def test_6_PUT_On_smartfolder_global_object_with_function_call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test create operation for Function Calls smartfolder:global object")
                data ={"name":"Smart_child_personal_ps1","is_shortcut":False}
                status,response = ib_NIOS.wapi_request('PUT',object_type=ref,params="?_function=save_as",fields=json.dumps(data))
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Function save_as illegal with this method',response)
                logging.info("Test Case 6 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=7)
        def test_7_DELETE_On_smartfolder_global_object_with_function_call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test create operation for Function Calls smartfolder:global object")
                data ={"global_flag":False}
                status,response = ib_NIOS.wapi_request('DELETE',object_type=ref,params="?_function=save_as",fields=json.dumps(data))
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Function save_as illegal with this method',response)
                logging.info("Test Case 7 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=8)
        def test_8_DELETE_the_smartfolder_global_object(self):
                logging.info("DELETE_the_smartfolder_global_object")
                data = {"name": "global_testing_smartofolder"}
                response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9jaGlsZF9wZXJzb25hbF80NA:Smart_child_personal_44/false", fields=json.dumps(data))
                logging.info("Test Case 8 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=9)
        def test_9_DELETE_the_smartfolder_global_object(self):
                logging.info("DELETE_the_smartfolder_global_object")
                data = {"name": "global_testing_smartofolder%20Copy"}
                response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5nbG9iYWxfdGVzdGluZ19zbWFydG9mb2xkZXIgQ29weQ:global_testing_smartofolder%20Copy/false", fields=json.dumps(data))
                logging.info("Test Case 9 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=10)
        def test_10_DELETE_the_smartfolder_global_object(self):
                logging.info("DELETE_the_smartfolder_global_object")
                data = {"name": "global_testing_smartofolder%20Copy1/false"}
                response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5nbG9iYWxfdGVzdGluZ19zbWFydG9mb2xkZXIgQ29weTE:global_testing_smartofolder%20Copy1/false", fields=json.dumps(data))
                logging.info("Test Case 10 Execution Completed")
                logging.info("============================")
					

        @pytest.mark.run(order=11)
        def test_11_DELETE_the_smartfolder_global_object(self):
                logging.info("DELETE_the_smartfolder_global_object")
                data = {"name": "Smart_child_personal_44/false"}
                response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hbF9bWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9jaGlsZF9wZXJzb25hbF80NA:Smart_child_personal_44/false", fields=json.dumps(data))
                logging.info("Test Case 11 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=12)
        def test_12_DELETE_the_smartfolder_global_object(self):
                logging.info("DELETE_the_smartfolder_global_object")
                data = {"name": "global_testing_smartofolder%20Copy/false"}
                response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5nbG9iYWxfdGVzdGluZ19zbWFydG9mb2xkZXIgQ29weQ:global_testing_smartofolder%20Copy/false", fields=json.dumps(data))
                logging.info("Test Case 12 Execution Completed")
                logging.info("============================")

				
