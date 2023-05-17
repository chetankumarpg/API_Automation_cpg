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
    def test_1_create_namedacl(self):
        logging.info("create_namedacl")
        data = {"access_list": [{"_struct": "addressac","address": "2.2.2.2","permission": "ALLOW"}],"name": "nac1"}
        response = ib_NIOS.wapi_request('POST', object_type="namedacl",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=2)
    def test_2_create_namedacl(self):
        logging.info("create_namedacl")
        data = {"access_list": [{"_struct": "addressac","address": "2.2.2.2","permission": "ALLOW"}],"name": "nac2"}
        response = ib_NIOS.wapi_request('POST', object_type="namedacl",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=3)
    def test_3_create_namedacl(self):
        logging.info("create_namedacl")
        data = {"access_list": [{"_ref": "namedacl/b25lLmRlZmluZWRfYWNsJDAubmFjMQ:nac1"},{"_ref": "namedacl/b25lLmRlZmluZWRfYWNsJDAubmFjMg:nac2"}],"name": "nac3"}
        response = ib_NIOS.wapi_request('POST', object_type="namedacl",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=4)
    def test_4_Get_namedacl_object(self):
        get_ref = ib_NIOS.wapi_request('GET', object_type="namedacl")
        logging.info(get_ref)
        res = json.loads(get_ref)
        ref = json.loads(get_ref)[0]['_ref']
        print ref
        logging.info("Test action field validate_acl_items in  function call of namedacl object")
        data ={}
        response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=validate_acl_items",fields=json.dumps(data))
        print response
        logging.info(response)
        read = re.search(r'200',response)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")







    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")

