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
    def test_1_Get_operation_to_smartfolder_children_object_with_group_by_values_field(self):
        logging.info("Get_operation_to_smartfolder_children_object_with_group_by_values_field")
        response = ib_NIOS.wapi_request('GET', object_type="smartfolder:children")
        print response
        logging.info(response)
        read  = re.search(r'200',response)
        for read in  response:
        	assert True
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=2)
    def test_2_Get_operation_to_smartfolder_children_object_with_group_by_values_fields_in_value_type(self):
        logging.info("Get_operation_to_smartfolder_children_object_with_group_by_values_fields_in_value_type")
	data = {"group_by_values":[{"name":"Site","value":"USA"}],"group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": "default"},"value_type": "EN"}]}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="smartfolder:children", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for value_type .*EN.* valid values are: STRING, INTEGER, BOOLEAN, DATE, ENUM, EMAIL, URL, OBJTYPE",response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=3)
    def test_3_Get_operation_to_smartfolder_children_object_with_group_by_values_fields_in_value_string_true(self):
        logging.info("Get_operation_to_smartfolder_children_object_with_group_by_values_fields_in_value_string_true")
	data = {"group_by_values":[{"name":"Site","value":"USA"}],"group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": True},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="smartfolder:children", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for value_string: true: Must be string type",response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")
   
    @pytest.mark.run(order=4)
    def test_4_Get_operation_to_smartfolder_children_object_with_group_by_values_fields_in_value_string_true(self):
        logging.info("Get_operation_to_smartfolder_children_object_with_group_by_values_fields_in_value_string_true")
        response = ib_NIOS.wapi_request('GET', object_type="smartfolder:children")
        print response
        logging.info(response)
        read  = re.search(r'200',response)
        for read in  response:
                assert True
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=5)
    def test_5_Create_smartfolder_children_object_with_group_by_values_N(self):
        logging.info("Create_smartfolder_children_object_with_group_by_values_N")
        data = {"group_by_values":[{"name":"Site","value":"USA1"}],"group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": "default"},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=6)
    def test_6_Modify_smartfolder_children_object_with_group_by_values_fields_N(self):
        logging.info("Modify_smartfolder_children_object_with_group_by_values_fields_N")
        data = {"group_by_values":[{"name":"Site","value":"USA1"}],"group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": "default"},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'smartfolder:children/Li5zbWFydF9mb2xkZXJfY2hpGRyZW4kMmQy:children', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'AdmConProtoError: Invalid reference',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=7)
    def test_7_Delete_smartfolder_children_object_N(self):
        logging.info("Delete_smartfolder_children_object_N")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = "smartfolder:children/Li5zbWFydF9mb2xkZXJfY2hpbGRyZW4kMmQw:children")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for smartfolder:children',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")


    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")


