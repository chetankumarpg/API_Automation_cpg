import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import os
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
    def test_1_get_ftpuser(self):
        logging.info("Get the ftpuser defaults fields ")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser")
        print status
        print response1
        logging.info(response1)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=2)
    def test_2_csv_ftpuser(self):
        logging.info("CSV export operation for ftpuser")
        data = {"_object":"ftpuser"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 404 and re.search(r'The CSV search did not match any objects',response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=3)
    def test_3_schedule_ftpuser(self):
        logging.info("Perform schedule operation for ftpuser")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="ftpuser",params="?_schedinfo.scheduled_time=1793807868")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"ftpuser does not support scheduling.",response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=4)
    def test_4_ftpuser(self):
        logging.info("Create operation for ftpuser")
        data = {"extattrs": {},"home_dir": "/ftpusers/ftpuser1","permission": "RW","username": "ftpuser1","password":"infoblox"}
        ftpuser = ib_NIOS.wapi_request('POST', object_type="ftpuser", params="?_return_fields=extattrs,home_dir,permission,username", fields=json.dumps(data))
        logging.info(ftpuser)
        res = json.loads(ftpuser)
        print res
        assert res["extattrs"] == {} and res["home_dir"] == "/ftpusers/ftpuser1" and res["permission"] == "RW" and res["username"] == "ftpuser1"
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=5)
    def test_5_get_ftpuser(self):
        logging.info("Get operation the ftpuser with all fields")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="ftpuser",params="?_return_fields=extattrs,home_dir,permission,username")
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["extattrs"] == {} and i["home_dir"] == "/ftpusers/ftpuser1" and i["permission"] == "RW" and i["username"] == "ftpuser1"
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=6)
    def test_6_global_search_ftpuser(self):
        logging.info("Global Search operation for ftpuser1")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="search", params="?search_string=ftpuser1")
        logging.info(get_ftpuser)
        assert re.search(r"ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1",get_ftpuser)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=7)
    def test_7_create_home_dir_ftpuser(self):
        logging.info("Update operation for create_home_dir field")
        status,response1 = ib_NIOS.wapi_request('GET', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=create_home_dir")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not readable: create_home_dir',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=8)
    def test_8_create_home_dir_with_true_ftpuser(self):
        logging.info("Update operation for create_home_dir fields with true")
        data = {"create_home_dir": True}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=create_home_dir", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not readable: create_home_dir',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=9)
    def test_9_create_home_dir_with_false_ftpuser(self):
        logging.info("Update operation for create_home_dir fields with false")
        data = {"create_home_dir": False}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=create_home_dir", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not readable: create_home_dir',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=10)
    def test_10_create_home_dir_with_invalid_ftpuser(self):
        logging.info("Update operation for create_home_dir fields with invalid value")
        data = {"create_home_dir": 1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=create_home_dir", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not readable: create_home_dir',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=11)
    def test_11_create_home_dir_with_search1_ftpuser(self):
        logging.info("Search operation for create_home_dir fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?create_home_dir~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: create_home_dir',response1)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=12)
    def test_12_create_home_dir_with_search2_ftpuser(self):
        logging.info("Search operation for create_home_dir fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?create_home_dir:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: create_home_dir',response1)
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=13)
    def test_13_create_home_dir_with_search3_ftpuser(self):
        logging.info("Search operation for create_home_dir fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?create_home_dir=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: create_home_dir',response1)
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=14)
    def test_14_create_home_dir_with_search4_ftpuser(self):
        logging.info("Search operation for create_home_dir fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?create_home_dir!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: create_home_dir',response1)
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=15)
    def test_15_create_home_dir_with_search5_ftpuser(self):
        logging.info("Search operation for create_home_dir fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?create_home_dir<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: create_home_dir',response1)
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=16)
    def test_16_create_home_dir_with_search6_ftpuser(self):
        logging.info("Search operation for create_home_dir fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?create_home_dir>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: create_home_dir',response1)
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=17)
    def test_17_extattrs_ftpuser(self):
        logging.info("Update operation for extattrs field")
        get_ftpuser = ib_NIOS.wapi_request('GET', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=extattrs")
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        assert res["extattrs"] == {}
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=18)
    def test_18_extattrs_with_true_ftpuser(self):
        logging.info("Update operation for extattrs fields with true")
        data = {"extattrs": {"IB Discovery Owned": {"value": "asf  ssdzghdf  egg2424533454@#@%@$"},"Site": {"value": "asfd@$$$$$$$#@!!13412d"}}}
        get_ftpuser = ib_NIOS.wapi_request('PUT', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=extattrs", fields=json.dumps(data))
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        assert res["extattrs"] == {"IB Discovery Owned": {"value": "asf  ssdzghdf  egg2424533454@#@%@$"},"Site": {"value": "asfd@$$$$$$$#@!!13412d"}}
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=19)
    def test_19_extattrs_with_search1_ftpuser(self):
        logging.info("Search operation for extattrs fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?extattrs~:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: extattrs',response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=20)
    def test_20_extattrs_with_search2_ftpuser(self):
        logging.info("Search operation for extattrs fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?extattrs:=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: extattrs',response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=21)
    def test_21_extattrs_with_search3_ftpuser(self):
        logging.info("Search operation for extattrs fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?extattrs=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: extattrs',response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=22)
    def test_22_extattrs_with_search4_ftpuser(self):
        logging.info("Search operation for extattrs fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?extattrs!=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: extattrs',response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=23)
    def test_23_extattrs_with_search5_ftpuser(self):
        logging.info("Search operation for extattrs fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?extattrs<=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: extattrs',response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=24)
    def test_24_extattrs_with_search6_ftpuser(self):
        logging.info("Search operation for extattrs fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?extattrs>=true")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: extattrs',response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=25)
    def test_25_home_dir_ftpuser(self):
        logging.info("Update operation for home_dir field")
        get_ftpuser = ib_NIOS.wapi_request('GET', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=home_dir")
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        assert res["home_dir"] == "/ftpusers/ftpuser1"
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=26)
    def test_26_home_dir_with_true_ftpuser(self):
        logging.info("Update operation for home_dir fields with true")
        data = {"home_dir": "/NewDirectory"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=home_dir", fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not allowed for update: home_dir",response1)
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=27)
    def test_27_home_dir_with_search1_ftpuser(self):
        logging.info("Search operation for home_dir fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?home_dir~:=NewDirectory")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: home_dir',response1)
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=28)
    def test_28_home_dir_with_search2_ftpuser(self):
        logging.info("Search operation for home_dir fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?home_dir:=NewDirectory")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: home_dir',response1)
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=29)
    def test_29_home_dir_with_search3_ftpuser(self):
        logging.info("Search operation for home_dir fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?home_dir=NewDirectory")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: home_dir',response1)
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=30)
    def test_30_home_dir_with_search4_ftpuser(self):
        logging.info("Search operation for home_dir fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?home_dir!=NewDirectory")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: home_dir',response1)
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=31)
    def test_31_home_dir_with_search5_ftpuser(self):
        logging.info("Search operation for home_dir fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?home_dir<=NewDirectory")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: home_dir',response1)
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=32)
    def test_32_home_dir_with_search6_ftpuser(self):
        logging.info("Search operation for home_dir fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?home_dir>=NewDirectory")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: home_dir',response1)
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=33)
    def test_33_password_ftpuser(self):
        logging.info("Update operation for password field")
        status,response1 = ib_NIOS.wapi_request('GET', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=password")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not readable: password",response1)
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=34)
    def test_34_password_with_true_ftpuser(self):
        logging.info("Update operation for password fields with true")
        data = {"password": "/infoblox"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=password", fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not readable: password",response1)
        logging.info("Test Case 33 Execution Completed")
    @pytest.mark.run(order=35)
    def test_35_password_with_true_ftpuser(self):
        logging.info("Update operation for password fields with true")
        data = {"password": "infobl     ox"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=password", fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not readable: password",response1)
        logging.info("Test Case 33 Execution Completed")
    @pytest.mark.run(order=36)
    def test_36_password_with_search1_ftpuser(self):
        logging.info("Search operation for password fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?password~:=infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: password',response1)
        logging.info("Test Case 36 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=37)
    def test_37_password_with_search2_ftpuser(self):
        logging.info("Search operation for password fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?password:=infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: password',response1)
        logging.info("Test Case 37 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=38)
    def test_38_password_with_search3_ftpuser(self):
        logging.info("Search operation for password fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?password=infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: password',response1)
        logging.info("Test Case 38 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=39)
    def test_39_password_with_search4_ftpuser(self):
        logging.info("Search operation for password fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?password!=infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: password',response1)
        logging.info("Test Case 39 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=40)
    def test_40_password_with_search5_ftpuser(self):
        logging.info("Search operation for password fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?password<=infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: password',response1)
        logging.info("Test Case 40 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=41)
    def test_41_password_with_search6_ftpuser(self):
        logging.info("Search operation for password fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?password>=infoblox")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: password',response1)
        logging.info("Test Case 41 Execution Completed")
        logging.info("============================")








    @pytest.mark.run(order=42)
    def test_42_permission_ftpuser(self):
        logging.info("Get operation for permission field")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?_return_fields=permission")
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["permission"] == "RW"
        logging.info("Test Case 42 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=43)
    def test_43_permission_ftpuser(self):
        logging.info("Update operation for permission field")
        data = {"permission": "RW"}
        get_ftpuser = ib_NIOS.wapi_request('PUT', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=permission",fields=json.dumps(data))
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        assert res["permission"] == "RW"
        logging.info("Test Case 43 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=44)
    def test_44_permission_ftpuser(self):
        logging.info("Update operation for permission field - RO")
        data = {"permission": "RO"}
        get_ftpuser = ib_NIOS.wapi_request('PUT', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=permission",fields=json.dumps(data))
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        assert res["permission"] == "RO"
        logging.info("Test Case 44 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=45)
    def test_45_permission_ftpuser(self):
        logging.info("Update operation for permission field - RO")
        data = {"permission": "ROO"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=permission",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Invalid value for permission (.*ROO.*) valid values are: RO, RW",response1)
        logging.info("Test Case 45 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=46)
    def test_46_permission_with_search1_ftpuser(self):
        logging.info("Search operation for permission fields with ~:= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?permission~:=RW")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: permission',response1)
        logging.info("Test Case 46 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=47)
    def test_47_permission_with_search2_ftpuser(self):
        logging.info("Search operation for permission fields with := modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?permission:=RW")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: permission',response1)
        logging.info("Test Case 47 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=48)
    def test_48_permission_with_search3_ftpuser(self):
        logging.info("Search operation for permission fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?permission=RW")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: permission',response1)
        logging.info("Test Case 48 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=49)
    def test_49_permission_with_search4_ftpuser(self):
        logging.info("Search operation for permission fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?permission!=RW")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: permission',response1)
        logging.info("Test Case 49 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=50)
    def test_50_permission_with_search5_ftpuser(self):
        logging.info("Search operation for permission fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?permission<=RW")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: permission',response1)
        logging.info("Test Case 50 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=51)
    def test_51_permission_with_search6_ftpuser(self):
        logging.info("Search operation for permission fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?permission>=RW")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: permission',response1)
        logging.info("Test Case 51 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=52)
    def test_52_username_ftpuser(self):
        logging.info("Get operation for username field")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?_return_fields=username")
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["username"] == "ftpuser1"
        logging.info("Test Case 52 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=53)
    def test53_username_ftpuser(self):
        logging.info("Update operation for username field")
        data = {"username": "user2"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref="ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1", params="?_return_fields=username",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not allowed for update: username",response1)
        logging.info("Test Case 53 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=54)
    def test_54_username_with_search1_ftpuser(self):
        logging.info("Search operation for username fields with ~:= modifier")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?username~:=user1")
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["username"] == "ftpuser1"
        logging.info("Test Case 54 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=55)
    def test_55_username_with_search1_ftpuser(self):
        logging.info("Search operation for username fields with ~:= modifier")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?username~:=User1")
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["username"] == "ftpuser1"
        logging.info("Test Case 55 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=56)
    def test_56_username_with_search1_ftpuser(self):
        logging.info("Search operation for username fields with ~:= modifier")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?username~:=ser1")
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["username"] == "ftpuser1"
        logging.info("Test Case 56 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=57)
    def test_57_username_with_search1_ftpuser(self):
        logging.info("Search operation for username fields with := modifier")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?username:=user1")
        logging.info(get_ftpuser)
        logging.info("Test Case 57 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=58)
    def test_58_username_with_search1_ftpuser(self):
        logging.info("Search operation for username fields with := modifier")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?username:=User1")
        logging.info(get_ftpuser)
        logging.info("Test Case 58 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=59)
    def test_59_username_with_search1_ftpuser(self):
        logging.info("Search operation for username fields with ~:= modifier")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?username:=ser1")
        logging.info(get_ftpuser)
        logging.info("Test Case 59 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=60)
    def test_60_username_with_search1_ftpuser(self):
        logging.info("Search operation for username fields with = modifier")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?username=ftpuser1")
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        for i in res:
            print i
            logging.info("found")
            assert i["username"] == "ftpuser1"
        logging.info("Test Case 60 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=61)
    def test_61_username_with_search3_ftpuser(self):
        logging.info("Search operation for username fields with = modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?username=%20user")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Invalid value for username: .* user.*: leading or trailing whitespace is not allowed.',response1)
        logging.info("Test Case 61 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=62)
    def test_62_username_with_search4_ftpuser(self):
        logging.info("Search operation for username fields with != modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?username!=user")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '!' not allowed for field: username",response1)
        logging.info("Test Case 49 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=63)
    def test_63_username_with_search5_ftpuser(self):
        logging.info("Search operation for username fields with <= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?username<=user")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '<' not allowed for field: username",response1)
        logging.info("Test Case 63 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=64)
    def test_64_username_with_search6_ftpuser(self):
        logging.info("Search operation for username fields with >= modifier")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="ftpuser", params="?username>=user")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '>' not allowed for field: username",response1)
        logging.info("Test Case 64 Execution Completed")
        logging.info("============================")






    @pytest.mark.run(order=66)
    def test_66_delete_ftpuser(self):
        logging.info("Delete operation the ftpuser")
        get_ftpuser = ib_NIOS.wapi_request('GET', object_type="ftpuser")
        logging.info(get_ftpuser)
        res = json.loads(get_ftpuser)
        print res
        ref1 = res[0]['_ref']
        response1 = ib_NIOS.wapi_request('DELETE', ref=ref1)
        logging.info(response1)
        assert re.search(r"ftpuser/b25lLmZ0cF91c2VyJGZ0cHVzZXIx:ftpuser1",response1)
        logging.info("Test Case 66 Execution Completed")
        logging.info("============================")

