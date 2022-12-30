# https://towardsdatascience.com/simple-gps-data-visualization-using-python-and-open-street-maps-50f992e9b676

# Lees leesme.txt

# main2.py laat toe een datum in te geven 'DDMMYYgpsx,csv' en de kaart te plotten
# alles binnen hetzelfde pat plaatsen!

import numpy as np

'''
map.png = mapHertsberge.png

				51.1176(lat min)
3.2561(long min)                3.3160(long max)
				51.0936(lat max)

(51.1176, 3.2561, 51.0936, 3.3160)

Ander voorbeeld
https://www.linkedin.com/pulse/geopandas-plotting-data-points-map-using-python-r%C3%A9gis-nisengwe/
Live grafieken
https://pythonprogramming.net/live-graphs-matplotlib-tutorial/

'''
#path = 'home/pi/Python3/LoraGPS/'
fname = str(input("Datum file (DDMMYY): "))     # gebruik als er letters/cijfers zijn (str)


from gps_class import GPSVis

vis = GPSVis(data_path= fname+'gpsx.csv',
	# print (fname)
	map_path='map.png',  # Path to map downloaded from the OSM.
	points=(51.1193,3.2599,51.0812,3.3505)) # Two coordinates of the map (upper left, lower right)

vis.create_image(color=(0,0,255), width=3)  # Set the color and the width of the GNSS tracks.

# vis.plot_map(output='save')     # save image to 'resultMap.png'
vis.plot_map(output='plot')       # plot image on screen

print()

'''

Map Hertsberge + Bossen

	51.1193
3.2599		3.3505
	51.0812
(51.1193,3.2599,51.0812,3.3505)
	
'''
