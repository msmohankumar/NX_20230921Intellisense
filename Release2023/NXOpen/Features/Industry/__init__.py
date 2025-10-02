from ....NXOpen import *
from ...Features import *
from ..Industry import *

import typing
import enum

class ProjectStructureNode(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetChildNodes(self, childNodes: typing.List[Features.Industry.ProjectStructureNode]) -> None:
        ...
    Checked: bool
    CreateAsRootPart: bool
    SelectedSpecialization: str


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


