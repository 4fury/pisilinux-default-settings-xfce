#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from distutils.core import setup

datas = [
    ('/usr/share/applications', glob.glob('applications/*')),
    ('/usr/share/pixmaps', glob.glob('pixmaps/*')),
    ('/usr/share/backgrounds/xfce', glob.glob('xfce/*')),
    ('/etc/xdg/xfce4/xfconf/xfce-perchannel-xml', glob.glob('xfce-perchannel-xml/*')),
    ('share/doc/pisilinux-default-settings-xfce', ['COPYING',
                                                'README']),
    ]

setup(
    name = 'pisilinux-default-settings-xfce',
    version = '1.0',
    data_files = datas,
    )
