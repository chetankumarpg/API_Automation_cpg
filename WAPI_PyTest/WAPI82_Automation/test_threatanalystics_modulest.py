import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS
class MemberThreatAnalytics(unittest.TestCase):

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
    def test_1_get_threatanalytics_moduleset(self):
        logging.info("Get the member:threat analytics member1")
        threatanalytics_moduleset = ib_NIOS.wapi_request('GET', object_type="threatanalytics:moduleset")
        logging.info(threatanalytics_moduleset)
        res = json.loads(threatanalytics_moduleset)
        print res
        ref1 = res[0]['_ref']
        response1 = ib_NIOS.wapi_request('GET', ref=ref1)
        logging.info(response1)
        res = json.loads(response1)
        print res
        assert res["version"] == "20160627"
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=2)
    def test_2_create_threatanalytics_moduleset(self):
        logging.info("Create the threatanalytics_moduleset  ")
        data = {"enable_auto_download": False,"enable_scheduled_download": False,"module_update_policy": "AUTOMATIC","name": "Infoblox"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="threatanalytics:moduleset",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for threatanalytics:moduleset',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=3)
    def test_3_modify_threatanalytics_moduleset(self):
        logging.info("Modify the threatanalytics_moduleset  ")
        data = {"enable_auto_download": False,"enable_scheduled_download": False,"module_update_policy": "AUTOMATIC","name": "Infoblox"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="threatanalytics:moduleset/YW5hbHl0aWNzLmFuYWx5dGljc19tb2R1bGVfc2V0JDIwMTYwNjI3:20160627",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation update not allowed for threatanalytics:moduleset',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=4)
    def test_4_delete_threatanalytics_moduleset(self):
        logging.info("Deleting the threatanalytics_moduleset")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = "threatanalytics:moduleset/YW5hbHl0aWNzLm1lbWJlcl9hbmFseXRpY3NfcHJvcGVydGllcyQw:infoblox.localdomain")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for threatanalytics:moduleset',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=5)
    def test_5_csvexport_threatanalytics_moduleset(self):
        logging.info("Perform CSV export for threatanalytics_moduleset")
        data = {"_object":"threatanalytics:moduleset"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'threatanalytics:moduleset objects do not support CSV export.',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=6)
    def test_6_globalsearch_threatanalytics_moduleset(self):
        logging.info("Perform Global search for threatanalytics_moduleset")
        threatanalytics_moduleset = ib_NIOS.wapi_request('GET', object_type="search",params="?search_string="+config.grid_fqdn)
        logging.info(threatanalytics_moduleset)
        res = json.loads(threatanalytics_moduleset)
        print res
        ref1 = res[2]['_ref']
        response1 = ib_NIOS.wapi_request('GET', ref=ref1)
        logging.info(response1)
        read  = re.search(r'200',response1)
        for read in  response1:
        	assert True
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=7)
    def test_7_approvable_Non_super_user_threatanalytics_moduleset(self):
        logging.info("Perform Non super user access to threatanalytics_moduleset object")
        threatanalytics_moduleset = ib_NIOS.wapi_request('GET', object_type="threatanalytics:moduleset", user="user", password="infoblox")
        logging.info(threatanalytics_moduleset)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=8)
    def test_8_approvable_Super_user_threatanalytics_moduleset(self):
        logging.info("Perform Super user access to member threat analytics object")
        threatanalytics_moduleset = ib_NIOS.wapi_request('GET', object_type="threatanalytics:moduleset")
        logging.info(threatanalytics_moduleset)
        res = json.loads(threatanalytics_moduleset)
        print res
        ref1 = res[0]['_ref']
        response1 = ib_NIOS.wapi_request('GET', ref=ref1)
        logging.info(response1)
        res = json.loads(response1)
        print res
        assert res["version"] == "20160627"
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=9)
    def test_9_schedule_threatanalytics_moduleset(self):
        logging.info("Perform schedule operation for member threat analytics")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="threatanalytics:moduleset",params="?_schedinfo.scheduled_time=1793807868")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for threatanalytics:moduleset',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=10)
    def test_10_version_with_search1_threatanalytics_moduleset(self):
        logging.info("Search operation for version fields with ~:= modifier")
        response1 = ib_NIOS.wapi_request('GET', object_type="threatanalytics:moduleset", params="?version~=20160627")
        res = json.loads(response1)
        print res
        for i in res:
           logging.info("found")
           assert i["version"] == "20160627"
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")

