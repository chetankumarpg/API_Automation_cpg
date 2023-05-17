import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class Auth_Policy(unittest.TestCase):

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
        def test_create_authpolicy(self):
                logging.info("Create A new authpolicy")
                data = {"admin_groups": "admin-group","auth_services":["localuser:authservice/Li5sb2NhbF91c2VyX2F1dGhfc2VydmljZSRk:Local%20Admin"],"default_group":"cloud-api-only","usage_type": "FULL"}
                status,response = ib_NIOS.wapi_request('POST', object_type="authpolicy", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Operation create not allowed for authpolicy',response)
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=2)
        def test_format_authpolicy(self):
                logging.info("Test the format of authpolicy object")
                response = ib_NIOS.wapi_request('GET', object_type="authpolicy")
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 2 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=3)
        def test_csv_export_authpolicy(self):
                logging.info("Test the restriction for the authentication policy object - CSV Export")
                data = {"_object":"authpolicy"}
                status,response = ib_NIOS.wapi_request('POST', object_type="authpolicy",params="?_function=csv_export",fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Function csv_export is not valid for this object',response)
                logging.info("Test Case 3 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=4)
        def test_schedule_authpolicy(self):
                logging.info("Perform schedule operation for authpolicy")
                status,response = ib_NIOS.wapi_request('POST', object_type="authpolicy",params="?_schedinfo.scheduled_time=1591056000")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Operation create not allowed for authpolicy',response)
                logging.info("Test Case 4 Execution Completed")
                logging.info("============================")

	@pytest.mark.run(order=5)
	def test_globalsearch_authpolicy(self):
        	logging.info("Test the restriction for the authentication policy object - Global search")
        	search_authpolicy = ib_NIOS.wapi_request('GET', object_type="search",params="?search_string=admin-group")
        	logging.info(search_authpolicy)
        	res = json.loads(search_authpolicy)
        	print res
        	for i in res:
        	    logging.info("found")
        	    assert i["name"] == "admin-group"
        	logging.info("Test Case 5 Execution Completed")
        	logging.info("============================")


        @pytest.mark.run(order=6)
        def test_return_fields_authpolicy(self):
                logging.info("Test the _return_fields for default values in authentication policy object")
                response = ib_NIOS.wapi_request('GET', object_type="authpolicy")
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 6 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=7)
	def test_admin_groups_field(self):
        	logging.info("Test the admin_groups field in authpolicy")
        	data = {"admin_groups" :   "admin-group"}
        	admin_groups = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?_return_fields=admin_groups")
        	logging.info(admin_groups)
        	res = json.loads(admin_groups)
        	print res
        	for i in res:
        	        print i
        	        logging.info("found")
        	        assert i["admin_groups"] == []
        	logging.info("Test Case 7 Execution Completed")
        	logging.info("============================")


        @pytest.mark.run(order=8)
        def test_Serach_admin_groups_exact_equality(self):
                logging.info("perform Search with =  for admin_groups field in authpolicy ")
                status,response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?admin_groups=admin_groups")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: admin_groups',response)
                logging.info("Test Case 8 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=9)
        def test_Serach_admin_groups_case_insensitive(self):
                logging.info("perform Search with :=  for admin_groups field in authpolicy ")
                status,response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?admin_groups:=admin_groups")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: admin_groups',response)
                logging.info("Test Case 9 Execution Completed")
                logging.info("=============================")



        @pytest.mark.run(order=10)
        def test_Serach_admin_groups_case_regular_expression(self):
                logging.info("perform Search with ~=  for admin_groups field in authpolicy ")
                status,response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?admin_groups:=admin_groups")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: admin_groups',response)
                logging.info("Test Case 10 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=11)
        def test_default_group_field(self):
                logging.info("Test the default_group field in authpolicy")
                data = {"default_group" : "cloud-api-only"}
                response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?_return_fields=default_group")
		logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True

                logging.info("Test Case 11 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=12)
        def test_Serach_default_group_exact_equality(self):
                logging.info("perform Search with =  for default_group field in authpolicy ")
                response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?default_group=cloud-api-only")
                logging.info(response)
                res = json.loads(response)
                for i in res:
                    print i
                    logging.info("found")
                    assert i["default_group"] == "cloud-api-only" and i["usage_type"] == "FULL"
                logging.info("Test Case 12 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=13)
        def test_Serach_default_group_case_insensitive(self):
                logging.info("perform Search with :=  for default_group field in authpolicy ")
                status,response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?default_group:=Cloud-api-only")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Search modifier \':\' not allowed for field: default_group',response)
                logging.info("Test Case 13 Execution Completed")
                logging.info("=============================")
				
        @pytest.mark.run(order=14)
        def test_Serach_default_group_case_regular_expression(self):
                logging.info("perform Search with ~=  for default_group field in authpolicy ")
                status,response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?default_group~=cloud-api-only")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Search modifier \'~\' not allowed for field: default_group',response)
                logging.info("Test Case 14 Execution Completed")
                logging.info("=============================")



        @pytest.mark.run(order=15)
        def test_usage_type_field(self):
                logging.info("Test the usage_type field in authpolicy")
                data = {"usage_type" : "FULL"}
                usage_type = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?_return_fields=usage_type")
                logging.info(usage_type)
                res = json.loads(usage_type)
                print res
                for i in res:
                        print i
                        logging.info("found")
                        assert i["usage_type"] == "FULL"
                logging.info("Test Case 15 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=16)
        def test_Serach_usage_type_exact_equality(self):
                logging.info("perform Search with =  for usage_type field in authpolicy ")
                response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?usage_type=FULL")
                logging.info(response)
                res = json.loads(response)
                for i in res:
                    print i
                    logging.info("found")
                    assert i["usage_type"] == "FULL" 
                logging.info("Test Case 16 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=17)
        def test_Serach_usage_type_case_insensitive(self):
                logging.info("perform Search with :=  for usage_type field in authpolicy ")
                status,response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?usage_type:=FULL")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Search modifier \':\' not allowed for field: usage_type',response)
                logging.info("Test Case 17 Execution Completed")
                logging.info("=============================")

				
        @pytest.mark.run(order=18)
        def test_Serach_usage_type_regular_expression(self):
                logging.info("perform Search with ~=  for usage_type field in authpolicy ")
                status,response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?usage_type~=FULL")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Search modifier \'~\' not allowed for field: usage_type',response)
                logging.info("Test Case 18 Execution Completed")
                logging.info("=============================")



        @pytest.mark.run(order=19)
        def test_auth_services_field(self):
                logging.info("Test the auth_services field in authpolicy")
                response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?_return_fields=auth_services")
                print response
                logging.info(response)
                assert re.search(r'localuser:authservice/',response)
                logging.info("Test Case 19 Execution Completed")
                logging.info("=============================")


        @pytest.mark.run(order=20)
        def test_Serach_auth_services_exact_equality(self):
                logging.info("perform Search with =  for auth_services field in authpolicy ")
                status,response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?auth_services=localuser:authservice/Li5sb2NhbF91c2VyX2F1dGhfc2VydmljZSQxMQ:Local%20Admin")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: auth_services',response)
                logging.info("Test Case 20 Execution Completed")
                logging.info("=============================")


	@pytest.mark.run(order=21)
        def test_Serach_auth_services_case_insensitive(self):
                logging.info("perform Search with :=  for auth_services field in authpolicy ")
                status,response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?auth_services:=localuser:authservice/Li5sb2NhbF91c2VyX2F1dGhfc2VydmljZSQxMQ:Local%20Admin")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: auth_services',response)
                logging.info("Test Case 21 Execution Completed")
                logging.info("=============================")
				
				

	@pytest.mark.run(order=22)
        def test_Serach_auth_services_regular_expression(self):
                logging.info("perform Search with ~=  for auth_services field in authpolicy ")
                status,response = ib_NIOS.wapi_request('GET',object_type="authpolicy",params="?auth_services~=localuser:authservice/Li5sb2NhbF91c2VyX2F1dGhfc2VydmljZSQxMQ:Local%20Admin")
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not searchable: auth_services',response)
                logging.info("Test Case 22 Execution Completed")
                logging.info("=============================")
	

        @pytest.mark.run(order=23)
        def test_DELETE_authpolicy(self):
		logging.info("perform DELETE operation on authpolicy object")
                get_ref = ib_NIOS.wapi_request('GET', object_type="authpolicy")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Deleting the authpolicy ")
                data ={"default_group": "cloud-api-only","usage_type": "FULL"}
                status,get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
                print status
                print get_status
                logging.info(get_status)
                assert status == 400 and re.search(r'AdmConProtoError: Operation delete not allowed for authpolicy',get_status)
                logging.info("Test Case 23 Execution Completed")
		logging.info("=============================")		


        @pytest.mark.run(order=24)
        #Update usage_type field as AUTH_ONLY
        def test_Update_On_usage_type_AUTH_ONLY(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="authpolicy")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation for usage_type field in authpolicy")
                data ={"usage_type": "AUTH_ONLY"}
                get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print get_status


        @pytest.mark.run(order=25)
        #Update usage_type field as FULL
        def test_Update_On_usage_type_FULL(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="authpolicy")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation for usage_type field in authpolicy")
                data ={"usage_type": "FULL"}
                get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print get_status
				
        @pytest.mark.run(order=26)
        #Update default_group field as admin-group
        def test_Update_On_default_group_admin_group(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="authpolicy")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation for default_group field in authpolicy")
                data ={"default_group": "admin-group"}
                get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print get_status




        @pytest.mark.run(order=27)
        #Update default_group field as cloud_api_only
        def test_Update_On_default_group_cloud_api_only(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="authpolicy")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Update operation for default_group field in authpolicy")
                data ={"default_group": "cloud-api-only"}
                get_status = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
                print get_status



	@classmethod
	def teardown_class(cls):
        	""" teardown any state that was previously setup with a call to
        	setup_class.
        	"""
        	logging.info("TEAR DOWN METHOD")

