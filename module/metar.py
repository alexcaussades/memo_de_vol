import requests
import json


class Metar:
    def __init__(self, icao):
        self.icao = icao


    def metar(icao):
        icao = icao.upper()
        url = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/" + icao + ".TXT"
        response = requests.get(url)
        data = response.text
        return data

    def decription_metar(icao):
        # regex en python pour extraire les données de la météo de l'aéroport
        data = Metar.metar(icao)
        return data
        