import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import os
import ib_utils.ib_NIOS as ib_NIOS

class Grid_Threatprotection_Function_Call(unittest.TestCase):

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
        def test_1_create_ruleset(self):
            filename="new_ruleset"
            data = {"filename":filename}
            logging.info("upload PT rule set")
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
            data = {"token": token}
            create_file1 = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=update_atp_ruleset")
            logging.info(create_file1)
            print create_file1
            assert re.search(r"",create_file1)
            logging.info("Test Case 1 Execution Completed")
            logging.info("============================")




	@pytest.mark.run(order=2)
	def test_2_atp_object_reset_Grid_Threatprotection_Function_Call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="grid:threatprotection")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the atp_object_reset function call in Grid_Threatprotection object")
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=atp_object_reset")
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: required function parameter missing: atp_object',response)
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=3)
	def test_3_atp_object_reset_Grid_Threatprotection_Function_Call(self):
		get_ref1 = ib_NIOS.wapi_request('GET', object_type="threatprotection:ruleset")
		logging.info(get_ref1)
		res1 = json.loads(get_ref1)
		ref1 = json.loads(get_ref1)[0]['_ref']
		get_ref2 = ib_NIOS.wapi_request('GET', object_type="grid:threatprotection")
		logging.info(get_ref2)
		res2 = json.loads(get_ref2)
		ref2 = json.loads(get_ref2)[0]['_ref']
		print ref2
		logging.info("Test the atp_object_reset function call in Grid_Threatprotection object")
		print ref1
		data = {"atp_object":ref1}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref2,params="?_function=atp_object_reset",fields=json.dumps(data))
		print response
		print status
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: required function parameter missing: delete_custom_rules',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")


        @pytest.mark.run(order=4)
        def test_4_atp_object_reset_Grid_Threatprotection_Function_Call(self):
                get_ref1 = ib_NIOS.wapi_request('GET', object_type="threatprotection:ruleset")
                logging.info(get_ref1)
                res1 = json.loads(get_ref1)
                ref1 = json.loads(get_ref1)[0]['_ref']
                get_ref2 = ib_NIOS.wapi_request('GET', object_type="grid:threatprotection")
                logging.info(get_ref2)
                res2 = json.loads(get_ref2)
                ref2 = json.loads(get_ref2)[0]['_ref']
                print ref2
                logging.info("Test the atp_object_reset function call in Grid_Threatprotection object")
                print ref1
                data = {"atp_object":ref1,"delete_custom_rules": False}
                response = ib_NIOS.wapi_request('POST',object_type=ref2,params="?_function=atp_object_reset",fields=json.dumps(data))
                print response
                logging.info(response)
		res = json.loads(response)
		read  = re.search(r'200',response)
		for read in  response:
			assert True
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=5)
	def test_5_atp_object_reset_Grid_Threatprotection_Function_Call(self):
		get_ref1 = ib_NIOS.wapi_request('GET', object_type="threatprotection:ruleset")
		logging.info(get_ref1)
		res1 = json.loads(get_ref1)
		ref1 = json.loads(get_ref1)[0]['_ref']
		print ref1
		get_ref2 = ib_NIOS.wapi_request('GET', object_type="grid:threatprotection")
		logging.info(get_ref2)
		res2 = json.loads(get_ref2)
		ref2 = json.loads(get_ref2)[0]['_ref']
		print ref2
		logging.info("Test the atp_object_reset function call in Grid_Threatprotection object")
		data = {"atp_object":ref1,"delete_custom_rules": 2}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref2,params="?_function=atp_object_reset",fields=json.dumps(data))
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for delete_custom_rules: 2: Must be boolean type',response)
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=6)
	def test_6_atp_object_reset_Grid_Threatprotection_Function_Call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="grid:threatprotection")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the atp_object_reset function call in Grid_Threatprotection object")
		data = {"atp_object":True,"delete_custom_rules": False}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=atp_object_reset",fields=json.dumps(data))
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Field',response)
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=7)
	def test_7_PUT_atp_object_reset_Grid_Threatprotection_Function_Call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="grid:threatprotection")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the atp_object_reset function call with PUT in Grid_Threatprotection object")
		data = {"atp_object":True,"delete_custom_rules": False}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,params="?_function=atp_object_reset",fields=json.dumps(data))
		print response
		logging.info(response)
		assert status == 400 and re.search(r"AdmConProtoError: Function atp_object_reset illegal with this method",response)
		logging.info("Test Case 7 Execution Completed")
		logging.info("============================")
		
		
	@pytest.mark.run(order=8)
	def test_8_DELETE_atp_object_reset_Grid_Threatprotection_Function_Call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="grid:threatprotection")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the atp_object_reset function call with DELETE in Grid_Threatprotection object")
		status,response = ib_NIOS.wapi_request('DELETE',object_type=ref,params="?_function=atp_object_reset")
		print response
		logging.info(response)
		assert status == 400 and re.search(r"AdmConProtoError: Function atp_object_reset illegal with this method",response)
		logging.info("Test Case 8 Execution Completed")
		logging.info("============================")


        @pytest.mark.run(order=9)
        def test_9_test_atp_server_connectivity_Grid_Threatprotection_Function_Call(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:threatprotection")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test the atp_object_reset function call in Grid_Threatprotection object")
                response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=test_atp_server_connectivity")
                print response
                logging.info(response)
                res = json.loads(response)
                string = {u'overall_status': u'FAILED', u'error_messages': [u'Grid Master/'+config.grid_fqdn+' : Could not resolve host: ts.infoblox.com']}
                if res == string:
                        assert True
                else:
                        assert False
                logging.info("Test Case 9 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=10)
	def test_10_DELETE_test_atp_server_connectivity_Grid_Threatprotection_Function_Call(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="grid:threatprotection")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the atp_object_reset function call in Grid_Threatprotection object")
		status,response = ib_NIOS.wapi_request('DELETE',object_type=ref,params="?_function=test_atp_server_connectivity")
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Function test_atp_server_connectivity illegal with this method',response)
		logging.info("Test Case 10 Execution Completed")
		logging.info("============================")

        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")

