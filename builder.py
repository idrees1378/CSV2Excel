
"""
Builder: This module is called from outside and calls builder to load csv and convert into xlsx
"""
import sys
import src.csv2excel as loader

def __init():
    if len(sys.argv) < 2:
        print("input file name is missing, please pass filename as the first argument.")
    else:
        loader.build(sys.argv[1])
__init()
