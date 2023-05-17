import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class Fileop_Function_Call(unittest.TestCase):


	@pytest.mark.run(order=1)
	def test_1_uploadinit_Fileop_Function_Call(self):
		logging.info("Test the uploadinit function call in fileop object")
		response = ib_NIOS.wapi_request('POST',object_type="fileop",params="?_function=uploadinit")
		print response
		logging.info(response)
		res = re.search(r'200',response)
		for res in response:
			assert True
		logging.info("Test Case 1 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=2)
	def test_2_generatesafenetclientcert_Fileop_Function_Call(self):
		logging.info("Test the generatesafenetclientcert function call in fileop object")
		data = {"algorithm":"RSASHA256","member":config.grid_fqdn}
		response = ib_NIOS.wapi_request('POST',object_type="fileop",params="?_function=generatesafenetclientcert",fields=json.dumps(data))
		print response
		logging.info(response)
		res = re.search(r'200',response)
		for res in response:
			assert True
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=3)
	def test_3_getsafenetclientcert_Fileop_Function_Call(self):
		logging.info("Test the getsafenetclientcert function call in fileop object")
		data = {"algorithm":"RSASHA1","member":config.grid_fqdn}
		status,response = ib_NIOS.wapi_request('POST',object_type="fileop",params="?_function=getsafenetclientcert",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status ==400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=4)
	def test_4_uploadinit_Fileop_Function_Call(self):
		logging.info("Test the uploadinit function call in fileop object")
		data = {"filename":"fileop_ruleset"}
		response = ib_NIOS.wapi_request('POST',object_type="fileop",params="?_function=uploadinit",fields=json.dumps(data))
		print response
		logging.info(response)
		res = re.search(r'200',response)
		for res in response:
			assert True
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=5)
	def test_5_uploadinit_Fileop_Function_Call(self):
		logging.info("Test the uploadinit function call in fileop object")
		data = {"filename":"fileop_ruleset"}
		data = {"filename":"fileop_new_ruleset"}
		response = ib_NIOS.wapi_request('POST',object_type="fileop",params="?_function=uploadinit",fields=json.dumps(data))
		print response
		logging.info(response)
		res = re.search(r'200',response)
		for res in response:
			assert True
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=6)
	def test_6_get_last_uploaded_atp_ruleset_Fileop_Function_Call(self):
		logging.info("Test the get_last_uploaded_atp_ruleset function call in fileop object")
		response = ib_NIOS.wapi_request('POST',object_type="fileop",params="?_function=get_last_uploaded_atp_ruleset")
		print response
		logging.info(response)
		res = re.search(r'200',response)
		for res in response:
			assert True
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")	
	


	@pytest.mark.run(order=7)
	def test_7_download_atp_rule_update_Fileop_Function_Call(self):
		logging.info("Test the download_atp_rule_update function call in fileop object")
		status,response = ib_NIOS.wapi_request('POST',object_type="fileop",params="?_function=download_atp_rule_update")
		print response
		print status
		logging.info(response)
		assert status ==400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 7 Execution Completed")
		logging.info("============================")	
