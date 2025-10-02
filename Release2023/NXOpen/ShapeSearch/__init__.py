from ...NXOpen import *
from ..ShapeSearch import *

import typing
import enum

class ShapeSearchBuilder(Builder):
    def __init__(self) -> None: ...
    def GetInputAttributesName(self) -> str:
        ...
    def SetInputAttributesName(self, inputAttributesName: str) -> None:
        ...
    def GetInputAttributesFilter(self) -> str:
        ...
    def SetInputAttributesFilter(self, inputAttributesFilter: str) -> None:
        ...
    def ExecuteSearch(self, isNew: bool, searchName: str, nTotalResults: int, errorMessage: str) -> None:
        ...
    def GetResults(self, searchName: str, startResultId: int, endResultId: int) -> None:
        ...
    def OpenResultPart(self, openPartType: ShapeSearch.ShapeSearchBuilder.OpenPartType, searchName: str, resultId: int) -> None:
        ...
    CustomShapeSizeLowerLimit: int
    CustomShapeSizeUpperLimit: int
    InputBody: SelectNXObjectList
    InputPart: str
    ReferenceSetName: str
    SearchShapeSimilarity: ShapeSearch.ShapeSearchBuilder.ShapeSimilarity
    SearchShapeSize: ShapeSearch.ShapeSearchBuilder.ShapeSize
    SearchType: ShapeSearch.ShapeSearchBuilder.SearchByType
    UseCustomShapeSize: bool


    class ShapeSize(enum.Enum):
        P90P110 = 0
        P80P120 = 1
        P70P130 = 2
        P50P200 = 3
        P25P400 = 4
    

    class ShapeSimilarity(enum.Enum):
        Gradient1 = 0
        Gradient2 = 1
        Gradient3 = 2
        Gradient4 = 3
        Gradient5 = 4
        Gradient6 = 5
        Gradient7 = 6
        Gradient8 = 7
        Gradient9 = 8
        Gradient10 = 9
    

    class SearchByType(enum.Enum):
        Attribute = 0
        Body = 1
        Part = 2
    

    class OpenPartType(enum.Enum):
        NotSetDisplayPart = 0
        SetDisplayPartOnlyWhenOpen = 1
        AlwaysSetDisplayPart = 2
    

class SearchManager(Utilities.NXRemotableObject):
    def __init__(self, owner: PartCollection) -> None: ...
    def CreateShapeSearchBuilder(self, part: Part) -> ShapeSearch.ShapeSearchBuilder:
        ...
    def Tag(self) -> Tag: ...



class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


