from . import Tables
from . import Geometry
from ...NXOpen import *
from ..Diagramming import *

import typing
import enum

class ZoneOrigin(enum.Enum):
    BottomRight = 0
    TopLeft = 1
    TopRight = 2
    BottomLeft = 3


class ViewOperations(Utilities.NXRemotableObject):
    def __init__(self, owner: Diagramming.SheetManager) -> None: ...
    def Fit(self, sheet: Diagramming.Sheet) -> None:
        ...
    def FitToElements(self, sheet: Diagramming.Sheet, elements: typing.List[Diagramming.SheetElement]) -> None:
        ...
    def SetViewport(self, sheet: Diagramming.Sheet, x: float, y: float, width: float, height: float) -> None:
        ...
    def Scale(self, sheet: Diagramming.Sheet, scale: float) -> None:
        ...
    def Tag(self) -> Tag: ...



class VerticalCenteringMarkType(enum.Enum):
    None = 0
    BottomArrow = 1
    TopArrow = 2
    BottomandTopArrow = 3
    BottomandTopLine = 4


class TrimmingMarkStyleType(enum.Enum):
    Triangle = 0
    Corner = 1


class TitleBlockCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Diagramming.TitleBlock]:
        ...
    def __init__(self, owner: Diagramming.DiagrammingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDefineTitleBlockBuilder(self, titleBlock: Diagramming.TitleBlock) -> Diagramming.DefineTitleBlockBuilder:
        ...
    def CreatePopulateTitleBlockBuilder(self, titleBlocks: typing.List[Diagramming.TitleBlock]) -> Diagramming.PopulateTitleBlockBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Diagramming.TitleBlock:
        ...
    def Tag(self) -> Tag: ...



class TitleBlockCellBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Diagramming.TitleBlockCellBuilder]) -> None:
        ...
    def Append(self, object: Diagramming.TitleBlockCellBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Diagramming.TitleBlockCellBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Diagramming.TitleBlockCellBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Diagramming.TitleBlockCellBuilder) -> None:
        ...
    def Erase(self, obj: Diagramming.TitleBlockCellBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Diagramming.TitleBlockCellBuilder]:
        ...
    def SetContents(self, objects: typing.List[Diagramming.TitleBlockCellBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Diagramming.TitleBlockCellBuilder, object2: Diagramming.TitleBlockCellBuilder) -> None:
        ...
    def Insert(self, location: int, object: Diagramming.TitleBlockCellBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class TitleBlockCellBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Label: str
    Lock: bool
    Value: str


class TitleBlock(NXObject):
    def __init__(self) -> None: ...


class TextStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    TextAlignment: Diagramming.TextStyleBuilder.TextAlignmentType
    TextAllowWrapping: bool
    TextAutoFit: Diagramming.TextStyleBuilder.TextAutoFitType
    TextColorFontWidth: TextColorFontWidthBuilder
    TextHeight: float
    TextOverlined: bool
    TextUnderlined: bool
    TruncationMode: Diagramming.TextStyleBuilder.TruncationModes


    class TruncationModes(enum.Enum):
        None = 0
        Trim = 1
        Suffix = 2
    

    class TextAutoFitType(enum.Enum):
        None = 0
        ResizeOutline = 1
        ShrinkText = 2
    

    class TextAlignmentType(enum.Enum):
        Left = 0
        Center = 1
        Right = 2
    

class SmartDiagrammingManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateReferenceGeometryBuilder(self, referenceGeometry: Diagramming.ReferenceGeometry) -> Diagramming.ReferenceGeometryBuilder:
        ...
    def Tag(self) -> Tag: ...



class SheetZoneSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ContinueZoneIndexingAcrossSheets: bool
    CornerZoneModification: float
    CreateZoneLabels: bool
    CreateZoneMarkings: bool
    CreateZones: bool
    HorizontalSize: float
    LabelColor: int
    LabelFont: int
    LabelHeight: float
    LabelItalicized: bool
    LabelWidth: int
    LabelsToSkip: str
    MarkingHeight: float
    MarkingLineColorWidth: LineColorFontWidthBuilder
    Origin: Diagramming.ZoneOrigin
    VerticalSize: float


class SheetTemplateBuilder(Builder):
    def __init__(self) -> None: ...
    Sheet: Diagramming.SheetBuilder
    SheetSize: Diagramming.SheetSizeBuilder


class SheetSizeBuilder(Builder):
    def __init__(self) -> None: ...


class SheetMarginSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BottomTrimmedMargin: float
    BottomUntrimmedMargin: float
    CreateUntrimmedMargins: bool
    LeftTrimmedMargin: float
    LeftUntrimmedMargin: float
    MarginLineColorFontWidth: LineColorFontWidthBuilder
    RightTrimmedMargin: float
    RightUntrimmedMargin: float
    TopTrimmedMargin: float
    TopUntrimmedMargin: float


class SheetManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def OpenSheet(self, sheet: Diagramming.Sheet) -> None:
        ...
    def Tag(self) -> Tag: ...

    ViewOperations: Diagramming.ViewOperations
    ActiveSheet: Diagramming.Sheet


class SheetElementBuilder(Diagramming.BaseObjectBuilder):
    def __init__(self) -> None: ...
    def GetMinNodeSize(self, sizeValues: float) -> None:
        ...
    def SetMinNodeSize(self, sizeValues: float) -> None:
        ...
    def GetAllowedTransformations(self, isAllowedTranslation: bool, isAllowedRotation: bool, isAllowedScale: bool, isAllowedShear: bool) -> None:
        ...
    def SetOwningSheet(self, owningSheet: Diagramming.Sheet) -> None:
        ...
    Height: float
    HeightPolicy: Diagramming.DiagrammingSizingpolicy
    Internal: bool
    Label: Diagramming.Annotation
    LabelName: str
    Location: Diagramming.LocationBuilder
    LocationStyle: Diagramming.DiagrammingLocationstyle
    MirrorX: bool
    MirrorY: bool
    Owner: Diagramming.SheetElement
    OwningSheet: Diagramming.Sheet
    ResizeOption: Diagramming.SheetElementBuilder.ResizeOptionType
    Rotation: float
    SourceElement: Diagramming.SheetElement
    UpToDate: bool
    Visible: bool
    Width: float
    WidthPolicy: Diagramming.DiagrammingSizingpolicy
    X: float
    Y: float
    ZDepth: int


    class ResizeOptionType(enum.Enum):
        AnyDirection = 0
        OnAnchor = 1
        SameRatio = 2
        SameRationOnCorner = 3
        SameRatioOnEdge = 4
    

class SheetElement(Diagramming.BaseObject):
    def __init__(self) -> None: ...


class SheetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Diagramming.Sheet]:
        ...
    def __init__(self, owner: Diagramming.DiagrammingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSheetBuilder(self, sheet: Diagramming.Sheet) -> Diagramming.SheetBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Diagramming.Sheet:
        ...
    def Tag(self) -> Tag: ...



class SheetBuilder(Diagramming.BaseObjectBuilder):
    def __init__(self) -> None: ...
    def GetFeatures(self) -> typing.List[Diagramming.SheetElement]:
        ...
    def GetSheetElements(self) -> typing.List[Diagramming.SheetElement]:
        ...
    def GetSize(self, height: float, width: float) -> None:
        ...
    def SetSize(self, height: float, width: float) -> None:
        ...
    AllowJumpers: bool
    Description: str
    JumperType: Diagramming.DiagrammingJumpertype
    Opacity: float
    PaxFileName: str
    PresentationName: str
    ToolTip: str
    Units: Unit
    UpdatePAXFile: bool


class SheetBorderSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ArrowAngle: float
    ArrowDirection: Diagramming.ArrowDirectionType
    ArrowHeadTail: float
    ArrowLength: float
    ArrowStyle: Diagramming.ArrowStyleType
    BorderLineWidth: float
    CenteringMarkLength: float
    CenteringMarksColorWidth: LineColorFontWidthBuilder
    CenteringMarksExtension: float
    CenteringMarksHorizontal: Diagramming.HorizontalCenteringMarkType
    CenteringMarksVertical: Diagramming.VerticalCenteringMarkType
    CreateBorders: bool
    CreateTrimmingMarks: bool
    DisplaySheetSizeInBorder: bool
    DistanceFromInnerBorder: float
    InnerLineCFW: LineColorFontWidthBuilder
    Method: Diagramming.Method
    OuterLineCFW: LineColorFontWidthBuilder
    TrimmingMarkColor: NXColor
    TrimmingMarkLength: float
    TrimmingMarkStyle: Diagramming.TrimmingMarkStyleType
    TrimmingMarkWidth: float


class SheetBordersAndZonesCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Diagramming.SheetBordersAndZones]:
        ...
    def __init__(self, owner: Diagramming.DiagrammingManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Diagramming.SheetBordersAndZones:
        ...
    def CreateSheetBordersAndZonesBuilder(self, bordersAndZones: Diagramming.SheetBordersAndZones) -> Diagramming.SheetBordersAndZonesBuilder:
        ...
    def Tag(self) -> Tag: ...



    class ZoneOrigin(enum.Enum):
        BottomRight = 0
        TopLeft = 1
        TopRight = 2
        BottomLeft = 3
    

    class ZoneMethod(enum.Enum):
        None = 0
        Standard = 1
        Custom = 2
    

class SheetBordersAndZonesBuilder(Builder):
    def __init__(self) -> None: ...
    def SetOwningSheet(self, owningSheet: Diagramming.Sheet) -> None:
        ...
    BottomMargin: float
    CenteringMarkExtension: float
    CreateBorders: bool
    CreateTrimmingMarks: bool
    CreateZoneLabels: bool
    CreateZoneMarking: bool
    HorizontalCenteringMark: Diagramming.SheetBordersAndZonesBuilder.HorizontalCenteringMarkType
    HorizontalSize: float
    LabelFont: int
    LabelHeight: float
    LeftMargin: float
    MarkingHeight: float
    Method: Diagramming.SheetBordersAndZonesBuilder.ZoneMethod
    Origin: Diagramming.SheetBordersAndZonesBuilder.ZoneOrigin
    RightMargin: float
    SheetBorderSettings: Diagramming.SheetBorderSettingsBuilder
    SheetMarginSettings: Diagramming.SheetMarginSettingsBuilder
    SheetZoneSettings: Diagramming.SheetZoneSettingsBuilder
    TopMargin: float
    TrimmingMarkLength: float
    TrimmingMarkThickness: float
    VerticalCenteringMark: Diagramming.SheetBordersAndZonesBuilder.VerticalCenteringMarkType
    VerticalSize: float
    Width: float


    class VerticalCenteringMarkType(enum.Enum):
        None = 0
        BottomArrow = 1
        TopArrow = 2
        BottomandTopArrow = 3
        BottomandTopLine = 4
    

    class TrimmingMarkStyleType(enum.Enum):
        Triangle = 0
        Corner = 1
    

    class HorizontalCenteringMarkType(enum.Enum):
        None = 0
        LeftArrow = 1
        RightArrow = 2
        LeftandRightArrow = 3
        LeftandRightLine = 4
    

    class ArrowStyleType(enum.Enum):
        Filled = 0
        Closed = 1
        ClosedSolid = 2
        Open = 3
    

    class ArrowDirectionType(enum.Enum):
        OutofSheet = 0
        IntoSheet = 1
    

class SheetBordersAndZones(NXObject):
    def __init__(self) -> None: ...


class Sheet(Diagramming.BaseObject):
    def __init__(self) -> None: ...
    def LogGroupToDelete(self, group: Diagramming.Group) -> None:
        ...


class ShapeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Diagramming.Shape]:
        ...
    def __init__(self, owner: Diagramming.DiagrammingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateShapeBuilder(self, shape: Diagramming.Shape) -> Diagramming.ShapeBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Diagramming.Shape:
        ...
    def Tag(self) -> Tag: ...



class ShapeBuilder(Diagramming.SheetElementBuilder):
    def __init__(self) -> None: ...


class Shape(Diagramming.ConnectableElement):
    def __init__(self) -> None: ...


class RenderingPropertiesBuilder(Diagramming.BaseSubObjectBuilder):
    def __init__(self) -> None: ...
    FillColor: NXColor
    FillOpacity: float
    LineFont: DisplayableObject.ObjectFont
    LineWidth: DisplayableObject.ObjectWidth
    StrokeColor: NXColor
    StrokeOpacity: float


class ReferenceGeometryBuilder(Diagramming.AnnotationBuilder):
    def __init__(self) -> None: ...
    def GetColor(self) -> float:
        ...
    def SetColor(self, color: float) -> None:
        ...
    def RefreshFromView(self, refresh: bool) -> None:
        ...
    def GetExternalFileReferenceAdapter(self, referenceObjectId: int) -> ExternalFileReferenceAdapter:
        ...
    def SetExternalFileReferenceAdapter(self, referenceObjectId: int, adapter: ExternalFileReferenceAdapter) -> None:
        ...
    def GetExternalFileDefinitionKey(self, adapter: ExternalFileReferenceAdapter) -> str:
        ...
    def EstablishReference(self, referenceObjectId: int, referenceType: ExternalFileReferenceAdapter.Type, externalFileSpec: str) -> ExternalFileReferenceAdapter:
        ...
    DisplayBorder: bool
    Scale: float
    Transparency: int
    View: str


class ReferenceGeometry(Diagramming.Annotation):
    def __init__(self) -> None: ...


class PortCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Diagramming.Port]:
        ...
    def __init__(self, owner: Diagramming.DiagrammingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePortBuilder(self, port: Diagramming.Port) -> Diagramming.PortBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Diagramming.Port:
        ...
    def Tag(self) -> Tag: ...



class PortBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Diagramming.PortBuilder]) -> None:
        ...
    def Append(self, object: Diagramming.PortBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Diagramming.PortBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Diagramming.PortBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Diagramming.PortBuilder) -> None:
        ...
    def Erase(self, obj: Diagramming.PortBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Diagramming.PortBuilder]:
        ...
    def SetContents(self, objects: typing.List[Diagramming.PortBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Diagramming.PortBuilder, object2: Diagramming.PortBuilder) -> None:
        ...
    def Insert(self, location: int, object: Diagramming.PortBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PortBuilder(Diagramming.SheetElementBuilder):
    def __init__(self) -> None: ...
    def GetAllowedParentSides(self, isAllowedLeftSide: bool, isAllowedRightSide: bool, isAllowedUpSide: bool, isAllowedDownSide: bool) -> None:
        ...
    def CanAnotherConnectionBeAdded(self) -> bool:
        ...
    def IsNumberOfConnectionInfinite(self) -> bool:
        ...
    def GetOwningConnectableElement(self) -> Diagramming.ConnectableElement:
        ...
    def GetConnections(self) -> typing.List[Diagramming.Connection]:
        ...
    Direction: Diagramming.Direction
    NumberAllowedConnections: int
    Pinned: bool
    Proxy: Diagramming.Port


class Port(Diagramming.SheetElement):
    def __init__(self) -> None: ...
    Label: Diagramming.Annotation


class PopulateTitleBlockBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCellValueForLabel(self, label: str) -> str:
        ...
    def SetCellValueForLabel(self, label: str, value: str) -> None:
        ...
    def GetCell(self, table: Diagramming.Tables.Table, rowIndex: int, columnIndex: int) -> Diagramming.TitleBlockCellBuilder:
        ...


class NodeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Diagramming.Node]:
        ...
    def __init__(self, owner: Diagramming.DiagrammingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateNodeBuilder(self, node: Diagramming.Node) -> Diagramming.NodeBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Diagramming.Node:
        ...
    def Tag(self) -> Tag: ...



class NodeBuilder(Diagramming.ConnectableElementBuilder):
    def __init__(self) -> None: ...
    def AddGroupMember(self, member: Diagramming.SheetElement) -> None:
        ...
    def RemoveGroupMember(self, member: Diagramming.SheetElement) -> None:
        ...
    def RemoveAllGroupMembers(self) -> None:
        ...
    Expanded: bool
    Fullfillment: bool
    GroupingAllowed: bool
    OffsheetReference: Diagramming.Node


class Node(Diagramming.ConnectableElement):
    def __init__(self) -> None: ...
    def GetPorts(self, ports: typing.List[Diagramming.Port]) -> None:
        ...
    Label: Diagramming.Annotation


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class Method(enum.Enum):
    None = 0
    Standard = 1
    Custom = 2


class LocationBuilder(Diagramming.BaseSubObjectBuilder):
    def __init__(self) -> None: ...
    def SetValueX(self, inputPercent: float, inputValue: float) -> None:
        ...
    def SetValueY(self, inputPercent: float, inputValue: float) -> None:
        ...
    EvaluatedValueX: float
    EvaluatedValueY: float
    InputPercentX: float
    InputPercentY: float
    InputValueX: float
    InputValueY: float
    Reference: Diagramming.SheetElement
    UpToDate: bool


class LeaderLineCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Diagramming.LeaderLine]:
        ...
    def __init__(self, owner: Diagramming.DiagrammingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLeaderLineBuilder(self, leaderLine: Diagramming.LeaderLine) -> Diagramming.LeaderLineBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Diagramming.LeaderLine:
        ...
    def Tag(self) -> Tag: ...



class LeaderLineBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Diagramming.LeaderLineBuilder]) -> None:
        ...
    def Append(self, object: Diagramming.LeaderLineBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Diagramming.LeaderLineBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Diagramming.LeaderLineBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Diagramming.LeaderLineBuilder) -> None:
        ...
    def Erase(self, obj: Diagramming.LeaderLineBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Diagramming.LeaderLineBuilder]:
        ...
    def SetContents(self, objects: typing.List[Diagramming.LeaderLineBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Diagramming.LeaderLineBuilder, object2: Diagramming.LeaderLineBuilder) -> None:
        ...
    def Insert(self, location: int, object: Diagramming.LeaderLineBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class LeaderLineBuilder(Diagramming.SheetElementBuilder):
    def __init__(self) -> None: ...
    def GetBendPoints(self, points: typing.List[Point2d]) -> None:
        ...
    def SetBendPoints(self, points: typing.List[Point2d]) -> None:
        ...
    def SetTerminator(self, terminator: Diagramming.SheetElement, segmentId: int, percentX: float, inputX: float, percentY: float, inputY: float) -> None:
        ...
    def GetTerminator(self, terminator: Diagramming.SheetElement, segmentId: int, percentX: float, inputX: float, percentY: float, inputY: float) -> None:
        ...
    ArrowType: Diagramming.DiagrammingArrowtype
    StubLength: float
    StubSides: Diagramming.DiagrammingStubsides
    VerticalAlignment: Diagramming.LeaderLineBuilder.VerticalAlignmentOption


    class VerticalAlignmentOption(enum.Enum):
        Top = 0
        Middle = 1
        Bottom = 2
    

class LeaderLine(Diagramming.Connection):
    def __init__(self) -> None: ...


class HorizontalCenteringMarkType(enum.Enum):
    None = 0
    LeftArrow = 1
    RightArrow = 2
    LeftandRightArrow = 3
    LeftandRightLine = 4


class GroupCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Diagramming.Group]:
        ...
    def __init__(self, owner: Diagramming.DiagrammingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateGroupBuilder(self, group: Diagramming.Group) -> Diagramming.GroupBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Diagramming.Group:
        ...
    def Tag(self) -> Tag: ...



class GroupBuilder(Diagramming.SheetElementBuilder):
    def __init__(self) -> None: ...
    def GetMember(self, memberSid: str) -> Diagramming.SheetElement:
        ...
    def GetMembers(self) -> typing.List[Diagramming.SheetElement]:
        ...
    def AddMember(self, sheetElement: Diagramming.SheetElement) -> None:
        ...
    def RemoveMember(self, member: Diagramming.SheetElement) -> None:
        ...
    def RemoveAllMembers(self) -> None:
        ...


class Group(Diagramming.SheetElement):
    def __init__(self) -> None: ...


class FormattedStringBuilder(Diagramming.BaseSubObjectBuilder):
    def __init__(self) -> None: ...
    def SetFormatValue(self, objTags: typing.List[NXObject], attrTitles: str, format: str) -> None:
        ...
    def SetFormatValue(self, objTags: typing.List[NXObject], parentTags: typing.List[NXObject], attrTitles: str, format: str) -> None:
        ...
    def AppendFormat(self, objTags: typing.List[NXObject], attrTitles: str, appendFormat: str) -> None:
        ...
    def ClearFormat(self) -> None:
        ...
    def GetReferencedAttributes(self, objTags: typing.List[NXObject]) -> str:
        ...
    Format: str
    String: str


class FontEnum(enum.Enum):
    Blockfont = 0


class Direction(enum.Enum):
    In = 1
    Out = 2
    Both = 3


class DiagrammingStubsides(enum.Enum):
    Auto = 0
    Left = 1
    Right = 2


class DiagrammingSizingpolicy(enum.Enum):
    Length = 0
    Auto = 1
    Percent = 2
    Inherit = 4


class DiagrammingRepeatstartposition(enum.Enum):
    Center = 0
    Start = 1
    End = 2


class DiagrammingManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateBulkEditBuilder(self) -> Diagramming.BulkEditBuilder:
        ...
    def CreateCannedAnnotationBuilder(self, annotation: Diagramming.Annotation) -> Diagramming.CannedAnnotationBuilder:
        ...
    def OpenSheet(self, sheet: Diagramming.Sheet) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Moved to SheetManager")"""
        ...
    def CreateSheetSizeBuilder(self, sheet: Diagramming.Sheet) -> Diagramming.SheetSizeBuilder:
        ...
    def CreateSheetTemplateBuilder(self, sheet: Diagramming.Sheet) -> Diagramming.SheetTemplateBuilder:
        ...
    def Tag(self) -> Tag: ...

    Nodes: Diagramming.NodeCollection
    Sheets: Diagramming.SheetCollection
    Connections: Diagramming.ConnectionCollection
    Groups: Diagramming.GroupCollection
    Shapes: Diagramming.ShapeCollection
    Ports: Diagramming.PortCollection
    Annotations: Diagramming.AnnotationCollection
    LeaderLines: Diagramming.LeaderLineCollection
    SheetBordersAndZones: Diagramming.SheetBordersAndZonesCollection
    Tables: Diagramming.Tables.TableCollection
    TitleBlocks: Diagramming.TitleBlockCollection
    Lines: Diagramming.Geometry.LineCollection
    Points: Diagramming.Geometry.PointCollection
    Rectangles: Diagramming.Geometry.RectangleCollection
    Arcs: Diagramming.Geometry.ArcCollection
    ActiveSheet: Diagramming.Sheet


class DiagrammingLocationstyle(enum.Enum):
    Absolute = 0
    Relative = 1


class DiagrammingJumpertype(enum.Enum):
    U = 1
    Break = 2


class DiagrammingJumperprioritytype(enum.Enum):
    Horizontal = 0
    Vertical = 1


class DiagrammingGeometrypointmarker(enum.Enum):
    Cross = 0
    Circle = 1


class DiagrammingFlowdirectionarrowstyle(enum.Enum):
    BottomFilledArrow = 0
    BottomOpenArrow = 1
    ClosedArrow = 2
    ClosedDoubleArrow = 3
    ClosedDoubleSolidArrow = 4
    ClosedSolidArrow = 5
    FilledArrow = 6
    FilledDoubleArrow = 7
    OpenArrow = 8
    OpenDoubleArrow = 9
    TopFilledArrow = 10
    TopOpenArrow = 11


class DiagrammingConnectionlabelverticaloffsetposition(enum.Enum):
    Left = 0
    Right = 1


class DiagrammingConnectionlabelposition(enum.Enum):
    Start = 1
    End = 2
    Center = 4
    Spaced = 8


class DiagrammingConnectionlabelhorizontaloffsetposition(enum.Enum):
    Above = 0
    Below = 1


class DiagrammingArrowtype(enum.Enum):
    None = 0
    Open = 1
    Filled = 2
    ClosedSolid = 3


class DiagrammingAnnotationboundarytype(enum.Enum):
    None = 0
    Circle = 1
    Ellipse = 2
    Rectangle = 3
    RoundedRectangle = 4


class DiagrammingAlignment(enum.Enum):
    Left = 0
    Center = 1
    Right = 2
    Justify = 3


class DefineTitleBlockBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTables(self, tables: typing.List[Diagramming.Tables.Table]) -> None:
        ...
    def SetTables(self, tables: typing.List[Diagramming.Tables.Table]) -> None:
        ...
    def GetCell(self, table: Diagramming.Tables.Table, rowIndex: int, columnIndex: int) -> Diagramming.TitleBlockCellBuilder:
        ...
    Cells: Diagramming.TitleBlockCellBuilderList


class ConnectionLocationBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Diagramming.ConnectionLocationBuilder]) -> None:
        ...
    def Append(self, object: Diagramming.ConnectionLocationBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Diagramming.ConnectionLocationBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Diagramming.ConnectionLocationBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Diagramming.ConnectionLocationBuilder) -> None:
        ...
    def Erase(self, obj: Diagramming.ConnectionLocationBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Diagramming.ConnectionLocationBuilder]:
        ...
    def SetContents(self, objects: typing.List[Diagramming.ConnectionLocationBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Diagramming.ConnectionLocationBuilder, object2: Diagramming.ConnectionLocationBuilder) -> None:
        ...
    def Insert(self, location: int, object: Diagramming.ConnectionLocationBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ConnectionLocationBuilder(Diagramming.LocationBuilder):
    def __init__(self) -> None: ...
    SegmentIdentifier: int


class ConnectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Diagramming.Connection]:
        ...
    def __init__(self, owner: Diagramming.DiagrammingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateConnectionBuilder(self, connection: Diagramming.Connection) -> Diagramming.ConnectionBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Diagramming.Connection:
        ...
    def Tag(self) -> Tag: ...



class ConnectionBuilder(Diagramming.SheetElementBuilder):
    def __init__(self) -> None: ...
    def GetBendPoints(self, points: typing.List[Point2d]) -> None:
        ...
    def SetBendPoints(self, points: typing.List[Point2d]) -> None:
        ...
    Discipline: str
    End: Diagramming.Port
    EndLocation: Diagramming.LocationBuilder
    ReverseEnd: bool
    Start: Diagramming.Port
    StartLocation: Diagramming.LocationBuilder


class Connection(Diagramming.SheetElement):
    def __init__(self) -> None: ...
    Label: Diagramming.Annotation


class ConnectableElementBuilder(Diagramming.SheetElementBuilder):
    def __init__(self) -> None: ...
    def GetAllPorts(self) -> typing.List[Diagramming.Port]:
        ...
    def GetPorts(self, direction: Diagramming.Direction) -> typing.List[Diagramming.Port]:
        ...


class ConnectableElement(Diagramming.SheetElement):
    def __init__(self) -> None: ...


class CannedAnnotationBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateLeaderLine(self) -> Diagramming.LeaderLineBuilder:
        ...
    def Inherit(self, inheritOption: Diagramming.CannedAnnotationBuilder.InheritOption, annotation: Diagramming.Annotation) -> None:
        ...
    AnnotationBuilder: Diagramming.AnnotationBuilder
    LeaderLines: Diagramming.LeaderLineBuilderList
    TextBoxIndent: int
    TextBoxModifiable: bool
    TextBoxShadowBox: bool


    class InheritOption(enum.Enum):
        Preferences = 0
        CustomerDefaults = 1
        Selection = 2
    

class BulkEditBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSheetElements(self, sheetElements: typing.List[Diagramming.SheetElement]) -> None:
        ...
    def SetDeltaXCoordinate(self, deltaXCoordinate: float) -> None:
        ...
    def SetDeltaYCoordinate(self, deltaYCoordinate: float) -> None:
        ...
    def SetHide(self, hide: bool) -> None:
        ...
    def SetHideLabel(self, hideLabel: bool) -> None:
        ...
    RenderingProperties: Diagramming.RenderingPropertiesBuilder


class BaseTaggedObjectBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...


class BaseSubObjectBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...


class BaseObjectBuilder(Builder):
    def __init__(self) -> None: ...


class BaseObject(DisplayableObject):
    def __init__(self) -> None: ...


class Axis(enum.Enum):
    X = 1
    Y = 2


class ArrowStyleType(enum.Enum):
    Filled = 0
    Closed = 1
    ClosedSolid = 2
    Open = 3


class ArrowDirectionType(enum.Enum):
    OutofSheet = 0
    IntoSheet = 1


class AnnotationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Diagramming.Annotation]:
        ...
    def __init__(self, owner: Diagramming.DiagrammingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateAnnotationBuilder(self, annotation: Diagramming.Annotation) -> Diagramming.AnnotationBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Diagramming.Annotation:
        ...
    def Tag(self) -> Tag: ...



class AnnotationBuilder(Diagramming.ConnectableElementBuilder):
    def __init__(self) -> None: ...
    BoundaryDisplay: bool
    BoundaryType: Diagramming.DiagrammingAnnotationboundarytype
    FormattedStringBuilder: Diagramming.FormattedStringBuilder
    Text: str
    TextStyleBuilder: Diagramming.TextStyleBuilder
    TextType: Diagramming.AnnotationBuilder.TextTypeOption


    class TextTypeOption(enum.Enum):
        Fixed = 0
        Parametric = 1
    

class Annotation(Diagramming.ConnectableElement):
    def __init__(self) -> None: ...


