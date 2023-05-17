import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class nat_group(unittest.TestCase):

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
        def test_1_create_ipv6dhcpoptiondefinition(self):
                logging.info("Create ipv6dhcpoptiondefinition Test")
                data = {"code": 23331,"name": "test1","type": "32-bit signed integer"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptiondefinition", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")
				
	@pytest.mark.run(order=2)
        def test_2_DELETE_ipv6dhcpoptiondefinition(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[17]['_ref']
                print ref
                logging.info("delete entry for ipv6dhcpoptiondefinition")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 2 Execution Completed")
                logging.info("============================")
				
				
	@pytest.mark.run(order=3)
	def test_3_create_ipv6dhcpoptiondefinition(self):
                logging.info("Create ipv6dhcpoptiondefinition Test with 32-bit usigned integer")
                data = {"code": 23331,"name": "test2","type": "32-bit unsigned integer"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptiondefinition", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")
				
				
				
				
	@pytest.mark.run(order=4)		
	def test_4_get_ipv6dhcpoptiondefinition(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[17]['_ref']
                print ref
                logging.info("delete entry for ipv6dhcpoptiondefinition")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 4 Execution Completed")
                logging.info("============================")
				
				
	@pytest.mark.run(order=5)
        def test_5_create_ipv6dhcpoptiondefinition(self):
                logging.info("Create ipv6dhcpoptiondefinition Test with 8-bit usigned integer")
                data = {"code": 23323,"name": "test3","type": "8-bit signed integer"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptiondefinition", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 5 Execution Completed")
                logging.info("============================")
				
	@pytest.mark.run(order=6)
        def test_6_get_ipv6dhcpoptiondefinition(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[17]['_ref']
                print ref
                logging.info("delete entry for ipv6dhcpoptiondefinition")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 6 Execution Completed")
                logging.info("============================")
				
	@pytest.mark.run(order=7)
        def test_7_create_ipv6dhcpoptiondefinition(self):
                logging.info("Create ipv6dhcpoptiondefinition Test")
                data = {"code": 23323,"name": "test4","type": "8-bit unsigned integer"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptiondefinition", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 7 Execution Completed")
                logging.info("============================")
				
	@pytest.mark.run(order=8)
        def test_8_get_ipv6dhcpoptiondefinition(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[17]['_ref']
                print ref
                logging.info("delete entry for ipv6dhcpoptiondefinition with 8-bit usigned integer")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 8 Execution Completed")
                logging.info("============================")
				
				
	@pytest.mark.run(order=9)
        def test_9_create_ipv6dhcpoptiondefinition(self):
                logging.info("Create ipv6dhcpoptiondefinition Test array of 32-bit signed integer")
                data = {"code": 23323,"name": "test5","type": "array of 32-bit unsigned integer"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptiondefinition", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 9 Execution Completed")
                logging.info("============================")
				
	@pytest.mark.run(order=10)
        def test_10_get_ipv6dhcpoptiondefinition(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[17]['_ref']
                print ref
                logging.info("delete entry for ipv6dhcpoptiondefinition with array of 32-bit signed integer")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 6 Execution Completed")
                logging.info("============================")
				
				
	@pytest.mark.run(order=11)
        def test_11_create_ipv6dhcpoptiondefinition(self):
                logging.info("Create ipv6dhcpoptiondefinition Test with array of 32-bit unsigned integer")
                data = {"code": 23323,"name": "test6","type": "array of 32-bit unsigned integer"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptiondefinition", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 11 Execution Completed")
                logging.info("============================")
				
	@pytest.mark.run(order=12)
        def test_12_get_ipv6dhcpoptiondefinition(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[17]['_ref']
                print ref
                logging.info("delete entry for ipv6dhcpoptiondefinition with array of 32-bit unsigned integer")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 12 Execution Completed")
                logging.info("============================")
				
	@pytest.mark.run(order=13)
        def test_13_create_ipv6dhcpoptiondefinition(self):
                logging.info("Create ipv6dhcpoptiondefinition Test with array of 8-bit signed integer")
                data = {"code": 23323,"name": "test7","type": "array of 8-bit unsigned integer"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptiondefinition", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 13 Execution Completed")
                logging.info("============================")
				
	@pytest.mark.run(order=14)
        def test_14_get_ipv6dhcpoptiondefinition(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[17]['_ref']
                print ref
                logging.info("delete entry for ipv6dhcpoptiondefinition with array of 8-bit signed integer")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 14 Execution Completed")
                logging.info("============================")
	
	@pytest.mark.run(order=15)
        def test_15_create_ipv6dhcpoptiondefinition(self):
                logging.info("Create ipv6dhcpoptiondefinition Test with array of array of ipv6-address")
                data = {"code": 23323,"name": "test8","type": "16-bit unsigned integer"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptiondefinition", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 15 Execution Completed")
                logging.info("============================")
				
	@pytest.mark.run(order=16)
        def test_16_get_ipv6dhcpoptiondefinition(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[17]['_ref']
                print ref
                logging.info("delete entry for ipv6dhcpoptiondefinition with array of 8-bit signed integer")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 16 Execution Completed")
                logging.info("============================")
				
				
	@pytest.mark.run(order=17)
        def test_17_create_ipv6dhcpoptiondefinition(self):
                logging.info("Create ipv6dhcpoptiondefinition Test with boolean")
                data = {"code": 23323,"name": "test9","type": "boolean"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptiondefinition", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 17 Execution Completed")
                logging.info("============================")
				
	@pytest.mark.run(order=18)
        def test_18_get_ipv6dhcpoptiondefinition(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[17]['_ref']
                print ref
                logging.info("delete entry for ipv6dhcpoptiondefinition with array of 8-bit signed integer")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 18 Execution Completed")
                logging.info("============================")
				
				
	@pytest.mark.run(order=19)
        def test_19_create_ipv6dhcpoptiondefinition(self):
                logging.info("Create ipv6dhcpoptiondefinition Test with domain-list")
                data = {"code": 23323,"name": "test10","type": "boolean"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptiondefinition",fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 19 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=20)
        def test_20_get_ipv6dhcpoptiondefinition(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[17]['_ref']
                print ref
                logging.info("delete entry for ipv6dhcpoptiondefinition with domain-list")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 20 Execution Completed")
                logging.info("============================")
				
				
				
				
	@pytest.mark.run(order=21)
        def test_21_create_ipv6dhcpoptiondefinition(self):
                logging.info("Create ipv6dhcpoptiondefinition Test")
                data = {"code": 23331,"name": "test11","type": "32-bit signed integer"}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptiondefinition", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 21 Execution Completed")
                logging.info("============================")
				
				
	@pytest.mark.run(order=22)
        def test_22_get_ipv6dhcpoptiondefinition(self):
                logging.info("Get get details using name ipv6dhcpoptiondefinition")
                response = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 22 Execution Completed")
                logging.info("============================")
				
	@pytest.mark.run(order=23)
        def test_22_get_ipv6dhcpoptiondefinition(self):
                logging.info("Get get details using code")
		data ={"name":"test11"}
                response = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 22 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=24)
        def test_24_get_ipv6dhcpoptiondefinition(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptiondefinition")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[17]['_ref']
                print ref
                logging.info("delete entry for ipv6dhcpoptiondefinition with array of 8-bit signed integer")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 24 Execution Completed")
                logging.info("============================")






        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

	

