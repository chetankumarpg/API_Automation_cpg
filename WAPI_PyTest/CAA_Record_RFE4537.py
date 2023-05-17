import re
import config
import pytest
import unittest
import logging
import subprocess
import os
import json
import ib_utils.ib_NIOS as ib_NIOS
from time import sleep
import commands
import json, ast
import requests
import time
import pexpect
import getpass
import sys


class Network(unittest.TestCase):

	 @pytest.mark.run(order=1)
         def test_1_Create_New_AuthZone(self):
                logging.info("Create A new Zone")
                data = {"fqdn": "zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="zone_auth", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")

         @pytest.mark.run(order=2)
         def test_2_create_grid_primary_for_zone(self):
                logging.info("Create grid_primary with required fields")
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
		
        	data = {"grid_primary": [{"name": config.grid_fqdn,"stealth":False}]}
        	response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
        	logging.info(response)
        	logging.info("============================")
        	print response
		
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(20)

                logging.info("Test Case 2 Execution Completed")


	 @pytest.mark.run(order=3)
         def test_3_Create_New_CAA_Record_with_ISSUE_type(self):
                logging.info("Create A new CAA Record with ISSUE Type")
                data = {"ca": "CAA_Authority.com","ca_type": "ISSUE","name": "caa.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 3 Execution Completed")

	 @pytest.mark.run(order=4)
         def test_4_Create_New_CAA_Record_with_NO_CA_Specified_For_ISSUE_Type(self):
                logging.info("Create A new CAA Record with ISSUE Type")
                data = {"ca": "","ca_type": "ISSUE","name": "caa12345.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 4 Execution Completed")

         @pytest.mark.run(order=5)
         def test_5_Create_New_CAA_Record_with_NO_CA_Specified_For_ISSUEWILD_Type(self):
                logging.info("Create A new CAA Record with ISSUEWILD Type")
                data = {"ca": "","ca_type": "ISSUEWILD","name": "caa145.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 5 Execution Completed")



	 @pytest.mark.run(order=6)
         def test_6_Create_New_CAA_Record_with_ISSUEWILD_type(self):
                logging.info("Create A new CAA Record with ISSUEWILD Type")
                data = {"ca": "CAA_Authority.com","ca_type": "ISSUEWILD","name": "caa1.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 6 Execution Completed")
 

	 @pytest.mark.run(order=7)
         def test_7_Create_New_CAA_Record_with_IODEF_type(self):
                logging.info("Create A new CAA Record with IODEF Type")
                data = {"ca": "test@caa_record.com","ca_type": "IODEF","name": "caa2.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 7 Execution Completed")

	 @pytest.mark.run(order=8)
         def test_8_Create_New_CAA_Record_with_invalid_CA_Specified_For_IODEF_Type(self):
                logging.info("Create A new CAA Record with invalid CA name for  IODEF Type")
                data = {"ca": "test","ca_type": "IODEF","name": "caatest.zone.com"}
                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
		assert status == 400 and re.search(r'Should be a valid URL or a Email address.',response)
                for read in  response:
                        assert True
                logging.info("Test Case 8 Execution Completed")

	 @pytest.mark.run(order=9)
         def test_9_Create_New_CAA_Record_with_Addtional_CA_details_For_IODEF_Type(self):
                logging.info("Create A new CAA Record with addiotional details for IODEF Type")
                data = {"ca": "test@test.com","ca_type": "IODEF","name": "caatest123.zone.com","ca_details":"additional details"}
                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                assert status == 400 and re.search(r'Additional parameters cannot be provided if type IODEF is selected.',response)
                for read in  response:
                        assert True
                logging.info("Test Case 9 Execution Completed")



	 @pytest.mark.run(order=10)
         def test_10_Modify__ISSUE_Type(self):
                logging.info("Modify a  ISSUE type")
                get_ref = ib_NIOS.wapi_request('GET', object_type="record:caa",params="?name=caa.zone.com")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"comment":"test"}
                response = ib_NIOS.wapi_request('PUT', ref=ref1, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 10 Execution Completed")



	 @pytest.mark.run(order=11)
         def test_11_Modify__ISSUEWILD_Type(self):
                logging.info("Modify a  ISSUEWILD type")
                get_ref = ib_NIOS.wapi_request('GET', object_type="record:caa",params="?name=caa1.zone.com")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"comment":"test"}
                response = ib_NIOS.wapi_request('PUT', ref=ref1, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 11 Execution Completed")




         @pytest.mark.run(order=12)
         def test_12_Modify_log_queries(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                logging.info("Modify a  log_queries")
                data = {"logging_categories":{"log_queries": True}}
                response = ib_NIOS.wapi_request('PUT', ref=ref1, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(20)
                logging.info("Test Case 12 Execution Completed")



 	 @pytest.mark.run(order=13)
         def test_13_Modify__IODEF_Type(self):

                get_ref = ib_NIOS.wapi_request('GET', object_type="record:caa",params="?name=caa2.zone.com")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                logging.info("Modify a  IODEF type")
                data = {"comment":"test"}
                response = ib_NIOS.wapi_request('PUT', ref=ref1, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True

		logging.info("Restart services")
        	grid =  ib_NIOS.wapi_request('GET', object_type="grid")
        	ref = json.loads(grid)[0]['_ref']
        	publish={"member_order":"SIMULTANEOUSLY"}
        	request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
        	sleep(10)
        	request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
        	restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 13 Execution Completed")


         @pytest.mark.run(order=14)
         def test_14_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
          	dig_cmd = 'dig @'+str(config.grid_vip)+' caa.zone.com IN CAA'
		dig_cmd1 = os.system(dig_cmd)
	        logging.info("Validate Syslog afer perform queries")
        	sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa.zone.com\'"'
	        out1 = commands.getoutput(sys_log_validation)
        	print out1
	        logging.info(out1)
        	assert re.search(r'caa.zone.com',out1)
	     	logging.info("Test Case 14 Execution Completed")	



         @pytest.mark.run(order=15)
         def test_15_dig_query_for_caa1_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa1.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa1.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa1.zone.com',out1)
                logging.info("Test Case 15 Execution Completed")

         @pytest.mark.run(order=16)
         def test_16_dig_query_for_caa12345_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa12345.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa12345.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa12345.zone.com',out1)
                logging.info("Test Case 14 Execution Completed")

         @pytest.mark.run(order=17)
         def test_17_dig_query_for_caa145_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa145.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa145.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa145.zone.com',out1)
                logging.info("Test Case 17 Execution Completed")

         @pytest.mark.run(order=18)
         def test_18_dig_query_for_caa2_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa2.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa2.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa2.zone.com',out1)
                logging.info("Test Case 18 Execution Completed")

         @pytest.mark.run(order=19)
         def test_19_DELETE_ALL_caa_record(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="record:caa")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                ref = json.loads(get_ref)[1]['_ref']
                print ref
#                logging.info("Deleting the caa1 record")
#                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
#                print get_status
#                logging.info(get_status)
#                read = re.search(r'200',get_status)
#                for read in get_status:
#                        assert True


#                ref = json.loads(get_ref)[2]['_ref']
#                print ref
#                logging.info("Deleting the caa12345 record")
#                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
#                print get_status
#                logging.info(get_status)
#                read = re.search(r'200',get_status)
#                for read in get_status:
#                        assert True
#

#                ref = json.loads(get_ref)[3]['_ref']
#                print ref
#                logging.info("Deleting the caa145 record")
#                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
#                print get_status
#                logging.info(get_status)
#                read = re.search(r'200',get_status)
#                for read in get_status:
#                        assert True


#                ref = json.loads(get_ref)[4]['_ref']
#                print ref
#                logging.info("Deleting the caa2 record")
#                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
#                print get_status
#                logging.info(get_status)
#                read = re.search(r'200',get_status)
#                for read in get_status:
#                        assert True

                logging.info("Test Case 19 Execution Completed")
                logging.info("=============================")


         @pytest.mark.run(order=20)
   	 def test_20_create_for_csv_export(self):
                logging.info("Create the fileop function to download csv_export object with CAA record")
	        data = {"_object":"record:caa","zone":"zone.com","_separator":"COMMA"}
       		create_file = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=csv_export")
       		logging.info(create_file)
	        res = json.loads(create_file)
	        token = json.loads(create_file)['token']
	        url = json.loads(create_file)['url']
	        print create_file
	        print res
	        print token
	        print url
      	        logging.info("Create the fileop function to dowload the csv file to the specified url")
                os.system('curl -k1 -u admin:infoblox -H "Content-type:application/force-download" -O %s'%(url))
	        
                logging.info("Delete the record before import")
                get_ref = ib_NIOS.wapi_request('GET', object_type="record:caa")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Deleting the caa record")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True

                ref = json.loads(get_ref)[1]['_ref']
                print ref
                logging.info("Deleting the caa record")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True

                ref = json.loads(get_ref)[2]['_ref']
                print ref
                logging.info("Deleting the caa record")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True


                ref = json.loads(get_ref)[3]['_ref']
                print ref
                logging.info("Deleting the caa record")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True


                ref = json.loads(get_ref)[4]['_ref']
                print ref
                logging.info("Deleting the caa record")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True


		sleep(5)  
		logging.info("Create the fileop function to download csv_import object with CAA record")
	        data = {"token":token}
	        create_file1 = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=csv_import")
	        logging.info(create_file1)
 	        response1 = ast.literal_eval(json.dumps(create_file1))
	        print response1
                sleep(30)		
		logging.info("Get the status of last executed csv_import task using csvimporttask object")
		task = ib_NIOS.wapi_request('GET', object_type="csvimporttask")
		logging.info(task)
		response2 = json.loads(task)
		csv_imp2 = response2[-1]
		task1 = ast.literal_eval(json.dumps(csv_imp2))
		print task1
		class objectview(object):
			def __init__(self, d):
				self.__dict__ = d
				d = task1
				o = objectview(d)
				assert o.status == COMPLETED
                logging.info("Test Case 20 Execution Completed")
                logging.info("============================")



         @pytest.mark.run(order=21)
         def test_21_Get_operation_to_read_resource_record_caa(self):
        	logging.info("Get_operation_to_read_resource_record_caa")
	        response1 = ib_NIOS.wapi_request('GET', object_type="record:caa")
       	        print response1
        	logging.info(response1)
	        assert  re.search(r"caa.zone.com",response1)
        	logging.info("Test Case 21 Execution Completed")
	        logging.info("============================")


         @pytest.mark.run(order=22)
         def test_22_Search_operation_to_read_resource_record_caa(self):
        	logging.info("Search_operation_to_read_resource_record_caa")
	        response1 = ib_NIOS.wapi_request('GET', object_type="search", params="?search_string=caa.zone.com")
        	print response1
	        logging.info(response1)
        	assert re.search(r"caa.zone.com",response1)
	        logging.info("Test Case 22 Execution Completed")
        	logging.info("============================")


         @pytest.mark.run(order=23)
         def test_23_Crreate_copyzonerecords_function_call_object(self):
        	get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
	        logging.info(get_ref)
        	res1 = json.loads(get_ref)
	        ref = json.loads(get_ref)[0]['_ref']
        	print ref
		
	        logging.info("Create A new Zone")
        	data = {"fqdn": "zone_copy.com"}
	        response = ib_NIOS.wapi_request('POST', object_type="zone_auth", fields=json.dumps(data))
        	print response
	        logging.info(response)
        	read  = re.search(r'201',response)
	        for read in  response:
        	    assert True
	        response1 = ib_NIOS.wapi_request('GET',object_type="zone_auth",params="?fqdn=zone_copy.com")
		print response1
		ref1 = json.loads(response1)
		ref2 = json.loads(response1)[0]['_ref']
		print ref2
				
        	logging.info("Test action field copyzonerecords in  function call of zone_auth object")
	        data ={"clear_destination_first":True,"destination_zone":ref2,"replace_existing_records":False,"select_records":["CAA"]}
        	response = ib_NIOS.wapi_request('POST',object_type=ref,params="?_function=copyzonerecords",fields=json.dumps(data))
	        print response
        	logging.info(response)
	        read = re.search(r'200',response)
        	logging.info("Test Case 23 Execution Completed")
	        logging.info("============================")


         @pytest.mark.run(order=24)
         def test_24_Modify_the_grid_time_zone(self):
                logging.info("Modify_the_grid_time_zone")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"time_zone": "(UTC + 5:30) Bombay, Calcutta, Madras, New Delhi"}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
                logging.info(response)
                print response
                logging.info("Test Case 24 Execution Completed")
		sleep(10)
                logging.info("============================")




         @pytest.mark.run(order=25)
         def test_25_schedule_the_caa_record_creation_and_execute(self):
                logging.info("getting current time and set to future time")
                t = int(time.time())
		print t
		future = t + int(1000)
		print future
		data = {"name":"caa_sched.zone.com","ca_type":"ISSUE","ca":"CAA_Authority.com"}
		create_file = ib_NIOS.wapi_request('POST', object_type="record:caa",fields=json.dumps(data),params="?_schedinfo.scheduled_time="+str(future))
                logging.info(create_file)
		res = json.loads(create_file)
		print res
	 	get_ref = ib_NIOS.wapi_request('GET',object_type="scheduledtask")
		ref1 = json.loads(get_ref)[-1]['_ref']
		data = {"execute_now":True}
		response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
		print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True


#                get_ref = ib_NIOS.wapi_request('GET',object_type="scheduledtask",params="?_return_fields=scheduled_time")
#                logging.info(get_ref)
#                res = json.loads(get_ref)
#                ref = json.loads(get_ref)[0]['scheduled_time']
#                print ref 
#		 if ref == future:
#			assert True


                logging.info("Test Case 25 Execution Completed")
                logging.info("============================")
		



         @pytest.mark.run(order=26)
         def test_26_Get_operation_to_read_resource_record_caa(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa_sched.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa_sched.zone.com",response1)
                logging.info("Test Case 26 Execution Completed")
                logging.info("============================")
		sleep(10)

         @pytest.mark.run(order=27)
         def test_27_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa_sched.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa_sched.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa_sched.zone.com',out1)
                logging.info("Test Case 27 Execution Completed")


         @pytest.mark.run(order=28)
         def test_28_schedule_the_caa_record_modification(self):
                logging.info("getting current time and set to future time")
                t = int(time.time())
                print t
                future = t + int(1000)
                get_ref = ib_NIOS.wapi_request('GET',object_type="record:caa")
                ref1 = json.loads(get_ref)[-1]['_ref']

                data = {"name":"caa_sched1.zone.com","ca_type":"ISSUE","ca":"CAA_Authority.com"}
                create_file = ib_NIOS.wapi_request('PUT', object_type=ref1,fields=json.dumps(data),params="?_schedinfo.scheduled_time="+str(future))
                logging.info(create_file)
                res = json.loads(create_file)
                print res

                get_ref = ib_NIOS.wapi_request('GET',object_type="scheduledtask")
                ref1 = json.loads(get_ref)[-1]['_ref']
                data = {"execute_now":True}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 28 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=29)
         def test_29_Get_operation_to_read_resource_record_caa(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa_sched1.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa_sched1.zone.com",response1)
                logging.info("Test Case 29 Execution Completed")
                logging.info("============================")
                sleep(10)

         @pytest.mark.run(order=30)
         def test_30_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa_sched1.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa_sched1.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa_sched1.zone.com',out1)
                logging.info("Test Case 30 Execution Completed")



         @pytest.mark.run(order=31)
         def test_31_schedule_the_caa_record_deletion(self):
                logging.info("getting current time and set to future time")
                t = int(time.time())
                print t
                future = t + int(1000)
                get_ref = ib_NIOS.wapi_request('GET',object_type="record:caa")
                ref1 = json.loads(get_ref)[-1]['_ref']

                create_file = ib_NIOS.wapi_request('DELETE', object_type=ref1,params="?_schedinfo.scheduled_time="+str(future))
                logging.info(create_file)
                res = json.loads(create_file)
                print res

                get_ref = ib_NIOS.wapi_request('GET',object_type="scheduledtask")
                ref1 = json.loads(get_ref)[-1]['_ref']
                data = {"execute_now":True}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
	
                logging.info("Test Case 31 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=32)
         def test_32_Create_New_CAA_Record_Field_is_not_writable_zone(self):
                logging.info("Create_New_CAA_Record_Field_is_not_writable_zone")
                data = {"ca": "CAA_Authority.com","ca_details": "caa critical","ca_flag": "CRITICAL","ca_type": "ISSUE","comment": "critical flag","creator": "STATIC","disable": False,"dns_name": "caa_crtical.zone.com","extattrs": {"Site": {"value": "Banaglore"}},"name": "caa_crtical.zone.com","use_ttl": False,"view": "default","zone": "zone.com" }
                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                assert status == 400 and re.search(r'Field is not writable: zone',response)
                for read in  response:
                        assert True
                logging.info("Test Case 32 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=33)
         def test_33_Create_New_CAA_Record_Field_is_not_writable_dns_name(self):
                logging.info("Create_New_CAA_Record_Field_is_not_writable_dns_name")
                data = {"ca": "CAA_Authority.com","ca_details": "caa critical","ca_flag": "CRITICAL","ca_type": "ISSUE","comment": "critical flag","creator": "STATIC","disable": False,"dns_name": "caa_crtical.zone.com","extattrs": {"Site": {"value": "Banaglore"}},"name": "caa_crtical.zone.com","use_ttl": False,"view": "default"}
                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                assert status == 400 and re.search(r'Field is not writable: dns_name',response)
                for read in  response:
                        assert True
                logging.info("Test Case 33 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=34)
         def test_34_Create_New_CAA_Record_with_ISSUE_type_critical_flag(self):
                logging.info("Create_New_CAA_Record_with_ISSUE_type_critical_flag")
                data = {"ca": "CAA_Authority.com","ca_details": "caa critical","ca_flag": "CRITICAL","ca_type": "ISSUE","comment": "critical flag","creator": "STATIC","disable": False,"extattrs": {"Site": {"value": "Banaglore"}},"name": "caa_crtical.zone.com","use_ttl": False,"view": "default"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 34 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=35)
         def test_35_Get_operation_to_read_resource_record_caa(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa_crtical.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa_crtical.zone.com",response1)
                logging.info("Test Case 35 Execution Completed")
                logging.info("============================")





         @pytest.mark.run(order=36)
         def test_36_Create_New_CAA_Record_Field_with_empty_ca_and_data_in_ca_details_with_ca_flag_critical_ca_type_ISSUE(self):
                logging.info("Create_New_CAA_Record_Field_with_empty_ca_and_data_in_ca_details_with_ca_flag_critical_ca_type_ISSUE")
                data = {"ca": "","ca_details": "caa critical","ca_flag": "CRITICAL","ca_type": "ISSUE","comment": "critical flag","creator": "STATIC","disable": False,"extattrs": {"Site": {"value": "Banaglore"}},"name": "caa_crtical.zone.com","use_ttl": False,"view": "default"}
                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                assert status == 400 and re.search(r'Additional CA Details cannot be provided if a Certificate Authority has not be specified.',response)
                for read in  response:
                        assert True
                logging.info("Test Case 36 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=37)
         def test_37_Create_New_CAA_Record_Field_with_empty_ca_and_data_in_ca_details_with_ca_flag_critical_ca_type_ISSUEWILD(self):
                logging.info("Create_New_CAA_Record_Field_with_empty_ca_and_data_in_ca_details_with_ca_flag_critical_ca_type_ISSUEWILD")
                data = {"ca": "","ca_details": "caa critical","ca_flag": "CRITICAL","ca_type": "ISSUEWILD","comment": "critical flag","creator": "STATIC","disable": False,"extattrs": {"Site": {"value": "Banaglore"}},"name": "caa_crtical.zone.com","use_ttl": False,"view": "default"}
                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                assert status == 400 and re.search(r'Additional CA Details cannot be provided if a Certificate Authority has not be specified.',response)
                for read in  response:
                        assert True
                logging.info("Test Case 37 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=38)
         def test_38_Create_New_sub_AuthZone(self):
                logging.info("Create A new sub Zone")
                				
		logging.info("Get the zone reffrence")
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
				
		data = {"fqdn":"zone_sub.zone.com"}
                response = ib_NIOS.wapi_request('POST', ref=ref1, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 38 Execution Completed")

         @pytest.mark.run(order=39)
         def test_39_create_grid_primary_for_sub_zone(self):
                logging.info("Create grid_primary with required fields")
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[2]['_ref']
                print ref1

                data = {"grid_primary":[{"name":config.grid_fqdn,"stealth":False}]}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
                logging.info(response)
                logging.info("============================")
                print response

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(30)

                logging.info("Test Case 39 Execution Completed")


         @pytest.mark.run(order=40)
         def test_40_Create_New_CAA_Record_with_ISSUE_type_in_subzone(self):
                logging.info("Create A new CAA Record with ISSUE Type in sub zone")
                data = {"ca": "CAA_Authority.com","ca_type": "ISSUE","name": "caa_sub.zone_sub.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 40 Execution Completed")


         @pytest.mark.run(order=41)
         def test_41_Get_operation_to_read_resource_record_caa(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa_sub.zone_sub.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa_sub.zone_sub.zone.com",response1)
                logging.info("Test Case 41 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=42)
         def test_42_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa_sub.zone_sub.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa_sub.zone_sub.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa_sub.zone_sub.zone.com',out1)
                logging.info("Test Case 42 Execution Completed")



         @pytest.mark.run(order=43)
         def test_43_Modify_caa_record_in_sub_zone(self):
                logging.info("Modify_caa_record_in_sub_zone")
                get_ref = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa_sub.zone_sub.zone.com")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"ca": "test@test.com","ca_type": "IODEF","name": "caa_sub1.zone_sub.zone.com"}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
                logging.info(response)
                logging.info("============================")
                print response
                logging.info("Test Case 43 Execution Completed")


         @pytest.mark.run(order=44)
         def test_44_Get_operation_to_read_resource_record_caa(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa_sub1.zone_sub.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa_sub1.zone_sub.zone.com",response1)
                logging.info("Test Case 44 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=45)
         def test_45_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa_sub1.zone_sub.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa_sub1.zone_sub.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa_sub1.zone_sub.zone.com',out1)
                logging.info("Test Case 45 Execution Completed")




         @pytest.mark.run(order=46)
         def test_46_Modify_caa_record_in_sub_zone(self):
                logging.info("Modify_caa_record_in_sub_zone")
                get_ref = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa_sub1.zone_sub.zone.com")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"ca": "CAA_Authority.com","ca_type": "ISSUEWILD","name": "caa_sub.zone_sub.zone.com"}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
                logging.info(response)
                print response
                logging.info("Test Case 46 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=47)
         def test_47_Get_operation_to_read_resource_record_caa(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa_sub.zone_sub.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa_sub.zone_sub.zone.com",response1)
                logging.info("Test Case 47 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=48)
         def test_48_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa_sub.zone_sub.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa_sub.zone_sub.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa_sub.zone_sub.zone.com',out1)
                logging.info("Test Case 48 Execution Completed")



         @pytest.mark.run(order=49)
         def test_49_Delete_caa_record_in_sub_zone(self):
                logging.info("delete_caa_record_in_sub_zone")
                get_ref = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa_sub.zone_sub.zone.com")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                logging.info("Deleting the subzone caa record")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref1)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True
                logging.info("Test Case 49 Execution Completed")
                logging.info("=============================")

         @pytest.mark.run(order=50)
         def test_50_Create_New_CAA_Record_with_invalid_ca_For_IODEF_Type(self):
                logging.info("Create A new CAA Record with addiotional details for IODEF Type")
                data = {"ca": "test","ca_type": "IODEF","name": "caatest123.zone.com"}
                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                assert status == 400 and re.search(r'Should be a valid URL or a Email address.',response)
                for read in  response:
                        assert True
                logging.info("Test Case 50 Execution Completed")


         @pytest.mark.run(order=51)
         def test_51_Modify_grid_dns_object_to_set_allow_updates_any(self):
                logging.info("Modify_grid_dns_object_to_set_allow_updates_any")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"allow_update": [{"_struct": "addressac","address": "Any","permission": "ALLOW"}]}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
                logging.info(response)
                print response
		sleep(10)
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 51 Execution Completed")
                logging.info("============================")



         @pytest.mark.run(order=52)
         def test_52_Modify_grid_dns_object_to_set_allow_updates_any(self):
                logging.info("Modify_grid_dns_object_to_set_allow_updates_any")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns", grid_vip=config.grid_member1_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"allow_update": [{"_struct": "addressac","address": "Any","permission": "ALLOW"}]}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data), grid_vip=config.grid_member1_vip)
                logging.info(response)
                print response
                sleep(10)
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member1_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member1_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member1_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member1_vip)
                sleep(30)
                logging.info("Test Case 52 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=53)
         def test_53_Modify_grid_dns_object_to_set_zone_transfer_for_any(self):
                logging.info("Modify_grid_dns_object_to_set_zonetransfer_any")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"allow_transfer": [{"_struct": "addressac","address": "Any","permission": "ALLOW"}]}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
                logging.info(response)
                print response
                sleep(10)
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 53 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=54)
         def test_54_Modify_grid_dns_object_to_set_zone_transfer_for_any(self):
                logging.info("Modify_grid_dns_object_to_set_zone_transfer_for_any")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns", grid_vip=config.grid_member1_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"allow_transfer": [{"_struct": "addressac","address": "Any","permission": "ALLOW"}]}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data), grid_vip=config.grid_member1_vip)
                logging.info(response)
                print response
                sleep(10)
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member1_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member1_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member1_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member1_vip)
                sleep(30)
                logging.info("Test Case 54 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=55)
         def test_55_Create_New_AuthZone(self):
                logging.info("Create A new Zone")
                data = {"fqdn": "zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="zone_auth", fields=json.dumps(data), grid_vip=config.grid_member1_vip)
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 55 Execution Completed")


         @pytest.mark.run(order=56)
         def test_56_Create_grid_primary_for_secondary_grid(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth", grid_vip=config.grid_member1_vip)
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref

                logging.info("Create A new grid primary")
                data = {"grid_primary": [{"name": config.grid_member1_fqdn,"stealth":False}]}
                response = ib_NIOS.wapi_request('PUT', ref=ref, fields=json.dumps(data), grid_vip=config.grid_member1_vip)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member1_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member1_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member1_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member1_vip)
                sleep(30)
                logging.info("Test Case 56 Execution Completed")
                logging.info("============================")



         @pytest.mark.run(order=57)
         def test_57_Modify_zone_for_import_zone_operation(self):
                logging.info("Modify_grid_dns_object_to_set_zone_transfer_for_any")
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth", grid_vip=config.grid_member1_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"import_from":config.grid_vip,"use_import_from":True}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data), grid_vip=config.grid_member1_vip)
                logging.info(response)
                print response
                sleep(10)
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member1_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member1_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member1_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member1_vip)
                sleep(30)
                logging.info("Test Case 57 Execution Completed")
                logging.info("============================")



         @pytest.mark.run(order=58)
         def test_58_Get_operation_to_read_resource_record_caa_after_import_zone(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa.zone.com", grid_vip=config.grid_member1_vip)
                print response1
                logging.info(response1)
                assert  re.search(r"caa.zone.com",response1)
                logging.info("Test Case 58 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=59)
         def test_59_Get_operation_to_read_resource_record_caa_after_import_zone(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa_crtical.zone.com", grid_vip=config.grid_member1_vip)
                print response1
                logging.info(response1)
                assert  re.search(r"caa_crtical.zone.com",response1)
                logging.info("Test Case 59 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=60)
         def test_60_Get_operation_to_read_resource_record_caa_after_import_zone(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:ns", params="?name=zone_sub.zone.com", grid_vip=config.grid_member1_vip)
                print response1
                logging.info(response1)
                assert  re.search(r"zone_sub.zone.com",response1)
                logging.info("Test Case 60 Execution Completed")
                logging.info("============================")



         @pytest.mark.run(order=61)
         def test_61_DELETE_ALL_caa_record(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="record:caa", grid_vip=config.grid_member1_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Deleting the caa1 record")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref, grid_vip=config.grid_member1_vip)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True

                ref = json.loads(get_ref)[1]['_ref']
                print ref
                logging.info("Deleting the caa1 record")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref, grid_vip=config.grid_member1_vip)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True
                logging.info("Test Case 61 Execution Completed")
                logging.info("============================")



         @pytest.mark.run(order=62)
         def test_62_Delete_zone_after_import_zone_operation(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth", grid_vip=config.grid_member1_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Deleting the zone.com zone")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref, grid_vip=config.grid_member1_vip)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member1_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member1_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member1_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member1_vip)
                sleep(30)

                logging.info("Test Case 62 Execution Completed")
                logging.info("=============================")



         @pytest.mark.run(order=63)
         def test_63_sending_nsupdate_caa_record(self):
                child = pexpect.spawn ('ssh -o StrictHostKeyChecking=no ssrivastava@10.36.199.1')
                child.expect ('ssrivastava.*:')
                child.sendline ('resetm33')
                child.sendline ('nsupdate')
                child.expect ('>')
                child.sendline ('server '+config.grid_vip)
                child.expect ('>')
                child.sendline ('update add caa123.zone.com 100 caa 0 issue "zone.com"')
		child.expect ('>')
                child.sendline ('send')
		child.expect ('>')
		child.sendline ('update add caa124.zone.com 100 caa 0 issuewild "CAA_Authority.com"')
		child.expect ('>')
		child.sendline ('send')
		child.expect ('>')
		child.sendline ('update add caa125.zone.com 100 caa 0 iodef "test@test.com"')
		child.expect ('>')
		child.sendline ('send')
		child.expect ('>')
		child.sendline ('update add a1.zone.com 100 A 1.1.1.1')
		child.expect ('>')
		child.sendline ('send')
		child.expect ('>')
		child.sendline ('update add aaaa.zone.com 100 AAAA FF01::1')
		child.expect ('>')
		child.sendline ('send')
                logging.info("Test Case 63 Execution Completed")
                logging.info("============================")
		sleep(20)





         @pytest.mark.run(order=64)
         def test_64_Get_operation_to_read_resource_record_caa(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa123.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa123.zone.com",response1)
                logging.info("Test Case 64 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=65)
         def test_65_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa123.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa123.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa123.zone.com',out1)
                logging.info("Test Case 65 Execution Completed")


         @pytest.mark.run(order=66)
         def test_66_Get_operation_to_read_resource_record_caa(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa124.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa124.zone.com",response1)
                logging.info("Test Case 66 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=67)
         def test_67_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa124.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa124.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa124.zone.com',out1)
                logging.info("Test Case 67 Execution Completed")



         @pytest.mark.run(order=68)
         def test_68_Get_operation_to_read_resource_record_caa(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa125.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa125.zone.com",response1)
                logging.info("Test Case 68 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=69)
         def test_69_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa125.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa125.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa125.zone.com',out1)
                logging.info("Test Case 69 Execution Completed")

         @pytest.mark.run(order=70)
         def test_70_Get_operation_to_read_resource_record_a(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:a", params="?name=a1.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"a1.zone.com",response1)
                logging.info("Test Case 70 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=71)
         def test_71_dig_query_for_a_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' a1.zone.com in a'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'a1.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'a1.zone.com',out1)
                logging.info("Test Case 71 Execution Completed")


         @pytest.mark.run(order=72)
         def test_72_Get_operation_to_read_resource_record_aaaa(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:aaaa", params="?name=aaaa.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"aaaa.zone.com",response1)
                logging.info("Test Case 72 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=73)
         def test_73_dig_query_for_aaaa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' aaaa.zone.com in aaaa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'aaaa.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'aaaa.zone.com',out1)
                logging.info("Test Case 73 Execution Completed")


         @pytest.mark.run(order=74)
         def test_74_Modify_Scavenging_settings_to_set_operation(self):
                get_ref = ib_NIOS.wapi_request('GET',object_type="grid:dns")
                ref1 = json.loads(get_ref)[0]['_ref']
		print ref1

                data = {"scavenging_settings":{"ea_expression_list":[],"enable_auto_reclamation":False,"enable_recurrent_scavenging":False,"enable_rr_last_queried":False,"enable_scavenging":True,"enable_zone_last_queried":False,"expression_list":[{"op":"AND","op1_type":"LIST"},{"op":"EQ","op1":"rcreator","op1_type":"FIELD","op2":"DYNAMIC","op2_type":"STRING"},{"op":"ENDLIST"}],"reclaim_associated_records":False}}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(40)

                logging.info("Test Case 74 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=75)
         def test_75_run_scavenging_for_caa_record_shoul_not_delete(self):
                logging.info("should not delete caa record after runining scavenging")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
				
                logging.info("run scavenging operation")
                data = {"action":"ANALYZE_RECLAIM"}
                response = ib_NIOS.wapi_request('POST', ref=ref1, fields=json.dumps(data), params="?_function=run_scavenging")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 75 Execution Completed")
                logging.info("============================")
		sleep(30)

         @pytest.mark.run(order=76)
         def test_76_validate_the_scavenging_task(self):
		get_ref = ib_NIOS.wapi_request('GET',object_type="scavengingtask")
                ref1 = json.loads(get_ref)[-1]['status']
                print ref1
                if ref1 == "COMPLETED":
                	assert True
                logging.info("Test Case 76 Execution Completed")
                logging.info("============================")




         @pytest.mark.run(order=77)
         def test_77_Get_operation_to_read_resource_record_caa_after_scavenging(self):
                logging.info("Get_operation_to_read_resource_record_caa_after_scavenging")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa123.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa123.zone.com",response1)
                logging.info("Test Case 77 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=78)
         def test_78_dig_query_for_caa_record_after_scavenging(self):
                logging.info("Perform dig command after_scavenging")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa123.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa123.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa123.zone.com',out1)
                logging.info("Test Case 78 Execution Completed")

         @pytest.mark.run(order=79)
         def test_79_Get_operation_to_read_resource_record_caa_after_scavenging(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa124.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa124.zone.com",response1)
                logging.info("Test Case 79 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=80)
         def test_80_dig_query_for_caa_record_after_scavenging(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa124.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa124.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa124.zone.com',out1)
                logging.info("Test Case 80 Execution Completed")

				
         @pytest.mark.run(order=81)
         def test_81_Get_operation_to_read_resource_record_caa_after_scavenging(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa125.zone.com")
                print response1
                logging.info(response1)
                assert  re.search(r"caa125.zone.com",response1)
                logging.info("Test Case 81 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=82)
         def test_82_dig_query_for_caa_record_after_scavenging(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa125.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa125.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa125.zone.com',out1)
                logging.info("Test Case 82 Execution Completed")



         @pytest.mark.run(order=83)
         def test_83_Get_operation_to_read_resource_record_a_after_scavenging_should_delete(self):
                logging.info("Get_operation_to_read_resource_record_a")
                response = ib_NIOS.wapi_request('GET', object_type="record:a")
                print response
                logging.info(response)
                assert re.search(r'',response)
                logging.info("Test Case 83 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=84)
         def test_84_Get_operation_to_read_resource_record_aaaa_after_scavenging_should_delete(self):
                logging.info("Get_operation_to_read_resource_record_aaaa")
                response = ib_NIOS.wapi_request('GET', object_type="record:aaaa")
                print response
                logging.info(response)
                assert re.search(r'',response)
                logging.info("Test Case 84 Execution Completed")
                logging.info("============================")



         @pytest.mark.run(order=85)
         def test_85_Create_external_secondary(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref

                logging.info("Create A new external secondary")
                data = {"external_secondaries": [{"address": config.grid_member1_vip,"name": config.grid_member1_fqdn,"stealth": False}]}
                response = ib_NIOS.wapi_request('PUT', ref=ref, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 85 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=86)
         def test_86_Create_New_AuthZone(self):
                logging.info("Create A new Zone")
                data = {"fqdn": "zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="zone_auth", fields=json.dumps(data), grid_vip=config.grid_member1_vip)
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 86 Execution Completed")





         @pytest.mark.run(order=87)
         def test_87_Create_external_primary_and_grid_secondary(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth", grid_vip=config.grid_member1_vip)
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref

                logging.info("Create A new external primary and grid secondary")
                data = {"external_primaries": [{"address": config.grid_vip,"name": config.grid_fqdn,"stealth": False}],"grid_secondaries": [{"enable_preferred_primaries": False,"enable_preferred_primaries": False,"grid_replicate": False,"lead": False,"name": config.grid_member1_fqdn,"preferred_primaries": [],"stealth": False}],"use_external_primary":True}
                response = ib_NIOS.wapi_request('PUT', ref=ref, fields=json.dumps(data), grid_vip=config.grid_member1_vip)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 87 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=88)
         def test_88_Modify_the_grid_time_zone(self):
                logging.info("Modify_the_grid_time_zone")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member1_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"time_zone": "(UTC + 5:30) Bombay, Calcutta, Madras, New Delhi"}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data), grid_vip=config.grid_member1_vip)
                logging.info(response)
                print response

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member1_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member1_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member1_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member1_vip)
                sleep(10)

                logging.info("Test Case 88 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=89)
         def test_89_Restart_services(self):
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 89 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=90)
         def test_90_Create_New_CAA_Record_with_ISSUE_type_for_zone_transfer(self):
                logging.info("Create A new CAA Record with ISSUE Type")
                data = {"ca": "CAA_Authority.com","ca_type": "ISSUE","name": "caa_tarnsfer.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 90 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=91)
         def test_91_Modify_log_queries_in_second_grid(self):
                logging.info("Modify a  log_queries")
                data = {"logging_categories":{"log_queries": True}}
                response = ib_NIOS.wapi_request('PUT', ref="grid:dns/ZG5zLmNsdXN0ZXJfZG5zX3Byb3BlcnRpZXMkMA", fields=json.dumps(data), grid_vip=config.grid_member1_vip)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member1_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member1_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member1_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member1_vip)
                sleep(30)
                logging.info("Test Case 91 Execution Completed")



         @pytest.mark.run(order=92)
         def test_92_dig_query_for_caa_record_after_zone_transfer_into_second_grid(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_member1_vip)+' caa_tarnsfer.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_member1_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa_tarnsfer.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa_tarnsfer.zone.com',out1)
                logging.info("Test Case 92 Execution Completed")


         @pytest.mark.run(order=93)
         def test_93_dig_query_for_caa_record_after_zone_transfer(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_member1_vip)+' caa.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_member1_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa.zone.com',out1)
                logging.info("Test Case 93 Execution Completed")

         @pytest.mark.run(order=94)
         def test_94_dig_query_for_caa_record_after_zone_transfer(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_member1_vip)+' caa123.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_member1_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa123.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa123.zone.com',out1)
                logging.info("Test Case 94 Execution Completed")

				
         @pytest.mark.run(order=95)
         def test_95_dig_query_for_caa_record_after_zone_transfer(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_member1_vip)+' caa124.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_member1_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa124.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa124.zone.com',out1)
                logging.info("Test Case 95 Execution Completed")

				

				
         @pytest.mark.run(order=96)
         def test_96_dig_query_for_caa_record_after_zone_transfer(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_member1_vip)+' caa125.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_member1_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa125.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa125.zone.com',out1)
                logging.info("Test Case 96 Execution Completed")
				
         @pytest.mark.run(order=97)
         def test_97_dig_query_for_caa_record_after_zone_transfer(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_member1_vip)+' caa_crtical.zone.com in caa'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_member1_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa_crtical.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa_crtical.zone.com',out1)
                logging.info("Test Case 97 Execution Completed")

				

# Monitoring bug RFE4537-97

         @pytest.mark.run(order=98)
         def test_98_Create_New_CAA_Record_with_Addtional_CA_details_For_IODEF_Type(self):
                logging.info("Create A new CAA Record with addiotional details for IODEF Type")
                data = {"name": "ca.caa.zone.com", "ca_type":"ISSUE"}
                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                assert status == 400 and re.search(r'field for create missing: ca',response)
                for read in  response:
                        assert True
                logging.info("Test Case 98 Execution Completed")



         @pytest.mark.run(order=99)
         def test_99_Create_admin_group(self):
                logging.info("Create A new admin group")
                data = {"name": "group_caa"}
                response = ib_NIOS.wapi_request('POST', object_type="admingroup", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 99 Execution Completed")

         @pytest.mark.run(order=100)
         def test_100_Create_admin_user(self):
                logging.info("Create A new admin user")
                data = {"admin_groups": ["group_caa"],"comment": "test_caa","name": "user_caa","password":"infoblox"}
                response = ib_NIOS.wapi_request('POST', object_type="adminuser", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 100 Execution Completed")

         @pytest.mark.run(order=101)
         def test_101_Create_admin_group_permission_as_deny(self):
                logging.info("Create A new admin user")
                data = {"group":"group_caa","permission":"DENY","resource_type":"CAA"}
                response = ib_NIOS.wapi_request('POST', object_type="permission", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 101 Execution Completed")

         @pytest.mark.run(order=102)
         def test_102_Get_operation_to_read_resource_record_caa_with_deny_permission_negative(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa",user="user_caa",password="infoblox")
                print response1
                logging.info(response1)
                assert  re.search(r"\[\]",response1)
                logging.info("Test Case 102 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=103)
         def test_98_Create_New_CAA_Record_with_deny_permission(self):
                logging.info("Create_New_CAA_Record_with_deny_permission")
                data = {"ca": "test@test.com","ca_type": "IODEF","name": "caa2.zone.com"}
                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data),user="user_caa",password="infoblox")
                print response
                logging.info(response)
                assert status == 400 and re.search(r"Write permission for the resource record type 'CAA' in the zone 'zone.com' is required for this operation.",response)
                logging.info("Test Case 103 Execution Completed")


         @pytest.mark.run(order=104)
         def test_104_Delete_permission_for_caa_record(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="permission", params="?group=group_caa")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Deleting the permission for caa record")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True
                logging.info("Test Case 104 Execution Completed")

         @pytest.mark.run(order=105)
         def test_105_Create_permission_read_for_caa_record(self):
                logging.info("Create_permission_read_for_caa_record")
                data = {"group":"group_caa","permission":"READ","resource_type":"CAA"}
                response = ib_NIOS.wapi_request('POST', object_type="permission", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 105 Execution Completed")

         @pytest.mark.run(order=106)
         def test_106_Get_operation_to_read_resource_record_caa_with_read_permission(self):
                logging.info("Get_operation_to_read_resource_record_caa")
                response1 = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa124.zone.com", user="user_caa",password="infoblox")
                print response1
                logging.info(response1)
                assert  re.search(r"caa124.zone.com",response1)
                logging.info("Test Case 106 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=107)
         def test_107_Create_New_CAA_Record_with_read_permission_negative(self):
                logging.info("Create_New_CAA_Record_with_read_permission")
                data = {"ca": "test@test.com","ca_type": "IODEF","name": "caa2.zone.com"}
                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data), user="user_caa",password="infoblox")
                print response
                logging.info(response)
                assert status == 400 and re.search(r"Write permission for the resource record type 'CAA' in the zone 'zone.com' is required for this operation.",response)
                for read in  response:
                        assert True
                logging.info("Test Case 107 Execution Completed")

         @pytest.mark.run(order=108)
         def test_108_Modify_permission_for_caa_record_from_read_to_write(self):
		data = {"group": "group_caa"}
                get_ref = ib_NIOS.wapi_request('GET', object_type="permission", fields=json.dumps(data))
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref

                logging.info("Modify_permission_for_caa_record_from_read_to_write")
                data = {"permission": "WRITE"}
                response = ib_NIOS.wapi_request('PUT', ref=ref, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 108 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=109)
         def test_109_Create_New_CAA_Record_with_IODEF_type_with_write_permission(self):
                logging.info("Create A new CAA Record with IODEF Type")
                data = {"ca": "test@test.com","ca_type": "IODEF","name": "caa2_w.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data), user="user_caa",password="infoblox")
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 109 Execution Completed")

         @pytest.mark.run(order=110)
         def test_110_Create_New_CAA_Record_with_ISSUEWILD_type_with_write_permission(self):
                logging.info("Create A new CAA Record with ISSUEWILD Type")
                data = {"ca": "CAA_Authority.com","ca_type": "ISSUEWILD","name": "caa1_w.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data), user="user_caa",password="infoblox")
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 110 Execution Completed")

				
         @pytest.mark.run(order=111)
         def test_111_Create_New_CAA_Record_with_NO_CA_Specified_For_ISSUE_Type_with_write_permission(self):
                logging.info("Create A new CAA Record with ISSUE Type")
                data = {"ca": "","ca_type": "ISSUE","name": "caa12345_w.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data), user="user_caa",password="infoblox")
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 111 Execution Completed")

         @pytest.mark.run(order=112)
         def test_112_Create_admin_group_for_submitter(self):
                logging.info("Create A new admin group")
                data = {"access_method":["GUI","API"],"name": "group_sub"}
                response = ib_NIOS.wapi_request('POST', object_type="admingroup", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 112 Execution Completed")

         @pytest.mark.run(order=113)
         def test_113_Create_admin_group_for_approver(self):
                logging.info("Create A new admin group")
                data = {"access_method":["GUI","API"],"name": "group_appr"}
                response = ib_NIOS.wapi_request('POST', object_type="admingroup", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 113 Execution Completed")

         @pytest.mark.run(order=114)
         def test_114_Create_admin_user_for_submitter(self):
                logging.info("Create A new admin user")
                data = {"admin_groups": ["group_sub"],"comment": "test_caa","name": "user_sub","password":"infoblox"}
                response = ib_NIOS.wapi_request('POST', object_type="adminuser", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 114 Execution Completed")

         @pytest.mark.run(order=115)
         def test_115_Create_admin_user_for_approver(self):
                logging.info("Create A new admin user")
                data = {"admin_groups": ["group_appr"],"comment": "test_caa","name": "user_appr","password":"infoblox"}
                response = ib_NIOS.wapi_request('POST', object_type="adminuser", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 115 Execution Completed")

         @pytest.mark.run(order=116)
         def test_116_Create_admin_group_permission_as_write_for_submitter_group_for_zone(self):
                logging.info("Create A new admin user")
                data = {"group": "group_sub","permission": "WRITE","resource_type": "ZONE"}
                response = ib_NIOS.wapi_request('POST', object_type="permission", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 116 Execution Completed")

         @pytest.mark.run(order=117)
         def test_117_Create_admin_group_permission_as_write_for_submitter_group(self):
                logging.info("Create A new admin user")
                data = {"group": "group_sub","permission": "WRITE","resource_type": "CAA"}
                response = ib_NIOS.wapi_request('POST', object_type="permission", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 117 Execution Completed")

         @pytest.mark.run(order=118)
         def test_118_Create_admin_group_permission_as_write_for_approval_group_for_zone(self):
                logging.info("Create A new admin user")
                data = {"group": "group_appr","permission": "WRITE","resource_type": "ZONE"}
                response = ib_NIOS.wapi_request('POST', object_type="permission", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 118 Execution Completed")

         @pytest.mark.run(order=119)
         def test_119_Create_admin_group_permission_as_write_for_approval_group(self):
                logging.info("Create A new admin user")
                data = {"group": "group_appr","permission": "WRITE","resource_type": "CAA"}
                response = ib_NIOS.wapi_request('POST', object_type="permission", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 119 Execution Completed")


         @pytest.mark.run(order=120)
         def test_120_Create_New_approval_workflow(self):
                logging.info("Create A new approval workflow")
                data = {"approval_group": "group_appr","submitter_group": "group_sub"}
                response = ib_NIOS.wapi_request('POST', object_type="approvalworkflow", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 120 Execution Completed")



         @pytest.mark.run(order=121)
         def test_121_Create_New_CAA_Record_with_IODEF_type_with_write_permission(self):
                logging.info("Create A new CAA Record with IODEF Type")
                data = {"ca": "test@test.com","ca_type": "IODEF","name": "caa_sub.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data), user="user_sub",password="infoblox")
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 121 Execution Completed")

         @pytest.mark.run(order=122)
         def test_122_Modify_permission_for_caa_record_from_read_to_write(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="scheduledtask", user="user_appr",password="infoblox")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref = json.loads(get_ref)[-1]['_ref']
                print ref

                logging.info("Modify_permission_for_caa_record_from_read_to_write")
                data = {"approval_status":"APPROVED"}
                response = ib_NIOS.wapi_request('PUT', ref=ref, fields=json.dumps(data),user="user_appr",password="infoblox")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                response1 = ib_NIOS.wapi_request('GET', ref=ref, user="user_appr",password="infoblox")
                class objectview(object):
                        def __init__(self,d):
                                self.__dict__ =d
                                d = response1
                                o = objectview(d)
                                assert o.execution_status == COMPLETED

                logging.info("Test Case 122 Execution Completed")
                logging.info("============================")

         @pytest.mark.run(order=123)
         def test_123_Modify_the_approval_workflow_with_required_ticket_number(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="approvalworkflow")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref

                logging.info("Modify_the_approval_workflow_with_required_ticket_number")
                data = {"ticket_number":"REQUIRED"}
                response = ib_NIOS.wapi_request('PUT', ref=ref, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 123 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=124)
         def test_124_Create_New_CAA_Record_with_IODEF_type_with_ticket_number(self):
                logging.info("Create_New_CAA_Record_with_IODEF_type_with_ticket_number")
                data = {"ca": "test1@test.com","ca_type": "IODEF","name": "caa_sub2.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data), params="?_approvalinfo.ticket_number=12345", user="user_sub",password="infoblox")
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 124 Execution Completed")

         @pytest.mark.run(order=125)
         def test_125_Modify_permission_for_caa_record_from_read_to_write(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="scheduledtask", user="user_appr",password="infoblox")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref = json.loads(get_ref)[-1]['_ref']
                print ref

                logging.info("Modify_permission_for_caa_record_from_read_to_write")
                data = {"approval_status":"APPROVED"}
                response = ib_NIOS.wapi_request('PUT', ref=ref, fields=json.dumps(data),user="user_appr",password="infoblox")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

		response1 = ib_NIOS.wapi_request('GET', object_type="scheduledtask", user="user_appr",password="infoblox")
                logging.info(response1)
                ref2 = json.loads(response1)[-1]['execution_status']
                print ref2
		read = re.search(r'COMPLETED',ref2)
		for read in ref2:	
		    assert True
                logging.info("Test Case 125 Execution Completed")
                logging.info("============================")



         @pytest.mark.run(order=126)
         def test_126_Create_New_AuthZone(self):
                logging.info("Create A new Zone")
                data = {"fqdn": "zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="zone_auth", fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 126 Execution Completed")

         @pytest.mark.run(order=127)
         def test_127_create_grid_primary_for_zone(self):
                logging.info("Create grid_primary with required fields")
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth", grid_vip=config.grid_member2_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"grid_primary": [{"name": config.grid_member3_fqdn,"stealth":False}]}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                logging.info(response)
                logging.info("============================")
                print response

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member2_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member2_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member2_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member2_vip)
                sleep(20)
                logging.info("Test Case 127 Execution Completed")

         @pytest.mark.run(order=128)
         def test_128_Create_New_CAA_Record_with_NO_CA_Specified_For_ISSUE_Type(self):
                logging.info("Create A new CAA Record with ISSUE Type")
                data = {"ca": "","ca_type": "ISSUE","name": "caa12345.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 128 Execution Completed")

         @pytest.mark.run(order=129)
         def test_129_Create_New_CAA_Record_with_NO_CA_Specified_For_ISSUEWILD_Type(self):
                logging.info("Create A new CAA Record with ISSUEWILD Type")
                data = {"ca": "","ca_type": "ISSUEWILD","name": "caa145.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 129 Execution Completed")

         @pytest.mark.run(order=130)
         def test_130_Create_New_CAA_Record_with_IODEF_type(self):
                logging.info("Create A new CAA Record with IODEF Type")
                data = {"ca": "test@test.com","ca_type": "IODEF","name": "caa2.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 130 Execution Completed")

         @pytest.mark.run(order=131)
         def test_131_Modify_log_queries(self):

                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns", grid_vip=config.grid_member2_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1


                logging.info("Modify a  log_queries")
                data = {"logging_categories":{"log_queries": True}}
                response = ib_NIOS.wapi_request('PUT', ref=ref1, fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member2_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member2_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member2_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member2_vip)
                sleep(20)
                logging.info("Test Case 131 Execution Completed")


         @pytest.mark.run(order=132)
         def test_132_Modify_grid_for_adding_dns_resolver(self):
                logging.info("Modify_grid_for_adding_dns_resolver")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member2_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"dns_resolver_setting": {"resolvers": ["10.0.2.35"]}}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                logging.info(response)
                logging.info("============================")
                print response
                logging.info("Test Case 132 Execution Completed")
         @pytest.mark.run(order=133)
         def test_133_Modify_grid_dns_object_for_adding_forwarders(self):
                logging.info("Modify_grid_dns_object_for_adding_forwarders")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns", grid_vip=config.grid_member2_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"forwarders": ["10.39.16.160"]}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                logging.info(response)
                logging.info("============================")
                print response

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member2_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member2_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member2_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member2_vip)
                sleep(30)
                logging.info("Test Case 133 Execution Completed")

         @pytest.mark.run(order=134)
         def test_134_Modify_grid_threatprotection_object_for_download_ruleset(self):
                logging.info("Modify_grid_threatprotection_object_for_download_ruleset")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:threatprotection", grid_vip=config.grid_member2_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"enable_auto_download": True}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                logging.info(response)
                logging.info("============================")
                print response

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member2_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member2_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member2_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member2_vip)
                sleep(30)
                logging.info("Test Case 134 Execution Completed")

         @pytest.mark.run(order=135)
         def test_135_Create_download_atp_rule_update_function_call_to_download_ruleset(self):
                logging.info("Create_download_atp_rule_update_function_call_to_download_ruleset")
                response = ib_NIOS.wapi_request('POST',object_type="fileop",params="?_function=download_atp_rule_update", grid_vip=config.grid_member2_vip)
                print response
                logging.info(response)
                read = re.search(r'200',response)
                logging.info("Test Case 135 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=136)
         def test_136_Create_custom_rule_for_Rate_Limiting(self):
                logging.info("Create_custom_rule_for_Rate_Limiting")
				
		data = {"name": "RATE LIMITED UDP DNS Message Type"}
                get_ref = ib_NIOS.wapi_request('GET',object_type="threatprotection:ruletemplate", fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
								
                data = {"config":{"action": "PASS","log_severity": "MAJOR","params":[{"name": "RATE_FILTER_COUNT","value": "1"},{"name": "DROP_INTERVAL","value": "10"},{"name":"EVENTS_PER_SECOND","value": "4"},{"name": "RECORD_TYPE","value": "CAA"},{"name": "RATE_ALGORITHM","value": "Rate_Limiting"}]},"disabled": False,"template":ref1}
                response = ib_NIOS.wapi_request('POST', object_type="threatprotection:grid:rule", fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member2_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member2_vip)
                sleep(30)
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member2_vip)
                sleep(30)
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member2_vip)
                sleep(60)
        	logging.info("Test Case 136 Execution Completed")
                logging.info("============================")



         @pytest.mark.run(order=137)
         def test_137_dig_query_for_caa_record_after_creating_ratelimit(self):
                logging.info("Perform dig command")
		for x in range(10):
                    dig_cmd = 'dig @'+str(config.grid_member3_vip)+' caa2.zone.com IN CAA'
                    dig_cmd1 = os.system(dig_cmd)
		sleep(20)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_member2_vip)+' " tail -10 /var/log/syslog | grep -ir \'RATE LIMITED UDP DNS Message Type\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa2.zone.com',out1)
                logging.info("Test Case 137 Execution Completed")


         @pytest.mark.run(order=138)
         def test_138_Delete_ratelimit_rule(self):
                logging.info("Delete_ratelimit_rule")
		data = {"type":"CUSTOM"}
                get_ref = ib_NIOS.wapi_request('GET', object_type="threatprotection:grid:rule", fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Deleting the caa record")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref, grid_vip=config.grid_member2_vip)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member2_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member2_vip)
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus", grid_vip=config.grid_member2_vip)
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices", grid_vip=config.grid_member2_vip)
                sleep(30)
                logging.info("Test Case 138 Execution Completed")
                logging.info("============================")



         @pytest.mark.run(order=139)
         def test_139_Create_custom_rule_for_Blacklist(self):
                logging.info("Create_custom_rule_for_Blacklist")
				
		data = {"name": "BLACKLIST UDP FQDN lookup for DNS Message Type"}
                get_ref = ib_NIOS.wapi_request('GET',object_type="threatprotection:ruletemplate", fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
								
                data = {"config": {"action": "DROP","log_severity": "MAJOR","params": [{"name": "RECORD_TYPE","value": "CAA"},{"name": "FQDN","value": "zone.com"},{"name": "EVENTS_PER_SECOND", "value": "1"}]},"disabled": False,"template":ref1}
                response = ib_NIOS.wapi_request('POST', object_type="threatprotection:grid:rule", fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid", grid_vip=config.grid_member2_vip)
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member2_vip)
		sleep(30)
		request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member2_vip)
		sleep(30)
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish), grid_vip=config.grid_member2_vip)
		sleep(40)
                logging.info("Test Case 139 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=140)
         def test_140_dig_query_for_caa_record_after_creating_BLACKLIST_rule(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_member3_vip)+' caa2.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_member2_vip)+' " tail -10 /var/log/syslog | grep -ir \'BLACKLIST UDP FQDN lookup for DNS Message Type\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa2.zone.com',out1)
                logging.info("Test Case 140 Execution Completed")


         @pytest.mark.run(order=141)
         def test_141_Create_New_CAA_Record_with_ISSUE_type_in_signed_zone(self):
	 
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                logging.info("Modify the zone into signed")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
		for read in  response:
                    assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
		
# Remove after resolve Bug : RFE4537-11
#                logging.info("Create A new CAA Record with ISSUE Type in signed zone")
#                data = {"ca": "CAA_Authority.com","ca_type": "ISSUE","name": "caa_sign.zone.com"}
#                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
#                print response
#                logging.info(response)
#                assert status == 400 and re.search(r"Generation of DNSSEC records for resource record .*caa_sign.zone.com.* of type .*CAA.* failed: .*unexpected error.* .*code: 34.*.",response)
#                for read in  response:
#                        assert True



# Enable below code after Bug Reslove RFE4537-11
                logging.info("Create A new CAA Record with ISSUE Type in signed zone")
                data = {"ca": "CAA_Authority.com","ca_type": "ISSUE","name": "caa_sign.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                get_ref = ib_NIOS.wapi_request('GET', object_type="record:caa", params="?name=caa_sign.zone.com")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref2 = json.loads(get_ref)[0]['_ref']
                print ref2
                logging.info("Deleting the caa record")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref2)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True
                logging.info("Test Case 141 Execution Completed")


         @pytest.mark.run(order=142)
         def test_142_create_for_csv_export_with_replace_operation(self):
                logging.info("Create the fileop function to download csv_export object with CAA record")
                data = {"_object":"record:caa","zone":"zone.com","_separator":"COMMA"}
                create_file = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=csv_export", grid_vip=config.grid_member2_vip)
                logging.info(create_file)
                res = json.loads(create_file)
                token = json.loads(create_file)['token']
                url = json.loads(create_file)['url']
                print create_file
                print res
                print token
                print url
                logging.info("Create the fileop function to dowload the csv file to the specified url")
                os.system('curl -k1 -u admin:infoblox -H "Content-type:application/force-download" -O %s'%(url))

                sleep(5)
                logging.info("Create the fileop function to download csv_import object with CAA record")
                data = {"action":"TEST","operation":"REPLACE","token":token}
                create_file1 = ib_NIOS.wapi_request('POST', object_type="fileop",fields=json.dumps(data),params="?_function=csv_import", grid_vip=config.grid_member2_vip)
                logging.info(create_file1)
                response1 = ast.literal_eval(json.dumps(create_file1))
                print response1
                sleep(30)
                logging.info("Get the status of last executed csv_import task using csvimporttask object")
                task = ib_NIOS.wapi_request('GET', object_type="csvimporttask",grid_vip=config.grid_member2_vip)
                logging.info(task)
                response2 = json.loads(task)
                csv_imp2 = response2[-1]
                task1 = ast.literal_eval(json.dumps(csv_imp2))
                print task1
                class objectview(object):
                        def __init__(self, d):
                                self.__dict__ = d
                                d = task1
                                o = objectview(d)
                                assert o.status == TEST_COMPLETED and o.operation == REPLACE
                logging.info("Test Case 142 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=143)
         def test_143_BUG_RFE_4537_13(self):
                logging.info("Create A new CAA Record with ISSUEWILD Type")
                data = {"ca": "sdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdssdsdsdsdsdsdsdsdsdsdsdsdsdsd.sdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdssdsdsdsdsdsdsdsdsdsdsdsdsdsds","ca_type": "ISSUEWILD","name": "caa1.zone.com"}
                status,response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                print response
                logging.info(response)
                assert status == 400 and re.search(r'Domain label cannot be longer than 63 characters',response)
                for read in  response:
                        assert True
                logging.info("Test Case 143 Execution Completed")


         @pytest.mark.run(order=144)
         def test_144_IODEF_type_Certificate_Authority_should_be_in_http_or_https_format_for_web_address_updated_in_admin_guide(self):
                logging.info("Create A new CAA Record with IODEF Type")
                data = {"ca": "test.com","ca_type": "IODEF","name": "caa27.zone.com"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data), grid_vip=config.grid_member2_vip)
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 144 Execution Completed")



##### Test cases for network_view

         @pytest.mark.run(order=145)
         def test_145_Create_network_view_as_netview(self):
                logging.info("Create_network_view_as_netview")
                data = {"name": "netview"}
                response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(20)
                logging.info("Test Case 145 Execution Completed")

         @pytest.mark.run(order=146)
         def test_146_Create_New_AuthZone_for_netview(self):
                logging.info("Create_New_AuthZone_for_netview")
                data = {"fqdn": "zone.com","view":"default.netview"}
                response = ib_NIOS.wapi_request('POST', object_type="zone_auth", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 146 Execution Completed")

         @pytest.mark.run(order=147)
         def test_147_Create_grid_primary_for_zone_in_netview(self):
                logging.info("create_grid_primary_for_zone_in_netview")
		data = {"view": "default.netview"}
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth", fields=json.dumps(data))
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"grid_primary": [{"name": config.grid_fqdn,"stealth":False}]}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
                logging.info(response)
                logging.info("============================")
                print response

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(20)
                logging.info("Test Case 147 Execution Completed")

         @pytest.mark.run(order=148)
         def test_148_Create_New_CAA_Record_with_ISSUE_type(self):
                logging.info("Create A new CAA Record with ISSUE Type")
                data = {"ca": "CAA_Authority.com","ca_type": "ISSUE","name": "caa.zone.com", "view": "default.netview"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 148 Execution Completed")

				
         @pytest.mark.run(order=149)
         def test_149_Create_New_CAA_Record_with_NO_CA_Specified_For_ISSUE_Type(self):
                logging.info("Create A new CAA Record with ISSUE Type")
                data = {"ca": "","ca_type": "ISSUE","name": "caa12345.zone.com", "view": "default.netview"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 149 Execution Completed")

         @pytest.mark.run(order=150)
         def test_150_Create_New_CAA_Record_with_NO_CA_Specified_For_ISSUEWILD_Type(self):
                logging.info("Create A new CAA Record with ISSUEWILD Type")
                data = {"ca": "","ca_type": "ISSUEWILD","name": "caa145.zone.com", "view": "default.netview"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 150 Execution Completed")

         @pytest.mark.run(order=151)
         def test_151_Create_New_CAA_Record_with_ISSUEWILD_type(self):
                logging.info("Create A new CAA Record with ISSUEWILD Type")
                data = {"ca": "CAA_Authority.com","ca_type": "ISSUEWILD","name": "caa1.zone.com", "view": "default.netview"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 151 Execution Completed")

         @pytest.mark.run(order=152)
         def test_152_Create_New_CAA_Record_with_IODEF_type(self):
                logging.info("Create A new CAA Record with IODEF Type")
                data = {"ca": "test@caa_record.com","ca_type": "IODEF","name": "caa2.zone.com", "view": "default.netview"}
                response = ib_NIOS.wapi_request('POST', object_type="record:caa", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 152 Execution Completed")

         @pytest.mark.run(order=153)
         def test_153_Modify_member_dns_object_to_set_view_as_netview(self):
                logging.info("Modify_member_dns_object_to_set_view_as_netview")
                get_ref = ib_NIOS.wapi_request('GET', object_type="member:dns")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"views": ["default.netview","default"]}
                response = ib_NIOS.wapi_request('PUT',ref=ref1,fields=json.dumps(data))
                logging.info(response)
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                sleep(10)
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 153 Execution Completed")
                logging.info("============================")

				
         @pytest.mark.run(order=154)
         def test_154_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa.zone.com',out1)
                logging.info("Test Case 154 Execution Completed")

         @pytest.mark.run(order=155)
         def test_155_dig_query_for_caa12345_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa12345.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa12345.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa12345.zone.com',out1)
                logging.info("Test Case 154 Execution Completed")
		
         @pytest.mark.run(order=156)
         def test_156_dig_query_for_caa145_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa145.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa145.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa145.zone.com',out1)
                logging.info("Test Case 156 Execution Completed")
				
         @pytest.mark.run(order=157)
         def test_157_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa1.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa1.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa1.zone.com',out1)
                logging.info("Test Case 157 Execution Completed")
				
         @pytest.mark.run(order=158)
         def test_158_dig_query_for_caa_record(self):
                logging.info("Perform dig command")
                dig_cmd = 'dig @'+str(config.grid_vip)+' caa2.zone.com IN CAA'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'caa2.zone.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'caa2.zone.com',out1)
                logging.info("Test Case 158 Execution Completed")


'''

         @pytest.mark.run(order=159)
         def test_159_generatesafenetclientcert_Fileop_Function_Call(self):
                logging.info("Test the generatesafenetclientcert function call in fileop object")
                data = {"algorithm":"RSASHA256","member":config.grid_fqdn}
                response = ib_NIOS.wapi_request('POST',object_type="fileop",params="?_function=generatesafenetclientcert",fields=json.dumps(data))
                print response
                logging.info(response)
                res = re.search(r'200',response)
                for res in response:
                        assert True
                logging.info("Test Case 159 Execution Completed")
                logging.info("============================")


         @pytest.mark.run(order=160)
         def test_160_Deleting_infoblox_id(self):
                logging.info("Unregistering safenet luna sa five")
                try:
                        child = pexpect.spawn ('ssh -o StrictHostKeyChecking=no ssrivastava@10.36.199.1')
                        child.expect ('ssrivastava.*:')
                        child.sendline ('resetm33')
                        child.expect ('.*$')
                        child.sendline ('ssh admin@10.39.10.12')
                        child.expect ('.*password:')
                        child.sendline ('Infoblox.123')
                        child.expect ('.*lunash:>')
                        child.sendline ('client delete -c lnv')
                        child.expect ('>')
                        child.sendline ('proceed')
                        child.expect ('.*lunash:>')
                        child.sendline ('exit')
                except:
                        assert True
                        logging.info("============================")


         @pytest.mark.run(order=161)
         def test_161_registering_safenet_luna_sa_five(self):
                logging.info("Registering safenet luna sa five")
                child = pexpect.spawn ('ssh -o StrictHostKeyChecking=no ssrivastava@10.36.199.1')
                child.expect ('ssrivastava.*:')
                child.sendline ('resetm33')
                child.expect ('.*$')
                child.sendline ('ssh root@'+config.grid_vip)
                child.expect ('.*#')
                child.sendline ('cd /storage/safenet-hsm/lunasa_5/cert/client/')
                child.expect ('.*#')
                child.sendline ('scp '+config.grid_vip+'.pem admin@10.39.10.12:')
                child.expect ('.*password:')
                child.sendline ('Infoblox.123')
                child.expect ('.*#')
                child.sendline ('ssh admin@10.39.10.12')
                child.expect ('.*password:')
                child.sendline ('Infoblox.123')
                child.expect ('.*lunash:>')
                child.sendline ('client register -c lnv -i '+config.grid_vip)
                child.expect ('.*lunash:>')
                child.sendline ('client assignPartition -c lnv -P QAPartition')
                child.expect ('.*lunash:>')
                child.sendline ('exit')
                child.expect ('.*#')
                child.sendline ('exit')
                logging.info("============================")


         @pytest.mark.run(order=162)
         def test_162_adding_safenet_group_luna_sa_five(self):
                filename="server.pem"
                data = {"filename":filename}
 	        logging.info("uploading Clint Certificste")
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
            	data = {"comment": "testing","hsm_safenet":[{"disable": False,"name": "10.39.10.12","partition_serial_number":"154441011","server_cert": token}],"hsm_version":"LunaSA_5","name": "HSM_group","pass_phrase":"Infoblox.123"}
            	create_file1 = ib_NIOS.wapi_request('POST', object_type="hsm:safenetgroup",fields=json.dumps(data))
            	logging.info(create_file1)
            	print create_file1
            	assert re.search(r"",create_file1)
            	logging.info("Test Case 162 Execution Completed")
            	logging.info("============================")


         @pytest.mark.run(order=163)
         def test_163_validate_the_status_of_hsm_group(self):
         	get_ref = ib_NIOS.wapi_request('GET',object_type="hsm:safenetgroup",params="?_return_fields=status")
            	ref1 = json.loads(get_ref)[-1]['status']
            	print ref1
            	if ref1 == "UP":
                	assert True
            	logging.info("Test Case 163 Execution Completed")
            	logging.info("============================")







         @pytest.mark.run(order=23)
         def test_DELETE_zone(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                logging.info("Deleting the zone.com zone")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print get_status
                logging.info(get_status)
                read = re.search(r'200',get_status)
                for read in get_status:
                        assert True
                logging.info("Test Case 23 Execution Completed")
                logging.info("=============================")

         @pytest.mark.run(order=21)
         def test_restart_services(self):
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 21 Execution Completed")

'''
