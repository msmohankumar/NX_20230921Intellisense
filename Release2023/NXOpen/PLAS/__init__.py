from ...NXOpen import *
from ..PLAS import *

import typing
import enum

class RunBuilder(Builder):
    def __init__(self) -> None: ...
    def GetLogicalObject(self) -> PDM.LogicalObject:
        ...
    def AutoAssignAttributes(self, objects: typing.List[NXObject]) -> ErrorList:
        ...
    def AutoAssignAttributesWithNamingPattern(self, objects: typing.List[NXObject], properties: typing.List[NXObject]) -> ErrorList:
        ...
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: str, titlePatterns: str) -> NXObject:
        ...
    Discipline: str
    IsUnassigned: bool
    LineTypePathId: str
    ObjectApplication: str
    PipeSpecPathId: str


class Run(PDM.ElementGroup):
    def __init__(self) -> None: ...
    def ReparentBranch(self, destinationRun: PLAS.Run, oldbranch: PDM.OrderedElementGroup) -> PDM.OrderedElementGroup:
        ...
    def GetBranches(self, branches: typing.List[PDM.OrderedElementGroup]) -> None:
        ...


class PlasManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateRunBuilder(self, run: PLAS.Run) -> PLAS.RunBuilder:
        ...
    def CreateControlLoopBuilder(self, run: PLAS.Run) -> PLAS.ControlLoopBuilder:
        ...
    def Tag(self) -> Tag: ...

    ActiveControlLoop: PLAS.Run
    ActiveRun: PLAS.Run


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class ControlLoopBuilder(PLAS.RunBuilder):
    def __init__(self) -> None: ...
    ProcessVariable: str


class ControlLoop(PLAS.Run):
    def __init__(self) -> None: ...


