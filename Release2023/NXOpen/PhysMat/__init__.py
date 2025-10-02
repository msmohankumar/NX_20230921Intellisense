from ...NXOpen import *
from ..PhysMat import *

import typing
import enum

class PhysicalMaterialListBuilder(Builder):
    def __init__(self) -> None: ...


class PhysicalMaterialLibMgrBuilder(Builder):
    def __init__(self) -> None: ...


class PhysicalMaterialAssignBuilder(Builder):
    def __init__(self) -> None: ...


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class DynaFieldAttributes(NXObject):
    def __init__(self) -> None: ...
    def GetApplication(self) -> Fields.IApplication:
        ...
    def DeleteApplicationData(self) -> None:
        ...
    def CopyToField(self, field: Fields.Field) -> None:
        ...
    DataTypeAttribute: PhysMat.DynaFieldAttributes.DataType
    LoadCurveUsageAttribute: PhysMat.DynaFieldAttributes.LoadCurveUsage
    NumDiscretizationPointsAttribute: int


    class LoadCurveUsage(enum.Enum):
        NormalAnalysisPhase = 0
        DynamicRelaxationPhase = 1
        BothPhases = 2
    

    class DataType(enum.Enum):
        ChemicalShrinkage = -100
        FabricStress = -2
        General = 0
        GeneralXY = 1
        GeneralRS = 6
    

class DynaFieldApplication(Fields.IApplication):
    def __init__(self) -> None: ...
    def CreateAttributes(self, loadCurveUsage: PhysMat.DynaFieldAttributes.LoadCurveUsage, dataType: PhysMat.DynaFieldAttributes.DataType, numDiscPts: int) -> PhysMat.DynaFieldAttributes:
        ...


