# Junatietokanta
Aiheen kuvaus:
Junatietokanta sisältää tietoa junista ja asemista, joilla ne pysähtyvät. Tietokannasta olisi helppo hakea yhteyksiä kahden aseman 
välillä. Tietokantaan olisi myös helppo lisätä uusia junia, asemia ja pysähdyksia csv-tiedostosta. Tietokanta sisältäisi myös
tietoa asiakkaista ja niiden tekemistä varauksista juniin. Järjestelmän tavoitteena on helpottaa tiedon hakua junista ja 
niihin tehtyjen varausten hallintaa.

Ympäristö on vielä hieman auki, mutta näillä näkymin tulen pystyttämään oman palvelimen tietokannalle. Oma palvelin sen takia, että
sovellus käyttää Pythonin Django-frameworkkiä, jota sen täytyy tukea. Itse selaimelta ei kuitenkaan mitään javascript-tukea 
kummoisempaa vaadita. Django on siitä näppärä, että tietokannan vaihtaminen ainakin teoriassa on helppoa, jos vaan kaikki tarvittavat
palikat ovat asennettuna (esim mysql tarvitsee python-mysql liitännän)

Ohjelmisto löytyy osoitteesta: , mutta jos haluaa kokeilla itse sovellusta omassa ympäristössä, tässä asennusohjeet:

1: Asenna python (käsittääkseni löytyy ubunduista valmiina) windowsille: https://www.python.org/downloads/release/python-351/ 
2: Asenna django: windows: avaa komentorivi järjestelmänvalvojana ja kirjoita "pip install django" 
	ubundu: kirjoita terminaaliin "sudo pip install django" 
3: kloonaa repositorio: git clone https://github.com/leo0074/Junatietokanta tai githubin sivun kautta, jos githubia ei löydy koneelta. 
4: Siirry komentorivillä/terminaalilla Junatietokanta-kansioon (kansio missä on manage.py) 
5: kirjoita "python manage.py runserver" ja serveri käynnistyy 
6: selaimessa kirjoita "http://127.0.0.1:8000/junaApp/" ja selaimen pitäisi ladata ohjelman etusivu.
