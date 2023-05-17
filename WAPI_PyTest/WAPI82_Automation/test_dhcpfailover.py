import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS
from time import sleep
class RangeTemplate(unittest.TestCase):



    @pytest.mark.run(order=1)
    def test_1_Enable_the_DHCP_service_to_Master_in_grid(self):
        logging.info("Enable_the_DHCP_service_to_Master_in_grid")
        data = {"enable_dhcp":True}
        response = ib_NIOS.wapi_request('PUT',ref='member:dhcpproperties/ZG5zLm1lbWJlcl9kaGNwX3Byb3BlcnRpZXMkMA:infoblox.localdomain',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=2)
    def test_2_Enable_the_DHCP_service_to_mumber_grid(self):
        logging.info("Enable_the_DHCP_service_to_mumber_grid")
        data = {"enable_dhcp":True}
        response = ib_NIOS.wapi_request('PUT',ref='member:dhcpproperties/ZG5zLm1lbWJlcl9kaGNwX3Byb3BlcnRpZXMkMQ:mem.com',fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response


    @pytest.mark.run(order=3)
    def test_3_Create_network_filed_in_grid_object(self):
        logging.info("Create_network_filed_in_grid_object")
        data = {"network":"10.0.0.0/8","network_view": "default"}
        response = ib_NIOS.wapi_request('POST',object_type='network', fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response

	
    @pytest.mark.run(order=4)
    def test_4_Create_primary_and_primary_server_type_fileds_in_dhcpfailover_object(self):
        logging.info("Create_primary_and_primary_server_type_fileds_in_dhcpfailover_object")
        data = {"name": "FA2","primary": "infoblox.localdomain","primary_server_type": "GRID","secondary": "mem.com","secondary_server_type": "GRID"}
        response = ib_NIOS.wapi_request('POST',object_type='dhcpfailover', fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response
	

	
    @pytest.mark.run(order=5)
    def test_5_Create_range_in_network_filed(self):
        logging.info("Create_range_in_network_filed")
        data = {"end_addr": "10.0.0.10","network": "10.0.0.0/8","network_view": "default","start_addr": "10.0.0.1"}
        response = ib_NIOS.wapi_request('POST',object_type='range', fields=json.dumps(data))
        logging.info(response)
        logging.info("============================")
        print response
			
    @pytest.mark.run(order=6)
    def test_6_DELETE_network(self):
         get_ref = ib_NIOS.wapi_request('GET', object_type="network")
         logging.info(get_ref)
         res = json.loads(get_ref)
         ref = json.loads(get_ref)[0]['_ref']
         print ref

         logging.info("Deleting the networkview Testing")
         get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
         print get_status
         logging.info(get_status)
         logging.info("Test Case 6 Execution Completed")
         logging.info("=============================")



    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")



