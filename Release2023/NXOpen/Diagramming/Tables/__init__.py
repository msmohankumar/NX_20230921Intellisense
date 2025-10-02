from ....NXOpen import *
from ...Diagramming import *
from ..Tables import *

import typing
import enum

class ZeroDisplay(enum.Enum):
    Zero = 0
    Dash = 1
    Empty = 2


class TextDirection(enum.Enum):
    Horizontal = 0
    VerticalRightReading = 1
    VerticalLeftReading = 2


class TableSettingsBuilder(Diagramming.BaseTaggedObjectBuilder):
    def __init__(self) -> None: ...
    AnchorLocation: Diagramming.Tables.AnchorLocation
    HeaderLocation: Diagramming.Tables.HeaderLocation
    HeaderOrientation: Diagramming.Tables.HeaderOrientation
    ProtectedFlag: bool


class TableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Diagramming.Tables.Table]:
        ...
    def __init__(self, owner: Diagramming.DiagrammingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTableBuilder(self, table: Diagramming.Tables.Table) -> Diagramming.Tables.TableBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Diagramming.Tables.Table:
        ...
    def Tag(self) -> Tag: ...



class TableBuilder(Diagramming.AnnotationBuilder):
    def __init__(self) -> None: ...
    def GetNumberOfColumns(self) -> int:
        ...
    def GetNumberOfHeaders(self) -> int:
        ...
    def GetNumberOfRows(self) -> int:
        ...
    def InsertHeaders(self, headerIndex: int, numHeaders: int) -> None:
        ...
    def InsertColumns(self, columnIndex: int, numColumns: int) -> None:
        ...
    def InsertRows(self, rowIndex: int, numRows: int) -> None:
        ...
    def RemoveHeaders(self, headerIndex: int, numHeaders: int) -> None:
        ...
    def RemoveColumns(self, columnIndex: int, numColumns: int) -> None:
        ...
    def RemoveRows(self, rowIndex: int, numRows: int) -> None:
        ...
    def GetHeaderCell(self, rowIndex: int, columnIndex: int) -> Diagramming.Tables.CellBuilder:
        ...
    def GetCell(self, rowIndex: int, columnIndex: int) -> Diagramming.Tables.CellBuilder:
        ...
    def GetHeader(self, headerIndex: int) -> Diagramming.Tables.CellRangeBuilder:
        ...
    def GetColumn(self, columnIndex: int) -> Diagramming.Tables.ColumnBuilder:
        ...
    def GetRow(self, rowIndex: int) -> Diagramming.Tables.RowBuilder:
        ...
    def GetFillColor(self, color: NXColor, opacity: float) -> None:
        ...
    def SetFillColor(self, color: NXColor, opacity: float) -> None:
        ...
    def MergeHeaderCells(self, topRow: int, leftColumn: int, bottomRow: int, rightColumn: int) -> None:
        ...
    def MergeCells(self, topRow: int, leftColumn: int, bottomRow: int, rightColumn: int) -> None:
        ...
    def UnMergeHeaderCell(self, rowIndex: int, columnIndex: int) -> None:
        ...
    def UnMergeCell(self, rowIndex: int, columnIndex: int) -> None:
        ...
    def Inherit(self, inheritOption: Diagramming.Tables.TableBuilder.InheritOption, annotation: Diagramming.Annotation) -> None:
        ...
    BottomBorder: Diagramming.RenderingPropertiesBuilder
    CellSettingsBuilder: Diagramming.Tables.CellSettingsBuilder
    ContinuationDataBuilder: Diagramming.Tables.ContinuationDataBuilder
    DefaultBottomBorder: Diagramming.RenderingPropertiesBuilder
    DefaultRightBorder: Diagramming.RenderingPropertiesBuilder
    InitialColumnWidth: float
    LeftBorder: Diagramming.RenderingPropertiesBuilder
    Locked: bool
    RightBorder: Diagramming.RenderingPropertiesBuilder
    TableSettingsBuilder: Diagramming.Tables.TableSettingsBuilder
    TopBorder: Diagramming.RenderingPropertiesBuilder


    class InheritOption(enum.Enum):
        Preferences = 0
        CustomerDefaults = 1
        Selection = 2
    

class Table(Diagramming.Annotation):
    def __init__(self) -> None: ...
    def GetTitleBlock(self) -> Diagramming.TitleBlock:
        ...
    def RemoveTitleBlock(self) -> None:
        ...


class SizingMethod(enum.Enum):
    Auto = 0
    Fixed = 1


class SizedSymbol():
    PaddingFromLastSymbol: float
    Symbol: TaggedObject
    Height: float
    Width: float
    def ToString(self) -> str:
        ...


class RowBuilder(Diagramming.Tables.CellRangeBuilder):
    def __init__(self) -> None: ...
    def SetHeight(self, size: float) -> None:
        ...


class OverflowBehavior(enum.Enum):
    Wrap = 0
    Truncate = 1
    OverflowBorder = 2
    ShrinkToFit = 3
    Suffix = 4


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class HeaderOrientation(enum.Enum):
    Vertical = 0
    Horizontal = 1


class HeaderLocation(enum.Enum):
    Start = 0
    End = 1


class ContinuationLocation(enum.Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3
    NextSheet = 4


class ContinuationDataBuilder(Diagramming.BaseTaggedObjectBuilder):
    def __init__(self) -> None: ...
    Location: Diagramming.Tables.ContinuationLocation
    MaximumSize: float
    Spacing: float


class ContentAlignment(enum.Enum):
    TopLeft = 0
    TopCenter = 1
    TopRight = 2
    MiddleLeft = 3
    MiddleCenter = 4
    MiddleRight = 5
    BottomLeft = 6
    BottomCenter = 7
    BottomRight = 8


class ColumnBuilder(Diagramming.Tables.CellRangeBuilder):
    def __init__(self) -> None: ...
    def SetWidth(self, size: float) -> None:
        ...


class CellSettingsBuilder(Diagramming.BaseTaggedObjectBuilder):
    def __init__(self) -> None: ...
    def GetContentTextStyle(self) -> Diagramming.TextStyleBuilder:
        ...
    ContentAlignment: Diagramming.Tables.ContentAlignment
    FillColor: NXColor
    FillOpacity: float
    OverflowBehavior: Diagramming.Tables.OverflowBehavior
    TextDirection: Diagramming.Tables.TextDirection
    ZeroDisplay: Diagramming.Tables.ZeroDisplay


class CellRangeBuilder(Diagramming.BaseTaggedObjectBuilder):
    def __init__(self) -> None: ...
    CanHide: bool
    Hidden: bool
    Size: float
    SizingMethod: Diagramming.Tables.SizingMethod


class CellBuilder(Diagramming.BaseTaggedObjectBuilder):
    def __init__(self) -> None: ...
    def GetCellSettings(self) -> Diagramming.Tables.CellSettingsBuilder:
        ...
    def SetImageFileLocation(self, fileName: str) -> None:
        ...
    def DeleteContent(self) -> None:
        ...
    def GetContent(self) -> typing.List[Diagramming.Tables.SizedSymbol]:
        ...
    def SetContent(self, symbols: typing.List[Diagramming.Tables.SizedSymbol]) -> None:
        ...
    def Inherit(self, inheritOption: Diagramming.Tables.CellBuilder.InheritOption, elementToInheritFrom: TaggedObject) -> None:
        ...
    BottomBorder: Diagramming.RenderingPropertiesBuilder
    FormattedStringBuilder: Diagramming.FormattedStringBuilder
    LeftBorder: Diagramming.RenderingPropertiesBuilder
    Locked: bool
    Padding: float
    RightBorder: Diagramming.RenderingPropertiesBuilder
    Text: str
    TopBorder: Diagramming.RenderingPropertiesBuilder


    class InheritOption(enum.Enum):
        Preferences = 0
        CustomerDefaults = 1
        Selection = 2
    

class AnchorLocation(enum.Enum):
    TopLeft = 0
    TopRight = 1
    BottomLeft = 2
    BottomRight = 3


class _SizedSymbol():
    paddingFromLastSymbol: float
    symbol: Tag
    height: float
    width: float


