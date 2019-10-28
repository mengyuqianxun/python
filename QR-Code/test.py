# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:10:34 2019

@author: 顾南城
"""
import os
from MyQR import myqr

version, level, qr_name = myqr.run(
    'https://github.com/mengyuqianxun',
    version=1,
    level='H',
    
    picture='mengyuqianxun.jpg',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='example1.jpg',
    save_dir=os.getcwd()
	)