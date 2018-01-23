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


def main():
    epd = epd4in2.EPD()
    epd.init()

    #  Here's the real shit
    debug = False
    x_coords = []
    y_coords = []
    colours  = []
    # markers  = []
    range_max = 1000000  # bigger numbers here give better accuaracy
    cap = 1000  # bigger numbers here give better accuaracy, but take longer

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

    #     if i>2:  # toggle these lines
        if i > cap-3:  # don't plot empty plots, it goes crazy
            fig = plt.scatter(x_coords, y_coords, c=colours, alpha=0.5)
            plt.axis('equal')
            plt.axis('off')
            fig.axes.get_xaxis().set_ticks([])
            fig.axes.get_yaxis().set_ticks([])
            plt.subplots_adjust(left=-0.25)

            plt.text(range_max*1.13,
                     range_max*0.5,
                     ("spi={pi_approx:.4f}\n"                  # π≅
                      "del={delta:.4f}\n"                      # πΔ=
                      "  N={N}").format(pi_approx=pi_approx,   # N=
                                      delta=math.pi - pi_approx,
                                      N=num_tests),
                     style='italic',
                     bbox={'facecolor': 'red', 'alpha': 0.2, 'pad': 6},
                     size=12)
            if debug:
                plt.show()  # you can show or save, not both
            else:
                filename = "p"  # +str(i)
                plt.savefig(filename + ".png", dpi=100)

                #  convert a .png image file to a .bmp image file using PIL
                file_in = filename + ".png"
                img = PILimage.open(file_in)
                file_out = filename + ".bmp"
                img.save(file_out)

            plt.clf()

            # For simplicity, the arguments are explicit numerical coordinates
            # image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
            # epd.display_frame(epd.get_frame_buffer(image))

            image = Image.open('p.bmp')
            epd.display_frame(epd.get_frame_buffer(image))

            # You can get frame buffer from an image or import the buffer directly:
            # epd.display_frame(imagedata.MONOCOLOR_BITMAP)

            time.sleep(0.5)


if __name__ == '__main__':
    main()
