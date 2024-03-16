
from enum import Enum
from pathlib import Path

from openpyxl import load_workbook

from src.eib_builder_logger import EibBuilderLogger
from src.mappings.mapper import Map


class BusinessProcessType(Enum):
    JOB_CHANGE = 1
    COMPENSATION = 2
    CHANGE_ORG = 3
    ASSIGN_PAYGROUP = 4
    CHANGE_PERSONAL_INFO = 5
    ASSIGN_ROLES = 6


logger = EibBuilderLogger()


class EibBuilder:
    def __init__(self):
        pass



    @classmethod
    def build(
        cls,
        data_records: list[Map],
        output_file_name: str = "change_job_eib",
        populate_data: list[BusinessProcessType] = [BusinessProcessType.JOB_CHANGE],
    ) -> None:
        """
        loads given csv file into object by calling __load_csv().
        """
        try:
            if not data_records:
                return
            build_eib = EibBuilder()
            workbook = load_workbook(
                filename="./templates/template_change_job_v42.1.xlsx"
            )
            if BusinessProcessType.JOB_CHANGE in populate_data:
                build_eib.set_change_job_data(workbook, data_records)
            if BusinessProcessType.COMPENSATION in populate_data:
                build_eib.set_compensation_data(workbook, data_records)
            if BusinessProcessType.CHANGE_ORG in populate_data:
                build_eib.set_change_org_data(workbook, data_records)
            if BusinessProcessType.ASSIGN_PAYGROUP in populate_data:
                build_eib.set_assign_paygroup_data(workbook, data_records)
            if BusinessProcessType.CHANGE_PERSONAL_INFO in populate_data:
                build_eib.set_change_personal_info_data(workbook, data_records)
            if BusinessProcessType.ASSIGN_ROLES in populate_data:
                build_eib.set_assign_roles_data(workbook, data_records)

            workbook.save(build_eib.__xlsx_fname(output_file_name))

            logger.log_messages(["Successfully created xlsx"])

        except Exception as error:
            print(error.args)

    def set_compensation_data(self, workbook, records: list):
        print("not implemented yet - set_compensation_data")

    def set_change_org_data(self, workbook, records: list):
        print("not implemented yet - set_change_org_data")

    def set_assign_paygroup_data(self, workbook, records: list):
        print("not implemented yet - set_assign_paygroup_data")

    def set_change_personal_info_data(self, workbook, records: list):
        print("not implemented yet - set_change_personal_info_data")

    def set_assign_roles_data(self, workbook, records: list):
        print("not implemented yet - set_assign_roles_data")

    def set_change_job_data(self, workbook, records: list):
        worksheet_change_job = workbook["Change Job"]
        header = worksheet_change_job[5]
        data_row = 6  # data cell starts on the 6th row after header finishes off in Chane_job_sample.xlsx

        for record in records:
            for header_cell in header:
                value = record.wdmap.get(header_cell.value, None)

                if value is None:
                    continue

                worksheet_change_job.cell(
                    row=data_row, column=header_cell.column
                ).value = value
            data_row += 1
        # set business process parameter for change job
        worksheet_overview = workbook["Overview"]
        worksheet_overview.cell(row=7, column=3).value = "Automatic Processing"

    def __xlsx_fname(self, ref_fname: str):
        fname = Path(ref_fname).stem
        return Path(fname + "-output").with_suffix(".xlsx")
