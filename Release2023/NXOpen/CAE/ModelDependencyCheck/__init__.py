from ....NXOpen import *
from ...CAE import *
from ..ModelDependencyCheck import *

import typing
import enum

class Result(NXObject):
    def __init__(self) -> None: ...
    def GetConflictingNodes(self) -> typing.List[CAE.FENode]:
        ...
    def GetConflictingDofs(self) -> int:
        ...
    FirstElement: CAE.FEElement
    FirstMesh: CAE.Mesh
    Id: str
    SecondElement: CAE.FEElement
    SecondMesh: CAE.Mesh


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class Manager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaeSession) -> None: ...
    def PerformCheck(self) -> None:
        ...
    def AutoResolveAllResults(self) -> None:
        ...
    def AutoResolveSubsetResults(self, resultsToResolve: typing.List[CAE.ModelDependencyCheck.Result]) -> None:
        ...
    def ExportResults(self, resultsFile: str) -> None:
        ...
    def GetResults(self) -> typing.List[CAE.ModelDependencyCheck.Result]:
        ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Tag(self) -> Tag: ...



