CREATE TABLE junaApp.Asema(
nimi varchar(30) NOT NULL PRIMARY KEY
kaupunki varchar(30) NOT NULL
pituus = Double(20)
leveys = Double(20)
);

CREATE TABLE junaApp.Juna(
numero INT() NOT NULL PRIMARY KEY
tyyppitunnus VARCHAR(5) NOT NULL
lahtoasema VARCHAR(30) NOT NULL
lahtoaika TIME() NOT NULL
paateasema VARCHAR(30) NOT NULL
saapuumisaika VARCHAR(30) NOT NULL
kulkupaivat VARCHAR(5) NOT NULL
);

CREATE TABLE junaApp.Pysahdys(
asema varchar(30) NOT NULL FOREING KEY REFERENCES junaApp_Asema(nimi)
junan_numero varchar(30) NOT NULL FOREING KEY REFERENCES junaApp_Juna(numero)
saapumisaika TIME()
lahtoaika TIME()
);

CREATE TABLE junaApp.Asiakas(
id varchar(30) NOT NULL PRIMARY KEY
etunimi varcrar(30) NOT NULL
sukunimi varcrar(30) NOT NULL
kotikaupunki varcrar(30) NOT NULL
salasana varcrar(30) NOT NULL
);

CREATE TABLE junaApp.Varaus(
id INT() NOT NULL PRIMARY KEY
varaajan_id INT() NOT NULL
junan_numero INT() NOT NULL
varauspaiva DATETIME(30) NOT NULL
lahtoasema varcrar(30) NOT NULL
maaraasema varcrar(30) NOT NULL
);