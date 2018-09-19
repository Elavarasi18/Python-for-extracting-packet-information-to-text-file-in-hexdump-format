import argparse
import numpy as np
import os.path
from pcapfile import savefile
import pathlib
import SaveHex
import sys

#   Argument
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str,
                    help="Input File")
parser.add_argument("-o", "--output", type=str,
                    help="Output File")
args = parser.parse_args()

input_file = args.input
output_file = args.output
print(input_file)
print(output_file)
#   Argument control
if type(input_file) == str and type(input_file) == str:
    pass
else:
    print('Arguments are not string')
    exit(0)
if os.path.isfile(input_file):
    pass
else:
    print('Input file cant find')
    exit(0)
#if os.path.isfile(output_file):
#    pass
#else:
#    print('Output file cant find')
#    exit(0)
#   ##############################333

#   ######################################################
test_cap = open(input_file, 'rb')
cap_file = savefile.load_savefile(test_cap, verbose=True)
pkt = cap_file.packets[0].packet

#   print(pkt)
#   print(pkt.timestamp)
data = np.frombuffer(pkt, dtype=np.int8)
#   print(pkt.raw())
#   print(capfile.packets[0].packet.payload)

str_hex = str(pkt)
str_hex = str_hex[2:-1]
s=str_hex
#s=int(s,16)
#s= str(str_hex.b16decode(hex_data))[2:-1]
s.encode('ascii','str_hex')
result = bytes.fromhex(s)
s = list(result)
a = np.array(s, dtype=int)
hex_W = SaveHex.SaveHex(a, output_file)
hex_W.save_data()
