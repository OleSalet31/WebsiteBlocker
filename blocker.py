
import time
from datetime import datetime as dt

hosts_path=r"/etc/hosts" #location of host file
hosts_temp="/Users/olesalet/Desktop/website_blocker/hosts"  #temporary file path to copied host file use for testing
redirect="127.0.0.1" #redirect blocked sites to this IP
website_to_block=["www.facebook.com","www.instagram.com"]


while True:
    #if the time right now is between the set time 09:00 to 16:00 add the sites to host file
    if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,15):
        print("Get to work already!")
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            for website in website_to_block:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
    #otherwise write all original lines in the host file except the list of sites
        with open(hosts_temp, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_to_block):
                    file.write(line)
            file.truncate()
        print("distrections allowd")
    time.sleep(5) #run program every 5 seconds
