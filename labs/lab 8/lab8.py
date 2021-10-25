"""
Name: Iva Karalic
lab8.py
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(i) + " "+ str(word) + "\n")
            i += 1
    infile.close()
    outfile.close()


def hourly_wage(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    for line in infile:
        parts = line.split()
        wage = float(parts[2])
        wage += 1.65
        wage = wage * int(parts[3])
        outfile.write(str(parts[0]) +" " + str(parts[1]) + " " + str(wage) +  "\n")
    infile.close()
    outfile.close()

def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        position = 10 - i
        acc += int(isbn[i]) * position
    return acc

def send_message(file, friend):
    infile=  open(file, "r")
    outfile = open(friend + ".txt" , "w+")
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()

def send_safe_message(file,friend,key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(encode(line, key))
    infile.close()
    outfile.close()

def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    pad_file = open(pad, "r")
    key = pad_file.read()
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(encode_better(line, key))
    infile.close()
    pad_file.close()
    outfile.close()


def main():
    # add other function calls here
    # number_words("Walrus.txt", "walrus_out.txt")
    # hourly_wage("hourly_wages.txt", "hourly_wages_out")
    # calc_check_sum("0072946520")
    # send_message("message.txt", "bob")
    # send_safe_message("secret_message.txt","kelly", 3)
    send_uncrackable_message("safest_message.txt", "aly", "pad.txt")



