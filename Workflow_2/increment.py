#!/usr/bin/env python3
import sys

def increment(input_file, output_file):
    """
    Reads number from input_file and increments it and writes it to output_file
    """
    inp_file = open(input_file,"r")
    num = int(inp_file.readline())
    inp_file.close()

    out_file = open(output_file,"w")
    out_file.write(str(num+1))
    out_file.close()

if __name__ == "__main__":
    
    input_file, output_file = sys.argv[1:]
    increment(input_file, output_file)
