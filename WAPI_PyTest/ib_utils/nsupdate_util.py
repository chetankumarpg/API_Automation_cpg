import re
import pytest
import unittest
import logging
import subprocess
import os
import json
import ib_utils.ib_NIOS as ib_NIOS
from time import sleep
import commands
import json, ast
import requests
import time
import pexpect
import getpass
import sys
import config
#auth_zone={"fqdn": "manoj990.com"}
    
def nsupdate_add(name,ttl,record_type,zone,record_data):
    child = pexpect.spawn ('ssh -o StrictHostKeyChecking=no root@'+config.client_ip)
    child.logfile=sys.stdout 
    child.expect (':')
    child.sendline ('infoblox')
    #child.sendline('ls -ltr')
    child.sendline ('nsupdate')
    child.expect ('>')
    child.sendline ('server '+config.grid_vip)
    child.expect ('>')
    child.sendline (('update add '+ ' '+str(name)+'.'+str(zone)+' '+str(ttl)+' '+str(record_type)+' '+str(record_data)))
    child.expect ('>')
    child.sendline ('send')
    child.expect ('>')
    


#nsupdate_add('arun','1800','IPSECKEY',auth_zone['fqdn'],'10 0 1 . AAIBAQEBIgEDUVN5hu01UztgZEeO7rJ7W9dNrhSbboG6OgUhr4KreAE=')
