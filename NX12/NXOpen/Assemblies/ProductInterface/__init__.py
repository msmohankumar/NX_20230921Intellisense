from ....NXOpen import *
from ...Assemblies import *
from ..ProductInterface import *

import typing
import enum

class PropertyBuilder(Builder):
    def __init__(self) -> None: ...
    Description: str
    InterfaceUsageType: int
    Name: str


class ObjectBuilder(Builder):
    def __init__(self) -> None: ...
    def AddProductInterfaceObject1(self, nxObject: NXObject, name: str, description: str, reverseDirection: bool) -> Assemblies.ProductInterface.InterfaceObject:
        ...
    def AddProductInterfaceObject2(self, nxObject: NXObject, name: str, description: str, reverseDirection: bool, interfaceUsageType: Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType) -> Assemblies.ProductInterface.InterfaceObject:
        ...
    def EditProductInterfaceObject(self, productInterface: Assemblies.ProductInterface.InterfaceObject, nxObject: NXObject, name: str, description: str, reverseDirection: bool) -> None:
        ...
    def EditProductInterfaceObject1(self, productInterface: Assemblies.ProductInterface.InterfaceObject, nxObject: NXObject, name: str, description: str, reverseDirection: bool, interfaceUsageType: Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType) -> None:
        ...
    def GetBuilderVersion(self) -> Assemblies.ProductInterface.ObjectBuilder.BuilderVersion:
        ...
    def SetBuilderVersion(self, version: Assemblies.ProductInterface.ObjectBuilder.BuilderVersion) -> None:
        ...
    def AddProductInterfaceObject(self, nxItem: NXObject) -> Assemblies.ProductInterface.InterfaceObject:
        ...
    def AddProductInterface(self, nxItem: NXObject, alreadyExisted: bool) -> Assemblies.ProductInterface.InterfaceObject:
        ...
    def RemoveProductInterfaceObject(self, prodIntItem: Assemblies.ProductInterface.InterfaceObject) -> None:
        ...
    def QueryProductInterfaceObjects(self, part: NXObject) -> typing.List[Assemblies.ProductInterface.InterfaceObject]:
        ...
    def SetUserComments(self, prodIntItem: Assemblies.ProductInterface.InterfaceObject, userComments: str) -> None:
        ...
    def UpdateAttributesFromPart(self, part: NXObject) -> None:
        ...
    MateSetting: Assemblies.ProductInterface.ObjectBuilder.Mate
    PartGeometryCopy: Features.PartGeometryCopyBuilder
    WaveSetting: Assemblies.ProductInterface.ObjectBuilder.Wave


    class Wave(enum.Enum):
        NoCheck = 0
        Warn = 1
        Prevent = 2
    

    class Mate(enum.Enum):
        NoCheck = 0
        Warn = 1
        Prevent = 2
    

    class BuilderVersion(enum.Enum):
        Original = 0
        One = 1
        Two = 2
        Three = 3
    

class InterfaceObject(NXObject):
    def __init__(self) -> None: ...
    def GetProductInterfaceObjectType(self) -> str:
        ...
    def GetProductInterfaceDefiningEntity(self) -> NXObject:
        ...
    def GetProductInterfaceObjectStatus(self) -> str:
        ...
    def SetUserComments(self, userComments: str) -> None:
        ...
    def GetUserComments(self) -> str:
        ...
    def RemoveProductInterfaceObject(self) -> None:
        ...
    def RenameProductInterfaceObject(self, name: str) -> None:
        ...
    def CheckProductInterfaceObject(self) -> Assemblies.ProductInterface.InterfaceObject.InvalidState:
        ...
    def FixInvalidProductInterfaceObject(self) -> bool:
        ...
    def InsertRelatedExpressions(self, relatedExps: typing.List[NXObject]) -> None:
        ...
    def RemoveRelatedExpression(self, relatedExp: NXObject) -> None:
        ...
    def RemoveAllRelatedExpressions(self) -> int:
        ...
    def GetRelatedExpressions(self) -> typing.List[NXObject]:
        ...
    def GetInterfaceUsageType(self) -> Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType:
        ...
    def SetInterfaceUsageType(self, usageType: Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType) -> None:
        ...
    def BreakPIReferencingLinks(self, usageType: Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType) -> None:
        ...


    class InvalidState(enum.Enum):
        Valid = 0
        Sleeping = 1
        IncorrectOrphan = 2
        SelfReferenced = 3
    

    class InterfaceUsageType(enum.Enum):
        Unknown = 0
        Output = 1
        Input = 2
        KeyPerformanceInterface = 3
    

class Collection(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateObjectBuilder(self) -> Assemblies.ProductInterface.ObjectBuilder:
        """[Obsolete("Deprecated in NX11.0.1.  Please use NXOpen.Assemblies.ProductInterface.Collection.CreateObjectBuilderWithVersion instead.")"""
        ...
    def CreateObjectBuilderWithVersion(self, version: int) -> Assemblies.ProductInterface.ObjectBuilder:
        ...
    def CreatePropertyBuilder(self) -> Assemblies.ProductInterface.PropertyBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> NXObject:
        ...
    def GetProductInterfaces(self) -> typing.List[Assemblies.ProductInterface.InterfaceObject]:
        ...
    def Tag(self) -> Tag: ...



