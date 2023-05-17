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
    def test_1_Get_operation_to_read_record_dnskey_object(self):
        logging.info("Get_operation_to_read_record_dnskey_object")
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="record:dnskey")
	logging.info(search_grid_fd)
        response = json.loads(search_grid_fd)
        print response
        for i in response:
            logging.info("found")
       	    if  i["name"] == "sub.domain.com":
	        print "found"
		assert i["name"] == "sub.domain.com" and i["view"] == "default"
	    else:
	        assert i["name"] == "domain.com" and i["view"] == "default"
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=2)
    def test_2_create_record_dnskey_object_N(self):
        logging.info("create_record_dnskey_object_N")
        data = {"name": "domain.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="record:dnskey",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for record:dnskey',response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=3)
    def test_3_Delete_record_dnskey_object_N(self):
        logging.info("Delete_record_dnskey_object_N")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = 'record:dnskey/ZG5zLmJpbmRfZG5za2V5JC5fZGVmYXVsdC5jb20uZG9tYWluLjcuNDk5OTg:domain.com/default')
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for record:dnskey',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=4)
    def test_4_Modify_record_dnskey_object_N(self):
        logging.info("Modify_record_dnskey_object_N")
	data = {"name": "domain.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'record:dnskey/ZG5zLmJpbmRfZG5za2V5JC5fZGVmYXVsdC5jb20uZG9tYWluLjcuNDk5OTg:domain.com/default', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation update not allowed for record:dnskey',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=5)
    def test_5_schedule_creation_for_record_dnskey(self):
        logging.info("schedule_creation_for_record_dnskey")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="record:dnskey",params="?_schedinfo.scheduled_time=2123235895")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for record:dnskey',response1)
        logging.info("Test Case 5 Execution Completed")

    @pytest.mark.run(order=6)
    def test_6_Search_operation_to_read_record_dnskey_object_with_modifier_equal(self):
        logging.info("Search_operation_to_read_record_dnskey_object_with_modifier_equal")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?comment=domain.com")
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=7)
    def test_7_Search_operation_to_read_record_dnskey_object_with_modifier_colon(self):
        logging.info("Search_operation_to_read_record_dnskey_object_with_modifier_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?comment:=domain.com")
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=8)
    def test_8_Search_operation_to_read_record_dnskey_object_with_modifier_negotation(self):
        logging.info("Search_operation_to_read_record_dnskey_object_with_modifier_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?comment~=domain.com")
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=9)
    def test_9_Search_operation_to_read_record_ds_object_with_comment(self):
        logging.info("Get_operation_to_read_record_ds_object_with_comment")
        data={"comment":" domain.com"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for comment: .* domain.com.*: leading or trailing whitespace is not allowed.',response1)
        logging.info("Test Case 39 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=10)
    def test_10_Get_operation_to_read_record_dnskey_object_with_creation_timeN(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_creation_timeN")
        data = {"creation_time":"12365456"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: creation_time',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=11)
    def test_11_Search_operation_to_read_record_dnskey_object_with_creator(self):
        logging.info("Search_operation_to_read_record_dnskey_object_with_creator")
        data={"creator":"lkpij"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for creator .*lkpij.* valid values are: SYSTEM",response1)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=12)
    def test_12_Get_operation_to_read_record_dnskey_object_with_name(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_name")
	data={"name":"domain.com"}
        search_record_dnskey = ib_NIOS.wapi_request('GET', object_type="record:dnskey", fields=json.dumps(data))
        logging.info(search_record_dnskey)
        response = json.loads(search_record_dnskey)
        print response
        for i in response:
            logging.info("found")
            assert i["name"] == "domain.com" and i["view"] == "default"
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=13)
    def test_13_Search_operation_to_read_record_dnskey_object_with_name_modifier_negotation(self):
        logging.info("Search_operation_to_read_record_dnskey_object_with_name_modifier_negotation")
        data={"name":"domain.com"}
        search_record_dnskey = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?name~=domain*")
        logging.info(search_record_dnskey)
        response = json.loads(search_record_dnskey)
        print response
        for i in response:
            logging.info("found")
            if  i["name"] == "sub.domain.com":
                print "found"
                assert i["name"] == "sub.domain.com" and i["view"] == "default"
            else:
                assert i["name"] == "domain.com" and i["view"] == "default"
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=14)
    def test_14_Get_operation_to_read_record_dnskey_object_with_domain_nameN(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_domain_nameN")
        data = {"dns_name":"domain.com"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: dns_name',response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=15)
    def test_15_Search_operation_to_read_record_dnskey_object_with_colon(self):
        logging.info("Get_operation_to_read_record_ds_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?view:=default")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: view",response1)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=16)
    def test_16_Search_operation_to_read_record_dnskey_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?view~=default")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: view",response1)
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=17)
    def test_17_Search_operation_to_read_record_dnskey_object_with_view(self):
        logging.info("Search_operation_to_read_record_dnskey_object_with_view")
        search_record_dnskey = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?view=default")
        logging.info(search_record_dnskey)
        response = json.loads(search_record_dnskey)
        print response
        for i in response:
            logging.info("found")
            if  i["name"] == "sub.domain.com":
                print "found"
                assert i["name"] == "sub.domain.com" and i["view"] == "default"
            else:
                assert i["name"] == "domain.com" and i["view"] == "default"
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")


     
    @pytest.mark.run(order=18)
    def test_18_Get_operation_to_read_record_dnskey_object_with_name(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_name")
        search_record_dnskey = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?_return_fields=zone" )
        response = json.loads(search_record_dnskey)
        print response
        for i in response:
            logging.info("found")
	    if  i["zone"] == "sub.domain.com":
                print "found"
                assert i["zone"] == "sub.domain.com"
            else:
                assert i["zone"] == "domain.com"
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=19)
    def test_19_Get_operation_to_read_record_dnskey_object_with_zone(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_name")
	data={"zone":"domain.com"}
        search_record_dnskey = ib_NIOS.wapi_request('GET', object_type="record:dnskey", fields=json.dumps(data))
        response = json.loads(search_record_dnskey)
        print response
        for i in response:
            logging.info("found")
            assert i["name"] == "domain.com" and i["view"] == "default"
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=20)
    def test_20_Search_operation_to_read_record_ds_object_with_zone(self):
        logging.info("Get_operation_to_read_record_ds_object_with_zone")
        data={"zone":" domain.com"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for zone: .* domain.com.*: leading or trailing whitespace is not allowed.',response1)
        logging.info("Test Case 39 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=21)
    def test_21_Get_operation_to_read_record_dnskey_object_with_creation_timeN(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_creation_timeN")
        data = {"ttl":"12365456"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ttl',response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=22)
    def test_22_Get_operation_with_algorithm(self):
        logging.info("Update operation for allow_uploads fields")
	data = {"algorithm":"NSEC3RSASHA1"}
        grid_fd = ib_NIOS.wapi_request('GET', object_type="record:dnskey", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=23)
    def test_23_Search_operation_to_read_record_dnskey_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?algorithm~=NSEC3RSASHA1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: algorithm",response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=24)
    def test_24_Search_operation_to_read_record_dnskey_object_with_colon(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?algorithm:=NSEC3RSASHA1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: algorithm",response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=25)
    def test_25_Get_operation_to_read_record_dnskey_object_with_flags(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_flags")
        search_record_dnskey = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?_return_fields=flags" )
        response = json.loads(search_record_dnskey)
        print response
	for i in response:
	    if  i["flags"] == 257:
                print "found"
                assert i["flags"] == 257
            else:
                assert i["flags"] == 256
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=26)
    def test_26_Get_operation_to_read_record_dnskey_object_with_flags(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_flags")
	data={"flags":"256"}
        search_record_dnskey = ib_NIOS.wapi_request('GET', object_type="record:dnskey", fields=json.dumps(data))
        response = json.loads(search_record_dnskey)
        print response
        for i in response:
	    if  i["name"] == "sub.domain.com":
                print "found"
                assert i["name"] == "sub.domain.com" and i["view"] == "default"
            else:
                 assert i["name"] == "domain.com" and i["view"] == "default"
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=27)
    def test_27_Search_operation_to_read_record_dnskey_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?flags~=256")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: flags",response1)
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")
		
		
    @pytest.mark.run(order=28)
    def test_28_Search_operation_to_read_record_dnskey_object_with_colon(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?flags:=256")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: flags",response1)
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=29)
    def test_29_Search_operation_to_read_record_dnskey_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?key_tag~=23507")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: key_tag",response1)
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")
		
		
    @pytest.mark.run(order=30)
    def test_30_Search_operation_to_read_record_dnskey_object_with_colon(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?key_tag:=256")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: key_tag",response1)
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=31)
    def test_31_Search_operation_to_read_record_dnskey_object_with_colon_in_public_key(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_colon_public_key")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dnskey", params="?public_key:=256")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: public_key",response1)
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")
    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")

