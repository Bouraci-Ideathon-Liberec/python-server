#!/bin/env python3

import shapefile
import json

_shp = shapefile.Reader("./data/13_Zaplavova_uzemi_povodi_Ohre_LK/PovodiOhre_Q5.shp")

_shapes = _shp.shapes()


def get_points():
	shapes = {}
	for poly in _shapes:
		shapes[str(poly)] = poly.points
	return json.dumps(shapes)
