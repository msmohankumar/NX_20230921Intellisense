from ....NXOpen import *
from ...CAM import *
from ..FBM import *

import typing
import enum

class ThreadFeatureGeometry(CAM.FBM.FeatureGeometry):
    def __init__(self) -> None: ...
    def SetThreadDataSource(self, source: CAM.FBM.ThreadFeatureGeometry.ThreadDataSource) -> None:
        ...
    def GetThreadDataSource(self) -> CAM.FBM.ThreadFeatureGeometry.ThreadDataSource:
        ...
    def GetFormUserDefined(self) -> str:
        ...
    def SetFormUserDefined(self, userDefinedForm: str) -> None:
        ...
    def UpdateThreadParameters(self, tagFeature: CAM.FBM.Feature) -> None:
        ...
    FormStandard: CAM.FBM.ThreadFeatureGeometry.Form
    ThreadRotation: CAM.FBM.ThreadFeatureGeometry.Rotation


    class ThreadDataSource(enum.Enum):
        FromModel = 0
        FromTable = 1
    

    class Rotation(enum.Enum):
        RightHand = 0
        LeftHand = 1
    

    class Form(enum.Enum):
        Unified = 0
        Acme = 1
        StubAcme = 2
        Buttress = 4
        Metric = 5
        Trapezoidal = 8
        Lowernherz = 9
        SparkPlug = 10
        Npt = 11
        HoseCoupling = 12
        FireHose = 13
        Unj = 14
        Nps = 15
        Bsp = 16
        Bstp = 17
        Helicoil = 18
        Ns = 19
        UserDefined = 20
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MachiningFeatureGeometry(CAM.FBM.FeatureGeometry):
    def __init__(self) -> None: ...


class FeatureSet(CAM.GeometrySet):
    def __init__(self) -> None: ...
    def GetFeature(self) -> CAM.FBM.Feature:
        ...
    def CreateFeature(self, entities: typing.List[NXObject]) -> CAM.FBM.Feature:
        ...


class FeatureGeometry(CAM.Geometry):
    def __init__(self) -> None: ...
    def CreateFeatureSet(self) -> CAM.FBM.FeatureSet:
        ...
    def AddFeatureSet(self, tagMachiningFeature: CAM.CAMFeature, featureType: str) -> CAM.FBM.FeatureSet:
        ...
    def GetFeatureSet(self, nIndex: int) -> CAM.FBM.FeatureSet:
        ...
    def SetDefaultAttribute(self, attributeName: str, dValue: float) -> None:
        ...
    def SetDefaultAttribute(self, attributeName: str, strValue: str) -> None:
        ...
    def SetDefaultAttribute(self, attributeName: str, nValue: int) -> None:
        ...
    def SetDefaultAttribute(self, attributeName: str, bValue: bool) -> None:
        ...
    def ReorderFeatures(self, sortType: CAM.FBM.FeatureGeometry.SortOrder) -> None:
        ...
    def ReorderFeaturesByDirection(self, direction: CAM.FBM.FeatureGeometry.SequenceDirectionType, pattern: CAM.FBM.FeatureGeometry.SequencePatternType, vecValue: Vector3d) -> None:
        ...
    def ReorderFeaturesByDirection(self, direction: CAM.FBM.FeatureGeometry.SequenceDirectionType, pattern: CAM.FBM.FeatureGeometry.SequencePatternType, vecValue: Vector3d, bandWidth: float) -> None:
        ...
    def ReverseFeatures(self) -> None:
        ...
    def ReloadList(self) -> None:
        ...
    def SetMachiningArea(self, machiningArea: str) -> None:
        ...
    def GetMachiningArea(self) -> str:
        ...
    def CreateFeatures(self, objects: typing.List[NXObject], featureType: str) -> typing.List[CAM.FBM.Feature]:
        ...
    UseModelDepth: bool


    class SortOrder(enum.Enum):
        Closest = 0
        ShortestPath = 1
        PrimaryDirection = 2
    

    class SequencePatternType(enum.Enum):
        Zig = 0
        ZigZag = 1
    

    class SequenceDirectionType(enum.Enum):
        Xm = 0
        Ym = 1
        Zm = 2
        Vector = 3
    

class Feature(NXObject):
    def __init__(self) -> None: ...
    def GetAttribute(self, attributeName: str) -> CAM.CAMAttribute:
        ...
    def SetAttributeValue(self, attributeName: str, dValue: float) -> None:
        ...
    def SetAttributeValue(self, attributeName: str, strValue: str) -> None:
        ...
    def SetAttributeValue(self, attributeName: str, nValue: int) -> None:
        ...
    def SetAttributeValue(self, attributeName: str, bValue: bool) -> None:
        ...
    def SetAttribute(self, tagAttribute: CAM.CAMAttribute) -> None:
        ...
    def GetAttributeDoubleValue(self, attributeName: str) -> float:
        ...
    def OverrideAttributeValue(self, attributeName: str, dValue: float) -> None:
        ...
    def OverrideAttributeValue(self, attributeName: str, nValue: int) -> None:
        ...
    def OverrideAttributeValue(self, attributeName: str, bValue: bool) -> None:
        ...
    def OverrideAttributeValue(self, attributeName: str, strValue: str) -> None:
        ...
    def OverrideAttributeValue(self, attributeName: str, ptValue: Point3d) -> None:
        ...
    def OverrideAttributeValue(self, attributeName: str, vecValue: Vector3d) -> None:
        ...
    def IsAttributeOverridden(self, attributeName: str) -> bool:
        ...
    def ResetAttributeValue(self, attributeName: str) -> None:
        ...
    def ResetAttributes(self) -> None:
        ...
    def FlipDirection(self) -> None:
        ...
    def SetCoordinateSystem(self, ptValue: Point3d, xAxis: Vector3d, yAxis: Vector3d) -> None:
        ...
    def GetMachiningArea(self, tagEntit: DisplayableObject) -> str:
        ...
    def Unlock(self) -> None:
        ...


