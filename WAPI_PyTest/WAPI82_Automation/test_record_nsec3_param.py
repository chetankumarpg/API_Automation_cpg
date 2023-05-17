import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS
from time import sleep
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
    def test_1_Create_auth_zone(self):
        logging.info("Create_auth_zone")
        data = {"fqdn":"domain.com"}
        response = ib_NIOS.wapi_request('POST',object_type='zone_auth', fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=2)
    def test_2_Modify_the_zone_to_add_grid_primary_member(self):
        logging.info("Modify_the_zone_to_add_grid_primary_member")
        data = {"grid_primary": [{"name": config.grid_fqdn ,"stealth":False}]}
        response = ib_NIOS.wapi_request('PUT',ref='zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4:domain.com/default',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response



    @pytest.mark.run(order=3)
    def test_3_Create_A_record(self):
        logging.info("Create_A_record")
        data = {"ipv4addr":"1.1.1.1","name":"a.domain.com"}
        response = ib_NIOS.wapi_request('POST',object_type='record:a', fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=4)
    def test_4_create_for_sign_the_zone(self):
        logging.info("create_for_sign_the_zone")
        data = {"operation":"SIGN"}
        response = ib_NIOS.wapi_request('POST',ref='zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4:domain.com/default',params='?_function=dnssec_operation',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response



    @pytest.mark.run(order=5)
    def test_5_Get_operation_to_read_record_nsec3_param_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_param_object_using_creator")
        search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3param")
        response = json.loads(search_record_nsec3)
        print response
        var= False
        if len(response)==1:
            
            for i in response:
                if "domain.com" in i["name"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=6)
    def test_6_create_record_nsec3_object_N(self):
        logging.info("create_record_nsec3_param_object_N")
        data = {"name": "domain.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="record:nsec3param",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for record:nsec3param',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=7)
    def test_7_DELETE_auth_zone(self):
        get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
        logging.info(get_ref)
        res = json.loads(get_ref)
        ref = json.loads(get_ref)[0]['_ref']
        print ref

        logging.info("Deleting the networkview Testing")
        data ={"fqdn":"domain.com"}
        get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
        print get_status
        logging.info(get_status)
        logging.info("Test Case 7 Execution Completed")
        logging.info("===========================")

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")

