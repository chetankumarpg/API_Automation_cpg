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
    def test_1_Get_the_fields_in_hsm_thalesgroup_object(self):
        logging.info("Get_the_fields_in_hsm_thalesgroup_object")
        get_hsm_thalesgroup = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup")
        logging.info(get_hsm_thalesgroup)
        res = json.loads(get_hsm_thalesgroup)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")
        print res

		
    @pytest.mark.run(order=2)
    def test_2_Global_search_with_string_in_hsm_thalesgroup_object_N(self):
        logging.info("Global_search_with_string_in_hsm_thalesgroup_object_N")
        search_hsm_thalesgroup = ib_NIOS.wapi_request('GET', object_type="search",params="?search_string=thales")
        logging.info(search_hsm_thalesgroup)
        res = json.loads(search_hsm_thalesgroup)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "Infoblox" and i["global_status"] == "INACTIVE" and i["storage_limit"] == 500 and  i["current_usage"] == 0 and i["allow_uploads"] == False
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=3)
    def test_3_Adding_the_scheduling_with_string_in_hsm_thalesgroup_object_N(self):
	logging.info("Adding_the_scheduling_with_string_in_hsm_thalesgroup_object_N")
	data ={"comment": "this is a thales group ","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "MODULE","thales_hsm":[{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}]}
	status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",params="?_schedinfo.scheduled_time=1591056000",fields=json.dumps(data))
	print status
	print response1
	logging.info(response1)
	assert  status == 400 and re.search(r'hsm:thalesgroup does not support scheduling.',response1)
	logging.info("Test Case 3 Execution Completed")
	logging.info("============================")

		    
    @pytest.mark.run(order=4)
    def test_4_Adding_CSV_export_field_in_the_hsm_thalesgroup_object_N(self):
        logging.info("Adding_CSV_export_field_in_the_hsm_thalesgroup_object_N")
        data = {"_object":"hsm:thalesgroup"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'hsm:thalesgroup objects do not support CSV export.',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=5)
    def test_5_Adding_the_hsm_thalesgroup_object_to_card_name_field_must_specify_N(self):
        logging.info("Adding_the_hsm_thalesgroup_object_to_card_name_field_must_specify_N")
        data = {"comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}],"pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'You must specify card_name when protection is set to .*SOFTCARD.*.',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=6)
    def test_6_Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_N(self):

	logging.info("Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_N")
	data = {"comment": "this is a thales group ","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "MODULE","status": "UP","thales_hsm":[{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_esn": "5C1C-371B-DECB","remote_ip": "10.39.10.10","remote_port": 9004,"status": "UP"}]}
	status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
	print status
	print response1
	logging.info(response1)
	assert  status == 400 and re.search(r'AdmConProtoError: field for create missing: hsm_version',response1)
	logging.info("Test Case 6 Execution Completed")
	logging.info("============================")


    @pytest.mark.run(order=7)
    def test_7_Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_N(self):
        logging.info("Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_N")
        data = {"comment": "this is a thales group ","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "MODULE","status": "UP","thales_hsm":[{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_esn": "5C1C-371B-DECB","remote_ip": "10.39.10.10","remote_port": 9004,"status": "UP","hsm_version": "LunaSA_5"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: status',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=8)
    def test_8_Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_N(self):
        logging.info("Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_N")
        data = {"comment": "this is a thales group ","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "MODULE","thales_hsm":[{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_esn": "5C1C-371B-DECB","remote_ip": "10.39.10.10","remote_port": 9004}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: remote_esn',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=9)
    def test_9_Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_Modules(self):
        logging.info("Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_Modules")
        data = {"comment": "this is a thales group ","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "MODULE","thales_hsm":[{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}]}
        response = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=10)
    def test_10_Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_softcard(self):
        logging.info("Adding_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_softcard")
        data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}],"pass_phrase":"Infoblox.123"}
        response = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=11)
    def test_11_Modifiy_the_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm(self):
        logging.info("Modifiy_the_hsm_safenetgroup_with_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm")
        data = {"comment": "this is a thales group ","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "MODULE","thales_hsm":[{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}]}
        response = ib_NIOS.wapi_request('PUT', ref = "hsm:thalesgroup/b25lLnRoYWxlc19oc21fZ3JvdXAkdGhhbGVz:thales",fields=json.dumps(data))
        logging.info("============================")
        print response

		

    @pytest.mark.run(order=12)
    def test_12_Get_the_fields_in_hsm_thalesgroup_object_N(self):
	logging.info("Get_the_fields_in_hsm_thalesgroup_object_N")
	status,response = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup",params="?_return_fields=comment,key_server_ip,name,status,pass_phrase,card_name,protection,key_server_ip,key_server_port,thales_hsm")
	print status
	print response
	logging.info(response)
	assert  status == 400 and re.search(r"Field is not readable: pass_phrase",response)
	logging.info("Test Case 12 Execution Completed")
	logging.info("============================")

				
    @pytest.mark.run(order=13)
    def test_13_return_fields_Get_the_all_fields_in_hsm_thalesgroup_object_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm(self):
	logging.info("Test_the_return_fields Get_the_all_fields_in_hsm_thalesgroup_object_comment_key_server_ip_name_status_card_name_protection_key_server_ip_key_server_port_thales_hsm_object")
	get_return_fields = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup",)
	logging.info(get_return_fields)
	res = json.loads(get_return_fields)
	print res
	string = [{u'comment': u'this is a thales group ', u'_ref': u'hsm:thalesgroup/b25lLnRoYWxlc19oc21fZ3JvdXAkdGhhbGVz:thales', u'key_server_ip': u'10.39.10.39', u'name': u'thales'}]
	if res == string:
		assert True
	else:
		assert False
	logging.info("Test Case  Execution Completed")
	logging.info("============================")



    @pytest.mark.run(order=14)
    def test_14_Search_operation_to_hsm_thalesgroup_object_in_field_card_name_N(self):
        logging.info("Search_operation_to_the_hsm_thalesgroup_object_in_field_card_name_N")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup",params="?card_name=HSMThales")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: card_name",response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=15)
    def test_15_Search_name_field_in_hsm_thalesgroup_object_with_comment(self):
        logging.info("Search_name_field_in_hsm_thalesgroup_object_with_comment")
        search_hsm_thalesgroup = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup", params="?comment=this is a thales group")
        response = json.loads(search_hsm_thalesgroup)
        print response
        for i in response:
                print i
                logging.info("found")
                assert i["comment"] == "this is a thales group " and i["key_server_ip"] == "10.39.10.39" and i["name"] == "thales"
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=16)
    def test_16_Search_comment_field_in_hsm_thalesgroup_object(self):
	logging.info("Search_comment_field_in_hsm_thalesgroup_object")
	search_hsm_thalesgroup = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup",params="?comment~=this is a thales group")
	response = json.loads(search_hsm_thalesgroup)
	print response
	for i in response:
		print i
		logging.info("found")
		assert i["comment"] == "this is a thales group " and i["key_server_ip"] == "10.39.10.39" and i["name"] == "thales"
	logging.info("Test Case 16 Execution Completed")
	logging.info("============================")


    @pytest.mark.run(order=17)
    def test_17_Search_comment_field_in_hsm_thalesgroup_object(self):
        logging.info("Search_comment_field_in_hsm_thalesgroup_object")
        search_hsm_thalesgroup = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup", params="?comment~=this is a thales group")
        response = json.loads(search_hsm_thalesgroup)
        print response
        for i in response:
               print i
               logging.info("found")
               assert i["comment"] == "this is a thales group " and i["key_server_ip"] == "10.39.10.39" and i["name"] == "thales"
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")	



    @pytest.mark.run(order=18)
    def test_18_Search_the_hsm_thalesgroup_object_in_field_key_server_ip_N(self):
        logging.info("Search_the_hsm_thalesgroup_object_in_field_key_server_ip_N")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup", params="?key_server_ip=10.39.10.39")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: key_server_ip',response1)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")
   

    @pytest.mark.run(order=19)
    def test_19_Adding_the_hsm_thalesgroup_object_in_field_key_server_ip_N(self):
        logging.info("Adding_the_hsm_thalesgroup_object_in_field_key_server_ip_N")
        data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": 10,"key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}],"pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for key_server_ip: 10: Must be string type',response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")
 


    @pytest.mark.run(order=20)
    def test_20_Search_the_hsm_thalesgroup_object_in_field_key_server_port_N(self):
        logging.info("Search_the_hsm_thalesgroup_object_in_field_key_server_port_N")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup", params="?key_server_port=9004")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: key_server_port',response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")
   


    @pytest.mark.run(order=21)
    def test_21_Adding_the_hsm_thalesgroup_object_in_field_key_server_port_N(self):
        logging.info("Adding_the_hsm_thalesgroup_object_in_field_key_server_port_N")
        data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": "9004","name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}],"pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for key_server_port: .*9004.*: Must be integer type',response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")
 

    @pytest.mark.run(order=22)
    def test_22_Search_name_field_in_hsm_thalesgroup_object(self):
        logging.info("Search_name_field_in_hsm_thalesgroup_object")
        search_hsm_thalesgroup = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup",params="?name=thales")
        response = json.loads(search_hsm_thalesgroup)
        print response
        for i in response:
                print i
                logging.info("found")
                assert i["name"] == "thales"
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=23)
    def test_23_Search_name_field_in_hsm_thalesgroup_object(self):
        logging.info("Search_name_field_in_hsm_thalesgroup_object")
        search_hsm_thalesgroup = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup",params="?name:=thales")
        response = json.loads(search_hsm_thalesgroup)
        print response
        for i in response:
                print i
                logging.info("found")
                assert i["name"] == "thales"
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=24)
    def test_24_Search_name_field_in_hsm_thalesgroup_object(self):
        logging.info("Search_name_field_in_hsm_thalesgroup_object")
        search_hsm_thalesgroup = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup",params="?name~=thales")
        response = json.loads(search_hsm_thalesgroup)
        print response
        for i in response:
                print i
                logging.info("found")
                assert i["name"] == "thales"
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=25)
    def test_25_Search_name_field_in_hsm_thalesgroup_object(self):
        logging.info("Search_name_field_in_hsm_thalesgroup_object")
        search_hsm_thalesgroup = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup",params="?name~:=thales")
        response = json.loads(search_hsm_thalesgroup)
        print response
        for i in response:
                print i
                logging.info("found")
                assert i["name"] == "thales"
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")
	

    @pytest.mark.run(order=26)
    def test_26_Adding_the_hsm_thalesgroup_object_to_name_field_N(self):
        logging.info("Adding_the_hsm_thalesgroup_object_to_name_field_N")
        data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}],"pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'field for create missing: name',response1)
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")
	


    @pytest.mark.run(order=27)
    def test_27_Search_the_hsm_thalesgroup_object_to_pass_phrase_N(self):
        logging.info("Search_the_hsm_thalesgroup_object_to_pass_phrase_N")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup", params="?pass_phrase=infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: pass_phrase',response1)
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")
   


    @pytest.mark.run(order=28)
    def test_28_Adding_the_hsm_thalesgroup_object_to_pass_phrase_field_N(self):
        logging.info("Adding_the_hsm_thalesgroup_object_to_pass_phrase_field_N")
        data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'You must specify pass_phrase when protection is set to .*SOFTCARD.*.',response1)
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")
 
    @pytest.mark.run(order=29)
    def test_29_Adding_the_hsm_thalesgroup_object_to_pass_phrase_field_should_be_in_string_type_N(self):
        logging.info("Adding_the_hsm_thalesgroup_object_to_pass_phrase_field_should_be_in_string_type_N")
        data = {"card_name":"HSMThales","comment": "this_is_a_thales_group","key_server_ip": "10.39.10.39","key_server_port": 9004,"name": "thales","protection": "SOFTCARD","thales_hsm": [{"disable": False,"keyhash": "821f3afc559c84d3b212af34d997386acb992141","remote_ip": "10.39.10.10","remote_port": 9004}],"pass_phrase":123}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:thalesgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for pass_phrase: 123: Must be string type',response1)
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=30)
    def test_30_Search_the_hsm_thalesgroup_object_in_field_protection_N(self):
        logging.info("Search_the_hsm_thalesgroup_object_in_field_protection_N")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup", params="?protection=SOFTCARD")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: protection',response1)
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=31)
    def test_31_Search_the_hsm_thalesgroup_object_in_field_status_N(self):
        logging.info("Search_the_hsm_thalesgroup_object_in_field_status_N")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup", params="?status=UP")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: status',response1)
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=32)
    def test_32_Search_the_hsm_thalesgroup_object_in_field_thales_hsm_N(self):
        logging.info("Search_the_hsm_thalesgroup_object_in_field_thales_hsm_N")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="hsm:thalesgroup", params="?thales_hsm=false")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: thales_hsm',response1)
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")
			


    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")


