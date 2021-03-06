#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Stochastically calculate pi and display it on an epaper screen, on a pot.

@filename   :   main.cpp
@brief      :   4.2inch e-paper display demo
@author     :   Yehui from Waveshare
Copyright (C) Waveshare     July 28 2017
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documnetation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to  whom the Software is
furished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from __future__ import division
from __future__ import unicode_literals
import epd4in2
import Image
# import ImageDraw
# import ImageFont
import math
import time
import random
from PIL import Image as PILimage
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 4, 3
# import imagedata

EPD_WIDTH = 400
EPD_HEIGHT = 300


def in_circle(range_max, pt=(50, 50)):
    """Check to see if a point is inside the circle inscribed in the range.

    It assumes that the centre of the circle is at the centre of the range.
    pt needs to be passed as an (x, y) tupple.
    """
    r = range_max*0.5
    dist = math.hypot(pt[0] - r, pt[1] - r)
    return dist < r

def sub_colour(c):
    if c == 0:
        return "k"
    else:
        return "r"


def main():
    """Run the pi finder."""
    epd = epd4in2.EPD()
    epd.init()

    #  Here's the real shit
    debug = False
    range_max = 1000000  # bigger numbers here give better accuaracy
    x_coords = [0, range_max, range_max,         0]
    y_coords = [0,         0, range_max, range_max]
    colours  = [0,         0,         0,         0]
    cap = 7200  # bigger numbers here give better accuaracy, but take longer

    while True:
        for i in range(cap):
            x = random.randint(0, range_max)
            y = random.randint(0, range_max)
            x_coords.append(x)
            y_coords.append(y)
            if in_circle(range_max, pt=(x, y)):
                colours.append(1)
            else:
                colours.append(0)

            num_tests = len(colours)
            num_in    = sum(colours)
            # num_out   = num_tests-num_in
            pi_approx = (4*num_in)/num_tests

            if i > 2:
                value_output = ("π  ≅{pi_approx:.4f}\n"                 # π≅
                                "πΔ ={delta:.4f}\n"                     # πΔ=
                                "N  ={N}").format(pi_approx=pi_approx,  # N=
                                                  delta=math.pi - pi_approx,
                                                  N=num_tests)
                fig = plt.scatter(x_coords,
                                  y_coords,
                                  c=[sub_colour(c) for c in colours],
                                  alpha=0.5,
                                  marker="2")
                plt.axis('equal')
                plt.axis('off')
                fig.axes.get_xaxis().set_ticks([])
                fig.axes.get_yaxis().set_ticks([])
                plt.subplots_adjust(left=-0.25)

                plt.text(range_max*1.13,
                         range_max*0.5,
                         value_output,
                         style='italic',
                         bbox={'facecolor': 'red', 'alpha': 0.2, 'pad': 6},
                         size=12)

                circle = plt.Circle((range_max*0.5, range_max*0.5),
                                    range_max*0.5,
                                    color='r',
                                    fill=False,
                                    alpha=0.5,
                                    linewidth=2,
                                    linestyle=":",
                                    edgecolor='b')
                plt.gcf().gca().add_artist(circle)
                print(value_output)
                if debug:
                    plt.show()  # you can show or save, not both
                else:
                    filename = "p"  # +str(i)
                    plt.savefig(filename + ".png", dpi=100)

                    #  convert a .png image file to a .bmp image file using PIL
                    file_in = filename + ".png"
                    img = PILimage.open(file_in)
                    img2 = img.rotate(180)
                    img2.save(filename + ".bmp")

                plt.clf()

                image = Image.open('p.bmp')
                epd.display_frame(epd.get_frame_buffer(image))

                time.sleep(0.1)


if __name__ == '__main__':
    main()
