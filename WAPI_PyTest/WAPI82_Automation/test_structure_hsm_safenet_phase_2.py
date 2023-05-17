import re
import config
import pytest
import unittest
import logging
import subprocess
import json
from time import sleep
import ib_utils.ib_NIOS as ib_NIOS
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
    def test_1_Adding_the_hsm_safenetgroup_object_to_partition_serial_number_field_N(self):
        logging.info("Adding_the_hsm_safenetgroup_object_to_partition_serial_number_field_N")
        data = {"comment":"testing","hsm_safenet":[{"disable": False,"name":"10.39.10.12","partition_serial_number":154441010,"server_cert": "eJydUMFOwzAMvedHxmVp061ry21oTEJCA21wttokHZbaxKQp2v4eZ0hcuHGIZfs9P+dZa09XCPYs\nOGjvphhmHX0QpMSdRtf7bvAX6Z1NL17JTmLXxhaOthdUCA3QzThEdADCoI6CVuLO0FqcFvZCGK4Q\ncbQLQaXYq3VTVnnVFLWsq7xWSkynxRwGRjfM/4iRpvssU7lclVKpWpZZ6oFB/luEHgcL6LNgPwHN\n8v31+WW7W6o8V7eRRnJUhSQ7smCVtNFwVrP03xEGmkQxbIZzlTMrm9h5e7ZZHOn/m39sJV2wTnuD\n7py6BS94eDqkdPVLGL1Jt1HpXLvt2xaOj/tUl2KKR1KbdEpVMdijHcwE0YP2I7XhNlWLQzLZtQTo\naI7wZcOE3iWsYayT3w3jksg=\n"}],"hsm_version":"LunaSA_5","name": "HSM_group","pass_phrase":123}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for pass_phrase: 123: Must be string type',response1)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=2)
    def test_2_Adding_the_hsm_safenetgroup_object_to_name_field_N(self):
        logging.info("Adding_the_hsm_safenetgroup_object_to_name_field_N")
        data = {"comment":"testing","hsm_safenet":[{"disable": False,"name":"10.39.10.12","partition_serial_number":154441010,"server_cert":"eJydUMFOwzAMvedHxmVp061ry21oTEJCA21wttokHZbaxKQp2v4eZ0hcuHGIZfs9P+dZa09XCPYs\nOGjvphhmHX0QpMSdRtf7bvAX6Z1NL17JTmLXxhaOthdUCA3QzThEdADCoI6CVuLO0FqcFvZCGK4Q\ncbQLQaXYq3VTVnnVFLWsq7xWSkynxRwGRjfM/4iRpvssU7lclVKpWpZZ6oFB/luEHgcL6LNgPwHN\n8v31+WW7W6o8V7eRRnJUhSQ7smCVtNFwVrP03xEGmkQxbIZzlTMrm9h5e7ZZHOn/m39sJV2wTnuD\n7py6BS94eDqkdPVLGL1Jt1HpXLvt2xaOj/tUl2KKR1KbdEpVMdijHcwE0YP2I7XhNlWLQzLZtQTo\naI7wZcOE3iWsYayT3w3jksg=\n"}],"hsm_version":"LunaSA_5","name": 234,"pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for name: 234: Must be string type',response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=3)
    def test_3_Adding_the_hsm_safenetgroup_object_to_partition_serial_number_field_N(self):
        logging.info("Adding_the_hsm_safenetgroup_object_to_partition_serial_number_field_N")
        data = {"comment":"testing","hsm_safenet":[{"disable": False,"name":"10.39.10.12","partition_serial_number":154441010,"server_cert":"eJydUMFOwzAMvedHxmVp061ry21oTEJCA21wttokHZbaxKQp2v4eZ0hcuHGIZfs9P+dZa09XCPYs\nOGjvphhmHX0QpMSdRtf7bvAX6Z1NL17JTmLXxhaOthdUCA3QzThEdADCoI6CVuLO0FqcFvZCGK4Q\ncbQLQaXYq3VTVnnVFLWsq7xWSkynxRwGRjfM/4iRpvssU7lclVKpWpZZ6oFB/luEHgcL6LNgPwHN\n8v31+WW7W6o8V7eRRnJUhSQ7smCVtNFwVrP03xEGmkQxbIZzlTMrm9h5e7ZZHOn/m39sJV2wTnuD\n7py6BS94eDqkdPVLGL1Jt1HpXLvt2xaOj/tUl2KKR1KbdEpVMdijHcwE0YP2I7XhNlWLQzLZtQTo\naI7wZcOE3iWsYayT3w3jksg=\n"}],"hsm_version":"LunaSA_5","name":"HSM_group","pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for name: 234: Must be string type',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=4)
    def test_4_Adding_the_hsm_safenetgroup_object_to_name_field_N(self):
        logging.info("Adding_the_hsm_safenetgroup_object_to_name_field_N")
        data = {"comment":"testing","hsm_safenet":[{"disable": False,"name":10,"partition_serial_number":154441010,"server_cert": "eJydUMFOwzAMvedHxmVp061ry21oTEJCA21wttokHZbaxKQp2v4eZ0hcuHGIZfs9P+dZa09XCPYs\nOGjvphhmHX0QpMSdRtf7bvAX6Z1NL17JTmLXxhaOthdUCA3QzThEdADCoI6CVuLO0FqcFvZCGK4Q\ncbQLQaXYq3VTVnnVFLWsq7xWSkynxRwGRjfM/4iRpvssU7lclVKpWpZZ6oFB/luEHgcL6LNgPwHN\n8v31+WW7W6o8V7eRRnJUhSQ7smCVtNFwVrP03xEGmkQxbIZzlTMrm9h5e7ZZHOn/m39sJV2wTnuD\n7py6BS94eDqkdPVLGL1Jt1HpXLvt2xaOj/tUl2KKR1KbdEpVMdijHcwE0YP2I7XhNlWLQzLZtQTo\naI7wZcOE3iWsYayT3w3jksg=\n"}],"hsm_version":"LunaSA_5","name": "HSM_group","pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for name: 10: Must be string type',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")
		


    @pytest.mark.run(order=5)
    def test_5_Adding_the_hsm_safenetgroup_object_to_disable_field_N(self):
        logging.info("Adding_the_hsm_safenetgroup_object_to_disable_field_N")
        data = {"comment":"testing","hsm_safenet":[{"disable": "false","name":"10.39.10.12","partition_serial_number":154441010,"server_cert":"eJydUMFOwzAMvedHxmVp061ry21oTEJCA21wttokHZbaxKQp2v4eZ0hcuHGIZfs9P+dZa09XCPYs\nOGjvphhmHX0QpMSdRtf7bvAX6Z1NL17JTmLXxhaOthdUCA3QzThEdADCoI6CVuLO0FqcFvZCGK4Q\ncbQLQaXYq3VTVnnVFLWsq7xWSkynxRwGRjfM/4iRpvssU7lclVKpWpZZ6oFB/luEHgcL6LNgPwHN\n8v31+WW7W6o8V7eRRnJUhSQ7smCVtNFwVrP03xEGmkQxbIZzlTMrm9h5e7ZZHOn/m39sJV2wTnuD\n7py6BS94eDqkdPVLGL1Jt1HpXLvt2xaOj/tUl2KKR1KbdEpVMdijHcwE0YP2I7XhNlWLQzLZtQTo\naI7wZcOE3iWsYayT3w3jksg=\n"}],"hsm_version":"LunaSA_5","name":"HSM_group","pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for disable: .*false.*: Must be boolean type',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=6)
    def test_6_Adding_the_hsm_safenetgroup_object_to_Comment_field_N(self):
        logging.info("Adding_the_hsm_safenetgroup_object_to_Comment_field_N")
        data = {"comment":123,"hsm_safenet":[{"disable": False,"name":"10.39.10.12","partition_serial_number":154441010,"server_cert": "eJydUMFOwzAMvedHxmVp061ry21oTEJCA21wttokHZbaxKQp2v4eZ0hcuHGIZfs9P+dZa09XCPYs\nOGjvphhmHX0QpMSdRtf7bvAX6Z1NL17JTmLXxhaOthdUCA3QzThEdADCoI6CVuLO0FqcFvZCGK4Q\ncbQLQaXYq3VTVnnVFLWsq7xWSkynxRwGRjfM/4iRpvssU7lclVKpWpZZ6oFB/luEHgcL6LNgPwHN\n8v31+WW7W6o8V7eRRnJUhSQ7smCVtNFwVrP03xEGmkQxbIZzlTMrm9h5e7ZZHOn/m39sJV2wTnuD\n7py6BS94eDqkdPVLGL1Jt1HpXLvt2xaOj/tUl2KKR1KbdEpVMdijHcwE0YP2I7XhNlWLQzLZtQTo\naI7wZcOE3iWsYayT3w3jksg=\n"}],"hsm_version":"LunaSA_5","name": "HSM_group","pass_phrase":"Infoblox.123"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for comment: 123: Must be string type',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=7)
    def test_7_DELETE_the_hsm_safenetgroup(self):
	get_ref = ib_NIOS.wapi_request('GET', object_type="hsm:safenetgroup")
	logging.info(get_ref)
	res = json.loads(get_ref)
	ref = json.loads(get_ref)[0]['_ref']
        logging.info("DELETE_the_hsm_safenetgroup")
        response = ib_NIOS.wapi_request('DELETE', object_type=ref)
	logging.info(response)
	res=re.search(r'200',response)
	for res in response:
		assert True
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")



    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")
                                                       
