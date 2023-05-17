import ConfigParser
import logging
import httplib
import json
import ssl
import config
from json import loads

#CONF="reporting_conf.ini"
#parser = ConfigParser.SafeConfigParser()
#parser.read(CONF)
#GRID_VIP = parser.get('NIOS', 'GRID_VIP')
#USERNAME = parser.get('NIOS', 'USERNAME')
#PASSWORD = parser.get('NIOS', 'PASSWORD')

GRIDVIP = config.grid_vip
USERNAME = config.username
PASSWORD = config.password

DEFAULT_OBJECT_TYPE = 'network'
URLENCODED = 'application/json'
DEFAULT_CONTENT_TYPE = URLENCODED
VERSION = config.wapi_version
PATH = '/wapi/v' + VERSION + '/'

#logging.basicConfig(filename='output.log',level=logging.DEBUG,filemode='w')

# WAPI Call methods

def wapi_request(operation, ref='', params='', fields='', \
                    object_type=DEFAULT_OBJECT_TYPE, \
                    content_type=DEFAULT_CONTENT_TYPE,user=USERNAME,password=PASSWORD,grid_vip=GRIDVIP):
    '''
    Send an HTTPS request to the NIOS server.
    '''
    # Create connection and request header.
    # This class does not perform any verification of the server`s certificate.
    conn = httplib.HTTPSConnection(grid_vip,context=ssl._create_unverified_context())
    auth_header = 'Basic %s' % (':'.join([user, password])
                                .encode('Base64').strip('\r\n'))
    request_header = {'Authorization':auth_header,
                      'Content-Type': content_type}
    if ref:
        url = PATH + ref
    else:
        url = PATH + object_type
    if params:
        url += params
    conn.request(operation, url, fields, request_header)
    response = conn.getresponse();
    if response.status >= 200 and response.status < 300:
        return handle_success(response)
    elif response.status == 400 or response.status == 404:
        return response.status,handle_success(response)
    else:
        return handle_exception(response)
    
def handle_exception(response):
    '''
    If there was encountered an error while performing requested action,
    print response code and error message.
    '''
    logging.info('Request finished with error, response code: %i %s'\
            % (response.status, response.reason))
    json_object = json.loads(response.read())
    logging.info('Error message: %s' % json_object['Error'])
    raise Exception('WAPI Error message: %s' % json_object['Error'])
    return json_object


def handle_success(response):
    '''
    If the action requested by the client was received, understood, accepted
    and processed successfully, print response code and return response body.
    '''
    logging.info('Request finished successfully with response code: %i %s'\
            % (response.status, response.reason))
    return response.read()

def handle_exception_negative_case(response):
    '''
    If there was encountered an error while performing requested action,
    print response code and error message.
    '''
    logging.info('Request finished with error, response code: %i %s'\
            % (response.status, response.reason))
    return response.status, response.read()

