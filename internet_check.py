import requests
from win10toast import ToastNotifier
import time


def is_online(url = "https://www.google.com", timeout=5):
    try:
        response= requests.get(url, timeout=timeout)
        return response.status_code >= 200 and response.status_code<300
    except requests.ConnectionError:
        return False
    

    
# internet_status()
# check= ""      
# while True:
#    check_offline_online = internet_status()
#    if check_offline_online != check:
#        check= check_offline_online
    