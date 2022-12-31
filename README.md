# GPScoordinatesRECandPLOT
Raspberry PI Python3: records coordinates en plot later on a map

DEEL1.

Decodeert de data afkomstig van een GPS-module naar een leesbare vorm. Deze data is gecodeerd volgens NMEA0183 protocol.

Iedere seconde stuurt de GPS een reeks lijnen naar buiten met data op een snelheid van 9600 baud.

De inhoud en samenstelling wordt uitgelegd in bijlage NMEA0183.pdf

Het programma neemt de data binnen via de serial0-bus op GPIO15 split deze en maakt de volgende variabelen:

datum, time, latitude, longitude, altitude, snelheid, richting, aantal sat, afstand (afgelegde wes na start-up).

Er zijn gps-modules die enkel de US-satellieten ontvangen anderen ook de Chineese, Russische, Europese.

In het eerste geval begint de lijn met GPxxx in het andere geval GNxxx. Dit programma werkt met beide type modules.

Het programma 'serial_gpsXX.py' maakt 2 files aan. 'gpsd.csv' en bevat respectivelijk 'datum, time, latitude, longitude, altitude, snelheid, richting, aantal sat en afstand' de andere file 'gpsx.csv' bevat enkel 'latitude en longitude'. De files worden iedere 60 seconden aangevuld. Met de file 'gpsx.csv' kan een plot gemaakt worden op een kaart,zie DEEL2.  afgesloten. 
Beide files bevatten ook een datum. Dus worden volgende files aangemaakt: 'ddmmyygpsx.csv' en 'ddmmyygpsd.csv'. Zo kan bij het plotten alles beter gescheiden worden.

De file met de data 'ddmmyygpsd.csv' bevat ook de afgelegde weg. Ideaal om na een wandeling de afstand te bekijken. Met de plot wordt de wandeling zichtbaar.

Om een propere shut down mogelijk te maken voorzien we een reedcontact tussen GPIO17 en GND. Met een magneetje wordt de Raspberry proper afgesloten.


DEEL2.

Met een afzonderlijk programma kunnen we de eerder opgenomen coördinaten zichtbaar maken op een kaart. File 'ddmmyygpsx.csv'. Om dit te laten werken zijn er 4 files nodig. Het programma die bestaat uit 2 files 'main2.py' en 'gps_class.py'. Een kaart 'map.png' en de opgenomen coördinaten 'ddmmyygpsx.csv'. Zorg dat deze 4 files in de zelfde map staan zodat ze tijdens het proces door het programma terug gevonden worden.

Bij het starten zal het programma 'main2.py' wordt gevraagd naar de datum van de gewenste file. Daarna zal de 'map.png' aangevuld worden met een plot v/d coördinaten te zien in 'resultMap.png' of een plot op het scherm. De keuze gebeurt door de juiste lijn actief te maken in 'main2.py' de laatste 2 regels.

Op basis van: https://towardsdatascience.com/simple-gps-data-visualization-using-python-and-open-street-maps-50f992e9b676
NMEA0183 decoder: https://ozzmaker.com/using-python-with-a-gps-receiver-on-a-raspberry-pi/


AUTOSTART.

Dit ontwerp kan perfect werken met een Raspberry Zero 2W. Daarop een GPS-module Neo8n en een externe antenne. Dit is klein en geschikt om mee te nemen op fiets, auto of te voet. Daarom is het wenselijk dat bij het aansluiten van een voeding µC automatisch opstart.
De volgende bewerkingen worden in de terminal ingegeven.
- Zorg dat alle 'libraries' ingegeven worden met SUDO zodat ze voor alle gebruikers te bereiken zijn.
- Zorg dat alle files in dezelfde map zitten. Deze zijn 'serial_gpsXX.py' 'main2.py' 'gps_class.py' 'map.png' 
- geef in via terminal: sudo nano /etc/rc.local 
- voeg voor 'exit0' het pad toe die verwijst naar de plaats van het programma, voorbeeld: python /home/pi/Python3/serial_gps16.py 
- sla de aanpassing op en reboot
- test of de toepassing loopt met: ps aux | grep /home/pi/Python3 of korter: ps aux | grep /Python3  
- als alles goed is ziet u een nummer die aanheeft dat het proces loopt. Bij het opnieuw ingeven van vorigeinstructie komt steeds het zelfde nummer terug.
- dit proces kan gestopt worden met: sudo kill XXX waarbij XXX het procesnummer is.

