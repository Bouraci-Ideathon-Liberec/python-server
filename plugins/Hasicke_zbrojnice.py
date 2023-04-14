#!/bin/env python3

from . import _geo_file
import json
import pandas as pd

File = "./data/hasicke_zbrojnice/Hasičské_zbrojnice_v_Libereckém_kraji.csv"
df = pd.read_csv(File)


def table():
	temp = json.loads(df.to_json(orient="index"))

	row_list = []
	for key in temp.keys():
		row_list.append(temp[key])

	return json.dumps(row_list)


def get_closest(X: float = 0, Y: float = 0):
	X_list = list(df["X"])
	Y_list = list(df["Y"])
	point_list = []
	compare = []
	compare.append(X)
	compare.append(Y)

	for i in range(len(X_list)):
		point = []
		point.append(X_list[i])
		point.append(Y_list[i])
		point_list.append(point)

	dist = 999999
	saved_index = len(point_list)
	for i in range(len(point_list)):
		new_dist = _geo_file.point_distance(compare, point_list[i])
		if new_dist < dist:
			dist = new_dist
			saved_index = i

	return json.dumps(_geo_file.normalize_dict(df.loc[saved_index].to_dict()))
