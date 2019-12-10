#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from distutils.core import setup

datas = [
	('/etc/env.d', ['etc/env/80xfce_specific']),
	('/etc/skel/.config', ['etc/skel/xfce-mimeapps.list']),
	('/etc/xdg/xfce4/scripts', ['etc/xdg/additional-logout']),
	('/etc/xdg/autostart', ['etc/xdg/additional-logout.desktop']),
	('/usr/share/applications', glob.glob('usr/*')),
#	('/usr/share/pixmaps', glob.glob('art/pixmaps/*')),
#	('/usr/share/backgrounds/xfce', glob.glob('art/wallpapers/*')),
	]

setup (
	name = 'pisilinux-default-settings-xfce',
	version = '2.0',
	data_files = datas,
	)

