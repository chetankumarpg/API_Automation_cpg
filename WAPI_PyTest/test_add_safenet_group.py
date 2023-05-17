import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import os
import ib_utils.ib_NIOS as ib_NIOS

class CreateHsmSafenet(unittest.TestCase):

        @pytest.mark.run(order=1)
        def test_1_Adding_Safenet_Group(self):
            filename="server.pem"
            data = {"filename":filename}
            logging.info("uploading Clint Certificste")
            create_file = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=uploadinit")
            logging.info(create_file)
            res = json.loads(create_file)
            token = json.loads(create_file)['token']
            url = json.loads(create_file)['url']
            print create_file
            print res
            print token
            print url
            os.system('curl -k1 -u admin:infoblox -F name=%s -F filedata=@%s %s'%(filename,filename,url))
            filename="/"+filename
            print filename
            data = {"comment": "testing","hsm_safenet":[{"disable": False,"name": "10.39.10.12","partition_serial_number":"154441011","server_cert": token}],"hsm_version":"LunaSA_5","name": "HSM_group","pass_phrase":"Infoblox.123"}
            create_file1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
            logging.info(create_file1)
            print create_file1
            assert re.search(r"",create_file1)
            logging.info("Test Case 1 Execution Completed")
            logging.info("============================")

