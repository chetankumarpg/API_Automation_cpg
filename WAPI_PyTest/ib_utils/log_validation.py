########################################################################
#                                                                      #
# Copyright (c) Infoblox Inc., 2019                                    #
#                                                                      #
########################################################################
#
# File: log_validation.py
#
# Description:
#     Check the given config file contains the given pattern.
#
#
# Input Options:
#        import log_validation as logv
#	 logv.log_validation(".*ADD.*DLV.*","/var/log/syslog",config.grid_vip) (LookFor String,file_path,grid_ip)
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

from paramiko import client
import paramiko
import os
import sys
import config
import socket
import subprocess
import logging

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)



class grep(Exception):
    pass
    
class SSH:
    client=None

    def __init__(self,address):
        logging.info ("Log Validation Script")
        logging.info ("connecting to server \n : ", address)
        self.client=client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
        mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
        self.client.connect(address, username='root', pkey = mykey)
        
            
    def send_command(self,command):
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            result=stdout.read()
            return result
        else:
            logging.info("Connection not opened.")



def log_validation (string,file_path,IP_address, Host_address=host_ip):
    file_name='_'.join(file_path.split('/'))
    if (Host_address == host_ip ):
        command1='grep -i '+string +' /tmp/'+ str(IP_address)+file_name+'.log'
        print(command1)
        result=subprocess.check_output(command1,shell=True)
        print (result.decode("utf-8"))
        if (result!=None):
            logging.info ("Requested Logs Present")
        else:
            logging.info ("Requested Logs not found")
    else:
        try:
            logging.info ("Checking Log Info")
            connection=SSH(str(IP_address))
            command1='cat /tmp/'+ str(IP_address)+file_name+'.log'+'| grep -i '+string
            print (command1)
            result=connection.send_command(command1)
            print (result)
            if (result!=None):
                logging.info ("Requested Logs Present")
            else:
                logging.info ("Requested Logs not found")
        except grep:
            logging.info ("Pattern not found")




