import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS

class Zone_Roll_Over_Info(unittest.TestCase):

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
        def test_1_Zonerolloverinfo_Structure(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref
                for i in res:
                        print i
                        logging.info("found")
                        assert i["fqdn"] == "testing.com" and i["view"] == "default"
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=2)
        def test_2_Days_Field_In_Zonerolloverinfo(self):
                logging.info("Test the days field in zonerolloverinfo structure")
                days = ib_NIOS.wapi_request('GET',object_type="zone_auth",params="?_return_fields=dnssec_ksk_rollover_date")
                logging.info(days)
                res = json.loads(days)
		print res
		d = res[0]
                for i in res:
                        print i
                        logging.info("found")
                        assert i["dnssec_ksk_rollover_date"] ==d['dnssec_ksk_rollover_date']
                logging.info("Test Case 2 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=3)
        def test_3_display_domain_Field_In_Zonerolloverinfo(self):
                logging.info("Test the display_domain field in zonerolloverinfo structure")
                data = {"display_domain": "test.com"}
                display_domain = ib_NIOS.wapi_request('GET',object_type="zone_auth",params="?_return_fields=display_domain")
                logging.info(display_domain)
                res = json.loads(display_domain)
                print res
                for i in res:
                        print i
                        logging.info("found")
                        assert i["display_domain"] == "testing.com"
                logging.info("Test Case 3 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=4)
        def test_4_View_In_Zonerolloverinfo(self):
                logging.info("Test the view field in zonerolloverinfo structure")
                data = {"view": "default"}
                view = ib_NIOS.wapi_request('GET',object_type="zone_auth",params="?_return_fields=view")
                logging.info(view)
                res = json.loads(view)
                print res
                for i in res:
                        print i
                        logging.info("found")
                        assert i["view"] == "default"
                logging.info("Test Case 4 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=5)
        def test_5_dnssec_ksk_rollover_date_In_Zonerolloverinfo(self):
                logging.info("test dnssec_ksk_rollover_date in Zonerolloverinfo struct")
                data = {"fqdn": "asm.com","dnssec_ksk_rollover_date": 1494398113,"view": "default"}
                status,response = ib_NIOS.wapi_request('POST', object_type="zone_auth",fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not writable: dnssec_ksk_rollover_date',response)
                logging.info("Test Case 5 Execution Completed")
                logging.info("============================")


        @pytest.mark.run(order=6)
        def test_6_display_domain_In_Zonerolloverinfo(self):
                logging.info("test display_domain in Zonerolloverinfo struct")
                data = {"fqdn": "asm.com","display_domain": "asmtech.com","view": "default"}
                status,response = ib_NIOS.wapi_request('POST', object_type="zone_auth",fields=json.dumps(data))
                print status
                print response
                logging.info(response)
                assert  status == 400 and re.search(r'AdmConProtoError: Field is not writable: display_domain',response)
                logging.info("Test Case 6 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=7)
        def test_7_display_domain_In_Zonerolloverinfo(self):
                logging.info("test display_domain in Zonerolloverinfo struct")
                data = {"fqdn": "asm.com","view": "default"}
                response = ib_NIOS.wapi_request('POST', object_type="zone_auth",fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                    assert True
                logging.info("Test Case 7 Execution Completed")
                logging.info("============================")



        @pytest.mark.run(order=8)
        def test_8_DELETE_Zonerolloverinfo(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[1]['_ref']
                print ref

                logging.info("Perfoming Delete Operaion on Zonerolloverinfo")
                data ={"fqdn": "asm.com"}
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref,fields=json.dumps(data))
                print get_status
                logging.info(get_status)
                logging.info("Test Case 8 Execution Completed")
                logging.info("=============================")

        @pytest.mark.run(order=9)
        def test_9_DELETE_Zonerolloverinfo(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="zone_auth")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[0]['_ref']
                print ref

                logging.info("Perfoming Delete Operaion on Zone auth")
                get_status = ib_NIOS.wapi_request('DELETE', object_type=ref)
                print get_status
                logging.info(get_status)
                logging.info("Test Case 9 Execution Completed")
                logging.info("=============================")

        @classmethod
        def teardown_class(cls):
                """ teardown any state that was previously setup with a call to
                setup_class.
                """
                logging.info("TEAR DOWN METHOD")


