from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import engine
from genera_base import Paises
import requests

import json

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite



Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json", "r")
# archivo = request.get("------------------.json")

datos_json = archivo.json() # paso los datos del archivo a json
# archivo.json()


for d in datos_json:
    print(d)
    print(len(d.keys()))
    p = Paises(nombreP=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], \
            dial=d['Dial'], geonameID=d['Geoname ID'], itu=d['ITU'], lenguage=d['Languages'], \
                depend=d['is_independent'])
    session.add(p)

# confirmar transacciones

session.commit()
