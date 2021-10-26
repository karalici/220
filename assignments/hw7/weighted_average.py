"""
Name: Iva Karalic
weighted_average.py

Problem: It calculates the weighted average and it writes it in a new file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    class_acc = 0
    class_av_acc = 0
    for line in infile:
        newline = line.split(": ")
        name = newline[0].split()
        grade = newline[1].split()
        weight_acc = 0
        score_acc = 0
        full_name = " ".join(name)
        outfile.write(full_name + "'s average: ")
        for i in range(0, len(grade), 2):
            weight_acc += int(grade[i])
        if weight_acc < 100:
            outfile.write("Error: The weights are less than 100. \n")
        elif weight_acc > 100:
            outfile.write("Error: The weights are more than 100. \n")
        else:
            class_acc += 1
            for i in range(0, len(grade), 2):
                score_acc += int(grade[i]) * int(grade[i+1]) / 100
                class_av_acc += score_acc
            outfile.write(str(round(score_acc, 1)) + "\n")
    outfile.write("Class average: " + str(round(class_av_acc/class_acc)))


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == "__main__":
    main()
