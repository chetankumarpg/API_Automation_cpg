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
    def test_1_Modify_view_to_enable_dnssec(self):
        logging.info("Modify_view_to_enable_dnssec")
        data = {"dnssec_enabled":True}
        response = ib_NIOS.wapi_request('PUT',ref='view/ZG5zLnZpZXckLl9kZWZhdWx0:default/true',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=2)
    def test_2_Create_auth_zone(self):
        logging.info("Create_auth_zone")
        data = {"fqdn":"domain.com"}
        response = ib_NIOS.wapi_request('POST',object_type='zone_auth', fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=3)
    def test_3_Modify_the_zone_to_add_grid_primary_member(self):
        logging.info("Modify_the_zone_to_add_grid_primary_member")
        data = {"grid_primary": [{"name": config.grid_fqdn ,"stealth":False}]}
        response = ib_NIOS.wapi_request('PUT',ref='zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4:domain.com/default',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=4)
    def test_4_Create_A_record(self):
        logging.info("Create_A_record")
        data = {"ipv4addr":"1.1.1.1","name":"a.domain.com"}
        response = ib_NIOS.wapi_request('POST',object_type='record:a', fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response



    @pytest.mark.run(order=5)
    def test_5_Modify_to_enable_the_nsec_in_auth_zone(self):
        logging.info("Modify_to_enable_the_nsec_in_auth_zone")
        data = {"dnssec_key_params": {"next_secure_type": "NSEC"}}
        response = ib_NIOS.wapi_request('PUT',ref='zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4:domain.com/default',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=6)
    def test_6_create_for_sign_the_zone(self):
        logging.info("create_for_sign_the_zone")
        data = {"operation":"SIGN"}
        response = ib_NIOS.wapi_request('POST',ref='zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4:domain.com/default',params='?_function=dnssec_operation',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=7)
    def test_7_Get_operation_to_read_record_nsec_object(self):
        logging.info("Get_operation_to_read_record_nsec_object")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec")
        response = json.loads(search_record_nsec)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if i["name"] in ["domain.com","a.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=8)
    def test_8_create_record_nsec_object_N(self):
        logging.info("create_record_nsec_object_N")
        data = {"name": "domain.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="record:nsec",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for record:nsec',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=9)
    def test_9_Delete_record_nsec_object_N(self):
        logging.info("Delete_record_nsec_object_N")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = 'record:nsec/ZG5zLmJpbmRfZG5za2V5JC5fZGVmYXVsdC5jb20uZG9tYWluLjcuNDk5OTg:domain.com/default')
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for record:nsec',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=10)
    def test_10_Modify_record_nsec_object_N(self):
        logging.info("Modify_record_nsec_object_N")
        data = {"name": "domain.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'record:nsec/ZG5zLmJpbmRfZG5za2V5JC5fZGVmYXVsdC5jb20uZG9tYWluLjcuNDk5OTg:domain.com/default', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation update not allowed for record:nsec',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=11)
    def test_11_Get_operation_to_read_record_nsec_object_using_name_with_negoation(self):
        logging.info("Get_operation_to_read_record_nsec_object_using_name")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?name~=domain.co*")
        response = json.loads(search_record_nsec)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if i["name"] in ["domain.com","a.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=12)
    def test_12_Get_operation_to_read_record_nsec_object_using_name_with_colon(self):
        logging.info("Get_operation_to_read_record_nsec_object_using_name")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?name:=Domain.com")
        response = json.loads(search_record_nsec)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["name"] in ["domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")

		
		
		
		
    @pytest.mark.run(order=13)
    def test_13_Get_operation_to_read_record_nsec_object_using_name(self):
        logging.info("Get_operation_to_read_record_nsec_object_using_name")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?name=domain.com")
        response = json.loads(search_record_nsec)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["name"] in ["domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=14)
    def test_14_Get_operation_to_read_record_nsec_object_N(self):
        logging.info("Search operation for dns_name fields")
        data = {"dns_name":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: dns_name',response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=15)
    def test_15_Get_operation_to_read_record_nsec_object_using_view(self):
        logging.info("Get_operation_to_read_record_nsec_object_using_view")
	search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?view=default")
        response = json.loads(search_record_nsec)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if i["name"] in ["domain.com","a.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=16)
    def test_16_Search_operation_to_read_record_nsec_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_nsec_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?view~=defaul*")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: view",response1)
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=17)
    def test_17_Search_operation_to_read_record_nsec_object_with_colon(self):
        logging.info("Get_operation_to_read_record_nsec_object_with_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?view:=Default")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: view",response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=18)
    def test_18_Get_operation_to_read_record_nsec_object_using_zone(self):
        logging.info("Get_operation_to_read_record_nsec_object_using_zone")
	search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?zone=domain.com")
        response = json.loads(search_record_nsec)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if i["name"] in ["domain.com","a.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=19)
    def test_19_Search_operation_to_read_record_nsec_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_nsec_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?zone~=domain.co*")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: zone",response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=20)
    def test_20_Search_operation_to_read_record_nsec_object_with_colon(self):
        logging.info("Get_operation_to_read_record_nsec_object_with_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?zone:=Domain.com")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: zone",response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=21)
    def test_21_Modify_the_record_zone_with_wrong_value(self):
        logging.info("Modify the record zone object with wrong value")
        data = {"zone": " subzone.domain.com"}
        status,response = ib_NIOS.wapi_request('GET', object_type="record:nsec", fields=json.dumps(data))
        print response
        print status
        logging.info(response)
        assert status == 400 and re.search(r'Invalid value for zone: .* subzone.domain.com.*: leading or trailing whitespace is not allowed.',response)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=22)
    def test_22_Get_operation_to_read_record_nsec_object_N(self):
        logging.info("Search operation for ttl field")
        data = {"ttl":"suzon"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ttl',response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=23)
    def test_23_Get_the_record_nsec_object(self):
        logging.info("Get the record nsec object")
        data = {"creator":"subzo"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for creator .*.* valid values are: SYSTEM, STATIC, DYNAMIC',response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=24)
    def test_24_Get_operation_to_read_record_nsec_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec_object_using_creator")
	search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?creator=SYSTEM")
        response = json.loads(search_record_nsec)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if i["name"] in ["domain.com","a.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=25)
    def test_25_Get_operation_to_read_record_nsec_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec_object_using_creator")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?creator=STATIC")
        response = json.loads(search_record_nsec)
        print response
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=26)
    def test_26_Get_operation_to_read_record_nsec_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec_object_using_creator")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?creator=DYNAMIC")
        response = json.loads(search_record_nsec)
        print response
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=27)
    def test_27_Get_operation_to_read_record_nsec__object_N(self):
        logging.info("Search operation for creation_time field")
        data = {"creation_time":"DYNAMIC"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: creation_time',response1)
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=28)
    def test_28_Get_operation_to_read_record_nsec__object_N(self):
        logging.info("Search operation for last_queried field")
        data = {"last_queried":35676}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: last_queried',response1)
        logging.info("Test Case 28 Execution Completed")


    @pytest.mark.run(order=29)
    def test_29_Get_operation_to_read_record_nsec_object_N(self):
        logging.info("Search operation for cloud_info field")
        data = {"cloud_info":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: cloud_info',response1)
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=30)
    def test_30_Get_operation_to_read_record_nsec_object_using_next_owner_name(self):
        logging.info("Get_operation_to_read_record_nsec_object_using_next_owner_name")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?next_owner_name=domain.com")
        response = json.loads(search_record_nsec)
        print response
	var= False
        if len(response)==1:
            for i in response:
                if i["name"] in ["a.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=31)
    def test_31_Get_operation_to_read_record_nsec_object_using_next_owner_name(self):
        logging.info("Get_operation_to_read_record_nsec_object_using_next_owner_name")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?next_owner_name:=Domain.com")
        response = json.loads(search_record_nsec)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["name"] in ["a.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=32)
    def test_32_Get_operation_to_read_record_nsec_object_using_next_owner_name(self):
        logging.info("Get_operation_to_read_record_nsec_object_using_next_owner_name")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec", params="?next_owner_name~=domain.co*")
        response = json.loads(search_record_nsec)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if i["name"] in ["domain.com","a.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var

        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=33)
    def test_33_Get_operation_to_read_record_nsec_object_N(self):
        logging.info("Search operation for dns_next_owner_name field")
        data = {"dns_next_owner_name":"domain.com"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: dns_next_owner_name',response1)
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=34)
    def test_34_Get_operation_to_read_record_nsec_object_N(self):
        logging.info("Search operation for rrset_types field")
        data = {"rrset_types":"domain.com"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: rrset_types',response1)
        logging.info("Test Case 34 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=35)
    def test_35_Modify_view_to_disable_dnssec(self):
        logging.info("Modify_view_to_disable_dnssec")
        data = {"dnssec_enabled":False}
        response = ib_NIOS.wapi_request('PUT',ref='view/ZG5zLnZpZXckLl9kZWZhdWx0:default/true',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response

    @pytest.mark.run(order=36)
    def test_36_delete_zone_auth_object(self):
        logging.info("delete_zone_auth_object")
        delete_zone_auth = ib_NIOS.wapi_request('DELETE',ref = 'zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4:domain.com/default')
        logging.info(delete_zone_auth)
        print delete_zone_auth
        logging.info("Test Case 36 Execution Completed")
        logging.info("============================")






    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")

