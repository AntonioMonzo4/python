# Descarga versiÃ³n community: https://www.mongodb.com/try/download
# InstalaciÃ³n:https://www.mongodb.com/docs/manual/tutorial
# MÃ³dulo conexiÃ³n MongoDB: pip install pymongo
# EjecuciÃ³n: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# ConexiÃ³n: mongodb://localhost

from pymongo import MongoClient

db_client = MongoClient().local #Conexión a base de datos local, si es remota se pone la url completa 