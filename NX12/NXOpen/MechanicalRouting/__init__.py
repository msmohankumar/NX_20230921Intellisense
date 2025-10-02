from ...NXOpen import *
from ..MechanicalRouting import *

import typing
import enum

class TransformBlockBuilder(Builder):
    def __init__(self) -> None: ...
    ActiveTransformType: MechanicalRouting.TransformBlockBuilder.Transformtype
    ConstrainedPoint: Point
    InitialOrientation: Matrix3x3
    InitialPosition: Point3d
    OrientExpress: GeometricUtilities.OrientXpressBuilder
    Plane: Plane
    TempOrientation: Matrix3x3
    TempPosition: Point3d
    Vector: Direction


    class Transformtype(enum.Enum):
        None = -1
        OrientXpress = 0
        Vector = 1
        View = 2
        Manipulator = 3
        Plane = 4
    

class StockBuilder(Builder):
    def __init__(self) -> None: ...
    def PreCommit(self) -> None:
        ...
    def GetLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    CrossSectionDirection: Direction
    MirrorCrossSection: bool
    OrientationAngle: Expression
    SegmentCollector: Routing.RouteObjectCollector
    StockAnchor: str
    StockSettings: MechanicalRouting.PathStockPreferenceBuilder


class SplitBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCreatedComponents(self) -> typing.List[Assemblies.Component]:
        ...
    def PreCommit(self) -> None:
        ...
    def GetLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    ControlPointCollector: Routing.RouteObjectCollector


class RoutingManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetRoutingManager(self, owner: Session) -> MechanicalRouting.RoutingManager:
        ...
    def Tag(self) -> Tag: ...

    BuilderFactory: MechanicalRouting.BuilderFactory
    ConnectivityService: MechanicalRouting.ConnectivityService
    LogicalDesignService: MechanicalRouting.LogicalDesignService
    InsulationService: MechanicalRouting.InsulationService


class PipingComponentFileBuilder(Builder):
    def __init__(self) -> None: ...
    ComponentsCollector: Routing.RouteObjectCollector
    PcfFileName: str


class PathTransitionListManagerBuilder(Builder):
    def __init__(self) -> None: ...
    def CreatePathTransitionBuilder(self, part: Part) -> MechanicalRouting.PathTransitionBuilder:
        ...
    PathTransitionBuilderList: MechanicalRouting.PathTransitionBuilderList


class PathTransitionBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[MechanicalRouting.PathTransitionBuilder]) -> None:
        ...
    def Append(self, object: MechanicalRouting.PathTransitionBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: MechanicalRouting.PathTransitionBuilder) -> int:
        ...
    def FindItem(self, index: int) -> MechanicalRouting.PathTransitionBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: MechanicalRouting.PathTransitionBuilder) -> None:
        ...
    def Erase(self, obj: MechanicalRouting.PathTransitionBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[MechanicalRouting.PathTransitionBuilder]:
        ...
    def SetContents(self, objects: typing.List[MechanicalRouting.PathTransitionBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: MechanicalRouting.PathTransitionBuilder, object2: MechanicalRouting.PathTransitionBuilder) -> None:
        ...
    def Insert(self, location: int, object: MechanicalRouting.PathTransitionBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PathTransitionBuilder(Builder):
    def __init__(self) -> None: ...
    AddExtensionToggle: bool
    BackwardExtension: Expression
    BoxOrientation: MechanicalRouting.PathTransitionBuilder.HealOrientation
    ConnectedObject: NXObject
    EndPoint: Point
    ExtensionVector: Direction
    ForwardExtension: Expression
    HealSolutionCsys: CoordinateSystem
    HealTraversalOrder: MechanicalRouting.PathTransitionBuilder.TraversalOrder
    PathForwardThroughExtensionVector: bool
    TransitionType: MechanicalRouting.PathTransitionBuilder.Type


    class Type(enum.Enum):
        Direct = 0
        Heal = 1
        Intersect = 2
    

    class TraversalOrder(enum.Enum):
        Xyz = 0
        Xzy = 1
        Yzx = 2
        Yxz = 3
        Zxy = 4
        Zyx = 5
        Invalid = 6
    

    class HealOrientation(enum.Enum):
        Wcs = 0
        Absolute = 1
        Start = 2
        End = 3
        NewCsys = 4
    

class PathStockPreferenceBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetClassificationObjectIdentifier(self, classificationObjectId: str) -> None:
        """[Obsolete("Deprecated in NX11.0.1.  Use NXOpen.MechanicalRouting.PathStockPreferenceBuilder.SetClassificationObjectIdentifierForStock instead.")"""
        ...
    def GetClassificationObjectIdentifierForStock(self) -> str:
        ...
    def SetClassificationObjectIdentifierForStock(self, classificationObjectId: str) -> None:
        ...
    def GetFileSpecificationOfStockToPlace(self) -> str:
        ...
    def SetFileSpecificationOfStockToPlace(self, filename: str) -> None:
        ...
    def GetClassificationObjectIdentifierForSpaceReservation(self) -> str:
        ...
    def SetClassificationObjectIdentifierForSpaceReservation(self, classificationObjectId: str) -> None:
        ...
    def GetFileSpecificationOfSpaceReservationToPlace(self) -> str:
        ...
    def SetFileSpecificationOfSpaceReservationToPlace(self, filename: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AssignStockMethod: MechanicalRouting.PathStockPreferenceBuilder.AssignMethod
    Diameter: Expression
    FlatOvalHeight: Expression
    FlatOvalWidth: Expression
    RectangularHeight: Expression
    RectangularWidth: Expression
    SpaceReservationMethodType: MechanicalRouting.PathStockPreferenceBuilder.SpaceReservationMethod
    StartObject: NXObject
    StockMethodType: MechanicalRouting.PathStockPreferenceBuilder.StockMethod
    StockSubType: MechanicalRouting.PathStockPreferenceBuilder.AssignStockSubType
    StockType: MechanicalRouting.PathStockPreferenceBuilder.AssignStockType


    class StockMethod(enum.Enum):
        None = 0
        SpecifiedStock = 1
    

    class SpaceReservationMethod(enum.Enum):
        None = 0
        FromStartObject = 1
        Circular = 2
        Rectangular = 3
        FlatOval = 4
        SpecifiedSpaceReservation = 5
    

    class AssignStockType(enum.Enum):
        Stock = 0
        Overstock = 1
    

    class AssignStockSubType(enum.Enum):
        Stock = 0
        SpaceReservation = 1
    

    class AssignMethod(enum.Enum):
        None = 0
        FromStartObject = 1
        Circular = 2
        Rectangular = 3
        FlatOval = 4
        SpecifiedStock = 5
    

class PartPlacementBuilder(Builder):
    def __init__(self) -> None: ...
    def SetFileSpecificationOfPartToPlace(self, filename: str) -> None:
        ...
    def SetClassificationObjectIdentifier(self, classificationObjectId: str) -> None:
        ...
    def SetReferenceObjectForPlacement(self, referenceObject: TaggedObject, referencePositionPoint: Point3d) -> None:
        ...
    def LoadPart(self) -> BasePart:
        ...
    def CreatePartOccurrenceToPlace(self, referenceSet: str, layer: int) -> Assemblies.Component:
        ...
    def ProcessComponentsForEdit(self) -> None:
        ...
    def InitializePlacementEngineBuilder(self) -> Placement.PlacementEngineBuilder:
        ...
    def PreCommitThisPlacement(self) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use MechanicalRouting.PartPlacementBuilder.ProcessPlacedPart followed by MechanicalRouting.PartPlacementBuilder.PrepareDataForConnectivity.")"""
        ...
    def ProcessPlacedPart(self) -> None:
        ...
    def ProcessPostPlaceParts(self) -> typing.List[Assemblies.Component]:
        ...
    def GetCoincidentPortForCompatibility(self, portFromPlacedPart: Routing.Port) -> Routing.Port:
        ...
    def ProcessCompatibilityPostPlaceParts(self) -> typing.List[Assemblies.Component]:
        ...
    def PrepareDataForConnectivity(self) -> None:
        ...
    def CommitThisPlacement(self) -> MechanicalRouting.PartPlacementBuilder.PlacementValidationStatus:
        ...
    def SetPrimarySolutionsFlag(self, showPrimarySolutions: bool) -> None:
        ...
    def GetFilteredPlacementSolutions(self) -> typing.List[Placement.PlacementSolution]:
        ...
    def SetPortOfPlaceableObject(self, sourcePortObject: TaggedObject) -> None:
        ...
    def SetPositionAsOption(self, positioningType: MechanicalRouting.PartPlacementBuilder.PositionAsType) -> None:
        ...
    def RotatePlaceableObjectByAngle(self, rotationAngle: float) -> None:
        ...
    def SetClassificationObjectIdentifierOfPartToPostPlace(self, classificationObjectId: str) -> None:
        ...
    def SetClassificationObjectIdentifierOfCompatibilityPart(self, ccType: Routing.ReuseLibrary.PartType, classificationObjectId: str, portOne: Routing.Port, portTwo: Routing.Port) -> None:
        ...
    def UpdateReferenceSet(self, referenseSetName: str) -> None:
        ...
    def UpdateLayer(self, layerNumber: int) -> None:
        ...
    def AutoAssignAttributes(self) -> None:
        ...
    def GetLogicalObjectsHavingUnassignedRequiredAttributes(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def GetLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def GetErrorCodeForPlacementSolution(self, placementSolution: Placement.PlacementSolution) -> int:
        ...
    def SetAddUnconnectedEquipmentToActiveRunOption(self, canAddEquipmentToActiveRun: bool) -> None:
        ...
    def GetPortAtCutSideOfElbow(self) -> Routing.Port:
        ...
    ComponentsToEditCollector: Routing.RouteObjectCollector
    LogicalDesignObject: NXObject


    class PositionAsType(enum.Enum):
        Routing = 0
        Equipment = 1
    

    class PlacementValidationStatus(enum.Enum):
        Success = 0
        PartNotConnectedToRout = 1
    

class MovePathBuilder(Builder):
    def __init__(self) -> None: ...
    def StartDrag(self) -> None:
        ...
    def DragObjects(self) -> None:
        ...
    def StopDrag(self) -> None:
        ...
    def ResetDrag(self) -> None:
        ...
    DetachType: MechanicalRouting.MovePathBuilder.DetachTypes
    MaintainLength: bool
    Motion: GeometricUtilities.ModlMotion
    PathSelection: Routing.RouteObjectCollector
    Preview: bool


    class DetachTypes(enum.Enum):
        AlwaysMaintainConnections = 0
        AllowDetachOnConflict = 1
        DetachSelectedObjects = 2
    

class MergeBuilder(Builder):
    def __init__(self) -> None: ...
    CandidateStockComponentCollector: Routing.RouteObjectCollector
    SimplifyPath: bool
    TargetStockComponentCollector: Routing.RouteObjectCollector


class ManageInlineBehaviorBuilder(Builder):
    def __init__(self) -> None: ...
    def SetModelElementRevision(self, modelElementRevision: PDM.ModelElementRevision) -> None:
        ...
    def SetInlineBehavior(self, isInline: bool) -> None:
        ...
    def GetInlineBehavior(self) -> bool:
        ...


class LogicalDesignService(Utilities.NXRemotableObject):
    def __init__(self, owner: MechanicalRouting.RoutingManager) -> None: ...
    def Assign3DPortToLogicalPort(self, logicalPort: NXObject, physicalPort: Routing.Port) -> None:
        ...
    def Unassign3DPortsFromLogicalPort(self, container: Assemblies.Component, logicalPort: NXObject) -> None:
        ...
    def GetMappingStatus(self, routingObject: NXObject, container: Assemblies.Component) -> MechanicalRouting.LogicalDesignService.MappingStatus:
        ...
    def GetMappingStatusMessage(self, routingObject: NXObject, container: Assemblies.Component) -> str:
        ...
    def AssignComponentsToLogicalConnection(self, components: typing.List[Assemblies.Component], logicalConnection: NXObject) -> None:
        ...
    def UnassignComponentsToLogicalConnection(self, container: Assemblies.Component, logicalConnection: NXObject) -> None:
        ...
    def AssignComponentToLogicalEquipment(self, logicalEquipment: NXObject, component: Assemblies.Component) -> None:
        ...
    def UnassignComponentToLogicalEquipment(self, container: Assemblies.Component, logicalEquipment: NXObject) -> None:
        ...
    def GetRunsInContainer(self, container: Assemblies.Component) -> typing.List[NXObject]:
        ...
    def MakeRunActive(self, container: Assemblies.Component, run: NXObject) -> None:
        ...
    def GetActiveRun(self, container: Assemblies.Component) -> NXObject:
        ...
    def EnsureLogicalModelIsLoaded(self, container: Assemblies.Component) -> None:
        ...
    def ReassignComponentsFromLogicalConnection(self, container: Assemblies.Component, sourceLogicalConnection: NXObject, destinationObject: NXObject) -> None:
        ...
    def ReassignComponentsToRun(self, components: typing.List[Assemblies.Component], run: NXObject) -> None:
        ...
    def DeleteRuns(self, runs: typing.List[NXObject]) -> None:
        ...
    def LoadAllComponents(self, run: NXObject) -> None:
        ...
    def IsRunIncludedInSubset(self, container: Assemblies.Component, run: NXObject) -> bool:
        ...
    def Tag(self) -> Tag: ...



    class MappingStatus(enum.Enum):
        Pass = 0
        OutOfDate = 1
        Unloaded = 2
        Fail = 3
        Unknown = 4
    

class InsulationService(Utilities.NXRemotableObject):
    def __init__(self, owner: MechanicalRouting.RoutingManager) -> None: ...
    def GetAllInsulatedObjectsInContainer(self, container: Assemblies.Component) -> typing.List[NXObject]:
        ...
    def Tag(self) -> Tag: ...



class InsulationBuilder(Builder):
    def __init__(self) -> None: ...
    def PreCommit(self) -> None:
        ...
    def GetLogicalObject(self) -> PDM.LogicalObject:
        ...
    def SuggestWrapMethodBasedOnStockSettings(self) -> MechanicalRouting.InsulationBuilder.WrapType:
        ...
    AddInsulationOnFittings: bool
    GapDistance: Expression
    InsulationPartOccurrenceSelection: Assemblies.SelectComponent
    OverlapPercentage: Expression
    SegmentCollector: Routing.RouteObjectCollector
    StockSettings: MechanicalRouting.PathStockPreferenceBuilder
    WrapMethod: MechanicalRouting.InsulationBuilder.WrapType


    class WrapType(enum.Enum):
        NoWarp = 0
        OverlapSpiral = 1
        StripedSpiral = 2
    

class EditPointBuilder(Builder):
    def __init__(self) -> None: ...
    def StartDrag(self) -> None:
        ...
    def DragObjects(self) -> None:
        ...
    def StopDrag(self) -> None:
        ...
    def ResetDrag(self) -> None:
        ...
    ActiveEditSegmentType: MechanicalRouting.EditPointBuilder.Editsegmenttype
    ActiveMotionType: MechanicalRouting.EditPointBuilder.Motiontype
    BendAngle: float
    IsDetachObject: bool
    MaintainAngle: bool
    MaintainLength: bool
    PointSelection: Routing.RouteObjectCollector
    Segment: Line
    SegmentLength: float
    TransformTool: MechanicalRouting.TransformBlockBuilder


    class Motiontype(enum.Enum):
        MovePoint = 0
        EditSegment = 1
    

    class Editsegmenttype(enum.Enum):
        None = 0
        Length = 1
        Angle = 2
    

class EditPlacementBuilder(Builder):
    def __init__(self) -> None: ...
    PartPlacementBuilder: MechanicalRouting.PartPlacementBuilder


class DynamicCutElbowBehaviorBuilder(Builder):
    def __init__(self) -> None: ...
    def SetModelElementRevision(self, modelElementRevision: PDM.ModelElementRevision) -> None:
        ...
    def SetLockedCutElbow(self, lockState: bool) -> None:
        ...
    def IsLockedCutElbow(self) -> bool:
        ...


class CreatePathBuilder(Builder):
    def __init__(self) -> None: ...
    def CreatePathTransitionManagerBuilder(self, workPart: Part, workOcc: Assemblies.Component, displayPart: Part) -> MechanicalRouting.PathTransitionListManagerBuilder:
        ...
    def PreCommit(self) -> None:
        ...
    def GetLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    BendCornerSettings: MechanicalRouting.BendCornerTypeBuilder
    CornerSettings: MechanicalRouting.CornerBuilder
    PathTransitionListManagerBuilder: MechanicalRouting.PathTransitionListManagerBuilder
    PlaceDefaultElbow: bool
    SimplifyPath: bool
    SnapAngle: float
    SnapToElbowAngles: bool
    StockSettings: MechanicalRouting.PathStockPreferenceBuilder


class CornerBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BendCornerSettings: MechanicalRouting.BendCornerTypeBuilder
    CornerType: MechanicalRouting.CornerBuilder.Type


    class Type(enum.Enum):
        None = 0
        Bend = 1
        Miter = 2
    

class ConnectivityService(Utilities.NXRemotableObject):
    def __init__(self, owner: MechanicalRouting.RoutingManager) -> None: ...
    def GetConnectedPorts(self, part: Part, connectedPorts1: typing.List[Routing.Port], connectedPorts2: typing.List[Routing.Port]) -> None:
        ...
    def GetPortsConnectedToDesignElement(self, part: Assemblies.Component, connectedPorts1: typing.List[Routing.Port], connectedPorts2: typing.List[Routing.Port]) -> None:
        ...
    def Tag(self) -> Tag: ...



class ConnectBuilder(Builder):
    def __init__(self) -> None: ...
    ComponentsCollector: Assemblies.SelectComponentList


class BulkReplacementBuilder(Routing.BulkReplacementBuilder):
    def __init__(self) -> None: ...


class BuilderFactory(Utilities.NXRemotableObject):
    def __init__(self, owner: MechanicalRouting.RoutingManager) -> None: ...
    def CreateEditPointBuilder(self, part: Part, workOcc: Assemblies.Component) -> MechanicalRouting.EditPointBuilder:
        ...
    def CreatePartPlacementBuilder(self, part: Part, workOcc: Assemblies.Component) -> MechanicalRouting.PartPlacementBuilder:
        ...
    def CreateEditPlacementBuilder(self, part: Part, workOcc: Assemblies.Component) -> MechanicalRouting.EditPlacementBuilder:
        ...
    def CreateManageInlineBehaviorBuilder(self, part: Part) -> MechanicalRouting.ManageInlineBehaviorBuilder:
        ...
    def CreateMovePathBuilder(self, part: Part, workOcc: Assemblies.Component) -> MechanicalRouting.MovePathBuilder:
        ...
    def CreateCreatePathBuilder(self, part: Part, workOcc: Assemblies.Component) -> MechanicalRouting.CreatePathBuilder:
        ...
    def CreateStockBuilder(self, part: Part, workOcc: Assemblies.Component, segmentsOrStocks: typing.List[NXObject]) -> MechanicalRouting.StockBuilder:
        ...
    def CreateSplitBuilder(self, part: Part, controlPoints: typing.List[Routing.ControlPoint]) -> MechanicalRouting.SplitBuilder:
        ...
    def CreateTransformBlockBuilder(self, part: Part) -> MechanicalRouting.TransformBlockBuilder:
        ...
    def CreateInsulationBuilder(self, part: Part, insulationPartOccurrence: Assemblies.Component) -> MechanicalRouting.InsulationBuilder:
        ...
    def CreateAssignCornerBuilder(self, part: Part, workOcc: Assemblies.Component) -> MechanicalRouting.AssignCornerBuilder:
        ...
    def CreateMergeBuilder(self, part: Part, workOcc: Assemblies.Component) -> MechanicalRouting.MergeBuilder:
        ...
    def CreateConnectBuilder(self, part: Part, components: typing.List[Assemblies.Component]) -> MechanicalRouting.ConnectBuilder:
        ...
    def CreateDynamicCutElbowBehaviorBuilder(self, part: Part) -> MechanicalRouting.DynamicCutElbowBehaviorBuilder:
        ...
    def CreatePipingComponentFileBuilder(self, part: Part) -> MechanicalRouting.PipingComponentFileBuilder:
        ...
    def CreateBulkReplacementBuilder(self, part: Part, workOcc: Assemblies.Component, segmentsOrStocks: typing.List[NXObject]) -> MechanicalRouting.BulkReplacementBuilder:
        ...
    def Tag(self) -> Tag: ...



class BendCornerTypeBuilder(MechanicalRouting.BaseCornerTypeBuilder):
    def __init__(self) -> None: ...
    def ImportBendRadiusTable(self, bendTableFilename: str) -> None:
        ...
    BendTable: str
    Method: MechanicalRouting.BendCornerTypeBuilder.BendMethod
    Radius: Expression
    RatioToDiameter: Expression


    class BendMethod(enum.Enum):
        Radius = 0
        RatioToDiameter = 1
        BendRadiusTable = 2
        InnerRadius = 3
    

class BaseCornerTypeBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...


class AssignCornerBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCreatedComponents(self) -> typing.List[Assemblies.Component]:
        ...
    def PreCommit(self) -> None:
        ...
    def GetLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    BendCornerSettings: MechanicalRouting.BendCornerTypeBuilder
    ControlPointSelection: Routing.RouteObjectCollector
    CornerSettings: MechanicalRouting.CornerBuilder
    Type: MechanicalRouting.AssignCornerBuilder.CornerType


    class CornerType(enum.Enum):
        None = 0
        Bend = 1
        Miter = 2
    

