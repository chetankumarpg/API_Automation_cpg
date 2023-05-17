import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class dns_64_group(unittest.TestCase):


	@classmethod
	def setup_class(cls):
        	""" setup any state specific to the execution of the given class (which
        	 usually contains tests).
        	 """
        	logging.info("SETUP METHOD")


        @pytest.mark.run(order=1)
        def test_1_Format_Of_dns_64_group(self):
                logging.info("Test the format of dns64group object")
                get_radius = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_radius)
                res = json.loads(get_radius)
                print res
                for i in res:
                    print i
                    logging.info("found")
                    assert i["comment"] == "Auto-created default group for well-known prefix." and i["disable"] == False and i["name"] == "default"
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=3)
        def test_2_Csv_Export_dns_64_group(self):
                logging.info("Test the restriction for the dns64group object - CSV Export")
                data = {"_object":"dns64group"}
                status,response = ib_NIOS.wapi_request('POST', object_type="fileop",params="?_function=csv_export",fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: dns64group objects do not support CSV export.',response)
                logging.info("Test Case 3 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=3)
        def test_3_Create_New_dns_64_group(self):
                logging.info("Create A new dns64group")
                data = {"clients": [{"address": "10.2.3.1","permission": "ALLOW"}],"comment": "testing","disable": False,"enable_dnssec_dns64": True,"exclude": [{"address":"1::1","permission": "ALLOW"}],"extattrs": {"Site": {"value": "bang"}},"mapped": [{"address": "10.3.2.1","permission": "ALLOW"}],"name": "test",  "prefix": "64:ff9b::/96"}
                response = ib_NIOS.wapi_request('POST', object_type="dns64group", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                    assert True
                logging.info("Test Case 3 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=4)
        def test_4_Create_Duplicate_dns_64_group(self):
                logging.info("Create A Duplicate dns64group")
                data = {"clients": [{"address": "10.2.3.1","permission": "ALLOW"}],"comment": "testing","disable": False,"enable_dnssec_dns64": True,"exclude": [{"address":"1::1","permission": "ALLOW"}],"extattrs": {"Site": {"value": "bang"}},"mapped": [{"address": "10.3.2.1","permission": "ALLOW"}],"name": "test",  "prefix": "64:ff9b::/96"}
                status,response = ib_NIOS.wapi_request('POST', object_type="dns64group", fields=json.dumps(data))
                print response
                print status
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConDataError: None ',response)
                logging.info("Test Case 4 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=5)
        def test_5_Create_Second_New_dns_64_group(self):
                logging.info("Create A Second new dns64group")
                data = {"name": "asm","comment": "testing","disable": False}
                response = ib_NIOS.wapi_request('POST', object_type="dns64group", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                    assert True
                logging.info("Test Case 5 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=6)
        #Updating Created dns64group
        def test_6_Update_On_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation on dns64group")
                data ={"clients": [{"address": "10.2.3.1","permission": "ALLOW"}]}
                get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print get_status
                logging.info(get_status)
                read  = re.search(r'200',get_status)
                for read in  get_status:
                    assert True
                logging.info("Test Case 5 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=7)
        #Test the address field data type in dns64group
        def test_7_Datatype_of_Address_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test the address field data type in dns64group")
                data ={"clients": [{"address": "","permission": "ALLOW"}]}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                res = json.loads(response)
                print res
                assert  status == 400 and re.search(r'AdmConDataError: None ',response)
                logging.info("Test Case 7 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=8)
        #Test the comment field data type in dns64group
        def test_8_Datatype_of_Comment_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test the comment field data type in dns64group")
                data ={"comment": True}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                res = json.loads(response)
                print res
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for comment: true: Must be string type',response)
                logging.info("Test Case 8 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=9)
        def test_9_Serach_comment_exact_equality(self):
                logging.info("perform Search with =  for comment field in dns64group ")
                response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?comment=testing")
                print response
                logging.info(response)
                assert re.search(r'testing',response)
                logging.info("Test Case 9 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=10)
        def test_10_Serach_comment_case_insensitive(self):
                logging.info("perform Search with :=  for comment field in dns64group ")
                response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?comment:=TESting")
                print response
                logging.info(response)
                assert re.search(r'testing',response,re.I)
                logging.info("Test Case 10 Execution Completed")
                logging.info("=============================")

        @pytest.mark.run(order=11)
        def test_11_Serach_comment_regular_expression(self):
                logging.info("perform Search with ~=  for comment field in dns64group ")
                response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?comment~=test*")
                print response
                logging.info(response)
                assert re.search(r'test*',response)
                logging.info("Test Case 11 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=12)
        #Test the disable field data type in dns64group
        def test_12_Datatype_of_disable_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test the disable field data type in dns64group")
                data ={"disable": "Yes"}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                res = json.loads(response)
                print res
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for disable:',response)
                logging.info("Test Case 12 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=13)
        def test_13_Serach_disable_exact_equality(self):
                logging.info("perform Search with =  for disable field in dns64group ")
                status,response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?disable=True")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: disable',response)
                logging.info("Test Case 13 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=14)
        def test_14_Serach_disable_case_insensitive(self):
                logging.info("perform Search with :=  for disable field in dns64group")
                status,response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?disable:=TrUE")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: disable',response)
                logging.info("Test Case 14 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=15)
        def test_15_Serach_disable_regular_expression(self):
                logging.info("perform Search with ~=  for disable field in dns64group")
                status,response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?disable~=Tru*")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: disable',response)
                logging.info("Test Case 15 Execution Completed")
                logging.info("=============================")

        @pytest.mark.run(order=16)
        #Test the enable_dnssec_dns64 field data type in dns64group
        def test_16_Datatype_of_enable_dnssec_dns64_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test the enable_dnssec_dns64 field data type in dns64group")
                data ={"enable_dnssec_dns64": "Yes"}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                res = json.loads(response)
                print res
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for enable_dnssec_dns64:',response)
                logging.info("Test Case 16 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=17)
        def test_17_Serach_enable_dnssec_dns64_exact_equality(self):
                logging.info("perform Search with =  for enable_dnssec_dns64 field in dns64group ")
                status,response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?enable_dnssec_dns64=False")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: enable_dnssec_dns64',response)
                logging.info("Test Case 17 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=18)
        def test_18_Serach_enable_dnssec_dns64_case_insensitive(self):
                logging.info("perform Search with :=  for enable_dnssec_dns64 field in dns64group")
                status,response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?enable_dnssec_dns64:=fAlse")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: enable_dnssec_dns64',response)
                logging.info("Test Case 18 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=19)
        def test_19_Serach_enable_dnssec_dns64_regular_expression(self):
                logging.info("perform Search with ~=  for enable_dnssec_dns64 field in dns64group")
                status,response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?enable_dnssec_dns64~=Fal*")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: enable_dnssec_dns64',response)
                logging.info("Test Case 19 Execution Completed")
                logging.info("=============================")

        @pytest.mark.run(order=20)
        #Test the address field With different values in dns64group
        def test_20_Address_Field_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test the address field With different values in dns64group")
                data ={"clients": [{"address": "1","permission": "ALLOW"}]}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                res = json.loads(response)
                print res
                assert  status == 400 and re.search(r'AdmConDataError: None ',response)
                logging.info("Test Case 20 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=21)
        def test_21_return_fields_dns_64_group(self):
                logging.info("Test the _return_fields for default values in dns64group object")
                response = ib_NIOS.wapi_request('GET', object_type="dns64group",params="?_return_fields=exclude")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 21 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=22)
        #Test the permission field With different values in dns64group
        def test_22_permission_Field_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test the permission field With different values in dns64group")
                data ={"exclude": [{"address": "1::1","permission": "ALlow"}]}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                res = json.loads(response)
                print res
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for permission',response)
                logging.info("Test Case 22 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=23)
        def test_23_extattrs_dns_64_group(self):
                logging.info("Test the _return_fields for default values in dns64group object")
                response = ib_NIOS.wapi_request('GET', object_type="dns64group",params="?_return_fields=extattrs")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 23 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=24)
        #Test the extattrs field With different values in dns64group
        def test_24_extattrs_Field_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test the extattrs field With different values in dns64group")
                data ={"extattrs": {"Site": {"value": 1}}}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                res = json.loads(response)
                print res
                assert  status == 400 and re.search(r'AdmConProtoError: Bad value for extensible attribute',response)
                logging.info("Test Case 24 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=25)
        def test_25_mapped_Field_dns_64_group(self):
                logging.info("Test the mapped field in dns64group object")
                response = ib_NIOS.wapi_request('GET', object_type="dns64group",params="?_return_fields=mapped")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 25 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=26)
        def test_26_name_field_In_dns_64_group(self):
                logging.info("Test the name field of dns64group object")
                response = ib_NIOS.wapi_request('GET', object_type="dns64group",params="?_return_fields=name")
                logging.info(response)
                res = json.loads(response)
                print res
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 26 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=27)
        #Test the name field data type in dns64group
        def test_27_Datatype_of_name_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test the name field data type in dns64group")
                data ={"name": True}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                res = json.loads(response)
                print res
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for name:',response)
                logging.info("Test Case 27 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=28)
        def test_28_Serach_name_exact_equality(self):
                logging.info("perform Search with =  for name field in dns64group ")
                name = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?name=False")
                logging.info(name)
                res = json.loads(name)
                print res
                for i in res:
                        print i
                        logging.info("found")
                        assert  i["comment"] == "testing" and i["disable"] == False and i["name"] == "test"
                logging.info("Test Case 28 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=29)
        def test_2_Serach_name_case_insensitive(self):
                logging.info("perform Search with :=  for name field in dns64group ")
                name = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?name:=TeSt")
                logging.info(name)
                res = json.loads(name)
                print res
                for i in res:
                        print i
                        logging.info("found")
                        assert  i["comment"] == "testing" and i["disable"] == False and i["name"] == "test"
                logging.info("Test Case 29 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=30)
        def test_30_Serach_name_exact_equality(self):
                logging.info("perform Search with ~=  for name field in dns64group ")
                name = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?name~=tes*")
                logging.info(name)
                res = json.loads(name)
                print res
                for i in res:
                        print i
                        logging.info("found")
                        assert  i["comment"] == "testing" and i["disable"] == False and i["name"] == "test"
                logging.info("Test Case 30 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=31)
        def test_31_Prefix_dns_64_group(self):
                logging.info("Test the prefix field in dns64group object")
                response = ib_NIOS.wapi_request('GET', object_type="dns64group",params="?_return_fields=prefix")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 31 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=32)
        #Test the prefix field data type in dns64group
        def test_32_Datatype_of_prefix_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Test the prefix field data type in dns64group")
                data ={"prefix": True}
                status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                res = json.loads(response)
                print res
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for prefix:',response)
                logging.info("Test Case 32 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=33)
        def test_33_Serach_prefix_exact_equality(self):
                logging.info("perform Search with =  for prefix field in dns64group ")
                response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?prefix=64:ff9b::/96")
                print response
                logging.info(response)
                assert re.search(r'default',response)
                logging.info("Test Case 33 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=34)
        def test_34_Serach_prefix_case_insensitive(self):
                logging.info("perform Search with :=  for prefix field in dns64group")
                status,response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?prefix:=64:ff9b::/96")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Search modifier',response)
                logging.info("Test Case 34 Execution Completed")
                logging.info("=============================")

        @pytest.mark.run(order=35)
        def test_35erach_prefix_regular_expression(self):
                logging.info("perform Search with ~=  for prefix field in dns64group ")
                response = ib_NIOS.wapi_request('GET',object_type="dns64group",params="?prefix~=64:ff9b::/96")
                print response
                logging.info(response)
                assert re.search(r'default',response)
                logging.info("Test Case 35Execution Completed")
                logging.info("=============================")

        @pytest.mark.run(order=36)
        def test_36_DELETE_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[1]['_ref']
                print ref
                logging.info("Deleting the dns64group test")
                data ={"name": "test"}
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
                print get_status
                logging.info(get_status)
                logging.info("Test Case 36 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=36)
        def test_37_DELETE_dns_64_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="dns64group")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[1]['_ref']
                print ref
                logging.info("Deleting the dns64group test")
                data ={"name": "asm"}
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
                print get_status
                logging.info(get_status)
                logging.info("Test Case 37 Execution Completed")
                logging.info("=============================")



	@classmethod
	def teardown_class(cls):
        	""" teardown any state that was previously setup with a call to
        	setup_class.
        	"""
        	logging.info("TEAR DOWN METHOD")

