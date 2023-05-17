import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class Safenet_Setup(unittest.TestCase):

        @pytest.mark.run(order=1)
        def test_1_generatesafenetclientcert_Fileop_Function_Call(self):
                logging.info("Test the generatesafenetclientcert function call in fileop object")
                data = {"algorithm":"RSASHA256","member":config.grid_fqdn}
                response = ib_NIOS.wapi_request('POST',object_type="fileop",params="?_function=generatesafenetclientcert",fields=json.dumps(data))
                print response
                logging.info(response)
                res = re.search(r'200',response)
                for res in response:
                        assert True
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=2)
        def test_2_Uploading_Cert(self):
                logging.info("Test Uploading the Cert with fileop")
                data = {"filename":"10.39.10.12.pem"}
                response = ib_NIOS.wapi_request('POST',object_type="fileop",params="?_function=uploadinit",fields=json.dumps(data))
                print response
                logging.info(response)
		
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")
