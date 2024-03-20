"""
Builder: This module is called from outside and calls builder to load csv and convert into xlsx
"""
import sys

from src.constants import BusinessProcessType
from src.eib_builder import EibBuilder
from src.load_input_data import LoadInputData


def __init():
    if len(sys.argv) < 2:
        print("input file name is missing, please pass filename as the first argument.")
    else:
        business_process_types: list[BusinessProcessType] = [
            BusinessProcessType.CHANGE_JOB,
            BusinessProcessType.PROPOSE_COMPENSATION,
            BusinessProcessType.CHANGE_ORGANIZATION,
            BusinessProcessType.ASSIGN_PAYGROUP,
            BusinessProcessType.CHANGE_PERSONAL_INFORMATION,
            BusinessProcessType.ASSIGN_ROLES,
        ]
        EibBuilder.build(
            LoadInputData.load_csv(sys.argv[1]),
            business_process_types=business_process_types,
        )


__init()
