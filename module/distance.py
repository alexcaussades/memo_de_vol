import os
import sys
import json
import requests
import time
import datetime
import random
import logging

class Distance:
    def __init__(self, niveau_de_vol, vitesse_air, distance_restante, vario_preffere = 1500):
        self.niveau_de_vol = niveau_de_vol
        self.vitesse_air = vitesse_air
        self.distance_restante = distance_restante
        self.vario_preffere = vario_preffere
        
    def taux_de_descente(self):
        a = ((self.vitesse_air * self.niveau_de_vol) / (60* self.distance_restante))
        if a < 0:
            return 0
        else:
            return a
        

    def estimation_temps(self):
        a  = ((self.vitesse_air * self.niveau_de_vol) / (60* self.vario_preffere))
        if a < 0:
            return 0
        else:
            return a
        
    def estimation_distance(self):
        a = (self.vitesse_air * self.niveau_de_vol) / (60* self.taux_de_descente())
        if a < 0:
            return 0
        else:
            return a
        
        
    def estimation_altitude(self):
        a = (self.vario_preffere * self.taux_de_descente())
        if a < 0:
            return 0
        else:
            return a
        
        
    def estimation_vitesse(self):
        a = (self.vitesse_air + self.vario_preffere)
        if a < 0:
            return 0
        else:
            return a
        
    def estimation_vitesse_sol(self):
        a = (self.vitesse_air - self.vario_preffere)
        if a < 0:
            return 0
        else:
            return a
        
    def estimation_distance_sol(self):
        a = (self.vitesse_air * self.niveau_de_vol) / (60* self.estimation_vitesse_sol())
        if a < 0:
            return 0
        else:
            return a
        
    def estimation_temps_sol(self):
        a = (self.vitesse_air * self.niveau_de_vol) / (60* self.estimation_vitesse_sol())
        if a < 0:
            return 0
        else:
            return a
        
    def estimation_altitude_sol(self):
        a = (self.vario_preffere * self.taux_de_descente())
        if a < 0:
            return 0
        else:
            return a
        
    def estimation_vitesse_sol(self):
        a = (self.vitesse_air - self.vario_preffere)
        if a < 0:
            return 0
        else:
            return a
        
        