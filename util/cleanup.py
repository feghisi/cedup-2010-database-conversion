# -*- coding: iso-8859-1 -*-
import os, sys, re

exclude_filename_list = [
	'CVS'
]

remove_ext_list = [
	".core",
	".pyc",
	".pyo",
	".bak",
	".swp",
]

remove_rexp_list = [
	re.compile(".#.*"),
	re.compile(".*\~$"),
]

def walkman(arg, dirname, file_list):
	for k in exclude_filename_list:
		if k in file_list:
			file_list.remove(k)
	
	dirname = dirname[2:]

	if dirname:
		dirname = dirname.split("/")
	else:
		dirname = []

	for filename in file_list:
		fullname = "/".join(dirname + [filename])
		basename, ext = os.path.splitext(filename)
		
		if ext in remove_ext_list:
			print fullname
			os.unlink(fullname)
		else:
			for fileRE in remove_rexp_list:
				if fileRE.match(filename):
					print fullname
					os.unlink(fullname)

os.path.walk("./", walkman, None)
