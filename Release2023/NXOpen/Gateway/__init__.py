from ...NXOpen import *
from ..Gateway import *

import typing
import enum

class PasteBuilder(Builder):
    def __init__(self) -> None: ...


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MassValueBuilder(Builder):
    def __init__(self) -> None: ...
    def GetMassValues(self) -> None:
        ...
    def UpdateMassValueSource(self, valueType: Gateway.MassValueBuilder.ValueSourceType) -> None:
        ...
    def UpdateDensityValueSource(self, valueType: Gateway.MassValueBuilder.ValueSourceType) -> None:
        ...
    def UpdateVolumeValueSource(self, valueType: Gateway.MassValueBuilder.ValueSourceType) -> None:
        ...
    Area: Gateway.MassValueBuilder.ValueSourceType
    AssignRolledUpAttribute: bool
    Density: Gateway.MassValueBuilder.ValueSourceType
    DeriveOption: int
    GravityCenterX: Gateway.MassValueBuilder.ValueSourceType
    GravityCenterY: Gateway.MassValueBuilder.ValueSourceType
    GravityCenterZ: Gateway.MassValueBuilder.ValueSourceType
    InertiaXX: Gateway.MassValueBuilder.ValueSourceType
    InertiaXY: Gateway.MassValueBuilder.ValueSourceType
    InertiaXZ: Gateway.MassValueBuilder.ValueSourceType
    InertiaYY: Gateway.MassValueBuilder.ValueSourceType
    InertiaYZ: Gateway.MassValueBuilder.ValueSourceType
    InertiaZZ: Gateway.MassValueBuilder.ValueSourceType
    Mass: Gateway.MassValueBuilder.ValueSourceType
    MassType: Gateway.MassValueBuilder.MassTypes
    Objects: SelectNXObjectList
    Volume: Gateway.MassValueBuilder.ValueSourceType


    class ValueSourceType(enum.Enum):
        Unset = 0
        Computed = 1
        Asserted = 2
        UserDefined1 = 3
        UserDefined2 = 4
        UserDefined3 = 5
        UserDefined4 = 6
        ComputedCoated = 7
    

    class MassTypes(enum.Enum):
        Unset = 0
        MassOnly = 1
        DensityOnly = 2
        VolumeOnly = 3
        DensityMass = 4
        DensityVolume = 5
        MassVolume = 6
        AssertAll = 7
    

class MassPropertyOptionsBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSourceHierarchy(self, variableSources: int) -> None:
        ...
    def SetSourceHierarchy(self, variableSources: int) -> None:
        ...
    AccuracyType: Gateway.MassPropertyOptionsBuilder.AccuracyTypes
    ComponentGroupName: str
    MarkerColorOfAllComponents: int
    MarkerColorOfDisplayedPart: int
    MarkerColorOfSelectedComponentSet: int
    MarkerColorOfSelectedComponents: int
    UseAllComponents: bool
    UseDisplayedPart: bool
    UseSelectedComponentSet: bool
    UseSelectedComponents: bool
    UseSourceHierarchy: bool


    class AccuracyTypes(enum.Enum):
        Value1 = 0
        Value2 = 1
        Value3 = 2
        Value4 = 3
        Value5 = 4
        Value6 = 5
    

class MassPartSpecificOptionsBuilder(Builder):
    def __init__(self) -> None: ...
    def RemovePartSpecificSetting(self) -> None:
        ...
    ReferenceSetName: str


class MassLimitationBuilder(Builder):
    def __init__(self) -> None: ...
    def GetLimitationValues(self) -> None:
        ...
    MaximumArea: Expression
    MaximumAreaStatus: bool
    MaximumDensity: Expression
    MaximumDensityStatus: bool
    MaximumGravityCenterStatusX: bool
    MaximumGravityCenterStatusY: bool
    MaximumGravityCenterStatusZ: bool
    MaximumGravityCenterX: Expression
    MaximumGravityCenterY: Expression
    MaximumGravityCenterZ: Expression
    MaximumMass: Expression
    MaximumMassStatus: bool
    MaximumMomentsInertiaStatusXX: bool
    MaximumMomentsInertiaStatusYY: bool
    MaximumMomentsInertiaStatusZZ: bool
    MaximumMomentsInertiaXX: Expression
    MaximumMomentsInertiaYY: Expression
    MaximumMomentsInertiaZZ: Expression
    MaximumProductsInertiaStatusXY: bool
    MaximumProductsInertiaStatusXZ: bool
    MaximumProductsInertiaStatusYZ: bool
    MaximumProductsInertiaXY: Expression
    MaximumProductsInertiaXZ: Expression
    MaximumProductsInertiaYZ: Expression
    MaximumVolume: Expression
    MaximumVolumeStatus: bool
    MinimumArea: Expression
    MinimumAreaStatus: bool
    MinimumDensity: Expression
    MinimumDensityStatus: bool
    MinimumGravityCenterStatusX: bool
    MinimumGravityCenterStatusY: bool
    MinimumGravityCenterStatusZ: bool
    MinimumGravityCenterX: Expression
    MinimumGravityCenterY: Expression
    MinimumGravityCenterZ: Expression
    MinimumMass: Expression
    MinimumMassStatus: bool
    MinimumMomentsInertiaStatusXX: bool
    MinimumMomentsInertiaStatusYY: bool
    MinimumMomentsInertiaStatusZZ: bool
    MinimumMomentsInertiaXX: Expression
    MinimumMomentsInertiaYY: Expression
    MinimumMomentsInertiaZZ: Expression
    MinimumProductsInertiaStatusXY: bool
    MinimumProductsInertiaStatusXZ: bool
    MinimumProductsInertiaStatusYZ: bool
    MinimumProductsInertiaXY: Expression
    MinimumProductsInertiaXZ: Expression
    MinimumProductsInertiaYZ: Expression
    MinimumVolume: Expression
    MinimumVolumeStatus: bool
    Objects: SelectNXObjectList


class MassExportBuilder(Builder):
    def __init__(self) -> None: ...
    def LoadSystemDefault(self) -> None:
        ...
    def SaveAsDefault(self) -> None:
        ...
    def RestoreDefault(self) -> None:
        ...
    def SaveToFile(self, fileName: str) -> None:
        ...
    def OpenFromFile(self, fileName: str) -> None:
        ...
    def SetToggleState(self, nodeType: Gateway.MassExportBuilder.NodeType, nodeId: int, state: bool) -> None:
        ...
    def MoveUp(self, nodeType: Gateway.MassExportBuilder.NodeType, nodeId: int) -> None:
        ...
    def MoveDown(self, nodeType: Gateway.MassExportBuilder.NodeType, nodeId: int) -> None:
        ...
    DataMode: Gateway.MassExportBuilder.DataModes
    FileName: str
    Objects: SelectNXObjectList
    Output: Gateway.MassExportBuilder.OutputTypes
    TemplateFileName: str
    UseLegacyLayoutForXLSX: bool


    class PerComponentResult(enum.Enum):
        ComponentName = 0
        ObjectDisplayName = 1
        ItemID = 2
        ItemName = 3
        ItemRevision = 4
        FileName = 5
        DescriptivePartName = 6
        ParentName = 7
        Count = 8
    

    class PerBodyResult(enum.Enum):
        BodyName = 0
        Count = 1
    

    class OverallResult(enum.Enum):
        Density = 0
        DensitySource = 1
        Area = 2
        AreaSource = 3
        Volume = 4
        VolumeSource = 5
        Mass = 6
        MassSource = 7
        Weight = 8
        WeightSource = 9
        CenterOfMassWCS = 10
        CenterOfMassAbsolute = 11
        CenterOfMassSource = 12
        FirstMomentsWCS = 13
        MomentsOfInertiaWCS = 14
        MomentsOfInertiaCentroidal = 15
        MomentsOfInertiaCentroidalSource = 16
        MomentsOfInertiaSpherical = 17
        ProductsOfInertiaWCS = 18
        ProductsOfInertiaCentroidal = 19
        ProductsOfInertiaCentroidalSource = 20
        PrincipalMomentsOfInertia = 21
        RadiiOfGyrationWCS = 22
        RadiiOfGyrationCentroidal = 23
        RadiiOfGyrationSpherical = 24
        PrincipalAxisWCS = 25
        EstimatedErrorRanges = 26
        Warnings = 27
        Count = 28
    

    class OutputTypes(enum.Enum):
        Information = 0
        Xlsx = 1
        Csv = 2
        Xml = 3
        Json = 4
    

    class NodeType(enum.Enum):
        ComponentHeader = 2
        BodyHeader = 3
        PerComponentResult = 4
        PerBodyResult = 5
        OverallResult = 6
    

    class DataModes(enum.Enum):
        AssemblyOnly = 0
        IncludeChildren = 1
        Solid = 2
    

    class ComponentHeader(enum.Enum):
        SourcePrecedence = 0
        ReferenceSetPrecedence = 1
        ReferenceSetUsed = 2
        ComponentGroup = 3
        Arrangement = 4
        Accuracy = 5
        Coating = 6
        Count = 7
    

    class BodyHeader(enum.Enum):
        SourcePrecedence = 0
        ReferenceSetUsed = 1
        Accuracy = 2
        Count = 3
    

class MassCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: PropertiesManager) -> None: ...
    def CreateCalculationBuilder(self, componentTags: typing.List[NXObject]) -> Gateway.MassCalculationBuilder:
        ...
    def CreateAssignmentBuilder(self, componentTag: NXObject) -> Gateway.MassAssignmentBuilder:
        ...
    def CreateLimitationBuilder(self, componentTag: NXObject) -> Gateway.MassLimitationBuilder:
        ...
    def CreateValueBuilder(self, componentTag: NXObject) -> Gateway.MassValueBuilder:
        ...
    def CreatePropertyOptionsBuilder(self) -> Gateway.MassPropertyOptionsBuilder:
        ...
    def CreatePartSpecificOptionsBuilder(self) -> Gateway.MassPartSpecificOptionsBuilder:
        ...
    def CreateExportBuilder(self, componentTags: typing.List[NXObject]) -> Gateway.MassExportBuilder:
        ...
    def Tag(self) -> Tag: ...



class MassCalculationBuilder(Builder):
    def __init__(self) -> None: ...
    ComponentGroupName: str
    IncludeChildren: bool
    Objects: SelectNXObjectList


class MassAssignmentBuilder(Builder):
    def __init__(self) -> None: ...
    def GetAssignmentValues(self) -> None:
        ...
    Area: Expression
    AreaStatus: bool
    AssignmentStatus: bool
    Density: Expression
    DensityStatus: bool
    DeriveOption: int
    GravityCenterStatus: bool
    GravityCenterX: Expression
    GravityCenterY: Expression
    GravityCenterZ: Expression
    InertiaStatus: bool
    Mass: Expression
    MassStatus: bool
    MassType: Gateway.MassAssignmentBuilder.MassTypes
    MomentsInertiaXX: Expression
    MomentsInertiaYY: Expression
    MomentsInertiaZZ: Expression
    Objects: SelectNXObjectList
    ProductsInertiaXY: Expression
    ProductsInertiaXZ: Expression
    ProductsInertiaYZ: Expression
    ValueType: Gateway.MassAssignmentBuilder.ValueTypes
    Volume: Expression
    VolumeStatus: bool


    class ValueTypes(enum.Enum):
        Asserted = 0
        UserDefined1 = 1
        UserDefined2 = 2
        UserDefined3 = 3
        UserDefined4 = 4
    

    class MassTypes(enum.Enum):
        MassOnly = 0
        DensityMass = 1
        DensityVolume = 2
        MassVolume = 3
    

class ImageExportBuilder(Builder):
    def __init__(self) -> None: ...
    def GetRegionTopLeftPoint(self) -> int:
        ...
    def SetRegionTopLeftPoint(self, regionTopLeftPoint: int) -> None:
        ...
    def GetCustomBackgroundColor(self) -> float:
        ...
    def SetCustomBackgroundColor(self, customBackgroundColor: float) -> None:
        ...
    BackgroundOption: Gateway.ImageExportBuilder.BackgroundOptions
    EnhanceEdges: bool
    FileFormat: Gateway.ImageExportBuilder.FileFormats
    FileName: str
    RegionHeight: int
    RegionMode: bool
    RegionWidth: int


    class FileFormats(enum.Enum):
        Png = 0
        Jpg = 1
        Gif = 2
        Tiff = 3
        Bmp = 4
        Xwd = 5
    

    class BackgroundOptions(enum.Enum):
        Original = 0
        CustomColor = 1
        Transparent = 2
    

class ImageCaptureManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def CreateImageCaptureBuilder(self) -> Gateway.ImageCaptureBuilder:
        ...
    def Tag(self) -> Tag: ...



class ImageCaptureBuilder(Builder):
    def __init__(self) -> None: ...
    def GetRegion(self, topLeftCorner: int, bottomRightCorner: int) -> None:
        ...
    def SetRegion(self, topLeftCorner: int, bottomRightCorner: int) -> None:
        ...
    CaptureMethod: Gateway.ImageCaptureBuilder.CaptureMethodType
    File: str
    Format: Gateway.ImageCaptureBuilder.ImageFormat
    ImageFile: str
    Size: Gateway.ImageCaptureBuilder.ImageSize


    class ImageSize(enum.Enum):
        Pixels16 = 0
        Pixels24 = 1
        Pixels32 = 2
        Pixels48 = 3
        Pixels64 = 4
        Pixels96 = 5
        Pixels128 = 6
    

    class ImageFormat(enum.Enum):
        Bmp = 0
        Jpg = 1
        Gif = 2
        Png = 3
        Tiff = 4
    

    class CaptureMethodType(enum.Enum):
        GraphicsArea = 0
        Region = 1
        File = 2
        Automatic = 3
    

class IGenericFileNewApplicationBuilder(Builder):
    def __init__(self) -> None: ...
    def AutoAssignAttributes(self, objects: typing.List[NXObject]) -> ErrorList:
        ...
    def AutoAssignAttributesWithNamingPattern(self, objects: typing.List[NXObject], properties: typing.List[NXObject]) -> ErrorList:
        ...
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: str, titlePatterns: str) -> NXObject:
        ...


class GenericFileNewBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def SetApplicationBuilder(self, applicationBuilder: Gateway.IGenericFileNewApplicationBuilder) -> None:
        ...


class CopyCutBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCopyCutStatus(self) -> Gateway.CopyCutBuilder.Status:
        ...
    def GetNonExportableObjects(self) -> typing.List[NXObject]:
        ...
    def GetObjects(self) -> typing.List[NXObject]:
        ...
    def SetObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    def ResetInitialCopyLocation(self) -> None:
        ...
    CanCopyAsSketch: bool
    DestinationFilename: str
    InitialCopyLocation: Point3d
    IsCut: bool
    ToClipboard: bool


    class Status(enum.Enum):
        NoObjectsCopied = 0
        NonExportableObjects = 1
        PartExportFailed = 2
        ErrorDuringCut = 3
        AllObjectsCopied = 4
    

class BookmarkFile(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def SaveWithDescription(self, pathName: str, bookmarkOption: BasePart.BookmarkOption, description: str) -> None:
        ...
    def Rename(self, oldPathName: str, newFileName: str, okToOverwriteExistingFile: bool) -> str:
        ...
    def SetDescription(self, pathName: str, description: str) -> None:
        ...
    def Delete(self, pathName: str) -> None:
        ...
    def Tag(self) -> Tag: ...



class BaseExplicitOrderBuilder(Builder):
    def __init__(self) -> None: ...
    def Save(self, orderList: str, saveName: str) -> None:
        ...
    def Paste(self, pastePoint: int, selectedEntries: str, currentOrder: str) -> str:
        ...
    def Delete(self, selectedEntries: str, currentOrder: str, numOfRemainingEntries: int) -> str:
        ...
    def Clear(self) -> None:
        ...
    def DownArrow(self, selectedEntries: str, currentOrder: str) -> str:
        ...
    def UpArrow(self, selectedEntries: str, currentOrder: str) -> str:
        ...
    def SaveAsTextFile(self, savedOrderName: str, saveFileName: str, overwriteFile: bool) -> None:
        ...
    SaveName: str


