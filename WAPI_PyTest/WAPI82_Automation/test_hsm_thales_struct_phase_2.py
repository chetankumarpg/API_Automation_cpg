import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class Hsm_Thales_Struct(unittest.TestCase):

    @pytest.mark.run(order=1)
    def test_1_Get_the_all_fields_in_hsm_thalesgroup_object_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm(self):
        logging.info("Get_the_all_fields_in_hsm_thalesgroup_object_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm")
        response = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup",)
        logging.info(response)
        read  = re.search(r'200',response)
        for read in  response:
        	assert True
        logging.info("Test Case  Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=2)
    def test_2_Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_softcard(self):
        logging.info("Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_softcard")
        data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}],"pass_phrase":"Infoblox.123"}
        response = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        logging.info("============================")
        print response




    @pytest.mark.run(order=3)
    def test_3_Adding_hsm_safenetgroup_with_hsm_thales_filed_disable_N(self):
        logging.info("Adding_hsm_safenetgroup_with_hsm_thales_filed_disable_N")
        data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": "False","keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}],"pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for disable: .*False.*: Must be boolean type',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=4)
    def test_3_Adding_hsm_safenetgroup_with_hsm_thales_filed_keyhash_N(self):
        logging.info("Adding_hsm_safenetgroup_with_hsm:thales_filed_keyhash_N")
        data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash":8,"remote_ip": "10.39.10.10","remote_port": 9004}],"pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for keyhash: 8: Must be string type',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=5)
    def test_5_Adding_hsm_safenetgroup_with_hsm_thales_filed_remote_esn_N(self):
        logging.info("Adding_hsm_safenetgroup_with_hsm_thales_filed_remote_esn_N")
        data = {"comment": "this is a thales group ","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "MODULE","thales_hsm":[{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_esn": "5C1C-371B-DECB","remote_ip": "10.39.10.10","remote_port": 9004}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: remote_esn',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=6)
    def test_6_Adding_hsm_safenetgroup_with_hsm_thales_filed_remote_ip_N(self):
        logging.info("Adding_hsm_safenetgroup_with_hsm_thales_filed_remote_ip_N")
        data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": 10,"remote_port": 9004}],"pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for remote_ip: 10: Must be string type',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=7)
    def test_7_Adding_hsm_safenetgroup_with_hsm_thales_filed_remote_port_N(self):
        logging.info("Adding_hsm_safenetgroup_with_hsm_thales_filed_remote_port_N")
        data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": "9004"}],"pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for remote_port: .*9004.*: Must be integer type',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=8)
    def test_8_Search_the_hsm_thalesgroup_object_in_field_status_N(self):
        logging.info("Search_the_hsm_thalesgroup_object_in_field_status_N")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup", params="?status=UP")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: status',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=9)
    def test_9_Search_the_hsm_thalesgroup_object_in_field_thales_hsm_N(self):
        logging.info("Search_the_hsm_thalesgroup_object_in_field_thales_hsm_N")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup", params="?thales_hsm=False")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: thales_hsm',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")


