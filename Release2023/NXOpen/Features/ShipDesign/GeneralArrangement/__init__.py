from .....NXOpen import *
from ....Features import *
from ...ShipDesign import *
from ..GeneralArrangement import *

import typing
import enum

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class FaceCharacteristicsBuilder(Builder):
    def __init__(self) -> None: ...
    CharacteristicColor: NXColor
    CharacteristicValue: int
    SelectFace: ScCollector


class EvacuationPlanBuilder(Builder):
    def __init__(self) -> None: ...
    def ClearExpressionsData(self) -> None:
        ...
    def AddExpressionData(self, strTitle: str, strFormular: str) -> None:
        ...
    Angle: Expression
    Color: int
    HorizontalFlip: bool
    Origin: Annotations.OriginBuilder
    Pattern: int
    Scale: Expression
    Style: Annotations.StyleBuilder
    VerticalFlip: bool


class DrawingViewItemBuilder(Features.ShipDesign.GeneralArrangement.DrawingItemBuilder):
    def __init__(self) -> None: ...
    HorizontalFrameBarPosition: Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.FrameBarPositionType
    ShowFireAndSafetyPlanSymbol: bool
    ShowHorizontalFrameBar: bool
    ShowOpeningFillingLine: bool
    ShowOverallDimension: bool
    ShowPMILabel: bool
    ShowVerticalFrameBar: bool
    VerticalFrameBarPosition: Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.FrameBarPositionType


    class FrameBarPositionType(enum.Enum):
        ViewTop = 0
        ViewCenterY = 1
        ViewBottom = 2
        ViewLeft = 3
        ViewCenterX = 4
        ViewRight = 5
    

class DrawingTableItemBuilder(Features.ShipDesign.GeneralArrangement.DrawingItemBuilder):
    def __init__(self) -> None: ...


class DrawingItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.GeneralArrangement.DrawingItemBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.GeneralArrangement.DrawingItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.GeneralArrangement.DrawingItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.GeneralArrangement.DrawingItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.GeneralArrangement.DrawingItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.GeneralArrangement.DrawingItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.GeneralArrangement.DrawingItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.GeneralArrangement.DrawingItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.GeneralArrangement.DrawingItemBuilder, object2: Features.ShipDesign.GeneralArrangement.DrawingItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.GeneralArrangement.DrawingItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DrawingItemBuilder(Builder):
    def __init__(self) -> None: ...
    CreateItem: bool


class DrawingAutomationBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateDrawingViewItemBuilder(self) -> Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder:
        ...
    def CreateDrawingTableItemBuilder(self) -> Features.ShipDesign.GeneralArrangement.DrawingTableItemBuilder:
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    ViewList: Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList
    ViewType: str


