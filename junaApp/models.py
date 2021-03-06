from django.db import models

#CREATE TABLE junaApp.Asema(
#nimi varchar(30) NOT NULL PRIMARY KEY
#kaupunki varchar(30) NOT NULL
#)
class Asema(models.Model):
    nimi = models.CharField(max_length=30, primary_key=True)
    kaupunki = models.CharField(max_length=30)

#CREATE TABLE junaApp.Juna(
#numero INT() NOT NULL PRIMARY KEY
#tyyppitunnus VARCHAR(5) NOT NULL
#lahtoasema VARCHAR(30) NOT NULL
#lahtoaika TIME() NOT NULL
#paateasema VARCHAR(30) NOT NULL
#saapuumisaika VARCHAR(30) NOT NULL
#kulkupaivat VARCHAR(5) NOT NULL
#)
class Juna(models.Model):
    numero = models.IntegerField(primary_key=True)
    tyyppi = models.CharField(max_length=5)
    lahtoasema = models.CharField(max_length=30)
    lahtoaika =models.TimeField()
    paateasema = models.CharField(max_length=30)
    saapumisaika =models.TimeField()
    kulkupaivat = models.CharField(max_length=5)

#CREATE TABLE junaApp.Pysahdys(
#asema varchar(30) NOT NULL FOREING KEY REFERENCES junaApp_Asema(nimi)
#junan_numero varchar(30) NOT NULL FOREING KEY REFERENCES junaApp_Juna(numero)
#saapumisaika TIME()
#lahtoaika TIME()
#)
class Pysahdys(models.Model):
    asema = models.CharField(max_length=30)
    junannumero = models.IntegerField()
    saapumisaika = models.TimeField()
    lahtoaika = models.TimeField()

