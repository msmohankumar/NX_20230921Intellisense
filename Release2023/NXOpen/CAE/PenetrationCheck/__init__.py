from ....NXOpen import *
from ...CAE import *
from ..PenetrationCheck import *

import typing
import enum

class TranslateNodesBuilder(Builder):
    def __init__(self) -> None: ...
    Csys: CoordinateSystem
    DirectionVector: Direction
    Distance: Expression
    Method: CAE.PenetrationCheck.TranslateNodesBuilder.MethodOptions
    MoveAdjacentNodes: bool
    NumberOfLayers: Expression
    PAngle: Expression
    PointSource: Point
    PointTarget: Point
    SelectNodes: CAE.SelectFENodeList
    TAngle: Expression
    VectorSource: Direction
    VectorTarget: Direction
    XDistance: Expression
    XScaleFactor: float
    YDistance: Expression
    YScaleFactor: float
    ZDistance: Expression
    ZScaleFactor: float


    class MethodOptions(enum.Enum):
        AlongNodeNormals = 0
        OppositeofNodeNormals = 1
        AlongDirection = 2
        WithOrientation = 3
        PointToPoint = 4
        AlignVectors = 5
        ScaleModel = 6
    

class ResultObject(NXObject):
    def __init__(self) -> None: ...
    def FreezeComponent(self, compToFreeze: int) -> None:
        ...
    def DeleteResultObject(self) -> None:
        ...


class ResultList(NXObject):
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class Manager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaeSession) -> None: ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def ClearManager(self, num: int) -> None:
        ...
    def RefreshResults(self, pObjects: typing.List[CAE.PenetrationCheck.ResultObject]) -> None:
        ...
    def ResultObjectAutomaticResolve(self, pObjects: typing.List[CAE.PenetrationCheck.ResultObject]) -> None:
        ...
    def PlotContours(self, viewIndex: int, pObjects: typing.List[CAE.PenetrationCheck.ResultObject]) -> None:
        ...
    def Tag(self) -> Tag: ...

    ActiveSet: CAE.PenetrationCheck.AnalysisSet


class AutomaticResolveBuilder(Builder):
    def __init__(self) -> None: ...
    def ResolveButton(self) -> None:
        ...
    MaxInterference: Expression
    MeshesToFreeze: SelectNXObjectList
    MinInterference: Expression
    ResolveOptions: CAE.PenetrationCheck.AutomaticResolveBuilder.ResolveType


    class ResolveType(enum.Enum):
        All = 0
        WithinLimits = 1
    

class AutomaticResolve(DisplayableObject):
    def __init__(self) -> None: ...


class AnalysisSet(NXObject):
    def __init__(self) -> None: ...
    def DeleteSet(self) -> None:
        ...
    def ChangeActiveSet(self) -> None:
        ...
    def RunInterferenceCheck(self) -> None:
        ...
    def PlotContours(self, viewIndex: int) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...


class AddSetBuilder(Builder):
    def __init__(self) -> None: ...
    BoundaryType: CAE.PenetrationCheck.AddSetBuilder.ThicknessBoundaryType
    ElemThickness: Expression
    InterferenceBetween: CAE.PenetrationCheck.AddSetBuilder.InterferenceBetweenType
    InterferenceOption: CAE.PenetrationCheck.AddSetBuilder.InterferenceType
    PenetrationSetName: str
    Selection: SelectNXObjectList
    SelectionType: CAE.PenetrationCheck.AddSetBuilder.SelectionTypeOptions
    SelfInterferenceOption: bool
    ThicknessFactor: Expression
    ThicknessSource: CAE.PenetrationCheck.AddSetBuilder.ThicknessSourceType


    class ThicknessSourceType(enum.Enum):
        ElementAssociatedData = 0
        UserDefined = 1
    

    class ThicknessBoundaryType(enum.Enum):
        Sharp = 0
        Round = 1
    

    class SelectionTypeOptions(enum.Enum):
        MeshObjects = 0
        ContactDefinitions = 1
    

    class InterferenceType(enum.Enum):
        All = 0
        Intersections = 1
        Penetrations = 2
    

    class InterferenceBetweenType(enum.Enum):
        MeshCollectorContainers = 0
        Meshes = 1
        ComponentFEMs = 2
    

class AddSet(DisplayableObject):
    def __init__(self) -> None: ...


