import sys
principal=float(sys.argv[1])                     #0 is place whaere pgm or file is stored .
rate=float(sys.argv[2])
time=float(sys.argv[3])
interest=(principal * rate * time)/100
print("Simple Intrest:",interest)