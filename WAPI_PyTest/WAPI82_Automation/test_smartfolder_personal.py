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
    def test_2_create_the_smartfolder_personal_object_with_name_and_comment(self):
        logging.info("create_the_smartfolder_personal_object_with_name_and_comment")
        data = { "comment":"folder_wapi","name":"Smart_personal_folder_wapi"}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=3)
    def test_3_create_the_smartfolder_personal_object_with_all_required_fields(self):
        logging.info("create_the_smartfolder_personal_object_with_all_required_fields")
        data = { "comment": "Smart_personal_folder_wapi","group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"name": "Smart_personal_folder_wapi7","query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": "default"},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        logging.info("============================")
        print response



    @pytest.mark.run(order=4)
    def test_4_create_the_smartfolder_personal_object_with_all_required_fields_N(self):
        logging.info("4_create_the_smartfolder_personal_object_with_all_required_fields_N")
        data = {"comment":"folder_wapi","name":"Smart_personal_folder_wapi","is_shortcut":False}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Field is not writable: is_shortcut',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")
                       


    @pytest.mark.run(order=5)
    def test_5_create_the_smartfolder_personal_object_with_csvexport_fields_N(self):
        logging.info("create_the_smartfolder_personal_object_with_csvexport_fields_N")
        data = {"_object":"smartfolder:personal"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'smartfolder:personal objects do not support CSV export.',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")





    @pytest.mark.run(order=6)
    def test_6_GET_operation_to_smartfolder_personal_object_with_Global_search_N(self):
        logging.info("GET_operation_to_smartfolder_personal_object_with_Global_search_N")
        get_smartfolder_personal = ib_NIOS.wapi_request('GET', object_type="smartfolder:personal")
        logging.info(get_smartfolder_personal)
        res = json.loads(get_smartfolder_personal)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")
        print res
	
    @pytest.mark.run(order=7)
    def test_7_Create_smartfolder_personal_with_schedinfo_scheduled_time_fields(self):
        logging.info("Create_smartfolder_personal_with_schedinfo_scheduled_time_fields")
        data = {"comment":"ps_folder","name":"Smart_personal_folder2"}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        logging.info("============================")
        print response
		

		
    @pytest.mark.run(order=8)
    def test_8_Adding_smartfolder_personal_with_name_comment_is_shortcut_N(self):
        logging.info("Adding_smartfolder_personal_with_name_comment_is_shortcut_N")
        data = {"comment":"folder_wapi","name":"Smart_personal_folder_wapi","is_shortcut":False}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Field is not writable: is_shortcut',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=9)
    def test_9_Adding_smartfolder_personal_with_name_and_comment_fields(self):
        logging.info("Adding_smartfolder_personal_with_name_and_comment_fields")
        data = {"comment":"folder_wapi","name":"Smart_personal_folder_wapi"}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=10)
    def test_10_Adding_smartfolder_personal_with_name_group_bys_query_items_and_comment_fields(self):
        logging.info("Adding_smartfolder_personal_with_name_group_bys_query_items_and_comment_fields")
        data = { "comment": "Smart_personal_folder_wapi","group_bys": [{"enable_grouping": True,"value": "Site","value_type": "EXTATTR"}],"name": "Smart_personal_folder_wapi7","query_items": [{"field_type": "NORMAL","name": "network_view","op_match": True,"operator": "EQ","value": {"value_string": "default"},"value_type": "ENUM"}]}
        response = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=11)
    def test_11_GET_operation_to_smartfolder_personal_object_with_name_group_bys_comment_query_items_is_shortcut(self):
        logging.info("GET_operation_to_smartfolder_personal_object_with_name_group_bys_comment_query_items_is_shortcut")
        get_smartfolder_personal = ib_NIOS.wapi_request('GET', object_type="smartfolder:personal")
        logging.info(get_smartfolder_personal)
        res = json.loads(get_smartfolder_personal)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")
        print res


    @pytest.mark.run(order=12)
    def test_12_Search_operation_to_smartfolder_personal_object_in_name_filed_with_Smart_personal_folder2(self):
        logging.info("Search_operation_to_smartfolder_personal_object_in_name_filed_with_Smart_personal_folder2")
        smartfolder_personal = ib_NIOS.wapi_request('GET', object_type='smartfolder:personal', params="?name=Smart_personal_folder2")
        res = json.loads(smartfolder_personal)
        print res
        for i in res:
           assert  i["name"] == "Smart_personal_folder2" and i["is_shortcut"] == False and i["comment"] == "ps_folder"
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=13)
    def test_13_Search_operation_to_smartfolder_personal_object_in_name_filed_with_Smart_personal_folder2(self):
        logging.info("Search_operation_to_smartfolder_personal_object_in_name_filed_with_Smart_personal_folder2")
        smartfolder_personal = ib_NIOS.wapi_request('GET', object_type='smartfolder:personal', params="?name:=Smart_personal_folder2")
        res = json.loads(smartfolder_personal)
        print res
        for i in res:
           assert  i["name"] == "Smart_personal_folder2" and i["is_shortcut"] == False and i["comment"] == "ps_folder"
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")	

    @pytest.mark.run(order=14)
    def test_14_Search_operation_to_smartfolder_personal_object_in_name_filed_with_Smart_personal_folder2(self):
        logging.info("Search_operation_to_smartfolder_personal_object_in_name_filed_with_Smart_personal_folder2")
        smartfolder_personal = ib_NIOS.wapi_request('GET', object_type='smartfolder:personal', params="?name~=Smart_personal_folder2")
        res = json.loads(smartfolder_personal)
        print res
        for i in res:
           assert  i["name"] == "Smart_personal_folder2" and i["is_shortcut"] == False and i["comment"] == "ps_folder"
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=15)
    def test_15_Search_operation_to_smartfolder_personal_object_in_name_filed_with_Smart_personal_folder2(self):
        logging.info("Search_operation_to_smartfolder_personal_object_in_name_filed_with_Smart_personal_folder2")
        smartfolder_personal = ib_NIOS.wapi_request('GET', object_type='smartfolder:personal', params="?name~:=Smart_personal_folder2")
        res = json.loads(smartfolder_personal)
        print res
        for i in res:
           assert  i["name"] == "Smart_personal_folder2" and i["is_shortcut"] == False and i["comment"] == "ps_folder"
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=16)
    def test_16_Search_operation_to_smartfolder_personal_object_in_comment_filed_with_ps_folder(self):
        logging.info("Search_operation_to_smartfolder_personal_object_in_comment_filed_with_ps_folder")
        smartfolder_personal = ib_NIOS.wapi_request('GET', object_type='smartfolder:personal', params="?comment~:=ps_folder")
        res = json.loads(smartfolder_personal)
        print res
        for i in res:
           assert  i["comment"] == "ps_folder" and i["is_shortcut"] == False and i["name"] == "Smart_personal_folder2"
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=17)
    def test_17_Search_operation_to_smartfolder_personal_object_in_comment_filed_with_ps_folder(self):
        logging.info("Search_operation_to_smartfolder_personal_object_in_comment_filed_with_ps_folder")
        smartfolder_personal = ib_NIOS.wapi_request('GET', object_type='smartfolder:personal', params="?comment~:=ps_folder")
        res = json.loads(smartfolder_personal)
        print res
        for i in res:
           assert  i["comment"] == "ps_folder" and i["is_shortcut"] == False and i["name"] == "Smart_personal_folder2"
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")	

    @pytest.mark.run(order=18)
    def test_18_Search_operation_to_smartfolder_personal_object_in_comment_filed_with_ps_folder(self):
        logging.info("Search_operation_to_smartfolder_personal_object_in_comment_filed_with_ps_folder")
        smartfolder_personal = ib_NIOS.wapi_request('GET', object_type='smartfolder:personal', params="?comment~=ps_folder")
        res = json.loads(smartfolder_personal)
        print res
        for i in res:
           assert  i["comment"] == "ps_folder" and i["is_shortcut"] == False and i["name"] == "Smart_personal_folder2"
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")	
		

    @pytest.mark.run(order=19)
    def test_19_Search_operation_to_smartfolder_personal_object_in_comment_filed_with_ps_folder(self):
        logging.info("Search_operation_to_smartfolder_personal_object_in_comment_filed_with_ps_folder")
        smartfolder_personal = ib_NIOS.wapi_request('GET', object_type='smartfolder:personal', params="?comment~:=ps_folder")
        res = json.loads(smartfolder_personal)
        print res
        for i in res:
           assert  i["comment"] == "ps_folder" and i["is_shortcut"] == False and i["name"] == "Smart_personal_folder2"
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")	


 
    @pytest.mark.run(order=20)
    def test_20_Modify_the_smartfolder_personal_object_name_filed_with_lakshmi(self):
        logging.info("Modify_the_smartfolder_personal_object_name_filed_with_lakshmi")
        data = {"name": "lakshmi"}
        response = ib_NIOS.wapi_request('PUT', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9wZXJzb25hbF9mb2xkZXJfd2FwaTc:Smart_personal_folder_wapi7/false", fields=json.dumps(data))
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=21)
    def test_21_Modify_the_smartfolder_personal_object_comment_filed_with_SFP(self):
        logging.info("Modify_the_smartfolder_personal_object_comment_filed_with_SFP")
        data = {"comment": "SFP"}
        response = ib_NIOS.wapi_request('PUT', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9wZXJzb25hbF9mb2xkZXJfd2FwaQ:Smart_personal_folder_wapi/false", fields=json.dumps(data))
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=22)
    def test_22_Modify_the_smartfolder_personal_object_group_bys_filed_with_false_N(self):
        logging.info("Modify_the_smartfolder_personal_object_group_bys_filed_with_false_N")
        data = {"group_bys": False}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5sYWtzaG1p:lakshmi/false', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'List value expected for field: group_bys',response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=23)
    def test_23_Create_smartfolder_personal_object_with_query_items_operator_Eq_N(self):
        logging.info("create_smartfolder_personal_object_with_query_items_operator_Eq_N")
        data = {"name":"testing1","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "Eq","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Invalid value for operator .*Eq.* valid values are: EQ, GT, GEQ, LT, LEQ, HAS_VALUE, BEGINS_WITH, ENDS_WITH, CONTAINS, RELATIVE_DATE, RISES_BY, DROPS_BY, INHERITANCE_STATE_EQUALS, IP_ADDR_WITHIN, SUFFIX_MATCH, MATCH_EXPR',response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=24)
    def test_24_Create_smartfolder_personal_object_with_query_items_operator_op_match_N(self):
        logging.info("create_smartfolder_personal_object_with_query_items_operator_op_match_N")
        data = {"name":"testing1","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": "","operator": "EQ","value": {"value_string": "bang"},"value_type": "STRING"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('.*Invalid value for op_match: .*.*: Must be boolean type.*',response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=25)
    def test_25_Create_smartfolder_personal_object_with_query_items_operator_value_type_BOOLEAN_N(self):
        logging.info("create_smartfolder_personal_object_with_query_items_operator_value_type_BOOLEAN_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "BOOLEAN"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*BOOLEAN, STRING.*',response1)
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=26)
    def test_26_Create_smartfolder_personal_object_with_query_items_operator_value_type_DATE_N(self):
        logging.info("create_smartfolder_personal_object_with_query_items_operator_value_type_DATE_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "DATE"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*DATE, STRING.*',response1)
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=27)
    def test_27_Create_smartfolder_personal_object_with_query_items_operator_value_type_ENUM_N(self):
        logging.info("create_smartfolder_personal_object_with_query_items_operator_value_type_ENUM_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "ENUM"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*ENUM, STRING.*',response1)
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=28)
    def test_28_Create_smartfolder_personal_object_with_query_items_operator_value_type_EMAIL_N(self):
        logging.info("create_smartfolder_personal_object_with_query_items_operator_value_type_EMAIL_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "EMAIL"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*EMAIL, STRING.*',response1)
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=29)
    def test_29_Create_smartfolder_personal_object_with_query_items_operator_value_type_URL_N(self):
        logging.info("create_smartfolder_personal_object_with_query_items_operator_value_type_URL_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "URL"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*URL, STRING.*',response1)
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=30)
    def test_30_Create_smartfolder_personal_object_with_query_items_operator_value_type_OBJTYPE_N(self):
        logging.info("create_smartfolder_personal_object_with_query_items_operator_value_type_OBJTYPE_N")
        data = {"name":"testing99","query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "OBJTYPE"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Value type of query item does not match meta data for field Site. .*OBJTYPE, STRING.*',response1)
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")

    
    @pytest.mark.run(order=31)
    def test_31_DELETE_the_smartfolder_personal(self):
        logging.info("DELETE_the_smartfolder_personal")
        data = {"name": "Smart_personal_folder2"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hbF9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9wZXJzb25hbF9mb2xkZXIy:Smart_personal_folder2/false", fields=json.dumps(data))
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=32)
    def test_32_DELETE_the_smartfolder_personal(self):
        logging.info("DELETE_the_smartfolder_personal")
        data = {"name": "Smart_personal_folder_wapi"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="martfolder:personal/Li5teV9wZXJzb25hb9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9wZXJzb25hbF9mb2xkZXJfd2FwaQ:Smart_personal_folder_wapi/false", fields=json.dumps(data))
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=33)
    def test_33_DELETE_the_smartfolder_personal(self):
        logging.info("DELETE_the_smartfolder_personal")
        data = {"name": "lakshmi/false"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hbFzbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5sYWtzaG1p:lakshmi/false", fields=json.dumps(data))
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=34)
    def test_34_DELETE_the_smartfolder_personal(self):
        logging.info("DELETE_the_smartfolder_personal")
        data = {"name": "Smart_personal_folder_wapi/false"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hbFzbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5TbWFydF9wZXJzb25hbF9mb2xkZXJfd2FwaQ:Smart_personal_folder_wapi/false", fields=json.dumps(data))
        logging.info("Test Case 34 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=35)
    def test_35_DELETE_the_smartfolder_personal(self):
        logging.info("DELETE_the_smartfolder_personal")
        data = {"name": "lakshmi/false"}
        response = ib_NIOS.wapi_request('DELETE', object_type="smartfolder:global",ref="smartfolder:personal/Li5teV9wZXJzb25hb9zbWFydF9mb2xkZXIkb25lLnBlcnNvbmFsX3NtYXJ0X2ZvbGRlciQuY29tLmluZm9ibG94Lm9uZS5hZG1pbiRhZG1pbi5sYWtzaG1p:lakshmi/false", fields=json.dumps(data))
        logging.info("Test Case 35 Execution Completed")
        logging.info("============================")
    
    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")




