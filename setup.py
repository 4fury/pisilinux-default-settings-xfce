#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from distutils.core import setup

datas = [
    ('/usr/share/applications', glob.glob('applications/*')),
    ('/usr/share/pixmaps', glob.glob('pixmaps/*')),
    ('/usr/share/backgrounds/xfce', glob.glob('xfce/*')),
    ('/etc/xdg/xfce4/xfconf/xfce-perchannel-xml', glob.glob('xfce-perchannel-xml/*')),
    ('share/doc/pardus-default-settings-xfce', ['AUTHORS',
                                                'COPYING',
                                                'README']),
    ]

setup(
    name = 'pardus-default-settings-xfce',
    version = '0.1.4',
    data_files = datas,
    )
