import glob

def separate(odd, even):
    """
    separates numbers from the files into even and odd numbers.
    returns odd_nums.txt and even_nums.txt
    """
    for filename in glob.glob("nums*.txt"):
        f = open(filename,"r")
        for line in f:
            num = line.strip("\n")
            if int(num)%2==0:
                even.write(num+"\n")
            else:
                odd.write(num+"\n")

    even.close()
    odd.close()

if __name__ == "__main__":
    odd = open("odd_nums.txt","a")
    even = open("even_nums.txt","a")
    separate(odd, even)