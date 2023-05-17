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
    def test_1_Modify_the_discoverytask_object_N(self):
        logging.info("Modify_the_discoverytask_object")
        data = {"tcp_ports":[{"comment": 123,"number": 1024}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for comment: 123: Must be string type',response1)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=2)
    def test_2_Modify_the_discoverytask_object(self):
        logging.info("Modify_the_discoverytask_object")
        data = {"tcp_ports":[{"comment": "kdm","number": 1024}]}
        response = ib_NIOS.wapi_request('PUT',ref='discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=3)
    def test_3_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", params="?tcp_ports=commen")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tcp_ports',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=4)
    def test_4_Modify_the_discoverytask_object_N(self):
        logging.info("Modify_the_discoverytask_object")
        data = {"tcp_ports":{"comment": "kdm","number": 1024}}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'List value expected for field: tcp_ports',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=5)
    def test_5_Modify_the_discoverytask_object_N(self):
        logging.info("Modify_the_discoverytask_object")
        data = {"tcp_ports":[{"comment": "kdm","number": 10123646444}]}
        status,response = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response
        logging.info(response)
        assert  status == 400 and re.search(r'Invalid value for number: 10123646444: Invalid value, must be between 0 and 4294967295',response)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=6)
    def test_6_Modify_the_discoverytask_object_N(self):
        logging.info("Modify_the_discoverytask_object")
        data = {"tcp_ports":[{"comment": "kdm","number": "123"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for number.*.* Must be integer type',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")




    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")
