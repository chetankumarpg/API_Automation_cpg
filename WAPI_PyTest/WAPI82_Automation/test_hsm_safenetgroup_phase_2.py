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
    def test_1_Get_the_fields_in_hsm_safenetgroup_object_N(self):
        logging.info("Get_the_fields_in_hsm_safenetgroup_object_N")
        status,response = ib_NIOS.wapi_request('GET', object_type="hsm:safenetgroup",params="?_return_fields=comment,group_sn,hsm_safenet,hsm_version,name,pass_phrase,status")
        print status
        print response
        logging.info(response)
        assert  status == 400 and re.search(r"Field is not readable: pass_phrase",response)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================") 


    @pytest.mark.run(order=2)
    def test_2_Get_the_all_fields_in_hsm_safenetgroup_object_comment_group_sn_hsm_safenet_hsm_version_name_status(self):
        logging.info("Get_the_all_fields_in_hsm_safenetgroup_object_comment_group_sn_hsm_safenet_hsm_version_name_status")
        response = ib_NIOS.wapi_request('GET', object_type="hsm:safenetgroup",)
        logging.info(response)
        print response
	read = re.search(r'200',response)
	for read in response:
		assert True
        logging.info("Test Case  Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=3)
    def test_3_Adding_the_hsm_safenet_object_to_pass_phrase_field_N(self):
        logging.info("Adding_the_hsm_safenet_object_to_pass_phrase_field_N")
        data = {"comment":"testing","group_sn": "1154441010\r","hsm_safenet": [{"disable": False,"is_fips_compliant": False,"name": "10.39.10.12","partition_capacity": 0,"partition_id":"DEVPartition","partition_serial_number": "154441010","status": "UP"}],"hsm_version": "LunaSA_5","name": "HSM_group","status": "UP"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'field for create missing: pass_phrase',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=4)
    def test_4_Adding_the_hsm_safenet_object_to_status_field_N(self):
        logging.info("Adding_the_hsm_safenet_object_to_status_field_N")
        data = {"comment":"testing","group_sn": "1154441010\r","hsm_safenet": [{"disable": False,"is_fips_compliant": False,"name": "10.39.10.12","partition_capacity": 0,"partition_id":"DEVPartition","partition_serial_number": "154441010","status": "UP"}],"hsm_version": "LunaSA_5","name": "HSM_group","status": "UP","pass_phrase":"MIIDVzCCAj+gAwIBAgIBADANBgkqhkiG9w0BAQsFADBvMQswCQYDVQQGEwJDQTEQ"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: status',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=5)
    def test_5_Adding_the_hsm_safenet_object_to_group_sn_field_N(self):
        logging.info("Adding_the_hsm_safenet_object_to_group_sn_field_N")
        data = {"comment":"testing","group_sn": "1154441010\r","hsm_safenet": [{"disable":False,"is_fips_compliant": False,"name": "10.39.10.12","partition_capacity": 0,"partition_id":"DEVPartition","partition_serial_number": "154441010","status": "UP"}],"hsm_version": "LunaSA_5","name": "HSM_group","pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: group_sn',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=6)
    def test_6_Adding_the_hsm_safenet_object_to_status_field_N(self):
        logging.info("Adding_the_hsm_safenet_object_to_status_field_N")
        data = {"comment":"testing","hsm_safenet": [{"disable": False,"is_fips_compliant": False,"name": "10.39.10.12","partition_capacity": 0,"partition_id": "DEVPartition","partition_serial_number":"154441010","status": "UP"}],"hsm_version": "LunaSA_5","name": "HSM_group","pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: status',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=7)
    def test_7_Adding_the_hsm_safenet_object_to_partition_capacity_field_N(self):
        logging.info("Adding_the_hsm_safenet_object_to_partition_capacity_field_N")
        data = {"comment":"testing","hsm_safenet": [{"disable": False,"is_fips_compliant": False,"name": "10.39.10.12","partition_capacity": 0,"partition_id": "DEVPartition","partition_serial_number":"154441010"}],"hsm_version": "LunaSA_5","name": "HSM_group","pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: partition_capacity',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=8)
    def test_8_Adding_the_hsm_safenet_object_to_is_fips_compliant_field_N(self):
        logging.info("Adding_the_hsm_safenet_object_to_is_fips_compliant_field_N")
        data = {"comment":"testing","hsm_safenet": [{"disable": False,"is_fips_compliant": False,"name": "10.39.10.12","partition_id": "DEVPartition","partition_serial_number":154441010}],"hsm_version": "LunaSA_5","name": "HSM_group","pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'AdmConProtoError: Field is not writable: is_fips_compliant',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")





    @pytest.mark.run(order=9)
    def test_9_Adding_the_hsm_safenet_object_to_partition_serial_number_field_N(self):
        logging.info("Adding_the_hsm_safenet_object_to_partition_serial_number_field_N")
        data = {"comment":"testing","hsm_safenet": [{"disable": False,"name": "10.39.10.12","partition_id": "DEVPartition","partition_serial_number": 154441010}],"hsm_version": "LunaSA_5","name":"HSM_group","pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for partition_serial_number: 154441010: Must be string type',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=10)
    def test_10_Adding_the_hsm_safenet_object_to_partition_id_field_N(self):
        logging.info("Adding_the_hsm_safenet_object_to_partition_id_field_N")
        data = {"comment":"testing","hsm_safenet": [{"disable": False,"name": "10.39.10.12","partition_id": "DEVPartition","partition_serial_number": "154441010"}],"hsm_version": "LunaSA_5","name":"HSM_group","pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: partition_id',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=11)
    def test_11_Adding_the_hsm_safenet_object_to_hsm_version_field_N(self):
        logging.info("Adding_the_hsm_safenet_object_to_hsm_version_field_N")
        data = {"comment": "testing","hsm_safenet": [{"disable": False,"name":"10.39.10.12","partition_serial_number":154441010,"server_cert":"eJydUMFuwjAMvedH4ELatLS03JgY0qSJTbCdrTZJmaU2yZJ0gr+fg7Rddtshlu3n915sKa27gdcX\nRkFaE6KfZbSeOcGWEs1g+9FeuTU6vXhzOrB9Fzs46YG5gkmAfsYxogFgCmVkrmRL5dbsvNBXh/4G\nESe9YK5iB7Fuq02er+uSF03T1GXLwnkx+5HgmggfMbqwzTKR87LiQjS8ylIPFNLnIgw4akCbef0J\nqFbvr88vu/1K5Hl1p7Scoii40xMJbpI2Ksoakv5LIeBur2gbykVOU1mg1buLzuLk/u8sxI8uaCOt\nQnNJ3YIMHp6OKS1/Byar0nFEutd+97aD0+Mh1RUL8eREnW4pNgQOqEcVIFqQdnKdv7MadkxL9p0D\nNG6O8KV9QGsS1hLW82+MCpMK\n"}],"hsm_version": "LunaSA_3","name": "HSM_group","pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for hsm_version .*LunaSA_3.* valid values are: LunaSA_4, LunaSA_5, LunaSA_6',response1)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")


    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")


