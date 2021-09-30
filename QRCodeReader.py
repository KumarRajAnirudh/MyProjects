# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:56:25 2021

@author: Kumar
"""

import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("QR2.jpg"))
print("Decoded text is: ", val)