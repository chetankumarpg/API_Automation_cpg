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
    def test_1_get_smartfolder_global(self):
        logging.info("Get the smartfolder:global defaults fields ")
        get_smartfolder_global = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
        logging.info(get_smartfolder_global)
        res = json.loads(get_smartfolder_global)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")
        print res


    @pytest.mark.run(order=2)
    def test_2_smartfolder_global_with_group_bys(self):
        logging.info("Create smartfolder:global with group_bys object")
        data = {"name": "global_testing_smartofolder55","group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=3)
    def test_3_group_bys_filed_with_search_smartfolder_global_object(self):
        logging.info("Search operation group_bys_filed_with_search_smartfolder_global_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="smartfolder:global", params="?group_bys=NORMAL")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: group_bys",response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=4)
    def test_4_smartfolder_global_with_group_bys(self):
        logging.info("Create smartfolder:global with group_bys object")
        data = { "comment": "samrt_global","group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"name": "global_testing_smartofolder","query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": "default"},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=5)
    def test_5_modify_smrtfolder_global_object_for_group_bys_fields(self):
        logging.info("modify_smrtfolder_global_object_for_group_bys_fields")
        data = { "comment": "samrt_global","group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"name": "global_testing_smartofolder","query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": "default"},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('PUT',ref='smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkZ2xvYmFsX3Rlc3Rpbmdfc21hcnRvZm9sZGVy:global_testing_smartofolder',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response
    
    @pytest.mark.run(order=6)
    def test_6_modify_smrtfolder_global_object_for_group_bys_fields_NORMAL(self):
        logging.info("modify_smrtfolder_global_object_for_group_bys_fields_NORMAL")
        data = {"group_bys": [{"enable_grouping": True,"value": "site","value_type": "NORMAL"}]}
        response = ib_NIOS.wapi_request('PUT',ref='smrtfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkU21hcnQgRm9sZGVyIEc:Smart%20Folder%20G',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response

    @pytest.mark.run(order=7)
    def test_7_modify_smrtfolder_global_object_for_group_bys_fields_EXTATTR(self):
        logging.info("modify_smrtfolder_global_object_for_group_bys_fields_EXTATTR")
        data = {"group_bys": [{"enable_grouping": True,"value":  "State","value_type": "EXTATTR"}]}
        response = ib_NIOS.wapi_request('PUT',ref='smrtfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkU21hcnQgRm9sZGVyIEc:Smart%20Folder%20G',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=8)
    def test_8_Modify_smrtfolder_global_object_for_group_bys_fields_normal(self):
        logging.info("Modify_smrtfolder_global_object_for_group_bys_fields_normal")
        data = {"group_bys": [{"enable_grouping": True,"value": "Site","value_type": "normal"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkZ2xvYmFsX3Rlc3Rpbmdfc21hcnRvZm9sZGVy:global_testing_smartofolder", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for value_type .*normal.* valid values are: NORMAL, EXTATTR',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=9)
    def test_9_get_smartfolder_global(self):
        logging.info("Get the smartfolder:global defaults fields ")
        get_smartfolder_global = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
        logging.info(get_smartfolder_global)
        res = json.loads(get_smartfolder_global)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")
	print res


    @pytest.mark.run(order=10)
    def test_10_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "global_testing_smartofolder"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkZ2xvYmFsX3Rlc3Rpbmdfc21hcnRvZm9sZGVyNTU:global_testing_smartofolder55", fields=json.dumps(data))
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=11)
    def test_11_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "global_testing_smartofolder"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkZ2xvYmFsX3Rlc3Rpbmdfc21hcnRvZm9sZGVy:global_testing_smartofolder", fields=json.dumps(data))
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")



    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")


