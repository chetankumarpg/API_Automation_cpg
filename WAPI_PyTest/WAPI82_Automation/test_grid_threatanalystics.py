import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS
class MemberFileDistribution(unittest.TestCase):

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
    def test_1_get_grid_threatanalytics(self):
        logging.info("Get operation for grid:threatanalytics object")
        response = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics")
        logging.info(response)
        print response
        read  = re.search(r'200',response)
        for read in  response:
        	assert True
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=2)
    def test_2_create_threat_analytics(self):
        logging.info("Create the grid threat analytics  ")
        data = {"enable_auto_download": False,"enable_scheduled_download": False,"module_update_policy": "AUTOMATIC","name": "Infoblox"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="grid:threatanalytics",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for grid:threatanalytics',response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=3)
    def test_3_delete_threat_analytics(self):
        logging.info("Deleting the grid threat analytics")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = "grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for grid:threatanalytics',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=4)
    def test_4_csvexport_threat_analytics(self):
        logging.info("Perform CSV export for grid threat analytics")
        data = {"_object":"grid:threatanalytics"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'grid:threatanalytics objects do not support CSV export.',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=5)
    def test_5_approvable_Non_super_user_threat_analytics(self):
        logging.info("Perform Non super user access to grid File distribution object")
        threat_analytics = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", user="user", password="infoblox")
        logging.info(threat_analytics)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=6)
    def test_6_approvable_Super_user_threat_analytics(self):
        logging.info("Perform Super user access to grid File distribution object")
        threat_analytics = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics",user="user1", password="infoblox")
        logging.info(threat_analytics)
        res = json.loads(threat_analytics)
        print res
        for i in res:
            logging.info("found")
            assert i["enable_auto_download"] == False and i["enable_scheduled_download"] == False and i["module_update_policy"] == "MANUAL" and  i["name"] == "Infoblox"
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=7)
    def test_7_globalsearch_threat_analytics(self):
        logging.info("Perform Global search for grid File distribution")
        search_threat_analytics = ib_NIOS.wapi_request('GET', object_type="search",params="?search_string=MANUAL")
        logging.info(search_threat_analytics)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=8)
    def test_8_schedule_threat_analytics(self):
        logging.info("Perform schedule operation for grid threat analytics")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="grid:threatanalytics",params="?_schedinfo.scheduled_time=1793807868")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for grid:threatanalytics',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=9)
    def test_9_get_all_fields_member_FD(self):
        logging.info("Update operation for allow_uploads fields")
        member_FD = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?_return_fields=name")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "Infoblox"
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=10)
    def test_10_current_moduleset_with_value_for_ref_threat_analytics(self):
        logging.info("Update operation for current_moduleset fields with value for threat analytics ")
        data = {"current_moduleset":"true"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=current_moduleset", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: current_moduleset',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=11)
    def test_11_current_moduleset_with_search1_threat_analytics(self):
        logging.info("Search operation for current_moduleset fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?current_moduleset~:=20160627")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: current_moduleset',response1)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=12)
    def test_12_current_moduleset_with_value_for_ref_threat_analytics(self):
        logging.info("Update operation for dns_tunnel_black_list_rpz_zone fields with value for threat analytics ")
        data = {"dns_tunnel_black_list_rpz_zones":"abc.com"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=dns_tunnel_black_list_rpz_zones", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'List value expected for field: dns_tunnel_black_list_rpz_zones',response1)
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=13)
    def test_13_dns_tunnel_black_list_rpz_zone_with_search_threat_analytics(self):
        logging.info("Search operation for dns_tunnel_black_list_rpz_zone fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?dns_tunnel_black_list_rpz_zones~:=com")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: dns_tunnel_black_list_rpz_zones',response1)
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")
		
		

    @pytest.mark.run(order=14)
    def test_14_enable_auto_download_filelist_with_true_threat_analytics(self):
        logging.info("Update operation for enable_auto_download fields with true")
        data = {"enable_auto_download": False}
        threat_analytics = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=enable_auto_download", fields=json.dumps(data))
        logging.info(threat_analytics)
        res = json.loads(threat_analytics)
        print res
        assert res["enable_auto_download"] == False
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")
		


    @pytest.mark.run(order=15)
    def test_15_enable_auto_download_with_search_threat_analytics(self):
        logging.info("Search operation for enable_auto_download fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?enable_auto_download~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_auto_download',response1)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=16)
    def test_16_enable_scheduled_download_with_value_for_ref_threat_analytics(self):
        logging.info("Update operation for enable_scheduled_download fields with value for threat analytics ")
        data = {"enable_scheduled_download": True}
        threat_analytics = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=enable_scheduled_download", fields=json.dumps(data))
        print threat_analytics
        logging.info(threat_analytics)
        res = json.loads(threat_analytics)
        print res
        assert res["enable_scheduled_download"] == False
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=17)
    def test_17_enable_scheduled_download_with_search_threat_analytics(self):
        logging.info("Search operation for enable_scheduled_download fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?enable_scheduled_download~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_scheduled_download',response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")
		
		
		
    @pytest.mark.run(order=18)
    def test_18_last_checked_for_update_with_value_for_ref_threat_analytics(self):
        logging.info("Update operation for last_checked_for_update fields with value for threat analytics ")
        data = {"last_checked_for_update":"1490616015"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=last_checked_for_update", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: last_checked_for_update',response1)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=19)
    def test_19_last_checked_for_update_with_search1_threat_analytics(self):
        logging.info("Search operation for last_checked_for_update fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?last_checked_for_update~:=1490616015")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: last_checked_for_update',response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")
		

    @pytest.mark.run(order=20)
    def test_20_last_module_update_time_with_value_for_ref_threat_analytics(self):
        logging.info("Update operation for last_module_update_time fields with value for threat analytics ")
        data = {"last_module_update_time":"true"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=last_module_update_time", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: last_module_update_time',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=21)
    def test_21_last_module_update_time_with_search1_threat_analytics(self):
        logging.info("Search operation for last_module_update_time fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?last_module_update_time~:=20160627")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: last_module_update_time',response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")
		

    @pytest.mark.run(order=22)
    def test_22_last_module_update_version_with_value_for_ref_threat_analytics(self):
        logging.info("Update operation for last_module_update_version fields with value for threat analytics ")
        data = {"last_module_update_version":1490616015}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=last_module_update_version", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: last_module_update_version',response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=23)
    def test_23_last_module_update_version_with_search1_threat_analytics(self):
        logging.info("Search operation for last_module_update_version fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?last_module_update_version~:=20160627")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: last_module_update_version',response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")
		


    @pytest.mark.run(order=24)
    def test_24_last_whitelist_update_time_with_value_for_ref_threat_analytics(self):
        logging.info("Update operation for last_whitelist_update_time fields with value for threat analytics ")
        data = {"last_whitelist_update_time":1490616015}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=last_whitelist_update_time", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: last_whitelist_update_time',response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=25)
    def test_25_last_whitelist_update_time_with_search1_threat_analytics(self):
        logging.info("Search operation for last_whitelist_update_time fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?last_whitelist_update_time~:=20160627")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: last_whitelist_update_time',response1)
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=26)
    def test_26_last_whitelist_update_version_with_value_for_ref_threat_analytics(self):
        logging.info("Update operation for last_whitelist_update_version fields with value for threat analytics ")
        data = {"last_whitelist_update_version":1490616015}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=last_whitelist_update_version", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: last_whitelist_update_version',response1)
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=27)
    def test_27_last_whitelist_update_version_with_search1_threat_analytics(self):
        logging.info("Search operation for last_whitelist_update_version fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?last_whitelist_update_version~:=20160627")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: last_whitelist_update_version',response1)
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")
		
		
    @pytest.mark.run(order=28)
    def test_28_module_update_policy_with_value_for_ref_threat_analytics(self):
        logging.info("Update operation for module_update_policy fields with value for threat analytics ")
        data = {"module_update_policy": "MANUAL"}
        threat_analytics = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=module_update_policy", fields=json.dumps(data))
        logging.info(threat_analytics)
        res = json.loads(threat_analytics)
        print res
        assert res["module_update_policy"] == "MANUAL"
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=29)
    def test_29_module_update_policy_with_search1_threat_analytics(self):
        logging.info("Search operation for module_update_policy fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?module_update_policy~:=20160627")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: module_update_policy',response1)
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")
		

    @pytest.mark.run(order=30)
    def test_30_name_with_value_for_ref_threat_analytics(self):
        logging.info("Update operation for name fields with value for threat analytics ")
        data = {"name":"Infoblox"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=name", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: name',response1)
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")
		
		
    @pytest.mark.run(order=31)
    def test_31_name_with_search1_threat_analytics(self):
        logging.info("Search operation for name fields with = modifier")
        threat_analytics = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?name=Infoblox")
        logging.info(threat_analytics)
        res = json.loads(threat_analytics)
        print res
        for i in res:
            logging.info("found")
            assert i["enable_auto_download"] == False and i["enable_scheduled_download"] == False and i["module_update_policy"] == "MANUAL" and  i["name"] == "Infoblox"
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")
		


    @pytest.mark.run(order=32)
    def test_32_scheduled_download_with_value_for_ref_threat_analytics(self):
        logging.info("Update operation for scheduled_download fields with value for threat analytics ")
        data = {"scheduled_download":"infoblox"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:threatanalytics/YW5hbHl0aWNzLmNsdXN0ZXJfYW5hbHl0aWNzX3Byb3BlcnRpZXMkMA:Infoblox", params="?_return_fields=scheduled_download", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=33)
    def test_33_scheduled_download_with_search1_threat_analytics(self):
        logging.info("Search operation for scheduled_download fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:threatanalytics", params="?scheduled_download~:=20160627")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: scheduled_download',response1)
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")
