#!/Users/Armstrong/anaconda/bin/python

from sys import argv
import os


def alnum(words):  #  Make the list of word alnum and lower
    if not words:
        return invalid()

    for i in range(len(words)):
        words[i] = "".join([c.lower() for c in words[i] if c.isalnum()])

    return words


def alnum_python(words):
    clean = alnum(words)
    clean[0] = clean[0].rjust(4, '0')
    return "_".join(clean)


def alnum_java(words):
    clean = alnum(words)
    rest = "".join([x.capitalize() for x in clean[2:]])
    head = "Q"+clean[0].rjust(4, '0')+"_"+clean[1]
    return head+rest


def invalid():
    print("Invalid input")
    exit()


if __name__ == "__main__":

    if len(argv) < 2:
        invalid()

    lc_dir = os.environ["HOME"] + "/Dropbox/Programming/LeetCode/"
    flags = ["-p", "-j"]

    if argv[1] not in flags:
        print("Please use the following flags:")
        print(flags)

    if argv[1] == "-p":
        name = alnum_python(argv[2:])
        print(name)
        file_name = lc_dir+"Python/"+name+".py"
        if os.path.isfile(file_name):
            print("File exists!")
        else:
            with open(file_name, "w") as file:
                file.write("from lib import *\n\n")
            print("Created new file!")

    if argv[1] == "-j":
        name = alnum_java(argv[2:])
        print(name)
        file_name = lc_dir+"Java/"+name+".java"
        if os.path.isfile(file_name):
            print("File exists!")
        else:
            with open(file_name, "w") as file:
                file.write("package Java;\n\nimport org.junit.jupiter.api.Test;\nimport static org.junit.jupiter.api.Assertions.*;\nimport java.util.*;\n\n")
                file.write("public class "+name+" {\n}")
            print("Created new file")
