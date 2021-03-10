import IP2Location
import IP2Proxy
import requests
from device_detector import DeviceDetector
from flask import request
from datetime import datetime
import socket



def get_device_info():
    device_info = {}
    ua = str(request.headers.get('User-Agent'))
    device = DeviceDetector(ua).parse()
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    temp_device_info = {"os_name":device.os_name(),"device_type":device.device_type(),"browser":device.client_name(),"time":current_time}
    device_info.update(temp_device_info)
    return device_info


def get_location():
    data = {}
    IP_address = request.remote_addr
    db = IP2Proxy.IP2Proxy()
    db.open("ahrvo/static/location_data/IP2PROXY-LITE-PX1.IPV6.CSV")
    check_proxy = db.is_proxy(str(IP_address))
    if check_proxy == "-1" or  check_proxy == -1:
        proxy = False
    else:
        proxy = True
    temp_proxy = {"proxy":proxy,"ip":IP_address}
    data.update(temp_proxy)
    IP2LocObj = IP2Location.IP2Location()
    IP2LocObj.open("ahrvo/static/location_data/IP2LOCATION-LITE-DB3.BIN")
    location = IP2LocObj.get_all(str(IP_address))
    temp_location = {"country":location.country_long,"region":location.region,"city":location.city}
    data.update(temp_location)
    device_info = get_device_info()
    data.update(device_info)
    return data
