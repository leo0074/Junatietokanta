from django.db import models
from django.db import connection

#CREATE TABLE junaApp.Asema(
#nimi varchar(30) NOT NULL PRIMARY KEY
#kaupunki varchar(30) NOT NULL
#pituus = Double(20)
#leveys = Double(20)
#)
class Asema(models.Model):
    nimi = models.CharField(max_length=30, primary_key=True)
    kaupunki = models.CharField(max_length=30)
    pituus = models.DecimalField(max_digits=12, decimal_places=8, blank=True)
    leveys = models.DecimalField(max_digits=12, decimal_places=8, blank=True)

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
    tyyppitunnus = models.CharField(max_length=5)
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
    junan_numero = models.IntegerField()
    saapumisaika = models.TimeField()
    lahtoaika = models.TimeField()

class Asiakas(models.Model):
    id = models.IntegerField(primary_key=True)
    etunimi = models.CharField(max_length=30)
    sukunimi = models.CharField(max_length=30)
    kotikaupunki = models.CharField(max_length=30)
    salasana = models.CharField(max_length=30)

class Varaus(models.Model):
    id = models.IntegerField(primary_key=True)
    varaajan_id = models.IntegerField()
    junan_numero = models.IntegerField()
    varauspaiva = models.DateTimeField()
    lahtoasema = models.CharField(max_length=30)
    maaraasema = models.CharField(max_length=30)
