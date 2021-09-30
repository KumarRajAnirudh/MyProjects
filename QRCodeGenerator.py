# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:48:17 2021

@author: Kumar
"""

import qrcode
img = qrcode.make("Hi Hello How are you")
img.save("QR2.jpg")