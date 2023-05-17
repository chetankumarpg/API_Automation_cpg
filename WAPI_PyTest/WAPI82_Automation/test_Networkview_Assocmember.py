import re
import json
import pytest
import unittest
import subprocess
import config
import logging
import ib_utils.ib_NIOS as ib_NIOS

class Networkview_Assocmember(unittest.TestCase):


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
	def test_1_Search_Networkview_Assocmember(self):
		logging.info("test the network associate member struct")
		data = {"name": "default","associated_members": {"member": "local.infoblox.com"}}
		status,response = ib_NIOS.wapi_request('GET',object_type="networkview",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: associated_members',response)
		logging.info("Test Case 1 Execution Completed")
		logging.info("=============================")


	@pytest.mark.run(order=2)
	def test_2_return_fields_Networkview_Assocmember(self):
		logging.info("test the network associate member struct")
		response = ib_NIOS.wapi_request('GET',object_type="networkview",params="?_return_fields=associated_members")
		print response
		logging.info(response)
		res = json.loads(response)
		print res
		for i in res:
			print i
			logging.info("found")
			assert i["associated_members"] == []
		logging.info("Test Case 2 Execution Completed")
		logging.info("=============================")

	@pytest.mark.run(order=3)
	def test_3_POST_Networkview_Assocmember(self):
		logging.info("test the network associate member struct")
		data = {"name": "default","associated_members": {"member": "local.infoblox.com"}}
		status,response = ib_NIOS.wapi_request('POST',object_type="networkview",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert  status == 400 and re.search(r'AdmConProtoError: Field is not writable: associated_members',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("=============================")


        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")



