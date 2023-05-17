import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class Ipv6_address_range_template(unittest.TestCase):


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
        def test_1_create_ipv6addressrangetemplate(self):
                logging.info("Create ipv6addressrangetemplate Test")
                data = {"name": "customtemplate1","number_of_addresses": 2048,"offset": 24}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6rangetemplate", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=2)
        #Test the "creation" of entry in "ipv6addressrangetemplate" structure
        def test_2_duplicate_ipv6addressrangetemplate(self):
                logging.info("creating ipv6addressrangetemplate Test")
                data = {"name": "customtemplate1","number_of_addresses": 2048,"offset": 24}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6rangetemplate", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConDataError: None',response)
                logging.info("Test Case 2 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=3)
        def test_3_name_ipv6addressrangetemplate(self):
                logging.info("name in ipv6addressrangetemplate Test")
                data = {"number_of_addresses": 2048,"offset": 24}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6rangetemplate", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: field for create missing: name',response)
                logging.info("Test Case 3 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=4)
        def test_4_address_ipv6addressrangetemplate(self):
                logging.info("address in ipv6addressrangetemplate Test")
                data = {"name": "customtemplate2","offset": 24}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6rangetemplate", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: field for create missing: number_of_addresses',response)
                logging.info("Test Case 4 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=5)
        def test_5_offset_ipv6addressrangetemplate(self):
                logging.info("offset in ipv6addressrangetemplate Test")
                data = {"name": "customtemplate1","number_of_addresses": 2048}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6rangetemplate", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: field for create missing: offset',response)
                logging.info("Test Case 5 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=6)
        def test_6_duplicate_name_ipv6addressrangetemplate(self):
                logging.info("Test dupliacte name field in ipv6addressrangetemplate")
                data = {"name": "customtemplate1","number_of_addresses": 2048,"offset": 24}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6rangetemplate", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'IBDataConflictError:',response)
                logging.info("Test Case 6 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=7)
        def test_7_get_ipv6addressrangetemplate(self):
                logging.info("Get get details using name ipv6addressrangetemplate")
                data = {"name": "customtemplate1"}
                response = ib_NIOS.wapi_request('GET', object_type="ipv6rangetemplate", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 7 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=8)
        def test_8_create_comment__ipv6addressrangetemplate(self):
                logging.info("Create ipv6addressrangetemplate Test")
                data = {"name": "customtemplate13","number_of_addresses": 2048,"offset": 24,"comment": "for the testing purpose"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6rangetemplate", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 8 Execution Completed")
                logging.info("============================")

         
        @pytest.mark.run(order=9)
        def test_9_duplicate_name_ipv6addressrangetemplate(self):
                logging.info("Test dupliacte name field in ipv6addressrangetemplate")
                data = {"offset": "48"}
                status,response = ib_NIOS.wapi_request('GET', object_type="ipv6rangetemplate", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: offset',response)
                logging.info("Test Case 9 Execution Completed")
                logging.info("============================")
 

  
        @pytest.mark.run(order=10)
        def test_10_get_ipv6addressrangetemplate(self):
                logging.info("serach details using offset using ipv6addressrangetemplate")
                data = {"name": "customtemplate1"}
                response = ib_NIOS.wapi_request('GET', object_type="ipv6rangetemplate", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 10 Execution Completed")
                logging.info("============================")

      
        @pytest.mark.run(order=11)
        def test_11_get_ipv6addressrangetemplate(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6rangetemplate")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref

                logging.info("edit details using offset using ipv6addressrangetemplate")
                data = {"name": "customtemplate22"}
                response = ib_NIOS.wapi_request('PUT', object_type=ref, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 11 Execution Completed")
                logging.info("============================")

 
        @pytest.mark.run(order=12)
        def test_12_get_ipv6addressrangetemplate(self):
		
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6rangetemplate")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("edit details using offset using ipv6addressrangetemplate")
                data = {"comment": "for the testing purpouse"}
                response = ib_NIOS.wapi_request('PUT', object_type=ref, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 12 Execution Completed")
                logging.info("============================")
       

        @pytest.mark.run(order=13)
        def test_13_get_ipv6addressrangetemplate(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6rangetemplate")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("delete entry for ipv6addressrangetemplate")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 13 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=14)
        def test_14_DELETE_ipv6addressrangetemplate(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6rangetemplate")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("delete entry for ipv6addressrangetemplate")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 14 Execution Completed")
                logging.info("============================")




        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

 

