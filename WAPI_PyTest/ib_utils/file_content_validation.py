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



class CalledProcessError(Exception):
    """This exception is raised when a process run by check_call() or
    check_output() returns a non-zero exit status.
    The exit status will be stored in the returncode attribute;
    check_output() will also store the output in the output attribute.
    """
    def __init__(self, returncode, cmd, output=None):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
    def __str__(self):
        return self.returncode
	
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



def log_validation (string,file_path,IP_address,Host_address=host_ip):
    file_name='_'.join(file_path.split('/'))
    print ("file_name :",file_name)
    if (Host_address == host_ip ):
        #command1='egrep -i \"'+string +'" /tmp/'+ str(IP_address)+file_name+'.log'
        try:
            command1='egrep -i \"{0}\" /tmp/{1}{2}'.format(string, IP_address,file_name) 
            logging.info(command1)
            result=subprocess.check_output(command1,shell=True)
            logging.info (result.decode("utf-8"))
            return result
            if (result!=None):
                logging.info ("Requested Logs Present")
            else:
                logging.info ("Requested Logs not found")
        except subprocess.CalledProcessError as e:     
            logging.info (e.returncode)        
    else:
        try:
            logging.info ("Checking Log Info")
            connection=SSH(str(IP_address))
            command1='cat /tmp/'+ str(IP_address)+file_name+'| egrep -i '+string
            command1='cat /tmp/{0}{1} | egrep -i \"{3}\"'.format(IP_address,file_name,string)
            logging.info (command1)
            result=connection.send_command(command1)
            logging.info (result)
            return result
            if (result!=None):
                logging.info ("Requested Logs Present")
            else:
                logging.info ("Requested Logs not found")
        except subprocess.CalledProcessError as e:     
            logging.info (e.returncode)



#check=log_validation("Arun|ADD for 'arec'","/var/log/syslog","10.35.111.6") #(LookFor String,file_path,grid_ip)
#print check
