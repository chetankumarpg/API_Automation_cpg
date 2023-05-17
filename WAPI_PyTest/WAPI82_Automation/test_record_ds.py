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
    def test_1_create_zone(self):
        logging.info("Create zone with required fields")
        data = {"fqdn": "domain.com","view": "default"}
        response = ib_NIOS.wapi_request('POST', object_type="zone_auth",fields=json.dumps(data))
	logging.info("============================")
        print response
    
    @pytest.mark.run(order=2)
    def test_2_create_grid_primary_for_zone(self):
        logging.info("Create grid_primary with required fields")
        data = {"grid_primary": [{"name": "infoblox.localdomain","stealth":False}]}
        response = ib_NIOS.wapi_request('PUT',ref='zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response

    @pytest.mark.run(order=3)
    def test_3_create_for_sign_the_zone(self):
        logging.info("create_for_sign_the_zone")
        data = {"operation":"SIGN"}
        response = ib_NIOS.wapi_request('POST',ref='zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4',params='?_function=dnssec_operation',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response

    @pytest.mark.run(order=4)
    def test_4_create_sub_zone(self):
        logging.info("create_sub_zone")
        data = {"fqdn": "sub.domain.com","view": "default"}
        response = ib_NIOS.wapi_request('POST',ref='zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response

    @pytest.mark.run(order=5)
    def test_5_create_grid_primary_for_subzone(self):
        logging.info("Create grid_primary for subzone with required fields")
        data = {"grid_primary": [{"name": "infoblox.localdomain","stealth":False}]}
        response = ib_NIOS.wapi_request('PUT',ref='zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4uc3Vi',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response	


    @pytest.mark.run(order=6)
    def test_6_create_for_sign_the_subzone(self):
        logging.info("create_for_sign_the_subzone")
        data = {"operation":"SIGN"}
        response = ib_NIOS.wapi_request('POST',ref='zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4uc3Vi',params='?_function=dnssec_operation',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response
    @pytest.mark.run(order=7)
    def test_7_create_record_ds_object_N(self):
        logging.info("create_record_ds_object_N")
        data = {"name": "domain.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="record:ds",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Operation create not allowed for record:ds',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=8)
    def test_8_Get_operation_to_read_record_ds_object(self):
        logging.info("Get_operation_to_read_record_ds_object")
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds")
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "sub.domain.com" and i["view"] == "default"
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=9)
    def test_3_delete_record_ds_object(self):
        logging.info("delete_record_ds_object")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = "record:ds/ZG5zLmJpbmRfZHMkLl9kZWZhdWx0LmNvbS5kb21haW4sc3Viem9uZSw1NzQ1Myw2LDE:subzone.domain.com/default")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for record:ds',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")  


    @pytest.mark.run(order=10)
    def test_10_Modify_the_record_ds_object(self):
        logging.info("Modify_the_record_ds_object")
        data = {"name": "domain.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="record:ds/ZG5zLmJpbmRfZG5za2V5JC5fZGVmYXVsdC5jb20uZG9tYWluLjcuNDk5OTg:domain.com/default", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation update not allowed for record:ds',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=11)
    def test_11_Create_schedule_the_record_ds_object(self):
        logging.info("create_schedule_the_record_ds_object")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="record:ds",params="?_schedinfo.scheduled_time=2123235895")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for record:ds',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=12)
    def test_12_Csvexport_for_record_ds_object(self):
        logging.info("csvexport_for_record_ds_object")
        status,response1 = ib_NIOS.wapi_request('POST', params="?_function=csv_export", user="admin", password="infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Function csv_export is not valid for this object',response1)
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=13)
    def test_13_Get_operation_to_read_record_ds_object_with_algorithm_field_using(self):
        logging.info("Get_operation_to_read_record_ds_object_with_algorithm_field_using(=) of value DSA")
	data = {"algorithm":"DSA"}
        grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds",user="admin", password="infoblox", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=14)
    def test_14_Get_operation_to_read_record_ds_object_with_algorithm_field_using_ECDSAP256SHA256(self):
        logging.info("Get_operation_to_read_record_ds_object_with_algorithm_field_using(=) of value ECDSAP256SHA256")
	data = {"algorithm":"ECDSAP256SHA256"}
        grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds",user="admin", password="infoblox", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=15)
    def test_15_Get_operation_to_read_record_ds_object_with_algorithm_field_using_ECDSAP384SHA384(self):
        logging.info("Get_operation_to_read_record_ds_object_with_algorithm_field_using(=) of value ECDSAP384SHA384")
	data = {"algorithm":"ECDSAP384SHA384"}
        grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds",user="admin", password="infoblox", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=16)
    def test_16_Get_operation_to_read_record_ds_object_with_algorithm_field_using_NSEC3RSASHA1(self):
        logging.info("Get_operation_to_read_record_ds_object_with_algorithm_field_using(=) of value NSEC3RSASHA1")
	data = {"algorithm":"NSEC3RSASHA1"}
        grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds",user="admin", password="infoblox", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=17)
    def test_17_Get_operation_to_read_record_ds_object_with_algorithm_field_using_RSAMD5(self):
        logging.info("Get_operation_to_read_record_ds_object_with_algorithm_field_using(=) of value RSAMD5")
	data = {"algorithm":"RSAMD5"}
        grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds",user="admin", password="infoblox", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=18)
    def test_18_Get_operation_to_read_record_ds_object_with_algorithm_field_using_RSASHA1(self):
        logging.info("Get_operation_to_read_record_ds_object_with_algorithm_field_using(=) of value RSASHA1")
	data = {"algorithm":"RSASHA1"}
        grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds",user="admin", password="infoblox", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=19)
    def test_19_Get_operation_to_read_record_ds_object_with_algorithm_field_using_RSASHA256(self):
        logging.info("Get_operation_to_read_record_ds_object_with_algorithm_field_using(=) of value RSASHA256")
	data = {"algorithm":"RSASHA256"}
        grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds",user="admin", password="infoblox", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=20)
    def test_20_Get_operation_to_read_record_ds_object_with_algorithm_field_using_RSASHA512(self):
        logging.info("Get_operation_to_read_record_ds_object_with_algorithm_field_using(=) of value RSASHA512")
	data = {"algorithm":"RSASHA512"}
        grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds",user="admin", password="infoblox", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=21)
    def test_21_Get_operation_to_read_record_ds_object_with_algorithm_field_using_NSEC3DSA(self):
        logging.info("Get_operation_to_read_record_ds_object_with_algorithm_field_using(=) of value NSEC3DSA")
	data = {"algorithm":"NSEC3DSA"}
        grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds",user="admin", password="infoblox", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=22)
    def test_22_Get_operation_to_read_record_ds_object_N(self):
        logging.info("Search operation for allow_uploads fields with ~:= modifier")
	data = {"cloud_info":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: cloud_info',response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=23)
    def test_23_Get_operation_to_read_record_ds_object_with_comment_field(self):
        logging.info("Get_operation_to_read_record_ds_object")
	data = {"comment":"Auto-created"}
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds", fields=json.dumps(data))
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "sub.domain.com" and i["view"] == "default"
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=24)
    def test_24_Search_operation_to_read_record_ds_object(self):
        logging.info("Get_operation_to_read_record_ds_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", params="?algorithm~=NSEC3DSA")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: algorithm",response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=25)
    def test_25_Search_operation_to_read_record_ds_object(self):
        logging.info("Get_operation_to_read_record_ds_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", params="?algorithm:=NSEC3DSA")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: algorithm",response1)
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=26)
    def test_26_Search_operation_to_read_record_ds_object_with_creation_time(self):
        logging.info("Get_operation_to_read_record_ds_object")
	data={"creation_time":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: creation_time',response1)
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=27)
    def test_27_return_fields_with_creator_time(self):
        logging.info("Update operation for allow_uploads fields")
        grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds", params="?_return_fields=creation_time")
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=28)
    def test_28_Search_operation_to_read_record_ds_object_with_digest(self):
        logging.info("Get_operation_to_read_record_ds_object_with_digest_field")
	data={"digest":"SYSTEM" }
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: digest',response1)
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=29)
    def test_29_Get_operation_to_read_record_ds_object_with_digest_type_field_value_SHA1(self):
        logging.info("Get_operation_to_read_record_ds_objectwith_digest_type_value_SHA1")
        data = {"digest_type":"SHA1"}
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds", fields=json.dumps(data))
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "sub.domain.com" and i["view"] == "default"
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=30)
    def test_30_Get_operation_to_read_record_ds_object_with_digest_type_field_value_SHA256(self):
        logging.info("Get_operation_to_read_record_ds_objectwith_digest_type_value_SHA256")
        data = {"digest_type":"SHA256"}
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="record:ds", fields=json.dumps(data))
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "sub.domain.com" and i["view"] == "default"
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=31)
    def test_31_Search_operation_to_read_record_ds_object_with_modifier_colon(self):
        logging.info("Get_operation_to_read_record_ds_object_modifier_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", params="?digest_type:=SHA256i")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: digest_type",response1)
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")
		
		
    @pytest.mark.run(order=32)
    def test_32_Search_operation_to_read_record_ds_object_with_modifier_negotiate(self):
        logging.info("Get_operation_to_read_record_ds_object_modifier_negotiate")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", params="?digest_type~=SHA256")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: digest_type",response1)
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=33)
    def test_33_Get_operation_to_read_record_ds_object_with_dns_name(self):
        logging.info("Search operation for allow_uploads fields with dns_name")
        data = {"dns_name":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: dns_name',response1)
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=34)
    def test_34_Search_operation_to_read_record_ds_object_with_keytag_modifier_colon(self):
        logging.info("Get_operation_to_read_record_ds_object_keytag_modifier_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", params="?key_tag:=2057453")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: key_tag",response1)
        logging.info("Test Case 34 Execution Completed")
        logging.info("============================")
		
		
    @pytest.mark.run(order=35)
    def test_35_Search_operation_to_read_record_ds_object_with_modifier_negotiate(self):
        logging.info("Get_operation_to_read_record_ds_object_modifier_negotiate")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", params="?key_tag~=SHA256")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: key_tag",response1)
        logging.info("Test Case 35 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=36)
    def test_36_Get_operation_to_read_record_ds_object_with_last_queried(self):
        logging.info("Search operation for allow_uploads fields with last_queried")
        data = {"last_queried":"2057453"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: last_queried',response1)
        logging.info("Test Case 36 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=37)
    def test_37_Get_operation_to_read_record_ds_object_with_ttl(self):
        logging.info("Search operation for allow_uploads fields with ttl")
        data = {"ttl":"subz"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ttl',response1)
        logging.info("Test Case 37 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=38)
    def test_38_Search_operation_to_read_record_ds_object_with_creator(self):
        logging.info("Get_operation_to_read_record_ds_object_with_creator")
	data={"creator":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for creator .*DSA.* valid values are: SYSTEM",response1)
        logging.info("Test Case 38 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=39)
    def test_39_Search_operation_to_read_record_ds_object_with_zone(self):
        logging.info("Get_operation_to_read_record_ds_object_with_zone")
	data={"zone":" default"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:ds", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for zone: .* default.*: leading or trailing whitespace is not allowed.',response1)
        logging.info("Test Case 39 Execution Completed")
        logging.info("============================")


    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")
