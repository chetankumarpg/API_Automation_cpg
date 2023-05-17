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
    def test_1_create_discovery_devicesupportbundle_object_N(self):
        logging.info("create_discovery_devicesupportbundle_object_N")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="discovery:devicesupportbundle")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for discovery:devicesupportbundle"',response1)
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=2)
    def test_2_Modify_the_discovery_devicesupportbundle_N(self):
        logging.info("Modify_the_discovery_devicesupportbundle_N")
        data = {"author": "infoblox","integrated_ind": True,"name": "Brocade-ICX745024-08_0_30cT213","version": "201608230000"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discovery:devicesupportbundle/Li5kZXZpY2Vfc3VwcG9ydF9idW5kbGUkQnJvY2FkZS1JQ1g3NDUwMjQtMDhfMF8zMGNUMjEz:Brocade-ICX745024-08_0_30cT213', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Operation update not allowed for discovery:devicesupportbundle",response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=3)
    def test_3_create_discovery_devicesupportbundle_object_N(self):
        logging.info("create_discovery_devicesupportbundle_object_N")
	data = {"_object":"discovery:devicesupportbundle"}
        status,response1 = ib_NIOS.wapi_request('POST', object_type="fileop", fields=json.dumps(data), params="?_function=csv_export")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'discovery:devicesupportbundle objects do not support CSV export.',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=4)
    def test_4_Get_operation_to_read_discovery_devicesupportbundle_object_N(self):
        logging.info("Get_operation_to_read_discovery_devicesupportbundle_object")
        data = {"author":"infoblox"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discovery:devicesupportbundle", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: author',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=5)
    def test_5_Get_operation_to_read_discovery_devicesupportbundle_object_N(self):
        logging.info("Get_operation_to_read_discovery_devicesupportbundle_object")
        data = {"integrated_ind":True}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discovery:devicesupportbundle", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: integrated_ind',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=6)
    def test_6_Get_operation_to_read_discovery_devicesupportbundle_object(self):
        logging.info("Get_operation_to_read_discovery_devicesupportbundle_object")
	data = {"name":"Brocade-ICX745024-08_0_30cT213"}
        search_discovery_devicesupportbundle = ib_NIOS.wapi_request('GET', object_type="discovery:devicesupportbundle", fields=json.dumps(data))
        response = json.loads(search_discovery_devicesupportbundle)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["author"] in ["infoblox"] and i["integrated_ind"] in [True] and i["name"] in ["Brocade-ICX745024-08_0_30cT213"] and i["version"] in ["201608230000"] :
                    var=True

        assert var
        logging.info("Test Case 6 Execution Completed")



    @pytest.mark.run(order=7)
    def test_7_Get_operation_to_read_discovery_devicesupportbundle_object(self):
        logging.info("Get_operation_to_read_discovery_devicesupportbundle_object")
	search_discovery_devicesupportbundle = ib_NIOS.wapi_request('GET', object_type="discovery:devicesupportbundle", params="?name:=brocade-icX745024-08_0_30cT213")
        response = json.loads(search_discovery_devicesupportbundle)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["author"] in ["infoblox"] and i["integrated_ind"] in [True] and i["name"] in ["Brocade-ICX745024-08_0_30cT213"] and i["version"] in ["201608230000"] :
                    var=True

        assert var
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")




    @pytest.mark.run(order=8)
    def test_8_Get_operation_to_read_discovery_devicesupportbundle_object(self):
        logging.info("Get_operation_to_read_discovery_devicesupportbundle_object")
        search_discovery_devicesupportbundle = ib_NIOS.wapi_request('GET', object_type="discovery:devicesupportbundle", params="?name~=Brocade-ICX745024-08_0_30cT2*")
        response = json.loads(search_discovery_devicesupportbundle)
        print response
        var= False
        if len(response)==1:
            for i in response:
                if i["author"] in ["infoblox"] and i["integrated_ind"] in [True] and i["name"] in ["Brocade-ICX745024-08_0_30cT213"] and i["version"] in ["201608230000"] :
                    var=True

        assert var
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=9)
    def test_9_Get_operation_to_read_discovery_devicesupportbundle_object_N(self):
        logging.info("Get_operation_to_read_discovery_devicesupportbundle_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discovery:devicesupportbundle", params="?name<=Brocade-ICX745024-08_0_30cT2*")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '<' not allowed for field: name",response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=10)
    def test_10_Get_operation_to_read_discovery_devicesupportbundle_object_N(self):
        logging.info("Get_operation_to_read_discovery_devicesupportbundle_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discovery:devicesupportbundle", params="?name>=Brocade-ICX745024-08_0_30cT2*")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Search modifier '>' not allowed for field: name",response1)
        logging.info("Test Case 10 execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=11)
    def test_11_Get_operation_to_read_discovery_devicesupportbundle_object_N(self):
        logging.info("Get_operation_to_read_discovery_devicesupportbundle_object")
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discovery:devicesupportbundle", params="?version=201608230000")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: version',response1)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")


    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")

