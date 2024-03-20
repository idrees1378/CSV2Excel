from __future__ import annotations

from enum import Enum

from src.mappings.maps import (
    AssignPayGroupMap,
    AssignRolesMap,
    ChangeJobMap,
    ChangeOrganizationMap,
    ChangePersonalInformationMap,
    ProposeCompensationMap,
)


class BusinessProcessType(Enum):
    CHANGE_JOB = 1
    PROPOSE_COMPENSATION = 2
    CHANGE_ORGANIZATION = 3
    ASSIGN_PAYGROUP = 4
    CHANGE_PERSONAL_INFORMATION = 5
    ASSIGN_ROLES = 6

BusinessProcessTypeToName={
    BusinessProcessType.CHANGE_JOB: "Change Job",
    BusinessProcessType.PROPOSE_COMPENSATION: "Propose Compensation",
    BusinessProcessType.CHANGE_ORGANIZATION: "Change Organization",
    BusinessProcessType.ASSIGN_PAYGROUP: "Assign Pay Group",
    BusinessProcessType.CHANGE_PERSONAL_INFORMATION: "Change Personal Information",
    BusinessProcessType.ASSIGN_ROLES: "Assign Roles"
}

BusinessProcessTypeToMappping={
    BusinessProcessType.CHANGE_JOB: ChangeJobMap,
    BusinessProcessType.PROPOSE_COMPENSATION: ProposeCompensationMap,
    BusinessProcessType.CHANGE_ORGANIZATION: ChangeOrganizationMap,
    BusinessProcessType.ASSIGN_PAYGROUP: AssignPayGroupMap,
    BusinessProcessType.CHANGE_PERSONAL_INFORMATION: ChangePersonalInformationMap,
    BusinessProcessType.ASSIGN_ROLES: AssignRolesMap
}

BusinessProcessTypeToProcessInstruction={
    BusinessProcessType.CHANGE_JOB: {"row": 7,  "value": "Automatic Processing"},
    BusinessProcessType.PROPOSE_COMPENSATION: {"row": 8,  "value": "Automatic Processing"},
    BusinessProcessType.CHANGE_ORGANIZATION: {"row": 11,  "value": "Automatic Processing"},
    BusinessProcessType.ASSIGN_PAYGROUP: {"row": 12,  "value": "Automatic Processing"},
    BusinessProcessType.CHANGE_PERSONAL_INFORMATION: {"row": 14,  "value": "Automatic Processing"},
    BusinessProcessType.ASSIGN_ROLES: {"row": 17,  "value": "Automatic Processing"}

}
