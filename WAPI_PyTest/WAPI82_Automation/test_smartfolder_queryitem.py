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
    def test_1_GET_operation_to_smartfolder_global_object_with_query_items(self):
        logging.info("GET_operation_to_smartfolder_global_object_with_query_items ")
        get_smartfolder_global = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
        logging.info(get_smartfolder_global)
        res = json.loads(get_smartfolder_global)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")
        print res
 

    @pytest.mark.run(order=2)
    def test_2_smartfolder_global_with_query_items_field_type_EXTATTR(self):
        logging.info("Create smartfolder:global with query_itemsquery_items_field_type_EXTATTR")
        data = {"name":"testing1","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "STRING"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=3)
    def test_3_smartfolder_global_with_query_items_field_type_NORMAL(self):
        logging.info("Create smartfolder:global with query_itemsquery_items_field_type_NORMAL")
        data = {"name":"Smart Folder1","query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value":{"value_string": "default"},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=4)
    def test_4_smartfolder_global_with_query_items_operator_EQ(self):
        logging.info("Create smartfolder:global with query_itemsquery_items_operator_EQ")
        data = {"name":"Smart Folder1","query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value":{"value_string": "default"},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=5)
    def test_5_smartfolder_global_with_query_items_operator_BEGINS_WITH(self):
        logging.info("Create smartfolder:global with query_itemsquery_items_operator_BEGINS_WITH")
        data = {"name":"testing3","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "BEGINS_WITH","value": {"value_string": "bang"},"value_type": "STRING"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        logging.info("============================")
        print response
		

    @pytest.mark.run(order=6)
    def test_6_smartfolder_global_with_query_items_operator_HAS_VALUE(self):
        logging.info("Create smartfolder:global with query_itemsquery_items_operator_HAS_VALUE")
        data = {"name":"testing2","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "HAS_VALUE","value": {"value_string": "bang"},"value_type": "STRING"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        logging.info("============================")
        print response
		
    @pytest.mark.run(order=7)
    def test_7_Create_smartfolder_global_object_with_query_items_operator_GT_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_GT_N")
	data = {"name":"SF2","query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "GT","value":{"value_string": "default"},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*IS GT.* for field .*network_view.*',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=8)
    def test_8_Create_smartfolder_global_object_with_query_items_operator_GEQ_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_GEQ_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "GEQ","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*IS NOT GEQ.* for ext attrs field .*Site.*',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=9)
    def test_9_Create_smartfolder_global_object_with_query_items_operator_GEQ_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_GEQ_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "LT","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*IS NOT LT.* for ext attrs field .*Site.*',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")

	
    @pytest.mark.run(order=10)
    def test_10_Create_smartfolder_global_object_with_query_items_operator_GEQ_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_GEQ_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "LEQ","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*IS NOT LEQ.* for ext attrs field .*Site.*',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=11)
    def test_11_Create_smartfolder_global_object_with_query_items_operator_ENDS_WITH_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_ENDS_WITH_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "ENDS_WITH","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*DOES NOT ENDS_WITH.* for ext attrs field .*Site.*',response1)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")
	

    @pytest.mark.run(order=12)
    def test_12_Create_smartfolder_global_object_with_query_items_operator_CONTAINS_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_CONTAINS_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "CONTAINS","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*DOES NOT CONTAINS.* for ext attrs field .*Site.*',response1)
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=13)
    def test_13_Create_smartfolder_global_object_with_query_items_operator_RELATIVE_DATE_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_RELATIVE_DATE_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "RELATIVE_DATE","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*DOES NOT RELATIVE_DATE.* for ext attrs field .*Site.*',response1)
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")	
		

    @pytest.mark.run(order=14)
    def test_14_Create_smartfolder_global_object_with_query_items_operator_RISES_BY_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_RISES_BY_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "RISES_BY","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*DOES NOT RISES_BY.* for ext attrs field .*Site.*',response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=15)
    def test_15_Create_smartfolder_global_object_with_query_items_operator_DROPS_BY_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_DROPS_BY_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "DROPS_BY","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*DOES NOT DROPS_BY.* for ext attrs field .*Site.*',response1)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=16)
    def test_16_Create_smartfolder_global_object_with_query_items_operator_INHERITANCE_STATE_EQUALS_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_INHERITANCE_STATE_EQUALS_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "INHERITANCE_STATE_EQUALS","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Inheritance state value must be in .*OVERRIDDEN.*,.*INHERITED.*',response1)
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=17)
    def test_17_Create_smartfolder_global_object_with_query_items_operator_IP_ADDR_WITHIN_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_IP_ADDR_WITHIN_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "IP_ADDR_WITHIN","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*DOES NOT IP_ADDR_WITHIN.* for ext attrs field .*Site.*',response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")
	
		
    @pytest.mark.run(order=18)
    def test_18_Create_smartfolder_global_object_with_query_items_operator_SUFFIX_MATCH_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_SUFFIX_MATCH_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "SUFFIX_MATCH","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*DOES NOT SUFFIX_MATCH.* for ext attrs field .*Site.*',response1)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")
		
		
		
    @pytest.mark.run(order=19)
    def test_19_Create_smartfolder_global_object_with_query_items_operator_MATCH_EXPR_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_MATCH_EXPR_N")
	data = {"name":"testing4","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "MATCH_EXPR","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid operator .*DOES NOT MATCH_EXPR.* for ext attrs field .*Site.*',response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")
				

    @pytest.mark.run(order=20)
    def test_20_Create_smartfolder_global_object_with_query_items_operator_Eq_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_Eq_N")
        data = {"name":"testing1","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "Eq","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid value for operator .*Eq.* valid values are: EQ, GT, GEQ, LT, LEQ, HAS_VALUE, BEGINS_WITH, ENDS_WITH, CONTAINS, RELATIVE_DATE, RISES_BY, DROPS_BY, INHERITANCE_STATE_EQUALS, IP_ADDR_WITHIN, SUFFIX_MATCH, MATCH_EXPR',response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")	

    @pytest.mark.run(order=21)
    def test_21_Create_smartfolder_global_object_with_query_items_operator_op_match_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_op_match_N")
        data = {"name":"testing1","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": "","operator": "EQ","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('.*Invalid value for op_match: .*.*: Must be boolean type.*',response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")
	
    @pytest.mark.run(order=22)
    def test_22_smartfolder_global_with_query_items_value_type_STRING(self):
        logging.info("Create smartfolder:global with query_itemsquery_items_value_type_STRING")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "STRING"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=23)
    def test_23_Create_smartfolder_global_object_with_query_items_operator_value_type_INTEGER_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_value_type_INTEGER_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "INTEGER"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*INTEGER, STRING.*',response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")
	


    @pytest.mark.run(order=24)
    def test_24_Create_smartfolder_global_object_with_query_items_operator_value_type_BOOLEAN_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_value_type_BOOLEAN_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "BOOLEAN"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*BOOLEAN, STRING.*',response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=25)
    def test_25_Create_smartfolder_global_object_with_query_items_operator_value_type_DATE_N(self):
        
        logging.info("create_smartfolder_global_object_with_query_items_operator_value_type_DATE_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "DATE"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*DATE, STRING.*',response1)
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=26)
    def test_26_Create_smartfolder_global_object_with_query_items_operator_value_type_ENUM_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_value_type_ENUM_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*ENUM, STRING.*',response1)
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=27)
    def test_27_Create_smartfolder_global_object_with_query_items_operator_value_type_EMAIL_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_value_type_EMAIL_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "EMAIL"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*EMAIL, STRING.*',response1)
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=28)
    def test_28_Create_smartfolder_global_object_with_query_items_operator_value_type_URL_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_value_type_URL_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "URL"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*URL, STRING.*',response1)
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=29)
    def test_29_Create_smartfolder_global_object_with_query_items_operator_value_type_OBJTYPE_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_value_type_OBJTYPE_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "OBJTYPE"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*OBJTYPE, STRING.*',response1)
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=30)
    def test_30_Create_smartfolder_global_object_with_query_items_operator_value_type_STRING_N(self):
        logging.info("create_smartfolder_global_object_with_query_items_operator_value_type_STRING_N")
        data = {"name":"testing11","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": 1234},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:global",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for value_string: 1234: Must be string type',response1)
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")
   


    @pytest.mark.run(order=31)
    def test_31_modify_smrtfolder_global_object_for_query_items_fields(self):
        logging.info("modify_smrtfolder_global_object_for_query_items_fields")
        data = {"query_items":[{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "STRING"}]}
        response = ib_NIOS.wapi_request('PUT',ref='smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkdGVzdGluZzk5:testing99',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=32)
    def test_32_Modify_smrtfolder_global_object_for_query_items_fields_N(self):
        logging.info("Modify_smrtfolder_global_object_for_query_items_fields_N")
        data = {"query_items": [{"field_type": "NORMAL","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkdGVzdGluZzI:testing2', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'.*Site.* is not a valid query item nor an existing extensible attribute.',response1)
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")


	
    @pytest.mark.run(order=33)
    def test_33_GET_operation_to_smartfolder_global_object_with_query_items(self):
        logging.info("GET_operation_to_smartfolder_global_object_with_query_items ")
        get_smartfolder_global = ib_NIOS.wapi_request('GET', object_type="smartfolder:global")
        logging.info(get_smartfolder_global)
        res = json.loads(get_smartfolder_global)
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")
        print res

        
    @pytest.mark.run(order=34)
    def test_34_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "global_testing_smartofolder"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydFmb2xkZXIkU21hcnQgRm9sZGVyMQ:Smart%20Folder1", fields=json.dumps(data))
        logging.info("Test Case 34 Execution Completed")
        logging.info("============================")
    
    @pytest.mark.run(order=35)
    def test_35_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "global_testing_smartofolder"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydFmb2xkZXIkU21hcnQgRm9sZGVyMQ:Smart%20Folder1", fields=json.dumps(data))
        logging.info("Test Case 35 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=36)
    def test_36_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "global_testing_smartofolder"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkdGVzdGluZzE:testing1", fields=json.dumps(data))
        logging.info("Test Case 36 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=37)
    def test_37_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "global_testing_smartofolder"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkU21hcnQgRm9sZGVyMQ:Smart%20Folder1", fields=json.dumps(data))
        logging.info("Test Case 37 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=38)
    def test_38_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "global_testing_smartofolder"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkdGVzdGluZzM:testing3", fields=json.dumps(data))
        logging.info("Test Case 38 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=39)
    def test_39_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "global_testing_smartofolder"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkdGVzdGluZzI:testing2", fields=json.dumps(data))
        logging.info("Test Case 39 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=40)
    def test_40_DELETE_the_smartfolder_global_object(self):
        logging.info("DELETE_the_smartfolder_global_object")
        data = {"name": "global_testing_smartofolder"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:global/b25lLmdsb2JhbF9zbWFydF9mb2xkZXIkdGVzdGluZzk5:testing99", fields=json.dumps(data))
        logging.info("Test Case 40 Execution Completed")
        logging.info("============================")


    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")
