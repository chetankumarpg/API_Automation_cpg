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
    def test_1_get_member_FD(self):
        logging.info("Get the member File distribution defaults fields ")
        get_member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution")
        logging.info(get_member_FD)
        res = json.loads(get_member_FD)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["host_name"] == config.grid_fqdn and i["ipv4_address"] == config.grid_vip and  i["status"] == "INACTIVE"
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")


    



    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")

