#!/bin/env python

"""
plot\_vfat\_and\_channel\_Scurve
================================
"""

if __name__ == '__main__':
    from gempython.gemplotting.macros.plotoptions import parser
    (options, args) = parser.parse_args()
    
    from gempython.gemplotting.macros.scurvePlottingUtitilities import overlay_scurve
    overlay_scurve(
            vfat=options.vfat, 
            vfatCH=options.strip, 
            fit_filename=options.filename, 
            vfatChNotROBstr=options.channels)
