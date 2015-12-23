from django.db import connection
from junaApp.models import *

def luo_asema(data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO junaApp_Asema (nimi, kaupunki, pituus, leveys) VALUES"
                   "('"+data["nimi"]+"','"+data["kaupunki"]+"','"+data["pituus"]+"','"+data["leveys"]+"' )")

def poista_asema(data):
    cursor = connection.cursor()
    cursor.execute("DELETE from junaApp_Asema where nimi='"+data["asema"]+"'")
    cursor.execute("DELETE from junaApp_Pysahdys where asema='"+data["asema"]+"'")

def asema_olemassa(nimi):
    if len(list(Asema.objects.raw("SELECT nimi FROM junaApp_Asema WHERE nimi='"+nimi+"'"))) is not 0:
        return True
    return False

def luo_juna(data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO junaApp_Juna (numero, tyyppi, lahtoasema, lahtoaika, paateasema, saapumisaika, kulkupaivat) VALUES"
                   "('"+data["numero"]+"','"+data["tyyppi"]+"','"+data["lahtoasema"]+"','"+data["lahtoaika"]+"','"+data["paateasema"]
                   +"','"+data["saapumisaika"]+"','"+data["kulkupaivat"]+"' )")

def poista_juna(data):
    cursor = connection.cursor()
    cursor.execute("DELETE from junaApp_Juna where numero='"+data["numero"]+"'")
    cursor.execute("DELETE from junaApp_Pysahdys where junan_numero='"+data["numero"]+"'")

def juna_olemassa(numero):
    lista = Juna.objects.raw("SELECT * FROM junaApp_Juna WHERE numero='"+numero+"'")
    lista = list(lista)
    lista = len(lista)
    print(lista)
    if len(list(Juna.objects.raw("SELECT numero FROM junaApp_Juna WHERE numero='"+numero+"'"))) is not 0:
        return True
    return False

def luo_pysahdys(data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO junaApp_Pysahdys (asema, junan_numero, saapumisaika, lahtoaika) VALUES"
                   "('"+data["asema"]+"','"+data["junan_numero"]+"','"+data["saapumisaika"]+"','"+data["lahtoaika"]+"' )")

def poista_pyshadys(data):
    cursor = connection.cursor()
    cursor.execute("DELETE from junaApp_Juna where asema='"+data["asema"]+"'")

def pysahdys_olemassa(data):
    if len(list(Pysahdys.objects.raw("SELECT numero FROM junaApp_Pysahdys WHERE numero='"+data["asema"]+"AND junan_numero='"+data["asema"]+"'"))) is not 0:
        return True
    return False