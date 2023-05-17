import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class discoverytask_function_call(unittest.TestCase):

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
		
    def test_create_network_discovery_control(self):
        logging.info("Creating network_discovery_control Test")
        try:
           data = {"name": "domain.com","view": "default"}
           response = ib_NIOS.wapi_request('POST', object_type="record:ds", fields=json.dumps(data))
           print response
          # logging.info(response)
          # logging.info("============================")
        except Exception as e:
                if "Operation create not allowed for record:ds" in e.message:
                        flag=True

                assert flag
	
		
    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")

