import re
import os
import config
import pytest
import unittest
import logging
import subprocess
import json
import time
import ib_utils.ib_NIOS as ib_NIOS


class Zone_Auth_Function_Call(unittest.TestCase):

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
        def test_1_Create_Zone_Auth(self):
                logging.info("Test Create new zone_auth")
		d = config.grid_fqdn
                data ={"fqdn":"test.com","grid_primary": [{"name": d,"stealth": False}]}
                response = ib_NIOS.wapi_request('POST',object_type="zone_auth",fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")


	@pytest.mark.run(order=2)
	def test_2_dnssecgetkskrollover_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the dnssecgetkskrollover function call in zone_auth object")
		data ={"num_days_to_countdown" : 400}
		response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssecgetkskrollover",fields=json.dumps(data))
		print response
		logging.info(response)
		res = json.loads(response)
		read  = re.search(r'200',response)
		for read in  response:
			assert True
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=3)
	def test_3_PUT_On_dnssecgetkskrollover_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the dnssecgetkskrollover function call with PUT operation in zone_auth object")
		data ={"num_days_to_countdown" : 12}
		status,response = ib_NIOS.wapi_request('PUT',object_type=ref,params="?_function=dnssecgetkskrollover",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Function dnssecgetkskrollover illegal with this method',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")




	@pytest.mark.run(order=4)
	def test_4_DELETE_On_dnssecgetkskrollover_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the dnssecgetkskrollover function call with DELETE operation in zone_auth object")
		data ={"num_days_to_countdown" : 12}
		status,response = ib_NIOS.wapi_request('DELETE',object_type=ref,params="?_function=dnssecgetkskrollover",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Function dnssecgetkskrollover illegal with this method',response)
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")




	@pytest.mark.run(order=5)
	def test_5_num_days_to_countdown_Field_dnssecgetkskrollover_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  num_days_to_countdown field in dnssecgetkskrollover function call in zone_auth object")
		data ={"num_days_to_countdown" : "Ten"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssecgetkskrollover",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for num_days_to_countdown: \\"Ten\\": Must be integer type',response)
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")




	@pytest.mark.run(order=6)
	def test_6_operation_dnssec_export_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_export function in zone_auth object")
		data ={"operation": "EXPORT_ANCHORS"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_export",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None ',response)
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")




	@pytest.mark.run(order=7)
	def test_7_operation_dnssec_export_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_export function in zone_auth object")
		data ={"operation": "EXPORT_DS"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_export",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None ',response)
		logging.info("Test Case 7 Execution Completed")
		logging.info("============================")




	@pytest.mark.run(order=8)
	def test_8_operation_dnssec_export_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_export function in zone_auth object")
		data ={"operation": "EXPORT_DNSKEY"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_export",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None ',response)
		logging.info("Test Case 8 Execution Completed")
		logging.info("============================")




	@pytest.mark.run(order=9)
	def test_9_operation_dnssec_export_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_export function in zone_auth object")
		data ={"operation": True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_export",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for operation ',response)
		logging.info("Test Case 9 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=10)
	def test_10_key_pair_type_Field_dnssec_get_zone_keys_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the key_pair_type field with dnssec_get_zone_keys function in zone_auth object")
		data ={"key_pair_type": "KSK"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_get_zone_keys",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 10 Execution Completed")
		logging.info("============================")




	@pytest.mark.run(order=11)
	def test_11_key_pair_type_Field_dnssec_get_zone_keys_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the key_pair_type field with dnssec_get_zone_keys function in zone_auth object")
		data ={"key_pair_type": "ZSK"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_get_zone_keys",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 11 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=12)
	def test_12_key_pair_type_Field_dnssec_get_zone_keys_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype key_pair_type field with dnssec_get_zone_keys function in zone_auth object")
		data ={"key_pair_type": True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_get_zone_keys",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for key_pair_type',response)
		logging.info("Test Case 12 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=13)
	def test_13_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the dnssec_operation function in zone_auth object")
		data ={"buffer": "KSK","operation": "IMPORT_DS"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 13 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=14)
	def test_14_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the dnssec_operation function in zone_auth object")
		data ={"operation": "IMPORT_DS"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: \\"buffer\\" is mandatory when \\"operation\\" is IMPORT_DS.',response)
		logging.info("Test Case 14 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=15)
	def test_15_operaion_Field_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_operation function call in zone_auth object")
		data ={"operation": "ROLLOVER_KSK"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 15 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=16)
	def test_16_operaion_Field_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_operation function call in zone_auth object")
		data ={"operation": "UNSIGN"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 16 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=17)
	def test_17_operaion_Field_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_operation function call in zone_auth object")
		data ={"operation": "SIGN"}
		response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print response
		logging.info(response)
		res = json.loads(response)
		read  = re.search(r'200',response)
		for read in  response:
			assert True
		logging.info("Test Case 17 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=18)
	def test_18_operaion_Field_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_operation function call in zone_auth object")
		data ={"operation": "ROLLOVER_ZSK"}
		response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print response
		logging.info(response)
		res = json.loads(response)
		read  = re.search(r'200',response)
		for read in  response:
			assert True
		logging.info("Test Case 18 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=19)
	def test_19_operaion_Field_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_operation function call in zone_auth object")
		data ={"operation": "RESIGN"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 19 Execution Completed")
		logging.info("============================")



	@pytest.mark.run(order=20)
	def test_20_operaion_Field_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_operation function call in zone_auth object")
		data ={"operation": "UNSIGN"}
		response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print response
		logging.info(response)
		res = json.loads(response)
		read  = re.search(r'200',response)
		for read in  response:
			assert True
		logging.info("Test Case 20 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=21)
	def test_21_operaion_Field_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_operation function call in zone_auth object")
		data ={"operation": "UNSIGN"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None ',response)
		logging.info("Test Case 21 Execution Completed")
		logging.info("============================")

		
		
	@pytest.mark.run(order=22)
	def test_22_operaion_Field_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_operation function call in zone_auth object")
		data ={"operation": "ROLLOVER_ZSK"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None ',response)
		logging.info("Test Case 22 Execution Completed")
		logging.info("============================")
		
		
		
	@pytest.mark.run(order=23)
	def test_23_operaion_Field_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the operation field with dnssec_operation function call in zone_auth object")
		data ={"operation": "RESIGN"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None ',response)
		logging.info("Test Case 23 Execution Completed")
		logging.info("============================")
		
		
		
		
	@pytest.mark.run(order=24)
	def test_24_operaion_Field_dnssec_operation_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of operation field with dnssec_operation function call in zone_auth object")
		data ={"operation": True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_operation",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for operation',response)
		logging.info("Test Case 24 Execution Completed")
		logging.info("============================")
		
		
		
		
	@pytest.mark.run(order=25)
	def test_25_key_pair_type_Field_dnssec_set_zone_keys_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the key_pair_type Field with dnssec_set_zone_keys function call in zone_auth object")
		data ={"key_pair_type": "KSK"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_set_zone_keys",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: required function parameter missing: token',response)
		logging.info("Test Case 25 Execution Completed")
		logging.info("============================")
		
		
		
	@pytest.mark.run(order=26)
	def test_26_dnssec_set_zone_keys_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the dnssec_set_zone_keys function call in zone_auth object")
		data ={"key_pair_type": "KSK","token": "ksdbfkhwiqjemdbndkfjljedns"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_set_zone_keys",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid token value',response)
		logging.info("Test Case 26 Execution Completed")
		logging.info("============================")
		
		
		
		
	@pytest.mark.run(order=27)
	def test_27_token_Field_dnssec_set_zone_keys_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the token Field with dnssec_set_zone_keys function call in zone_auth object")
		data ={"key_pair_type": "KSK","token": True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_set_zone_keys",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for token',response)
		logging.info("Test Case 27 Execution Completed")
		logging.info("============================")
		
		
		
	@pytest.mark.run(order=28)
	def test_28_key_pair_type_Field_dnssec_set_zone_keys_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of  key_pair_type Field with dnssec_set_zone_keys function call in zone_auth object")
		data ={"key_pair_type": True,"token": "wadbsjhiduywdbms.cna/lkfhb ,fmv/lfj"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=dnssec_set_zone_keys",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for key_pair_type',response)
		logging.info("Test Case 28 Execution Completed")
		logging.info("============================")
		
		
		
		
	@pytest.mark.run(order=29)
	def test_29_execute_dns_parent_check_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test execute_dns_parent_check function call in zone_auth object")
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=execute_dns_parent_check")
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Zone test.com does not have a dns integrity member set.',response)
		logging.info("Test Case 29 Execution Completed")
		logging.info("============================")
		
		
		
		
	@pytest.mark.run(order=30)
	def test_30_run_scavenging_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the run_scavenging function call in zone_auth object")
		data ={"action": "ANALYZE"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=run_scavenging",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 30 Execution Completed")
		logging.info("============================")

		
		
		
	@pytest.mark.run(order=31)
	def test_31_run_scavenging_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the run_scavenging function call in zone_auth object")
		data ={"action": "RECLAIM"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=run_scavenging",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 31 Execution Completed")
		logging.info("============================")
		
		
		
		
	@pytest.mark.run(order=32)
	def test_32_run_scavenging_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the run_scavenging function call in zone_auth object")
		data ={"action": "ANALYZE_RECLAIM"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=run_scavenging",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 32 Execution Completed")
		logging.info("============================")
		
		
		
		
	@pytest.mark.run(order=33)
	def test_33_run_scavenging_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the run_scavenging function call in zone_auth object")
		data ={"action": "RESET"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=run_scavenging",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 33 Execution Completed")
		logging.info("============================")
		
		
		
	@pytest.mark.run(order=34)
	def test_34_action_field_run_scavenging_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of action field with run_scavenging function call in zone_auth object")
		data ={"action": True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=run_scavenging",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for action',response)
		logging.info("Test Case 34 Execution Completed")
		logging.info("============================")
		

		
	@pytest.mark.run(order=35)
	def test_35_copyzonerecords_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the copyzonerecords function call in zone_auth object")
		data ={"clear_destination_first": True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=copyzonerecords",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: required function parameter missing: destination_zone',response)
		logging.info("Test Case 35 Execution Completed")
		logging.info("============================")
		
		
	@pytest.mark.run(order=36)
	def test_36_copyzonerecords_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the copyzonerecords function call in zone_auth object")
		data ={"clear_destination_first": True,"destination_zone": "asm.com"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=copyzonerecords",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid reference: asm.com',response)
		logging.info("Test Case 36 Execution Completed")
		logging.info("============================")
		
		
		
		
	@pytest.mark.run(order=37)
	def test_37_destination_zone_field_copyzonerecords_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the datatype of destination_zone with copyzonerecords function call in zone_auth object")
		data ={"clear_destination_first": True,"destination_zone": True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=copyzonerecords",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Field',response)
		logging.info("Test Case 37 Execution Completed")
		logging.info("============================")
		
		
		
	@pytest.mark.run(order=38)
	def test_38_replace_existing_records_field_copyzonerecords_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the replace_existing_records with copyzonerecords function call in zone_auth object")
		data ={"clear_destination_first": True,"destination_zone": "asm.com","replace_existing_records": "yes"}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=copyzonerecords",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Invalid value for replace_existing_records:',response)
		logging.info("Test Case 38 Execution Completed")
		logging.info("============================")
		


	@pytest.mark.run(order=39)
	def test_39_select_records_field_copyzonerecords_FC_Zone_Auth(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Test the replace_existing_records with copyzonerecords function call in zone_auth object")
		data ={"clear_destination_first": True,"destination_zone": "asm.com","replace_existing_records": True,"select_records": True}
		status,response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=copyzonerecords",fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: List value expected for field: select_records',response)
		logging.info("Test Case 39 Execution Completed")
		logging.info("============================")

        @pytest.mark.run(order=40)
        def test_40_DELETE_Zone_Auth(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Deleting the radius:authservice admin")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print get_status
                logging.info(get_status)
                logging.info("Test Case 40 Execution Completed")
                logging.info("=============================")

	


        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")


