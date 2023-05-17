import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS
class GridFileDistribution(unittest.TestCase):

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
    def test_1_get_grid_FD(self):
        logging.info("Get the grid File distribution defaults fields ")
        get_grid_fd = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution")
        logging.info(get_grid_fd)
        res = json.loads(get_grid_fd)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["name"] == "Infoblox" and i["global_status"] == "INACTIVE" and i["storage_limit"] == 500 and  i["current_usage"] == 0 and i["allow_uploads"] == False
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=2)
    def test_2_create_grid_FD(self):
        logging.info("Get the grid File distribution defaults fields ")
        data = {"allow_uploads": False,"current_usage": 0,"global_status": "INACTIVE","name": "Infoblox","storage_limit": 500}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="grid:filedistribution",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for grid:filedistribution',response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=3)
    def test_3_delete_grid_FD(self):
        logging.info("Deleting the grid File distribution")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = "grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for grid:filedistribution',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=4)
    def test_4_csvexport_grid_FD(self):
        logging.info("Perform CSV export for grid File distribution")
        data = {"_object":"grid:filedistribution"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'grid:filedistribution objects do not support CSV export.',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=5)
    def test_5_globalsearch_grid_FD(self):
        logging.info("Perform Global search for grid File distribution")
        search_grid_fd = ib_NIOS.wapi_request('GET', object_type="search",params="?search_string=500")
        logging.info(search_grid_fd)
        res = json.loads(search_grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "Infoblox" and i["global_status"] == "INACTIVE" and i["storage_limit"] == 500 and  i["current_usage"] == 0 and i["allow_uploads"] == False
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=6)
    def test_6_schedule_grid_FD(self):
        logging.info("Perform schedule operation for grid File distribution")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="grid:filedistribution",params="?_schedinfo.scheduled_time=1793807868")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for grid:filedistribution',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=7)
    def test_7_approvable_Non_super_user_grid_FD(self):
        logging.info("Perform Non super user access to grid File distribution object")
        grid_fd = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", user="user", password="infoblox")
        logging.info(grid_fd)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=8)
    def test_8_approvable_Super_user_grid_FD(self):
        logging.info("Perform Super user access to grid File distribution object")
        grid_fd = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution",user="user1", password="infoblox")
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        for i in res:
            logging.info("found")
            assert i["name"] == "Infoblox" and i["global_status"] == "INACTIVE" and i["storage_limit"] == 500 and  i["current_usage"] == 0 and i["allow_uploads"] == False
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=9)
    def test_9_approvable_Non_super_user_with_ref_grid_FD(self):
        logging.info("Perform Non super user access to grid File distribution object with reference")
        status,response1 = ib_NIOS.wapi_request('GET', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", user="user", password="infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 404 and re.search(r'Reference grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox not found',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=10)
    def test_10_approvable_Super_user_with_ref_grid_FD(self):
        logging.info("Perform Super user access to grid File distribution object with reference")
        status,response1 = ib_NIOS.wapi_request('GET', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox",user="user1", password="infoblox")
        logging.info(response1)
        res = json.loads(response1)
        print status
        print response1
        logging.info(response1)
        assert  status == 404 and re.search(r'Reference grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox not found',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=11)
    def test_11_allow_uploads_grid_FD(self):
        logging.info("Update operation for allow_uploads fields")
        data = {"allow_uploads": False}
        grid_fd = ib_NIOS.wapi_request('GET', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=allow_uploads", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        assert res["allow_uploads"] == False
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=12)
    def test_12_allow_uploads_with_true_grid_FD(self):
        logging.info("Update operation for allow_uploads fields with true")
        data = {"allow_uploads": True}
        grid_fd = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=allow_uploads", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        assert res["allow_uploads"] == True
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=13)
    def test_13_allow_uploads_with_invalid_grid_FD(self):
        logging.info("Update operation for allow_uploads fields with invalid value")
        data = {"allow_uploads": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=allow_uploads", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for allow_uploads: 1: Must be boolean type',response1)
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=14)
    def test_14_allow_uploads_with_search1_grid_FD(self):
        logging.info("Search operation for allow_uploads fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?allow_uploads~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=15)
    def test_15_allow_uploads_with_search2_grid_FD(self):
        logging.info("Search operation for allow_uploads fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?allow_uploads:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=16)
    def test_16_allow_uploads_with_search3_grid_FD(self):
        logging.info("Search operation for allow_uploads fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?allow_uploads=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=17)
    def test_17_allow_uploads_with_search4_grid_FD(self):
        logging.info("Search operation for allow_uploads fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?allow_uploads!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=18)
    def test_18_allow_uploads_with_search5_grid_FD(self):
        logging.info("Search operation for allow_uploads fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?allow_uploads<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=19)
    def test_19_allow_uploads_with_search6_grid_FD(self):
        logging.info("Search operation for allow_uploads fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?allow_uploads>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: allow_uploads',response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")





    @pytest.mark.run(order=20)
    def test_20_backup_storage_with_true_grid_FD(self):
        logging.info("Update operation for backup_storage fields with true")
        data = {"backup_storage": True}
        grid_fd = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=backup_storage", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        assert res["backup_storage"] == True
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=21)
    def test_21_backup_storage_with_invalid_grid_FD(self):
        logging.info("Update operation for backup_storage fields with invalid value")
        data = {"backup_storage": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=backup_storage", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for backup_storage: 1: Must be boolean type',response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=22)
    def test_22_backup_storage_with_search1_grid_FD(self):
        logging.info("Search operation for backup_storage fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?backup_storage~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: backup_storage',response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=23)
    def test_23_backup_storage_with_search2_grid_FD(self):
        logging.info("Search operation for backup_storage fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?backup_storage:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: backup_storage',response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=24)
    def test_24_backup_storage_with_search3_grid_FD(self):
        logging.info("Search operation for backup_storage fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?backup_storage=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: backup_storage',response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=25)
    def test_25_backup_storage_with_search4_grid_FD(self):
        logging.info("Search operation for backup_storage fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?backup_storage!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: backup_storage',response1)
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=26)
    def test_26_backup_storage_with_search5_grid_FD(self):
        logging.info("Search operation for backup_storage fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?backup_storage<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: backup_storage',response1)
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=27)
    def test_27_backup_storage_with_search6_grid_FD(self):
        logging.info("Search operation for backup_storage fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?backup_storage>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: backup_storage',response1)
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=28)
    def test_28_current_usage_grid_FD(self):
        logging.info("Update operation for current_usage fields")
        grid_fd = ib_NIOS.wapi_request('GET', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=current_usage")
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        assert res["current_usage"] == 0
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=29)
    def test_29_current_usage_with_invalid_grid_FD(self):
        logging.info("Update operation for current_usage fields with invalid value")
        data = {"current_usage": 0}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=current_usage", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: current_usage',response1)
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=30)
    def test_30_current_usage_with_search1_grid_FD(self):
        logging.info("Search operation for current_usage fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?current_usage~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: current_usage',response1)
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=31)
    def test_31_current_usage_with_search2_grid_FD(self):
        logging.info("Search operation for current_usage fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?current_usage:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: current_usage',response1)
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=32)
    def test_32_current_usage_with_search3_grid_FD(self):
        logging.info("Search operation for current_usage fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?current_usage=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: current_usage',response1)
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=33)
    def test_33_current_usage_with_search4_grid_FD(self):
        logging.info("Search operation for current_usage fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?current_usage!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: current_usage',response1)
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=34)
    def test_34_current_usage_with_search5_grid_FD(self):
        logging.info("Search operation for current_usage fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?current_usage<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: current_usage',response1)
        logging.info("Test Case 34 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=35)
    def test_35_current_usage_with_search6_grid_FD(self):
        logging.info("Search operation for current_usage fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?current_usage>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: current_usage',response1)
        logging.info("Test Case 35 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=36)
    def test_36_enable_anonymous_ftp_grid_FD(self):
        logging.info("Update operation for enable_anonymous_ftp fields")
        grid_fd = ib_NIOS.wapi_request('GET', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=enable_anonymous_ftp")
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        assert res["enable_anonymous_ftp"] == False
        logging.info("Test Case 36 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=37)
    def test_37_enable_anonymous_ftp_with_false_grid_FD(self):
        logging.info("Update operation for enable_anonymous_ftp fields with false")
        data = {"enable_anonymous_ftp": False}
        grid_fd = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=enable_anonymous_ftp", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        assert res["enable_anonymous_ftp"] == False
        logging.info("Test Case 37 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=38)
    def test_38_enable_anonymous_ftp_with_true_grid_FD(self):
        logging.info("Update operation for enable_anonymous_ftp fields with true")
        data = {"enable_anonymous_ftp": True}
        grid_fd = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=enable_anonymous_ftp", fields=json.dumps(data))
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        assert res["enable_anonymous_ftp"] == True
        logging.info("Test Case 38 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=39)
    def test_39_enable_anonymous_ftp_with_invalid_grid_FD(self):
        logging.info("Update operation for enable_anonymous_ftp fields with invalid value")
        data = {"enable_anonymous_ftp": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=enable_anonymous_ftp", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for enable_anonymous_ftp: 1: Must be boolean type',response1)
        logging.info("Test Case 40 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=40)
    def test_40_enable_anonymous_ftp_with_search1_grid_FD(self):
        logging.info("Search operation for enable_anonymous_ftp fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?enable_anonymous_ftp~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_anonymous_ftp',response1)
        logging.info("Test Case 40 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=41)
    def test_41_enable_anonymous_ftp_with_search2_grid_FD(self):
        logging.info("Search operation for enable_anonymous_ftp fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?enable_anonymous_ftp:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_anonymous_ftp',response1)
        logging.info("Test Case 41 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=42)
    def test_42_enable_anonymous_ftp_with_search3_grid_FD(self):
        logging.info("Search operation for enable_anonymous_ftp fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?enable_anonymous_ftp=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_anonymous_ftp',response1)
        logging.info("Test Case 42 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=43)
    def test_43_enable_anonymous_ftp_with_search4_grid_FD(self):
        logging.info("Search operation for enable_anonymous_ftp fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?enable_anonymous_ftp!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_anonymous_ftp',response1)
        logging.info("Test Case 43 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=44)
    def test_44_enable_anonymous_ftp_with_search5_grid_FD(self):
        logging.info("Search operation for enable_anonymous_ftp fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?enable_anonymous_ftp<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_anonymous_ftp',response1)
        logging.info("Test Case 44 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=45)
    def test_45_enable_anonymous_ftp_with_search6_grid_FD(self):
        logging.info("Search operation for enable_anonymous_ftp fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?enable_anonymous_ftp>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: enable_anonymous_ftp',response1)
        logging.info("Test Case 45 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=46)
    def test_46_global_status_grid_FD(self):
        logging.info("Update operation for global_status fields")
        grid_fd = ib_NIOS.wapi_request('GET', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=global_status")
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        assert res["global_status"] == "INACTIVE"
        logging.info("Test Case 46 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=47)
    def test_47_global_status_with_invalid_grid_FD(self):
        logging.info("Update operation for global_status fields with invalid value")
        data = {"global_status": 0}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=global_status", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: global_status',response1)
        logging.info("Test Case 47 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=48)
    def test_48_global_status_with_search1_grid_FD(self):
        logging.info("Search operation for global_status fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?global_status~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: global_status',response1)
        logging.info("Test Case 48 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=49)
    def test_49_global_status_with_search2_grid_FD(self):
        logging.info("Search operation for global_status fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?global_status:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: global_status',response1)
        logging.info("Test Case 49 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=50)
    def test_50_global_status_with_search3_grid_FD(self):
        logging.info("Search operation for global_status fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?global_status=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: global_status',response1)
        logging.info("Test Case 50 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=51)
    def test_51_global_status_with_search4_grid_FD(self):
        logging.info("Search operation for global_status fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?global_status!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: global_status',response1)
        logging.info("Test Case 51 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=52)
    def test_52_global_status_with_search5_grid_FD(self):
        logging.info("Search operation for global_status fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?global_status<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: global_status',response1)
        logging.info("Test Case 52 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=53)
    def test_53_global_status_with_search6_grid_FD(self):
        logging.info("Search operation for global_status fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?global_status>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: global_status',response1)
        logging.info("Test Case 53 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=54)
    def test_54_name_grid_FD(self):
        logging.info("Update operation for name fields")
        grid_fd = ib_NIOS.wapi_request('GET', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=name")
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        assert res["name"] == "Infoblox"
        logging.info("Test Case 54 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=55)
    def test_55_name_with_invalid_grid_FD(self):
        logging.info("Update operation for name fields with invalid value")
        data = {"name": 0}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=name", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: name',response1)
        logging.info("Test Case 55 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=56)
    def test_56_name_with_search1_grid_FD(self):
        logging.info("Search operation for name fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?name~:=Infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '~' not allowed for field: name",response1)
        logging.info("Test Case 56 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=57)
    def test_57_name_with_search2_grid_FD(self):
        logging.info("Search operation for name fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?name:=Infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier ':' not allowed for field: name",response1)
        logging.info("Test Case 57 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=58)
    def test_58_name_with_search3_grid_FD(self):
        logging.info("Search operation for name fields with = modifier")
        get_grid_fd = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?name=Infoblox")
        logging.info(get_grid_fd)
        res = json.loads(get_grid_fd)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["name"] == "Infoblox" and i["global_status"] == "INACTIVE" and i["storage_limit"] == 500 and  i["current_usage"] == 0 and i["allow_uploads"] == True
        logging.info("Test Case 58 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=59)
    def test_59_name_with_search4_grid_FD(self):
        logging.info("Search operation for name fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?name!=Infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '!' not allowed for field: name",response1)
        logging.info("Test Case 59 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=60)
    def test_60_name_with_search5_grid_FD(self):
        logging.info("Search operation for name fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?name<=Infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '<' not allowed for field: name",response1)
        logging.info("Test Case 60 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=61)
    def test_61_name_with_search6_grid_FD(self):
        logging.info("Search operation for name fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?name>=Infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '>' not allowed for field: name",response1)
        logging.info("Test Case 61 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=62)
    def test_62_storage_limit_grid_FD(self):
        logging.info("Update operation for storage_limit fields")
        grid_fd = ib_NIOS.wapi_request('GET', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=storage_limit")
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        assert res["storage_limit"] == 500
        logging.info("Test Case 62 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=63)
    def test_63_storage_limit_grid_FD(self):
        logging.info("Update operation for storage_limit fields")
        grid_fd = ib_NIOS.wapi_request('GET', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=storage_limit")
        logging.info(grid_fd)
        res = json.loads(grid_fd)
        print res
        assert res["storage_limit"] == 500
        logging.info("Test Case 63 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=64)
    def test_64_storage_limit_with_invalid_grid_FD(self):
        logging.info("Update operation for storage_limit fields with invalid value")
        data = {"storage_limit": 0}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=storage_limit", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'The current usage exceeds the new storage limit. Current Usage: 0.*MB Limit: 0 MB. Reset the storage limit',response1)
        logging.info("Test Case 64 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=65)
    def test_65_storage_limit_with_outof_range_grid_FD(self):
        logging.info("Update operation for storage_limit fields with out of range value")
        data = {"storage_limit": 111111111}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=storage_limit", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid file distribution storage limit. Storage limit must be an integer from 1 to 10000',response1)
        logging.info("Test Case 65 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=66)
    def test_66_storage_limit_with_maximum_value_grid_FD(self):
        logging.info("Update operation for storage_limit fields with maximum value")
        data = {"storage_limit": 10000}
        get_grid_fd = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox", params="?_return_fields=storage_limit", fields=json.dumps(data))
        logging.info(get_grid_fd)
        res = json.loads(get_grid_fd)
        print res
        for i in res:
            print i
            logging.info("found")
            assert res["storage_limit"] == 10000
        logging.info("Test Case 66 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=67)
    def test_67_storage_limit_with_search1_grid_FD(self):
        logging.info("Search operation for storage_limit fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?storage_limit~:=0")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: storage_limit',response1)
        logging.info("Test Case 67 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=68)
    def test_68_storage_limit_with_search2_grid_FD(self):
        logging.info("Search operation for storage_limit fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?storage_limit:=0")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: storage_limit',response1)
        logging.info("Test Case 68 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=69)
    def test_69_storage_limit_with_search3_grid_FD(self):
        logging.info("Search operation for storage_limit fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?storage_limit=0")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: storage_limit',response1)
        logging.info("Test Case 69 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=70)
    def test_70_storage_limit_with_search4_grid_FD(self):
        logging.info("Search operation for storage_limit fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?storage_limit!=0")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: storage_limit',response1)
        logging.info("Test Case 70 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=71)
    def test_71_storage_limit_with_search5_grid_FD(self):
        logging.info("Search operation for storage_limit fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?storage_limit<=0")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: storage_limit',response1)
        logging.info("Test Case 71 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=72)
    def test_72_storage_limit_with_search6_grid_FD(self):
        logging.info("Search operation for storage_limit fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution", params="?storage_limit>=0")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: storage_limit',response1)
        logging.info("Test Case 72 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=73)
    def test_73_get_all_grid_FD(self):
        logging.info("Get the grid File distribution all the fields ")
        get_grid_fd = ib_NIOS.wapi_request('GET', object_type="grid:filedistribution",params="?_return_fields=allow_uploads,backup_storage,current_usage,enable_anonymous_ftp,global_status,name,storage_limit")
        logging.info(get_grid_fd)
        res = json.loads(get_grid_fd)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["name"] == "Infoblox" and i["global_status"] == "INACTIVE" and i["storage_limit"] == 10000 and  i["current_usage"] == 0 and i["allow_uploads"] == True and i["backup_storage"] == True and i["enable_anonymous_ftp"] == True
        logging.info("Test Case 73 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=74)
    def test_74_get_grid_FD(self):
        logging.info("Get the grid File distribution all the fields ")
        data = {"allow_uploads":False,"backup_storage":False,"enable_anonymous_ftp":False,"storage_limit":500}
        get_grid_fd = ib_NIOS.wapi_request('PUT', ref="grid:filedistribution/b25lLnRmdHBfc3RvcmFnZSQw:Infoblox",params="?_return_fields=allow_uploads,backup_storage,current_usage,enable_anonymous_ftp,global_status,name,storage_limit",fields=json.dumps(data))
        logging.info(get_grid_fd)
        res = json.loads(get_grid_fd)
        print res
        logging.info("found")
        assert res["name"] == "Infoblox" and res["global_status"] == "INACTIVE" and res["storage_limit"] == 500 and  res["current_usage"] == 0 and res["allow_uploads"] == False and res["backup_storage"] == False and res["enable_anonymous_ftp"] == False
        logging.info("Test Case 74 Execution Completed")
        logging.info("============================")


    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")

