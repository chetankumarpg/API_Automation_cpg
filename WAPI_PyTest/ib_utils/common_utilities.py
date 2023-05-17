import re
import config
import pytest
import unittest
import logging
import os
import os.path
from os.path import join
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS



def generate_token_from_file(filepath, filename):
        dir_name=filepath
        base_filename=filename
        filename= os.path.join(dir_name, base_filename)
        data = {"filename":base_filename}
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
        return token

def get_object_reference(object_type,data):
	object_type1=object_type
        data = data
        get_ref = ib_NIOS.wapi_request('GET',object_type=object_type1,fields=json.dumps(data))
        logging.info(get_ref)
        res = json.loads(get_ref)
        ref = json.loads(get_ref)[0]['_ref']
        print res
        print ref
        return ref

