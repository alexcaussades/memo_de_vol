import os
import json
import requests
import time
import datetime
import random
import logging
import module.distance as distance

# Load the configuration file
with open("data/logiciel.json", "r") as file:
    logiciel = json.load(file)

print("Hello " + os.getlogin() + " welcome to the application " + logiciel["data"]["name"])
time.sleep(1)
print("system startup")
time.sleep(1)

print("What's your choice for this application? ")
print("1. Calculate the descent rate")
print("2. Calculate the estimated time")
print("3. vor entry / next point")
print("7. Exit")

choice = input("Enter your choice: ")


if choice == "1":
    niveau_de_vol = int(input("Enter the level of flight: "))
    vitesse_air = int(input("Enter the airspeed: "))
    distance_restante = int(input("Enter the remaining distance: "))
    vario_preffere = (input("Enter the preferred vario: "))
    
    try:
        vario_preffere = int(vario_preffere)
    except:
        print("value for default 1500")
        vario_preffere =  vario_preffere if vario_preffere != "" else 1500
    
    
    d = distance.Distance(niveau_de_vol, vitesse_air, distance_restante, vario_preffere)
    print("The descent rate is: ", d.taux_de_descente())

if choice == "2":
    niveau_de_vol = int(input("Enter the level of flight: "))
    vitesse_air = int(input("Enter the airspeed: "))
    distance_restante = int(input("Enter the remaining distance: "))
    vario_preffere = int(input("Enter the preferred vario: "))
    
    d = distance.Distance(niveau_de_vol, vitesse_air, distance_restante, vario_preffere)
    print("The estimated time is: ", d.estimation_temps())