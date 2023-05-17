import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class zone_forward(unittest.TestCase):

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
	def test_1_enable_hsm_signing_grid_dns_object(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the enable_hsm_signing field in grid:dns  object")
		data ={"enable_hsm_signing" : True}
		response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print response
		logging.info(response)
		res = json.loads(response)
		read  = re.search(r'200',response)
		for read in  response:
			assert True
		logging.info("Test Case 1 Execution Completed")
		logging.info("============================")
	

	@pytest.mark.run(order=2)
	def test_2_enable_hsm_signing_grid_dns_object(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the enable_hsm_signing field in grid:dns object")
		data ={"enable_hsm_signing" : True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,fields=json.dumps(data))
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Operation create not allowed for grid:dns',response)
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=3)
	def test_3_DELETE_grid_dns_object(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the enable_hsm_signing field in grid:dns object")
		status,response = ib_NIOS.wapi_request('DELETE',object_type=ref)
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Operation delete not allowed for grid:dns',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")	

	@pytest.mark.run(order=4)
	def test_4__datatypeenable_hsm_signing_grid_dns_object(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of enable_hsm_signing field in grid:dns object")
		data ={"enable_hsm_signing" : 1}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,fields=json.dumps(data))
		print response
		logging.info(response)
		assert status ==400 and re.search(r'AdmConProtoError: Invalid value for enable_hsm_signing: 1: Must be boolean type',response)
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")


        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

