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
    def test_1_get_member_FD(self):
        logging.info("Get the member File distribution defaults fields ")
        response = ib_NIOS.wapi_request('GET', object_type="member:filedistribution")
        logging.info(response)
        read  = re.search(r'201',response)
        for read in  response:
	        assert True
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=2)
    def test_2_create_member_FD(self):
        logging.info("Get the grid File distribution defaults fields ")
        data = {"host_name": config.grid_fqdn,"ipv4_address": "10.35.2.172"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="member:filedistribution",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for member:filedistribution',response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=3)
    def test_3_delete_member_FD(self):
        logging.info("Deleting the grid File distribution")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = "member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for member:filedistribution',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=4)
    def test_4_csvexport_member_FD(self):
        logging.info("Perform CSV export for grid File distribution")
        data = {"_object":"member:filedistribution"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'member:filedistribution objects do not support CSV export.',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=5)
    def test_5_globalsearch_member_FD(self):
        logging.info("Perform Global search for grid File distribution")
        search_member_FD = ib_NIOS.wapi_request('GET', object_type="search",params="?search_string=infoblox.localdomain")
        logging.info(search_member_FD)
        res = json.loads(search_member_FD)
        print res
        for i in res:
            logging.info("found")
            assert i["host_name"] == config.grid_fqdn
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=6)
    def test_6_schedule_member_FD(self):
        logging.info("Perform schedule operation for grid File distribution")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="member:filedistribution",params="?_schedinfo.scheduled_time=1793807868")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for member:filedistribution',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=7)
    def test_7_approvable_Non_super_user_member_FD(self):
        logging.info("Perform Non super user access to grid File distribution object")
        member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", user="user", password="infoblox")
        logging.info(member_FD)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=8)
    def test_8_approvable_Super_user_member_FD(self):
        logging.info("Perform Super user access to grid File distribution object")
        member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution",user="user1", password="infoblox")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        for i in res:
            logging.info("found")
            assert i["host_name"] == config.grid_fqdn and i["ipv4_address"] == "10.35.2.172" and i["ipv6_address"] == "2620:10a:6000:2400::2ac" and  i["status"] == "INACTIVE"
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=9)
    def test_9_approvable_Non_super_user_with_ref_member_FD(self):
        logging.info("Perform Non super user access to grid File distribution object with reference")
        status,response1 = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", user="user", password="infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 404 and re.search(r'Reference member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain not found',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=10)
    def test_10_approvable_Super_user_with_ref_member_FD(self):
        logging.info("Perform Super user access to grid File distribution object with reference")
        response = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain")
	print response
        logging.info(response)
        read  = re.search(r'200',response)
        for read in  response:
	        assert True

        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=11)
    def test_11_allow_uploads_member_FD(self):
        logging.info("Update operation for allow_uploads fields")
        member_FD = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=allow_uploads")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["allow_uploads"] == False
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=12)
    def test_12_allow_uploads_with_true_member_FD(self):
        logging.info("Update operation for allow_uploads fields with true")
        data = {"allow_uploads": True}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=allow_uploads", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["allow_uploads"] == True
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=13)
    def test_13_allow_uploads_with_false_member_FD(self):
        logging.info("Update operation for allow_uploads fields with false")
        data = {"allow_uploads": False}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=allow_uploads", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["allow_uploads"] == False
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=14)
    def test_14_allow_uploads_with_invalid_member_FD(self):
        logging.info("Update operation for allow_uploads fields with invalid value")
        data = {"allow_uploads": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=allow_uploads", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for allow_uploads: 1: Must be boolean type',response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=15)
    def test_15_allow_uploads_with_search1_member_FD(self):
        logging.info("Search operation for allow_uploads fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?allow_uploads~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=16)
    def test_16_allow_uploads_with_search2_member_FD(self):
        logging.info("Search operation for allow_uploads fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?allow_uploads:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=17)
    def test_17_allow_uploads_with_search3_member_FD(self):
        logging.info("Search operation for allow_uploads fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?allow_uploads=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=18)
    def test_18_allow_uploads_with_search4_member_FD(self):
        logging.info("Search operation for allow_uploads fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?allow_uploads!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=19)
    def test_19_allow_uploads_with_search5_member_FD(self):
        logging.info("Search operation for allow_uploads fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?allow_uploads<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=20)
    def test_20_allow_uploads_with_search6_member_FD(self):
        logging.info("Search operation for allow_uploads fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?allow_uploads>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=21)
    def test_21_comment_member_FD(self):
        logging.info("Update operation for comment fields")
        response = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=comment")
        logging.info(response)
	read = re.search(r'200',response)
	for read in response:
		assert True
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=22)
    def test_22_comment_with_value_member_FD(self):
        logging.info("Update operation for comment fields with value")
        data = {"comment": "update member filedistribution details for master node"}
        response = ib_NIOS.wapi_request('PUT', ref="member/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=comment", fields=json.dumps(data))
        logging.info(response)
        print response
	read = re.search(r'200',response)
	for read in response:
	        assert True
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=23)
    def test_23_comment_member_FD(self):
        logging.info("Get operation after update for comment fields")
        response = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=comment")
        logging.info(response)
        print response
	read = re.search(r'200',response)
	for read in response:
        	assert  True
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=24)
    def test_24_comment_with_value_for_ref_member_FD(self):
        logging.info("Update operation for comment fields with value for member ")
        data = {"comment": "update member filedistribution details for master node"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=comment", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: comment',response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=25)
    def test_25_comment_with_search1_member_FD(self):
        logging.info("Search operation for comment fields with ~:= modifier in member FD")
        response = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?comment~:=node")
        logging.info(response)
        res = json.loads(response)
        read  = re.search(r'200',response)
        for read in  response:
	        assert True

        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=26)
    def test_26_comment_with_search1_member(self):
        logging.info("Search operation for name fields with ~:= modifier in member")
        response = ib_NIOS.wapi_request('GET', object_type="member", params="?comment~:=master")
        logging.info(response)
	print response
        read  = re.search(r'200',response)
        for read in  response:
	        assert True

        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=27)
    def test_27_comment_with_search2_member(self):
        logging.info("Search operation for comment fields with = modifier in member")
        get_member = ib_NIOS.wapi_request('GET', object_type="member", params="?comment=update%20member%20filedistribution%20details%20for%20master%20node")
        logging.info(get_member)
        res = json.loads(get_member)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["config_addr_type"] == "BOTH" and i["host_name"] == config.grid_fqdn and i["platform"] == "INFOBLOX" and  i["service_type_configuration"] == "ALL_V4"
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=28)
    def test_28_comment_with_search2_member_FD(self):
        logging.info("Search operation for comment fields with = modifier in member FD")
        get_member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?comment=update%20member%20filedistribution%20details%20for%20master%20node")
        logging.info(get_member_FD)
        res = json.loads(get_member_FD)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["host_name"] == config.grid_fqdn and i["ipv4_address"] == "10.35.2.172" and i["ipv6_address"] == "2620:10a:6000:2400::2ac" and  i["status"] == "INACTIVE"
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=29)
    def test_29_comment_with_search3_member_FD(self):
        logging.info("Search operation for name fields with := modifier")
        get_member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?comment:=update%20Member%20filedistribution%20details%20for%20master%20node")
        logging.info(get_member_FD)
        res = json.loads(get_member_FD)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["host_name"] == config.grid_fqdn and i["ipv4_address"] == "10.35.2.172" and i["ipv6_address"] == "2620:10a:6000:2400::2ac" and  i["status"] == "INACTIVE"
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=30)
    def test_30_comment_with_search4_member_FD(self):
        logging.info("Search operation for comment fields with :~= modifier in member FD")
        response = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?comment:~=Member%20Filedistribution%20")
        logging.info(response)
        print response
        read  = re.search(r'200',response)
        for read in  response:
                assert True
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=31)
    def test_31_comment_with_search5_member_FD(self):
        logging.info("Search operation for comment fields with != modifier in member FD")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?comment!=node")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '!' not allowed for field: comment",response1)
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=32)
    def test_32_comment_with_search6_member_FD(self):
        logging.info("Search operation for comment fields with <= modifier in member FD")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?comment<=node")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '<' not allowed for field: comment",response1)
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=33)
    def test_33_comment_with_search7_member_FD(self):
        logging.info("Search operation for comment fields with >= modifier in member FD")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?comment>=node")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '>' not allowed for field: comment",response1)
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=34)
    def test_34_enable_ftp_member_FD(self):
        logging.info("Update operation for enable_ftp fields")
        member_FD = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_ftp"] == False
        logging.info("Test Case 34 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=35)
    def test_35_enable_ftp_with_true_member_FD(self):
        logging.info("Update operation for enable_ftp fields with true")
        data = {"enable_ftp": True}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_ftp"] == True
        logging.info("Test Case 35 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=36)
    def test_36_enable_ftp_with_false_member_FD(self):
        logging.info("Update operation for enable_ftp fields with false")
        data = {"enable_ftp": False}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_ftp"] == False
        logging.info("Test Case 36 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=37)
    def test_37_enable_ftp_with_invalid_member_FD(self):
        logging.info("Update operation for enable_ftp fields with invalid value")
        data = {"enable_ftp": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for enable_ftp: 1: Must be boolean type',response1)
        logging.info("Test Case 37 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=38)
    def test_38_enable_ftp_with_search1_member_FD(self):
        logging.info("Search operation for enable_ftp fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp',response1)
        logging.info("Test Case 38 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=39)
    def test_39_enable_ftp_with_search2_member_FD(self):
        logging.info("Search operation for enable_ftp fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp',response1)
        logging.info("Test Case 39 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=40)
    def test_40_enable_ftp_with_search3_member_FD(self):
        logging.info("Search operation for enable_ftp fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp',response1)
        logging.info("Test Case 40 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=41)
    def test_41_enable_ftp_with_search4_member_FD(self):
        logging.info("Search operation for enable_ftp fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp',response1)
        logging.info("Test Case 41 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=42)
    def test_42_enable_ftp_with_search5_member_FD(self):
        logging.info("Search operation for enable_ftp fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp',response1)
        logging.info("Test Case 42 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=43)
    def test_43_enable_ftp_with_search6_member_FD(self):
        logging.info("Search operation for enable_ftp fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp',response1)
        logging.info("Test Case 43 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=44)
    def test_44_enable_ftp_filelist_member_FD(self):
        logging.info("Update operation for enable_ftp_filelist fields")
        member_FD = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp_filelist")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_ftp_filelist"] == False
        logging.info("Test Case 44 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=45)
    def test_45_enable_ftp_filelist_with_true_member_FD(self):
        logging.info("Update operation for enable_ftp_filelist fields with true")
        data = {"enable_ftp_filelist": True}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp_filelist", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_ftp_filelist"] == True
        logging.info("Test Case 45 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=46)
    def test_46_enable_ftp_filelist_with_false_member_FD(self):
        logging.info("Update operation for enable_ftp_filelist fields with false")
        data = {"enable_ftp_filelist": False}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp_filelist", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_ftp_filelist"] == False
        logging.info("Test Case 46 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=47)
    def test_47_enable_ftp_filelist_with_invalid_member_FD(self):
        logging.info("Update operation for enable_ftp_filelist fields with invalid value")
        data = {"enable_ftp_filelist": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp_filelist", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for enable_ftp_filelist: 1: Must be boolean type',response1)
        logging.info("Test Case 47 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=48)
    def test_48_enable_ftp_filelist_with_search1_member_FD(self):
        logging.info("Search operation for enable_ftp_filelist fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_filelist~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_filelist',response1)
        logging.info("Test Case 48 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=49)
    def test_49_enable_ftp_filelist_with_search2_member_FD(self):
        logging.info("Search operation for enable_ftp_filelist fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_filelist:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_filelist',response1)
        logging.info("Test Case 49 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=50)
    def test_50_enable_ftp_filelist_with_search3_member_FD(self):
        logging.info("Search operation for enable_ftp_filelist fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_filelist=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_filelist',response1)
        logging.info("Test Case 50 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=51)
    def test_51_enable_ftp_filelist_with_search4_member_FD(self):
        logging.info("Search operation for enable_ftp_filelist fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_filelist!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_filelist',response1)
        logging.info("Test Case 51 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=52)
    def test_52_enable_ftp_filelist_with_search5_member_FD(self):
        logging.info("Search operation for enable_ftp_filelist fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_filelist<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_filelist',response1)
        logging.info("Test Case 52 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=53)
    def test_53_enable_ftp_filelist_with_search6_member_FD(self):
        logging.info("Search operation for enable_ftp_filelist fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_filelist>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_filelist',response1)
        logging.info("Test Case 53 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=54)
    def test_54_enable_ftp_passive_member_FD(self):
        logging.info("Update operation for enable_ftp_passive fields")
        member_FD = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp_passive")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_ftp_passive"] == True
        logging.info("Test Case 54 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=55)
    def test_55_enable_ftp_passive_with_true_member_FD(self):
        logging.info("Update operation for enable_ftp_passive fields with true")
        data = {"enable_ftp_passive": True}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp_passive", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_ftp_passive"] == True
        logging.info("Test Case 55 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=56)
    def test_56_enable_ftp_passive_with_false_member_FD(self):
        logging.info("Update operation for enable_ftp_passive fields with false")
        data = {"enable_ftp_passive": False}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp_passive", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_ftp_passive"] == False
        logging.info("Test Case 56 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=57)
    def test_57_enable_ftp_passive_with_invalid_member_FD(self):
        logging.info("Update operation for enable_ftp_passive fields with invalid value")
        data = {"enable_ftp_passive": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_ftp_passive", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for enable_ftp_passive: 1: Must be boolean type',response1)
        logging.info("Test Case 57 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=58)
    def test_58_enable_ftp_passive_with_search1_member_FD(self):
        logging.info("Search operation for enable_ftp_passive fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_passive~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_passive',response1)
        logging.info("Test Case 58 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=59)
    def test_59_enable_ftp_passive_with_search2_member_FD(self):
        logging.info("Search operation for enable_ftp_passive fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_passive:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_passive',response1)
        logging.info("Test Case 59 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=60)
    def test_60_enable_ftp_passive_with_search3_member_FD(self):
        logging.info("Search operation for enable_ftp_passive fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_passive=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_passive',response1)
        logging.info("Test Case 60 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=61)
    def test_61_enable_ftp_passive_with_search4_member_FD(self):
        logging.info("Search operation for enable_ftp_passive fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_passive!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_passive',response1)
        logging.info("Test Case 61 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=62)
    def test_62_enable_ftp_passive_with_search5_member_FD(self):
        logging.info("Search operation for enable_ftp_passive fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_passive<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_passive',response1)
        logging.info("Test Case 62 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=63)
    def test_63_enable_ftp_passive_with_search6_member_FD(self):
        logging.info("Search operation for enable_ftp_passive fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_ftp_passive>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_ftp_passive',response1)
        logging.info("Test Case 63 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=64)
    def test_64_enable_http_member_FD(self):
        logging.info("Update operation for enable_http fields")
        member_FD = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_http"] == False
        logging.info("Test Case 64 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=65)
    def test_65_enable_http_with_true_member_FD(self):
        logging.info("Update operation for enable_http fields with true")
        data = {"enable_http": True}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_http"] == True
        logging.info("Test Case 65 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=66)
    def test_66_enable_http_with_false_member_FD(self):
        logging.info("Update operation for enable_http fields with false")
        data = {"enable_http": False}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_http"] == False
        logging.info("Test Case 66 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=67)
    def test_67_enable_http_with_invalid_member_FD(self):
        logging.info("Update operation for enable_http fields with invalid value")
        data = {"enable_http": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for enable_http: 1: Must be boolean type',response1)
        logging.info("Test Case 67 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=68)
    def test_68_enable_http_with_search1_member_FD(self):
        logging.info("Search operation for enable_http fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http',response1)
        logging.info("Test Case 68 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=69)
    def test_69_enable_http_with_search2_member_FD(self):
        logging.info("Search operation for enable_http fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http',response1)
        logging.info("Test Case 69 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=70)
    def test_70_enable_http_with_search3_member_FD(self):
        logging.info("Search operation for enable_http fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http',response1)
        logging.info("Test Case 70 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=71)
    def test_71_enable_http_with_search4_member_FD(self):
        logging.info("Search operation for enable_http fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http',response1)
        logging.info("Test Case 71 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=72)
    def test_72_enable_http_with_search5_member_FD(self):
        logging.info("Search operation for enable_http fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http',response1)
        logging.info("Test Case 72 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=73)
    def test_73_enable_http_with_search6_member_FD(self):
        logging.info("Search operation for enable_http fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http',response1)
        logging.info("Test Case 73 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=74)
    def test_74_enable_http_acl_member_FD(self):
        logging.info("Update operation for enable_http_acl fields")
        member_FD = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http_acl")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_http_acl"] == False
        logging.info("Test Case 74 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=75)
    def test_75_enable_http_acl_with_true_member_FD(self):
        logging.info("Update operation for enable_http_acl fields with true")
        data = {"enable_http_acl": True}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http_acl", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_http_acl"] == True
        logging.info("Test Case 75 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=76)
    def test_76_enable_http_acl_with_false_member_FD(self):
        logging.info("Update operation for enable_http_acl fields with false")
        data = {"enable_http_acl": False}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http_acl", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_http_acl"] == False
        logging.info("Test Case 76 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=77)
    def test_77_enable_http_acl_with_invalid_member_FD(self):
        logging.info("Update operation for enable_http_acl fields with invalid value")
        data = {"enable_http_acl": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http_acl", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for enable_http_acl: 1: Must be boolean type',response1)
        logging.info("Test Case 77 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=78)
    def test_78_enable_http_acl_with_search1_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 78 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=79)
    def test_79_enable_http_acl_with_search2_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 79 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=80)
    def test_80_enable_http_acl_with_search3_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 80 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=81)
    def test_81_enable_http_acl_with_search4_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 81 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=82)
    def test_82_enable_http_acl_with_search5_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 82 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=83)
    def test_83_enable_http_acl_with_search6_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 83 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=84)
    def test_84_enable_http_acl_member_FD(self):
        logging.info("Update operation for enable_http_acl fields")
        member_FD = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http_acl")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_http_acl"] == False
        logging.info("Test Case 84 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=85)
    def test_85_enable_http_acl_with_true_member_FD(self):
        logging.info("Update operation for enable_http_acl fields with true")
        data = {"enable_http_acl": True}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http_acl", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_http_acl"] == True
        logging.info("Test Case 85 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=86)
    def test_86_enable_http_acl_with_false_member_FD(self):
        logging.info("Update operation for enable_http_acl fields with false")
        data = {"enable_http_acl": False}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http_acl", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["enable_http_acl"] == False
        logging.info("Test Case 86 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=87)
    def test_87_enable_http_acl_with_invalid_member_FD(self):
        logging.info("Update operation for enable_http_acl fields with invalid value")
        data = {"enable_http_acl": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=enable_http_acl", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for enable_http_acl: 1: Must be boolean type',response1)
        logging.info("Test Case 87 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=88)
    def test_88_enable_http_acl_with_search1_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 88 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=89)
    def test_89_enable_http_acl_with_search2_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 89 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=90)
    def test_90_enable_http_acl_with_search3_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 90 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=91)
    def test_91_enable_http_acl_with_search4_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 91 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=92)
    def test_92_enable_http_acl_with_search5_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 92 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=93)
    def test_93_enable_http_acl_with_search6_member_FD(self):
        logging.info("Search operation for enable_http_acl fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?enable_http_acl>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_http_acl',response1)
        logging.info("Test Case 93 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=94)
    def test_94_ftp_acls_member_FD(self):
        logging.info("Get operation for ftp_acls fields")
        member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=ftp_acls")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        logging.info("Test Case 94 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=95)
    def test_95_ftp_acls_with_true_member_FD(self):
        logging.info("Update operation for ftp_acls fields with acl values")
        data = {"ftp_acls":[{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.36.199.8","permission": "DENY"},{"address": "10.35.0.0/16","permission": "ALLOW"},{"address": "10.37.0.0/16","permission": "DENY"},{"address": "Any","permission": "ALLOW"}] }
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_acls", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["ftp_acls"] == [{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.36.199.8","permission": "DENY"},{"address": "10.35.0.0/16","permission": "ALLOW"},{"address": "10.37.0.0/16","permission": "DENY"},{"address": "Any","permission": "ALLOW"}]
        logging.info("Test Case 95 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=96)
    def test_96_ftp_acls_with_true_member_FD(self):
        logging.info("Update operation for ftp_acls fields with empty values")
        data = {"ftp_acls":[] }
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_acls", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        logging.info("Test Case 96 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=97)
    def test_97_ftp_acls_with_invalid1_grid_FD(self):
        logging.info("Update operation for ftp_acls fields with invalid value for address")
        data = {"ftp_acls":[{"address": "10.36.199.711","permission": "ALLOW"}] }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid address_string '10.36.199.711'",response1)
        logging.info("Test Case 97 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=98)
    def test_98_ftp_acls_with_invalid2_grid_FD(self):
        logging.info("Update operation for ftp_acls fields with invalid value for permission")
        data = {"ftp_acls":[{"address": "10.36.199.7","permission": "ALLOW1"}] }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for permission .*ALLOW1.* valid values are: ALLOW, DENY',response1)
        logging.info("Test Case 98 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=99)
    def test_99_ftp_acls_with_invalid3_grid_FD(self):
        logging.info("Update operation for ftp_acls fields with invalid value for address with network")
        data = {"ftp_acls":[{"address": "10.35.0.0/166","permission": "ALLOW"}] }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid address_string '10.35.0.0/166'",response1)
        logging.info("Test Case 99 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=100)
    def test_100_ftp_acls_with_invalid4_grid_FD(self):
        logging.info("Update operation for ftp_acls fields with invalid value for permission DENY")
        data = {"ftp_acls":[{"address": "10.37.0.0/16","permission": "DENY1"}] }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for permission .*"DENY1.* valid values are: ALLOW, DENY',response1)
        logging.info("Test Case 100 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=101)
    def test_101_ftp_acls_with_invalid5_grid_FD(self):
        logging.info("Update operation for ftp_acls fields with invalid value for address with ANY value")
        data = {"ftp_acls":[{"address": "ANY","permission": "ALLOW"}] }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid address_string 'ANY'",response1)
        logging.info("Test Case 101 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=102)
    def test_102_ftp_acls_with_true_member_FD(self):
        logging.info("Update operation for ftp_acls fields with acl values 1")
        data = {"ftp_acls": [{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.36.199.8","permission": "DENY"},{"address": "10.37.0.0/16","permission": "ALLOW"},{"address": "10.35.0.0/16","permission": "DENY"},{"address": "Any","permission": "DENY"}]}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_acls", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["ftp_acls"] == [{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.36.199.8","permission": "DENY"},{"address": "10.37.0.0/16","permission": "ALLOW"},{"address": "10.35.0.0/16","permission": "DENY"},{"address": "Any","permission": "DENY"}]
        logging.info("Test Case 102 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=103)
    def test_103_ftp_acls_with_search1_member_FD(self):
        logging.info("Search operation for ftp_acls fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_acls~:=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_acls',response1)
        logging.info("Test Case 103 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=104)
    def test_104_ftp_acls_with_search2_member_FD(self):
        logging.info("Search operation for ftp_acls fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_acls:=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_acls',response1)
        logging.info("Test Case 104 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=105)
    def test_105_ftp_acls_with_search3_member_FD(self):
        logging.info("Search operation for ftp_acls fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_acls=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_acls',response1)
        logging.info("Test Case 105 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=106)
    def test_106_ftp_acls_with_search4_member_FD(self):
        logging.info("Search operation for ftp_acls fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_acls!=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_acls',response1)
        logging.info("Test Case 106 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=107)
    def test_107_ftp_acls_with_search5_member_FD(self):
        logging.info("Search operation for ftp_acls fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_acls<=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_acls',response1)
        logging.info("Test Case 107 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=108)
    def test_108_ftp_acls_with_search6_member_FD(self):
        logging.info("Search operation for ftp_acls fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_acls>=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_acls',response1)
        logging.info("Test Case 108 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=109)
    def test_109_ftp_port_member_FD(self):
        logging.info("Get operation for ftp_port fields")
        member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=ftp_port")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        response1 = str(res)
        assert  re.search(r'21',response1)
        logging.info("Test Case 109 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=110)
    def test_110_ftp_port_with_invalid1_grid_FD(self):
        logging.info("Update operation for ftp_port fields with invalid value ")
        data = {"ftp_port": 0.0 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_port", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for ftp_port: 0.0: Must be integer type',response1)
        logging.info("Test Case 110 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=111)
    def test_111_ftp_port_with_invalid2_grid_FD(self):
        logging.info("Update operation for ftp_port fields with invalid value for permission")
        data = {"ftp_port": -1 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_port", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for ftp_port: -1: Invalid value, must be between 0 and 4294967295',response1)
        logging.info("Test Case 111 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=112)
    def test_112_ftp_port_with_invalid3_grid_FD(self):
        logging.info("Update operation for ftp_port fields with invalid value for permission")
        data = {"ftp_port": 4294967295 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_port", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid FTP port number. It should be an integer from 1 to 63999',response1)
        logging.info("Test Case 112 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=113)
    def test_113_ftp_port_with_invalid4_grid_FD(self):
        logging.info("Update operation for ftp_port fields with invalid value for permission")
        data = {"ftp_port": "a" }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_port", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for ftp_port: .*a.*: Must be integer type',response1)
        logging.info("Test Case 113 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=114)
    def test_114_ftp_port_with_invalid4_grid_FD(self):
        logging.info("Update operation for ftp_port fields with invalid value for permission")
        data = {"ftp_port": 0 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_port", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid FTP port number. It should be an integer from 1 to 63999',response1)
        logging.info("Test Case 114 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=115)
    def test_115_ftp_port_with_search1_member_FD(self):
        logging.info("Search operation for ftp_port fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_port~:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_port',response1)
        logging.info("Test Case 115 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=116)
    def test_116_ftp_port_with_search2_member_FD(self):
        logging.info("Search operation for ftp_port fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_port:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_port',response1)
        logging.info("Test Case 116 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=117)
    def test_117_ftp_port_with_search3_member_FD(self):
        logging.info("Search operation for ftp_port fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_port=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_port',response1)
        logging.info("Test Case 117 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=118)
    def test_118_ftp_port_with_search4_member_FD(self):
        logging.info("Search operation for ftp_port fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_port!=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_port',response1)
        logging.info("Test Case 118 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=119)
    def test_119_ftp_port_with_search5_member_FD(self):
        logging.info("Search operation for ftp_port fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_port<=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_port',response1)
        logging.info("Test Case 119 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=120)
    def test_120_ftp_port_with_search6_member_FD(self):
        logging.info("Search operation for ftp_port fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_port>=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_port',response1)
        logging.info("Test Case 120 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=121)
    def test_121_ftp_status_member_FD(self):
        logging.info("Get operation for ftp_status fields")
        member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=ftp_status")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        response1 = str(res)
        assert  re.search(r'INACTIVE',response1)
        logging.info("Test Case 121 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=122)
    def test_122_ftp_status_with_invalid1_grid_FD(self):
        logging.info("Update operation for ftp_status fields with invalid value ")
        data = {"ftp_status": 1 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ftp_status", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: ftp_status',response1)
        logging.info("Test Case 122 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=123)
    def test_123_ftp_status_with_search1_member_FD(self):
        logging.info("Search operation for ftp_status fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_status~:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_status',response1)
        logging.info("Test Case 123 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=124)
    def test_124_ftp_status_with_search2_member_FD(self):
        logging.info("Search operation for ftp_status fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_status:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_status',response1)
        logging.info("Test Case 124 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=125)
    def test_125_ftp_status_with_search3_member_FD(self):
        logging.info("Search operation for ftp_status fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_status=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_status',response1)
        logging.info("Test Case 125 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=126)
    def test_126_ftp_status_with_search4_member_FD(self):
        logging.info("Search operation for ftp_status fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_status!=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_status',response1)
        logging.info("Test Case 126 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=127)
    def test_127_ftp_status_with_search5_member_FD(self):
        logging.info("Search operation for ftp_status fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_status<=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_status',response1)
        logging.info("Test Case 127 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=128)
    def test_128_ftp_status_with_search6_member_FD(self):
        logging.info("Search operation for ftp_status fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ftp_status>=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ftp_status',response1)
        logging.info("Test Case 128 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=129)
    def test_129_host_name_member_FD(self):
        logging.info("Get operation for host_name fields")
        response = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=host_name")
        logging.info(response)
        print response
        read  = re.search(r'200',response)
        for read in  response:
                assert True

        logging.info("Test Case 129 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=130)
    def test_130_host_name_with_invalid1_grid_FD(self):
        logging.info("Update operation for host_name fields with invalid value ")
        data = {"host_name": 1 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=host_name", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: host_name',response1)
        logging.info("Test Case 130 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=131)
    def test_131_host_name_with_search1_member_FD(self):
        logging.info("Search operation for host_name fields with ~:= modifier")
        member_fd = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?host_name~:=infoblox.localdomain")
        logging.info(member_fd)
        res = json.loads(member_fd)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["host_name"] == config.grid_fqdn and i["status"] == "INACTIVE" and i["ipv4_address"] == "10.35.2.172" and  i["ipv6_address"] == "2620:10a:6000:2400::2ac"
        logging.info("Test Case 131 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=132)
    def test_132_host_name_with_search2_member_FD(self):
        logging.info("Search operation for host_name fields with := modifier")
        member_fd = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?host_name:=infoblox.localdomain")
        logging.info(member_fd)
        res = json.loads(member_fd)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["host_name"] == config.grid_fqdn and i["status"] == "INACTIVE" and i["ipv4_address"] == "10.35.2.172" and  i["ipv6_address"] == "2620:10a:6000:2400::2ac"
        logging.info("Test Case 132 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=133)
    def test_133_host_name_with_search3_member_FD(self):
        logging.info("Search operation for host_name fields with = modifier")
        member_fd = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?host_name=infoblox.localdomain")
        logging.info(member_fd)
        res = json.loads(member_fd)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["host_name"] == config.grid_fqdn and i["status"] == "INACTIVE" and i["ipv4_address"] == "10.35.2.172" and  i["ipv6_address"] == "2620:10a:6000:2400::2ac"
        logging.info("Test Case 133 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=134)
    def test_134_host_name_with_search4_member_FD(self):
        logging.info("Search operation for host_name fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?host_name!=infoblox.localdomain")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '!' not allowed for field: host_name",response1)
        logging.info("Test Case 134 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=135)
    def test_135_host_name_with_search5_member_FD(self):
        logging.info("Search operation for host_name fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?host_name<=infoblox.localdomain")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '<' not allowed for field: host_name",response1)
        logging.info("Test Case 135 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=136)
    def test_136_host_name_with_search6_member_FD(self):
        logging.info("Search operation for host_name fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?host_name>=infoblox.localdomain")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '>' not allowed for field: host_name",response1)
        logging.info("Test Case 136 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=137)
    def test_137_http_acls_member_FD(self):
        logging.info("Get operation for http_acls fields")
        member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=http_acls")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        logging.info("Test Case 137 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=138)
    def test_138_http_acls_with_valid1_grid_FD(self):
        logging.info("Update operation for http_acls fields with acl value ")
        data = {"http_acls":[{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.35.0.0/16","permission": "ALLOW"}],"enable_http_acl": True }
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=http_acls", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert  res["http_acls"] == [{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.35.0.0/16","permission": "ALLOW"}]
        logging.info("Test Case 138 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=139)
    def test_139_http_acls_with_Invalid1_grid_FD(self):
        logging.info("Update operation for http_acls fields with acl value ")
        data = {"http_acls":[{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.35.0.0/16","permission": "DENY"}],"enable_http_acl":True }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=http_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Anonymous ACL contains ac item with permission 'DENY' which is not allowed for 'HTTP'",response1)
        logging.info("Test Case 139 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=140)
    def test_140_http_acls_with_Invalid1_grid_FD(self):
        logging.info("Update operation for http_acls fields with acl value ")
        data = {"http_acls":[{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.35.0.0/166","permission": "ALLOW"}],"enable_http_acl":True }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=http_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid address_string '10.35.0.0/166'",response1)
        logging.info("Test Case 140 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=141)
    def test_141_http_acls_with_search1_member_FD(self):
        logging.info("Search operation for http_acls fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_acls~:=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_acls',response1)
        logging.info("Test Case 141 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=142)
    def test_142_http_acls_with_search2_member_FD(self):
        logging.info("Search operation for http_acls fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_acls:=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_acls',response1)
        logging.info("Test Case 142 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=143)
    def test_143_http_acls_with_search3_member_FD(self):
        logging.info("Search operation for http_acls fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_acls=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_acls',response1)
        logging.info("Test Case 143 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=144)
    def test_144_http_acls_with_search4_member_FD(self):
        logging.info("Search operation for http_acls fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_acls!=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_acls',response1)
        logging.info("Test Case 144 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=145)
    def test_145_http_acls_with_search5_member_FD(self):
        logging.info("Search operation for http_acls fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_acls<=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_acls',response1)
        logging.info("Test Case 145 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=146)
    def test_146_http_acls_with_search6_member_FD(self):
        logging.info("Search operation for http_acls fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_acls>=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_acls',response1)
        logging.info("Test Case 146 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=147)
    def test_147_http_status_member_FD(self):
        logging.info("Get operation for http_status fields")
        member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=http_status")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        response1 = str(res)
        assert  re.search(r'INACTIVE',response1)
        logging.info("Test Case 147 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=148)
    def test_148_http_status_with_invalid1_grid_FD(self):
        logging.info("Update operation for http_status fields with invalid value ")
        data = {"http_status": 1 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=http_status", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: http_status',response1)
        logging.info("Test Case 148 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=149)
    def test_149_http_status_with_search1_member_FD(self):
        logging.info("Search operation for http_status fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_status~:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_status',response1)
        logging.info("Test Case 149 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=150)
    def test_150_http_status_with_search2_member_FD(self):
        logging.info("Search operation for http_status fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_status:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_status',response1)
        logging.info("Test Case 150 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=151)
    def test_151_http_status_with_search3_member_FD(self):
        logging.info("Search operation for http_status fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_status=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_status',response1)
        logging.info("Test Case 151 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=152)
    def test_152_http_status_with_search4_member_FD(self):
        logging.info("Search operation for http_status fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_status!=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_status',response1)
        logging.info("Test Case 152 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=153)
    def test_153_http_status_with_search5_member_FD(self):
        logging.info("Search operation for http_status fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_status<=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_status',response1)
        logging.info("Test Case 153 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=154)
    def test_154_http_status_with_search6_member_FD(self):
        logging.info("Search operation for http_status fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?http_status>=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: http_status',response1)
        logging.info("Test Case 154 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=155)
    def test_155_ipv4_address_member_FD(self):
        logging.info("Get operation for ipv4_address fields")
        response = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=ipv4_address")
        logging.info(response)
        print response
        read  = re.search(r'200',response)
        for read in  response:
                assert True

        logging.info("Test Case 155 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=156)
    def test_156_ipv4_address_with_invalid1_grid_FD(self):
        logging.info("Update operation for ipv4_address fields with invalid value ")
        data = {"ipv4_address": 1 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ipv4_address", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: ipv4_address',response1)
        logging.info("Test Case 156 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=157)
    def test_157_ipv4_address_with_search1_member_FD(self):
        logging.info("Search operation for ipv4_address fields with ~:= modifier")
        member_fd = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv4_address~=10.35.2.172")
        logging.info(member_fd)
        res = json.loads(member_fd)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["host_name"] == config.grid_fqdn and i["status"] == "INACTIVE" and i["ipv4_address"] == "10.35.2.172" and  i["ipv6_address"] == "2620:10a:6000:2400::2ac"
        logging.info("Test Case 157 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=158)
    def test_158_ipv4_address_with_search3_member_FD(self):
        logging.info("Search operation for ipv4_address fields with = modifier")
        member_fd = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv4_address=10.35.2.172")
        logging.info(member_fd)
        res = json.loads(member_fd)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["host_name"] == config.grid_fqdn and i["status"] == "INACTIVE" and i["ipv4_address"] == "10.35.2.172" and  i["ipv6_address"] == "2620:10a:6000:2400::2ac"
        logging.info("Test Case 158 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=159)
    def test_159_ipv4_address_with_search2_member_FD(self):
        logging.info("Search operation for ipv4_address fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv4_address:=10.35.2.172")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: ipv4_address",response1)
        logging.info("Test Case 160 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=160)
    def test_160_ipv4_address_with_search4_member_FD(self):
        logging.info("Search operation for ipv4_address fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv4_address!=10.35.2.172")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '!' not allowed for field: ipv4_address",response1)
        logging.info("Test Case 160 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=161)
    def test_161_ipv4_address_with_search5_member_FD(self):
        logging.info("Search operation for ipv4_address fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv4_address<=10.35.2.172")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '<' not allowed for field: ipv4_address",response1)
        logging.info("Test Case 161 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=162)
    def test_162_ipv4_address_with_search6_member_FD(self):
        logging.info("Search operation for ipv4_address fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv4_address>=10.35.2.172")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '>' not allowed for field: ipv4_address",response1)
        logging.info("Test Case 162 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=163)
    def test_163_ipv4_address_member_FD(self):
        logging.info("Get operation for ipv6_address fields")
        response = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=ipv6_address")
        logging.info(response)
        res = json.loads(response)
        print response
        read  = re.search(r'200',response)
        for read in  response:
                assert True

        logging.info("Test Case 163 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=164)
    def test_164_ipv6_address_with_invalid1_grid_FD(self):
        logging.info("Update operation for ipv6_address fields with invalid value ")
        data = {"ipv6_address": 1 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=ipv6_address", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not writable: ipv6_address",response1)
        logging.info("Test Case 164 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=165)
    def test_165_ipv6_address_with_search1_member_FD(self):
        logging.info("Search operation for ipv6_address fields with ~:= modifier")
        response = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv6_address~=2620:10a:6000:2400::")
        logging.info(response)
        print response
        read  = re.search(r'200',response)
        for read in  response:
                assert True

        logging.info("Test Case 165 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=166)
    def test_166_ipv6_address_with_search3_member_FD(self):
        logging.info("Search operation for ipv6_address fields with = modifier")
        member_fd = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv6_address=2620:10a:6000:2400::2ac")
        logging.info(member_fd)
        res = json.loads(member_fd)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["host_name"] == config.grid_fqdn and i["status"] == "INACTIVE" and i["ipv4_address"] == "10.35.2.172" and  i["ipv6_address"] == "2620:10a:6000:2400::2ac"
        logging.info("Test Case 166 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=167)
    def test_167_ipv6_address_with_search2_member_FD(self):
        logging.info("Search operation for ipv6_address fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv6_address:=2620:10a:6000:2400::2ac")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: ipv6_address",response1)
        logging.info("Test Case 167 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=168)
    def test_168_ipv6_address_with_search4_member_FD(self):
        logging.info("Search operation for ipv6_address fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv6_address!=2620:10a:6000:2400::2ac")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '!' not allowed for field: ipv6_address",response1)
        logging.info("Test Case 168 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=169)
    def test_169_ipv6_address_with_search5_member_FD(self):
        logging.info("Search operation for ipv6_address fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv6_address<=2620:10a:6000:2400::2ac")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '<' not allowed for field: ipv6_address",response1)
        logging.info("Test Case 169 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=170)
    def test_170_ipv6_address_with_search6_member_FD(self):
        logging.info("Search operation for ipv6_address fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?ipv6_address>=2620:10a:6000:2400::2ac")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '>' not allowed for field: ipv6_address",response1)
        logging.info("Test Case 170 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=171)
    def test_171_status_member_FD(self):
        logging.info("Get operation for status fields")
        member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=status")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        response1 = str(res)
        assert  re.search(r'INACTIVE',response1)
        logging.info("Test Case 171 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=172)
    def test_172_status_with_invalid1_grid_FD(self):
        logging.info("Update operation for status fields with invalid value ")
        data = {"status": 1 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=status", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: status',response1)
        logging.info("Test Case 172 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=173)
    def test_173_status_with_search1_member_FD(self):
        logging.info("Search operation for status fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?status~:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: status',response1)
        logging.info("Test Case 173 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=174)
    def test_174_status_with_search2_member_FD(self):
        logging.info("Search operation for status fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?status:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: status',response1)
        logging.info("Test Case 174 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=175)
    def test_175_status_with_search3_member_FD(self):
        logging.info("Search operation for status fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?status=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: status',response1)
        logging.info("Test Case 175 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=176)
    def test_176_status_with_search4_member_FD(self):
        logging.info("Search operation for status fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?status!=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: status',response1)
        logging.info("Test Case 176 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=177)
    def test_177_status_with_search5_member_FD(self):
        logging.info("Search operation for status fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?status<=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: status',response1)
        logging.info("Test Case 177 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=178)
    def test_178_status_with_search6_member_FD(self):
        logging.info("Search operation for status fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?status>=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: status',response1)
        logging.info("Test Case 178 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=179)
    def test_179_tftp_acls_member_FD(self):
        logging.info("Get operation for tftp_acls fields")
        member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=tftp_acls")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        logging.info("Test Case 179 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=180)
    def test_180_tftp_acls_with_true_member_FD(self):
        logging.info("Update operation for tftp_acls fields with acl values")
        data = {"tftp_acls":[{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.36.199.8","permission": "DENY"},{"address": "10.35.0.0/16","permission": "ALLOW"},{"address": "10.37.0.0/16","permission": "DENY"},{"address": "Any","permission": "ALLOW"}] }
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_acls", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["tftp_acls"] == [{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.36.199.8","permission": "DENY"},{"address": "10.35.0.0/16","permission": "ALLOW"},{"address": "10.37.0.0/16","permission": "DENY"},{"address": "Any","permission": "ALLOW"}]
        logging.info("Test Case 180 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=181)
    def test_181_tftp_acls_with_true_member_FD(self):
        logging.info("Update operation for tftp_acls fields with empty values")
        data = {"tftp_acls":[] }
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_acls", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        logging.info("Test Case 181 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=182)
    def test_182_tftp_acls_with_invalid1_grid_FD(self):
        logging.info("Update operation for tftp_acls fields with invalid value for address")
        data = {"tftp_acls":[{"address": "10.36.199.711","permission": "ALLOW"}] }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid address_string '10.36.199.711'",response1)
        logging.info("Test Case 182 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=183)
    def test_183_tftp_acls_with_invalid2_grid_FD(self):
        logging.info("Update operation for tftp_acls fields with invalid value for permission")
        data = {"tftp_acls":[{"address": "10.36.199.7","permission": "ALLOW1"}] }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for permission .*ALLOW1.* valid values are: ALLOW, DENY',response1)
        logging.info("Test Case 183 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=184)
    def test_184_tftp_acls_with_invalid3_grid_FD(self):
        logging.info("Update operation for tftp_acls fields with invalid value for address with network")
        data = {"tftp_acls":[{"address": "10.35.0.0/166","permission": "ALLOW"}] }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid address_string '10.35.0.0/166'",response1)
        logging.info("Test Case 184 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=185)
    def test_185_tftp_acls_with_invalid4_grid_FD(self):
        logging.info("Update operation for tftp_acls fields with invalid value for permission DENY")
        data = {"tftp_acls":[{"address": "10.37.0.0/16","permission": "DENY1"}] }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for permission .*"DENY1.* valid values are: ALLOW, DENY',response1)
        logging.info("Test Case 185 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=186)
    def test_186_tftp_acls_with_invalid5_grid_FD(self):
        logging.info("Update operation for tftp_acls fields with invalid value for address with ANY value")
        data = {"tftp_acls":[{"address": "ANY","permission": "ALLOW"}] }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_acls", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid address_string 'ANY'",response1)
        logging.info("Test Case 186 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=187)
    def test_187_tftp_acls_with_true_member_FD(self):
        logging.info("Update operation for tftp_acls fields with acl values 1")
        data = {"tftp_acls": [{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.36.199.8","permission": "DENY"},{"address": "10.37.0.0/16","permission": "ALLOW"},{"address": "10.35.0.0/16","permission": "DENY"},{"address": "Any","permission": "DENY"}]}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_acls", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["tftp_acls"] == [{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.36.199.8","permission": "DENY"},{"address": "10.37.0.0/16","permission": "ALLOW"},{"address": "10.35.0.0/16","permission": "DENY"},{"address": "Any","permission": "DENY"}]
        logging.info("Test Case 187 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=188)
    def test_188_tftp_acls_with_search1_member_FD(self):
        logging.info("Search operation for tftp_acls fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_acls~:=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_acls',response1)
        logging.info("Test Case 188 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=189)
    def test_189_tftp_acls_with_search2_member_FD(self):
        logging.info("Search operation for tftp_acls fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_acls:=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_acls',response1)
        logging.info("Test Case 189 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=190)
    def test_190_tftp_acls_with_search3_member_FD(self):
        logging.info("Search operation for tftp_acls fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_acls=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_acls',response1)
        logging.info("Test Case 190 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=191)
    def test_191_tftp_acls_with_search4_member_FD(self):
        logging.info("Search operation for tftp_acls fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_acls!=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_acls',response1)
        logging.info("Test Case 191 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=192)
    def test_192_tftp_acls_with_search5_member_FD(self):
        logging.info("Search operation for tftp_acls fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_acls<=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_acls',response1)
        logging.info("Test Case 192 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=193)
    def test_193_tftp_acls_with_search6_member_FD(self):
        logging.info("Search operation for tftp_acls fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_acls>=10.36.199.7")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_acls',response1)
        logging.info("Test Case 193 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=194)
    def test_194_tftp_port_member_FD(self):
        logging.info("Get operation for tftp_port fields")
        member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=tftp_port")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        response1 = str(res)
        assert  re.search(r'69',response1)
        logging.info("Test Case 194 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=195)
    def test_195_tftp_port_with_invalid1_grid_FD(self):
        logging.info("Update operation for tftp_port fields with invalid value ")
        data = {"tftp_port": 0.0 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_port", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for tftp_port: 0.0: Must be integer type',response1)
        logging.info("Test Case 195 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=196)
    def test_196_tftp_port_with_invalid2_grid_FD(self):
        logging.info("Update operation for tftp_port fields with invalid value for permission")
        data = {"tftp_port": -1 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_port", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for tftp_port: -1: Invalid value, must be between 0 and 4294967295',response1)
        logging.info("Test Case 196 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=197)
    def test_197_tftp_port_with_invalid3_grid_FD(self):
        logging.info("Update operation for tftp_port fields with invalid value for permission")
        data = {"tftp_port": 4294967295 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_port", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid TFTP port number. It should be an integer from 1 to 63999',response1)
        logging.info("Test Case 197 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=198)
    def test_198_tftp_port_with_invalid4_grid_FD(self):
        logging.info("Update operation for tftp_port fields with invalid value for permission")
        data = {"tftp_port": "a" }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_port", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for tftp_port: .*a.*: Must be integer type',response1)
        logging.info("Test Case 198 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=199)
    def test_199_tftp_port_with_invalid4_grid_FD(self):
        logging.info("Update operation for tftp_port fields with invalid value for permission")
        data = {"tftp_port": 0 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_port", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid TFTP port number. It should be an integer from 1 to 63999',response1)
        logging.info("Test Case 199 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=200)
    def test_200_tftp_port_with_search1_member_FD(self):
        logging.info("Search operation for tftp_port fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_port~:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_port',response1)
        logging.info("Test Case 200 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=201)
    def test_201_tftp_port_with_search2_member_FD(self):
        logging.info("Search operation for tftp_port fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_port:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_port',response1)
        logging.info("Test Case 201 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=202)
    def test_202_tftp_port_with_search3_member_FD(self):
        logging.info("Search operation for tftp_port fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_port=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_port',response1)
        logging.info("Test Case 202 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=203)
    def test_203_tftp_port_with_search4_member_FD(self):
        logging.info("Search operation for tftp_port fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_port!=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_port',response1)
        logging.info("Test Case 203 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=204)
    def test_204_tftp_port_with_search5_member_FD(self):
        logging.info("Search operation for tftp_port fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_port<=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_port',response1)
        logging.info("Test Case 204 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=205)
    def test_205_tftp_port_with_search6_member_FD(self):
        logging.info("Search operation for tftp_port fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_port>=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_port',response1)
        logging.info("Test Case 205 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=206)
    def test_206_tftp_status_member_FD(self):
        logging.info("Get operation for tftp_status fields")
        member_FD = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?_return_fields=tftp_status")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        response1 = str(res)
        assert  re.search(r'INACTIVE',response1)
        logging.info("Test Case 206 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=207)
    def test_207_tftp_status_with_invalid1_grid_FD(self):
        logging.info("Update operation for tftp_status fields with invalid value ")
        data = {"tftp_status": 1 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=tftp_status", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: tftp_status',response1)
        logging.info("Test Case 207 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=208)
    def test_208_tftp_status_with_search1_member_FD(self):
        logging.info("Search operation for tftp_status fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_status~:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_status',response1)
        logging.info("Test Case 208 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=209)
    def test_209_tftp_status_with_search2_member_FD(self):
        logging.info("Search operation for tftp_status fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_status:=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_status',response1)
        logging.info("Test Case 209 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=210)
    def test_210_tftp_status_with_search3_member_FD(self):
        logging.info("Search operation for tftp_status fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_status=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_status',response1)
        logging.info("Test Case 210 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=211)
    def test_211_tftp_status_with_search4_member_FD(self):
        logging.info("Search operation for tftp_status fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_status!=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_status',response1)
        logging.info("Test Case 211 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=212)
    def test_212_tftp_status_with_search5_member_FD(self):
        logging.info("Search operation for tftp_status fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_status<=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_status',response1)
        logging.info("Test Case 212 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=213)
    def test_213_tftp_status_with_search6_member_FD(self):
        logging.info("Search operation for tftp_status fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?tftp_status>=1")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tftp_status',response1)
        logging.info("Test Case 213 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=214)
    def test_214_use_allow_uploads_member_FD(self):
        logging.info("Update operation for use_allow_uploads fields")
        member_FD = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=use_allow_uploads")
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["use_allow_uploads"] == True
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=215)
    def test_215_use_allow_uploads_with_true_member_FD(self):
        logging.info("Update operation for use_allow_uploads fields with False")
        data = {"use_allow_uploads": False}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=use_allow_uploads", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["use_allow_uploads"] == False
        logging.info("Test Case 215 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=216)
    def test_216_use_allow_uploads_with_false_member_FD(self):
        logging.info("Update operation for use_allow_uploads fields with true")
        data = {"use_allow_uploads": True}
        member_FD = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=use_allow_uploads", fields=json.dumps(data))
        logging.info(member_FD)
        res = json.loads(member_FD)
        print res
        assert res["use_allow_uploads"] == True
        logging.info("Test Case 216 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=217)
    def test_217_use_allow_uploads_with_invalid_member_FD(self):
        logging.info("Update operation for use_allow_uploads fields with invalid value")
        data = {"use_allow_uploads": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=use_allow_uploads", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for use_allow_uploads: 1: Must be boolean type',response1)
        logging.info("Test Case 217 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=218)
    def test_218_use_allow_uploads_with_search1_member_FD(self):
        logging.info("Search operation for use_allow_uploads fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?use_allow_uploads~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: use_allow_uploads',response1)
        logging.info("Test Case 218 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=219)
    def test_219_use_allow_uploads_with_search2_member_FD(self):
        logging.info("Search operation for use_allow_uploads fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?use_allow_uploads:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: use_allow_uploads',response1)
        logging.info("Test Case 219 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=220)
    def test_220_use_allow_uploads_with_search3_member_FD(self):
        logging.info("Search operation for use_allow_uploads fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?use_allow_uploads=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: use_allow_uploads',response1)
        logging.info("Test Case 220 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=221)
    def test_221_use_allow_uploads_with_search4_member_FD(self):
        logging.info("Search operation for use_allow_uploads fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?use_allow_uploads!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: use_allow_uploads',response1)
        logging.info("Test Case 221 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=222)
    def test_222_use_allow_uploads_with_search5_member_FD(self):
        logging.info("Search operation for use_allow_uploads fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?use_allow_uploads<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: use_allow_uploads',response1)
        logging.info("Test Case 222 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=223)
    def test_223_use_allow_uploads_with_search6_member_FD(self):
        logging.info("Search operation for use_allow_uploads fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="member:filedistribution", params="?use_allow_uploads>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: use_allow_uploads',response1)
        logging.info("Test Case 223 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=224)
    def test_224_get_member_FD_with_all_fields(self):
        logging.info("Update operation for use_allow_uploads fields")
        response = ib_NIOS.wapi_request('GET', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=allow_uploads,comment,enable_ftp,enable_ftp_filelist,enable_ftp_passive,enable_http,enable_http_acl,enable_tftp,ftp_acls,ftp_port,ftp_status,host_name,http_acls,http_status,ipv4_address,ipv6_address,status,tftp_acls,tftp_port,tftp_status,use_allow_uploads")
        logging.info(response)
        print response
        read  = re.search(r'200',response)
        for read in  response:
                assert True

        logging.info("Test Case 224 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=225)
    def test_225_update_member_FD_with_all_fields(self):
        logging.info("Update operation for all fields")
        data = {"allow_uploads": True,"enable_ftp": True,"enable_ftp_filelist": True,"enable_ftp_passive": True,"enable_http": True,"enable_http_acl": True,"enable_tftp": True,"ftp_acls":[{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.36.199.8","permission": "DENY"},{"address": "10.35.0.0/16","permission": "ALLOW"},{"address": "10.37.0.0/16","permission": "DENY"},{"address": "Any","permission": "ALLOW"}],"ftp_port": 21,"http_acls":[{"address": "10.36.199.7","permission": "ALLOW"},{"address": "10.35.0.0/16","permission": "ALLOW"}],"tftp_acls": [{"address": "10.36.199.8","permission": "ALLOW"},{"address": "10.36.199.7","permission": "DENY"},{"address": "10.37.0.0/16","permission": "ALLOW"},{"address": "10.35.0.0/16","permission": "DENY"},{"address": "Any","permission": "DENY"}],"tftp_port": 69,"use_allow_uploads": True}
        response = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=allow_uploads,comment,enable_ftp,enable_ftp_filelist,enable_ftp_passive,enable_http,enable_http_acl,enable_tftp,ftp_acls,ftp_port,ftp_status,host_name,http_acls,http_status,ipv4_address,ipv6_address,status,tftp_acls,tftp_port,tftp_status,use_allow_uploads", fields=json.dumps(data))
        logging.info(response)
        print response
        read  = re.search(r'200',response)
        for read in  response:
                assert True

        logging.info("Test Case 225 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=226)
    def test_226_default_values_member_FD(self):
        logging.info("Update operation to make the default values for all fields in member FD")
        data = {"allow_uploads": False,"enable_ftp": False,"enable_ftp_filelist": False,  "enable_ftp_passive": True,"enable_http": False,"enable_http_acl": False,"enable_tftp": False,"ftp_acls": [],"ftp_port": 21,"http_acls": [],"tftp_acls": [],"tftp_port": 69,"use_allow_uploads": False}
        response = ib_NIOS.wapi_request('PUT', ref="member:filedistribution/b25lLm1lbWJlcl90ZnRwX3Byb3BlcnRpZXMkMA:infoblox.localdomain", params="?_return_fields=allow_uploads,comment,enable_ftp,enable_ftp_filelist,enable_ftp_passive,enable_http,enable_http_acl,enable_tftp,ftp_acls,ftp_port,ftp_status,host_name,http_acls,http_status,ipv4_address,ipv6_address,status,tftp_acls,tftp_port,tftp_status,use_allow_uploads", fields=json.dumps(data))
        logging.info(response)
        res = json.loads(response)
        print response
        read  = re.search(r'200',response)
        for read in  response:
                assert True

        logging.info("Test Case 226 Execution Completed")
        logging.info("============================")

