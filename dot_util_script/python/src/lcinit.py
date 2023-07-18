#!/usr/bin/env python3

import argparse
import os

try:
    LC_DIR = os.environ["LEETCODE"] + "/"
except:
    LC_DIR = os.environ["DROPBOX"] + "/Programming/LeetCode/"


def alnum(word_list):
    """Change the list of words to lower case words that is alphanumeric

    e.g.
       ['25.', 'Reverse', 'Nodes', 'in', 'k-Group']
       ==>
       ['25', 'reverse', 'nodes', 'in', 'kgroup']
    """
    for i, word in enumerate(word_list):
        word_list[i] = "".join(char.lower() for char in word if char.isalnum())
    return word_list


def alnum_python(words):
    """Generate python style question name

    e.g.
        ['25.', 'Reverse', 'Nodes', 'in', 'k-Group']
        ==>
        ['25', 'reverse', 'nodes', 'in', 'kgroup']
        ==>
        "0025_reverse_nodes_in_kgroup"
    """
    clean = alnum(words)
    clean[0] = clean[0].rjust(4, "0")
    return "_".join(clean)


def alnum_java(words):
    """Generate java style question name

    e.g.
        ['25.', 'Reverse', 'Nodes', 'in', 'k-Group']
        ==>
        ['25', 'reverse', 'nodes', 'in', 'kgroup']
        ==>
        "Q0025_reverseNodesInKgroup"
    """

    clean = alnum(words)
    rest = "".join(x.capitalize() for x in clean[2:])
    head = "Q" + clean[0].rjust(4, "0") + "_" + clean[1]
    return head + rest


def python_output(question_name, stdout):
    """print out python file name and template
    or create a new python file in python LC_DIR

    Args:
        question_name: processed question name
        stdout: Whether to print out
    """
    init_template = [
        "from Python.lib import *",
        "from typing import *",
        "from collections import *",
        "from heapq import *",
        "from random import *",
        "from bisect import *",
        "from itertools import *",
        "",
        "",
        "class Solution:",
        "",
    ]
    init_template = "\n".join(line for line in init_template)
    print(question_name)
    print("====================")
    if stdout:
        print(init_template)
    else:
        file_name = LC_DIR + "Python/" + question_name + ".py"
        if os.path.isfile(file_name):
            print("File exists!")
        else:
            with open(file_name, "w") as target_file:
                target_file.write(init_template)
            print("Created new Python file!")


def java_output(question_name, stdout):
    """print out java file name and template
    or create a new java file in java LC_DIR

    Args:
        question_name: processed question name
        stdout: Whether to print out
    """
    init_template = [
        "import org.junit.jupiter.api.Test;",
        "import static org.junit.jupiter.api.Assertions.*;",
        "import java.util.*;",
        "",
        "",
        "public class " + question_name + " {",
        "}",
        "",
    ]
    init_template = "\n".join(line for line in init_template)
    print(question_name)
    print("====================")
    if stdout:
        print(init_template)
    else:
        file_name = LC_DIR + "Java/" + question_name + ".java"
        if os.path.isfile(file_name):
            print("File exists!")
        else:
            with open(file_name, "w") as target_file:
                target_file.write(init_template)
            print("Created new Java file!")


def arg_parser():
    """Parse command line argument"""
    parser = argparse.ArgumentParser(
        prog="lcinit", description="Initiate LeetCode files"
    )
    # Raw string
    parser.add_argument("raw_string", nargs="+", metavar="STRING", type=str)
    # # Old Version Control Flow
    # # File extension, required, support [python, java]
    # parser.add_argument("-e", "--extension",
    #                     choices=["py", "java"],
    #                     required=True,
    #                     help="extension of the file to be generated")
    parser.add_argument(
        "-p",
        "--python",
        action="store_true",
        default=False,
        help="generate python file",
    )
    parser.add_argument(
        "-j", "--java", action="store_true", default=False, help="generate java file"
    )
    # Flag. Whether print to stdout or write to a file
    parser.add_argument(
        "-o",
        "--stdout",
        action="store_true",
        default=False,
        help="print to stdout, default to file",
    )
    args = parser.parse_args()
    return args


def main_run():
    args = arg_parser()

    # if args.extension == "py":  # e for extension
    #     # raw_string: input from command line
    #     question_name = alnum_python(args.raw_string)
    #     # stdout: boolean. True => to stdout; False => to file
    #     python_output(question_name, args.stdout)
    # if args.extension == "java":
    #     question_name = alnum_java(args.raw_string)
    #     java_output(question_name, args.stdout)

    # Flag for each language. Can generate files for multiple language
    def print_sep_line():
        sep_str_ls = ["", "~~~~~~~~~~", ""]
        print("\n".join(sep_str_ls))

    if args.python:
        question_name = alnum_python(args.raw_string)
        # stdout: boolean. True => to stdout; False => to file
        python_output(question_name, args.stdout)
        print_sep_line()
    if args.java:
        question_name = alnum_java(args.raw_string)
        java_output(question_name, args.stdout)
        print_sep_line()
    if not (args.java or args.python):
        print("No file is generated. Please add language flag, e.g. [-p], [-j]")


if __name__ == "__main__":
    main_run()
