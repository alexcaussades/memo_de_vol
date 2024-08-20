import requests
import json

def metar(icao):
    icao = icao.upper()
    url = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/" + icao + ".TXT"
    response = requests.get(url)
    data = response.text
    return data