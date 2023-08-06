from enum import Enum


class AddGranularAclsKind(str, Enum):
    SCRIPT = "script"
    GROUP = "group_"
    RESOURCE = "resource"
    SCHEDULE = "schedule"
    VARIABLE = "variable"
    FLOW = "flow"
    FOLDER = "folder"

    def __str__(self) -> str:
        return str(self.value)
