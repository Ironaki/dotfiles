#!/usr/bin/env python3
# coding: utf-8
"""
    Plain text vocab learning tools

Five levels of vocab in files named
1.txt -> 5.txt
(least remembered -> most remembered)

Each file contains following schema:
    | line number | content              |
    |-------------+----------------------|
    | 1           | Timestamp            |
    | 2 -> n      | [Vocab] ** [Details] |
"""

import random
import shutil
from datetime import datetime


def read_file(path):
    """ Read in a file, return list of vocabs (all lines except the first one)

    Args:
        path: path of the file

    Returns:
        vocab_list: list of vocabs
    """
    with open(path, "r") as vocab_file:
        lines = vocab_file.readlines()

    return lines[1:]  # The first line is the time stamp


def split_list(vocab_list, num):
    """ Randomly split vocabs list into
     vocab list to memorize / not to memorize
    (all words if num is larger than the available words)

    Args:
        vocab_list: list of vocabs
        num: number of vocabs to work on

    Returns:
        mem_list: the vocab to work on
        non_mem_list: the vocab not to work on
    """
    line_num = len(vocab_list)
    if line_num < num:  # n of available vocabs < n to work on
        print("There are only {} words. Select all".format(line_num))
        num = line_num

    random.shuffle(vocab_list)
    return vocab_list[:num], vocab_list[num:]


def word_option(word_line):
    """ Show the word. Show details according to the command.

    Args:
        word_line: a line in the original file (one vocab)

    Options:
        d: details if available
        replace: replace the word
        delete: delete the word
        add: add new details for the word

    Return:
        word_line: word, altered if used alter command
        bool: whether or not memorized
    """
    alt_command = ["delete", "replace", "a"]
    y_n = ["y", "n"]
    print("~~~>")

    if "**" not in word_line:  # When there are no details
        print(word_line.strip(" \n　"))
        ans = input("y/n: ")

        if ans in alt_command:  # accept alternative command
            if ans == "delete":
                return "", False
            if ans == "replace":
                new_word = input("Replace with: ")
                word_line = new_word+"\n"
            if ans == "a":
                extra = input("Enter new details: ")
                word_line = word_line.replace("\n", " ** "+extra+"\n")

        while ans not in y_n:
            ans = input("y/n: ")

        return word_line, True if ans == "y" else word_line, False
    else:  # When there are details
        word = word_line.split("**")
        print(word[0].strip(" 　"))
        ans = input("y/n/d: ")

        if ans == "d":  # Show details
            print(word[1].strip(" 　\n"))
            ans = input("y/n: ")

        if ans in alt_command:
            if ans == "delete":
                return "", False
            if ans == "replace":
                new_word = input("Replace with: ")
                word_line = new_word+"\n"
            if ans == "a":
                extra = input("Enter new details: ")
                word_line = word_line.replace("\n", " "+extra+"\n")

        while ans not in y_n:
            ans = input("y/n: ")

        return word_line, True if ans == "y" else word_line, False


def word_run_options(vocab_list):
    """ run word_option for a vocab list
    return stay vocab list/ promotion vocab list
    """
    stay_list = []
    prom_list = []
    for word_line in vocab_list:
        word_line, to_prom = word_option(word_line)
        if word_line:
            if to_prom:
                prom_list.append(word_line)
            else:
                stay_list.append(word_line)
    return stay_list, prom_list


def backup_files(valid_level):
    """ Backup files in "bak" directory
    Record the timestamp in a file

    Args:
        valid_level: [str] List of number of levels
    """
    with open("bak/time", "w") as time_file:
        time_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n")
    for level in valid_level:
        shutil.copy(str(level)+".txt", "bak/")


def choose_level(valid_level, total_level):
    """ User chooses a level
    Return level to work on (int)
    """
    level = 0
    while level not in valid_level:
        level = input("What is the level to review? ")
        # Try to convert to int
        try:
            level = int(level)
        except ValueError:
            print("A valid level is between 1 and {}.".format(total_level))
            level = 0
            continue
        # Try to see if level is valid
        if level not in valid_level:
            print("A valid level is between 1 and {}.".format(total_level))
    return level


def choose_number_of_words():
    """ User chooses number of words to work on
    Return number of words (int)
    """
    num = 0
    while num <= 0 or num >= 30:
        num = input("How many words to work on? ")
        # Try to convert to int
        try:
            num = int(num)
        except ValueError:
            print("Please enter a positive number.")
            num = 0
            continue
        # number is too small ask
        if num <= 0:
            print("Please enter a positive number.")
        # Ask for confirmation if number is large
        if num >= 30:
            print("{} seems a lot.".format(num))
            con = input("Do you want to continue? (y/n) ")
            if con == "y":
                break
    return num


def get_stay_prom_level(level, max_level):
    """ get stay and promotion level of the chosen level

    If a word is not memorized (stay),
    it stays in the level (not max_level), or go to level 1 (max_level)

    If a word is memorized (promotion):
    it promotes to next level (not max_level), or stays (max_level)

    Args:
        level
        max_level

    Return:
        stay_level
        prom_level
    """
    if level == max_level:
        return level, level+1
    return 1, level


def print_instruction():
    """ Print out instruction """
    instruction = """
~~~~~~~~~~~~~~~~~~~~~~~~~~
y/n for memorized or not
d for details if available
a to add details to the word
delete to delete the word
replace to replace the word
~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
    print(instruction)


def write_file(non_mem_list, stay_list, prom_list, stay_level, prom_level):
    """ Write vocab list to file
    If the vocab is not chosen or not memorized,
    it stays in the stay_level file (file get overwritten)

    If the vocab is memorized,
    it is promoted to prom_level file (appended)
    """
    # Overwrite the original file with new timestamp
    with open(str(stay_level)+".txt", "w") as stay_file:
        stay_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n")
        for line in non_mem_list:
            stay_file.write(line)
        for line in stay_list:
            stay_file.write(line)

    # Append memorized word to the higher level file
    with open(str(prom_level)+".txt", "a") as prom_file:
        for line in prom_list:
            prom_file.write(line)


if __name__ == "__main__":

    TOTAL_LEVEL = 5
    VALID_LEVEL = [x for x in range(1, TOTAL_LEVEL+1)]

    # Backup file first
    backup_files(VALID_LEVEL)

    # User input level information
    LEVEL = choose_level(VALID_LEVEL, TOTAL_LEVEL)

    # User input vocab number
    NUM = choose_number_of_words()

    # Display level and num of vocabs information
    print("You want to review {} words at level {}".format(NUM, LEVEL))

    # now read the file
    VOCAB_LIST = read_file(str(LEVEL)+".txt")

    # split into mem and non_mem list
    MEM_LIST, NON_MEM_LIST = split_list(VOCAB_LIST, NUM)

    # get stay and prom level
    STAY_LEVEL, PROM_LEVEL = get_stay_prom_level(LEVEL, TOTAL_LEVEL)

    # print out instruction
    print_instruction()

    # run word option
    STAY_LIST, PROM_LIST = word_run_options(MEM_LIST)

    write_file(NON_MEM_LIST, STAY_LIST, PROM_LIST, STAY_LEVEL, PROM_LEVEL)

    # finish up
    print("(^•ω •^) Great, you worked on {} words, and memorized {}"
          .format(len(MEM_LIST), len(PROM_LIST)))
