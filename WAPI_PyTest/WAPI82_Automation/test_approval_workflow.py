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
    def test_1_create_admin_group(self):
        logging.info("Create admin group with required fields")
        data = {"name":"app_wf"}
        response = ib_NIOS.wapi_request('POST', object_type="admingroup",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=2)
    def test_2_create_admin_group(self):
        logging.info("Create admin group with required fields")
        data = {"name":"app_wf1"}
        response = ib_NIOS.wapi_request('POST', object_type="admingroup",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=3)
    def test_3_create_approval_workflow_with_all_fields(self):
        logging.info("create_approval_workflow_with_all_fields")
        data = {"approval_group":"app_wf","submitter_group":"app_wf1","approver_comment":"REQUIRED","submitter_comment":"REQUIRED","ticket_number":"REQUIRED","enable_approval_notify":False,"approval_notify_to":"SUBMITTER","enable_approved_notify":False,"approved_notify_to":"APPROVER","enable_failed_notify":False,"failed_notify_to":"SUBMITTER","enable_notify_group":True,"enable_notify_user":True,"enable_rejected_notify":False,"rejected_notify_to":"APPROVER","enable_rescheduled_notify":False,"rescheduled_notify_to":"SUBMITTER","enable_succeeded_notify":False,"succeeded_notify_to":"SUBMITTER"}
        response = ib_NIOS.wapi_request('POST', object_type="approvalworkflow",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=4)
    def test_4_delete_approval_workflow(self):
        logging.info("delete_approval_workflow")
        response = ib_NIOS.wapi_request('DELETE', ref = 'approvalworkflow/b25lLndvcmtmbG93X2FwcHJvdmFsJC5hcHBfd2Yx:app_wf1')
        logging.info("============================")
        print response

    @pytest.mark.run(order=5)
    def test_5_create_approval_workflow_with_all_fields(self):
        logging.info("create_approval_workflow_with_all_fields")
        data = {"approval_group":"app_wf","submitter_group":"app_wf1"}
        response = ib_NIOS.wapi_request('POST', object_type="approvalworkflow",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=6)
    def test_6_Modify_the_approval_workflow(self):
        logging.info("Modify_the_approval_workflow")
        data = {"approver_comment":"REQUIRED","submitter_comment":"REQUIRED","ticket_number":"REQUIRED","enable_approval_notify":False,"approval_notify_to":"SUBMITTER","enable_approved_notify":True,"approved_notify_to":"APPROVER","enable_failed_notify":False,"failed_notify_to":"SUBMITTER","enable_notify_group":True,"enable_notify_user":True,"enable_rejected_notify":False,"rejected_notify_to":"APPROVER","enable_rescheduled_notify":False,"rescheduled_notify_to":"SUBMITTER","enable_succeeded_notify":False,"succeeded_notify_to":"SUBMITTER"}
        response = ib_NIOS.wapi_request('PUT', ref = "approvalworkflow/b25lLndvcmtmbG93X2FwcHJvdmFsJC5hcHBfd2Yx",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=7)
    def test_7_Get_operation_to_read_approval_workflow_object(self):
        logging.info("Get_operation_to_read_approval_workflow_object")
        search_record_dname = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?approval_group=app_wf" )
        response = json.loads(search_record_dname)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["approval_group"] in ["app_wf"] and i["submitter_group"] in ["app_wf1"]:
                                   var=True

        assert var
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=8)
    def test_8_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?submitter_group:=app_wf1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: submitter_group",response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=9)
    def test_9_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?approver_comment=REQUIRED")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: approver_comment",response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=10)
    def test_10_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?submitter_comment=REQUIRED")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: submitter_comment",response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=11)
    def test_11_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?ticket_number=REQUIRED")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: ticket_number",response1)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=12)
    def test_12_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?enable_approval_notify=False")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: enable_approval_notify",response1)
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=13)
    def test_13_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?approval_notify_to=SUBMITTER")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: approval_notify_to",response1)
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=14)
    def test_14_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?enable_approved_notify=False")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: enable_approved_notify",response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=15)
    def test_15_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?approved_notify_to=SUBMITTER")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: approved_notify_to",response1)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=16)
    def test_16_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?enable_failed_notify=False")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: enable_failed_notify",response1)
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=17)
    def test_17_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?failed_notify_to=SUBMITTER")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: enable_failed_notify",response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=17)
    def test_17_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?enable_notify_group=False")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: enable_notify_group",response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=18)
    def test_18_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?enable_notify_user=False")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: enable_notify_user",response1)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=19)
    def test_19_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?enable_rejected_notify=False")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: enable_rejected_notify",response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=20)
    def test_20_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?rejected_notify_to=SUBMITTER")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: rejected_notify_to",response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=21)
    def test_21_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?enable_rescheduled_notify=False")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: enable_rescheduled_notify",response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=22)
    def test_22_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?rescheduled_notify_to=SUBMITTER")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: rescheduled_notify_to",response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=23)
    def test_23_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?enable_succeeded_notify=SUBMITTER")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: enable_succeeded_notify",response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=24)
    def test_24_Search_operation_to_read_approval_workflow_object(self):
        logging.info("Search_operation_to_read_approval_workflow_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="approvalworkflow", params="?succeeded_notify_to=SUBMITTER")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not searchable: succeeded_notify_to",response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")

