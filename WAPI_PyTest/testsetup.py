# Add the network to the MS server 
    logger.info('Adding the DHCP and the DNS data for the MS server')
    logger.info('Adding the MS server DHCP data')
    logger.info("Preparation for DHCP Lease History")
    logger.info("Adding network 10.0.0.0/8")

    net_obj = {"members":[{"_struct": "msdhcpserver", "ipv4addr": "10.102.31.70" ,"name": "mserver1"}], \
            "network": "10.0.0.0/8"}
    network1 = ib_NIOS.wapi_request('POST', object_type="network", fields=json.dumps(net_obj))
    logger.info("Adding Range 10.1.2.180 - 10.2.2.181")
    range_obj = {"start_addr": "10.1.2.180","end_addr": "10.2.2.181","ms_server": {"_struct": "msdhcpserver","ipv4addr": "10.102.31.70","name": "range1"}}
    range = ib_NIOS.wapi_request('POST', object_type="range", fields=json.dumps(range_obj))
    logger.info("Restart DHCP Services")
    grid =  ib_NIOS.wapi_request('GET', object_type="grid")
    ref = json.loads(grid)[0]['_ref']
    request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
    logger.info("Wait for 30 sec.,")
    sleep(40) #wait for 10 secs for the member to get started

    logger.info('Adding the Second  MS DHCP server data')
    logger.info("Adding network 20.0.0.0/16")

    net_obj = {"members":[{"_struct": "msdhcpserver", "ipv4addr": "10.102.31.70" ,"name": "mserver2"}], \
            "network": "20.0.0.0/16"}
    network2 = ib_NIOS.wapi_request('POST', object_type="network", fields=json.dumps(net_obj))
    logger.info("Adding Range 20.0.1.60 - 20.0.2.120")
    range_obj = {"start_addr":"20.0.1.60","end_addr":"20.0.2.120","ms_server":{"_struct": "msdhcpserver","ipv4addr": "10.102.30.3","name": "range2"}}
    range = ib_NIOS.wapi_request('POST', object_type="range", fields=json.dumps(range_obj))
    logger.info("Restart DHCP Services")
    grid =  ib_NIOS.wapi_request('GET', object_type="grid")
    ref = json.loads(grid)[0]['_ref']
    request_restart = ib_NIOS.wapi_request('POST', object_type = ref + "?_function=requestrestartservicestatus")
    logger.info("Wait for 30 sec.,")
    sleep(4000) #wait for 10 secs for the member to get started

