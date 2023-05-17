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
    def test_1_Add_operation_to_upgradeschedule_object_with_distribution_time_name_upgrade_time(self):
        logging.info("Add_operation_to_upgradeschedule_object_with_distribution_time_name_upgrade_time")
        data = {"distribution_time": 1591056900,"name": "infoblox","upgrade_time": 1591056000}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="upgradeschedule", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Operation create not allowed for upgradeschedule",response1)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")





    @pytest.mark.run(order=2)
    def test_2_Modify_operation_to_upgradeschedule_object(self):
        get_ref = ib_NIOS.wapi_request('GET', object_type="upgradeschedule")
        logging.info(get_ref)
        res = json.loads(get_ref)
        ref = json.loads(get_ref)[0]['_ref'] 
        print ref

        logging.info("Modify_operation_to_upgradeschedule_object")
        data = {"active": True,"start_time": 1495653300,"time_zone": "(UTC + 5:30) Bombay, Calcutta, Madras, New Delhi","upgrade_groups": [{"distribution_time": 1495463400,"name": "Default","time_zone": "(UTC + 5:30) Bombay, Calcutta, Madras, New Delhi","upgrade_time": 1495701000},{"distribution_time": 1495472400,"name": "infoblox","time_zone": "(UTC + 5:30) Bombay, Calcutta, Madras, New Delhi","upgrade_time": 1495713600}]}
        status,response1 = ib_NIOS.wapi_request('PUT',object_type=ref, fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not writable: time_zone",response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")



   
    @pytest.mark.run(order=3)
    def test_3_Modify_the_upgradeschedule_object(self):
        logging.info("Modify_the_upgradeschedule_object")
        data = {"active": True,"start_time": 1495653300,"upgrade_groups": [{"distribution_time": 1495463400,"name": "Default","upgrade_time": 1495701000},{"distribution_time": 1495472400,"name": "infoblox","upgrade_time": 1495713600}]}
        creator = ib_NIOS.wapi_request('PUT', ref = 'upgradeschedule/Li51cGdyYWRlc2NoZWR1bGUkdXBncmFkZV9zY2hlZHVsZQ:upgrade', fields=json.dumps(data))
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=4)
    def test_4_GET_the_upgradeschedule_object_with_active_start_tie_time_zone_upgrade_groups_fileds(self):
        logging.info("GET_the_upgradeschedule_object_with_active_start_tie_time_zone_upgrade_groups_fileds")
        response = ib_NIOS.wapi_request('GET',object_type="upgradeschedule",params="?_return_fields=active")
        print response
        logging.info(response)
        read = re.search(r'200',response)
        for read in response:
                 assert True
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=5)
    def test_5_Modify_operation_to_upgradeschedule_object_distribution_time(self):
        logging.info("Modify_operation_to_upgradeschedule_object_distribution_time")
        data = {"active": True,"start_time": 1495653300,"upgrade_groups": [{"distribution_time": "","name": "Default","upgrade_time": 1495701000},{"distribution_time": 1495472400,"name": "infoblox","upgrade_time": 1495713600}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'upgradeschedule/Li51cGdyYWRlc2NoZWR1bGUkdXBncmFkZV9zY2hlZHVsZQ:upgrade', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Error converting argument distribution_time: Invalid value, must be an integer between 0 and 4294967295",response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=6)
    def test_6_Modify_operation_to_upgradeschedule_object_upgrade_time_N(self):
        logging.info("Modify_operation_to_upgradeschedule_object_upgrade_time_N")
        data = {"active": True,"start_time": 1495653300,"upgrade_groups": [{"distribution_time": 149546,"name": "Default","upgrade_time": ""},{"distribution_time": 1495472400,"name": "infoblox","upgrade_time": 1495713600}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'upgradeschedule/Li51cGdyYWRlc2NoZWR1bGUkdXBncmFkZV9zY2hlZHVsZQ:upgrade', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Error converting argument upgrade_time: Invalid value, must be an integer between 0 and 4294967295",response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=7)
    def test_7_Modify_operation_to_upgradeschedule_object_name(self):
        logging.info("Modify_operation_to_upgradeschedule_object_name")
        data = {"active": True,"start_time": 1495653300,"upgrade_groups": [{"distribution_time": 149546,"name": "Default","upgrade_time": 1495701000},{"distribution_time": 1495472400,"name": 123,"upgrade_time": 1495713600}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'upgradeschedule/Li51cGdyYWRlc2NoZWR1bGUkdXBncmFkZV9zY2hlZHVsZQ:upgrade', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for name: 123: Must be string type",response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=8)
    def test_8_Modify_operation_to_upgradeschedule_object_distribution_time(self):
        logging.info("Modify_operation_to_upgradeschedule_object_distribution_time")
        data = {"active": "","start_time": 1495653300,"upgrade_groups": [{"distribution_time": "","name": "Default","upgrade_time": 1495701000},{"distribution_time": 1495472400,"name": "infoblox","upgrade_time": 1495713600}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'upgradeschedule/Li51cGdyYWRlc2NoZWR1bGUkdXBncmFkZV9zY2hlZHVsZQ:upgrade', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"AdmConProtoError: Invalid value for active:",response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=9)
    def test_9_GET_On_Upgradeschedule(self):
        logging.info("Test GET On upgradeschedule")
        response = ib_NIOS.wapi_request('GET',object_type="upgradeschedule")
        print response
        logging.info(response)
        res = json.loads(response)
        print res
        read  = re.search(r'200',response)
        for read in  response:
        	assert True
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")




    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")


