from ...NXOpen import *
from ..Gateway import *

import typing
import enum

class PasteBuilder(Builder):
    def __init__(self) -> None: ...


class ImageExportBuilder(System.Object):
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


