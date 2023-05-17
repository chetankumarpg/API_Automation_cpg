import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import os
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
    def test_1_upload_support_bundle_into_server(self):
        filename="A_dsb.xml"
        data = {"filename":"A_dsb.xml"}
        logging.info("Create the zip file using fileop")
        create_file = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=uploadinit")
        logging.info(create_file)
        res = json.loads(create_file)
        token = json.loads(create_file)['token']
        url = json.loads(create_file)['url']
        print create_file
        print res
        print token
        print url
	os.system('tar -cf A_dsb.tar %s'%(filename))
        os.system('curl -k1 -u admin:infoblox -F file=@%s %s'%(filename,url))
        print filename
        data = {"token": token,"filename":filename}
        create_file1 = ib_NIOS.wapi_request('POST', object_type="discovery",fields=json.dumps(data),params="?_function=import_device_support_bundle")
        logging.info(create_file1)
        print create_file1
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=2)
    def test_2_Delete_device_support_bundle(self):
        logging.info("Delete_device_support_bundle")
        response = ib_NIOS.wapi_request('DELETE', ref = 'discovery:devicesupportbundle/Li5kZXZpY2Vfc3VwcG9ydF9idW5kbGUkQV9kc2I:A_dsb')
        logging.info("============================")
        print response


    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")

