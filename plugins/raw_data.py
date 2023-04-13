#!/bin/env python3

from pathlib import Path
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
	for p in Path( './data' ).rglob( '*' ):
		if p.is_file():
			file_hash = {}
			file_hash["location"]=str(p)
			file_hash["MD5"] = _hashfile(p)
			file_hash["extenstion"] = p.suffix[1:]
			files_dict[p.name] = file_hash
	return json.dumps(files_dict)


def _transpose_2D(mat):
	mat_T = [list(x) for x in zip(*mat)]
	return mat_T
