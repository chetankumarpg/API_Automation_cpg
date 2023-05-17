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
    def test_1_Adding_upgradegroup_with_name_comment_members_fields(self):
        logging.info("Adding_upgradegroup_with_name_comment_members_fields")
        data = {"members": [{"member": "2210.com"},{"member": "nd.com"}],"name": "infoblox","comment":"infoblox_group1"}
        response = ib_NIOS.wapi_request('POST', object_type="upgradegroup",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=2)
    def test_2_GET_operation_to_upgradegroup_object(self):
        logging.info("GET_operation_to_upgradegroup_object_")
        get_upgradegroup = ib_NIOS.wapi_request('GET', object_type="upgradegroup")
        logging.info(get_upgradegroup)
        res = json.loads(get_upgradegroup)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")
        print res	
   

    @pytest.mark.run(order=3)
    def test_3_create_the_upgradegroup_object_with_csvexport_fields_N(self):
        logging.info("create_the_upgradegroup_object_with_csvexport_fields_N")
        data = {"_object":"upgradegroup"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'upgradegroup objects do not support CSV export.',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")
	


    @pytest.mark.run(order=4)
    def test_4_Search_the_upgradegroup_object_with_search_string_field(self):
        logging.info("Search_the_upgradegroup_object_with_search_string_field")
        response = ib_NIOS.wapi_request('GET', object_type="search", params="?search_string=infoblox group")
        print response
        logging.info(response)
        read  = re.search(r'200',response)
        for read in  response:
        	assert True
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=5)
    def test_5_Adding_scheduled_time_filed_for_the_upgradegroup_object(self):
        logging.info("Adding_scheduled_time_filed_for_the_upgradegroup_object")
        data = {"name": "infoblox1"}
        response = ib_NIOS.wapi_request('POST', object_type="upgradegroup",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=6)
    def test_6_GET_the_upgradegroup_object_with_name_comment_time_zone_upgrade_time_distribution_time_upgrade_policy_distribution_policy_members(self):
        logging.info("GET_the_upgradegroup_object_with_name_comment_time_zone_upgrade_time_distribution_time_upgrade_policy_distribution_policy_members")
        get_upgradegroup = ib_NIOS.wapi_request('GET', object_type="upgradegroup")
        logging.info(get_upgradegroup)
        res = json.loads(get_upgradegroup)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")
        print res	



    @pytest.mark.run(order=7)
    def test_7_Search_name_field_in_upgradegroup_object_with_name(self):
        logging.info("Search_name_field_in_upgradegroup_object_with_name")
        search_upgradegroup = ib_NIOS.wapi_request('GET', object_type="upgradegroup", params="?name~=infoblox1")
        response = json.loads(search_upgradegroup)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["name"] in ["infoblox1"]  :
                    var=True

        assert var
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")

	


    @pytest.mark.run(order=8)
    def test_8_Search_name_field_in_upgradegroup_object_with_name(self):
        logging.info("Search_name_field_in_upgradegroup_object_with_name")
        search_upgradegroup = ib_NIOS.wapi_request('GET', object_type="upgradegroup", params="?name:=infoblox1")
        response = json.loads(search_upgradegroup)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["name"] in ["infoblox1"]  :
                    var=True

        assert var
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=9)
    def test_9_Search_name_field_in_upgradegroup_object_with_name(self):
        logging.info("Search_name_field_in_upgradegroup_object_with_name")
        search_upgradegroup = ib_NIOS.wapi_request('GET', object_type="upgradegroup", params="?name=infoblox1")
        response = json.loads(search_upgradegroup)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["name"] in ["infoblox1"]  :
                    var=True

        assert var
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=10)
    def test_10_Search_name_field_in_upgradegroup_object_with_name(self):
        logging.info("Search_name_field_in_upgradegroup_object_with_name")
        search_upgradegroup = ib_NIOS.wapi_request('GET', object_type="upgradegroup", params="?name~:=infoblox1")
        response = json.loads(search_upgradegroup)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["name"] in ["infoblox1"]  :
                    var=True

        assert var
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=11)
    def test_11_Search_name_field_in_upgradegroup_object_with_comment(self):
        logging.info("Search_name_field_in_upgradegroup_object_with_comment")
        response = ib_NIOS.wapi_request('GET', object_type="upgradegroup", params="?comment~:=Grid Master Group")
        print response
        logging.info(response)
        read  = re.search(r'200',response)
        for read in  response:
                assert True

        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")
	


    @pytest.mark.run(order=12)
    def test_12_Search_name_field_in_upgradegroup_object_with_comment(self):
        logging.info("Search_name_field_in_upgradegroup_object_with_comment")
        response = ib_NIOS.wapi_request('GET', object_type="upgradegroup", params="?comment~=Grid Master Group")
        print response
        logging.info(response)
        read  = re.search(r'200',response)
        for read in  response:
                assert True

        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=13)
    def test_13_Search_name_field_in_upgradegroup_object_with_comment(self):
        logging.info("Search_name_field_in_upgradegroup_object_with_comment")
        response = ib_NIOS.wapi_request('GET', object_type="upgradegroup", params="?comment:=Grid Master Group")
        logging.info(response)
        read  = re.search(r'200',response)
        for read in  response:
                assert True

        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=14)
    def test_14_Search_name_field_in_upgradegroup_object_with_comment(self):
        logging.info("Search_name_field_in_upgradegroup_object_with_comment")
        response = ib_NIOS.wapi_request('GET', object_type="upgradegroup", params="?comment=Grid Master Group")
        logging.info(response)
        read  = re.search(r'200',response)
        for read in  response:
                assert True

        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=15)
    def test_15_GET_the_upgradegroup_with_name_distribution_policy_distribution_time(self):
        logging.info("GET_the_upgradegroup_with_name_distribution_policy_distribution_time")
        get_upgradegroup = ib_NIOS.wapi_request('GET', object_type="upgradegroup")
        logging.info(get_upgradegroup)
        res = json.loads(get_upgradegroup)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")
        print res



    @pytest.mark.run(order=16)
    def test_16_Modify_the_upgradegroup_with_name_distribution_policy_distribution_time(self):
        logging.info("Modify_the_upgradegroup_with_name_distribution_policy_distribution_time")
        data = {"name": "infoblox","distribution_policy": "SIMULTANEOUSLY","distribution_time": 1494873900}
        response = ib_NIOS.wapi_request('PUT',ref='upgradegroup/b25lLnVwZ3JhZGVfZ3JvdXAkaW5mb2Jsb3g:infoblox',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response




    @pytest.mark.run(order=17)
    def test_17_GET_the_upgradegroup_with_upgrade_dependent_group_upgrade_policy_upgrade_time_name(self):
        logging.info("GET_the_upgradegroup_with_upgrade_dependent_group_upgrade_policy_upgrade_time_name")
        get_upgradegroup = ib_NIOS.wapi_request('GET', object_type="upgradegroup")
        logging.info(get_upgradegroup)
        res = json.loads(get_upgradegroup)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")
        print res



    @pytest.mark.run(order=18)
    def test_18_Modify_the_upgradegroup_with_upgrade_dependent_group_upgrade_policy_upgrade_time_name(self):
        logging.info("Modify_the_upgradegroup_with_upgrade_dependent_group_upgrade_policy_upgrade_time_name")
        data = {"name": "infoblox","upgrade_policy": "SEQUENTIALLY","upgrade_time": 1494948600}
        response = ib_NIOS.wapi_request('PUT',ref='upgradegroup/b25lLnVwZ3JhZGVfZ3JvdXAkaW5mb2Jsb3g:infoblox',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response
		


	


    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")


   
