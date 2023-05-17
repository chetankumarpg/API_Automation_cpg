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
        data = {"fqdn":"qatest.com"}
        response = ib_NIOS.wapi_request('POST',object_type='zone_auth', fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=2)
    def test_2_Modify_the_zone_to_add_grid_primary_member(self):
        get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
        logging.info(get_ref)
        res = json.loads(get_ref)
        ref = json.loads(get_ref)[0]['_ref']
        print ref
	
        logging.info("Modify_the_zone_to_add_grid_primary_member")
        data = {"grid_primary": [{"name": config.grid_fqdn,"stealth":False}]}
        response = ib_NIOS.wapi_request('PUT',ref=ref,fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response

    @pytest.mark.run(order=3)
    def test_3_Create_A_record(self):
        logging.info("Create_A_record")
        data = {"ipv4addr":"1.1.1.1","name":"a.qatest.com"}
        response = ib_NIOS.wapi_request('POST',object_type='record:a', fields=json.dumps(data))
	print response
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=4)
    def test_4_create_for_sign_the_zone(self):
        get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
        logging.info(get_ref)
        res = json.loads(get_ref)
        ref = json.loads(get_ref)[0]['_ref']
        print ref
        logging.info("create_for_sign_the_zone")
        data = {"operation":"SIGN"}
        response = ib_NIOS.wapi_request('POST',ref=ref,params='?_function=dnssec_operation',fields=json.dumps(data))
        logging.info(response)
	print response
        logging.info("============================")

    @pytest.mark.run(order=5)
    def test_5_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
	response = ib_NIOS.wapi_request('GET', object_type="record:nsec3")
        logging.info(response)
        read  = re.search(r'200',response)
        for read in  response:
                   assert True
        logging.info("Test Case 5  Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=6)
    def test_6_create_record_nsec3_object_N(self):
        logging.info("create_record_nsec3_object_N")
        data = {"name": "qatest.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="record:nsec3",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for record:nsec3',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=7)
    def test_7_Delete_record_nsec3_object_N(self):
        logging.info("Delete_record_nsec3_object_N")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = 'record:nsec3/ZG5zLmJpbmRfZG5za2V5JC5fZGVmYXVsdC5jb20uZG9tYWluLjcuNDk5OTg:qatest.com/default')
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for record:nsec3',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=8)
    def test_8_Modify_record_nsec3_object_N(self):
        logging.info("Modify_record_nsec3_object_N")
        data = {"name": "qatest.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'record:nsec3/ZG5zLmJpbmRfZG5za2V5JC5fZGVmYXVsdC5jb20uZG9tYWluLjcuNDk5OTg:qatest.com/default', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation update not allowed for record:nsec3',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=9)
    def test_9_Get_operation_to_read_record_nsec3_object_N(self):
        logging.info("Search operation for dns_name fields")
        data = {"dns_name":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: dns_name',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=13)
    def test_13_Get_operation_to_read_record_nsec3_object_using_flags(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_flags")
	search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?flags=0")
        response = json.loads(search_record_nsec3)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if "qatest.com" in i["name"]  and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=14)
    def test_14_Get_operation_to_read_record_nsec3_object_using_flags(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_flags")
        search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?flags<=0")
        response = json.loads(search_record_nsec3)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if "qatest.com" in i["name"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=15)
    def test_15_Get_operation_to_read_record_nsec3_object_using_flags(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_flags")
        search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?flags>=0")
        response = json.loads(search_record_nsec3)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if "qatest.com" in i["name"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=16)
    def test_16_Get_operation_to_read_record_nsec3_object_using_view(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_view")
	search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?view=default")
        response = json.loads(search_record_nsec3)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if "qatest.com" in i["name"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=17)
    def test_17_Get_operation_to_read_record_nsec3_object_using_view(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_view")
        search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?zone=qatest.com")
        response = json.loads(search_record_nsec3)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if "qatest.com" in i["name"]  and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=18)
    def test_18_Get_operation_to_read_record_nsec3_object_N(self):
        logging.info("Search operation for ttl field")
        data = {"ttl":"suzon"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ttl',response1)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=19)
    def test_19_Get_the_record_nsec3_object(self):
        logging.info("Get the record nsec3 object")
        data = {"creator":"subzo"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for creator .*.* valid values are: SYSTEM, STATIC, DYNAMIC',response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=20)
    def test_20_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
	search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?creator=SYSTEM")
        response = json.loads(search_record_nsec3)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if "qatest.com" in i["name"]  and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=21)
    def test_21_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
        search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?creator=STATIC")
        response = json.loads(search_record_nsec3)
        print response
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=22)
    def test_22_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
        search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?creator=STATIC")
        response = json.loads(search_record_nsec3)
        print response
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=23)
    def test_23_Get_operation_to_read_record_nsec3__object_N(self):
        logging.info("Search operation for creation_time  field")
        data = {"creation_time":"DYNAMIC"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: creation_time',response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=24)
    def test_24_Get_operation_to_read_record_nsec3__object_N(self):
        logging.info("Search operation for last_queried field")
        data = {"last_queried":35676}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: last_queried',response1)
        logging.info("Test Case 24 Execution Completed")

    @pytest.mark.run(order=25)
    def test_25_Get_operation_to_read_record_nsec3_object_N(self):
        logging.info("Search operation for cloud_info field")
        data = {"cloud_info":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: cloud_info',response1)
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=26)
    def test_26_Get_operation_to_read_record_nsec3_object_N(self):
        logging.info("Search operation for next_owner_name field")
        data = {"next_owner_name":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: next_owner_name',response1)
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=27)
    def test_27_Get_operation_to_read_record_nsec3_object_N(self):
        logging.info("Search operation for rrset_types field")
        data = {"rrset_types":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: rrset_types',response1)
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=28)
    def test_28_Get_the_record_nsec3_object(self):
        logging.info("Get the record nsec3 object")
        data = {"algorithm":"subzo"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for algorithm .*.* valid values are: RSAMD5, RSASHA1, RSASHA512, NSEC3DSA, NSEC3RSASHA1, RSASHA256, DSA',response1)
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=29)
    def test_29_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?algorithm=RSAMD5")
        response = json.loads(search_record_nsec)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if "qatest.com" in i["name"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=30)
    def test_30_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?algorithm=RSASHA1")
        response = json.loads(search_record_nsec)
        print response
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=31)
    def test_31_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?algorithm=RSASHA512")
        response = json.loads(search_record_nsec)
        print response
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=32)
    def test_32_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?algorithm=NSEC3DSA")
        response = json.loads(search_record_nsec)
        print response
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=33)
    def test_33_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?algorithm=NSEC3RSASHA1")
        response = json.loads(search_record_nsec)
        print response
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=34)
    def test_34_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?algorithm=RSASHA256")
        response = json.loads(search_record_nsec)
        print response
        logging.info("Test Case 34 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=35)
    def test_35_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?algorithm=DSA")
        response = json.loads(search_record_nsec)
        print response
        logging.info("Test Case 35 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=36)
    def test_36_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
	search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?iterations=10")
        response = json.loads(search_record_nsec3)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if "qatest.com" in i["name"]  and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 36 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=37)
    def test_37_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
        search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?iterations<=10")
        response = json.loads(search_record_nsec3)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if "qatest.com" in i["name"]  and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 37 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=38)
    def test_38_Get_operation_to_read_record_nsec3_object_using_creator(self):
        logging.info("Get_operation_to_read_record_nsec3_object_using_creator")
        search_record_nsec3 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", params="?iterations>=10")
        response = json.loads(search_record_nsec3)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if "qatest.com" in i["name"]  and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 38 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=39)
    def test_39_Get_operation_to_read_record_nsec_object_N(self):
        logging.info("Search operation for salt field")
        data = {"salt":"qatest.com"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:nsec3", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: salt',response1)
        logging.info("Test Case 39 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=40)
    def test_40_DELETE_record_nsec(self):
        get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
        logging.info(get_ref)
        res = json.loads(get_ref)
        ref = json.loads(get_ref)[0]['_ref']
        print ref
        logging.info("DELETE record_nsec")
        response1 = ib_NIOS.wapi_request('DELETE', object_type=ref)
        print response1
        logging.info(response1)
        logging.info("Test Case 40 Execution Completed")
        logging.info("============================")
    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")


