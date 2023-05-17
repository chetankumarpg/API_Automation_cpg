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
    def test_1_get_member_threatanalytics1(self):
        logging.info("Get the member:threat analytics member1")
        threat_analytics = ib_NIOS.wapi_request('GET', object_type="member:threatanalytics")
        logging.info(threat_analytics)
        res = json.loads(threat_analytics)
        print res
        ref1 = res[0]['_ref']
        response1 = ib_NIOS.wapi_request('GET', ref=ref1)
        logging.info(response1)
        res = json.loads(response1)
        print res
        assert res["host_name"] == "infoblox.localdomain" and res["ipv4_address"] == "10.35.134.2" and res["status"] == "INACTIVE"
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=2)
    def test_2_get_member_threatanalytics2(self):
        logging.info("Get the member:threat analytics member1")
        threat_analytics = ib_NIOS.wapi_request('GET', object_type="member:threatanalytics")
        logging.info(threat_analytics)
        res = json.loads(threat_analytics)
        print res
        ref1 = res[1]['_ref']
        response1 = ib_NIOS.wapi_request('GET', ref=ref1)
        logging.info(response1)
        res = json.loads(response1)
        print res
        assert res["host_name"] == "member.com" and res["ipv4_address"] == "10.35.118.4" and res["status"] == "INACTIVE"
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=3)
    def test_3_create_member_threat_analytics(self):
        logging.info("Create the member threat analytics  ")
        data = {"enable_auto_download": False,"enable_scheduled_download": False,"module_update_policy": "AUTOMATIC","name": "Infoblox"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="member:threatanalytics",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for member:threatanalytics',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=4)
    def test_4_delete_member_threat_analytics(self):
        logging.info("Deleting the member threat analytics")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = "member:threatanalytics/YW5hbHl0aWNzLm1lbWJlcl9hbmFseXRpY3NfcHJvcGVydGllcyQw:infoblox.localdomain")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for member:threatanalytics',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")
		
		
    @pytest.mark.run(order=5)
    def test_5_csvexport_member_threat_analytics(self):
        logging.info("Perform CSV export for grid threat analytics")
        data = {"_object":"member:threatanalytics"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'member:threatanalytics objects do not support CSV export.',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=6)
    def test_6_globalsearch_member_threat_analytics(self):
        logging.info("Perform Global search for member threat analytics")
        search_threat_analytics = ib_NIOS.wapi_request('GET', object_type="search",params="?search_string=infoblox.localdomain")
        logging.info(search_threat_analytics)
        res = json.loads(search_threat_analytics)
        print res
        ref1 = res[2]['_ref']
        response1 = ib_NIOS.wapi_request('GET', ref=ref1)
        logging.info(response1)
        res = json.loads(response1)
        print res
        assert res["host_name"] == "infoblox.localdomain" and res["ipv4_address"] == "10.35.134.2" and res["status"] == "INACTIVE"
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")
		
		
    @pytest.mark.run(order=7)
    def test_7_approvable_Non_super_user_member_threat_analytics(self):
        logging.info("Perform Non super user access to member threat analytics object")
        threat_analytics = ib_NIOS.wapi_request('GET', object_type="member:threatanalytics", user="user", password="infoblox")
        logging.info(threat_analytics)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=8)
    def test_8_approvable_Super_user_threat_analytics(self):
        logging.info("Perform Super user access to member threat analytics object")
        threat_analytics = ib_NIOS.wapi_request('GET', object_type="member:threatanalytics",user="user1", password="infoblox")
        logging.info(threat_analytics)
        res = json.loads(threat_analytics)
        print res
        ref1 = res[0]['_ref']
        response1 = ib_NIOS.wapi_request('GET', ref=ref1)
        logging.info(response1)
        res = json.loads(response1)
        print res
        assert res["host_name"] == "infoblox.localdomain" and res["ipv4_address"] == "10.35.134.2" and res["status"] == "INACTIVE"
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=9)
    def test_9_schedule_threat_analytics(self):
        logging.info("Perform schedule operation for member threat analytics")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="member:threatanalytics",params="?_schedinfo.scheduled_time=1793807868")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for member:threatanalytics',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")
		
		
    @pytest.mark.run(order=10)
    def test_10_get_all_fields_member_TA1(self):
        logging.info("Get operation for read all the fields 1")
        member_TA = ib_NIOS.wapi_request('GET', ref="member:threatanalytics", params="?_return_fields=comment,enable_service,host_name,ipv4_address,ipv6_address,status")
        logging.info(member_TA)
        res = json.loads(member_TA)
        print res
        ref1 = res[0]['_ref']
        response1 = ib_NIOS.wapi_request('GET', ref=ref1,params="?_return_fields=comment,enable_service,host_name,ipv4_address,ipv6_address,status")
        logging.info(response1)
        res = json.loads(response1)
        print res
        assert res["host_name"] == "infoblox.localdomain" and res["ipv4_address"] == "10.35.134.2" and res["status"] == "INACTIVE" and res["enable_service"] == False
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=11)
    def test_11_get_all_fields_member_TA2(self):
        logging.info("Get operation for read all the fields 1")
        member_TA = ib_NIOS.wapi_request('GET', ref="member:threatanalytics", params="?_return_fields=comment,enable_service,host_name,ipv4_address,ipv6_address,status")
        logging.info(member_TA)
        res = json.loads(member_TA)
        print res
        ref1 = res[1]['_ref']
        response1 = ib_NIOS.wapi_request('GET', ref=ref1,params="?_return_fields=comment,enable_service,host_name,ipv4_address,ipv6_address,status")
        logging.info(response1)
        res = json.loads(response1)
        print res
        assert res["host_name"] == "member.com" and res["ipv4_address"] == "10.35.118.4" and res["status"] == "INACTIVE" and res["enable_service"] == False
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=12)
    def test_12_comment_with_value_for_ref_member_threat_analytics(self):
        logging.info("Update operation for comment fields with value for member threat analytics ")
        data = {"comment":"member filedistribution details for master node check"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:threatanalytics/YW5hbHl0aWNzLm1lbWJlcl9hbmFseXRpY3NfcHJvcGVydGllcyQw:infoblox.localdomain", params="?_return_fields=comment", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: comment',response1)
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=13)
    def test_13_comment_with_value_threat_analytics(self):
        logging.info("Update operation for comment fields with true")
        data = {"comment": "member filedistribution details for master node"}
        member = ib_NIOS.wapi_request('PUT', ref="member/b25lLnZpcnR1YWxfbm9kZSQw:infoblox.localdomain", params="?_return_fields=comment", fields=json.dumps(data))
        logging.info(member)
	response1 = ib_NIOS.wapi_request('GET', object_type="member:threatanalytics", params="?comment=member%20filedistribution%20details%20for%20master%20node")
        res = json.loads(response1)
        print res
	for i in res:
            logging.info("found")
            assert i["host_name"] == "infoblox.localdomain" and i["ipv4_address"] == "10.35.134.2" and i["status"] == "INACTIVE"
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=14)
    def test_14_enable_service_with_value_for_ref_member_threat_analytics(self):
        logging.info("Update operation for enable_service fields with value for threat analytics ")
        data = {"enable_service":True}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:threatanalytics/YW5hbHl0aWNzLm1lbWJlcl9hbmFseXRpY3NfcHJvcGVydGllcyQw:infoblox.localdomain", params="?_return_fields=enable_service", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'You must configure the blacklist RPZ before starting the analytics service.',response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=15)
    def test_15_enable_service_with_search1_threat_analytics(self):
        logging.info("Search operation for enable_service fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:threatanalytics", params="?enable_service~:=False")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_service',response1)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")
 

    @pytest.mark.run(order=16)
    def test_16_host_name_with_value_for_ref_member_threat_analytics(self):
        logging.info("Update operation for host_name fields with value for member threat analytics ")
        data = {"host_name":"infoblox"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:threatanalytics/YW5hbHl0aWNzLm1lbWJlcl9hbmFseXRpY3NfcHJvcGVydGllcyQw:infoblox.localdomain", params="?_return_fields=host_name", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: host_name',response1)
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=17)
    def test_17_host_name_with_value_threat_analytics(self):
        logging.info("Search operation for host_name fields with true")
	response1 = ib_NIOS.wapi_request('GET', object_type="member:threatanalytics", params="?host_name~:=infoblox.localdomain")
        res = json.loads(response1)
        print res
	for i in res:
            logging.info("found")
            assert i["host_name"] == "infoblox.localdomain" and i["ipv4_address"] == "10.35.134.2" and i["status"] == "INACTIVE"
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=18)
    def test_18_ipv4_address_with_value_for_ref_member_threat_analytics(self):
        logging.info("Update operation for ipv4_address fields with value for member threat analytics ")
        data = {"ipv4_address":"10.35.5.5"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:threatanalytics/YW5hbHl0aWNzLm1lbWJlcl9hbmFseXRpY3NfcHJvcGVydGllcyQw:infoblox.localdomain", params="?_return_fields=ipv4_address", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: ipv4_address',response1)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=19)
    def test_19_ipv4_address_with_value_threat_analytics(self):
        logging.info("Search operation for ipv4_address fields with true")
	response1 = ib_NIOS.wapi_request('GET', object_type="member:threatanalytics", params="?ipv4_address~=10.35.134.2")
        res = json.loads(response1)
        print res
	for i in res:
            logging.info("found")
            assert i["host_name"] == "infoblox.localdomain" and i["ipv4_address"] == "10.35.134.2" and i["status"] == "INACTIVE"
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=20)
    def test_20_ipv6_address_with_value_for_ref_member_threat_analytics(self):
        logging.info("Update operation for ipv6_address fields with value for member threat analytics ")
        data = {"ipv6_address":"2620:10a:6000:2400:8888"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:threatanalytics/YW5hbHl0aWNzLm1lbWJlcl9hbmFseXRpY3NfcHJvcGVydGllcyQw:infoblox.localdomain", params="?_return_fields=ipv6_address", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: ipv6_address',response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")
		
    @pytest.mark.run(order=21)
    def test_21_ipv4_address_with_value_threat_analytics(self):
        logging.info("Search operation for ipv6_address fields with true")
	response1 = ib_NIOS.wapi_request('GET', object_type="member:threatanalytics", params="?ipv6_address~=2620:10a:6000:2400:")
        res = json.loads(response1)
        print res
	for i in res:
            logging.info("found")
            assert i["host_name"] == "infoblox.localdomain" and i["ipv6_address"] == "2620:10a:6000:2400::8602" and i["status"] == "INACTIVE"
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")
		

    @pytest.mark.run(order=22)
    def test_22_status_with_value_for_ref_member_threat_analytics(self):
        logging.info("Update operation for status fields with value for member threat analytics ")
        data = {"status":"INACTIVE"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:threatanalytics/YW5hbHl0aWNzLm1lbWJlcl9hbmFseXRpY3NfcHJvcGVydGllcyQw:infoblox.localdomain", params="?_return_fields=status", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: status',response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=23)
    def test_23_status_with_search1_threat_analytics(self):
        logging.info("Search operation for status fields with ~:= modifier")
        data = {"comment": "member filedistribution details for master node"}
        member = ib_NIOS.wapi_request('PUT', ref="member/b25lLnZpcnR1YWxfbm9kZSQw:infoblox.localdomain", params="?_return_fields=comment", fields=json.dumps(data))
        logging.info(member)
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:threatanalytics", params="?status~:=INACTIVE")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: status',response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")
 
