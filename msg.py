#!/usr/bin/env python
from sense_hat import SenseHat
import sys

s = SenseHat()

msg = str(sys.argv[1])

s.show_message(msg)

