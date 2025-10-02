from ....NXOpen import *
from ...Features import *
from ..AECDesign import *

import typing
import enum

class ProjectSetupBuilder(Builder):
    def __init__(self) -> None: ...
    def AddSharedParts(self, parts: typing.List[Part]) -> None:
        ...
    def GetRootNode(self) -> Features.Industry.ProjectStructureNode:
        ...
    IsNewStructure: bool
    IsSaveAsSharePart: bool
    ProjectName: str


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


