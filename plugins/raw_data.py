#!/bin/env python3

import os
import hashlib
import json


def _hashfile(filename=""):
	BUF_SIZE = 65536
	md5 = hashlib.md5()
	with open(filename, 'rb') as f:
		while True:
			data = f.read(BUF_SIZE)
			if not data:
				break
			md5.update(data)
	return md5.hexdigest()


def list_datasets():
	files_dict = {}
	for name in os.listdir("./data"):
		file_hash = {}
		file_hash["MD5"] = _hashfile("./data" + "/" + name)
		file_hash["extenstion"] = name.split(".")[-1]
		files_dict[name] = file_hash
	return json.dumps(files_dict)


def _transpose_2D(mat):
	mat_T = [list(x) for x in zip(*mat)]
	return mat_T
