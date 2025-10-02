from ...NXOpen import *
from ..Formboard import *

import typing
import enum

class UpdateFormboardBuilder(Builder):
    def __init__(self) -> None: ...
    def GetHarnessPart(self) -> Part:
        ...
    def SetHarnessPart(self, harnessPart: Part) -> None:
        ...
    def SetHarnesses(self, harnesses: typing.List[Routing.Electrical.HarnessDevice]) -> None:
        ...
    def FindMapping(self) -> None:
        ...
    def DetermineDiscrepancies(self) -> None:
        ...
    def GetNumberOfDiscrepancies(self) -> int:
        ...
    def GetDiscrepancy(self, index: int) -> Formboard.UpdateDiscrepancy:
        ...
    def RemoveBendsOfRadialBends(self) -> None:
        ...
    def CreateBendsOfRadialBends(self) -> None:
        ...
    LengthOptions: Formboard.LayoutLengthOptions


class UpdateDiscrepancy(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Description: str
    DiscrepancyObjectType: Formboard.UpdateDiscrepancy.ObjectType
    DiscrepancyType: Formboard.UpdateDiscrepancy.Type
    FormboardObject: NXObject
    HarnessObject: NXObject


    class Type(enum.Enum):
        Unknown = 0
        Missing = 1
        Extra = 2
        Modified = 3
    

    class ObjectType(enum.Enum):
        Unknown = 0
        Rcp = 1
        Segment = 2
        Clip = 3
        Component = 4
        Harness = 5
        Wire = 6
        Cable = 7
        Shield = 8
        Connector = 9
        Device = 10
        Overstock = 11
        Fillerstock = 12
        FittingOverstock = 13
    

class ShapeSegmentBuilder(Builder):
    def __init__(self) -> None: ...
    def ChangeType(self, newType: int) -> None:
        ...
    def NewSegment(self, newSegment: Routing.ISegment) -> None:
        ...
    def UpdateLineAngleVec(self, newDir: Vector3d) -> None:
        ...
    def GetLineData(self, anchorSeg: Routing.ISegment, anchorRcp: Routing.ControlPoint, angle: float) -> None:
        ...
    def CreateNewRadialBend(self, firstPivot: Point3d, firstBendMethod: int, firstBendValue: float, secondPivot: Point3d, secondBendMethod: int, secondBendValue: float) -> None:
        ...
    def AddRadialPivot(self, pivotLocation: Point3d, bendMethod: int, bendValue: float) -> None:
        ...
    def RemoveRadialPivot(self, pivotIndex: int) -> None:
        ...
    def UpdateRadialPivot(self, pivotIndex: int, newLocation: Point3d, newBendMethod: int, newBendValue: float) -> None:
        ...
    def CreateNewSpline(self, anchorLocation: Point3d, firstPoint: Point3d, secondPoint: Point3d) -> None:
        ...
    def RemoveSplinePoint(self, pointIndex: int) -> None:
        ...
    def AddSplinePoint(self, pointLocation: Point3d) -> int:
        ...
    def UpdateSplinePoint(self, pointIndex: int, pointLocation: Point3d, inDrag: bool) -> None:
        ...
    def CommitCurrentOperation(self) -> None:
        ...
    def SwapAnchorEnd(self) -> None:
        ...
    def SetActiveView(self, view: TaggedObject) -> None:
        ...


class PathLengthAnnotationBuilder(Builder):
    def __init__(self) -> None: ...
    def SetPathLengthAnnotationEndPoints(self, firstEndPoint: Point, secondEndPoint: Point) -> None:
        ...
    def CreatePointsAtRcps(self, firstEndRcp: Routing.ControlPoint, secondEndRcp: Routing.ControlPoint) -> None:
        ...
    ExpressionName: str
    FirstEndPoint: Point
    Leader: Annotations.LeaderBuilder
    Origin: Annotations.OriginBuilder
    RouteObjectCollector: Routing.RouteObjectCollector
    SecondEndPoint: Point
    ShowLeadersToggle: bool
    Style: Annotations.StyleBuilder
    Text: Annotations.TextWithEditControlsBuilder
    Type: Formboard.PathLengthAnnotationBuilder.Types


    class Types(enum.Enum):
        PointsOnCurves = 0
        RoutingPathLength = 1
    

class OrientBranchBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateRotationAngle(self, angle: float) -> None:
        """[Obsolete("Deprecated in NX9.0.1.  This method is no longer required.")"""
        ...
    def StartDrag(self) -> None:
        """[Obsolete("Deprecated in NX9.0.1.  This method is no longer required.")"""
        ...
    def StopDrag(self) -> None:
        """[Obsolete("Deprecated in NX9.0.1.  This method is no longer required.")"""
        ...
    def InitializeFromSegment(self) -> None:
        """[Obsolete("Deprecated in NX9.0.1.  This method is no longer required.")"""
        ...
    def SetBranchSeedObject(self, segmentTag: Routing.ISegment) -> None:
        ...
    def UnSuppressConstraints(self) -> None:
        """[Obsolete("Deprecated in NX7.5.3.  This method is no longer relevant and calls to this can be safely removed.")"""
        ...
    BranchAngleType: Formboard.OrientBranchBuilder.BranchAngleMethod
    FromPoint: Point
    FromVector: Direction
    RefRotationAngle: Expression
    ReferenceVector: Direction
    RotationAngle: Expression
    SelectBranch: Routing.RouteObjectCollector
    ToPoint: Point
    ToVector: Direction


    class BranchAngleMethod(enum.Enum):
        AnglefromReferenceVector = 0
        Angle = 1
        AlignAxisToVector = 2
        TwoPoints = 3
    

class ObjectAttributeReferenceBuilder(Builder):
    def __init__(self) -> None: ...
    AnnotLeader: Annotations.LeaderBuilder
    CompOrigin: Annotations.OriginBuilder
    EnumType: Formboard.ObjectAttributeReferenceBuilder.LeaderType
    ObjectSelection: SelectNXObject


    class LeaderType(enum.Enum):
        None = 0
        SingleLocation = 1
        StartandEndLocations = 2
    

class LayoutLengthOptions(Builder):
    def __init__(self) -> None: ...
    NetlistLengthIncrement: Expression
    NetlistRoundingMethod: Formboard.LayoutLengthOptions.RoundingMethod
    OverstockLengthIncrement: Expression
    OverstockRoundingMethod: Formboard.LayoutLengthOptions.RoundingMethod
    SegmentLengthIncrement: Expression
    SegmentRoundingMethod: Formboard.LayoutLengthOptions.RoundingMethod


    class RoundingMethod(enum.Enum):
        Exact = 0
        Nearest = 1
        UpToNearest = 2
        DownToNearest = 3
    

class FormboardManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Routing.RouteManager) -> None: ...
    def IsFormboard(self) -> bool:
        ...
    def StoreHarnessesToFlatten(self, harnesses: typing.List[Routing.Electrical.HarnessDevice]) -> None:
        ...
    def AddPartAs3dHarness(self, harnessPart: Part) -> None:
        ...
    def CreateLayoutBuilder(self) -> Formboard.FormboardLayoutBuilder:
        ...
    def CreateOrientBranchBuilder(self) -> Formboard.OrientBranchBuilder:
        ...
    def CreateFlipComponentBuilder(self) -> Formboard.FlipComponentBuilder:
        ...
    def CreateShapeSegmentBuilder(self, segment: Routing.ISegment) -> Formboard.ShapeSegmentBuilder:
        ...
    def CreateFaceAnnotationBuilder(self) -> Formboard.FaceAnnotationBuilder:
        ...
    def CreateObjectAttributeReferenceBuilder(self) -> Formboard.ObjectAttributeReferenceBuilder:
        ...
    def CreatePathLengthAnnotationBuilder(self, annotation: Annotations.Annotation) -> Formboard.PathLengthAnnotationBuilder:
        ...
    def CreateUpdateFormboardBuilder(self) -> Formboard.UpdateFormboardBuilder:
        ...
    def GetFmbdPlaneConstraints(self, fmbdPlane: NXObject, constraints: typing.List[Positioning.ComponentConstraint]) -> None:
        ...
    def ShowFormboardConstraints(self) -> None:
        ...
    def HideFormboardConstraints(self) -> None:
        ...
    def CalculateLegacyComponentClocking(self, component1: Assemblies.Component, component2: Assemblies.Component, displayStyle: Formboard.FormboardManager.LegacyComponentOrientationDisplayStyle, rotationVector: Vector3d, clockingAngle: float, confidenceLevel: Formboard.FormboardManager.LegacyComponentOrientationConfidenceLevel) -> None:
        ...
    def Tag(self) -> Tag: ...



    class LegacyComponentOrientationDisplayStyle(enum.Enum):
        NoDisplay = 0
        DisplayCurveNormals = 1
        DisplaySurface = 2
        DisplayAll = 3
    

    class LegacyComponentOrientationConfidenceLevel(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
    

class FormboardLayoutBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateDefaultGeometry(self) -> None:
        ...
    def UpdateLayout(self) -> None:
        ...
    def TranslateToNewOrigin(self) -> None:
        ...
    BranchAngleMethod: Formboard.FormboardLayoutBuilder.BranchAngle
    BranchShapeType: Formboard.FormboardLayoutBuilder.BranchShape
    LengthOptions: Formboard.LayoutLengthOptions
    MainRunEndSelection: Routing.SelectControlPoint
    MainRunMethod: Formboard.FormboardLayoutBuilder.MainRunType
    MainRunOrigin: Point
    MainRunStartSelection: Routing.SelectControlPoint
    MaximumRandomAngle: Expression
    MinimumRandomAngle: Expression
    PrimaryStandardAngle: Expression
    ReverseMainRun: bool
    SecondaryStandardAngle: Expression
    TertiaryStandardAngle: Expression


    class MainRunType(enum.Enum):
        Longest = 0
        Thickest = 1
        UserSelection = 2
    

    class BranchShape(enum.Enum):
        Straight = 0
        Angled = 1
    

    class BranchAngle(enum.Enum):
        AsDesigned = 0
        StandardAngles = 1
        MaximumAngles = 2
        RandomAngles = 3
    

class FlipComponentBuilder(Builder):
    def __init__(self) -> None: ...
    def StartDrag(self) -> None:
        ...
    def StopDrag(self) -> None:
        ...
    def InitializeFromComponent(self) -> None:
        ...
    def FlipComponent(self) -> None:
        ...
    def CreateDatumAxis(self) -> typing.List[NXObject]:
        ...
    def SetRotationAngle(self, angle: float) -> None:
        ...
    AxisTypeEnum: Formboard.FlipComponentBuilder.AxisType
    CompSel: SelectNXObject
    CustomAxis: Axis
    PathAxisSel: SelectNXObject


    class AxisType(enum.Enum):
        PathLocations = 0
        Custom = 1
    

class FaceAnnotationBuilder(Builder):
    def __init__(self) -> None: ...
    CgmflBrsr: str
    CompSel: SelectNXObject
    DestEnum: Formboard.FaceAnnotationBuilder.DrwDestination
    PntOrigin: Point
    StrAnnot: str
    StrAnnotFileName: str
    TogBlank: bool
    Type: Formboard.FaceAnnotationBuilder.Types


    class Types(enum.Enum):
        ComponentAttribute = 0
        CgmFileSelection = 1
        PatternFileSelection = 2
    

    class DrwDestination(enum.Enum):
        DrawingSheet = 0
        Model = 1
    

