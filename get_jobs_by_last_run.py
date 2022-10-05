import getpass

import time
from datetime import datetime

import math

from jenkinsapi.jenkins import Jenkins

url = input("Jenkins URL: ")
username = input("Username: ")
password = getpass.getpass("Password: ")

J = Jenkins(url, username, password)
print("Jenkins Version: " + J.version)

current_time = datetime.now()
current_time_unix = time.mktime(current_time.timetuple())

for item in J.keys():
  last_build = J.get_job(item).get_last_build().get_timestamp()
  
  lb_time = last_build

  lb_time_unix = time.mktime(lb_time.timetuple())

  time_delta = lb_time_unix - current_time_unix

  days_since_build = math.floor((time_delta / 60))
  print("Item: " + item + " // Last Run: " + str(days_since_build) + " min")