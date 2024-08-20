import os
import json
import requests
import time
import datetime
import random
import logging
import module.distance as distance



print("Hello " + os.getlogin())
time.sleep(1)
print("system startup")
time.sleep(1)

print("What's your choice for this application? ")
print("1. Calculate the descent rate")
print("2. Calculate the estimated time")

print("7. Exit")

choice = input("Enter your choice: ")
