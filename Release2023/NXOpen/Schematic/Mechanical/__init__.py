from ....NXOpen import *
from ...Schematic import *
from ..Mechanical import *

import typing
import enum

class RunCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Schematic.Mechanical.Run]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Schematic.Mechanical.Run:
        ...
    def CreateRunBuilder(self, run: Schematic.Mechanical.Run) -> Schematic.Mechanical.RunBuilder:
        ...
    def Tag(self) -> Tag: ...



class RunBuilder(Builder):
    def __init__(self) -> None: ...
    def SetPartOperationCreateBuilder(self, createBuilder: PDM.PartOperationCreateBuilder) -> None:
        ...
    Discipline: str
    DisplayName: str
    Identifier: str
    LineType: str
    ObjectApplication: str
    Specification: str
    Standalone: bool


class Run(Schematic.Model.BaseObject):
    def __init__(self) -> None: ...
    Discipline: str
    Specification: str


