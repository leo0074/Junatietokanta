from django.db import connection
from junaApp.models import *

def luo_asema(data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO junaApp_Asema (nimi, kaupunki) VALUES"
                   "('"+data["nimi"]+"','"+data["kaupunki"]+"',0,0)")

def poista_asema(data):
    cursor = connection.cursor()
    cursor.execute("DELETE from junaApp_Asema where nimi='"+data["asema"]+"'")
    cursor.execute("DELETE from junaApp_Pysahdys where asema='"+data["asema"]+"'")

def asema_olemassa(nimi):
    if len(list(Asema.objects.raw("SELECT nimi FROM junaApp_Asema WHERE nimi='"+nimi+"'"))) is not 0:
        return True
    return False

def paivita_asema(data):
    cursor = connection.cursor()
    cursor.execute("UPDATE junaApp_Asema SET kaupunki='"+data["kaupunki"]+"' WHERE nimi='"+data["nimi"]+"'")

def hae_asemat():
    return Asema.objects.raw('SELECT nimi FROM junaApp_Asema')

def luo_juna(data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO junaApp_Juna (numero, tyyppi, lahtoasema, lahtoaika, paateasema, saapumisaika, kulkupaivat) VALUES"
                   "('"+data["numero"]+"','"+data["tyyppi"]+"','"+data["lahtoasema"]+"','"+data["lahtoaika"]+"','"+data["paateasema"]
                   +"','"+data["saapumisaika"]+"','"+data["kulkupaivat"]+"' )")

def poista_juna(data):
    print(data)
    cursor = connection.cursor()
    cursor.execute("DELETE from junaApp_Juna where numero='"+data["juna"]+"'")
    cursor.execute("DELETE from junaApp_Pysahdys where junannumero='"+data["juna"]+"'")

def juna_olemassa(numero):
    if len(list(Juna.objects.raw("SELECT numero FROM junaApp_Juna WHERE numero='"+numero+"'"))) is not 0:
        return True
    return False

def paivita_juna(data):
    cursor = connection.cursor()
    cursor.execute("UPDATE junaApp_Juna SET numero='"+data["numero"]+"' and tyyppi='"+data["tyyppi"]+"' WHERE numero='"+data["numero"]+"'")


def hae_junat():
    return Juna.objects.raw("SELECT * from junaApp_Juna")

def luo_pysahdys(data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO junaApp_Pysahdys (asema, junannumero, saapumisaika, lahtoaika) VALUES"
                   "('"+data["asema"]+"','"+data["juna"]+"','"+data["saapumisaika"]+"','"+data["lahtoaika"]+"' )")

def poista_pyshadys(data):
    cursor = connection.cursor()
    cursor.execute("DELETE from junaApp_Juna where asema='"+data["asema"]+"'")

def pysahdys_olemassa(data):
    if len(list(Pysahdys.objects.raw("SELECT * FROM junaApp_Pysahdys WHERE asema='"+data["asema"]+"' AND junannumero='"+data["juna"]+"'"))) is not 0:
        return True
    return False

def hae_pysahdykset():
    return Pysahdys.objects.raw("SELECT * from junaApp_Pysahdys ORDER BY junannumero, saapumisaika")