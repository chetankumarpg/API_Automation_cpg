import re
import config
import pytest
import unittest
import logging
import subprocess
import json
from time import sleep
import ib_utils.ib_NIOS as ib_NIOS
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
    def test_1_Get_operation_to_read_discoverytask_object(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        search_record_nsec = ib_NIOS.wapi_request('GET', object_type="discoverytask")
        response = json.loads(search_record_nsec)
        print response
        var= False
        if len(response)==2:
            for i in response:
                if i["discovery_task_oid"] in ["current","scheduled"] and i["member_name"] in [config.grid_fqdn]:
                    var=True

        assert var
        logging.info("Test Case 1 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=2)
    def test_2_create_discoverytask_object_N(self):
        logging.info("create_discoverytask_object_N")
        status,response1 = ib_NIOS.wapi_request('POST', object_type="discoverytask")
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation create not allowed for discoverytask',response1)
        logging.info("Test Case 2 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=3)
    def test_3_Delete_discoverytask_object_N(self):
        logging.info("Delete_discoverytask_object_N")
        status,response1 = ib_NIOS.wapi_request('DELETE', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current')
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Operation delete not allowed for discoverytask',response1)
        logging.info("Test Case 3 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=4)
    def test_4_Modify_discoverytask_object_N(self):
        logging.info("Modify_discoverytask_object_N")
	data = {"name": "bind_dname.domain.com","target": "target.org"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current',params="?_schedinfo.scheduled_time=2123235895", fields= json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'discoverytask does not support scheduling.',response1)
        logging.info("Test Case 4 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=5)
    def test_5_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data = {"state": "COMPLETE"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: state',response1)
        logging.info("Test Case 5 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=6)
    def test_6_Modify_discoverytask_object_N(self):
        logging.info("Modify_discoverytask_object_N")
	data = {"state": "COMPLETE"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields= json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: state',response1)
        logging.info("Test Case 6 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=7)
    def test_7_Modify_discoverytask_object_N(self):
        logging.info("Modify_discoverytask_object_N")
	data = {"state_time": "COMPLETE"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields= json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: state_time',response1)
        logging.info("Test Case 7 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=8)
    def test_8_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data = {"state": "COMPLETE"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: state',response1)
        logging.info("Test Case 8 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=9)
    def test_9_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data = {"status": "COMPLETE"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: status',response1)
        logging.info("Test Case 9 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=10)
    def test_10_Modify_discoverytask_object_N(self):
        logging.info("Modify_discoverytask_object_N")
	data = {"status": "Current status: Ended\n\n Discovered: 0\n Pending processing: 0\n Managed: 0\n Unmanaged: 0\n Conflicts: 0\n\n Existing object updated with discovery data: 0"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields= json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: status',response1)
        logging.info("Test Case 10 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=11)
    def test_11_Modify_discoverytask_object_N(self):
        logging.info("Modify_discoverytask_object_N")
	data = {"status_time":""}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields= json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not writable: status_time',response1)
        logging.info("Test Case 11 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=12)
    def test_12_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data = {"status_time": "COMPLETE"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: status_time',response1)
        logging.info("Test Case 12 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=13)
    def test_13_Modify_the_discoverytask_object_with_mode(self):
        logging.info("Modify_the_discoverytask_object_with_mode")
        data = {"mode":""}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for mode .*.* valid values are: FULL, ICMP, NETBIOS, TCP, CSV",response1)
        logging.info("Test Case 13 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=14)
    def test_14_create_discoverytask_with_modify_mode(self):
        logging.info("Create discoverytask with required fields")
        data = {"mode":"FULL"}
        response = ib_NIOS.wapi_request('PUT', ref = "discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=15)
    def test_15_create_discoverytask_with_modify_mode(self):
        logging.info("Create discoverytask with required fields")
        data = {"mode":"ICMP"}
        response = ib_NIOS.wapi_request('PUT', ref = "discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=16)
    def test_16_create_discoverytask_with_modify_mode(self):
        logging.info("Create discoverytask with required fields")
	data = {"mode":"NETBIOS"}
        response = ib_NIOS.wapi_request('PUT', ref = "discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current",fields=json.dumps(data))
        logging.info("============================")
        print response
		
		
    @pytest.mark.run(order=17)
    def test_17_create_discoverytask_with_modify_mode(self):
        logging.info("Create discoverytask with required fields")
        data = {"mode":"TCP"}
        response = ib_NIOS.wapi_request('PUT', ref = "discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current",fields=json.dumps(data))
        logging.info("============================")
        print response
		
    @pytest.mark.run(order=18)
    def test_18_create_discoverytask_with_modify_mode(self):
        logging.info("Create discoverytask with required fields")
        data = {"mode":"CSV"}
        response = ib_NIOS.wapi_request('PUT', ref = "discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current",fields=json.dumps(data))
        logging.info("============================")
        print response	


    @pytest.mark.run(order=19)
    def test_19_Modify_the_discoverytask_object_with_mode(self):
        logging.info("Modify_the_discoverytask_object_with_mode")
        data = {"mode":"%20CSV"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for mode .*%20CSV.* valid values are: FULL, ICMP, NETBIOS, TCP, CSV",response1)
        logging.info("Test Case 19 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=20)
    def test_20_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data ={"mode": "COMPLETE"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: mode',response1)
        logging.info("Test Case 20 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=21)
    def test_21_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data = {"network_view":"null"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: network_view',response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=22)
    def test_22_Modify_discoverytask_object_N(self):
        get_ref = ib_NIOS.wapi_request('GET', object_type="discoverytask")
        logging.info(get_ref)
        res = json.loads(get_ref)
        ref = json.loads(get_ref)[0]['_ref']
        print ref
        logging.info("Modify_discoverytask_object_N")
	data = {"network_view": "null"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = ref, fields= json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 404 and re.search(r'AdmConDataNotFoundError: Network View null not found',response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")



    @pytest.mark.run(order=23)
    def test_23_create_discoverytask_with_modify_network_view(self):
        logging.info("Create discoverytask with network_view field")
        data = {"network_view":"defa"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = "discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current",fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 404 and re.search(r'AdmConDataNotFoundError: Network View defa not found',response1)
        logging.info("Test Case 22 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=24)
    def test_24_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data = {"networks":"networks"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: networks',response1)
        logging.info("Test Case 21 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=25)
    def test_25_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data = {"tcp_ports":"commen"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tcp_ports',response1)
        logging.info("Test Case 25 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=26)
    def test_26_Modify_discoverytask_object_N(self):
        logging.info("Modify_discoverytask_object_N")
	data = {"tcp_ports":{"comment": "kdm","number": 1024}}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields= json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'List value expected for field: tcp_ports',response1)
        logging.info("Test Case 26 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=27)
    def test_27_create_discoverytask_with_modify_tcp_ports(self):
        logging.info("Create discoverytask with tcp_ports field")
        data = {"tcp_ports":[{"comment": "kdm","number": 1024}]}
        response = ib_NIOS.wapi_request('PUT', ref = "discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=28)
    def test_28_Modify_the_discoverytask_object_with_networks(self):
        logging.info("Modify_the_discoverytask_object_with_networks")
        data = {"tcp_ports":[{"comment": "kdm","number": ""}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for number.*.* Must be integer type",response1)
        logging.info("Test Case 28 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=29)
    def test_29_Modify_the_discoverytask_object_with_networks(self):
        logging.info("Modify_the_discoverytask_object_with_networks")
        data = {"tcp_ports":[{"comment": 123,"number": 1024}]}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for comment: 123: Must be string type",response1)
        logging.info("Test Case 29 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=30)
    def test_30_Modify_the_discoverytask_object_with_tcp_scan_technique(self):
        logging.info("Modify_the_discoverytask_object_with_tcp_scan_technique")
        data = {"tcp_scan_technique": "SY"}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for tcp_scan_technique .*.* valid values are: SYN, CONNECT",response1)
        logging.info("Test Case 30 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=31)
    def test_31_create_discoverytask_with_modify_tcp_scan_technique(self):
        logging.info("Create discoverytask with tcp_scan_technique field")
        data = {"tcp_scan_technique": "CONNECT"}
        response = ib_NIOS.wapi_request('PUT', ref = "discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=32)
    def test_32_create_discoverytask_with_modify_tcp_scan_technique(self):
        logging.info("Create discoverytask with tcp_scan_technique field")
        data = {"tcp_scan_technique": "SYN"}
        response = ib_NIOS.wapi_request('PUT', ref = "discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=33)
    def test_33_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data = {"tcp_scan_technique":"CONNECT"}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: tcp_scan_technique',response1)
        logging.info("Test Case 33 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=34)
    def test_34_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data = {"ping_retries":2}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ping_retries',response1)
        logging.info("Test Case 34 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=35)
    def test_35_Modify_the_discoverytask_object_with_ping_retries(self):
        logging.info("Modify_the_discoverytask_object_with_ping_retries")
        data = {"ping_retries": 6}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"ping_retries must be between 1 and 5",response1)
        logging.info("Test Case 35 Execution Completed")
        logging.info("============================")
    @pytest.mark.run(order=36)
    def test_36_Modify_the_discoverytask_object_with_ping_retries(self):
        logging.info("Modify_the_discoverytask_object_with_ping_retries")
        data = {"ping_retries":""}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for ping_retries.*.* Must be integer type",response1)
        logging.info("Test Case 36 Execution Completed")
        logging.info("============================")


    @pytest.mark.run(order=37)
    def test_37_create_discoverytask_with_modify_ping_retries(self):
        logging.info("Create discoverytask with ping_retries field")
        data = {"ping_retries": 4}
        response = ib_NIOS.wapi_request('PUT', ref = "discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current",fields=json.dumps(data))
        logging.info("============================")
        print response

    @pytest.mark.run(order=38)
    def test_38_Modify_the_discoverytask_object_with_ping_timeout(self):
        logging.info("Modify_the_discoverytask_object_with_ping_timeout")
        data = {"ping_timeout":""}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Invalid value for ping_timeout.*.* Must be integer type",response1)
        logging.info("Test Case 38 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=39)
    def test_39_Modify_the_discoverytask_object_with_ping_timeout_N(self):
        logging.info("Modify_the_discoverytask_object_with_ping_timeout")
        data = {"ping_timeout":12365456}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"ping_timeout must be between 5 and 4000",response1)
        logging.info("Test Case 39 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=40)
    def test_40_create_discoverytask_with_modify_ping_timeout(self):
        logging.info("Create discoverytask with ping_timeout field")
        data = {"ping_timeout":122}
        response = ib_NIOS.wapi_request('PUT', ref = "discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current",fields=json.dumps(data))
        logging.info("============================")
        print response


    @pytest.mark.run(order=41)
    def test_41_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data = {"ping_timeout":121}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: ping_timeout',response1)
        logging.info("Test Case 41 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=42)
    def test_42_Modify_the_discoverytask_object_with_warning_N(self):
        logging.info("Modify_the_discoverytask_object_with_warning")
        data = {"warning":122}
        status,response1 = ib_NIOS.wapi_request('PUT', ref = 'discoverytask/ZG5zLmRpc2NvdmVyeV90YXNrJGN1cnJlbnQ:current', fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r"Field is not writable: warning",response1)
        logging.info("Test Case 42 Execution Completed")
        logging.info("============================")

    @pytest.mark.run(order=43)
    def test_43_Get_operation_to_read_discoverytask_object_N(self):
        logging.info("Get_operation_to_read_discoverytask_object")
        data = {"warning":121}
        status,response1 = ib_NIOS.wapi_request('GET', object_type="discoverytask", fields=json.dumps(data))
        print status
        print response1
        logging.info(response1)
        assert  status == 400 and re.search(r'Field is not searchable: warning',response1)
        logging.info("Test Case 43 Execution Completed")
        logging.info("============================")
    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logging.info("TEAR DOWN METHOD")
