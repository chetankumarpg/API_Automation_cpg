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
    def test_1_create_zone(self):
        logging.info("Create zone with required fields")
        data = {"fqdn": "domain.com","view": "default"}
        response = ib_NIOS.wapi_request('POST', object_type="zone_auth",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=2)
    def test_2_create_grid_primary_for_zone(self):
        logging.info("Create grid_primary with required fields")
        data = {"grid_primary": [{"name": config.grid_fqdn ,"stealth":False}]}
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
        data = {"grid_primary": [{"name": config.grid_fqdn ,"stealth":False}]}
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
    def test_7_Get_operation_to_read_record_rrsig_object(self):
        logging.info("Get_operation_to_read_record_rrsig_object")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig")
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==14:
            for i in response:
                if i["name"] in ["domain.com","domain.com","domain.com","domain.com","qkp1cg3a6l8b2ksta3asuc1jf5ni2lul.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sf5q28fgbk6jdg3r0tskl4q5r0o9lkts.sub.domain.com","l19s7aiv647k0nkpdah6i1ua4i84e0cf.domain.com","sub.domain.com","sub.domain.com","domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=8)
    def test_8_create_record_rrsig_object_N(self):
        logging.info("create_record_rrsig_object_N")
        data = {"name": "domain.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="record:rrsig",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for record:rrsig',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=9)
    def test_9_Delete_record_rrsig_object_N(self):
        logging.info("Delete_record_rrsig_object_N")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = 'record:rrsig/ZG5zLmJpbmRfZG5za2V5JC5fZGVmYXVsdC5jb20uZG9tYWluLjcuNDk5OTg:domain.com/default')
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for record:rrsig',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=10)
    def test_10_Modify_record_rrsig_object_N(self):
        logging.info("Modify_record_rrsig_object_N")
        data = {"name": "domain.com","view": "default"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'record:rrsig/ZG5zLmJpbmRfZG5za2V5JC5fZGVmYXVsdC5jb20uZG9tYWluLjcuNDk5OTg:domain.com/default', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation update not allowed for record:rrsig',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")  

    @pytest.mark.run(order=11)
    def test_11_schedule_creation_for_record_rrsig(self):
        logging.info("schedule_creation_for_record_rrsig")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="record:rrsig",params="?_schedinfo.scheduled_time=2123235895")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for record:rrsig',response1)
        logging.info("Test Case 11 Execution Completed")


    @pytest.mark.run(order=12)
    def test_12_Modify_the_record_rrsig_object(self):
        logging.info("Modify the record rrsig object")
        data = {"algorithm": "thu"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for algorithm .* valid values are: RSAMD5, ECDSAP256SHA256, ECDSAP384SHA384, RSASHA256, RSASHA512, NSEC3DSA, NSEC3RSASHA1, RSASHA1, DSA",response1)
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=13)
    def test_13_Get_the_record_rrsig_object_using_algorithm_RSAMD5(self):
        logging.info("Modify_the_record_rrsig_object_using_algorithm_RSAMD5")
        data = {"algorithm": "RSAMD5"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=14)
    def test_14_Get_the_record_rrsig_object_using_algorithm_ECDSAP256SHA256(self):
        logging.info("Modify_the_record_rrsig_object_using_algorithm_ECDSAP256SHA256")
        data = {"algorithm": "ECDSAP256SHA256"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=15)
    def test_15_Get_the_record_rrsig_object_using_algorithm_ECDSAP384SHA384(self):
        logging.info("Modify_the_record_rrsig_object_using_algorithm_ECDSAP384SHA384")
        data = {"algorithm": "ECDSAP384SHA384"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=16)
    def test_16_Get_operation_to_read_record_rrsig_object(self):
        logging.info("Get_operation_to_read_record_rrsig_object")
        data = {"algorithm":"RSASHA256"}
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==14:
            for i in response:
                if i["name"] in ["domain.com","domain.com","domain.com","domain.com","eica2858k7lb24buf1in8oulji94uqet.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","tlm6b4jc62cemjupj6rf6ei4bjq7qrgc.sub.domain.com","bkljcf7e2i2la4tfd0bcip55o8ugseig.domain.com","sub.domain.com","sub.domain.com","domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=17)
    def test_17_Get_the_record_rrsig_object_using_algorithm_RSASHA512(self):
        logging.info("Modify_the_record_rrsig_object_using_algorithm_RSASHA512")
        data = {"algorithm": "RSASHA512"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=18)
    def test_18_Get_the_record_rrsig_object_using_algorithm_NSEC3DSA(self):
        logging.info("Modify_the_record_rrsig_object_using_algorithm_NSEC3DSA")
        data = {"algorithm": "NSEC3DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=19)
    def test_19_Get_the_record_rrsig_object_using_algorithm_NSEC3RSASHA1(self):
        logging.info("Modify_the_record_rrsig_object_using_algorithm_NSEC3RSASHA1")
        data = {"algorithm": "NSEC3RSASHA1"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=20)
    def test_20_Get_the_record_rrsig_object_using_algorithm_RSASHA1(self):
        logging.info("Modify_the_record_rrsig_object_using_algorithm_RSASHA1")
        data = {"algorithm": "RSASHA1"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=21)
    def test_21_Get_the_record_rrsig_object_using_algorithm_DSA(self):
        logging.info("Modify_the_record_rrsig_object_using_algorithm_DSA")
        data = {"algorithm": "DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=22)
    def test_22_Search_operation_to_read_record_rrsig_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?algorithm~=NSEC3RSASHA1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: algorithm",response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=23)
    def test_23_Search_operation_to_read_record_rrsig_object_with_colon(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?algorithm:=NSEC3RSASHA1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: algorithm",response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=24)
    def test_24_Get_operation_to_read_record_rrsig_object_N(self):
        logging.info("Search operation for allow_uploads fields with ~:= modifier")
        data = {"cloud_info":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: cloud_info',response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=25)
    def test_25_Get_operation_to_read_record_rrsig_object(self):
        logging.info("Get_operation_to_read_record_rrsig_object")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?name=domain.com")
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==5:
            for i in response:
                if i["name"] in ["domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=26)
    def test_26_Get_operation_to_read_record_rrsig_object(self):
        logging.info("Get_operation_to_read_record_rrsig_object")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?name:=domain.com")
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==5:
            for i in response:
                if i["name"] in ["domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=27)
    def test_27_Get_operation_to_read_record_rrsig_object(self):
        logging.info("Get_operation_to_read_record_rrsig_object")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?name~=domain.co*" )
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==14:
            for i in response:
                if i["name"] in ["domain.com","domain.com","domain.com","domain.com","h8e28tufcjjav3338045s7nmcgtf2ooj.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","oh72b27c94b0ga188uc2asvd42g4s583.sub.domain.com","9e439k4d6t3ma0sgcoa6hi7fohcd3rc4.domain.com","sub.domain.com","sub.domain.com","domain.com",] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=28)
    def test_28_Get_operation_to_read_record_rrsig_object_N(self):
        logging.info("Search operation for allow_uploads fields with ~:= modifier")
        data = {"dns_name":"DSA"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: dns_name',response1)
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=29)
    def test_29_Get_operation_to_read_record_rrsig_object_with_view(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_view")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?view=default" )
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==14:
            for i in response:
                if i["name"] in ["domain.com","domain.com","domain.com","domain.com","domain.com","nour42m3fsvvtc0cj47e2c10hvhgumie.domain.com","rdmdun79i809l2g014rskhg964r2ikam.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","npef89juel4vl04o3hor5rqoolbgup1j.sub.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=30)
    def test_30_Search_operation_to_read_record_rrsig_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?view~=defaul*")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: view",response1)
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=31)
    def test_31_Search_operation_to_read_record_rrsig_object_with_colon(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?view:=Default")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: view",response1)
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=32)
    def test_32_Get_operation_to_read_record_rrsig_object_with_view(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_view")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?zone=sub.domain.com" )
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==6:
            for i in response:
                if i["name"] in ["sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","npef89juel4vl04o3hor5rqoolbgup1j.sub.domain.com","npef89juel4vl04o3hor5rqoolbgup1j.sub.domain.com","sub.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=33)
    def test_33_Search_operation_to_read_record_rrsig_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?zone~=sub.domain.com")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: zone",response1)
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=34)
    def test_34_Search_operation_to_read_record_rrsig_object_with_colon(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?zone:=sub.domain.com")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: zone",response1)
        logging.info("Test Case 34 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=35)
    def test_35_Modify_the_record_dname_with_wrong_target(self):
        logging.info("Modify the record dname object with wrong target")
        data = {"zone": " subzone.domain.com"}
        status,response = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print response
        print status
        logging.info(response)
        assert status == 400 and re.search(r'Invalid value for zone: .* subzone.domain.com.*: leading or trailing whitespace is not allowed.',response)
        logging.info("Test Case 35 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=36)
    def test_36_Get_operation_to_read_record_rrsig_object_N(self):
        logging.info("Search operation for ttl field")
        data = {"ttl":"suzon"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ttl',response1)
        logging.info("Test Case 36 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=37)
    def test_37_Get_the_record_rrsig_object(self):
        logging.info("Get the record rrsig object")
        data = {"creator":"subzo"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for creator .*.* valid values are: SYSTEM, STATIC, DYNAMIC',response1)
        logging.info("Test Case 37 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=38)
    def test_38_Get_operation_to_read_record_rrsig_object_with_creator(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_creator")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?creator=SYSTEM" )
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==14:
            for i in response:
                if i["name"] in ["domain.com","domain.com","domain.com","domain.com","nour42m3fsvvtc0cj47e2c10hvhgumie.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","npef89juel4vl04o3hor5rqoolbgup1j.sub.domain.com","rdmdun79i809l2g014rskhg964r2ikam.domain.com","sub.domain.com","sub.domain.com","domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 38 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=39)
    def test_39_Get_operation_to_read_record_rrsig_object_with_creator(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_creator")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?creator=STATIC" )
        response = json.loads(search_record_rrsig)
        print response
        logging.info("Test Case 39 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=40)
    def test_40_Get_operation_to_read_record_rrsig_object_with_creator(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_creator")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?creator=DYNAMIC" )
        response = json.loads(search_record_rrsig)
        print response
        logging.info("Test Case 40 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=41)
    def test_41_Get_operation_to_read_record_rrsig_object_N(self):
        logging.info("Search operation for ttl field")
        data = {"creation_time":"DYNAMIC"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: creation_time',response1)
        logging.info("Test Case 41 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=42)
    def test_42_Get_operation_to_read_record_rrsig_object_N(self):
        logging.info("Search operation for ttl field")
        data = {"last_queried":35676}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: last_queried',response1)
        logging.info("Test Case 42 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=43)
    def test_43_Get_operation_to_read_record_rrsig_object_with_type_covered(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_type_covered")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?type_covered=DS" )
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["name"] in ["sub.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 43 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=43)
    def test_43_Get_operation_to_read_record_rrsig_object_with_type_covered_with_colon_modifier(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_type_covered")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?type_covered:=dS" )
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["name"] in ["sub.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 43 Execution Completed")
        logging.info("============================")

		

    @pytest.mark.run(order=44)
    def test_44_Get_operation_to_read_record_rrsig_object_with_type_covered_with_colon_modifier(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_type_covered")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?type_covered~=D*")
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==14:
            for i in response:
                if i["name"] in ["domain.com","domain.com","domain.com","domain.com","0fi2j378sc3el1ec74o4ej391bs8nehh.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","qt0j0jek9ichd1op5tev94843gsiivmb.sub.domain.com","27smlu0g871009jr0h2sg1j64mvcn9q4.domain.com","sub.domain.com","sub.domain.com","domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 44 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=46)
    def test_46_Modify_the_record_dname_with_wrong_type_covered(self):
        logging.info("Modify the record dname object with wrong type_covered")
        data = {"type_covered": " DS"}
        status,response = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print response
        print status
        logging.info(response)
        assert status == 400 and re.search(r'Invalid value for type_covered: .*.*: leading or trailing whitespace is not allowed.',response)
        logging.info("Test Case 46 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=47)
    def test_47_Get_operation_to_read_record_rrsig_object_with_type_covered_with_colon_modifier(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_type_covered")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?labels=2" )
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==5:
            for i in response:
                if i["name"] in ["domain.com","domain.com","domain.com","domain.com","domain.com"] and i["view"] in ["default"]:
                    var=True


        assert var
        logging.info("Test Case 47 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=48)
    def test_48_Search_operation_to_read_record_rrsig_object_with_negotation(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_negotation")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?original_ttl~=28800")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: original_ttl",response1)
        logging.info("Test Case 48 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=49)
    def test_49_Search_operation_to_read_record_rrsig_object_with_colon(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_colon")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", params="?original_ttl:=28800")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: original_ttl",response1)
        logging.info("Test Case 49 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=50)
    def test_50_Get_operation_to_read_record_rrsig_object_with_original_ttl(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_original_ttl")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?original_ttl=28800" )
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==5:
            for i in response:
                if i["name"] in ["domain.com","sub.domain.com","sub.domain.com","sub.domain.com","domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 50 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=51)
    def test_51_Get_operation_to_read_record_rrsig_object_with_expiration_timeN(self):
        logging.info("Search operation for field expiration_time")
        data = {"expiration_time":28800}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: expiration_time',response1)
        logging.info("Test Case 51 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=52)
    def test_52_Get_operation_to_read_record_rrsig_object_with_inception_timeN(self):
        logging.info("Search operation for field inception_time")
        data = {"inception_time":28800}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: inception_time',response1)
        logging.info("Test Case 52 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=53)
    def test_53_Get_operation_to_read_record_rrsig_object_with_signer_name(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_signer_name")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?signer_name=sub.domain.com" )
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==6:
            for i in response:
                if i["name"] in ["sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","qt0j0jek9ichd1op5tev94843gsiivmb.sub.domain.com","sub.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 53 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=54)
    def test_54_Get_operation_to_read_record_rrsig_object_with_signer_name_using_colon(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_signer_name")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?signer_name:=Sub.domain.com" )
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==6:
            for i in response:
                if i["name"] in ["sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","qt0j0jek9ichd1op5tev94843gsiivmb.sub.domain.com","sub.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 54 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=55)
    def test_55_Get_operation_to_read_record_rrsig_object_with_signer_name_using_negotation(self):
        logging.info("Get_operation_to_read_record_rrsig_object_with_signer_name")
        search_record_rrsig = ib_NIOS.wapi_request('GET', object_type="record:rrsig",params="?signer_name~=sub.domain.co*")
        response = json.loads(search_record_rrsig)
        print response
        var= False
        if len(response)==6:
            for i in response:
                if i["name"] in ["sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","sub.domain.com","qt0j0jek9ichd1op5tev94843gsiivmb.sub.domain.com","sub.domain.com"] and i["view"] in ["default"]:
                    var=True

        assert var
        logging.info("Test Case 55 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=56)
    def test_56_Get_operation_to_read_record_rrsig_object_with_dns_signer_name_N(self):
        logging.info("Search operation for field dns_signer_name")
        data = {"dns_signer_name":"subzone.domain.com"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: dns_signer_name',response1)
        logging.info("Test Case 56 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=57)
    def test_57_Get_operation_to_read_record_rrsig_object_with_dns_signature_N(self):
        logging.info("Search operation for field signature")
        data = {"signature":"subzone.domain.com"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="record:rrsig", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: signature',response1)
        logging.info("Test Case 57 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=58)
    def test_58_delete_zone_auth_sub_zone_object(self):
        logging.info("delete_zone_auth_sub_zone_object")
        delete_zone_auth = ib_NIOS.wapi_request('DELETE',ref = 'zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4uc3Vi:sub.domain.com/default')
        logging.info(delete_zone_auth)
        print delete_zone_auth
        logging.info("Test Case 58 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=59)
    def test_59_delete_zone_auth_zone_object(self):
        logging.info("delete_zone_auth_zone_object")
        delete_zone_auth = ib_NIOS.wapi_request('DELETE',ref = 'zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmNvbS5kb21haW4:domain.com/default')
        logging.info(delete_zone_auth)
        print delete_zone_auth
        logging.info("Test Case 59 Execution Completed")
        logging.info("============================")
        logging.info("Perform Publish Operation")
        grid =  ib_NIOS.wapi_request('GET', object_type="grid")
        ref = json.loads(grid)[0]['_ref']
        publish={"member_order":"SIMULTANEOUSLY"}
        request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
        sleep(10)
        request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
        restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")





    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")
