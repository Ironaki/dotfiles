#!/usr/bin/env python3
# coding: utf-8
"""
    Preprocess csv for icsv2ledger

Work flow:

[-m, --method] flag is required from command line

==>

main_run() WITH method_flag passed, e.g. method_flag = "amazon"

==>

<method_flag>_process(), e.g. amazon_process()

==>

read_file() -> processing for the method -> write_file()

"""

import argparse
import re


def read_file(file_path, encoding="utf-8"):
    """Read the file, return list of lines"""
    with open(file_path, encoding=encoding) as f:
        text_list = f.readlines()
    return text_list


def write_file(file_path, text_list, encoding="utf-8"):
    """Write the file from list of lines"""
    with open(file_path, encoding=encoding, mode="w") as f:
        f.writelines(text_list)


def amazon_process(file_path):
    """Preprocess AmazonCard csv. Overwrite the file"""
    text_list = read_file(file_path, "shift-jis")
    for i, text in enumerate(text_list):
        words = text.split(",")
        if words[1] == "ZWIFT":
            words[2] = words[3]
            text_list[i] = ",".join(words)
    write_file(file_path, text_list[:-3])  # last 3 lines irrelevant


def rakutencard_process(file_path):
    """Preprocess RakutenCard csv, overwrite the file"""
    text_list = read_file(file_path)
    write_file(file_path, text_list)


def shinsei_process(file_path):
    """Process Shinsei csv, overwrite the file"""
    text_list = read_file(file_path, "utf-16")  # Uncommon encoding
    write_file(file_path, text_list[8:])


def mitsui_process(file_path):
    """Process Mitsui csv, overwrite the file"""
    text_list = read_file(file_path, "shift-jis")
    # Sample line start :R01.08.01
    # line_start = re.compile("^R(\d\d)")
    # for i, line in enumerate(text_list[1:-1]):
    #     # Workaround for group in sub doesn't work
    #     year = line_start.match(line).group(1)
    #     # replace Japanese year to western year
    #     new_line = re.sub(line_start,
    #                       reiwa_to_western(year),
    #                       line)
    #     text_list[i+1] = new_line
    write_file(file_path, text_list)


def rakutenbank_process(file_path):
    """Process RakutenBank csv, overwirte the file"""
    text_list = read_file(file_path, "shift-jis")
    write_file(file_path, text_list)


def alipay_process(file_path):
    """Process AliPay csv, overwrite the file"""
    text_list = read_file(file_path, "gb18030")
    write_file(file_path, text_list[4:-7])


def wechat_process(file_path):
    """Process WeChat csv, overwrite the file"""
    text_list = read_file(file_path)
    text_list = text_list[16:]
    text_list = [line.replace("¥", "") for line in text_list]  # Take out ¥ sign
    # Edge Cases for wechat, What's wrong with Tencent engineers...
    text_list = [
        line.replace("TSURUHA CO.,LTD", "TSURUHA CO.LTD") for line in text_list
    ]
    for i, line in enumerate(text_list):
        # Make income negative compare to expense
        text_list[i] = line.replace("收入,", "收入,-")
    write_file(file_path, text_list)


# def reiwa_to_western(year, input_type=str):
#     """ Change reiwa year to western year """
#     if input_type == str:
#         return str(2018+int(year))
#     if input_type == int:
#         return 2018+year
#     raise TypeError("Input type is not supported")


def arg_parser():
    desc = "Preprocess csv files to be used in icsv2ledger"
    parser = argparse.ArgumentParser(prog="Ledger Preprocessor", description=desc)
    parser.add_argument("file_path", nargs="+", metavar="FILE", type=str)
    # Required method for processing the csv file
    # each flag in choices corresponds to one *_process function
    parser.add_argument(
        "-m",
        "--method",
        choices=[
            "amazon",
            "rakutencard",
            "shinsei",
            "mitsui",
            "rakutenbank",
            "alipay",
            "wechat",
        ],
        required=True,
        help="choose a method of preprocessing",
    )
    args = parser.parse_args()
    return args


def main_run():
    args = arg_parser()

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
