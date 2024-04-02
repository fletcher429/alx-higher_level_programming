#/usr/bin/python3
"""
Errors and exceptions can lead to program failure or 
unexpected behavior, and Python comes with 
a robust set of tools to improve the stability of the code.
"""


try:
     inp = input()
     print ('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
     print ('Caught KeyboardInterrupt')
else:
     print ('No exception occurred')