#!/usr/bin/env python3
# coding: utf-8

import os
import argparse
import re
from pprint import pprint

LEDGER_DIR = os.environ["DROPBOX"]+"/Ledger/"


def read_file(file_path, encoding="utf-8"):
    """ Read the file as list of lines """
    with open(file_path, encoding=encoding) as f:
        text_list = f.readlines()
    return text_list


def write_file(file_path, text_list, encoding="utf-8"):
    """ Write the file """
    with open(file_path, encoding=encoding, mode="w") as f:
        f.writelines(text_list)


def amazon_process(file_path):
    """ Preprocess AmazonCard csv
    Overwrite the file """
    text_list = read_file(file_path, "shift-jis")
    write_file(file_path, text_list[:-3])  # last 3 lines irrelevant


def rakutencard_process(file_path):
    """ Preprocess RakutenCard csv
    Overwrite the file """
    text_list = read_file(file_path, "shift-jis")
    write_file(file_path, text_list)


def shinsei_process(file_path):
    """ Process Shinsei csv
    Overwirte the file """
    text_list = read_file(file_path, "utf-16")
    write_file(file_path, text_list[8:])


def mitsui_process(file_path):
    """ Process Mitsui csv
    Overwirte the file """
    text_list = read_file(file_path, "shift-jis")
    line_start = re.compile("^R(\d\d)")
    for i, line in enumerate(text_list[1:-1]):
        year = line_start.match(line).group(1)
        new_line = re.sub(line_start,
                          reiwa_to_western(year),
                          line)
        text_list[i+1] = new_line
    write_file(file_path, text_list[:-1])


def rakutenbank_process(file_path):
    """ Process RakutenBank csv
    Overwirte the file """
    text_list = read_file(file_path, "shift-jis")
    write_file(file_path, text_list)


def alipay_process(file_path):
    """ Process AliPay csv
    Overwrite the file"""
    text_list = read_file(file_path, "gb18030")
    write_file(file_path, text_list[4:-7])


def wechat_process(file_path):
    """ Process WeChat csv
    Overwrite the file """
    text_list = read_file(file_path)
    text_list = text_list[16:]
    text_list = [line.replace("¥", "") for line in text_list]
    for i, line in enumerate(text_list):
        text_list[i] = line.replace("收入,", "收入,-")
    write_file(file_path, text_list)


def reiwa_to_western(year, input_type=str):
    """ Change reiwa year to western year """
    if input_type == str:
        return str(2018+int(year))
    if input_type == int:
        return 2018+year
    raise TypeError("Input type is not supported")


def arg_parser():
    desc = "Preprocess csv files to be used in icsv2ledger"
    parser = argparse.ArgumentParser(prog="Ledger Preprocessor",
                                     description=desc)
    parser.add_argument("file_path",
                        nargs="+",
                        metavar="FILE",
                        type=str)
    parser.add_argument("-m", "--method",
                        choices=["amazon", "rakutencard",
                                 "shinsei", "mitsui", "rakutenbank",
                                 "alipay", "wechat"],
                        required=True,
                        help="choose a method of preprocessing")
    args = parser.parse_args()
    return args


def main_run():
    args = arg_parser()
    # cur_dir = os.getcwd()+'/'

    for fp in args.file_path:
        if args.method == "amazon":
            amazon_process(fp)
        if args.method == "shinsei":
            shinsei_process(fp)
        if args.method == "mitsui":
            mitsui_process(fp)
        if args.method == "rakutencard":
            rakutencard_process(fp)
        if args.method == "alipay":
            alipay_process(fp)
        if args.method == "rakutenbank":
            rakutenbank_process(fp)
        if args.method == "wechat":
            wechat_process(fp)


if __name__ == "__main__":

    main_run()
