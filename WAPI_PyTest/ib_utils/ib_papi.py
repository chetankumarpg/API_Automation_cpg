"""
 Copyright (c) Infoblox Inc., 2016

 Modle Name  : ib_papi 
 Description : This module is used to execute PAPI utility 

"""
import subprocess
import config
import os


"""
This module will add SSH keys into the box.
"""

def addkeys(gm_ip):
    rc=subprocess.call(['addkeys',gm_ip ])
    return rc


"""
This module will download Perl module from Grid master. 
"""
def download_pm(gm_ip):
    rc=subprocess.call(['getPAPI',gm_ip,'/var/tmp/InfobloxPM/'])
    return rc
    
