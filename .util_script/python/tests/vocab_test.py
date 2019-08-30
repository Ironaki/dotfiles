# coding: utf-8

import sys
sys.path.append("../src")

import vocab
import random

file1_path = "files/1.txt"


def test_split_list():
    vocab_list_c1 = vocab.read_file(file1_path)
    vocab_list_c2 = vocab.read_file(file1_path)
    vocab_list_c3 = vocab.read_file(file1_path)
    vocab_list_c4 = vocab.read_file(file1_path)
    random.seed(42)
    mem_list_exp42 = ['孤児院\n', '釘付け **（くぎづけ）\n', 'たらし込む\n', '下見\n']
    non_mem_list_exp42 = ['ぐうだら **\u3000*口*\n', 'なりふり **\u3000『なりふり構わない』\n', '良し悪し **（よしあし）\n', 'うっぷん **（鬱憤）\n', '遮る ** （さえぎる）\n', '手並み\n']
    mem_list, non_mem_list = vocab.split_list(vocab_list_c1, 4)
    assert mem_list == mem_list_exp42
    assert non_mem_list == non_mem_list_exp42
    random.seed(42)
    mem_list_2, non_mem_list_2 = vocab.split_list(vocab_list_c2, 10)
    random.seed(42)
    mem_list_3, non_mem_list_3 = vocab.split_list(vocab_list_c3, 10)
    assert (mem_list_2, non_mem_list_2) == (mem_list_3, non_mem_list_3)
    random.seed(7)
    mem_list_4, non_mem_list_4 = vocab.split_list(vocab_list_c4, 10)
    assert (mem_list_2, non_mem_list_2) != (mem_list_4, non_mem_list_4)
    
if __name__ == "__main__":
    # Test choose_level
    TOTAL_LEVEL = 5
    VALID_LEVEL = [x for x in range(1, TOTAL_LEVEL+1)]
    level = vocab.choose_level(VALID_LEVEL, TOTAL_LEVEL)
    print("SUCCESS! choose_level returns:", level)
    # Test choose_number_of_words    
    num = vocab.choose_number_of_words()
    print("SUCESS! choose_number_of_words:", num)
