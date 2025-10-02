from . import Mechanical
from . import Model
from ...NXOpen import *
from ..Schematic import *

import typing
import enum

class SymbolSourceOption(enum.Enum):
    ReuseLibrary = 0
    ExistingSymbol = 1
    ModelNode = 2


class SheetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Schematic.Sheet]:
        ...
    def __init__(self, owner: Schematic.SchematicManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Schematic.Sheet:
        ...
    def Tag(self) -> Tag: ...



class Sheet(NXObject):
    def __init__(self) -> None: ...


class SchematicManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateSheet(self) -> Schematic.Sheet:
        ...
    def CreateNodeBuilder(self, node: Schematic.Node) -> Schematic.NodeBuilder:
        ...
    def CreateConnectionBuilder(self, connection: Schematic.Connection) -> Schematic.ConnectionBuilder:
        ...
    def CreateFdaBuilder(self, node: Diagramming.Node) -> Schematic.FlowDirectionArrowBuilder:
        ...
    def CreateBulkEditBuilder(self) -> Schematic.BulkEditBuilder:
        ...
    def CreatePreferencesBuilder(self, sheet: Schematic.Sheet) -> Schematic.PreferencesBuilder:
        ...
    def CreatePortBuilder(self, port: Schematic.Port) -> Schematic.PortBuilder:
        ...
    def Tag(self) -> Tag: ...

    Sheets: Schematic.SheetCollection
    Nodes: Schematic.NodeCollection
    Connections: Schematic.ConnectionCollection
    Ports: Schematic.PortCollection


class RotateAngleOption(enum.Enum):
    Zero = 0
    Ninety = 1
    OneHundredAndEighty = 2
    TwoHundredAndSeventy = 3


class PreferencesGeneralBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    HidePorts: bool


class PreferencesConnectionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AllowNonOrthogonalConnections: bool
    ArrowSize: float
    ArrowStyle: Diagramming.DiagrammingFlowdirectionarrowstyle
    JumperGap: float
    JumperPriority: Diagramming.DiagrammingJumperprioritytype
    JumperPriorityUseLineType: bool
    JumperType: Diagramming.DiagrammingJumpertype
    MinimumSegmentLength: float
    SnapAngle: float
    TeeSize: float


class PreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    Annotation: Schematic.PreferencesAnnotationBuilder
    Connection: Schematic.PreferencesConnectionBuilder
    General: Schematic.PreferencesGeneralBuilder


class PreferencesAnnotationBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ConnectionLabelHorizontalOffsetPosition: Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition
    ConnectionLabelOffset: float
    ConnectionLabelPositionCenter: bool
    ConnectionLabelVerticalOffsetPosition: Diagramming.DiagrammingConnectionlabelverticaloffsetposition
    TablesBorderCellSettings: Diagramming.RenderingPropertiesBuilder
    TablesCellSettings: Diagramming.Tables.CellSettingsBuilder
    TextStyleConnectionBuilder: Diagramming.TextStyleBuilder
    TextStyleNoteBuilder: Diagramming.TextStyleBuilder


class PortDirectionOption(enum.Enum):
    Input = 0
    Output = 1
    BiDirectional = 2


class PortCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Schematic.Port]:
        ...
    def __init__(self, owner: Schematic.SchematicManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Schematic.Port:
        ...
    def Tag(self) -> Tag: ...



class PortBuilder(Schematic.BaseObjectBuilder):
    def __init__(self) -> None: ...
    def GetNode(self) -> Schematic.Node:
        ...
    def SetNode(self, schNode: Schematic.Node) -> None:
        ...
    ExistingSymbol: Diagramming.Port
    LockAspectRatio: bool
    RelativePercentX: float
    RelativePercentY: float
    RelativeValueX: float
    RelativeValueY: float
    Scale: float
    ScaleX: float
    ScaleY: float
    SymbolId: str
    SymbolSourceType: Schematic.SymbolSourceOption


class Port(NXObject):
    def __init__(self) -> None: ...


class NodeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Schematic.Node]:
        ...
    def __init__(self, owner: Schematic.SchematicManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Schematic.Node:
        ...
    def Tag(self) -> Tag: ...



class NodeBuilder(Schematic.BaseObjectBuilder):
    def __init__(self) -> None: ...
    def GetLocation(self) -> Point2d:
        ...
    def SetLocation(self, location: Point2d) -> None:
        ...
    def GetNode(self) -> Diagramming.Node:
        ...
    def DetachAllConnections(self) -> None:
        ...
    def SetInlineSymbolLocation(self, connection: Schematic.Connection, segementId: int, percent: float) -> None:
        ...
    def GetInlineSymbolLocation(self, connection: Schematic.Connection, segementId: int, percent: float) -> None:
        ...
    ExistingSymbol: Diagramming.Node
    FlipHorizontal: bool
    FlipVertical: bool
    LockAspectRatio: bool
    Rotate: Schematic.RotateAngleOption
    Scale: float
    ScaleX: float
    ScaleY: float
    SymbolId: str
    SymbolSourceType: Schematic.SymbolSourceOption


class Node(NXObject):
    def __init__(self) -> None: ...


class FlowDirectionArrowBuilder(Builder):
    def __init__(self) -> None: ...
    def GetConnection(self) -> Schematic.Connection:
        ...
    def SetConnection(self, connection: Schematic.Connection) -> None:
        ...
    def ReverseDirection(self) -> None:
        ...
    LocationPercent: float
    LocationSegment: int


class FlowDirectionArrow(NXObject):
    def __init__(self) -> None: ...


class ConnectionEndType(enum.Enum):
    Start = 0
    End = 1


class ConnectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Schematic.Connection]:
        ...
    def __init__(self, owner: Schematic.SchematicManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Schematic.Connection:
        ...
    def Tag(self) -> Tag: ...



class ConnectionBuilder(Schematic.BaseObjectBuilder):
    def __init__(self) -> None: ...
    def GetLineType(self) -> str:
        ...
    def SetLineType(self, lineType: str) -> None:
        ...
    def GetBendPoints(self, points: typing.List[Point2d]) -> None:
        ...
    def SetBendPoints(self, points: typing.List[Point2d]) -> None:
        ...
    def GetConnection(self) -> Diagramming.Connection:
        ...
    def GetStartLocation(self) -> Point2d:
        ...
    def SetStartLocation(self, startLocation: Point2d) -> None:
        ...
    def GetEndLocation(self) -> Point2d:
        ...
    def SetEndLocation(self, endLocation: Point2d) -> None:
        ...
    def GetStart(self) -> Schematic.Port:
        ...
    def SetStart(self, port: Schematic.Port) -> None:
        ...
    def GetEnd(self) -> Schematic.Port:
        ...
    def SetEnd(self, port: Schematic.Port) -> None:
        ...
    def GetTeeStartLocation(self, connection: Schematic.Connection, segmentId: int, percent: float) -> None:
        ...
    def SetTeeStartLocation(self, connection: Schematic.Connection, segmentId: int, percent: float) -> None:
        ...
    def GetTeeEndLocation(self, connection: Schematic.Connection, segmentId: int, percent: float) -> None:
        ...
    def SetTeeEndLocation(self, connection: Schematic.Connection, segmentId: int, percent: float) -> None:
        ...
    ElementId: str


class Connection(NXObject):
    def __init__(self) -> None: ...


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


class BaseObjectBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDisciplines(self) -> str:
        ...
    def SetDisciplines(self, disciplines: str) -> None:
        ...
    Id: str
    Label: str
    Sheet: Schematic.Sheet


