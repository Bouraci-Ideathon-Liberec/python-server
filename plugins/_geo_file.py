#!/bin/env python3

import shapefile
import numpy as np


def distance(X1, Y1, X2, Y2):
	return np.sqrt(((X1 - X2)**2) + ((Y1 - Y2)**2))


def point_distance(point1: list = [], point2: list = []):
	return distance(point1[0], point1[1], point2[0], point2[1])


def open_file(path):
	return shapefile.Reader(path, encoding="windows-1250")


def get_shaperecords(Shapefile):
	return Shapefile.shapeRecords()


def raw_shape(ShapeRecord):
	data = {}
	data.update(ShapeRecord.record.as_dict())
	data["points"] = ShapeRecord.shape.points
	return data
