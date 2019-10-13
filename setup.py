#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from distutils.core import setup

datas = [
	('/usr/share/applications', glob.glob('applications/*')),
#	('/usr/share/pixmaps', glob.glob('pixmaps/*')),
#	('/usr/share/backgrounds/xfce', glob.glob('xfce/*')),
	]

setup (
	name = 'pisilinux-default-settings-xfce',
	version = '2.0',
	data_files = datas,
	)
