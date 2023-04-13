#!/bin/env python3

import shapefile


def open_file(path):
	return shapefile.Reader(path, encoding="windows-1250")


def get_shaperecords(Shapefile):
	return Shapefile.shapeRecords()


def raw_shape(ShapeRecord):
	data = {}
	data.update(ShapeRecord.record.as_dict())
	data["points"] = ShapeRecord.shape.points
	return data
