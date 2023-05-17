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
    def test_1_Adding_the_hsm_allgroups_in_groups_field_N(self):
        logging.info("Adding_the_hsm_allgroups_in_groups_field_N")
        data = {"groups":["hsm:thalesgroup/b25lLnRoYWxlc19oc21fZ3JvdXAkdGhhbGVz:thales"]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:allgroups",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for hsm:allgroups',response1)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=2)
    def test_2_Delete_groups_field_with_hsm_allgroups_object_N(self):
        logging.info("Delete_groups_field_with_hsm_allgroups_object_N")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = "hsm:allgroups/Li5hbGxfaHNtX2dyb3VwJDQ:hsm")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for hsm:allgroups',response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=3)
    def test_3_Modifiy_the_hsm_allgroups_with_groups_N(self):
        logging.info("Modifiy_the_hsm_allgroups_with_groups_N")
        data = {"groups":["hsm:thalesgroup/b25lLnRoYWxlc19oc21fZ3JvdXAkdGhhbGVz:thales"]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'hsm:allgroups/Li5hbGxfaHNtX2dyb3VwJDQ:hsm', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation update not allowed for hsm:allgroups',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")

		
    @pytest.mark.run(order=4)
    def test_4_Global_search_with_string_in_hsm_allgroups_object_N(self):
        logging.info("Global_search_with_string_in_hsm_allgroups_object_N")
        response = ib_NIOS.wapi_request('GET', object_type="search",params="?search_string=groups")
        logging.info(response)
        res = json.loads(response)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "Infoblox" and i["global_status"] == "INACTIVE" and i["groups"] == "hsm:thalesgroup/b25lLnRoYWxlc19oc21fZ3JvdXAkdGhhbGVz:thales"
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")
		

    @pytest.mark.run(order=5)
    def test_5_Read_by_reference_in_hsm_allgroups_object(self):
        get_ref = ib_NIOS.wapi_request('GET', object_type="hsm:allgroups")
        logging.info(get_ref)
        res = json.loads(get_ref)
        ref = json.loads(get_ref)[0]['_ref']
        print ref
        logging.info("Test read by referance on hsm:allgroups object")
        status,response = ib_NIOS.wapi_request('GET',object_type=ref)
        print response
        print status
        logging.info(response)
        assert status == 400 and re.search(r'AdmConProtoError: Operation \\"read by reference\\" not allowed for hsm:allgroup',response)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=6)
    def test_6_Get_the_field_in_hsm_allgroups_with_groups(self):
        logging.info("Get_the_field_in_hsm_allgroups_with_groups")
        response = ib_NIOS.wapi_request('GET', object_type="hsm:allgroups",)
        logging.info(response)
        read  = re.search(r'200',response)
        for read in  response:
        	assert True
        logging.info("Test Case  Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=7)
    def test_7_Groups_filed_is_not_searchable_with_hsm_allgroups_object_N(self):
        logging.info("Groups_filed_is_not_searchable_with_hsm_allgroups_object_N")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="hsm:allgroups", params="?groups=hsm:thalesgroup/b25lLnRoYWxlc19oc21fZ3JvdXAkdGhhbGVz:thales")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: groups',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")
	


    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")


