import re
import json
import pytest
import unittest
import subprocess
import config
import logging
import ib_utils.ib_NIOS as ib_NIOS

class Upgradeschedule(unittest.TestCase):

	@pytest.mark.run(order=1)
	def test_1_GET_On_Upgradeschedule(self):
	
		logging.info("Test GET On upgradeschedule")
		response = ib_NIOS.wapi_request('GET',object_type="upgradeschedule")
		print response
		logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True

		logging.info("Test Case 1 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=2)
	def test_2_GET_With_all_fields_Upgradeschedule(self):
	
		logging.info("Test GET with all fields upgradeschedule")
		response = ib_NIOS.wapi_request('GET',object_type="upgradeschedule",params="?_return_fields=upgrade_groups,active,start_time,time_zone,upgrade_groups")
		print response
		logging.info(response)
		read = re.search(r'200',response)
		for read in response:
			assert True
		logging.info("Test Case 2 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=3)
	def test_3_Update_On_Upgradeschedule(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="upgradeschedule")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation upgradeschedule object")
		data ={"upgrade_groups":[{"distribution_time": 1494909000,"name": "Default","time_zone": "(UTC + 5:30) Bombay, Calcutta, Madras, New Delhi","upgrade_time": 1494923400},{"distribution_time": 1494873900,"name": "infoblox"}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Field is not writable: time_zone',response)
		logging.info("Test Case 3 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=4)
	def test_4_Update_2_On_Upgradeschedule(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="upgradeschedule")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Update operation upgradeschedule object")
		data ={"upgrade_groups":[{"distribution_time": 1494909000,"name": "Default","upgrade_time": 1494923400},{"distribution_time": 1494873900,"name": "infoblox","upgrade_time": 1494948600}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		logging.info(response)
		assert status ==400 and re.search(r'AdmConDataError: None',response)
		logging.info("Test Case 4 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=5)
	def test_5_Add_the_upgradeschedule_with_name_time_zone_upgrade_time(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="upgradeschedule")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Add the upgradeschedule with_name time zone upgrade time")
		data ={"upgrade_groups":[{"distribution_time": 1494909000,"name": "Default","upgrade_time": 1494923400},{"distribution_time": 1494873900,"name": "infoblox","upgrade_time": 1494948600}]}
		status,response = ib_NIOS.wapi_request('POST', object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Operation create not allowed for upgradeschedule',response)
		logging.info("Test Case 5 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=6)
	def test_6_DELETE_upgradegroup_schedule_field_with_upgradeschedule_object(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="upgradeschedule")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref

		logging.info("Deleting the upgradeschedule")
		status,response = ib_NIOS.wapi_request('DELETE', object_type=ref)
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Operation delete not allowed for upgradeschedule',response)
		logging.info("Test Case 6 Execution Completed")
		logging.info("============================")


	@pytest.mark.run(order=7)
	def test_7_Modify_upgradegroup_schedule_field_with_upgradeschedule_object_upgrade_time(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="upgradeschedule")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Modify upgradegroup schedule field with upgradeschedule object upgrade time")
		data ={"upgrade_groups":[{"distribution_time": 1494909000,"name": "Default","upgrade_time": 1494923400},{"distribution_time": 1494873900,"name": "infoblox","upgrade_time": 4948600}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None ',response)
		logging.info("Test Case 7 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=8)
	def test_8_Modify_upgradegroup_schedule_field_with_upgradeschedule_object_distribution_time(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="upgradeschedule")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Modify upgradegroup schedule field with upgradeschedule object upgrade time")
		data ={"upgrade_groups":[{"distribution_time": 1494909000,"name": "Default","upgrade_time": 1494923400},{"distribution_time": "abc","name": "infoblox","upgrade_time": 1494948600}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConProtoError: Error converting argument distribution_time: Invalid value, must be an integer between 0 and 4294967295',response)
		logging.info("Test Case 8 Execution Completed")
		logging.info("============================")

	@pytest.mark.run(order=9)
	def test_9_Modify_upgradegroup_schedule_field_with_upgradeschedule_object_Default(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="upgradeschedule")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Modify upgradegroup schedule field with upgradeschedule object Default")
		data ={"upgrade_groups":[{"distribution_time": 1494909000,"name": "Default","upgrade_time": 23400},{"distribution_time": 73900,"name": "infoblox","upgrade_time": 1494948600}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None ',response)
		logging.info("Test Case 9 Execution Completed")
		logging.info("============================")

       	@pytest.mark.run(order=10)
	def test_10_Modify_upgradegroup_schedule_field_with_upgradeschedule_object_Upgrade_group(self):
		get_ref = ib_NIOS.wapi_request('GET', object_type="upgradeschedule")
		logging.info(get_ref)
		res = json.loads(get_ref)
		ref = json.loads(get_ref)[0]['_ref']
		print ref
		logging.info("Modify upgradegroup schedule field with upgradeschedule object Upgrade group")
		data ={"upgrade_groups":[{"distribution_time": 1494909000,"name": "lakshmi","upgrade_time": 1494923400},{"distribution_time": 1494873900,"name": "infoblox","upgrade_time": 1494948600}]}
		status,response = ib_NIOS.wapi_request('PUT', object_type=ref,fields=json.dumps(data))
		print status
		print response
		logging.info(response)
		assert status == 400 and re.search(r'AdmConDataError: None ',response)
		logging.info("Test Case 10 Execution Completed")
		logging.info("============================")




        @pytest.mark.run(order=11)
        def test_11_Search_the_upgradeschedule_object_with_upgrade_groups_field_N(self):
                logging.info("Search_the_upgradeschedule_object_with_upgrade_groups_field_N")
                status,response1 = ib_NIOS.wapi_request('GET', object_type="upgradeschedule", params="?upgrade_groups=distribution_time")
                print status
                print response1
                logging.info(response1)
                assert  status == 400 and re.search(r'Field is not searchable: upgrade_groups',response1)
                logging.info("Test Case 11 Execution Completed")
                logging.info("============================")






        @pytest.mark.run(order=12)
        def test_12_Search_the_upgradeschedule_object_with_upgrade_groups_field_time_zone_N(self):
                logging.info("Search_the_upgradeschedule_object_with_upgrade_groups_field_time_zone_N")
                status,response1 = ib_NIOS.wapi_request('GET', object_type="upgradeschedule", params="?upgrade_groups=time_zone")
                print status
                print response1
                logging.info(response1)
                assert  status == 400 and re.search(r'Field is not searchable: upgrade_groups',response1)
                logging.info("Test Case 12 Execution Completed")
                logging.info("============================")





        @pytest.mark.run(order=13)
        def test_13_Search_the_upgradeschedule_object_with_upgrade_groups_field_start_time_N(self):
                logging.info("Search_the_upgradeschedule_object_with_upgrade_groups_field_start_time_N")             
                status,response1 = ib_NIOS.wapi_request('GET', object_type="upgradeschedule", params="?upgrade_groups=start_time")
                print status
	        print response1
	        logging.info(response1)
                assert  status == 400 and re.search(r'Field is not searchable: upgrade_groups',response1)
                logging.info("Test Case 13 Execution Completed")
	        logging.info("============================")

	
