
# This test suite is for 'RFE-6478: DNSSEC secure' feature of 8.3. 
# Grid Configurations: Grid1 master and Grid2 Master
# Preperation data: Grid2 has FMZ, IPV4 RMZ, IPV6 RMZ for grid dns, member dns and DNS view level cases of grid1. Enable DNS service on grid2 and set TTL to 10 secs.
# Grid1 has DNS service enabled, All recursion enable, Global forwarders enabled(grid2), Root name servers enabled(grid2),Trust anhors configured at grid dns, member dns and DNS view editors as required by test cases on grid1.
# 'ib_NIOS.py' utility in 'ib_utils' need to have support of Grid2 session configuration(Eg. def wapi_request_2) for this test suite to run. This test suite requires SA Grid1 and SA Grid2
#Author: Narasimha Swamy.N 

import re
import config
import pytest
import unittest
import logging
import subprocess
import os
import json
import commands
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
        def test_1_Modify_grid_dns_object_to_set_allow_updates_any(self):
		logging.info("Modify_grid_dns_object_to_set_TTL to 10 secs")
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="grid:dns")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                data = {"default_ttl": 10}
                response = ib_NIOS.wapi_request_2('PUT',ref=ref1,fields=json.dumps(data))
                logging.info(response)
                print response
                sleep(10)
                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request_2('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")


# Grid DNS Properties 
# Data on grid2 to be used for Grid DNS Properties data on grid1 for DNSSEC secure feature
        @pytest.mark.run(order=2)
        def test_2_Create_New_AuthZone(self):
		logging.info("Create zone 'test.com'")
                #data = {"fqdn": "test.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}],"operation": "SIGN"}
                data = {"fqdn": "test.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                #response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth",params="?_function=dnssec_operation", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 2 Execution Completed")
	
 	@pytest.mark.run(order=3)
        def test_3_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=test.com")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                logging.info("Modify the zone test.com to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 3 Execution Completed")

	@pytest.mark.run(order=4)
        def test_4_Create_New_AuthZone(self):
                logging.info("Create zone 'non_dnssec.test.com'")
                data = {"fqdn": "non_dnssec.test.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 4 Execution Completed")

	@pytest.mark.run(order=5)
        def test_5_Create_New_AuthZone(self):
                logging.info("Create zone 'dnssec.test.com'")
                data = {"fqdn": "dnssec.test.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 5 Execution Completed")
        
        @pytest.mark.run(order=6)
        def test_6_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=dnssec.test.com")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone dnssec.test.com to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request_2('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 6 Execution Completed")
	
	@pytest.mark.run(order=7)
        def test_7_Create_New_A_Record_in_subzone(self):
                logging.info("Create A new 'arec1.dnssec.test.com' in sub zone dnssec.test.com")
                data = {"name": "arec1.dnssec.test.com","ipv4addr": "1.1.1.1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:a", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 7 Execution Completed")

	@pytest.mark.run(order=8)
        def test_8_Create_New_A_Record_in_subzone(self):
                logging.info("Create A new 'arec1.non_dnssec.test.com' in sub zone non_dnssec.test.com")
                data = {"name": "arec1.non_dnssec.test.com","ipv4addr": "1.1.1.2"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:a", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 8 Execution Completed")

	@pytest.mark.run(order=9)
        def test_9_Create_New_AuthZone(self):
                logging.info("Create ipv4 reverse zone '20.0.0.0/8'")
                data = {"fqdn": "20.0.0.0/8","zone_format": "IPV4","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV4 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 9 Execution Completed")

        @pytest.mark.run(order=10)
        def test_10_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=20.0.0.0/8")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '20.in-addr.arpa' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 10 Execution Completed")
	
	@pytest.mark.run(order=11)
        def test_11_Create_New_AuthZone(self):
                logging.info("Create ipv4 reverse sub zone '20.0.0.0/16'")
                data = {"fqdn": "20.0.0.0/16","zone_format": "IPV4","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV4 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 11 Execution Completed")
	
	@pytest.mark.run(order=12)
        def test_12_Create_New_AuthZone(self):
                logging.info("Create ipv4 reverse zone '20.1.0.0/16'")
                data = {"fqdn": "20.1.0.0/16","zone_format": "IPV4","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV4 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 12 Execution Completed")
        
	@pytest.mark.run(order=13)
        def test_13_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=20.0.0.0/16")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '0.20.in-addr.arpa' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request_2('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 13 Execution Completed")

	@pytest.mark.run(order=14)
        def test_14_Create_New_IPV4_PTR_Record_in_subzone(self):
                logging.info("Create PTR new '1.0.0.20.in-addr.arpa' in sub zone 20.0.0.0/16")
                data = {"ptrdname": "ipv4_ptr_20_0_0_1.com","ipv4addr": "20.0.0.1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 14 Execution Completed")

	@pytest.mark.run(order=15)
        def test_15_Create_New_IPV4_PTR_Record_in_subzone(self):
                logging.info("Create PTR new '1.0.1.20.in-addr.arpa' in sub zone 20.1.0.0/16")
                data = {"ptrdname": "ipv4_ptr_20_1_0_1.com","ipv4addr": "20.1.0.1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 15 Execution Completed")

	@pytest.mark.run(order=16)
        def test_16_Create_New_AuthZone(self):
                logging.info("Create ipv6 reverse zone '1000::/16'")
                data = {"fqdn": "1000::/16","zone_format": "IPV6","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV6 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 16 Execution Completed")

        @pytest.mark.run(order=17)
        def test_17_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=1000::/16")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '1000::/16' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 17 Execution Completed")

	@pytest.mark.run(order=18)
        def test_18_Create_New_AuthZone(self):
                logging.info("Create ipv6 reverse zone '1000::/32'")
                data = {"fqdn": "1000::/32","zone_format": "IPV6","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV6 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 18 Execution Completed")

	@pytest.mark.run(order=19)
        def test_19_Create_New_AuthZone(self):
                logging.info("Create ipv6 reverse zone '1000:1::/32'")
                data = {"fqdn": "1000:1::/32","zone_format": "IPV6","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV6 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 19 Execution Completed")

        @pytest.mark.run(order=20)
        def test_20_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=1000::/32")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '1000::/32' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request_2('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 20 Execution Completed")

	@pytest.mark.run(order=21)
        def test_21_Create_New_IPV6_PTR_Record_in_subzone(self):
                logging.info("Create IPV6 PTR '1000::1' in sub zone 1000::/32")
                data = {"ptrdname": "ipv6_ptr1.com","ipv6addr": "1000::1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 21 Execution Completed")

	@pytest.mark.run(order=22)
        def test_22_Create_New_IPV6_PTR_Record_in_subzone(self):
                logging.info("Create IPV6 PTR '1000:1::1' in sub zone 1000:1::/32")
                data = {"ptrdname": "ipv6_ptr2.com","ipv6addr": "1000:1::1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 22 Execution Completed")

# Member DNS properties
# Data on grid2 to be used for Member DNS Properties data on grid1 for DNSSEC secure feature
        @pytest.mark.run(order=23)
        def test_23_Create_New_AuthZone(self):
		logging.info("Create Auth zone 'foo.com'")
                data = {"fqdn": "foo.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 23 Execution Completed")
	
 	@pytest.mark.run(order=24)
        def test_24_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=foo.com")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone foo.com to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 24 Execution Completed")

	@pytest.mark.run(order=25)
        def test_25_Create_New_AuthZone(self):
                logging.info("Create Auth zone 'non_dnssec.foo.com'")
                data = {"fqdn": "non_dnssec.foo.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 25 Execution Completed")

	@pytest.mark.run(order=26)
        def test_26_Create_New_AuthZone(self):
                logging.info("Create Auth zone 'dnssec.foo.com'")
                data = {"fqdn": "dnssec.foo.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 26 Execution Completed")
        
        @pytest.mark.run(order=27)
        def test_27_Modify_zone_to_sign(self):

                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=dnssec.foo.com")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone dnssec.foo.com to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request_2('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 27 Execution Completed")
	
	@pytest.mark.run(order=28)
        def test_28_Create_New_A_Record_in_subzone(self):
                logging.info("Create A new 'arec1.dnssec.foo.com' in sub zone dnssec.foo.com")
                data = {"name": "arec1.dnssec.foo.com","ipv4addr": "2.1.1.1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:a", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 28 Execution Completed")

	@pytest.mark.run(order=29)
        def test_29_Create_New_A_Record_in_subzone(self):
                logging.info("Create A new 'arec1.non_dnssec.foo.com' in sub zone non_dnssec.foo.com")
                data = {"name": "arec1.non_dnssec.foo.com","ipv4addr": "2.1.1.2"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:a", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 29 Execution Completed")

	@pytest.mark.run(order=30)
        def test_30_Create_New_AuthZone(self):
                logging.info("Create ipv4 reverse zone '30.0.0.0/8'")
                data = {"fqdn": "30.0.0.0/8","zone_format": "IPV4","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV4 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 30 Execution Completed")

        @pytest.mark.run(order=31)
        def test_31_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=30.0.0.0/8")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '30.in-addr.arpa' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 31 Execution Completed")
	
	@pytest.mark.run(order=32)
        def test_32_Create_New_AuthZone(self):
                logging.info("Create ipv4 reverse sub zone '30.0.0.0/16'")
                data = {"fqdn": "30.0.0.0/16","zone_format": "IPV4","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV4 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 32 Execution Completed")
	
	@pytest.mark.run(order=33)
        def test_33_Create_New_AuthZone(self):
                logging.info("Create ipv4 reverse zone '30.1.0.0/16'")
                data = {"fqdn": "30.1.0.0/16","zone_format": "IPV4","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV4 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 33 Execution Completed")
        
	@pytest.mark.run(order=34)
        def test_34_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=30.0.0.0/16")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '0.30.in-addr.arpa' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request_2('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 34 Execution Completed")

	@pytest.mark.run(order=35)
        def test_35_Create_New_IPV4_PTR_Record_in_subzone(self):
                logging.info("Create PTR new '1.0.0.30.in-addr.arpa' in sub zone 30.0.0.0/16")
                data = {"ptrdname": "ipv4_ptr_30_0_0_1.com","ipv4addr": "30.0.0.1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 35 Execution Completed")

	@pytest.mark.run(order=36)
        def test_36_Create_New_IPV4_PTR_Record_in_subzone(self):
                logging.info("Create PTR new '1.0.1.30.in-addr.arpa' in sub zone 30.1.0.0/16")
                data = {"ptrdname": "ipv4_ptr_30_1_0_1.com","ipv4addr": "30.1.0.1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 36 Execution Completed")

	@pytest.mark.run(order=37)
        def test_37_Create_New_AuthZone(self):
                logging.info("Create ipv6 reverse zone '2000::/16'")
                data = {"fqdn": "2000::/16","zone_format": "IPV6","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV6 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 37 Execution Completed")

        @pytest.mark.run(order=38)
        def test_38_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=2000::/16")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '2000::/16' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 38 Execution Completed")

	@pytest.mark.run(order=39)
        def test_39_Create_New_AuthZone(self):
                logging.info("Create ipv6 reverse zone '2000::/32'")
                data = {"fqdn": "2000::/32","zone_format": "IPV6","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV6 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 39 Execution Completed")

	@pytest.mark.run(order=40)
        def test_40_Create_New_AuthZone(self):
                logging.info("Create ipv6 reverse zone '2000:1::/32'")
                data = {"fqdn": "2000:1::/32","zone_format": "IPV6","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV6 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 40 Execution Completed")

        @pytest.mark.run(order=41)
        def test_41_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=2000::/32")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '2000::/32' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request_2('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 41 Execution Completed")

	@pytest.mark.run(order=42)
        def test_42_Create_New_IPV6_PTR_Record_in_subzone(self):
                logging.info("Create IPV6 PTR '2000::1' in sub zone 2000::/32")
                data = {"ptrdname": "ipv6_ptr1.com","ipv6addr": "2000::1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 42 Execution Completed")

	@pytest.mark.run(order=43)
        def test_43_Create_New_IPV6_PTR_Record_in_subzone(self):
                logging.info("Create IPV6 PTR '2000:1::1' in sub zone 2000:1::/32")
                data = {"ptrdname": "ipv6_ptr2.com","ipv6addr": "2000:1::1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 43 Execution Completed")


# DNS view Properties 
# Data on grid2 to be used for Member DNS Properties data on grid1 for DNSSEC secure feature
        @pytest.mark.run(order=44)
        def test_44_Create_New_AuthZone(self):
		logging.info("Create Auth zone 'bar.com'")
                data = {"fqdn": "bar.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 44 Execution Completed")
	
 	@pytest.mark.run(order=45)
        def test_45_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=bar.com")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone bar.com to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 45 Execution Completed")

	@pytest.mark.run(order=46)
        def test_46_Create_New_AuthZone(self):
                logging.info("Create Auth zone 'non_dnssec.bar.com'")
                data = {"fqdn": "non_dnssec.bar.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 46 Execution Completed")

	@pytest.mark.run(order=47)
        def test_47_Create_New_AuthZone(self):
                logging.info("Create Auth zone 'dnssec.bar.com'")
                data = {"fqdn": "dnssec.bar.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 47 Execution Completed")
        
        @pytest.mark.run(order=48)
        def test_48_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=dnssec.bar.com")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone dnssec.bar.com to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request_2('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 48 Execution Completed")
	
	@pytest.mark.run(order=49)
        def test_49_Create_New_A_Record_in_subzone(self):
                logging.info("Create A new 'arec1.dnssec.bar.com' in sub zone dnssec.foo.com")
                data = {"name": "arec1.dnssec.bar.com","ipv4addr": "3.1.1.1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:a", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 49 Execution Completed")

	@pytest.mark.run(order=50)
        def test_50_Create_New_A_Record_in_subzone(self):
                logging.info("Create A new 'arec1.non_dnssec.bar.com' in sub zone non_dnssec.foo.com")
                data = {"name": "arec1.non_dnssec.bar.com","ipv4addr": "3.1.1.2"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:a", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 50 Execution Completed")

	@pytest.mark.run(order=51)
        def test_51_Create_New_AuthZone(self):
                logging.info("Create ipv4 reverse zone '40.0.0.0/8'")
                data = {"fqdn": "40.0.0.0/8","zone_format": "IPV4","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV4 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 51 Execution Completed")
	
        @pytest.mark.run(order=52)
        def test_52_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=40.0.0.0/8")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '40.in-addr.arpa' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 52 Execution Completed")
	
	@pytest.mark.run(order=53)
        def test_53_Create_New_AuthZone(self):
                logging.info("Create ipv4 reverse sub zone '40.0.0.0/16'")
                data = {"fqdn": "40.0.0.0/16","zone_format": "IPV4","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV4 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 53 Execution Completed")
	
	@pytest.mark.run(order=54)
        def test_54_Create_New_AuthZone(self):
                logging.info("Create ipv4 reverse zone '40.1.0.0/16'")
                data = {"fqdn": "40.1.0.0/16","zone_format": "IPV4","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV4 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 54 Execution Completed")
        
	@pytest.mark.run(order=55)
        def test_55_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=40.0.0.0/16")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '0.40.in-addr.arpa' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request_2('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 55 Execution Completed")

	@pytest.mark.run(order=56)
        def test_56_Create_New_IPV4_PTR_Record_in_subzone(self):
                logging.info("Create PTR new '1.0.0.40.in-addr.arpa' in sub zone 40.0.0.0/16")
                data = {"ptrdname": "ipv4_ptr_40_0_0_1.com","ipv4addr": "40.0.0.1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 56 Execution Completed")

	@pytest.mark.run(order=57)
        def test_57_Create_New_IPV4_PTR_Record_in_subzone(self):
                logging.info("Create PTR new '1.0.1.40.in-addr.arpa' in sub zone 40.1.0.0/16")
                data = {"ptrdname": "ipv4_ptr_40_1_0_1.com","ipv4addr": "40.1.0.1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 57 Execution Completed")

	@pytest.mark.run(order=58)
        def test_58_Create_New_AuthZone(self):
                logging.info("Create ipv6 reverse zone '3000::/16'")
                data = {"fqdn": "3000::/16","zone_format": "IPV6","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV6 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 58 Execution Completed")

        @pytest.mark.run(order=59)
        def test_59_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=3000::/16")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '3000::/16' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 59 Execution Completed")

	@pytest.mark.run(order=60)
        def test_60_Create_New_AuthZone(self):
                logging.info("Create ipv6 reverse zone '3000::/32'")
                data = {"fqdn": "3000::/32","zone_format": "IPV6","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV6 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 60 Execution Completed")

	@pytest.mark.run(order=61)
        def test_61_Create_New_AuthZone(self):
                logging.info("Create ipv6 reverse zone '3000:1::/32'")
                data = {"fqdn": "3000:1::/32","zone_format": "IPV6","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth IPV6 reverse zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 61 Execution Completed")

        @pytest.mark.run(order=62)
        def test_62_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=3000::/32")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone '3000::/32' to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request_2('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 62 Execution Completed")


	@pytest.mark.run(order=63)
        def test_63_Create_New_IPV6_PTR_Record_in_subzone(self):
                logging.info("Create IPV6 PTR '3000::1' in sub zone 3000::/32")
                data = {"ptrdname": "ipv6_ptr1.com","ipv6addr": "3000::1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 63 Execution Completed")

	@pytest.mark.run(order=64)
        def test_64_Create_New_IPV6_PTR_Record_in_subzone(self):
                logging.info("Create IPV6 PTR '3000:1::1' in sub zone 3000:1::/32")
                data = {"ptrdname": "ipv6_ptr2.com","ipv6addr": "3000:1::1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:ptr", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 64 Execution Completed")

#Data for Grid DNS properties for hierarchy of zones on grid1 for DNSSEC secure feature

	@pytest.mark.run(order=65)
        def test_65_Create_New_AuthZone(self):
                logging.info("Create Auth zone 'sub1.test.com'")
                data = {"fqdn": "sub1.test.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 65 Execution Completed")

        @pytest.mark.run(order=66)
        def test_66_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=sub1.test.com")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone sub1.test.com to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 66 Execution Completed")

	@pytest.mark.run(order=67)
        def test_67_Create_New_AuthZone(self):
                logging.info("Create Auth zone 'child1.sub1.test.com'")
                data = {"fqdn": "child1.sub1.test.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 67 Execution Completed")

        @pytest.mark.run(order=68)
        def test_68_Modify_zone_to_sign(self):
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth", params="?fqdn=child1.sub1.test.com")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
                logging.info("Modify the zone child1.sub1.test.com to sign the zone")
                data = {"operation":"SIGN"}
                response = ib_NIOS.wapi_request_2('POST', ref=ref1, fields=json.dumps(data), params="?_function=dnssec_operation")
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                    assert True
                logging.info("Test Case 68 Execution Completed")

	@pytest.mark.run(order=69)
        def test_69_Create_New_AuthZone(self):
                logging.info("Create Auth zone 'child2.sub1.test.com'")
                data = {"fqdn": "child2.sub1.test.com","grid_primary": [{"name": config.grid2_fqdn,"stealth":False}], "comment": "Auth zone" }
                response = ib_NIOS.wapi_request_2('POST', object_type="zone_auth" ,fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True

                logging.info("Restart services")
                grid =  ib_NIOS.wapi_request_2('GET', object_type="grid")
                ref = json.loads(grid)[0]['_ref']
                publish={"member_order":"SIMULTANEOUSLY"}
                request_publish = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=publish_changes",fields=json.dumps(publish))
                sleep(10)
                request_restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=requestrestartservicestatus")
                restart = ib_NIOS.wapi_request_2('POST', object_type = ref + "?_function=restartservices")
                sleep(30)
                logging.info("Test Case 69 Execution Completed")

	@pytest.mark.run(order=70)
        def test_70_Create_New_A_Record_in_subzone(self):
                logging.info("Create A new 'arec1.sub1.test.com' in sub zone sub1.test.com")
                data = {"name": "arec1.sub1.test.com","ipv4addr": "4.1.1.1"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:a", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 70 Execution Completed")

	@pytest.mark.run(order=71)
        def test_71_Create_New_A_Record_in_subzone(self):
                logging.info("Create A new 'arec1.child1.sub1.test.com' in sub zone child1.sub1.test.com")
                data = {"name": "arec1.child1.sub1.test.com","ipv4addr": "4.1.1.2"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:a", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 71 Execution Completed")

	@pytest.mark.run(order=72)
        def test_72_Create_New_A_Record_in_subzone(self):
                logging.info("Create A new 'arec1.child2.sub1.test.com' in sub zone child2.sub1.test.com")
                data = {"name": "arec1.child2.sub1.test.com","ipv4addr": "4.1.1.3"}
                response = ib_NIOS.wapi_request_2('POST', object_type="record:a", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 72 Execution Completed")

# Grid1 Test cases

# Test DNSSEC secure feature at Grid dns properties editor. Code to copy trust anchor from grid2 to grid1

	@pytest.mark.run(order=73)
        def test_73_Modify_grid_dns_object_to_set_allow_recursive_queries_global_forwarder_trust_anchor_test_com(self):
                logging.info("Modify_grid_dns_object_to_set_allow_recursive_queries_global_forwarder_trust_anchor_test_com")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1
		logging.info("Get zone reference for zone test.com")
                get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth",  params="?fqdn=test.com")
                logging.info(get_ref)
                res2 = json.loads(get_ref)
                ref2 = json.loads(get_ref)[0]['_ref']
                print ref2

		data_trust1 = {"operation" : "EXPORT_ANCHORS"}
		get_ref = ib_NIOS.wapi_request_2('POST', object_type = ref2 +"?_function=dnssec_export", fields=json.dumps(data_trust1))
                logging.info(get_ref)
                response = json.loads(get_ref)
		token = response['token']
		url = response['url']
		cmd = "curl -k1 -u admin:infoblox  -H \"Content-Type: application/force-download\" -O " + str(url)
		response = commands.getoutput(cmd)
		cmd = "curl -k1 -u admin:infoblox -H \"Content-Type: application/json\" -X POST \"https://config.grid2_fqdn/wapi/v2.9/fileop?_function=downloadcomplete\" -d '{\"token\": token}'"
		response = commands.getoutput(cmd)
		with    open("trust_anchors.txt", "r") as fin:
        		val = fin.read()
		print val
		arr_list = val.split()
		#print arr_list[4]
		token = arr_list[4].lstrip('"')
		token = token.rstrip('";')
                data = {"allow_recursive_query": True, "forwarders": [config.grid2_vip], "forward_only": True, "dnssec_trusted_keys": [{"algorithm": "8", "dnssec_must_be_secure": False, "fqdn": "test.com","key": token, "secure_entry_point": True}],  "logging_categories": {"log_responses": True}   }
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
                logging.info("Test Case 73 Execution Completed")
                logging.info("============================")


# Test for default DNSSEC trust anchor feature behaviour. IE.. if 'Responses must be secure' is disabled for trust anchor, query for non dnssec record should pass with 'NOERROR'.

	@pytest.mark.run(order=74)
	def test_74_dig_query_for_arec1_non_dnssec_test_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.non_dnssec.test.com for existing behaviour. IE.. With 'Responses must be secure' feature disabled")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.non_dnssec.test.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.non_dnssec.test.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'arec1.non_dnssec.test.com IN A response: NOERROR',out1)
                logging.info("Test Case 74 Execution Completed")

## Test DNSSEC secure feature when "Responses must be secure" feature is enabled at Grid DNS properties editor

	@pytest.mark.run(order=75)
        def test_75_Modify_grid_dns_object_to_enable_responses_must_be_secure_for_trust_anchor_test_com(self):
                logging.info("Modify_grid_dns_object_to_enable_responses_must_be_secure_for_trust_anchor_test_com")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
                logging.info(get_ref)
                res1 = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

# Export keys for FMZ from grid2 to add to grid1
		get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth",  params="?fqdn=test.com")
                logging.info(get_ref)
                res2 = json.loads(get_ref)
                ref2 = json.loads(get_ref)[0]['_ref']
                print ref2

                data_fmz_trust = {"operation" : "EXPORT_ANCHORS"}
                get_ref = ib_NIOS.wapi_request_2('POST', object_type = ref2 +"?_function=dnssec_export", fields=json.dumps(data_fmz_trust))
                logging.info(get_ref)
                response_fmz = json.loads(get_ref)
                token_fmz = response_fmz['token']
                url_fmz = response_fmz['url']
                cmd = "curl -k1 -u admin:infoblox  -H \"Content-Type: application/force-download\" -O " + str(url_fmz)
                response_fmz = commands.getoutput(cmd)

                cmd = "curl -k1 -u admin:infoblox -H \"Content-Type: application/json\" -X POST \"https://config.grid2_fqdn/wapi/v2.9/fileop?_function=downloadcomplete\" -d '{\"token\": token}'"
                response_fmz = commands.getoutput(cmd)
                with    open("trust_anchors.txt", "r") as fin:
                        val = fin.read()
		print "################ Trust Anchor of FMZ Start #################\n"
                print val
		print "################ Trust Anchor of FMZ End #################\n"
                arr_list = val.split()
                token_fmz = arr_list[4].lstrip('"')
                token_fmz = token_fmz.rstrip('";')

# Export keys for IPV4 RMZ from grid2 to add to grid1
		get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth",  params="?fqdn=20.0.0.0/8")
                logging.info(get_ref)
                res3 = json.loads(get_ref)
                ref3 = json.loads(get_ref)[0]['_ref']
                print ref3

                data_ipv4_rmz_trust = {"operation" : "EXPORT_ANCHORS"}
                get_ref = ib_NIOS.wapi_request_2('POST', object_type = ref3 +"?_function=dnssec_export", fields=json.dumps(data_ipv4_rmz_trust))
                logging.info(get_ref)
                response_ipv4_rmz = json.loads(get_ref)
                token_ipv4_rmz = response_ipv4_rmz['token']
                url_ipv4_rmz = response_ipv4_rmz['url']
                cmd = "curl -k1 -u admin:infoblox  -H \"Content-Type: application/force-download\" -O " + str(url_ipv4_rmz)
                response_ipv4_fmz = commands.getoutput(cmd)

                cmd = "curl -k1 -u admin:infoblox -H \"Content-Type: application/json\" -X POST \"https://config.grid2_fqdn/wapi/v2.9/fileop?_function=downloadcomplete\" -d '{\"token\": token}'"
                response_ipv4_rmz = commands.getoutput(cmd)
                with    open("trust_anchors.txt", "r") as fin:
                        val = fin.read()
		print "################ Trust Anchor of IPV4 RMZ Start #################\n"
                print val
		print "################ Trust Anchor of IPV4 RMZ End #################\n"
                arr_list = val.split()
                token_ipv4_rmz = arr_list[4].lstrip('"')
                token_ipv4_rmz = token_ipv4_rmz.rstrip('";')

# Export keys for IPV6 RMZ from grid2 to add to grid1
		get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth",  params="?fqdn=1000::/16")
                logging.info(get_ref)
                res4 = json.loads(get_ref)
                ref4 = json.loads(get_ref)[0]['_ref']
                print ref4

                data_ipv6_rmz_trust = {"operation" : "EXPORT_ANCHORS"}
                get_ref = ib_NIOS.wapi_request_2('POST', object_type = ref4 +"?_function=dnssec_export", fields=json.dumps(data_ipv6_rmz_trust))
                logging.info(get_ref)
                response_ipv6_rmz = json.loads(get_ref)
                token_ipv6_rmz = response_ipv6_rmz['token']
                url_ipv6_rmz = response_ipv6_rmz['url']
                cmd = "curl -k1 -u admin:infoblox  -H \"Content-Type: application/force-download\" -O " + str(url_ipv6_rmz)
                response_ipv6_fmz = commands.getoutput(cmd)

                cmd = "curl -k1 -u admin:infoblox -H \"Content-Type: application/json\" -X POST \"https://config.grid2_fqdn/wapi/v2.9/fileop?_function=downloadcomplete\" -d '{\"token\": token}'"
                response_ipv6_rmz = commands.getoutput(cmd)
                with    open("trust_anchors.txt", "r") as fin:
                        val = fin.read()
		print "################ Trust Anchor of IPV6 RMZ Start #################\n"
                print val
		print "################ Trust Anchor of IPV6 RMZ End #################\n"
                arr_list = val.split()
                token_ipv6_rmz = arr_list[4].lstrip('"')
                token_ipv6_rmz = token_ipv6_rmz.rstrip('";')

# dnssec trust keys to add to grid1
		data = {"dnssec_trusted_keys": [{"algorithm": "8", "dnssec_must_be_secure": True, "fqdn": "test.com","key": token_fmz, "secure_entry_point": True},{"algorithm": "8", "dnssec_must_be_secure": True, "fqdn": "20.in-addr.arpa","key": token_ipv4_rmz, "secure_entry_point": True},{"algorithm": "8", "dnssec_must_be_secure": True, "fqdn": "0.0.0.1.ip6.arpa","key": token_ipv6_rmz, "secure_entry_point": True}]}
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
                logging.info("Test Case 75 Execution Completed")
                logging.info("============================")

	@pytest.mark.run(order=76)
	def test_76_dig_query_for_arec1_dnssec_test_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.dnssec.test.com  when DNSSEC secure feature enabled and global forwarders configured as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.dnssec.test.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.dnssec.test.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'arec1.dnssec.test.com IN A response: NOERROR',out1)
                logging.info("Test Case 76 Execution Completed")
		
	@pytest.mark.run(order=77)
	def test_77_dig_query_for_arec1_non_dnssec_test_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.non_dnssec.test.com when DNSSEC secure feature enabled and global forwarders configured as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.non_dnssec.test.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.non_dnssec.test.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                #assert re.search(r'validating arec1.non_dnssec.test.com\/A: must be secure failure',out1)
                assert re.search(r'info must-be-secure resolving \'arec1.non_dnssec.test.com/A/IN\'',out1)
                logging.info("Test Case 77 Execution Completed")
	
	@pytest.mark.run(order=78)
	def test_78_dig_query_for_IPV4_PTR_20_0_0_1_record(self):
                logging.info("Perform dig command for 'IPV4 PTR' record 1.0.0.20.in-addr.arpa  when DNSSEC secure feature enabled and global forwarders configured as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.20.in-addr.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.20.in-addr.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'1.0.0.20.in-addr.arpa IN PTR response: NOERROR',out1)
                logging.info("Test Case 78 Execution Completed")

	@pytest.mark.run(order=79)
	def test_79_dig_query_for_IPV4_PTR_20_1_0_1_record(self):
                logging.info("Perform dig command for 'IPV4 PTR' non-dnssec record 1.0.1.20.in-addr.arpa when DNSSEC secure feature enabled and global forwarders configured as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.1.20.in-addr.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.1.20.in-addr.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'info must-be-secure resolving \'1.0.1.20.in-addr.arpa/PTR/IN\'',out1)
                logging.info("Test Case 79 Execution Completed")

	@pytest.mark.run(order=80)
	def test_80_dig_query_for_IPV6_PTR_1000_1_record(self):
                logging.info("Perform dig command for 'IPV6 PTR' record 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.ip6.arpa when DNSSEC secure feature enabled and global forwarders configured as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.ip6.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.ip6.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.ip6.arpa IN PTR response: NOERROR',out1)
                logging.info("Test Case 80 Execution Completed")

	@pytest.mark.run(order=81)
	def test_81_dig_query_for_IPV6_PTR_1000_1_1_record(self):
                logging.info("Perform dig command for non-dnssec 'IPV6 PTR' record 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.1.ip6.arpa when DNSSEC secure feature enabled and global forwarders configured as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.1.ip6.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.1.ip6.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'info must-be-secure resolving \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.1.ip6.arpa/PTR/IN\'',out1)
                logging.info("Test Case 81 Execution Completed")

# Test DNSSEC secure feature on hierarchy of zones

	@pytest.mark.run(order=82)
	def test_82_dig_query_for_arec1_sub1_test_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.sub1.test.com  when DNSSEC secure feature enabled and global forwarders configured as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.sub1.test.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.sub1.test.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'arec1.sub1.test.com IN A response: NOERROR',out1)
                logging.info("Test Case 82 Execution Completed")

	@pytest.mark.run(order=83)
	def test_83_dig_query_for_arec1_child1_sub1_test_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.child1_sub1.test.com  when DNSSEC secure feature enabled and global forwarders configured as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.child1.sub1.test.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.child1.sub1.test.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'arec1.child1.sub1.test.com IN A response: NOERROR',out1)
                logging.info("Test Case 83 Execution Completed")

	@pytest.mark.run(order=84)
	def test_84_dig_query_for_arec1_child2_sub1_test_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.child2.sub1.test.com when DNSSEC secure feature enabled and global forwarders configured as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.child2.sub1.test.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.child2.sub1.test.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'info must-be-secure resolving \'arec1.child2.sub1.test.com/A/IN\'',out1)
                logging.info("Test Case 84 Execution Completed")

	'''
# This part of cases with custom root name servers is blocked because of bug NIOS-65581. Uncomment and run this test cases when the bug is fixed.
# Test DNSSEC secure feature with custom root name server configured as grid2 and trust anchors of FMZ, IPV4/IPV6 RMZ on Grid dns properties editor.

	@pytest.mark.run(order=85)
        def test_85_Modify_grid_dns_object_to_set_allow_recursive_queries_global_forwarder_trust_anchor(self):
                logging.info("Modify_grid_dns_object_to_set_allow_recursive_queries_global_forwarder_trust_anchor and custom root name server as grid2 in grid dns properties editor")
                get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

                #data = {"allow_recursive_query": True, "forwarders": ["10.35.112.13"]}
                data = {"forwarders": [], "forward_only": False, "custom_root_name_servers": [{ "address": config.grid2_vip, "name": config.grid2_fqdn }] }
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
                logging.info("Test Case 85 Execution Completed")
                logging.info("============================")

	@pytest.mark.run(order=86)
	def test_86_dig_query_for_arec1_dnssec_test_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.dnssec.test.com  when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.dnssec.test.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.dnssec.test.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'arec1.dnssec.test.com IN A response: NOERROR',out1)
                logging.info("Test Case 86 Execution Completed")

		
	@pytest.mark.run(order=87)
	def test_87_dig_query_for_arec1_non_dnssec_test_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.non_dnssec.test.com when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.non_dnssec.test.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.non_dnssec.test.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                #assert re.search(r'validating arec1.non_dnssec.test.com\/A: must be secure failure',out1)
                assert re.search(r'info must-be-secure resolving \'arec1.non_dnssec.test.com/A/IN\'',out1)
                logging.info("Test Case 87 Execution Completed")
	
	@pytest.mark.run(order=88)
	def test_88_dig_query_for_IPV4_PTR_20_0_0_1_record(self):
                logging.info("Perform dig command for 'IPV4 PTR' record 1.0.0.20.in-addr.arpa  when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.20.in-addr.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.20.in-addr.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'1.0.0.20.in-addr.arpa IN PTR response: NOERROR',out1)
                logging.info("Test Case 88 Execution Completed")

	@pytest.mark.run(order=89)
	def test_89_dig_query_for_IPV4_PTR_20_1_0_1_record(self):
                logging.info("Perform dig command for 'IPV4 PTR' non-dnssec record 1.0.1.20.in-addr.arpa when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.1.20.in-addr.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.1.20.in-addr.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'info must-be-secure resolving \'1.0.1.20.in-addr.arpa/PTR/IN\'',out1)
                logging.info("Test Case 89 Execution Completed")

	@pytest.mark.run(order=90)
	def test_90_dig_query_for_IPV6_PTR_1000_1_record(self):
                logging.info("Perform dig command for 'IPV6 PTR' record 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.ip6.arpa when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.ip6.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.ip6.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.ip6.arpa IN PTR response: NOERROR',out1)
                logging.info("Test Case 90 Execution Completed")

	@pytest.mark.run(order=91)
	def test_91_dig_query_for_IPV6_PTR_1000_1_1_record(self):
                logging.info("Perform dig command for non-dnssec 'IPV6 PTR' record 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.1.ip6.arpa when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.1.ip6.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.1.ip6.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'info must-be-secure resolving \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.1.ip6.arpa/PTR/IN\'',out1)
                logging.info("Test Case 91 Execution Completed")


# Test DNSSEC secure feature on hierarchy of zones with custom root name servers configured in grid dns properies editor

	@pytest.mark.run(order=92)
	def test_92_dig_query_for_arec1_sub1_test_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.sub1.test.com  when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.sub1.test.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.sub1.test.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'arec1.sub1.test.com IN A response: NOERROR',out1)
                logging.info("Test Case 92 Execution Completed")

	@pytest.mark.run(order=93)
	def test_93_dig_query_for_arec1_child1_sub1_test_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.child1_sub1.test.com  when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.child1.sub1.test.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.child1.sub1.test.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'arec1.child1.sub1.test.com IN A response: NOERROR',out1)
                logging.info("Test Case 93 Execution Completed")
		
	@pytest.mark.run(order=94)
	def test_94_dig_query_for_arec1_child2_sub1_test_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.child2.sub1.test.com when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.child2.sub1.test.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.child2.sub1.test.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'info must-be-secure resolving \'arec1.child2.sub1.test.com/A/IN\'',out1)
                logging.info("Test Case 94 Execution Completed")

	'''	

# Test DNSSEC secure feature at Member DNS properties.

	@pytest.mark.run(order=95)
        def test_95_Modify_member_dns_object_to_set_allow_recursive_queries_global_forwarder_trust_anchor(self):
                logging.info("Modify_memberdns_object_to_set_trust_anchor and custom root name server as grid2 in grid dns properties editor")
                get_ref = ib_NIOS.wapi_request('GET', object_type="member:dns")
                #get_ref = ib_NIOS.wapi_request('GET', object_type="grid:dns")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

# Export keys for FMZ from grid2 to add to grid1
		get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth",  params="?fqdn=foo.com")
                logging.info(get_ref)
                res2 = json.loads(get_ref)
                ref2 = json.loads(get_ref)[0]['_ref']
                print ref2

                data_fmz_trust = {"operation" : "EXPORT_ANCHORS"}
                get_ref = ib_NIOS.wapi_request_2('POST', object_type = ref2 +"?_function=dnssec_export", fields=json.dumps(data_fmz_trust))
                logging.info(get_ref)
                response_fmz = json.loads(get_ref)
                token_fmz = response_fmz['token']
                url_fmz = response_fmz['url']
                cmd = "curl -k1 -u admin:infoblox  -H \"Content-Type: application/force-download\" -O " + str(url_fmz)
                response_fmz = commands.getoutput(cmd)

                cmd = "curl -k1 -u admin:infoblox -H \"Content-Type: application/json\" -X POST \"https://config.grid2_fqdn/wapi/v2.9/fileop?_function=downloadcomplete\" -d '{\"token\": token}'"
                response_fmz = commands.getoutput(cmd)
                with    open("trust_anchors.txt", "r") as fin:
                        val = fin.read()
		print "################ Trust Anchor of FMZ Start #################\n"
                print val
		print "################ Trust Anchor of FMZ End #################\n"
                arr_list = val.split()
                token_fmz = arr_list[4].lstrip('"')
                token_fmz = token_fmz.rstrip('";')

# Export keys for IPV4 RMZ from grid2 to add to grid1
		get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth",  params="?fqdn=30.0.0.0/8")
                logging.info(get_ref)
                res3 = json.loads(get_ref)
                ref3 = json.loads(get_ref)[0]['_ref']
                print ref3

                data_ipv4_rmz_trust = {"operation" : "EXPORT_ANCHORS"}
                get_ref = ib_NIOS.wapi_request_2('POST', object_type = ref3 +"?_function=dnssec_export", fields=json.dumps(data_ipv4_rmz_trust))
                logging.info(get_ref)
                response_ipv4_rmz = json.loads(get_ref)
                token_ipv4_rmz = response_ipv4_rmz['token']
                url_ipv4_rmz = response_ipv4_rmz['url']
                cmd = "curl -k1 -u admin:infoblox  -H \"Content-Type: application/force-download\" -O " + str(url_ipv4_rmz)
                response_ipv4_fmz = commands.getoutput(cmd)

                cmd = "curl -k1 -u admin:infoblox -H \"Content-Type: application/json\" -X POST \"https://config.grid2_fqdn/wapi/v2.9/fileop?_function=downloadcomplete\" -d '{\"token\": token}'"
                response_ipv4_rmz = commands.getoutput(cmd)
                with    open("trust_anchors.txt", "r") as fin:
                        val = fin.read()
		print "################ Trust Anchor of IPV4 RMZ Start #################\n"
                print val
		print "################ Trust Anchor of IPV4 RMZ End #################\n"
                arr_list = val.split()
                token_ipv4_rmz = arr_list[4].lstrip('"')
                token_ipv4_rmz = token_ipv4_rmz.rstrip('";')

# Export keys for IPV6 RMZ from grid2 to add to grid1
		get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth",  params="?fqdn=2000::/16")
                logging.info(get_ref)
                res4 = json.loads(get_ref)
                ref4 = json.loads(get_ref)[0]['_ref']
                print ref4

                data_ipv6_rmz_trust = {"operation" : "EXPORT_ANCHORS"}
                get_ref = ib_NIOS.wapi_request_2('POST', object_type = ref4 +"?_function=dnssec_export", fields=json.dumps(data_ipv6_rmz_trust))
                logging.info(get_ref)
                response_ipv6_rmz = json.loads(get_ref)
                token_ipv6_rmz = response_ipv6_rmz['token']
                url_ipv6_rmz = response_ipv6_rmz['url']
                cmd = "curl -k1 -u admin:infoblox  -H \"Content-Type: application/force-download\" -O " + str(url_ipv6_rmz)
                response_ipv6_fmz = commands.getoutput(cmd)

                cmd = "curl -k1 -u admin:infoblox -H \"Content-Type: application/json\" -X POST \"https://config.grid2_fqdn/wapi/v2.9/fileop?_function=downloadcomplete\" -d '{\"token\": token}'"
                response_ipv6_rmz = commands.getoutput(cmd)
                with    open("trust_anchors.txt", "r") as fin:
                        val = fin.read()
		print "################ Trust Anchor of IPV6 RMZ Start #################\n"
                print val
		print "################ Trust Anchor of IPV6 RMZ End #################\n"
                arr_list = val.split()
                token_ipv6_rmz = arr_list[4].lstrip('"')
                token_ipv6_rmz = token_ipv6_rmz.rstrip('";')

# dnssec trust keys to add to grid1
		data = { "dnssec_enabled": True, "dnssec_trusted_keys": [{"algorithm": "8", "dnssec_must_be_secure": True, "fqdn": "foo.com","key": token_fmz, "secure_entry_point": True},{"algorithm": "8", "dnssec_must_be_secure": True, "fqdn": "30.in-addr.arpa","key": token_ipv4_rmz, "secure_entry_point": True},{"algorithm": "8", "dnssec_must_be_secure": True, "fqdn": "0.0.0.2.ip6.arpa","key": token_ipv6_rmz, "secure_entry_point": True}]}
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
                logging.info("Test Case 95 Execution Completed")
                logging.info("============================")

	@pytest.mark.run(order=96)
	def test_96_dig_query_for_arec1_dnssec_foo_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.dnssec.foo.com  when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.dnssec.foo.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.dnssec.foo.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'arec1.dnssec.foo.com IN A response: NOERROR',out1)
                logging.info("Test Case 96 Execution Completed")

	@pytest.mark.run(order=97)
	def test_97_dig_query_for_arec1_non_dnssec_foo_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.non_dnssec.foo.com when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.non_dnssec.foo.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.non_dnssec.foo.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                #assert re.search(r'validating arec1.non_dnssec.test.com\/A: must be secure failure',out1)
                assert re.search(r'info must-be-secure resolving \'arec1.non_dnssec.foo.com/A/IN\'',out1)
                logging.info("Test Case 97 Execution Completed")
	
	@pytest.mark.run(order=98)
	def test_98_dig_query_for_IPV4_PTR_30_0_0_1_record(self):
                logging.info("Perform dig command for 'IPV4 PTR' record 1.0.0.30.in-addr.arpa  when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.30.in-addr.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.30.in-addr.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'1.0.0.30.in-addr.arpa IN PTR response: NOERROR',out1)
                logging.info("Test Case 98 Execution Completed")

	@pytest.mark.run(order=99)
	def test_99_dig_query_for_IPV4_PTR_30_1_0_1_record(self):
                logging.info("Perform dig command for 'IPV4 PTR' non-dnssec record 1.0.1.30.in-addr.arpa when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.1.30.in-addr.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.1.30.in-addr.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'info must-be-secure resolving \'1.0.1.30.in-addr.arpa/PTR/IN\'',out1)
                logging.info("Test Case 99 Execution Completed")

	@pytest.mark.run(order=100)
	def test_100_dig_query_for_IPV6_PTR_2000_1_record(self):
                logging.info("Perform dig command for 'IPV6 PTR' record 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.ip6.arpa when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.ip6.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.ip6.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.ip6.arpa IN PTR response: NOERROR',out1)
                logging.info("Test Case 100 Execution Completed")

	@pytest.mark.run(order=101)
	def test_101_dig_query_for_IPV6_PTR_2000_1_1_record(self):
                logging.info("Perform dig command for non-dnssec 'IPV6 PTR' record 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.2.ip6.arpa when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.2.ip6.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.2.ip6.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'info must-be-secure resolving \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.2.ip6.arpa/PTR/IN\'',out1)
                logging.info("Test Case 101 Execution Completed")

# Test DNSSEC secure feature at DNS view level 

	@pytest.mark.run(order=102)
        def test_102_Modify_dns_view_object_to_set_allow_recursive_queries_global_forwarder_trust_anchor(self):
                logging.info("Modify_DNS_view_object_to_set_trust_anchor and custom root name server as grid2 in grid dns properties editor")
                get_ref = ib_NIOS.wapi_request('GET', object_type="view")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref1 = json.loads(get_ref)[0]['_ref']
                print ref1

# Export keys for FMZ from grid2 to add to grid1
		get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth",  params="?fqdn=bar.com")
                logging.info(get_ref)
                res2 = json.loads(get_ref)
                ref2 = json.loads(get_ref)[0]['_ref']
                print ref2

                data_fmz_trust = {"operation" : "EXPORT_ANCHORS"}
                get_ref = ib_NIOS.wapi_request_2('POST', object_type = ref2 +"?_function=dnssec_export", fields=json.dumps(data_fmz_trust))
                logging.info(get_ref)
                response_fmz = json.loads(get_ref)
                token_fmz = response_fmz['token']
                url_fmz = response_fmz['url']
                cmd = "curl -k1 -u admin:infoblox  -H \"Content-Type: application/force-download\" -O " + str(url_fmz)
                response_fmz = commands.getoutput(cmd)

                cmd = "curl -k1 -u admin:infoblox -H \"Content-Type: application/json\" -X POST \"https://config.grid2_fqdn/wapi/v2.9/fileop?_function=downloadcomplete\" -d '{\"token\": token}'"
                response_fmz = commands.getoutput(cmd)
                with    open("trust_anchors.txt", "r") as fin:
                        val = fin.read()
		print "################ Trust Anchor of FMZ Start #################\n"
                print val
		print "################ Trust Anchor of FMZ End #################\n"
                arr_list = val.split()
                token_fmz = arr_list[4].lstrip('"')
                token_fmz = token_fmz.rstrip('";')

# Export keys for IPV4 RMZ from grid2 to add to grid1
		get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth",  params="?fqdn=40.0.0.0/8")
                logging.info(get_ref)
                res3 = json.loads(get_ref)
                ref3 = json.loads(get_ref)[0]['_ref']
                print ref3

                data_ipv4_rmz_trust = {"operation" : "EXPORT_ANCHORS"}
                get_ref = ib_NIOS.wapi_request_2('POST', object_type = ref3 +"?_function=dnssec_export", fields=json.dumps(data_ipv4_rmz_trust))
                logging.info(get_ref)
                response_ipv4_rmz = json.loads(get_ref)
                token_ipv4_rmz = response_ipv4_rmz['token']
                url_ipv4_rmz = response_ipv4_rmz['url']
                cmd = "curl -k1 -u admin:infoblox  -H \"Content-Type: application/force-download\" -O " + str(url_ipv4_rmz)
                response_ipv4_fmz = commands.getoutput(cmd)

                cmd = "curl -k1 -u admin:infoblox -H \"Content-Type: application/json\" -X POST \"https://config.grid2_fqdn/wapi/v2.9/fileop?_function=downloadcomplete\" -d '{\"token\": token}'"
                response_ipv4_rmz = commands.getoutput(cmd)
                with    open("trust_anchors.txt", "r") as fin:
                        val = fin.read()
		print "################ Trust Anchor of IPV4 RMZ Start #################\n"
                print val
		print "################ Trust Anchor of IPV4 RMZ End #################\n"
                arr_list = val.split()
                token_ipv4_rmz = arr_list[4].lstrip('"')
                token_ipv4_rmz = token_ipv4_rmz.rstrip('";')

# Export keys for IPV6 RMZ from grid2 to add to grid1
		get_ref = ib_NIOS.wapi_request_2('GET', object_type="zone_auth",  params="?fqdn=3000::/16")
                logging.info(get_ref)
                res4 = json.loads(get_ref)
                ref4 = json.loads(get_ref)[0]['_ref']
                print ref4

                data_ipv6_rmz_trust = {"operation" : "EXPORT_ANCHORS"}
                get_ref = ib_NIOS.wapi_request_2('POST', object_type = ref4 +"?_function=dnssec_export", fields=json.dumps(data_ipv6_rmz_trust))
                logging.info(get_ref)
                response_ipv6_rmz = json.loads(get_ref)
                token_ipv6_rmz = response_ipv6_rmz['token']
                url_ipv6_rmz = response_ipv6_rmz['url']
                cmd = "curl -k1 -u admin:infoblox  -H \"Content-Type: application/force-download\" -O " + str(url_ipv6_rmz)
                response_ipv6_fmz = commands.getoutput(cmd)

                cmd = "curl -k1 -u admin:infoblox -H \"Content-Type: application/json\" -X POST \"https://config.grid2_fqdn/wapi/v2.9/fileop?_function=downloadcomplete\" -d '{\"token\": token}'"
                response_ipv6_rmz = commands.getoutput(cmd)
                with    open("trust_anchors.txt", "r") as fin:
                        val = fin.read()
		print "################ Trust Anchor of IPV6 RMZ Start #################\n"
                print val
		print "################ Trust Anchor of IPV6 RMZ End #################\n"
                arr_list = val.split()
                token_ipv6_rmz = arr_list[4].lstrip('"')
                token_ipv6_rmz = token_ipv6_rmz.rstrip('";')

# dnssec trust keys to add to grid1
		data = { "dnssec_enabled": True, "dnssec_trusted_keys": [{"algorithm": "8", "dnssec_must_be_secure": True, "fqdn": "bar.com","key": token_fmz, "secure_entry_point": True},{"algorithm": "8", "dnssec_must_be_secure": True, "fqdn": "40.in-addr.arpa","key": token_ipv4_rmz, "secure_entry_point": True},{"algorithm": "8", "dnssec_must_be_secure": True, "fqdn": "0.0.0.3.ip6.arpa","key": token_ipv6_rmz, "secure_entry_point": True}]}
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
                logging.info("Test Case 102 Execution Completed")
                logging.info("============================")

	@pytest.mark.run(order=103)
	def test_103_dig_query_for_arec1_dnssec_bar_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.dnssec.bar.com  when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.dnssec.bar.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.dnssec.bar.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'arec1.dnssec.bar.com IN A response: NOERROR',out1)
                logging.info("Test Case 103 Execution Completed")
		
	@pytest.mark.run(order=104)
	def test_104_dig_query_for_arec1_non_dnssec_bar_com_A_record(self):
                logging.info("Perform dig command for 'A' record arec1.non_dnssec.bar.com when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' arec1.non_dnssec.bar.com IN A +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'arec1.non_dnssec.bar.com\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                #assert re.search(r'validating arec1.non_dnssec.test.com\/A: must be secure failure',out1)
                assert re.search(r'info must-be-secure resolving \'arec1.non_dnssec.bar.com/A/IN\'',out1)
                logging.info("Test Case 104 Execution Completed")
	
	@pytest.mark.run(order=105)
	def test_105_dig_query_for_IPV4_PTR_40_0_0_1_record(self):
                logging.info("Perform dig command for 'IPV4 PTR' record 1.0.0.40.in-addr.arpa  when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.40.in-addr.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.40.in-addr.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'1.0.0.40.in-addr.arpa IN PTR response: NOERROR',out1)
                logging.info("Test Case 105 Execution Completed")

	@pytest.mark.run(order=106)
	def test_106_dig_query_for_IPV4_PTR_40_1_0_1_record(self):
                logging.info("Perform dig command for 'IPV4 PTR' non-dnssec record 1.0.1.40.in-addr.arpa when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.1.40.in-addr.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.1.40.in-addr.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'info must-be-secure resolving \'1.0.1.40.in-addr.arpa/PTR/IN\'',out1)
                logging.info("Test Case 106 Execution Completed")

	@pytest.mark.run(order=107)
	def test_107_dig_query_for_IPV6_PTR_3000_1_record(self):
                logging.info("Perform dig command for 'IPV6 PTR' record 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.3.ip6.arpa when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.3.ip6.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.3.ip6.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.3.ip6.arpa IN PTR response: NOERROR',out1)
                logging.info("Test Case 107 Execution Completed")

	@pytest.mark.run(order=108)
	def test_108_dig_query_for_IPV6_PTR_3000_1_1_record(self):
                logging.info("Perform dig command for non-dnssec 'IPV6 PTR' record 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.3.ip6.arpa when DNSSEC secure feature enabled and custom root name server as grid2 in grid dns properties editor")
                dig_cmd = 'dig @'+str(config.grid_vip)+' 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.3.ip6.arpa IN PTR +dnssec'
                dig_cmd1 = os.system(dig_cmd)
                logging.info("Validate Syslog afer perform queries")
                sys_log_validation = 'ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@'+str(config.grid_vip)+' " tail -3 /var/log/syslog | grep -ir \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.3.ip6.arpa\'"'
                out1 = commands.getoutput(sys_log_validation)
                print out1
                logging.info(out1)
                assert re.search(r'info must-be-secure resolving \'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.3.ip6.arpa/PTR/IN\'',out1)
                logging.info("Test Case 108 Execution Completed")

