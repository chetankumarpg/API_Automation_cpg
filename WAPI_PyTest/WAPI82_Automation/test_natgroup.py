import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class nat_group(unittest.TestCase):

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
        def test_1_create_natgroup(self):
                logging.info("Create natgroup Test")
                data = {"name": "natgroup1","comment":"for the qa testing"}
                response = ib_NIOS.wapi_request('POST', object_type="natgroup", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=2)
        #Test the "creation" of entry in "natgroup" structure
        def test_2_duplicate_natgroup(self):
                logging.info("duplicating natgroup entry Test")
                data = {"name": "natgroup1","comment": "for the qa testing"}
                status,response = ib_NIOS.wapi_request('POST', object_type="natgroup", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConDataError: None',response)
                logging.info("Test Case 2 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=3)
        def test_3_name_natgroup(self):
                logging.info("name in natgroup Test")
                data = {"comment": "for the qa testing"}
                status,response = ib_NIOS.wapi_request('POST', object_type="natgroup", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: field for create missing: name',response)
                logging.info("Test Case 3 Execution Completed")
                logging.info("============================")




        @pytest.mark.run(order=4)
        def test_4_get_natgroup(self):
                logging.info("Get get details using name natgroup")
                data = {"name": "natgroup1"}
                response = ib_NIOS.wapi_request('GET', object_type="natgroup", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 4 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=5)
        def test_5_get_natgroup(self):
                logging.info("Get get details using comment")
                data = {"comment": "for the qa testing"}
                response = ib_NIOS.wapi_request('GET', object_type="natgroup", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 5 Execution Completed")
                logging.info("============================")



	@pytest.mark.run(order=6)

	def test_6_put_natgroup_comment(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="natgroup")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("editing the comment for the natgroup")
                data ={"comment": "for the validation effort"}
                get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                name = ib_NIOS.wapi_request('GET',object_type="natgroup",params="?_return_fields=comment")
                logging.info(name)
                res = json.loads(name)
                print res
                for i in res:
                        print i
                        logging.info("found")
                assert i["comment"] == "for the validation effort"
                logging.info("Test Case 6 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=7)

        def test_7_delete_natgroup_name(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="natgroup")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref

                logging.info("Deleting the natgroup object using comment")
                data ={"comment": "for the validation effort"}
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
                print get_status
                logging.info(get_status)
                logging.info("Test Case 7 Execution Completed")
                logging.info("=============================")

		
	@pytest.mark.run(order=8)
		
        def test_9_post_natgroup_without_name(self):
                logging.info("add natgroup without comment")
                data = {"name": "natgroup2"}
                response = ib_NIOS.wapi_request('POST', object_type="natgroup", fields=json.dumps(data))
                print response
		logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 8 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=9)

        def test_10_put_natgroup_name(self):
                logging.info("edit details using offset using natgroup")
                get_ref = ib_NIOS.wapi_request('GET', object_type="natgroup")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation for name in the natgroup")
                data ={"name": "nat22"}
                get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                name = ib_NIOS.wapi_request('GET',object_type="natgroup",params="?_return_fields=name")
                logging.info(name)
                res = json.loads(name)
                print res
                for i in res:
                        print i
                        logging.info("found")
                assert i["name"] == "nat22"
                logging.info("Test Case 9 Execution Completed")
                logging.info("============================") 
				
				
		
        @pytest.mark.run(order=10)

        def test_10_delete_natgroup_name(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="natgroup")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref

                logging.info("Deleting the natgroup object")
                data ={"name": "nat22"}
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
                print get_status
                logging.info(get_status)
                logging.info("Test Case 8  Execution Completed")
                logging.info("=============================")    


        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")


