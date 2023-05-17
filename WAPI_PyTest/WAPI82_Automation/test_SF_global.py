import re
import config
import pytest
import unittest
import logging
import subprocess
import json
from time import sleep
import ib_utils.ib_NIOS as ib_NIOS
class RangeTemplate(unittest.TestCase):

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
    def test_1_GET_operation_to_smartfolder_global_object(self):
        logging.info("GET_operation_to_smartfolder_global_object")
        get_smartfolder_global = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
        logging.info(get_smartfolder_global)
        res = json.loads(get_smartfolder_global)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")
        print res

    @pytest.mark.run(order=2)
    def test_2_smartfolder_global(self):
        logging.info("Create smartfolder:global with required fields")
        data = { "comment":"asmsmortfolderinfoblo","name":"zones_and_record"}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=3)
    def test_3_smartfolder_global(self):
        logging.info("Create smartfolder:global with required all fields")
        data = { "comment": "samrt_global","group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"name": "global_testing_smartofolder","query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": "default"},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        logging.info("============================")
        print response	

    @pytest.mark.run(order=4)
    def test_4_Modify_smartfolder_global(self):
        logging.info("Modify _smartfolder_global with required fields")
        data = {"name": "SF_global2","query_items":[{"field_type": "NORMAL","name": "zone_type","op_match": True,"operator": "EQ","value":{"value_string": "Authoritative"},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('PUT',ref='smartfolder_global/ZG5zLm9wdGlvbl9kZWZpbml0aW9uJGluZm8uLmZhbHNlLjI1Mg',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response

    @pytest.mark.run(order=5)
    def test_5_csvexport_smartfolder_global(self):
        logging.info("Perform CSV export for smartfolder_global")
        data = {"_object":"smartfolder:global"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'smartfolder:global objects do not support CSV export.',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")
	
  
    @pytest.mark.run(order=6)
    def test_6_GET_operation_to_smartfolder_global_object_with_Global_search_N(self):
        logging.info("GET_operation_to_smartfolder_global_object_with_Global_search_N")
        get_smartfolder_global = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
        logging.info(get_smartfolder_global)
        res = json.loads(get_smartfolder_global)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")
        print res	
		 

    @pytest.mark.run(order=7)
    def test_7_Get_operation_to_smartfolder_global_object_with_name_field(self):
        logging.info("Get_operation_to_smartfolder_global_object")
        data = {"name":"zones_and_record"}
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="smartfolder:global", fields=json.dumps(data))
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "zones_and_record" and i["comment"] == "asmsmortfolderinfoblo"
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=8)
    def test_8_Get_operation_to_smartfolder_global_object_with_name_field(self):
        logging.info("Get_operation_to_smartfolder_global_object")
        data = {"name":"zones_and_record"}
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="smartfolder:global", fields=json.dumps(data))
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "zones_and_record" and i["comment"] == "asmsmortfolderinfoblo"
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=9)
    def test_9_Get_operation_to_smartfolder_global_object_with_name_field(self):
        logging.info("Get_operation_to_smartfolder_global_object")
        data = {"name":"zones_and_record"}
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="smartfolder:global", fields=json.dumps(data))
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "zones_and_record" and i["comment"] == "asmsmortfolderinfoblo"
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")
 
    @pytest.mark.run(order=10)
    def test_10_Get_operation_to_smartfolder_global_object_with_name_field(self):
        logging.info("Get_operation_to_smartfolder_global_object")
        data = {"name":"zones_and_record"}
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="smartfolder:global", fields=json.dumps(data))
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "zones_and_record" and i["comment"] == "asmsmortfolderinfoblo"
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=11)
    def test_11_Get_operation_to_smartfolder_global_object_with_comment_field(self):
        logging.info("Get_operation_to_smartfolder_global_object")
        data = {"comment":"asmsmortfolderinfoblo"}
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="smartfolder:global", fields=json.dumps(data))
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "zones_and_record" and i["comment"] == "asmsmortfolderinfoblo"
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=12)
    def test_12_Get_operation_to_smartfolder_global_object_with_comment_field(self):
        logging.info("Get_operation_to_smartfolder_global_object")
        data = {"comment":"asmsmortfolderinfoblo"}
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="smartfolder:global", fields=json.dumps(data))
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "zones_and_record" and i["comment"] == "asmsmortfolderinfoblo"
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")	

    @pytest.mark.run(order=13)
    def test_13_Get_operation_to_smartfolder_global_object_with_comment_field(self):
        logging.info("Get_operation_to_smartfolder_global_object")
        data = {"comment":"asmsmortfolderinfoblo"}
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="smartfolder:global", fields=json.dumps(data))
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "zones_and_record" and i["comment"] == "asmsmortfolderinfoblo"
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=14)
    def test_14_Get_operation_to_smartfolder_global_object_with_comment_field(self):
        logging.info("Get_operation_to_smartfolder_global_object")
        data = {"comment":"asmsmortfolderinfoblo"}
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="smartfolder:global", fields=json.dumps(data))
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "zones_and_record" and i["comment"] == "asmsmortfolderinfoblo"
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")
    

    @pytest.mark.run(order=15)
    def test_15_smartfolder_global(self):
        logging.info("Create smartfolder:global with schedinfo.scheduled_time fields")
        data = { "comment":"amrt_globa","name":"global_testing_smartofolder1"}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=16)
    def test_16_Modify_the_smartfolder_global_object(self):
        logging.info("Modify_the_smartfolder_global_object")
        data = {"name": "SF_global"}
        response = ib_NIOS.wapi_request('PUT', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkem9uZXNfYW5kX3JlY29yZA:zones_and_record", fields=json.dumps(data))
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=17)
    def test_17_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "SF_global"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkZ2xvYmFsX3Rlc3Rpbmdfc21hcnRvZm9sZGVyMQ:global_testing_smartofolder1", fields=json.dumps(data))
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")


    

    @pytest.mark.run(order=18)
    def test_18_GET_operation_to_smartfolder_global_object(self):
        logging.info("GET_operation_to_smartfolder_global_object")
        get_smartfolder_global = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
        logging.info(get_smartfolder_global)
        res = json.loads(get_smartfolder_global)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")
        print res

    @pytest.mark.run(order=19)
    def test_19_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "SF_global"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkU0ZfZ2xvYmFs:SF_global", fields=json.dumps(data))
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")
		

    @pytest.mark.run(order=20)
    def test_20_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "global_testing_smartofolder"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkZ2xvYmFsX3Rlc3Rpbmdfc21hcnRvZm9sZGVy:global_testing_smartofolder", fields=json.dumps(data))
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")
		

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")
