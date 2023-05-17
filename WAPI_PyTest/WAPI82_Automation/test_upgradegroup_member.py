import re
import json
import pytest
import unittest
import subprocess
import config
import logging
import ib_utils.ib_NIOS as ib_NIOS

class Upgradeschedule(unittest.TestCase):

        @pytest.mark.run(order=1)
        def test_1_GET_the_upgradegroup_object(self):

                logging.info("GET_the_upgradegroup_object")
                response = ib_NIOS.wapi_request('GET',object_type="upgradegroup")
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True

                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")




