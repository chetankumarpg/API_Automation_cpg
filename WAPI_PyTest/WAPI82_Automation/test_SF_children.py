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
    def test_1_GET_operation_to_smartfolder_children_object(self):
        logging.info("GET_operation_to_smartfolder_children_object")
        get_smartfolder_children = ib_NIOS.wapi_request('GET', object_type="smartfolder:children")
        logging.info(get_smartfolder_children)
        res = json.loads(get_smartfolder_children)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")
        print res


    @pytest.mark.run(order=2)
    def test_2_Create_smartfolder_children_object_with_name_and_comment_N(self):
        logging.info("Create_smartfolder_children_object_with_name_and_comment_N")
        data = {"name": "domain.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=3)
    def test_3_Modify_smrtfolder_children_object_for_dns_name_fields_N(self):
        logging.info("Modify_smrtfolder_children_object_for_dns_name_fields_N")
        data = {"dns_name": "subzone.domain.com"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'smartfolder:children/Li5zbWFydF9mb2xkZXJfY2hpbGRyZW4kMTQw:children', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation update not allowed for smartfolder:children',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=4)
    def test_4_Delete_smartfolder_children_object_N(self):
        logging.info("Delete_smartfolder_children_object_N")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = 'smartfolder:children/Li5zbWFydF9mb2xkZXJfY2hpbGRyZW4kMTNm:children')
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for smartfolder:children',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=5)
    def test_5_smartfolder_children_object_global_search_fields_with_search_string_value_string(self):
               logging.info("GET_smartfolder_children_object_global_search_fields_with_search_string_value_string")
               data = {"value_string": "10.0.0.0/8"}
               response = ib_NIOS.wapi_request('GET',object_type="search",params="?search_string=value_string")
               print response
               logging.info(response)
               read  = re.search(r'200',response)
               for read in  response:
                       assert True
               logging.info("Test Case 5 Execution Completed")
               logging.info("=============================")


    @pytest.mark.run(order=6)
    def test_6_Create_smartfolder_children_object_with_resource_value_string_and_value_type_fields_scheduled_N(self):
        logging.info("Create_smartfolder_children_object_with_resource_value_string_and_value_type_fields_scheduled_N")
        data = {"resource":"grid:servicerestart:group/b25lLnJlc3RhcnRfZ3JvdXAkLmNvbS5pbmZvYmxveC5kbnMuY2x1c3Rlcl9kbnNfcHJvcGVydGllcyQwLkRlZmF1bHQgRE5T:Default%20DNS","value":{"value_string": "Default DNS"},"value_type": "STRING"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=7)
    def test_7_Adding_csvexport_field_in_the_smartfolder_children_object_N(self):
        logging.info("Perform_Adding_csvexport_field_in_the_smartfolder_children_object_N")
        data = {"_object":"smartfolder:children"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'smartfolder:children objects do not support CSV export',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=8)
    def test_8_GET_operation_to_smartfolder_children_object_with_value_value_type_and_resource_fields(self):
        logging.info("GET_operation_to_smartfolder_children_object_with_value_value_type_and_resource_fields")
        get_smartfolder_children = ib_NIOS.wapi_request('GET', object_type="smartfolder:children")
        logging.info(get_smartfolder_children)
        res = json.loads(get_smartfolder_children)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")
        print res


    @pytest.mark.run(order=9)
    def test_9_Search_operation_to_smartfolder_children_object_with_resource_N(self):
        logging.info("Search_operation_to_smartfolder_children_object_with_resource_N")
        data={"resource":"grid:servicerestart:group/b25lLnJlc3RhcnRfZ3JvdXAkLmNvbS5pbmZvYmxveC5kbnMuY2x1c3Rlcl9kbnNfcHJvcGVydGllcyQwLkRlZmF1bHQgRE5T:Default%20DNS"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="smartfolder:children", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: resource',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=10)
    def test_10_Search_operation_to_smartfolder_children_object_with_value_N(self):
        logging.info("Search_operation_to_smartfolder_children_object_with_value_N")
        data={"value":{"value_string": "Default DNS"}}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="smartfolder:children", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: value',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")
		
		
		
    @pytest.mark.run(order=11)
    def test_11_Search_operation_to_smartfolder_children_object_with_value_type_N(self):
        logging.info("Search_operation_to_smartfolder_children_object_with_value_type_N")
        data={"value_type":"STRING"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="smartfolder:children", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: value_type',response1)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")		
  
    @pytest.mark.run(order=12)
    def test_12_Create_smartfolder_children_object_with_value_type_BOOLEAN_N(self):
        logging.info("Create_smartfolder_children_object_with_value_type_BOOLEAN_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "BOOLEAN"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")


	
    @pytest.mark.run(order=13)
    def test_13_Create_smartfolder_children_object_with_query_items_operator_value_type_DATE_N(self):
        logging.info("create_smartfolder_children_object_with_query_items_operator_value_type_DATE_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "DATE"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=14)
    def test_14_Create_smartfolder_children_object_with_query_items_operator_value_type_EMAIL_N(self):
        logging.info("create_smartfolder_children_object_with_query_items_operator_value_type_EMAIL_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "EMAIL"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=15)
    def test_15_Create_smartfolder_children_object_with_query_items_operator_value_type_ENUM_N(self):
        logging.info("create_smartfolder_children_object_with_query_items_operator_value_type_ENUM_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")

		

    @pytest.mark.run(order=16)
    def test_16_Create_smartfolder_children_object_with_query_items_operator_value_type_OBJTYPE_N(self):
        logging.info("create_smartfolder_children_object_with_query_items_operator_value_type_OBJTYPE_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "OBJTYPE"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=17)
    def test_17_Create_smartfolder_children_object_with_query_items_operator_value_type_URL_N(self):
        logging.info("create_smartfolder_children_object_with_query_items_operator_value_type_URL_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "URL"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=18)
    def test_18_Create_smartfolder_children_object_with_query_itemvalue_field_in_value_integer_N(self):
        logging.info("Create_smartfolder_children_object_with_query_itemvalue_field_in_value_integer_N")
        data = {"name":"Active Directory Sites123","query_items":[{"field_type":"NORMAL","name":"type","op_match":True,"operator":"EQ","value":{"value_string": "MsAdSitesSite","value_boolean":True,"value_integer":"abc"},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=19)
    def test_19_Create_smartfolder_children_object_with_query_itemvalue_field_in_value_string_N(self):
        logging.info("Create_smartfolder_children_object_with_query_itemvalue_field_in_value_string_N")
        data = {"name":"Active Directory Sites","query_items":[{"field_type":"NORMAL","name":"type","op_match":True,"operator":"EQ","value":{"value_string": "MsAdSitesSite","value_boolean":True,"value_integer":12},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=20)
    def test_20_Get_operation_to_smartfolder_children_object_with_group_by_values_field(self):
        logging.info("Get_operation_to_smartfolder_children_object_with_group_by_values_field")
        data = {"group_by_values":[{"name":"Site","value":"USA"}],"group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"query_items": [{"field_type": "NORMAL","name": "network_view","op_match": "Yes","operator": "EQ","value": {"value_string": "default"},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="smartfolder:children", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"AdmConProtoError: Invalid value for op_match:",response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=21)
    def test_21_Get_operation_to_smartfolder_children_object_with_group_by_values_fields_in_value_string_true(self):
        logging.info("Get_operation_to_smartfolder_children_object_with_group_by_values_fields_in_value_string_true")
        data = {"group_by_values":[{"name":"Site","value":"USA"}],"group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": True},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="smartfolder:children", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for value_string: true: Must be string type",response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=22)
    def test_22_Create_smartfolder_children_object_with_group_by_values_N(self):
        logging.info("Create_smartfolder_children_object_with_group_by_values_N")
        data = {"group_by_values":[{"name":"Site","value":"USA1"}],"group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": "default"},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=23)
    def test_23_Create_smartfolder_children_object_with_name_and_comment_N(self):
        logging.info("Create_smartfolder_children_object_with_name_and_comment_N")
        data = {"name": "global_testing_smartofolder55","group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:children",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for smartfolder:children',response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")
				
		

    @pytest.mark.run(order=24)
    def test_24_group_bys_filed_with_search_smartfolder_children_object(self):
        logging.info("Search operation group_bys_filed_with_search_smartfolder_children_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="smartfolder:children", params="?group_bys=NORMAL")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r".*query_items.* is required when grouping arguments are given .*group_bys.*, .*group_by_values.*.",response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=25)
    def test_25_Get_operation_to_smartfolder_children_object_with_smart_folder_fields_N(self):
        logging.info("Get_operation_to_smartfolder_children_object_with_smart_folder_fields_N")
        data = {"smart_folder":"global_testing"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="smartfolder:children", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid reference: global_testing",response1)
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")




    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")


