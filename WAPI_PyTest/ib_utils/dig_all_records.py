import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS
import sys
import config
import re


print ("Usage : Pass argument as dig ({fqdn:zone106.com})")

#zone={"fqdn":"zone106.com"}

def dig(zone_name,record_type):
    #records=[]
    record_list=[]
    print zone_name
    if record_type is None:
        print("Perform query for all records ")
        record_list=ib_NIOS.wapi_request('GET',object_type="allrecords?zone="+zone_name['fqdn'])
        record_list=json.loads(record_list)
        #print record_list
        for i in record_list:
            dig_cmd = 'dig @'+str(config.grid_vip)+' '+str(i['name'])+str('.'+zone_name['fqdn'])+str(' IN ')+str(i['name'])
            #print dig_cmd
            result = subprocess.check_output(dig_cmd,shell=True)
            #print result
            record_queried=str(i['name'])+str('.'+zone_name['fqdn'])+str(' IN ')+str(i['name'])
            assert re.search(record_queried,result)
            print ("Dig Query Successful for all records")
    else:
        print("Perform query for requested records ")
        if (record_type in ('rp','hinfo','ipseckey','apl','afsdb','dlv','sshfp','loc','cert','cds')):
            record_list=ib_NIOS.wapi_request('GET',object_type="record:unknown"+"?zone="+zone_name['fqdn'])
            record_list=json.loads(record_list)
            record_list=record_list[0]
            #print record_list 
            #print type(record_list)
            if (str(record_list['name'].split('.')[0]) == str(record_type)):
                dig_cmd = 'dig @'+str(config.grid_vip)+' '+str(record_list['name'])+str(' IN ')+str(record_type)
                #print dig_cmd
                result = subprocess.check_output(dig_cmd,shell=True)
                print result
                record_queried=str(record_list['name'])+str(' IN ')+str(record_type)
                #print (":::::::::::::::::::::",record_queried)
                #print (type(record_queried))
                #print type(result)
                assert re.search(record_queried,result)
                print ("Dig Query Successful for requested  records")
            else:
                print  ("Please check your record name and type")
        else:
            record_list=ib_NIOS.wapi_request('GET',object_type="record:"+str(record_type)+"?zone="+zone_name['fqdn'])
            record_list=json.loads(record_list)
            for i in record_list:
            #record_list=record_list[0]
            #print record_list
            #print type(record_list)
                print i
                dig_cmd = 'dig @'+str(config.grid_vip)+' '+str(i['name'])+str('.'+zone_name['fqdn'])+str(' IN ')+str(record_type)
                result = subprocess.check_output(dig_cmd,shell=True)
                print result
                record_queried=str(i['name'])+str('.'+zone_name['fqdn'])+str(' IN ')+str(record_type)
            #print (":::::::::::::::::::::",record_queried)
            #print (type(record_queried))
            #print type(result)
                assert re.search(record_queried,result)
                print ("Dig Query Successful for requested  records")
            

dig({"fqdn":"test.com"},"a")
