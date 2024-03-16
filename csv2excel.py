
"""
Builder: This module is called from outside and calls builder to load csv and convert into xlsx
"""
import sys

from src.eib_builder import BusinessProcessType, EibBuilder
from src.load_input_data import LoadInputData


def __init():
    if len(sys.argv) < 2:
        print("input file name is missing, please pass filename as the first argument.")
    else:
        populate_data:list[BusinessProcessType] = [BusinessProcessType.JOB_CHANGE, BusinessProcessType.COMPENSATION,BusinessProcessType.CHANGE_ORG,BusinessProcessType.ASSIGN_PAYGROUP,BusinessProcessType.CHANGE_PERSONAL_INFO,BusinessProcessType.ASSIGN_ROLES]

        EibBuilder.build(LoadInputData.load_csv(sys.argv[1]),populate_data=populate_data)
__init()
