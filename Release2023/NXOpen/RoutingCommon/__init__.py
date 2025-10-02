from ...NXOpen import *
from ..RoutingCommon import *

import typing
import enum

class TransformBlockBuilder(Builder):
    def __init__(self) -> None: ...
    ActiveTransformType: RoutingCommon.TransformBlockBuilder.Transformtype
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
    

class SubdivideCurveBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSubdividedCurves(self) -> typing.List[Curve]:
        ...
    ArcLength: GeometricUtilities.OnPathDimensionBuilder
    CreateTangencySetting: bool
    EndPercentage: GeometricUtilities.OnPathDimensionBuilder
    NumberOfSegments: int
    ReverseDirection: bool
    SelectedSegment: Routing.RouteObjectCollector
    StartPercentage: GeometricUtilities.OnPathDimensionBuilder
    SubdivideAtPoint: GeometricUtilities.OnPathDimensionBuilder
    Type: RoutingCommon.SubdivideCurveBuilder.Types


    class Types(enum.Enum):
        AtPoint = 0
        EqualSegments = 1
        ArcLengthSegments = 2
    

class StockBuilder(Builder):
    def __init__(self) -> None: ...
    def PreCommit(self) -> None:
        ...
    def GetLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    IsNonCircular: bool
    SegmentCollector: Routing.RouteObjectCollector
    StockSettings: Routing.StockBlockBuilder


class SplitBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCreatedComponents(self) -> typing.List[Assemblies.Component]:
        ...
    def PreCommit(self) -> None:
        ...
    def GetLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    ControlPointCollector: Routing.RouteObjectCollector


class SplinePointBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[RoutingCommon.SplinePointBuilder]) -> None:
        ...
    def Append(self, object: RoutingCommon.SplinePointBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: RoutingCommon.SplinePointBuilder) -> int:
        ...
    def FindItem(self, index: int) -> RoutingCommon.SplinePointBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: RoutingCommon.SplinePointBuilder) -> None:
        ...
    def Erase(self, obj: RoutingCommon.SplinePointBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[RoutingCommon.SplinePointBuilder]:
        ...
    def SetContents(self, objects: typing.List[RoutingCommon.SplinePointBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: RoutingCommon.SplinePointBuilder, object2: RoutingCommon.SplinePointBuilder) -> None:
        ...
    def Insert(self, location: int, object: RoutingCommon.SplinePointBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SplinePointBuilder(Builder):
    def __init__(self) -> None: ...
    def GetPoint(self) -> Point:
        ...
    def SetPoint(self, point: Point) -> int:
        ...
    def MovePoint(self, location: Point3d) -> None:
        ...
    def SetOffsetOption(self, offsetOption: RoutingCommon.SplinePointBuilder.OffsetOption) -> None:
        ...
    def GetOffsetOption(self) -> RoutingCommon.SplinePointBuilder.OffsetOption:
        ...
    def GetOffsetDirection(self) -> Direction:
        ...
    def SetOffsetDirection(self, dirr: Direction) -> None:
        ...
    def GetOffsetExpressionString(self) -> str:
        ...
    def SetOffsetExpressionString(self, offsetExpressionString: str) -> None:
        ...
    def DetachPoint(self) -> None:
        ...
    def InferExtension(self, spline: Curve, point: Point, direction: Direction, tangent: Vector3d, normal: Vector3d) -> None:
        ...
    def GetForwardExpression(self) -> Expression:
        ...
    def GetBackwardExpression(self) -> Expression:
        ...
    def ReverseDirection(self, direction: Direction) -> None:
        ...
    def SwapExtensions(self) -> None:
        ...
    def MoveDirection(self, direction: Direction) -> None:
        ...
    def AssignNewDirection(self, direction: Direction) -> None:
        ...
    def GetControlPoint(self) -> Routing.ControlPoint:
        ...
    def AskTangencyInformation(self, controlPoint: Routing.ControlPoint, targetCurve: Curve, origin: Point3d, vector: Vector3d) -> None:
        ...
    def AskTangencyGeometry(self, targetCurve: Curve, origin: Point3d, vector: Vector3d) -> None:
        ...
    Direction: Direction
    LockToSelected: bool
    Tangency: bool


    class OffsetOption(enum.Enum):
        None = 0
        Point = 1
        Surface = 2
        Port = 3
    

class SplineBuilder(Builder):
    def __init__(self) -> None: ...
    def RemoveDefiningPoint(self, index: int) -> None:
        ...
    def GetLockedLengthExpression(self) -> Expression:
        ...
    def GetWorkPart(self) -> Part:
        ...
    def LockSplineLengthNoShaping(self, length: Expression) -> None:
        ...
    def RemoveAllShaping(self) -> None:
        ...
    def AddSlackToSpline(self, lengthType: RoutingCommon.SplineBuilder.LengthType, lengthValue: Expression, slackDirection: Direction) -> None:
        ...
    def AssignExtensionAtPointIndex(self, pointIndex: int, location: Point3d, direction: Vector3d, forward: float, backward: float) -> None:
        ...
    def AssignExtension(self, controlPoint: Routing.ControlPoint, targetCurve: Curve, location: Point3d, direction: Vector3d, distance: float) -> None:
        ...
    def AssignTangency(self, thisControlPoint: Routing.ControlPoint, thisCurve: Curve, targetControlPoint: Routing.ControlPoint, targetCurve: Curve) -> None:
        ...
    def LockSplineLengthWithShapingFixedPoints(self, length: Expression, slackDirection: Direction) -> None:
        ...
    def LockSplineLengthWithShaping(self, length: Expression, slackDirection: Direction) -> None:
        ...
    def ShapeByAdditionalLengthMovingPoints(self, length: Expression, lengthType: RoutingCommon.SplineBuilder.LengthType) -> None:
        ...
    def RemoveTangency(self, point: RoutingCommon.SplinePointBuilder) -> None:
        ...
    def CanAssignTangency(self, point: RoutingCommon.SplinePointBuilder) -> bool:
        ...
    def IsCurvatureControlled(self) -> bool:
        ...
    def EnableCurvatureControl(self, minRadiusExp: Expression) -> None:
        ...
    def DisableCurvatureControl(self) -> None:
        ...
    def GetBoundedCurvatureRadius(self) -> Expression:
        ...
    def HasCurvatureControlFailed(self) -> bool:
        ...
    MinimumCheckingAllowableRatio: Expression
    MinimumCheckingAllowableValue: Expression
    MinimumCheckingMethod: RoutingCommon.SplineBuilder.SplineAttributeOptions
    PointList: RoutingCommon.SplinePointBuilderList
    RemoveExtensionUponDetach: bool
    ShowSplineMinimumRadius: bool
    SplineCurve: Curve
    StockSettings: Routing.StockBlockBuilder
    UseMinimumCheckingValue: bool


    class SplineAttributeOptions(enum.Enum):
        Radius = 0
        RatioToDiameter = 1
    

    class LengthType(enum.Enum):
        LockLength = 0
        TotalPercentage = 1
        TotalAdditional = 2
        Undefined = 3
    

class SimplifyCurvesBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSimplifiedCurves(self) -> typing.List[Curve]:
        ...
    SegmentCollector: Routing.RouteObjectCollector


class RoutingManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetRoutingManager(self, owner: Session) -> RoutingCommon.RoutingManager:
        ...
    def IsRouteSystemAssembly(self, part: Part) -> bool:
        ...
    def IsShapeComponentPart(self, part: BasePart) -> bool:
        """[Obsolete("Deprecated in NX1980.0.0.  This method is no longer required. Use IsStockComponentPart, IsInsulationComponentPart instead")"""
        ...
    def IsReusableComponentPart(self, part: BasePart) -> bool:
        ...
    def MakeComponentReusable(self, component: Assemblies.Component) -> bool:
        ...
    def PerformDetachOperationOnRcp(self, rcp: Routing.ControlPoint) -> bool:
        ...
    def PerformDetachOperationOnPort(self, port: Routing.Port) -> bool:
        ...
    def IsStockComponentPart(self, part: BasePart) -> bool:
        ...
    def IsInsulationComponentPart(self, part: BasePart) -> bool:
        ...
    def StoreReuseLibraryDisciplineWithinPart(self, part: Part, discipline: str) -> bool:
        ...
    def StoreReuseLibrarySpecificationWithinPart(self, part: Part, specification: str) -> bool:
        ...
    def GetSavedDisciplineAndSpecificationFromThePart(self, part: Part, discipline: str, specification: str) -> None:
        ...
    def RestoreDisciplineAndSpecificationFromThePart(self, part: Part, disciplineSuccess: bool, specificationSuccess: bool) -> None:
        ...
    def ConditionAssemblyForTraditionalRouting(self, part: Part) -> bool:
        ...
    def Tag(self) -> Tag: ...

    BuilderFactory: RoutingCommon.BuilderFactory
    InsulationService: RoutingCommon.InsulationService


class ReparentPartsBuilder(Builder):
    def __init__(self) -> None: ...
    def PreCommit(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def ShowStockSummary(self) -> None:
        ...
    ActionType: RoutingCommon.ReparentPartsBuilder.StockActionType
    AllowSelectionOfLiveStock: bool
    SelectedParts: Routing.RouteObjectCollector


    class StockActionType(enum.Enum):
        CreateNew = 0
        TransferExisting = 1
    

class PathTransitionListManagerBuilder(Builder):
    def __init__(self) -> None: ...
    def CreatePathTransitionBuilder(self, part: Part) -> RoutingCommon.PathTransitionBuilder:
        ...
    PathTransitionBuilderList: RoutingCommon.PathTransitionBuilderList


class PathTransitionBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[RoutingCommon.PathTransitionBuilder]) -> None:
        ...
    def Append(self, object: RoutingCommon.PathTransitionBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: RoutingCommon.PathTransitionBuilder) -> int:
        ...
    def FindItem(self, index: int) -> RoutingCommon.PathTransitionBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: RoutingCommon.PathTransitionBuilder) -> None:
        ...
    def Erase(self, obj: RoutingCommon.PathTransitionBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[RoutingCommon.PathTransitionBuilder]:
        ...
    def SetContents(self, objects: typing.List[RoutingCommon.PathTransitionBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: RoutingCommon.PathTransitionBuilder, object2: RoutingCommon.PathTransitionBuilder) -> None:
        ...
    def Insert(self, location: int, object: RoutingCommon.PathTransitionBuilder) -> None:
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
    BoxOrientation: RoutingCommon.PathTransitionBuilder.HealOrientation
    ConnectedObject: NXObject
    EndPoint: Point
    ExtensionVector: Direction
    ForwardExtension: Expression
    HealSolutionCsys: CoordinateSystem
    HealTraversalOrder: RoutingCommon.PathTransitionBuilder.TraversalOrder
    PathForwardThroughExtensionVector: bool
    TransitionType: RoutingCommon.PathTransitionBuilder.Type


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
    

class PathDimensionBuilder(GeometricUtilities.OnPathDimensionBuilder):
    def __init__(self) -> None: ...
    def UpdateExpression(self) -> None:
        ...
    def GetOrderedPathCurves(self, pathCurves: typing.List[Curve]) -> None:
        ...
    def SetOrderedPathCurves(self, pathCurves: typing.List[Curve]) -> None:
        ...
    def GetValueAsLength(self) -> float:
        ...


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
        """[Obsolete("Deprecated in NX12.0.0.  Use RoutingCommon.PartPlacementBuilder.ProcessPlacedPart.")"""
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
    def CommitThisPlacement(self) -> RoutingCommon.PartPlacementBuilder.PlacementValidationStatus:
        ...
    def SetPrimarySolutionsFlag(self, showPrimarySolutions: bool) -> None:
        ...
    def GetFilteredPlacementSolutions(self) -> typing.List[Placement.PlacementSolution]:
        ...
    def SetPortOfPlaceableObject(self, sourcePortObject: TaggedObject) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  No replacement method will be provided.")"""
        ...
    def SetPositionAsOption(self, positioningType: RoutingCommon.PartPlacementBuilder.PositionAsType) -> None:
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
    def GetLibraryDefinedAttributeHolder(self) -> Routing.AttributeHolder:
        ...
    def GetLibraryDefinedPostPlacementAttributeHolder(self) -> Routing.AttributeHolder:
        ...
    def CopyAttributesToPartToPlace(self, sourcePartOccurrence: Assemblies.Component) -> None:
        ...
    def ResetAttributesOnLibraryDefinedAttributeHolder(self) -> None:
        ...
    def ResetAttributesOnPostPlaceLibraryDefinedAttributeHolder(self) -> None:
        ...
    def DesignateComponentForPlacementSolutionComputation(self, partOccurrence: Assemblies.Component) -> None:
        ...
    def PerformOperationsAfterPlacement(self) -> None:
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
    CopyModeType: RoutingCommon.MovePathBuilder.CopyMode
    DetachType: RoutingCommon.MovePathBuilder.DetachTypes
    MaintainLength: bool
    Motion: GeometricUtilities.ModlMotion
    PathSelection: Routing.RouteObjectCollector
    Preview: bool
    TargetAssembly: Assemblies.SelectComponent


    class DetachTypes(enum.Enum):
        AlwaysMaintainConnections = 0
        DetachSelectedObjects = 1
    

    class CopyMode(enum.Enum):
        NoCopy = 0
        CopyToWorkPart = 1
        CopyToTarget = 2
    

class MergeBuilder(Builder):
    def __init__(self) -> None: ...
    CandidateStockComponentCollector: Routing.RouteObjectCollector
    SimplifyPath: bool
    TargetStockComponentCollector: Routing.RouteObjectCollector


class ManageInlineBehaviorBuilder(Builder):
    def __init__(self) -> None: ...
    def SetModelElementRevision(self, modelElementRevision: PDM.ModelElementRevision) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use RoutingCommon.ManageInlineBehaviorBuilder.SetComponent instead.")"""
        ...
    def SetComponent(self, component: Assemblies.Component) -> None:
        ...
    def SetComponents(self, components: typing.List[TaggedObject]) -> None:
        ...
    def SetInlineBehavior(self, isInline: bool) -> None:
        ...
    def GetInlineBehavior(self) -> bool:
        ...


class InsulationService(Utilities.NXRemotableObject):
    def __init__(self, owner: RoutingCommon.RoutingManager) -> None: ...
    def GetAllInsulatedObjectsInContainer(self, container: Assemblies.Component) -> typing.List[NXObject]:
        ...
    def Tag(self) -> Tag: ...



class InsulationBuilder(Builder):
    def __init__(self) -> None: ...
    def PreCommit(self) -> None:
        ...
    def GetLogicalObject(self) -> PDM.LogicalObject:
        ...
    def SuggestWrapMethodBasedOnStockSettings(self) -> RoutingCommon.InsulationBuilder.WrapType:
        ...
    def UpdatePath(self) -> None:
        ...
    def GetOrderedPath(self, orderedPath: typing.List[TaggedObject]) -> None:
        ...
    def CreateScalarPoint(self, partToCreatePointIn: Part, pointLocation: float) -> TaggedObject:
        ...
    AddInsulationOnFittings: bool
    ApplicationMethod: RoutingCommon.InsulationBuilder.ApplicationType
    EndOffsetPoint: RoutingCommon.PathDimensionBuilder
    EndPoint: RoutingCommon.PathDimensionBuilder
    GapDistance: Expression
    InsulationPartOccurrenceSelection: Assemblies.SelectComponent
    OffsetMethod: RoutingCommon.InsulationBuilder.OffsetMethodType
    OverlapPercentage: Expression
    SegmentCollector: Routing.RouteObjectCollector
    StartOffsetPoint: RoutingCommon.PathDimensionBuilder
    StartPoint: RoutingCommon.PathDimensionBuilder
    StockSettings: Routing.StockBlockBuilder
    SwitchStartEnd: bool
    WrapMethod: RoutingCommon.InsulationBuilder.WrapType


    class WrapType(enum.Enum):
        NoWarp = 0
        OverlapSpiral = 1
        StripedSpiral = 2
    

    class OffsetMethodType(enum.Enum):
        FromBothEnds = 0
        FromOneEnd = 1
    

    class ApplicationType(enum.Enum):
        EntireSegments = 0
        Offsets = 1
        PointAndLength = 2
    

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
    ActiveEditSegmentType: RoutingCommon.EditPointBuilder.Editsegmenttype
    ActiveMotionType: RoutingCommon.EditPointBuilder.Motiontype
    BendAngle: float
    MaintainAngle: bool
    MaintainLength: bool
    PointSelection: Routing.RouteObjectCollector
    Segment: Routing.ISegment
    SegmentLength: float
    TransformTool: RoutingCommon.TransformBlockBuilder


    class Motiontype(enum.Enum):
        MovePoint = 0
        EditSegment = 1
    

    class Editsegmenttype(enum.Enum):
        None = 0
        Length = 1
        Angle = 2
    

class EditPlacementBuilder(Builder):
    def __init__(self) -> None: ...
    PartPlacementBuilder: RoutingCommon.PartPlacementBuilder


class DerivedPathBuilder(Builder):
    def __init__(self) -> None: ...
    Associativity: RoutingCommon.DerivedPathBuilder.AssociativityType
    CurveSelection: Section
    NumberOfPoints: int
    SelectedCurveVisibility: RoutingCommon.DerivedPathBuilder.SelectedCurveStatus


    class SelectedCurveStatus(enum.Enum):
        Visible = 0
        Hidden = 1
    

    class AssociativityType(enum.Enum):
        Associative = 0
        Copy = 1
    

class CustomManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def AddDesignRule(self, reason: Routing.CustomManager.DesignRuleReason, name: str, description: str, designRuleMethod: RoutingCommon.CustomManager.DesignRule) -> int:
        ...
    def RemoveDesignRule(self, designRuleMethodId: int) -> None:
        ...
    def RemoveAllDesignRulesForReason(self, reason: Routing.CustomManager.DesignRuleReason) -> None:
        ...
    def RemoveAllDesignRules(self) -> None:
        ...
    def GetDesignRulesRegisteredForReason(self, reason: Routing.CustomManager.DesignRuleReason, registeredDesignRuleIds: int) -> None:
        ...
    def GetViolationsForReason(self, reason: Routing.CustomManager.DesignRuleReason) -> typing.List[Routing.DesignRuleViolation]:
        ...
    def GetViolationsOfRule(self, designRuleName: str) -> typing.List[Routing.DesignRuleViolation]:
        ...
    def CreateViolationForReason(self, designRuleName: str, reason: Routing.CustomManager.DesignRuleReason, shortDescription: str, longDescription: str, objects: typing.List[NXObject]) -> Routing.DesignRuleViolation:
        ...
    def DeleteViolationsOnObjectForReason(self, reason: Routing.CustomManager.DesignRuleReason, nxObject: NXObject) -> None:
        ...
    def DeleteViolationsOfRuleOnObject(self, designRuleName: str, nxObject: NXObject) -> None:
        ...
    def RemoveAllPlugins(self) -> None:
        ...
    def SetRSDApplicationEnterPlugin(self, applicationEnterPlugin: RoutingCommon.CustomManager.RSDApplicationEnterPlugin) -> None:
        ...
    def RemoveRSDApplicationEnterPlugin(self) -> None:
        ...
    def SetRSDApplicationExitPlugin(self, applicationExitPlugin: RoutingCommon.CustomManager.RSDApplicationExitPlugin) -> None:
        ...
    def RemoveRSDApplicationExitPlugin(self) -> None:
        ...
    def SetCablewayXmlFileNamePlugin(self, xmlFileNamePlugin: RoutingCommon.CustomManager.CablewayXmlFileNamePlugin) -> None:
        ...
    def RemoveCablewayXmlFileNamePlugin(self) -> None:
        ...
    def SetCablewayUniqueNodeNamePlugin(self, uniqueNodeNamePlugin: RoutingCommon.CustomManager.CablewayUniqueNodeNamePlugin) -> None:
        ...
    def RemoveCablewayUniqueNodeNamePlugin(self) -> None:
        ...
    def SetCablewayUniqueSegmentNamePlugin(self, uniqueSegmentNamePlugin: RoutingCommon.CustomManager.CablewayUniqueSegmentNamePlugin) -> None:
        ...
    def RemoveCablewayUniqueSegmentNamePlugin(self) -> None:
        ...
    def SetCablewayDeviceIdentifierPlugin(self, cablewayDeviceIdentifierPlugin: RoutingCommon.CustomManager.CablewayDeviceIdentifierPlugin) -> None:
        ...
    def RemoveCablewayDeviceIdentifierPlugin(self) -> None:
        ...
    def SetCablewayPreExportPlugin(self, cablewayPreExportPlugin: RoutingCommon.CustomManager.CablewayPreExportPlugin) -> None:
        ...
    def RemoveCablewayPreExportPlugin(self) -> None:
        ...
    def SetCablewayPostExportPlugin(self, cablewayPostExportPlugin: RoutingCommon.CustomManager.CablewayPostExportPlugin) -> None:
        ...
    def RemoveCablewayPostExportPlugin(self) -> None:
        ...
    def SetCablewayAreaNamePlugin(self, cablewayAreaNamePlugin: RoutingCommon.CustomManager.CablewayAreaNamePlugin) -> None:
        ...
    def RemoveCablewayAreaNamePlugin(self) -> None:
        ...
    def SetWiringComponentNamePlugin(self, wiringComponentNamePlugin: RoutingCommon.CustomManager.ComponentNamePlugin) -> None:
        ...
    def RemoveWiringComponentNamePlugin(self) -> None:
        ...
    def Tag(self) -> Tag: ...



    

    

    

    

    

    

    

    

    

    

    

    class Application(enum.Enum):
        Electrical = 0
        Mechanical = 1
    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

class CreatePathBuilder(Builder):
    def __init__(self) -> None: ...
    def CreatePathTransitionManagerBuilder(self, workPart: Part, workOcc: Assemblies.Component, displayPart: Part) -> RoutingCommon.PathTransitionListManagerBuilder:
        ...
    def PreCommit(self) -> None:
        ...
    def GetLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def GetBendCornerAttributes(self, attributes: typing.List[NXObject.AttributeInformation]) -> None:
        ...
    def SetBendCornerAttributes(self, attributes: typing.List[NXObject.AttributeInformation]) -> None:
        ...
    def RemoveBendCornerAttributes(self, corners: typing.List[Routing.Corner]) -> None:
        ...
    def SetLogicalConnection(self, connection: TaggedObject) -> None:
        ...
    def GetLogicalConnection(self) -> TaggedObject:
        ...
    BendCornerSettings: RoutingCommon.BendCornerTypeBuilder
    CornerSettings: RoutingCommon.CornerBuilder
    PathStockBuilder: RoutingCommon.StockBuilder
    PathTransitionListManagerBuilder: RoutingCommon.PathTransitionListManagerBuilder
    StockSettings: Routing.StockBlockBuilder


class CornerBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BendCornerSettings: RoutingCommon.BendCornerTypeBuilder
    CornerType: RoutingCommon.CornerBuilder.Type


    class Type(enum.Enum):
        None = 0
        Bend = 1
        Miter = 2
    

class ConnectBuilder(Builder):
    def __init__(self) -> None: ...
    ComponentsCollector: Assemblies.SelectComponentList


class BuilderFactory(Utilities.NXRemotableObject):
    def __init__(self, owner: RoutingCommon.RoutingManager) -> None: ...
    def CreateInsulationBuilder(self, part: Part, workOcc: Assemblies.Component, insulationPartOccurrence: Assemblies.Component) -> RoutingCommon.InsulationBuilder:
        ...
    def CreateAssignComponentNameBuilder(self, part: Part, workOcc: Assemblies.Component) -> RoutingCommon.AssignComponentNameBuilder:
        ...
    def CreateSubdivideCurveBuilder(self, part: Part, segment: NXObject, pickPoint: Point3d) -> RoutingCommon.SubdivideCurveBuilder:
        ...
    def CreateSimplifyCurvesBuilder(self, part: Part, workOcc: Assemblies.Component, segments: typing.List[Routing.ISegment]) -> RoutingCommon.SimplifyCurvesBuilder:
        ...
    def CreateStockBuilder(self, part: Part, workOcc: Assemblies.Component, segmentsOrStocks: typing.List[NXObject]) -> RoutingCommon.StockBuilder:
        ...
    def CreateSplitBuilder(self, part: Part, controlPoints: typing.List[Routing.ControlPoint]) -> RoutingCommon.SplitBuilder:
        ...
    def CreateConnectBuilder(self, part: Part, components: typing.List[Assemblies.Component]) -> RoutingCommon.ConnectBuilder:
        """[Obsolete("Deprecated in NX1847.0.0.  This method is no longer required. Use overloaded version of this method")"""
        ...
    def CreateConnectBuilder(self, part: Part, workOcc: Assemblies.Component, components: typing.List[Assemblies.Component]) -> RoutingCommon.ConnectBuilder:
        ...
    def CreateMergeBuilder(self, part: Part, workOcc: Assemblies.Component) -> RoutingCommon.MergeBuilder:
        ...
    def CreateMovePathBuilder(self, part: Part, workOcc: Assemblies.Component) -> RoutingCommon.MovePathBuilder:
        ...
    def CreateEditPointBuilder(self, part: Part, workOcc: Assemblies.Component) -> RoutingCommon.EditPointBuilder:
        ...
    def CreateTransformBlockBuilder(self, part: Part) -> RoutingCommon.TransformBlockBuilder:
        ...
    def CreateAssignCornerBuilder(self, part: Part, workOcc: Assemblies.Component) -> RoutingCommon.AssignCornerBuilder:
        ...
    def CreatePathBuilder(self, part: Part, workOcc: Assemblies.Component) -> RoutingCommon.CreatePathBuilder:
        ...
    def CreatePartPlacementBuilder(self, part: Part, workOcc: Assemblies.Component) -> RoutingCommon.PartPlacementBuilder:
        ...
    def CreateEditPlacementBuilder(self, part: Part, workOcc: Assemblies.Component) -> RoutingCommon.EditPlacementBuilder:
        ...
    def CreateManageInlineBehaviorBuilder(self, part: Part) -> RoutingCommon.ManageInlineBehaviorBuilder:
        """[Obsolete("Deprecated in NX1847.0.0.  This method is no longer required.")"""
        ...
    def CreateManageInlineBehaviorBuilder(self, part: Part, workOcc: Assemblies.Component) -> RoutingCommon.ManageInlineBehaviorBuilder:
        ...
    def CreateSplineBuilder(self, part: Part, rootpart: Part, activePathComp: Assemblies.Component, spline: Curve) -> RoutingCommon.SplineBuilder:
        ...
    def CreateSplinePointBuilder(self, part: Part, splineBuilder: RoutingCommon.SplineBuilder) -> RoutingCommon.SplinePointBuilder:
        ...
    def CreateReparentPartsBuilder(self, part: Part) -> RoutingCommon.ReparentPartsBuilder:
        ...
    def CreateDerivedPathBuilder(self, part: Part) -> RoutingCommon.DerivedPathBuilder:
        ...
    def Tag(self) -> Tag: ...



class BendCornerTypeBuilder(RoutingCommon.BaseCornerTypeBuilder):
    def __init__(self) -> None: ...
    Method: RoutingCommon.BendCornerTypeBuilder.BendMethod
    Radius: Expression
    RadiusFromBendTable: float
    RatioToAttributeName: str
    RatioToAttributeValue: Expression
    RatioToDiameter: Expression
    StockPartNumberFromBendTable: str


    class BendMethod(enum.Enum):
        Radius = 0
        RatioToDiameter = 1
        RatioToAttribute = 2
        BendRadiusTable = 3
        InnerRadius = 4
    

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
    def GetBendCornerAttributes(self, attributes: typing.List[NXObject.AttributeInformation]) -> None:
        ...
    def SetBendCornerAttributes(self, attributes: typing.List[NXObject.AttributeInformation]) -> None:
        ...
    def RemoveBendCornerAttributes(self, corners: typing.List[Routing.Corner]) -> None:
        ...
    BendCornerSettings: RoutingCommon.BendCornerTypeBuilder
    ControlPointSelection: Routing.RouteObjectCollector
    CornerSettings: RoutingCommon.CornerBuilder
    Type: RoutingCommon.AssignCornerBuilder.CornerType


    class CornerType(enum.Enum):
        None = 0
        Bend = 1
        Miter = 2
    

class AssignComponentNameBuilder(Builder):
    def __init__(self) -> None: ...
    def SetPartSpecOnLogicalObject(self, logicalObject: PDM.LogicalObject, partSpec: str) -> None:
        ...


