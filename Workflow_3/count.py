import sys

def count(input_file, output_file):
    """
    counts the numbers in the input file and writes it to the output file.
    """
    inp_file = open(input_file,"r")
    num_list = inp_file.readlines()
    inp_file.close()

    out_file = open(output_file,"w")
    out_file.write(str(len(num_list)))
    out_file.close()

if __name__ == "__main__":
    
    input_file, output_file = sys.argv[1:]
    count(input_file, output_file)