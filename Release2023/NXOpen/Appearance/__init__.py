from ...NXOpen import *
from ..Appearance import *

import typing
import enum

class VisualMaterialUsage(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...


class Scheme(NXObject):
    def __init__(self) -> None: ...
    def GetSchemeName(self) -> str:
        ...
    def GetSchemeDescription(self) -> str:
        ...
    def GetAppearanceDesignators(self, designators: typing.List[Appearance.Designator]) -> None:
        ...
    def GetVisualMaterialForDesignator(self, designator: Appearance.Designator) -> Appearance.VisualMaterialUsage:
        ...


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class Designator(NXObject):
    def __init__(self) -> None: ...
    def ClearGeometricEntites(self) -> None:
        ...


class DataManager(NXObject):
    def __init__(self) -> None: ...
    def GetProductAssembly(self) -> str:
        ...
    def GetLoadedAssembly(self) -> str:
        ...
    def GetCurrentWorkAppearanceArea(self) -> Appearance.Area:
        ...
    def SetCurrentWorkAppearanceArea(self, appearanceArea: Appearance.Area) -> None:
        ...
    def GetAllLoadedAppearanceAreas(self, appearanceAreas: typing.List[Appearance.Area]) -> None:
        ...
    def UnloadAppearanceData(self, part: Part) -> ErrorList:
        ...
    def SaveAppearanceScheme(self) -> PDM.OperationErrors:
        ...
    def GetAppearanceArea(self, appearanceAreaName: str) -> Appearance.Area:
        ...


class Area(NXObject):
    def __init__(self) -> None: ...
    def GetAllAppearanceDesignators(self, designators: typing.List[Appearance.Designator]) -> None:
        ...
    def GetActiveAppearanceScheme(self) -> Appearance.Scheme:
        ...
    def GetDesignator(self, designatorName: str) -> Appearance.Designator:
        ...
    def GetScheme(self, schemeName: str) -> Appearance.Scheme:
        ...


class AppearanceUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetAppearanceManager(self) -> Appearance.DataManager:
        ...
    def GetVisualMaterialUsage(self) -> Appearance.VisualMaterialUsage:
        ...
    def GetParentAppearanceArea(self, designator: Appearance.Designator) -> Appearance.Area:
        ...
    def SetDesignatorName(self, parentAppAreaName: str, currentDesignatorName: str, newDesignatorName: str) -> None:
        ...
    def SetDesignatorDescription(self, parentAppAreaName: str, designatorName: str, newDesignatorDescription: str) -> None:
        ...
    def ApplyAppearanceScheme(self, areaName: str, schemeName: str) -> ErrorList:
        ...
    def SetVisualMaterialForDesignator(self, parentAppAreaName: str, designatorName: str, visualMaterialName: str, materialSource: int) -> ErrorList:
        ...
    def RemoveAppearanceDesignator(self, parentAppAreaName: str, designatorName: str) -> ErrorList:
        ...
    def RemoveVisualMaterialOnDesignator(self, parentAppAreaName: str, designatorName: str) -> ErrorList:
        ...
    def DeleteAppearanceScheme(self, parentAppAreaName: str, schemeName: str) -> ErrorList:
        ...
    def RemoveGeometricEntities(self, parentAppAreaName: str, designatorName: str, geometricEntities: typing.List[TaggedObject]) -> ErrorList:
        ...
    def Tag(self) -> Tag: ...



class AppearanceSchemeBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSchemeName(self, schemeName: str) -> None:
        ...
    def SetSchemeActionType(self, actionType: Appearance.AppearanceSchemeBuilder.Action) -> None:
        ...
    def SetAppearanceArea(self, appearanceArea: Appearance.Area) -> None:
        ...
    def SetCurrentAppearanceScheme(self, appearanceScheme: Appearance.Scheme) -> None:
        ...
    def GetNewAppearanceScheme(self) -> Appearance.Scheme:
        ...
    def GetErrorWarningList(self) -> ErrorList:
        ...


    class Action(enum.Enum):
        New = 0
        Copy = 1
        Rename = 2
    

class AppearanceManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateAppearanceDesignatorBuilder(self, schemeName: str) -> Appearance.AppearanceDesignatorBuilder:
        ...
    def CreateAppearanceEditTextureBuilder(self, designatorName: str, schemeName: str) -> Appearance.AppearanceEditTexture:
        ...
    def CreateAppearanceSchemeBuilder(self) -> Appearance.AppearanceSchemeBuilder:
        ...
    def SetProductAssembly(self, productAssembly: str) -> ErrorList:
        ...
    def UnloadAllAppearanceData(self) -> ErrorList:
        ...
    def Tag(self) -> Tag: ...



class AppearanceEditTexture(Builder):
    def __init__(self) -> None: ...
    AnchorType: Appearance.AppearanceEditTexture.AnchorTypes
    AspectRatio: float
    MappingProjection: int
    Scale: float
    StudioMaterialName: str
    TextureNormalVector: Direction
    TextureOrigin: Point
    TextureUpVector: Direction


    class Scaling(enum.Enum):
        ToFace = 0
        ToImageSize = 1
        ToUniformScale = 2
        ToNonUniformScale = 3
    

    class MaterialProjectionsType(enum.Enum):
        Uv = 0
        Planar = 1
        Box = 2
        Spherical = 3
        Cylindrical = 4
    

    class DecalProjectionsType(enum.Enum):
        Planar = 0
        Cylindrical = 1
        Spherical = 2
        Uv = 3
    

    class AnchorTypes(enum.Enum):
        TopLeft = 0
        Center = 1
        BottomLeft = 2
        TopMiddle = 3
        TopRight = 4
        LeftMiddle = 5
        RightMiddle = 6
        BottomMiddle = 7
        BottomRight = 8
    

class AppearanceDesignatorBuilder(Builder):
    def __init__(self) -> None: ...
    def RemoveConflictedFaceMaterial(self, conflictDesignatorTag: typing.List[TaggedObject], conflictAppMat: typing.List[TaggedObject], conflictEntities: typing.List[TaggedObject]) -> None:
        ...
    DesignatorDescription: str
    DesignatorName: str
    ParentAppearanceArea: str
    SelectionList: SelectNXObjectList


