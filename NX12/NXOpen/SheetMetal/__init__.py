from ...NXOpen import *
from ..SheetMetal import *

import typing
import enum

class FlatPatternSettings(TaggedObject):
    def __init__(self) -> None: ...
    def GetFlatPatternObjectTypeDisplay(self, objectType: SheetMetal.FlatPatternSettings.FlatPatternObjectType) -> SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay:
        ...
    def SetFlatPatternObjectTypeDisplay(self, objectType: SheetMetal.FlatPatternSettings.FlatPatternObjectType, displayData: SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay) -> None:
        ...
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay:
        ...
    def SetFlatPatternCalloutTypeDisplay(self, calloutType: str, displayData: SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay) -> None:
        ...
    def GetFlatPatternAllObjectTypeDisplay(self, displayData: typing.List[SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay]) -> None:
        ...
    def GetFlatPatternAllCalloutTypeDisplay(self, displayData: typing.List[SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay]) -> None:
        ...


    class FlatPatternSettingsFlatPatternObjectTypeDisplay():
        Type: SheetMetal.FlatPatternSettings.FlatPatternObjectType
        IsEnabled: int
        Color: NXColor
        Font: ViewDependentDisplayManager.Font
        Width: ViewDependentDisplayManager.Width
        def ToString(self) -> str:
            ...
    

    class FlatPatternObjectType(enum.Enum):
        BendCenterLine = 0
        BendUpCenterLine = 1
        BendDownCenterLine = 2
        BendTangentLine = 3
        OuterMoldLine = 4
        InnerMoldLine = 5
        ExteriorCurves = 6
        InteriorCurves = 7
        InteriorCutoutCurves = 8
        InteriorFeatureCurves = 9
        LighteningHoleCenter = 10
        JoggleLine = 11
        AddedTopGeometry = 12
        AddedBottomGeometry = 13
        ToolMarker = 14
    

    class FlatPatternSettingsFlatPatternCalloutTypeDisplay():
        Type: str
        IsEnabled: int
        Name: str
        def ToString(self) -> str:
            ...
        def __init__(self, Type: str, IsEnabled: int, Name: str) -> None: ...
    

