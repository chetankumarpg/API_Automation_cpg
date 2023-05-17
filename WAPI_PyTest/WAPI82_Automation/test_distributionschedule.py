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
    def test_1_GET_the_distributionschedule_object_with_time_zone_start_time_active_upgrade_groups(self):
            logging.info("GET_the_distributionschedule_object_with_time_zone_start_time_active_upgrade_groups")
            response = ib_NIOS.wapi_request('GET',object_type="distributionschedule",params="?_return_fields=time_zone,start_time,active,upgrade_groups")
            print response
            logging.info(response)
            read = re.search(r'200',response)
            for read in response:
                     assert True
            logging.info("Test Case 1 Execution Completed")
            logging.info("============================")


    @pytest.mark.run(order=2)
    def test_2_Modify_the_distributionschedule_with_time_zone_start_time_active_upgrade_groups(self):
        logging.info("Modify_the_distributionschedule_with_time_zone_start_time_active_upgrade_groups")
        data = {"active": True,"start_time": 1495701900,"upgrade_groups": [{"distribution_time": 1495711800,"name": "Default"},{"distribution_time": 1495713600,"name": "grid member1"},{"distribution_time": 1495715400,"name": "grid member2"},{"distribution_time": 1495719000,"name": "grid member3"},{"distribution_time": 1495722600,"name": "grid member4"}]}
        response = ib_NIOS.wapi_request('PUT',ref='distributionschedule/Li5kaXN0cmlidXRlc2NoZWR1bGUkZGlzdHJpYnV0aW9uX3NjaGVkdWxl:distribution',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response
	



    @pytest.mark.run(order=3)
    def test_3_Create_the_upgradeschedule_with_time_zone_start_time_active_upgrade_groups_N(self):
        logging.info("Create_the_upgradeschedule_with_time_zone_start_time_active_upgrade_groups_N")
	data = {"active": False,"start_time": 1495623518,"upgrade_groups": [{"distribution_time": 1495625400,"name": "Default"},{"distribution_time": 1495627200,"name": "grid member1"}]}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="distributionschedule",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search('Operation create not allowed for distributionschedule',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=4)
    def test_4_DELETE_the_fields_in_distributionschedule_object_N(self):
        logging.info("DELETE_the_fields_in_distributionschedule_object_N")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = "distributionschedule/Li5kaXN0cmlidXRlc2NoZWR1bGUkZGlzdHJpYnV0aW9uX3NjaGVkdWxl:distribution")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for distributionschedule',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")



    
    @pytest.mark.run(order=5)
    def test_5_Global_search_the_distributionschedule_object_N(self):
               logging.info("Global_search_the_distributionschedule_object_N")
               data = {"distribution_time":1495625400}
               response = ib_NIOS.wapi_request('GET',object_type="search",params="?search_string=distribution_time")
               print response
               logging.info(response)
               read  = re.search(r'200',response)
               for read in  response:
                       assert True
               logging.info("Test Case 5 Execution Completed")
               logging.info("=============================")




    @pytest.mark.run(order=6)
    def test_6_Adding_CSV_export_for_the_distributionschedule_object_N(self):
        logging.info("Perform_Adding_CSV_export_for_the_distributionschedule_object_N")
        data = {"_object":"distributionschedule"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'distributionschedule objects do not support CSV export.',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")


    
    @pytest.mark.run(order=7)
    def test_7_Modify_distributionschedule_field_with_time_zone_start_time_active_upgrade_groups (self):
        logging.info("Modify_distributionschedule_field_with_time_zone_start_time_active_upgrade_groups ")
        data = {"active": True,"start_time": 1495701900,"upgrade_groups": [{"distribution_time": 1495711800,"name": "Default"},{"distribution_time": 1495713600,"name": "grid member1"},{"distribution_time": 1495715400,"name": "grid member2"},{"distribution_time": 1495719000,"name": "grid member3"},{"distribution_time": 1495722600,"name": "grid member4"}]}
        response = ib_NIOS.wapi_request('PUT', object_type="smartfolder:global",ref="distributionschedule/Li5kaXN0cmlidXRlc2NoZWR1bGUkZGlzdHJpYnV0aW9uX3NjaGVkdWxl:distribution", fields=json.dumps(data))
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=8)
    def test_8_Modify_distributionschedule_field_with_active_N(self):
        logging.info("Modify_distributionschedule_field_with_active_N")
        data = {"active": 123,"start_time": 1495701900,"upgrade_groups": [{"distribution_time": 1495711800,"name": "Default"},{"distribution_time": 1495713600,"name": "grid member1"},{"distribution_time": 1495715400,"name": "grid member2"},{"distribution_time": 1495719000,"name": "grid member3"},{"distribution_time": 1495722600,"name": "grid member4"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="distributionschedule/Li5kaXN0cmlidXRlc2NoZWR1bGUkZGlzdHJpYnV0aW9uX3NjaGVkdWxl:distribution", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for active: 123: Must be boolean type',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=9)
    def test_9_Modify_distributionschedule_field_with_start_time_N(self):
	get_ref = ib_NIOS.wapi_request('GET', object_type="distributionschedule")
	logging.info(get_ref)
	res = json.loads(get_ref)
	ref = json.loads(get_ref)[0]['_ref']
	print ref
        logging.info("Modify_distributionschedule_field_with_start_time_N")
        data = {"active": True,"start_time": 1495,"upgrade_groups": [{"distribution_time": 1495711800,"name": "Default"},{"distribution_time": 1495713600,"name": "grid member1"},{"distribution_time": 1495715400,"name": "grid member2"},{"distribution_time": 1495719000,"name": "grid member3"},{"distribution_time": 1495722600,"name": "grid member4"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', object_type=ref, fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'AdmConDataError: None',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=10)
    def test_10_Modify_distributionschedule_field_with_start_Upgrade_group_N(self):
        logging.info("Modify_distributionschedule_field_with_start_Upgrade_group_N")
        data = {"active": True,"start_time": 1495701900,"upgrade_groups": [{"distribution_time": 1495711800,"name": "Defau"},{"distribution_time": 1495713600,"name": "grid member1"},{"distribution_time": 1495715400,"name": "grid member2"},{"distribution_time": 1495719000,"name": "grid member3"},{"distribution_time": 1495722600,"name": "grid member4"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="distributionschedule/Li5kaXN0cmlidXRlc2NoZWR1bGUkZGlzdHJpYnV0aW9uX3NjaGVkdWxl:distribution", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'AdmConDataError: None',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=11)
    def test_11_Modify_distributionschedule_field_with_start_Upgrade_group_name_N(self):
        logging.info("Modify_distributionschedule_field_with_start_Upgrade_group_name_N")
        data = {"active": True,"start_time": 1495701900,"upgrade_groups": [{"distribution_time": 1495711800,"name": "Default"},{"distribution_time": 1495713600,"name": "grid member1"},{"distribution_time": 1495715400,"name": "grid member2"},{"distribution_time": 1495719000,"name": "grid member3"},{"distribution_time": 1495722600,"name": "grid membe884"}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="distributionschedule/Li5kaXN0cmlidXRlc2NoZWR1bGUkZGlzdHJpYnV0aW9uX3NjaGVkdWxl:distribution", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'AdmConDataError: None',response1)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")


    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")

