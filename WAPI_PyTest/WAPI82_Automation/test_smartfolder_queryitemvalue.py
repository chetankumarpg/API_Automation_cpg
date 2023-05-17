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
    def test_1_GET_operation_to_smartfolder_personal_object(self):
        logging.info("GET_operation_to_smartfolder_personal_object")
        get_smartfolder_personal = ib_NIOS.wapi_request('GET', object_type="smartfolder:personal")
        logging.info(get_smartfolder_personal)
        res = json.loads(get_smartfolder_personal)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")
        print res
   
    @pytest.mark.run(order=2)
    def test_2_Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_integer(self):
        logging.info("Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_integer")
        data = {"name":"Active Directory Sites123","query_items":[{"field_type":"NORMAL","name":"type","op_match":True,"operator":"EQ","value":{"value_string": "MsAdSitesSite","value_boolean":True,"value_integer":12},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=3)
    def test_3_Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_integer_N(self):
        logging.info("Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_integer_N")
        data = {"name":"Active Directory Sites123","query_items":[{"field_type":"NORMAL","name":"type","op_match":True,"operator":"EQ","value":{"value_string": "MsAdSitesSite","value_boolean":True,"value_integer":"abc"},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for value_integer.*.* Must be integer type',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=4)
    def test_4_Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_string(self):
        logging.info("Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_string")
        data = {"name":"Active Directory Sites","query_items":[{"field_type":"NORMAL","name":"type","op_match":True,"operator":"EQ","value":{"value_string": "MsAdSitesSite","value_boolean":True,"value_integer":12},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=5)
    def test_5_Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_string_N(self):
        logging.info("Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_string_N")
        data = {"name":"Active Directory Sites","query_items":[{"field_type":"NORMAL","name":"type","op_match":True,"operator":"EQ","value":{"value_string": "MsAdSitesSite_folder","value_boolean":True,"value_integer":12},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid value MsAdSitesSite_folder for field type of type ENUM',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=6)
    def test_6_Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_boolean(self):
        logging.info("Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_boolean")
        data = {"name":"Active Directory Sites22","query_items":[{"field_type":"NORMAL","name":"type","op_match":True,"operator":"EQ","value":{"value_string": "MsAdSitesSite","value_boolean":True,"value_integer":12},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=7)
    def test_7_Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_boolean_N(self):
        logging.info("Create_smartfolder_personal_object_with_query_itemvalue_field_in_value_boolean_N")
        data = {"name":"Active Directory Sites22","query_items":[{"field_type":"NORMAL","name":"type","op_match":True,"operator":"EQ","value":{"value_string": "MsAdSitesSite","value_boolean":"","value_integer":12},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid value for value_boolean: .*.*: Must be boolean type',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")
  

    @pytest.mark.run(order=8)
    def test_8_Modify_smartfolder_personal_object_with_query_itemvalue_field_in_value_date_N(self):
        logging.info("Modify_smartfolder_personal_object_with_query_itemvalue_field_in_value_date_N")
        data = {"query_items": [{"field_type": "NORMAL","name": "type","op_match": True,"operator": "EQ","value": {"value_string": "MsAdSitesSite","value_boolean":True,"value_integer":123,"value_date":""},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5BY3RpdmUgRGlyZWN0b3J5IFNpdGVzMjI:Active%20Directory%20Sites22/false', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'.Error converting argument value_date: Invalid value, must be an integer between 0 and 4294967295',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=9)
    def test_9_Modify_smartfolder_personal_object_with_query_itemvalue_field_in_value_date(self):
        logging.info("Modify_smartfolder_personal_object_with_query_itemvalue_field_in_value_date")
        data = {"query_items": [{"field_type": "NORMAL","name": "type","op_match": True,"operator": "EQ","value": {"value_string": "MsAdSitesSite","value_boolean":True,"value_integer":123,"value_date":4294967294},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('PUT',ref='smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5BY3RpdmUgRGlyZWN0b3J5IFNpdGVzMjI:Active%20Directory%20Sites22/false',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response

    @pytest.mark.run(order=10)
    def test_10_DELETE_the_smartfolder_personal_object_with_query_itemvalue_field(self):
        logging.info("DELETE_the_smartfolder_personal_object_with_query_itemvalue_field")
        data = {"name": "Active%20Directory%20Sites/false"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5BY3RpdmUgRGlyZWN0b3J5IFNpdGVz:Active%20Directory%20Sites/false", fields=json.dumps(data))
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=11)
    def test_11_DELETE_the_smartfolder_personal_object_with_query_itemvalue_field(self):
        logging.info("DELETE_the_smartfolder_personal_object_with_query_itemvalue_field")
        data = {"name": "Active%20Directory%20Sites123/false"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:personal",ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5BY3RpdmUgRGlyZWN0b3J5IFNpdGVzMTIz:Active%20Directory%20Sites123/false", fields=json.dumps(data))
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=12)
    def test_12_DELETE_the_smartfolder_personal_object_with_query_itemvalue_field(self):
        logging.info("DELETE_the_smartfolder_personal_object_with_query_itemvalue_field")
        data = {"name": "Active%20Directory%20Sites22/false"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:personal",ref="smartfolder:personal/Li5teV9wZXJzb25hbFzbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5BY3RpdmUgRGlyZWN0b3J5IFNpdGVzMjI:Active%20Directory%20Sites22/false", fields=json.dumps(data))
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=13)
    def test_13_DELETE_the_smartfolder_personal_object_with_query_itemvalue_field(self):
        logging.info("DELETE_the_smartfolder_personal_object_with_query_itemvalue_field")
        data = {"name": "Active%20Directory%20Sites22/false"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:personal",ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5BY3RpdmUgRGlyZWN0b3J5IFNpdGVzMjI:Active%20Directory%20Sites22/false", fields=json.dumps(data))
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")
		

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")


