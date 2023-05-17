########################################################################
#                                                                      #
# Copyright (c) Infoblox Inc., 2019                                    #
#                                                                      #
########################################################################
#
# File: log_capture.py
#
# Description:
#     Captures log based on log path and Grid_IP using start(to start log capture) or stop (to stop log capture) functions.
#
#
# Input Options:
#	  start : 
#			log_action("start","/var/log/syslog",'10.35.113.14')
#	  stop :
#			log_action("stop","/var/log/syslog",'10.35.113.14')
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
import logging
from time import sleep
from paramiko import SSHClient
from scp import SCPClient
import subprocess

pid_list=[]
check_pid=[]
global host_name
global host_ip


host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

class tail(Exception):
    logging.info ("File not found please pass valid one")





class SSH:
    client=None

    def __init__(self,address):
        logging.info("connecting to server \n : ",address)
        self.client=client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
        mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
        self.client.connect(address, username='root', pkey = mykey)
            
    def send_command(self,command):
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            result=stdout.read()
            process_list=result.split(',')
            for i in process_list:
                process_id=i.split('\n')
                for i in process_id:
                    PID=i.split(' ')
                    try:
                        CPID=PID[5]
                        pid_list.append(CPID)
                    except IndexError:
                        pass
            return pid_list
        else:
            logging.info("Connection not opened.")




    def kill_command(self,check_pid,command):
        for i in check_pid:
            logging.info (i)
            if i is not None:
                if(self.client):
                    kill_command=command + str(i)
                    stdin, stdout, stderr = self.client.exec_command(kill_command)
                    logging.info (stdout.read())
            
                   
def ExecCmd(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True)
        logging.info (str(output))
    except subprocess.CalledProcessError as error:
        logging.info ("CMD {} failed with error {}".format(cmd, error))



def log_action (action,file_path,IP):
    file_name='_'.join(file_path.split('/'))
    logging.info (file_name)
    if (action=='start'):
        try:
            logging.info ("Log validation started")
            connection=SSH(str(IP))
            create_dir='mkdir dump'
            create=connection.send_command(create_dir)
            connection.send_command('ls')
            command1='tail -f '+ file_path +' >> /root/dump/'+ str(IP)+file_name+ ' 2>&1 &'
            print ("check here :",command1)
            command2='ps -ef | grep -i '+ file_path
            check_pid=connection.send_command(command1)
            if len(check_pid)>2:
                logging.info ("Already process is running invoking kill all process")
                connection.kill_command(check_pid,'kill -9 ')
        except tail:
            logging.info ("file not found")
            connection.send_command(command1)
    elif(action=='stop'):
        file_name='_'.join(file_path.split('/'))
        command2="scp -o StrictHostKeyChecking=no -o BatchMode=yes -o UserKnownHostsFile=/dev/null root@["+str(IP)+"]:/root/dump/"+str(IP)+file_name+" /tmp/"
        print (":::::::::::::::::::::::::::::",command2)
        logging.info (command2)
        ExecCmd(command2)
        copy_file='cp -r /root/dump/'+ str(IP)+file_name + '  /tmp/'
        #print ("copy_file ::::::::::::::::::", copy_file)
        remove_cmd='rm -rf /root/dump/'+ str(IP)+file_name
        connection=SSH(str(IP))
        copy=connection.send_command(copy_file)
        remove=connection.send_command(remove_cmd)
        logging.info ("Log validation stopped")
    else:
        logging.info ("please specify either you want to start or stop logs")        
        
#log_action("start","/infoblox/var/infoblox.log","10.35.155.15")
#sleep(10)
#log_action("stop","/infoblox/var/infoblox.log","10.35.155.15")
