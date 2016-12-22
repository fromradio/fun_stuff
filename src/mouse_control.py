#! /bin/env python
# -*- coding: utf-8 -*-
# author: Ruimin Wang, wangruimiN@qiyi.com

from __future__ import print_function
import pyautogui
import sys
sys.stdout.flush()
print("Press Ctrl-C to quit.")

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        sys.stdout.write(positionStr + '\r')
        # print('\b' * len(positionStr), end='')
        sys.stdout.flush()
        pass
except KeyboardInterrupt:
    print('\nDone')
