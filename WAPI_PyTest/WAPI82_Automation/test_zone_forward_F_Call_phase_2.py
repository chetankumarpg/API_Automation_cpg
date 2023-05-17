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
        def test_1_Create_zone_forward(self):
                logging.info("Test Create new zone_forward")
                data ={"fqdn": "test.com","forward_to": [{"address": "10.35.118.15", "name": "test"}]}
                response = ib_NIOS.wapi_request('POST',object_type="zone_forward",fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")



	@pytest.mark.run(order=2)
	def test_2_lock_unlock_zone_FC_zone_forward(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_forward")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the lock_unlock_zone function call in zone_forward object")
		data ={"operation": "LOCK"}
		response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=lock_unlock_zone",fields=json.dumps(data))
		print response
		logging.info(response)
		res = json.loads(response)
		read  = re.search(r'200',response)
		for read in  response:
			assert True
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")

		
		
	@pytest.mark.run(order=3)
	def test_3_lock_unlock_zone_FC_zone_forward(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_forward")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the lock_unlock_zone function call in zone_forward object")
		data ={"operation": "UNLOCK"}
		response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=lock_unlock_zone",fields=json.dumps(data))
		print response
		logging.info(response)
		res = json.loads(response)
		read  = re.search(r'200',response)
		for read in  response:
			assert True
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")
		
		
		
	@pytest.mark.run(order=4)
	def test_4_lock_unlock_zone_FC_zone_forward_datatype(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_forward")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the lock_unlock_zone function call in zone_forward object with the datatype of operation field")
		data ={"operation": True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=lock_unlock_zone",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for operation' ,response)
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")
		


	@pytest.mark.run(order=5)
	def test_5_DELETE_lock_unlock_zone_FC_zone_forward(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_forward")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test DELETE on lock_unlock_zone function call in zone_forward object")
		status,response = ib_NIOS.wapi_request('DELETE',object_type=ref,params="?_function=lock_unlock_zone")
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Function lock_unlock_zone illegal with this method' ,response)
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")


		
	@pytest.mark.run(order=6)
	def test_6_Update_lock_unlock_zone_FC_zone_forward_datatype(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_forward")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test Update lock_unlock_zone function call in zone_forward object with the datatype of operation field")
		data ={"operation": "UNLOCK"}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,params="?_function=lock_unlock_zone",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Function lock_unlock_zone illegal with this method' ,response)
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")
		
        @pytest.mark.run(order=7)
        def test_7_DELETE_zone_forward(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_forward")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Deleting the zone_forward")
                response = ib_NIOS.wapi_request('DELETE', object_type=ref)
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 7 Execution Completed")
                logging.info("=============================")
		



        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

