########################################################################
#                                                                      #
# Copyright (c) Infoblox Inc., 2019                                    #
#                                                                      #
########################################################################
#
# File: dig_utility.py
#
# Description:
#     Performs Dig query on the given records.
#
#
# Input Options:
#        import dig_utility as dig
#	 dig(record_name,auth_zone,record_type,LookFor)
#  Output:
#    0: Test success
#    1: Test failed
#
# Author: Rajeev Patil
#
#
# History:
#    21/02/2019 (Rajeev Patil) - Created
########################################################################


import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS
import sys
import config
import re



def dig(record_name,zone_name,record_type,LookFor):
    if  record_type in "any":
        logging.info("Perform query by considering record type as ANY ")
        dig_cmd = 'dig @'+str(config.grid_vip)+' '+str(record_name)+str('.'+zone_name['fqdn'])+str(' IN ')+"ANY"
        logging.info (dig_cmd)
        result = subprocess.check_output(dig_cmd,shell=True)
        logging.info (result)
        read=re.findall(result,LookFor)
        for read in result:
            assert True
        logging.info ("Dig Query Successful for your records")
    elif (record_type in ('rp','hinfo','ipseckey','apl','afsdb','dlv','sshfp','loc','cert','cds')):
        logging.info("Perform query by considering your record type")
        dig_cmd = 'dig @'+str(config.grid_vip)+' '+str(record_name)+str('.'+zone_name['fqdn'])+str(' IN ')+str(record_type)
        logging.info (dig_cmd)
        result = subprocess.check_output(dig_cmd,shell=True)
        logging.info (result)
        status="NOERROR"
        noerror=re.findall(result,status)
        for noerror in result:
            read=re.findall(result,LookFor)
            for read in result:
                assert True
        logging.info ("Dig Query Successful for your record type")
    elif (record_type in ('ns','soa','a','aaaa','cname','dname','mx','srv','naptr','txt','ptr','axfr','nsec','rrsig','dnskey')):
        dig_cmd = 'dig @'+str(config.grid_vip)+' '+str(record_name)+str('.'+zone_name['fqdn'])+str(' IN ')+str(record_type)
        logging.info (dig_cmd)
        result = subprocess.check_output(dig_cmd,shell=True)
        logging.info (result)
        status="NOERROR"
        noerror=re.findall(result,status)
        read=re.findall(result,LookFor)
        for noerror in result:
            for read in result:
                assert True
        logging.info ("Dig Query Successful for your requested record type")
    else:
          logging.info ("Database Type Error","Validation type not recognized, please use either \"ns\", \"soa\", \"a\", \"aaaa\",\"cname\",\"dname\",\"mx\",,\"srv\",\"txt\",\"naptr\",\"ptr\",\"NSEC\",\"RRSIG\",\"axfr")        


