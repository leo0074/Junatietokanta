from django.db import connection
def luo_asema(data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO junaApp_Asema (nimi, kaupunki, pituus, leveys) VALUES"
                   "('"+data["nimi"]+"','"+data["kaupunki"]+"','"+data["pituus"]+"','"+data["leveys"]+"' )")

def poista_asema(data):
    cursor = connection.cursor()
    cursor.execute("DELETE from junaApp_Asema where nimi='"+data["asema"]+"'")
    cursor.execute("DELETE from junaApp_Pysahdys where asema='"+data["asema"]+"'")