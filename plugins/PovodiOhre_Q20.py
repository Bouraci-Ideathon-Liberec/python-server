#!/bin/env python3

from . import _geo_file
import json

_shapes = _geo_file.get_shaperecords(_geo_file.open_file("./data/13_Zaplavova_uzemi_povodi_Ohre_LK/PovodiOhre_Q20.shp"))


def get_points(index: int = -1):

	shapes = {}
	if index == -1:
		for shape in _shapes:
			shapes[str(shape.shape)] = shape.shape.points
	else:
		shape = _shapes[index]
		shapes[str(shape.shape)] = shape.shape.points
	return json.dumps(shapes)


def get_info(index: int = -1):
	shapes = {}

	if index == -1:
		for shape in _shapes:
			shapes[str(shape.record.oid)] = shape.record.as_dict()
	else:
		shape = _shapes[index]
		shapes[str(shape.record.oid)] = shape.record.as_dict()
	return json.dumps(shapes)


def get_shape(index: int = 0):
	shape = _shapes[index]
	return json.dumps(_geo_file.raw_shape(shape))


def num_of_shapes():
	return json.dumps(len(_shapes))
