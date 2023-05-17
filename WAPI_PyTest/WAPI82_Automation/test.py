import re
import os
import json
import pytest
import unittest
import subprocess
import config
import logging
import ib_utils.ib_NIOS as ib_NIOS

class Microsoft_Superscope(unittest.TestCase):


    @pytest.mark.run(order=1)
    def test_1_Add_operation_to_upgradeschedule_object_with_distribution_time_name_upgrade_time(self):
        logging.info("Add_operation_to_upgradeschedule_object_with_distribution_time_name_upgrade_time")
        data = {"distribution_time": 1591056900,"name": "infoblox","upgrade_time": 1591056000}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="upgradeschedule", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Operation create not allowed for upgradeschedule",response1)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")

