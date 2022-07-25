#!/usr/bin/env python3
# coding: utf-8
"""
    Plain text vocab learning tools

Five levels of vocab in files named
1.txt -> 5.txt
(least remembered -> most remembered)
"""

import random
import shutil
from datetime import datetime
from urllib import parse


class Vocab:
    def __init__(self, vocab_list):
        self.vocab = vocab_list[0].strip()
        self.details = vocab_list[1:]

    def print_vocab(self):
        print(self.vocab)

    def print_details(self):
        print("\n".join(line.strip() for line in self.details))

    def print_weblio_url(self):
        encoded_vocab = parse.quote(self.vocab.encode())
        print(f"https://www.weblio.jp/content/{encoded_vocab}")

    def set_details(self, details):
        self.details = [f"{details}\n"]

    def has_details(self):
        return "".join(self.details).strip() != ""

    def get_prompt(self):
        if self.has_details():
            return "y/n or m/d/a (more/delete/add detail) ~~~> "
        else:
            return "y/n or d/a (delete/add detail) ~~~> "

    def write_to_file(self, f):
        f.write(self.vocab + "\n")
        f.writelines(self.details + ["\n"])

    def __repr__(self):
        return "\n".join([self.vocab] + self.details)


def read_file(path):
    """Read in a file, return list of Vocab

    Args:
        path: path of the file

    Returns:
        vocab_list: list of Vocab
    """
    with open(path, "r") as vocab_file:
        lines = vocab_file.readlines()

    lines = lines[1:] + [
        ""
    ]  # The first line is the timestamp. Add "" as the delimiter of the last one
    vocabs = []
    vocab_lines = []
    for line in lines:
        if line.strip() == "":  # delimiter between vocabularies is an empty line
            if vocab_lines:
                vocabs.append(Vocab(vocab_lines))
            vocab_lines = []
        else:
            vocab_lines.append(line)
    return vocabs


def split_list(vocab_list, num):
    """Randomly split vocabs list into
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
        print(f"There are only {line_num} words. Select all.")
        num = line_num

    random.shuffle(vocab_list)
    return vocab_list[:num], vocab_list[num:]


def word_option(vocab: Vocab):
    """Show the word. Show details according to the command.

    Args:
        word_line: a line in the original file (one vocab)

    Options:
        d: details if available
        replace: replace the word
        delete: delete the word
        add: add new details for the word

    Return:
        word_line: word, altered if used alter command
        bool: memorized or not
    """
    alt_command = ["m", "d", "a"]
    y_n = ["y", "n"]

    print("~~~>")
    vocab.print_vocab()
    print("")
    vocab.print_weblio_url()
    print("")
    ans = input(vocab.get_prompt())
    while ans not in y_n:
        if ans in alt_command:
            if ans == "d":
                return None, True
            if ans == "m":
                vocab.print_details()
            if ans == "a":
                details = input("Enter new details: ")
                vocab.set_details(details)
        ans = input(vocab.get_prompt())

    return vocab, ans.strip() == "y"


def word_run_options(vocab_list):
    """run word_option for a vocab list
    return stay vocab list/ promotion vocab list
    """
    stay_list = []
    prom_list = []
    for vocab in vocab_list:
        vocab, to_prom = word_option(vocab)
        if vocab:
            if to_prom:
                prom_list.append(vocab)
            else:
                stay_list.append(vocab)
    return stay_list, prom_list


def backup_files(valid_level):
    """Backup files in "bak" directory
    Record the timestamp in a file

    Args:
        valid_level: [str] List of number of levels
    """
    with open("bak/time", "w") as time_file:
        time_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    for level in valid_level:
        shutil.copy(str(level) + ".txt", "bak/")


def choose_level(valid_level, total_level):
    """User chooses a level
    Return level to work on (int)
    """
    level = 0
    while level not in valid_level:
        level = input("What is the level to review? ")
        # Try to convert to int
        try:
            level = int(level)
        except ValueError:
            print(f"A valid level is between 1 and {total_level}.")
            level = 0
            continue
        # Try to see if level is valid
        if level not in valid_level:
            print(f"A valid level is between 1 and {total_level}.")
    return level


def choose_number_of_words():
    """User chooses number of words to work on
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
    """get stay and promotion level of the chosen level

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
    if level != max_level:
        return level, level + 1
    return 1, level


def write_file(non_mem_list, stay_list, prom_list, stay_level, prom_level):
    """Write vocab list to file
    If the vocab is not chosen or not memorized,
    it stays in the stay_level file (file get overwritten)

    If the vocab is memorized,
    it is promoted to prom_level file (appended)
    """
    # Overwrite the original file with new timestamp
    with open(str(stay_level) + ".txt", "w") as stay_file:
        stay_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for vocab in non_mem_list + stay_list:
            vocab.write_to_file(stay_file)

    # Append memorized word to the higher level file
    with open(str(prom_level) + ".txt", "a") as prom_file:
        for vocab in prom_list:
            vocab.write_to_file(prom_file)


def main():
    total_level = 5
    valid_level = [x for x in range(1, total_level + 1)]

    # Backup file first
    backup_files(valid_level)

    # User input level information
    level = choose_level(valid_level, total_level)

    # User input vocab number
    num = choose_number_of_words()

    # Display level and num of vocabs information
    print(f"You want to review {num} words at level {level}")

    # now read the file
    vocab_list = read_file(str(level) + ".txt")

    # split into mem and non_mem list
    mem_list, non_mem_list = split_list(vocab_list, num)

    # get stay and prom level
    stay_level, prom_level = get_stay_prom_level(level, total_level)

    # run word option
    stay_list, prom_list = word_run_options(mem_list)

    write_file(non_mem_list, stay_list, prom_list, stay_level, prom_level)

    # finish up
    print(
        f"(^•ω •^) Great, you worked on {len(mem_list)} words, and memorized {len(prom_list)}"
    )


if __name__ == "__main__":
    main()
