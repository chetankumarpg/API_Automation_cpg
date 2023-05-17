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
    def test_1_get_tftpfiledir(self):
        logging.info("Get the tftpfiledir defaults fields ")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=2)
    def test_2_csv_tftpfiledir(self):
        logging.info("CSV export operation for tftpfiledir")
        data = {"_object":"tftpfiledir"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'tftpfiledir objects do not support CSV export.',response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=3)
    def test_3_schedule_tftpfiledir(self):
        logging.info("Perform schedule operation for tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="tftpfiledir",params="?_schedinfo.scheduled_time=1793807868")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"tftpfiledir does not support scheduling.",response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=4)
    def test_4_create_tftpfiledir(self):
        logging.info("Create the tftpfiledir file type")
        data = {"directory": "/","name": "license-backup.csv","type": "FILE"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="tftpfiledir",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'A file can only be created with the upload file operation',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=5)
    def test_5_create_tftpfiledir1(self):
        logging.info("Create the tftpfiledir Directory type -1")
        data = {"directory": "/","name": "Dir1","type": "DIRECTORY"}
        response1 = ib_NIOS.wapi_request('POST', object_type="tftpfiledir",fields=json.dumps(data))
        logging.info(response1)
        assert  re.search(r"tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIx:DIRECTORY/Dir1",response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=6)
    def test_6_create_tftpfiledir2(self):
        logging.info("Create the tftpfiledir Directory type -2")
        data = {"directory": "/","name": "Dir2","type": "DIRECTORY"}
        response1 = ib_NIOS.wapi_request('POST', object_type="tftpfiledir",fields=json.dumps(data))
        logging.info(response1)
        assert  re.search(r"tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIy:DIRECTORY/Dir2",response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=7)
    def test_7_create_tftpfiledir3(self):
        os.system('touch aab.xml')
        filename="aab.xml"
        data = {"filename":filename}
        logging.info("Create the tftpfiledir File type using fileop")
        create_file = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=uploadinit")
        logging.info(create_file)
        res = json.loads(create_file)
        token = json.loads(create_file)['token']
        url = json.loads(create_file)['url']
        print create_file
        print res
        print token
        print url
        os.system('curl -k1 -u admin:infoblox -F name=%s -F filedata=@%s %s'%(filename,filename,url))
        filename="/"+filename
        print filename
        data = {"token": token,"type":"TFTP_FILE","dest_path":filename}
        create_file1 = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=setfiledest")
        logging.info(create_file1)
        print create_file1
        assert re.search(r"",create_file1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=8)
    def test_8_create_tftpfiledir2(self):
        os.system('touch abc.xml')
        filename="abc.xml"
        data = {"filename":filename}
        logging.info("Create the tftpfiledir File1 using fileop")
        create_file = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=uploadinit")
        logging.info(create_file)
        res = json.loads(create_file)
        token = json.loads(create_file)['token']
        url = json.loads(create_file)['url']
        print create_file
        print res
        print token
        print url
        os.system('curl -k1 -u admin:infoblox -F name=%s -F filedata=@%s %s'%(filename,filename,url))
        filename="/"+filename
        print filename
        data = {"token": token,"type":"TFTP_FILE","dest_path":filename}
        create_file1 = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=setfiledest")
        logging.info(create_file1)
        print create_file1
        assert re.search(r"",create_file1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=9)
    def test_9_get_tftpfiledir(self):
        logging.info("Get the tftpfiledir directory1 with defaults fields ")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        i = res[0]
        print i
        assert i["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIx:DIRECTORY/Dir1" and i["directory"] == "/" and i["name"] == "Dir1" and  i["type"] == "DIRECTORY"
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=10)
    def test_10_get_tftpfiledir(self):
        logging.info("Get the tftpfiledir directory2 with defaults fields ")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        i = res[1]
        print i
        assert i["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIy:DIRECTORY/Dir2" and i["directory"] == "/" and i["name"] == "Dir2" and  i["type"] == "DIRECTORY"
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=11)
    def test_11_get_tftpfiledir(self):
        logging.info("Get the tftpfiledir directory1 with defaults fields ")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        i = res[2]
        print i
        assert i["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9hYWIueG1s:FILE/aab.xml" and i["directory"] == "/" and i["name"] == "aab.xml" and  i["type"] == "FILE"
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=12)
    def test_12_get_tftpfiledir(self):
        logging.info("Get the tftpfiledir directory2 with defaults fields ")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        i = res[3]
        print i
        assert i["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9hYmMueG1s:FILE/abc.xml" and i["directory"] == "/" and i["name"] == "abc.xml" and  i["type"] == "FILE"
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=13)
    def test_13_get_tftpfiledir(self):
        logging.info("Get the tftpfiledir directory1 with defaults fields ")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        i = res[0]
        j = res[1]
        k = res[2]
        l = res[3]
        assert i["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIx:DIRECTORY/Dir1" and i["directory"] == "/" and i["name"] == "Dir1" and  i["type"] == "DIRECTORY" and j["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIy:DIRECTORY/Dir2" and j["directory"] == "/" and j["name"] == "Dir2" and  j["type"] == "DIRECTORY" and k["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9hYWIueG1s:FILE/aab.xml" and k["directory"] == "/" and k["name"] == "aab.xml" and  k["type"] == "FILE" and l["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9hYmMueG1s:FILE/abc.xml" and l["directory"] == "/" and l["name"] == "abc.xml" and  l["type"] == "FILE"
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=14)
    def test_14_get_tftpfiledir(self):
        logging.info("Get the tftpfiledir file1 with global search ")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="search",params="?search_string=abc.xml")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        l = res[0]
        assert l["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9hYmMueG1s:FILE/abc.xml" and l["directory"] == "/" and l["name"] == "abc.xml" and  l["type"] == "FILE"
        logging.info("Test Case 14 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=15)
    def test_15_get_tftpfiledir(self):
        logging.info("Get the tftpfiledir directory1 with global search ")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="search",params="?search_string=Dir1")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        i = res[0]
        assert i["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIx:DIRECTORY/Dir1" and i["directory"] == "/" and i["name"] == "Dir1" and  i["type"] == "DIRECTORY"
        logging.info("Test Case 15 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=16)
    def test_16_approvable_Non_super_user_tftpfiledir(self):
        logging.info("Perform Non super user access to tftpfiledir object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir", user="user", password="infoblox")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 16 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=17)
    def test_17_approvable_non_super_user_get_file_tftpfiledir(self):
        logging.info("Get the tftpfiledir directory1 with defaults fields ")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[2]['_ref']
        status,response1 = ib_NIOS.wapi_request('GET', ref=ref1, user="user", password="infoblox")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Error getting reference tftpfiledir/.*:FILE/.*: Cannot read directory: permission denied",response1)
        logging.info("Test Case 17 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=18)
    def test_18_approvable_non_super_user_get_dir_tftpfiledir(self):
        logging.info("Get the tftpfiledir directory1 with defaults fields ")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[1]['_ref']
        status,response1 = ib_NIOS.wapi_request('GET', ref=ref1, user="user", password="infoblox")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Error getting reference tftpfiledir/.*:DIRECTORY/.*: Cannot read directory: permission denied",response1)
        logging.info("Test Case 18 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=19)
    def test_19_approvable_Super_user_tftpfiledir(self):
        logging.info("Perform super user access to tftpfiledir object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir", user="user1", password="infoblox")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=20)
    def test_20_get_directory_field_tftpfiledir(self):
        logging.info("Get the directory field in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?_return_fields=directory,name,type")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=21)
    def test_21_update_directory_field_tftpfiledir(self):
        logging.info("Update the directory field in tftpfiledir-File")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[2]['_ref']
        data = {"directory": "/"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=directory",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not allowed for update: directory",response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=22)
    def test_22_update_directory_field_tftpfiledir(self):
        logging.info("Update the directory field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[1]['_ref']
        data = {"directory": "/"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=directory",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not allowed for update: directory",response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=23)
    def test_23_search_directory_field_tftpfiledir(self):
        logging.info("Search the directory field with '~:=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory~:=/")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 23 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=24)
    def test_24_search_directory_field_tftpfiledir(self):
        logging.info("Search the directory field with ':=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory:=/")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 24 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=25)
    def test_25_search_directory_field_tftpfiledir(self):
        logging.info("Search the directory field with '=' Modifier in tftpfiledir ")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        i = res[0]
        j = res[1]
        k = res[2]
        l = res[3]
        assert i["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIx:DIRECTORY/Dir1" and i["directory"] == "/" and i["name"] == "Dir1" and  i["type"] == "DIRECTORY" and j["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIy:DIRECTORY/Dir2" and j["directory"] == "/" and j["name"] == "Dir2" and  j["type"] == "DIRECTORY" and k["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9hYWIueG1s:FILE/aab.xml" and k["directory"] == "/" and k["name"] == "aab.xml" and  k["type"] == "FILE" and l["_ref"] == "tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9hYmMueG1s:FILE/abc.xml" and l["directory"] == "/" and l["name"] == "abc.xml" and  l["type"] == "FILE"
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=26)
    def test_26_search_directory_field_tftpfiledir(self):
        logging.info("Search the directory field with '~:=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory!=/")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=27)
    def test_27_search_directory_field_tftpfiledir(self):
        logging.info("Search the directory field with '~:=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory<=/")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 27 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=28)
    def test_28_search_directory_field_tftpfiledir(self):
        logging.info("Search the directory field with '~:=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory>=/")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=29)
    def test_29_get_is_synced_to_gm_field_tftpfiledir(self):
        logging.info("Get the is_synced_to_gm field in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?_return_fields=is_synced_to_gm")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=30)
    def test_30_update_is_synced_to_gm_field_tftpfiledir(self):
        logging.info("Update the is_synced_to_gm field in tftpfiledir-File")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[2]['_ref']
        data = {"is_synced_to_gm":False }
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=is_synced_to_gm",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not writable: is_synced_to_gm",response1)
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=31)
    def test_31_update_directory_field_tftpfiledir(self):
        logging.info("Update the directory field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[1]['_ref']
        data = {"is_synced_to_gm":False }
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=is_synced_to_gm",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not writable: is_synced_to_gm",response1)
        logging.info("Test Case 31 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=32)
    def test_32_search_is_synced_to_gm_field_tftpfiledir(self):
        logging.info("Search the is_synced_to_gm field with '~:=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?is_synced_to_gm~:=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 32 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=33)
    def test_33_search_is_synced_to_gm_field_tftpfiledir(self):
        logging.info("Search the is_synced_to_gm field with ':=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?is_synced_to_gm:=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=34)
    def test_34_search_is_synced_to_gm_field_tftpfiledir(self):
        logging.info("Search the is_synced_to_gm field with '=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?is_synced_to_gm=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 34 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=35)
    def test_35_search_is_synced_to_gm_field_tftpfiledir(self):
        logging.info("Search the is_synced_to_gm field with '!=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?is_synced_to_gm!=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 35 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=36)
    def test_36_search_is_synced_to_gm_field_tftpfiledir(self):
        logging.info("Search the is_synced_to_gm field with '<=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?is_synced_to_gm<=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 36 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=37)
    def test_37_search_is_synced_to_gm_field_tftpfiledir(self):
        logging.info("Search the is_synced_to_gm field with '>=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?is_synced_to_gm>=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 37 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=38)
    def test_38_get_last_modify_field_tftpfiledir(self):
        logging.info("Get the last_modify field in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?_return_fields=last_modify")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 38 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=39)
    def test_39_update_last_modify_field_tftpfiledir(self):
        logging.info("Update the last_modify field in tftpfiledir-File")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[2]['_ref']
        data = {"last_modify":1490100057 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=last_modify",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not writable: last_modify",response1)
        logging.info("Test Case 39 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=40)
    def test_40_update_last_modify_field_tftpfiledir(self):
        logging.info("Update the last_modify field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[1]['_ref']
        data = {"last_modify":1490100057 }
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=last_modify",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not writable: last_modify",response1)
        logging.info("Test Case 40 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=41)
    def test_41_search_last_modify_field_tftpfiledir(self):
        logging.info("Search the last_modify field with '~:=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?last_modify~:=1490100057")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 41 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=42)
    def test_42_search_last_modify_field_tftpfiledir(self):
        logging.info("Search the last_modify field with ':=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?last_modify:=1490100057")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 42 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=43)
    def test_43_search_last_modify_field_tftpfiledir(self):
        logging.info("Search the last_modify field with '=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?last_modify=1490100057")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 43 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=44)
    def test_44_search_last_modify_field_tftpfiledir(self):
        logging.info("Search the last_modify field with '!=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?last_modify!=1490100057")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 44 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=45)
    def test_45_search_last_modify_field_tftpfiledir(self):
        logging.info("Search the last_modify field with '<=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?last_modify<=1490100057")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 45 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=46)
    def test_46_search_last_modify_field_tftpfiledir(self):
        logging.info("Search the last_modify field with '>=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?last_modify>=1490100057")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 46 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=47)
    def test_47_get_name_field_tftpfiledir(self):
        logging.info("Get the name field in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?_return_fields=name")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 47 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=48)
    def test_48_update_name_field_tftpfiledir(self):
        logging.info("Update the name field in tftpfiledir-File")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[2]['_ref']
        data = {"name":"file1"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=name",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"File renaming is not supported",response1)
        logging.info("Test Case 48 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=49)
    def test_49_update_name_field_tftpfiledir(self):
        logging.info("Update the directory field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[1]['_ref']
        data = {"name":"NewDirectory1"}
        response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=last_modify",fields=json.dumps(data))
        logging.info(response1)
        print response1
        assert  re.search(r"tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9OZXdEaXJlY3Rvcnkx:DIRECTORY/NewDirectory1",response1)
        logging.info("Test Case 49 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=50)
    def test_50_update_name_field_tftpfiledir(self):
        logging.info("Update the directory field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[1]['_ref']
        data = {"name":"a NewDirectory1"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=name",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"A directory name can only contain alphanumeric characters and dot, dash or underscore characters. A single dot is not allowed",response1)
        logging.info("Test Case 50 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=51)
    def test_51_update_name_field_tftpfiledir(self):
        logging.info("Update the directory field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[1]['_ref']
        data = {"name":"._-NewDirectory1"}
        response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=last_modify",fields=json.dumps(data))
        logging.info(response1)
        print response1
        assert  re.search(r"tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC8uXy1OZXdEaXJlY3Rvcnkx:DIRECTORY/._-NewDirectory1",response1)
        logging.info("Test Case 51 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=52)
    def test_52_update_name_field_tftpfiledir(self):
        logging.info("Update the directory field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
        data = {"name":"Dir2"}
        response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=last_modify",fields=json.dumps(data))
        logging.info(response1)
        print response1
        assert  re.search(r"tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIy:DIRECTORY/Dir2",response1)
        logging.info("Test Case 52 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=53)
    def test_53_search_last_modify_field_tftpfiledir(self):
        logging.info("Search the last_modify field with '~:=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?name~:=1490100057")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 53 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=54)
    def test_54_search_name_field_tftpfiledir(self):
        logging.info("Search the name field with ':=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?name:=Dir1")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 54 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=55)
    def test_55_search_name_field_tftpfiledir(self):
        logging.info("Search the name field with '=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?name=Dir1")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 55 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=56)
    def test_56_search_name_field_tftpfiledir(self):
        logging.info("Search the name field with '!=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?name!=Dir1")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 56 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=57)
    def test_57_search_name_field_tftpfiledir(self):
        logging.info("Search the name field with '<=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?name<=Dir1")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 57 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=58)
    def test_58_search_name_field_tftpfiledir(self):
        logging.info("Search the name field with '>=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?name>=Dir1")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 58 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=59)
    def test_59_get_type_field_tftpfiledir(self):
        logging.info("Get the type field in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?_return_fields=type")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 59 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=60)
    def test_60_update_type_field_tftpfiledir(self):
        logging.info("Update the type field in tftpfiledir-File")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[2]['_ref']
        response1 = ib_NIOS.wapi_request('GET', ref=ref1,params="?_return_fields=type")
        logging.info(response1)
        res = json.loads(response1)
        assert  res["type"] == "FILE"
        logging.info("Test Case 60 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=61)
    def test_61_update_type_field_tftpfiledir(self):
        logging.info("Update the type field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[1]['_ref']
        response1 = ib_NIOS.wapi_request('GET', ref=ref1,params="?_return_fields=type")
        logging.info(response1)
        print response1
        res = json.loads(response1)
        assert  res["type"] == "DIRECTORY"
        logging.info("Test Case 61 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=62)
    def test_62_update_type_field_tftpfiledir(self):
        logging.info("Update the type field in tftpfiledir-File")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[2]['_ref']
        data = {"type":"DIRECTORY"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=type",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not allowed for update: type",response1)
        logging.info("Test Case 62 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=63)
    def test_63_update_type_field_tftpfiledir(self):
        logging.info("Update the type field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[1]['_ref']
        data = {"type":"FILE"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=type",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Field is not allowed for update: type",response1)
        logging.info("Test Case 63 Execution Completed")
        logging.info("============================")





    @pytest.mark.run(order=64)
    def test_64_search_type_field_tftpfiledir(self):
        logging.info("Search the type field with '~:=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?type~:=Directory")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 64 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=65)
    def test_65_search_type_field_tftpfiledir(self):
        logging.info("Search the type field with ':=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?type:=Directory")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 65 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=66)
    def test_66_search_type_field_tftpfiledir(self):
        logging.info("Search the type field with '=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?type=Directory")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 66 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=67)
    def test_67_search_type_field_tftpfiledir(self):
        logging.info("Search the type field with '!=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?type!=Directory")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 67 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=68)
    def test_68_search_type_field_tftpfiledir(self):
        logging.info("Search the type field with '<=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?type<=Directory")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 68 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=69)
    def test_69_search_type_field_tftpfiledir(self):
        logging.info("Search the type field with '>=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?type>=Directory")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 69 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=70)
    def test_70_search_type_field_tftpfiledir(self):
        logging.info("Search the type field with '=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?type=FILE")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 70 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=71)
    def test_71_search_type_field_tftpfiledir(self):
        logging.info("Search the type field with '=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?type=DIRECTORY")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 71 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=72)
    def test_72_get_recursive_field_tftpfiledir(self):
        logging.info("Get the recursive field in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?_return_fields=recursive")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 72 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=73)
    def test_73_update_recursive_field_tftpfiledir(self):
        logging.info("Update the recursive field in tftpfiledir-File")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[2]['_ref']
        data = {"recursive":False}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=recursive",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400
        logging.info("Test Case 73 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=74)
    def test_74_update_recursive_field_tftpfiledir(self):
        logging.info("Update the recursive field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[1]['_ref']
        data = {"recursive":1}
        status,response1 = ib_NIOS.wapi_request('PUT', ref=ref1,params="?_return_fields=recursive",fields=json.dumps(data))
        logging.info(response1)
        print status
        print response1
        assert  status == 400
        logging.info("Test Case 74 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=75)
    def test_75_search_recursive_field_tftpfiledir(self):
        logging.info("Search the recursive field with '~:=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?recursive~:=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 75 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=76)
    def test_76_search_recursive_field_tftpfiledir(self):
        logging.info("Search the recursive field with ':=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?recursive:=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 76 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=77)
    def test_77_search_recursive_field_tftpfiledir(self):
        logging.info("Search the recursive field with '=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?recursive=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 77 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=78)
    def test_78_search_recursive_field_tftpfiledir(self):
        logging.info("Search the recursive field with '!=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?recursive!=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 78 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=79)
    def test_79_search_recursive_field_tftpfiledir(self):
        logging.info("Search the recursive field with '<=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?recursive<=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 79 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=80)
    def test_80_search_recursive_field_tftpfiledir(self):
        logging.info("Search the recursive field with '>=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?recursive>=true")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 80 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=81)
    def test_81_search_recursive_field_tftpfiledir(self):
        logging.info("Search the recursive field with '=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?recursive=false")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 81 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=82)
    def test_82_search_recursive_field_tftpfiledir(self):
        logging.info("Search the recursive field with '=' Modifier in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?recursive=false11")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 82 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=83)
    def test_83_get_all_fields_tftpfiledir(self):
        logging.info("Get the all fields in tftpfiledir")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?_return_fields=directory,is_synced_to_gm,last_modify,name,type,vtftp_dir_members")
        logging.info(response1)
        print status
        print response1
        assert  status == 400 and re.search(r"Required search parameter 'directory' is missing",response1)
        logging.info("Test Case 83 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=84)
    def test_84_update_type_field_tftpfiledir(self):
        logging.info("Delete the type field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
        response1 = ib_NIOS.wapi_request('DELETE', ref=ref1)
        logging.info(response1)
        print response1
        assert  re.search(r"tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIx:DIRECTORY/Dir1",response1)
        logging.info("Test Case 84 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=85)
    def test_85_update_type_field_tftpfiledir(self):
        logging.info("Delete the type field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
        response1 = ib_NIOS.wapi_request('DELETE', ref=ref1)
        logging.info(response1)
        print response1
        assert  re.search(r"tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9EaXIy:DIRECTORY/Dir2",response1)
        logging.info("Test Case 85 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=86)
    def test_86_update_type_field_tftpfiledir(self):
        logging.info("Delete the type field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
        response1 = ib_NIOS.wapi_request('DELETE', ref=ref1)
        logging.info(response1)
        print response1
        assert  re.search(r"tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9hYWIueG1s:FILE/aab.xml",response1)
        logging.info("Test Case 86 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=87)
    def test_87_update_type_field_tftpfiledir(self):
        logging.info("Delete the type field in tftpfiledir -Directory")
        get_tftpfiledir = ib_NIOS.wapi_request('GET', object_type="tftpfiledir",params="?directory=/")
        logging.info(get_tftpfiledir)
        res = json.loads(get_tftpfiledir)
        print res
        ref1 = res[0]['_ref']
        response1 = ib_NIOS.wapi_request('DELETE', ref=ref1)
        logging.info(response1)
        print response1
        assert  re.search(r"tftpfiledir/Li5vbmUuZGlyZWN0b3J5JC9hYmMueG1s:FILE/abc.xml",response1)
        logging.info("Test Case 87 Execution Completed")
        logging.info("============================")

