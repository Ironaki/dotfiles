#!/usr/bin/env python3
import os
from datetime import date, time, timedelta
from bisect import bisect_left


def parse_row(row):
    row_split = row.split(" ")
    return date.fromisoformat(row_split[0]), int(row_split[1])


def range_sum(records, start_date, end_date):
    """

    :param start_date: inclusive
    :param end_date: exclusive
    :return:
    """
    start_index = bisect_left(records, start_date, key=lambda r: r[0])
    end_index = bisect_left(records, end_date, key=lambda r: r[0])
    time_sum = sum(r[1] for r in records[start_index:end_index])
    return time_sum
    # return time_sum


def summary(records):
    today = date.today()

    def summary_once(start_date, end_date):
        time_sum = range_sum(records, start_date, end_date)
        hours, minutes = time_sum // 60, time_sum % 60
        print(
            f"{str(hours).rjust(3, ' ')}:{str(minutes).rjust(2, '0')}  {start_date} ~ {end_date-timedelta(days=1)}"
        )

    print("Weekly Progress in the Last Four Weeks:")
    for i in range(4):
        start_date = today - timedelta(weeks=i + 1)
        end_date = today - timedelta(weeks=i)
        summary_once(start_date, end_date)

    print()
    print("Monthly Progress in the Last Four Months:")
    for i in range(4):
        start_date = today - timedelta(days=30 * (i + 1))
        end_date = today - timedelta(days=30 * i)
        summary_once(start_date, end_date)


home_dir = os.getenv("HOME")
file_path = f"{home_dir}/Dropbox/Guitar/time.txt"

if __name__ == "__main__":
    with open(file_path) as f:
        file_rows = f.read().split("\n")
        records = [parse_row(row) for row in file_rows if row]
        summary(records)
