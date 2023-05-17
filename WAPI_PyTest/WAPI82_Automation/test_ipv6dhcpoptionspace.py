import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class Ipv6_ipv6dhcp_option_range(unittest.TestCase):


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
        def test_create_ipv6dhcpoptionspace(self):
                logging.info("Create ipv6dhcpoptionspace Test")
                data = {"name": "dhcpv6optionrange1","enterprise_number": 433321}
                response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptionspace", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=2)
        #Test the "creation" of entry in "ipv6dhcpoptionspace" structure
        def test_duplicate_ipv6dhcpoptionspace(self):
                logging.info("creating ipv6dhcpoptionspace Test")
                data = {"name": 123,"enterprise_number": 433321}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptionspace", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for name: 123: Must be string type',response)
                logging.info("Test Case 2 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=3)
        def test_name_ipv6dhcpoptionspace(self):
                logging.info("name in ipv6dhcpoptionspace Test")
                data ={"name": "asm"}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptionspace", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: field for create missing: enterprise_number',response)
                logging.info("Test Case 3 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=4)
        def test_address_ipv6dhcpoptionspace(self):
                logging.info("address in ipv6dhcpoptionspace Test")
                data = {"name": "dhcpv6optionrange2","enterprise_number": True}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptionspace", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for enterprise_number: true: Must be integer type',response)
                logging.info("Test Case 4 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=5)
        def offset_ipv6dhcpoptionspace(self):
                logging.info("offset in ipv6dhcpoptionspace Test")
                data = {"name": "dhcpv6optionrange1","code": 2048,"comment":True}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptionspace", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for comment: true: Must be string type',response)
                logging.info("Test Case 5 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=6)
        def test_duplicate_name_ipv6dhcpoptionspace(self):
                logging.info("Test dupliacte name field in ipv6dhcpoptionspace")
                data = {"name": "dhcpv6optionrange1","enterprise_number": 433321}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptionspace", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConDataError: None',response)
                logging.info("Test Case 6 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=7)
        def test_get_ipv6dhcpoptionspace(self):
                logging.info("Get fetails using name ipv6dhcpoptionspace")
                data = {"name": "dhcpv6optionrange1"}
                response = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptionspace", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'200',response)
                for read in  response:
                        assert True
                logging.info("Test Case 7 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=8)
        def test_tsig_key_ipv6dhcpoptionspace(self):
                logging.info("Test tsig_key field type in ipv6dhcpoptionspace")
                data = {"name": "Testing","remote_forward_zones": [{"fqdn": "asm123.com","gss_tsig_dns_principal": "saklfjlk","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.39.39.45","tsig_key": 1234,"tsig_key_alg": "HMAC-MD5","tsig_key_name": "test"}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptionspace", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: field for create missing: enterprise_number',response)
                logging.info("Test Case 8 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=9)
        def test_tsig_key_alg_ipv6dhcpoptionspace(self):
                logging.info("Test tsig_key_alg field type in ipv6dhcpoptionspace")
                data = {"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.0.0.2","tsig_key": "lDenNrBKS7JMqodB0I703ldthZloYcwMycdS4vqWiOY=","tsig_key_alg": "true","tsig_key_name": "test"}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptionspace", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: field for create missing: enterprise_number',response)
                logging.info("Test Case 9 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=10)
        def test_tsig_key_name_ipv6dhcpoptionspace(self):
                logging.info("Test tsig_key_name field type in ipv6dhcpoptionspace")
                data = {"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.0.0.2","tsig_key": "lDenNrBKS7JMqodB0I703ldthZloYcwMycdS4vqWiOY=","tsig_key_alg": "HMAC-MD5","tsig_key_name": 12345}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="ipv6dhcpoptionspace", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: field for create missing: enterprise_number',response)
                logging.info("Test Case 10 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=11)
        def test_DELETE_ipv6dhcpoptionspace(self):
                logging.info("Test Deletinf the neworkview")
                get_ref = ib_NIOS.wapi_request('GET', object_type="ipv6dhcpoptionspace")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[1]['_ref']
                print ref
                logging.info("Deleting the ipv6dhcpoptionspace Testing")
                data ={"name": "Testing"}
                response = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
                print response
                logging.info(response)


        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")


