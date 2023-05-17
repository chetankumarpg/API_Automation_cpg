import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS
class smartfolder_personal(unittest.TestCase):

        @pytest.mark.run(order=1)
        def test_create_query_items(self):
                logging.info("Create query_items Test")
                data = {"query_items": [{"field_type": "EXTATTR","name": "Site","op_match": True,"operator": "EQ","value": {"value_string": "bang"},"value_type": "STRING"}]}
                response = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal", fields=json.dumps(data))
                logging.info(response)
                logging.info("============================")
                print response

        @pytest.mark.run(order=2)
        def test_create_csv_export(self):
                logging.info("Create csv_export Test")
                data = {"_object ":"smartfolder:global"}
                response = ib_NIOS.wapi_request('POST', object_type="smartfolder:personal", fields=json.dumps(data))
                logging.info(response)
                logging.info("============================")
                print response
