__author__ = "Arunkumar CM"
__email__  = "acm@infoblox.com"

########################################################################################
#  Usage                                                                               #
#  1. from Bgp_and_OSPF_IPV4 import Start_bird_process as Bgp                          #
#  2. Bgp(<bird or bird6>,<bgp or ospf>)                                               #
########################################################################################
import getopt
import re
import config
import pytest
import unittest
import logging
import subprocess
import os
import json
import ib_utils.ib_NIOS as ib_NIOS
import commands
import json, ast
import requests
from time import sleep as sleep
import pexpect
import paramiko
import time
import sys
import socket
from paramiko import client
global host_ip
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
#host_ip="10.36.198.9"
ipv6_ip=socket.getaddrinfo(host_name, None, socket.AF_INET6)
ipv6_ip=ipv6_ip[0][4][0]


def get_user_input(filename):
    with open (filename,'r') as fobj:
        res=fobj.read()
        res = json.loads(res)
        return res

class SSH:
    client=None

    def __init__(self,address):
        logging.info ("connecting to server \n : ", address)
        self.client=client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(host_ip, username='root',password='infoblox',port=22)

    def send_command(self,command):
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            result=stdout.read()
            return result
'''
def scp_to_server():
    directory=os. getcwd()
    print directory
    os.system("chmod 777 "+directory)
    SSH_OPTIONS="-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"
    cmd="cp /root/*.conf "+directory
    print cmd
    print ("sshpass -p infoblox ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@10.36.198.9 "+ cmd)
    a=os.system("sshpass -p infoblox ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@10.36.198.9 "+ cmd)
'''
def scp_to_server():
    directory=os. getcwd()
    print directory
    os.system("chmod 777 "+directory)
    SSH_OPTIONS="-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"
    cmd=":/root/bird.conf "+directory
    print cmd
    print ("sshpass -p infoblox scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@10.36.198.9"+ cmd)
    a=os.system("sshpass -p infoblox scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@10.36.198.9"+ cmd)

def modify_bird_ipv4_conf_file_for_BGP(user_input):
    values=user_input
    local_as=values["BGP"]["local_as"]
    remote_as=values["BGP"]["remote_as"]
    directory=os. getcwd()
    command1="sed -i -e s/'source address [0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'/'source address "+host_ip +"'/g "+directory +"/bird.conf"
    os.system(command1)
    command2="sed -i -e s/'neighbor [0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'/'neighbor "+config.grid_vip +"'/g "+directory +"/bird.conf"
    os.system(command2)
    command3="sed -i -e s/'local as [0-9][0-9]*'/'local as "+str(local_as)+"'/g "+directory +"/bird.conf"
    os.system(command3)
    command4="sed -i -e s/'neighbor [0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\} as [0-9][0-9]*'/'neighbor "+config.grid_vip+" as "+str(remote_as)+"'/g "+directory +"/bird.conf"
    os.system(command4)

def modify_bird_ipv4_conf_file_for_OSPF(user_input):
    values=user_input
    print values
    directory=os. getcwd()
    area_id=values["OSPF"]["area_id"]
    command1="sed -i -e s/'area .* {'/'area "+str(area_id)+" {'/g "+directory +"/bird.conf"
    os.system(command1)

def modify_bird_ipv6_conf_file_for_OSPF(user_input):
    values=user_input
    area_id=values["OSPF"]["area_id"]
    directory=os. getcwd()
    values=user_input
    command1="sed -i -e s/'area .*{'/'area "+str(area_id)+"{'/g "+directory +"/bird6.conf"
    os.system(command1)

def copy_ipv4_bird_file_to_bird_directory():
    directory=os. getcwd()
    cmd="cp "+directory+"/bird.conf /usr/local/etc/"
    a=os.system("sshpass -p infoblox ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@"+host_ip+" "+cmd)
    os.system("rm -rf "+directory+"/*.conf" )

def modify_bird_ipv6_conf_file_for_BGP(user_input):
    values=user_input
    local_as=values["BGP"]["local_as"]
    remote_as=values["BGP"]["remote_as"]
    directory=os. getcwd()
    command1="sed -i -e s/'source address .*;'/'source address "+ipv6_ip +";'/g "+directory +"/bird6.conf"
    os.system(command1)
    command3="sed -i -e s/'local as [0-9][0-9]*'/'local as "+str(local_as)+"'/g "+directory +"/bird6.conf"
    os.system(command3)
    command4="sed -i -e s/'neighbor .* as [0-9][0-9]*'/'neighbor "+config.grid_ipv6_ip+" as "+str(remote_as)+"'/g "+directory +"/bird6.conf"
    os.system(command4)


def copy_ipv6_bird_file_to_bird_directory():
    directory=os. getcwd()
    cmd="cp "+directory+"/bird6.conf /usr/local/etc/"
    a=os.system("sshpass -p infoblox ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@"+host_ip+" "+cmd)
    os.system("rm -rf "+directory+"/*.conf" )

def install_bird_package(command):
    user="root"
    password="infoblox"
    logging.info("Entering function")
    child=pexpect.spawn('ssh -o StrictHostKeyChecking=no %s@%s' % (user,host_ip))
    child.logfile = sys.stdout
    child.expect("password: |\#|\$",timeout=30)
    child.sendline(password)
    child.expect("#|\$")
    child.sendline("echo \$PYTHONPATH")
    child.sendline("chmod 777 /run/bird")
    child.expect("#|\$",timeout=30)
    child.sendline("dnf install "+command.strip('\"'))
    logging.info("login succesfull")
    i=child.expect(["Is this ok \[y/N\]:","#|\$"],timeout=30)
    logging.info("Value of i is "+str(i))
    if i==0:
        try:
            child.sendline("y")
            child.expect("#|\$",timeout=240)
            child.close()
            return 0
        except:
            print("Curl error (28): Timeout was reached")
    elif i==1: 
       child.sendline("exit")
       child.close()


def ExecCmd(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True)
        logging.info (str(output))
    except subprocess.CalledProcessError as error:
        logging.info ("CMD {} failed with error {}".format(cmd, error))


def Start_bird_process (command,protocol,filename):
    user_input=get_user_input(filename)
    connection=SSH(str(host_ip))
    install_bird_package(command)
    scp_to_server()
    if len(protocol)==1:
        if protocol[0]=="bgp":
            if command=="bird":
                modify_bird_ipv4_conf_file_for_BGP(user_input)
                copy_ipv4_bird_file_to_bird_directory()
                command1="pidof "+command
                check_pid=connection.send_command(command1)
                if check_pid!="":
                    logging.info ("Already process is running invoking kill all process")
                    command1="kill -9 "+check_pid
                    check_pid=connection.send_command(command1)
                    sleep(10)
                    command2=command+' -c /usr/local/etc/bird.conf'
                    res=connection.send_command(command2)
                    print res
                    connection.send_command(command2)
                else:
                    command2=command+' -c /usr/local/etc/bird.conf'
                    print command2
                    connection.send_command(command2)
        elif protocol[0]=="ospf":
            if command=="bird":
                modify_bird_ipv4_conf_file_for_OSPF(user_input)
                copy_ipv4_bird_file_to_bird_directory()
                command1="pidof "+command
                check_pid=connection.send_command(command1)
                print check_pid
                if check_pid!="":
                    logging.info ("Already process is running invoking kill all process")
                    command1="kill -9 "+check_pid
                    check_pid=connection.send_command(command1)
                    sleep(10)
                    command2=command+' -c /usr/local/etc/bird.conf'
                    connection.send_command(command2)
                else:
                    command2=command+' -c /usr/local/etc/bird.conf'
                    connection.send_command(command2)


    elif len(protocol)==2:
        if command=="bird6":
            modify_bird_ipv6_conf_file_for_BGP(user_input)
            modify_bird_ipv6_conf_file_for_OSPF(user_input)
            copy_ipv6_bird_file_to_bird_directory()
            command1="pidof "+command
            check_pid=connection.send_command(command1)
            if check_pid!="":
                logging.info ("Already process is running invoking kill all process")
                command1="kill -9 "+check_pid
                check_pid=connection.send_command(command1)
                sleep(10)
                command2=command+' -c /usr/local/etc/bird6.conf'
                connection.send_command(command2)
            else:
                command2=command+' -c /usr/local/etc/bird6.conf'
		print command2
                connection.send_command(command2)
    
        elif command=="bird":
            modify_bird_ipv4_conf_file_for_BGP(user_input)
            modify_bird_ipv4_conf_file_for_OSPF(user_input)
            copy_ipv4_bird_file_to_bird_directory()
            command1="pidof "+command
            check_pid=connection.send_command(command1)
            print check_pid
            if check_pid!="":
                logging.info ("Already process is running invoking kill all process")
                command1="kill -9 "+check_pid
                check_pid=connection.send_command(command1)
                sleep(10)
                command2=command+' -c /usr/local/etc/bird.conf'
                connection.send_command(command2)
            else:
                command2=command+' -c /usr/local/etc/bird.conf'
                connection.send_command(command2)

#Start_bird_process ("bird",["ospf","bgp"],"/import/qaddi/rkarjagi/API_Automation/WAPI_PyTest/suites/RFE_9170/BGP/arun.json")
