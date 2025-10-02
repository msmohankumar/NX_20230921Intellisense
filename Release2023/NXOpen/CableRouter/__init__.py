from ...NXOpen import *
from ..CableRouter import *

import typing
import enum

class NetworkUtilizationSettingsBuilder(Builder):
    def __init__(self) -> None: ...
    DisplayStyle: CableRouter.NetworkUtilizationSettingsBuilder.DisplayMethod
    ExceedingFillColor: NXColor
    Range1Color: NXColor
    Range1Number: float
    Range2Color: NXColor
    Range2Number: float
    Range3Color: NXColor
    SelectedColorCount: CableRouter.NetworkUtilizationSettingsBuilder.AmountOfColors
    SpecifiedFillAmount: float
    SpecifiedFillColor: NXColor


    class DisplayMethod(enum.Enum):
        ExceedingRange = 0
        ExceedingDefinedRange = 1
        RangeAreas = 2
    

    class AmountOfColors(enum.Enum):
        Two = 0
        Three = 1
    

class CableSettingsBuilder(Builder):
    def __init__(self) -> None: ...
    AvailableColor: NXColor
    BasicDisplayProperties: LineColorFontWidthBuilder
    CableSelectionColor: NXColor
    EndDeviceColor: NXColor
    FitOnSelection: bool
    LabelFontSize: float
    LabelTextProperties: TextColorFontWidthBuilder
    LayerNumber: int
    ShowDeviceLabels: bool
    ShowDevices: bool
    ShowNodeLabels: bool
    ShowNodes: bool
    ShowSegmentLabels: bool
    ShowSegments: bool
    StartDeviceColor: NXColor
    VirtualDisplayProperties: LineColorFontWidthBuilder


class CableRouterManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetCableRouterManager(self, owner: Session) -> CableRouter.CableRouterManager:
        ...
    def Tag(self) -> Tag: ...

    CableRouterCollection: CableRouter.CableRouterCollection


class CableRouterCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: CableRouter.CableRouterManager) -> None: ...
    def CreateCableSettingsBuilder(self, part: Part) -> CableRouter.CableSettingsBuilder:
        ...
    def CreateNetworkUtilizationSettingsBuilder(self, part: Part) -> CableRouter.NetworkUtilizationSettingsBuilder:
        ...
    def Tag(self) -> Tag: ...



