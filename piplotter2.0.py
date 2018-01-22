from __future__ import division
from PIL import Image
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import time


# create a cartesian array as a dictionary of numbered points
coordinates = [(x,y) for x in range(1000) for y in range(1000)]
labels = range(0,999999)
space = dict(zip(labels, coordinates))

#create a pair of inputs 
CIR = 0
SQR = 0 

#draws circle section
x = np.linspace(0, 1000, 1000)
y = (1000000-(x**2))**.5
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'b-')
plt.axis([0, 1000, 0, 1000])
ax.set_yticklabels([])
ax.set_xticklabels([])

#initialise a while loop
K = 1
while K <> 0:
    #select a point at random
    query = np.random.randint(0, 999999, 1)[0]

    #searches for point in dictionary
    result = space.get(query)
	
    #calculate circle sum 
    circle_sum = result[0]**2 + result[1]**2

    #is it inside the circle?
    if circle_sum <= 1000000:
        CIR = CIR + 1
    else:
        SQR = SQR + 1
    
    K = K + 1
    #prints uptdated pi value
    if CIR <> 0 and SQR <> 0:
        PI_EST = (4.0)/(SQR/CIR + 1.0)
    else: 
        PI_EST = 'calculating' 
           
	#plots scatter
    a = result[0]
    b = result[1]
    #z = np.sqrt(a**2 + b**2)
    if circle_sum <= 1000000:
        scat = plt.scatter(a, b, s=20, c=11111, marker=(4, 2))
    else:
        scat = plt.scatter(a, b, s=20, c=666666, marker=(5, 2))
	fig.canvas.draw()    
	
	#plots caption
    cap = ax.text(30, -70, "PI = %s   # = %d" % (PI_EST, K), style='italic',
    bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    fig.canvas.draw()
	#saveout image
    plt.savefig('plot.png', dpi = 300)
	
	# convert a .png image file to a .bmp image file using PIL
    file_in = "plot.png"
    img = Image.open(file_in)
    file_out = "plot.bmp"
    img.save(file_out)

	#wait half a second
    time.sleep(.5)    
    cap.remove()
    


    

