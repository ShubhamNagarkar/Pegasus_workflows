#!/usr/bin/env python3
import emoji
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="arguments for emojify")
    parser.add_argument('--i', type=str, help='enter input file name')
    parser.add_argument('--o', type=str, help='enter output file name')
    args = parser.parse_args()
    input_file = args.i
    output_file = args.o
    
    f1 = open(input_file,"r")
    line = f1.readline().strip('\n')
    line = emoji.emojize(line+' :thumbs_up:')
    f1.close()
   
    f2 = open(output_file,"w")
    f2.write(line)
    f2.close()