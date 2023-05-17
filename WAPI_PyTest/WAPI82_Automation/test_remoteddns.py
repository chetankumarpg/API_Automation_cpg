import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class Remote_Ddns_Zone(unittest.TestCase):

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
        def test_create_remoteddnszone(self):
                logging.info("Create RemoteDdnsZone Test")
                data = {"name": "Testing","remote_forward_zones": [{"fqdn": "asm123.com","gss_tsig_dns_principal": "saklfjlk","gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.39.39.45"}]}
                response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")

	@pytest.mark.run(order=2)
        #Test the "fqdn" field in "remoteddnszone" structure
	def test_fqdn_remoteddnszone(self):
                logging.info("fqdn in RemoteDdnsZone Test")
                data = {"name": "Infoblox","remote_forward_zones": [{"gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.0.0.2"}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Required field missing: fqdn',response)
                logging.info("Test Case 2 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=3)
	def test_gss_tsig_dns_principal_remoteddnszone(self):
		logging.info("gss_tsig_dns_principal in RemoteDdnsZone Test")
		data = {"name": "ASM","remote_forward_zones": [{"fqdn": "asm123.com","gss_tsig_dns_principal": 123,"gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.0.0.2"}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print status
                print response
		logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for gss_tsig_dns_principal: 123: Must be string type',response)
                logging.info("Test Case 3 Execution Completed")
                logging.info("============================")

	@pytest.mark.run(order=4)
	def test_gss_tsig_domain_remoteddnszone(self):
                logging.info("gss_tsig_domain in RemoteDdnsZone Test")
                data = {"name": "Infoblox","remote_forward_zones": [{"fqdn": "asm123.com","gss_tsig_dns_principal": "test","gss_tsig_domain": 1234,"key_type": "GSS-TSIG","server_address": "10.0.0.2"}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for gss_tsig_domain: 1234: Must be string type',response)
                logging.info("Test Case 4 Execution Completed")
                logging.info("============================")

	@pytest.mark.run(order=5)
	def test_key_type_remoteddnszone(self):
                logging.info("key_type in RemoteDdnsZone Test")
                data = {"name": "Infoblox","remote_forward_zones": [{"fqdn": "asm123.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "ASM","server_address": "10.0.0.2"}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for key_type',response)
                logging.info("Test Case 5 Execution Completed")
                logging.info("============================")


	@pytest.mark.run(order=6)
	def test_server_address_remoteddnszone(self):
                logging.info("Test server_address field in RemoteDdnsZone")
                data = {"name": "Infoblox","remote_forward_zones": [{"fqdn": "asm123.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "ASM"}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Required field missing: server_address',response)
                logging.info("Test Case 6 Execution Completed")
                logging.info("============================")	

        @pytest.mark.run(order=7)
        def test_server_address_type_remoteddnszone(self):
                logging.info("Test server_address field type in RemoteDdnsZone")
                data = {"name": "Infoblox","remote_forward_zones": [{"fqdn": "asm123.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.39.A.45"}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for server_address:',response)
                logging.info("Test Case 7 Execution Completed")
                logging.info("============================")	


	
        @pytest.mark.run(order=8)
        def test_tsig_key_remoteddnszone(self):
                logging.info("Test tsig_key field type in RemoteDdnsZone")
                data = {"name": "Testing","remote_forward_zones": [{"fqdn": "asm123.com","gss_tsig_dns_principal": "saklfjlk","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.39.39.45","tsig_key": 1234,"tsig_key_alg": "HMAC-MD5","tsig_key_name": "test"}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for tsig_key: 1234: Must be string type',response)
                logging.info("Test Case 8 Execution Completed")
                logging.info("============================")

        @pytest.mark.run(order=9)
        def test_tsig_key_alg_remoteddnszone(self):
                logging.info("Test tsig_key_alg field type in RemoteDdnsZone")
                data = {"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.0.0.2","tsig_key": "lDenNrBKS7JMqodB0I703ldthZloYcwMycdS4vqWiOY=","tsig_key_alg": "true","tsig_key_name": "test"}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for tsig_key_alg',response)
                logging.info("Test Case 9 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=10)
        def test_tsig_key_name_remoteddnszone(self):
                logging.info("Test tsig_key_name field type in RemoteDdnsZone")
                data = {"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.0.0.2","tsig_key": "lDenNrBKS7JMqodB0I703ldthZloYcwMycdS4vqWiOY=","tsig_key_alg": "HMAC-MD5","tsig_key_name": 12345}]}
                status,response = ib_NIOS.wapi_request('POST', object_type="networkview", fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Invalid value for tsig_key_name: 12345: Must be string type',response)
                logging.info("Test Case 10 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=11)
        def test_DELETE_remoteddnszone(self):
		logging.info("Test Deletinf the neworkview")
                get_ref = ib_NIOS.wapi_request('GET', object_type="networkview")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[1]['_ref']
                print ref
                logging.info("Deleting the Networkview Testing")
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




