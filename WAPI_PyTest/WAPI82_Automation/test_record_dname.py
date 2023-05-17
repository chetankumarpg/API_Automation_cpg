import re
import config
import pytest
import unittest
import logging
import subprocess
import json
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
    def test_2_create_record_dname(self):
        logging.info("Create record dname with required fields")
        data = {"name": "bind_dname.domain.com","target": "target.org"}
        response = ib_NIOS.wapi_request('POST', object_type="record:dname",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=3)
    def test_3_create_record_dname_with_wrong_domain(self):
        logging.info("create record dname object with wrong domain name")
	data = {"name": "bind_dname.domain.c","target": "target.org"}
	status,response = ib_NIOS.wapi_request('POST', object_type='record:dname', fields=json.dumps(data))
	print response
	print status
	logging.info(response)
	assert status == 400 and re.search(r'The action is not allowed. A parent was not found.',response)
	logging.info("Test Case 3 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=4)
    def test_4_create_record_dname_with_wrong_target(self):
	logging.info("create record dname object with wrong target")
	data = {"name": "bind_dname.domain.com","target":True}
	status,response = ib_NIOS.wapi_request('POST', object_type='record:dname', fields=json.dumps(data))
	print response
	print status
	logging.info(response)
	assert status == 400 and re.search(r'Invalid value for target: true: Must be string type',response)
	logging.info("Test Case 4 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=5)
    def test_5_Get_record_dname_with_name(self):
        logging.info("Get record dname object with name")
        data = {"name": "bind_dname.domain.com"}
        record_dname = ib_NIOS.wapi_request('GET', object_type='record:dname', fields=json.dumps(data))
	res = json.loads(record_dname)
	print res
	for i in res:
	    assert  i["name"] == "bind_dname.domain.com" and i["target"] == "target.org" and i["view"] == "default"
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=6)
    def test_6_Get_record_dname_with_name(self):
        logging.info("Get record dname object with name using colon")
        record_dname = ib_NIOS.wapi_request('GET', object_type='record:dname', params="?name:=bind_dname.domain.com")
        res = json.loads(record_dname)
        print res
        for i in res:
            assert  i["name"] == "bind_dname.domain.com" and i["target"] == "target.org" and i["view"] == "default"
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=7)
    def test_7_Get_record_dname_with_name(self):
        logging.info("Get record dname object with name using negotation")
        record_dname = ib_NIOS.wapi_request('GET', object_type='record:dname', params="?name~=bind_dname.domain.com")
        res = json.loads(record_dname)
        print res
        for i in res:
            assert  i["name"] == "bind_dname.domain.com" and i["target"] == "target.org" and i["view"] == "default"
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=8)
    def test_8_Modify_the_record_dname_with_wrong_target(self):
        logging.info("Modify the record dname object with wrong target")
	data = {"comment": " testing record:dname"}
	status,response = ib_NIOS.wapi_request('PUT', ref='record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZQ:bind_dname.domain.com/default', fields=json.dumps(data))
	print response
	print status
	logging.info(response)
	assert status == 400 and re.search(r'Invalid value for comment: .* testing record:dname.*: leading or trailing whitespace is not allowed.',response)
	logging.info("Test Case 8 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=9)
    def test_9_Modify_the_record_dname(self):
        logging.info("Modify the record dname object")
	data = {"dns_name": "bind_dname.domain.com"}
	status,response = ib_NIOS.wapi_request('PUT', ref = 'record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZQ:bind_dname.domain.com/default', fields=json.dumps(data))
	print response
	print status
	logging.info(response)
	assert status == 400 and re.search(r'Field is not writable: dns_name',response)
	logging.info("Test Case 9 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=10)
    def test_10_Search_the_record_dname_object(self):
        logging.info("Search the record dname object")
	data = {"dns_name":" bind_dname.domain.com"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dname", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: dns_name",response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=11)
    def test_11_Search_the_record_dname_object_with_disable(self):
        logging.info("Search the record dname object with disable")
	data = {"disable":True}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dname", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: disable",response1)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=12)
    def test_12_Modify_the_record_dname_object_with_disable(self):
        logging.info("Modify the record dname object with disable")
	data = {"disable":"Tru"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZQ:bind_dname.domain.com/default', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for disable: .*Tru.*: Must be boolean type",response1)
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=13)
    def test_13_Get_the_record_dname_object_with_ttl(self):
        logging.info("Get the record dname object with ttl")
	data = {"ttl":""}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dname", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: ttl",response1)
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=14)
    def test_14_create_record_dname(self):
        logging.info("Create record dname with required fields")
        data = {"name": "bind_dname_ttl.domain.com","target": "target.org_ttl","ttl":429}
        response = ib_NIOS.wapi_request('POST', object_type="record:dname",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=15)
    def test_15_create_record_dname_with_modify_ttl(self):
        logging.info("Create record dname with required fields")
        data = {"ttl": 0}
        response = ib_NIOS.wapi_request('PUT', ref = "record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZV90dGw:bind_dname_ttl.domain.com/default",fields=json.dumps(data))
        logging.info("============================")
        print response
    @pytest.mark.run(order=16)
    def test_16_create_record_dname_for_view(self):
        logging.info("Create record dname with required fields for view")
        data = {"name": "bind_dname_view.domain.com","target": "target.org_view","view": "default"}
        response = ib_NIOS.wapi_request('POST', object_type="record:dname",fields=json.dumps(data))
        logging.info("============================")
        print response



    @pytest.mark.run(order=17)
    def test_17_Modify_the_record_dname_object_with_view(self):
        logging.info("Get the record dname object with view")
	data = {"view":"default"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = "record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZV92aWV3:bind_dname_view.domain.com/default", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not allowed for update: view",response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=18)
    def test_18_Get_operation_to_read_record_dname_object_with_view(self):
        logging.info("Get_operation_to_read_record_dname_object_with_view")
        search_record_dname = ib_NIOS.wapi_request('GET', object_type="record:dname", params="?view=default" )
        response = json.loads(search_record_dname)
        print response
        var= False
        if len(response)==3:
            for i in response:
                if i["name"] in ["bind_dname.domain.com","bind_dname_ttl.domain.com","bind_dname_view.domain.com"] and i["target"] in ["target.org","target.org_ttl","target.org_view"] and i["view"] in ["default"]:
				   var=True
				   
	assert var
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=19)
    def test_19_Get_operation_to_read_record_dname_object_with_zone(self):
        logging.info("Get_operation_to_read_record_dname_object_with_zone")
        search_record_dname = ib_NIOS.wapi_request('GET', object_type="record:dname", params="?zone=domain.com" )
        response = json.loads(search_record_dname)
        print response
        var= False
        if len(response)==3:
            for i in response:
                if i["name"] in ["bind_dname.domain.com","bind_dname_ttl.domain.com","bind_dname_view.domain.com"] and i["target"] in ["target.org","target.org_ttl","target.org_view"] and i["view"] in ["default"]:
				   var=True
				   
	    assert var

        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=20)
    def test_20_Modify_the_record_dname_object_with_zone(self):
        logging.info("Modify the record dname object with zone")
	data = {"zone":" domain.com"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZQ:bind_dname.domain.com/default', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not writable: zone",response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=21)
    def test_21_Search_operation_to_read_record_dname_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dname", params="?zone~=domain.com")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: zone",response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=22)
    def test_22_Search_operation_to_read_record_dname_object_with_colon(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dname", params="?zone:=domain.com")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: zone",response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=23)
    def test_23_Get_the_record_dname_with_wrong_zone(self):
        logging.info("Modify the record dname object with zone")
        data = {"zone": " domain.com"}
        status,response = ib_NIOS.wapi_request('GET', object_type="record:dname", fields=json.dumps(data))
        print response
        print status
        logging.info(response)
        assert status == 400 and re.search(r'Invalid value for zone: .* domain.com.*: leading or trailing whitespace is not allowed.',response)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=24)
    def test_24_delete_record_dname(self):
        logging.info("delete record dname with required fields")
        response = ib_NIOS.wapi_request('DELETE', ref = 'record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZV90dGw:bind_dname_ttl.domain.com/default')
        logging.info("============================")
        print response
    @pytest.mark.run(order=25)
    def test_25_delete_record_dname(self):
        logging.info("delete record dname with required fields")
        response = ib_NIOS.wapi_request('DELETE', ref = 'record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZV92aWV3:bind_dname_view.domain.com')
        logging.info("============================")
        print response


    @pytest.mark.run(order=26)
    def test_26_Search_operation_to_read_record_dname_object_with_extattrs(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_extattrs")
        extr = ib_NIOS.wapi_request('GET', object_type="record:dname", params="_return_fields=extattrs")
        logging.info(extr)
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=27)
    def test_27_Modify_the_record_dname_object_with_disable(self):
        logging.info("Modify the record dname object with disable")
        data = {"creator": " STATIC"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZQ:bind_dname.domain.com/default', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for creator .* STATIC.* valid values are: STATIC, DYNAMIC, SYSTEM",response1)
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=28)
    def test_28_Modify_the_record_dname_object_with_disable(self):
        logging.info("Modify the record dname object with disable")
        data = {"creator": "SYSTEM"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZQ:bind_dname.domain.com/default', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Creator of records cannot be changed to or from SYSTEM.",response1)
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=29)
    def test_29_Modify_the_record_dname_object_with_creator(self):
        logging.info("Modify the record dname object with creator")
        data = {"creator": "DYNAMIC"}
        creator = ib_NIOS.wapi_request('PUT', ref = 'record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZQ:bind_dname.domain.com/default', fields=json.dumps(data))
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=30)
    def test_30_Get_operation_to_read_record_dname_object_with_zone(self):
        logging.info("Get_operation_to_read_record_dname_object_with_zone")
	data = {"creator":"DYNAMIC"}
        search_record_dname = ib_NIOS.wapi_request('GET', object_type="record:dname", fields=json.dumps(data))
        response = json.loads(search_record_dname)
        print response
        var= False
	if len(response)==1:
            for i in response:
                if i["name"] in ["bind_dname.domain.com"] and i["target"] in ["target.org"] and i["view"] in ["default"]:
				   var=True
				   
	    assert var

    @pytest.mark.run(order=31)
    def test_31_Search_operation_to_read_record_dname_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dname", params="?creator~=DYNAMIC")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: creator",response1)
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=32)
    def test_32_Search_operation_to_read_record_dname_object_with_colon(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dname", params="?creator:=DYNAMIC")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: creator",response1)
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=33)
    def test_33_Search_operation_to_read_record_dname_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_negotation")
	data = {"name": "bind_dname.domain.com","target": "target.org","view": "default","creation_time": 1490159141}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="record:dname", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not writable: creation_time",response1)
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=34)
    def test_34_Modify_the_record_dname_object_with_creation_time(self):
        logging.info("Modify the record dname object with creation_time")
        data = {"creation_time":1490159141}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZQ:bind_dname.domain.com/default', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not writable: creation_time",response1)
        logging.info("Test Case 34 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=35)
    def test_35_Search_operation_to_read_record_dname_object_with_colon(self):
        logging.info("Get_operation_to_read_record_dnskey_object_with_colon")
	data = {"creation_time":1490159141}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dname", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: creation_time",response1)
        logging.info("Test Case 35 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=36)
    def test_36_create_operation_for_record_dname_object_with_ddns_principal(self):
        logging.info("create_operation_for_record_dname_object_with_ddns_principal")
	data = {"name": "bind_dname_ddns.domain.com","target": "target.org_ddns","ddns_principal": "ddns"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="record:dname", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Cannot assign DDNS principal to a resource record since the creator type of the record is not DYNAMIC.",response1)
        logging.info("Test Case 36 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=37)
    def test_37_Create_record_dname(self):
        logging.info("Create record dname with required fields")
	data = {"name": "bind_dname_ddns.domain.com","target": "target.org_ddns","ddns_principal": "ddns","creator": "DYNAMIC"}
        response = ib_NIOS.wapi_request('POST', object_type="record:dname", fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=38)
    def test_38_delete_record_dname(self):
        logging.info("delete record dname with required fields")
        response = ib_NIOS.wapi_request('DELETE', ref = 'record:dname/ZG5zLmJpbmRfZG5hbWUkLl9kZWZhdWx0LmNvbS5kb21haW4uYmluZF9kbmFtZV9kZG5z:bind_dname_ddns.domain.com/default')
        logging.info("============================")
        print response
	
    @pytest.mark.run(order=39)
    def test_39_create_operation_for_record_dname_object_with_ddns_protected(self):
        logging.info("create_operation_for_record_dname_object_with_ddns_protected")
	data = {"ddns_protected":True}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:dname", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: ddns_protected",response1)
        logging.info("Test Case 39 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=40)
    def test_40_Get_operation_to_read_record_dname_object_with_reclaimable(self):
        logging.info("Get_operation_to_read_record_dname_object_with_reclaimable")
	data = {"reclaimable":False}
        search_record_dname = ib_NIOS.wapi_request('GET', object_type="record:dname", fields=json.dumps(data))
        response = json.loads(search_record_dname)
        print response
        var= False
	if len(response)==1:
            for i in response:
                if i["name"] in ["bind_dname.domain.com"] and i["target"] in ["target.org"] and i["view"] in ["default"]:
		    var=True
				   
	    assert var



    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")
