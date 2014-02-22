from distutils.core import setup
import py2exe
import os

image_files = ["res/base.png", "res/button.png", "res/shoulder_left.png", "res/shoulder_right.png", "res/stick.png"]

setup(
	name = "360 Pad Viewer",
	version = "0.6",
	description = "Works for the Xbox 360 controller on PC",
	data_files = [
		("res", image_files),
		("", ["config.txt"])
	],
	options = {},
	windows =[{
		"script": "main.py",
		"icon_resources": [(1, "icon.ico")]
	}],
	zipfile = None
)