# -*- coding: utf-8 -*-

import os
from tracklib.core.ObsTime import ObsTime
from tracklib.io.TrackReader import TrackReader

# 2015-10-12 17:49:02

ObsTime.setReadFormat("4Y-2M-2D 2h:2m:2s")
resource_path = '/home/marie-dominique/tracklib/tracklib_00_tmp/data'
chemin = os.path.join(resource_path, 'trace10_mm.dat')
track = TrackReader.readFromCsv(chemin, 2, 3, -1, 1, h=1, separator=",")
track.plot()
    