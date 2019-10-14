#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, glob
from distutils.core import setup

datas = [
	('/usr/share/applications', glob.glob('applications/*')),
	('/etc/skel/.config', ['xfce-mimeapps.list']),
	('/etc/xdg/xfce4/scripts', ['additional-logout']),
	('/etc/xdg/autostart', ['additional-logout.desktop']),
#	('/usr/share/pixmaps', glob.glob('pixmaps/*')),
#	('/usr/share/backgrounds/xfce', glob.glob('xfce/*')),
	]

setup (
	name = 'pisilinux-default-settings-xfce',
	version = '2.0',
	data_files = datas,
	)
