from . import VehicleDesign
from . import ShipDesign
from . import Subdivision
from . import SheetMetal
from ...NXOpen import *
from ..Features import *

import typing
import enum

class WrapUnwrap(Features.CurveFeature):
    def __init__(self) -> None: ...


class WrapGeometryBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AddOffset: Expression
    Associative: bool
    CloseGaps: Features.WrapGeometryBuilder.CloseGapType
    DistTol: float
    Geometry: SelectDisplayableObjectList
    IsInterpart: bool
    PlanesList: PlaneList
    SplitOffset: Expression


    class CloseGapType(enum.Enum):
        Sharp = 0
        Beveled = 1
        NoOffset = 2
    

class WrapGeometry(Features.BodyFeature):
    def __init__(self) -> None: ...


class WrapBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    Associative: bool
    Curves: Section
    CutLineAngle: Expression
    DistanceTolerance: float
    Faces: ScCollector
    Plane: SelectISurface
    SpecifyPlane: Plane
    Type: Features.WrapBuilder.Types


    class Types(enum.Enum):
        Wrap = 0
        Unwrap = 1
    

class WaveSketchBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CommitCreateOnTheFly(self) -> Features.Feature:
        ...
    def GetWaveLinkInformation(self, info: str, xformExists: bool, xformOrigin: Point3d, xformOrientation: Matrix3x3, xformScale: float) -> None:
        ...
    def GetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def SetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def GetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    def SetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    Associative: bool
    DisplayReferenceGeometry: bool
    HideOriginal: bool
    InheritDisplayProperties: bool
    MakePositionIndependent: bool
    ParentPart: Features.WaveSketchBuilder.ParentPartType
    Sketches: SelectTaggedObjectList
    SourcePartOccurrence: TaggedObject


    class ParentPartType(enum.Enum):
        WorkPart = 0
        OtherPart = 1
    

class WaveSketch(Features.Feature):
    def __init__(self) -> None: ...


class WaveRoutingBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CommitCreateOnTheFly(self) -> Features.Feature:
        ...
    def GetWaveLinkInformation(self, info: str, xformExists: bool, xformOrigin: Point3d, xformOrientation: Matrix3x3, xformScale: float) -> None:
        ...
    Associative: bool
    MakePositionIndependent: bool
    RoutingObjects: SelectObjectList


class WaveRouting(Features.Feature):
    def __init__(self) -> None: ...


class WavePointBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CommitCreateOnTheFly(self) -> Features.Feature:
        ...
    def GetWaveLinkInformation(self, info: str, xformExists: bool, xformOrigin: Point3d, xformOrientation: Matrix3x3, xformScale: float) -> None:
        ...
    def GetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def SetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def GetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    def SetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    Associative: bool
    DrawLineBetweenPoints: bool
    FixAtCurrentTimestamp: bool
    FrecAtTimeStamp: Features.Feature
    InheritDisplayProperties: bool
    MakePositionIndependent: bool
    ParentPart: Features.WavePointBuilder.ParentPartType
    Points: SelectPointList
    SourcePartOccurrence: TaggedObject


    class ParentPartType(enum.Enum):
        WorkPart = 0
        OtherPart = 1
    

class WavePoint(Features.Feature):
    def __init__(self) -> None: ...


class WaveLinkBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    BlankOriginal: bool
    CompositeCurveBuilder: Features.CompositeCurveBuilder
    CopyThreads: bool
    ExtractFaceBuilder: Features.ExtractFaceBuilder
    FixAtCurrentTimestamp: bool
    MakePositionIndependent: bool
    MirrorBodyBuilder: Features.MirrorBodyBuilder
    Type: Features.WaveLinkBuilder.Types
    WaveDatumBuilder: Features.WaveDatumBuilder
    WavePointBuilder: Features.WavePointBuilder
    WaveRoutingBuilder: Features.WaveRoutingBuilder
    WaveSketchBuilder: Features.WaveSketchBuilder


    class Types(enum.Enum):
        CurveLink = 0
        PointLink = 1
        DatumLink = 2
        SketchLink = 3
        FaceLink = 4
        RegionLink = 5
        BodyLink = 6
        MirrorBodyLink = 7
        RoutingObjectLink = 8
    

class WaveLink(Features.Feature):
    def __init__(self) -> None: ...


class WaveInterfaceLinkerBuilder(Builder):
    def __init__(self) -> None: ...
    def SetALL(self) -> None:
        ...
    def ClearAll(self) -> None:
        ...
    def InsertObjects(self, selectedObjects: typing.List[TaggedObject]) -> None:
        ...
    def RemoveObjects(self, removedObjects: typing.List[TaggedObject]) -> None:
        ...
    Associative: bool
    CopyThreads: bool
    DisplayReferenceGeometry: bool
    InheritDisplayProperties: bool
    MakePositionIndependent: bool
    SourcePartOccurrence: TaggedObject


class WaveDatumBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CommitCreateOnTheFly(self) -> Features.Feature:
        ...
    def GetWaveLinkInformation(self, info: str, xformExists: bool, xformOrigin: Point3d, xformOrientation: Matrix3x3, xformScale: float) -> None:
        ...
    def SetSynchlinkEntry(self, entryState: bool) -> None:
        ...
    def GetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def SetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def GetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    def SetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    Associative: bool
    Datums: SelectObjectList
    DisplayScale: float
    HideOriginal: bool
    InheritDisplayProperties: bool
    MakePositionIndependent: bool
    ParentPart: Features.WaveDatumBuilder.ParentPartType
    ReverseDirection: bool
    SourcePartOccurrence: TaggedObject


    class ParentPartType(enum.Enum):
        WorkPart = 0
        OtherPart = 1
    

class WaveDatum(Features.Feature):
    def __init__(self) -> None: ...


class VirtualCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    BlendFace: ScCollector
    RevolvedFace: ScCollector
    Type: Features.VirtualCurveBuilder.Types


    class Types(enum.Enum):
        RotationAxis = 0
        BlendCenterline = 1
        VirtualIntersection = 2
    

class VirtualCurve(Features.CurveFeature):
    def __init__(self) -> None: ...


class VirtualBlendEdgeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Selection: SelectNXObject


class VehicleDesignCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def CreateManikinBuilder(self, manikin: Features.VehicleDesign.Manikin) -> Features.VehicleDesign.ManikinBuilder:
        ...
    def CreateTireEnvelopeBuilder(self, tireEnvelope: Features.VehicleDesign.TireEnvelope) -> Features.VehicleDesign.TireEnvelopeBuilder:
        ...
    def CreateAllAroundVisionBuilder(self, allAroundVision: Features.VehicleDesign.AllAroundVision) -> Features.VehicleDesign.AllAroundVisionBuilder:
        ...
    def CreateBaseDataImportExportBuilder(self) -> Features.VehicleDesign.BaseDataImportExportBuilder:
        ...
    def CreateOilPanBuilder(self, oilPan: Features.VehicleDesign.OilPan) -> Features.VehicleDesign.OilPanBuilder:
        ...
    def CreateBaseDataBuilder(self) -> Features.VehicleDesign.BaseDataBuilder:
        ...
    def CreateWheelCoveringBuilder(self, wheelCovering: Features.VehicleDesign.WheelCovering) -> Features.VehicleDesign.WheelCoveringBuilder:
        ...
    def CreateStaticCurbBuilder(self, feature: Features.VehicleDesign.StaticCurb) -> Features.VehicleDesign.StaticCurbBuilder:
        ...
    def CreateDynamicCurbBuilder(self, dynamicCurb: Features.VehicleDesign.DynamicCurb) -> Features.VehicleDesign.DynamicCurbBuilder:
        ...
    def CreateSlopeBuilder(self, feature: Features.VehicleDesign.Slope) -> Features.VehicleDesign.SlopeBuilder:
        ...
    def CreateCrashBarrierBuilder(self, crashBarrier: Features.VehicleDesign.CrashBarrier) -> Features.VehicleDesign.CrashBarrierBuilder:
        ...
    def CreateWheelFixingBuilder(self, wheelFixing: Features.VehicleDesign.WheelFixing) -> Features.VehicleDesign.WheelFixingBuilder:
        ...
    def CreateBumperPendulumBuilder(self, bumperPendulum: Features.VehicleDesign.BumperPendulum) -> Features.VehicleDesign.BumperPendulumBuilder:
        ...
    def CreateInnerAngleBuilder(self, innerAngle: Features.VehicleDesign.InnerAngle) -> Features.VehicleDesign.InnerAngleBuilder:
        ...
    def CreateGroundClearanceBuilder(self, groundClearance: Features.VehicleDesign.GroundClearance) -> Features.VehicleDesign.GroundClearanceBuilder:
        ...
    def CreateCloseRangeVisibilityBuilder(self, closeRangeVisibility: Features.VehicleDesign.CloseRangeVisibility) -> Features.VehicleDesign.CloseRangeVisibilityBuilder:
        ...
    def CreatePedestrianProtectionBuilder(self, pedestrianProtection: Features.VehicleDesign.PedestrianProtection) -> Features.VehicleDesign.PedestrianProtectionBuilder:
        ...
    def CreateVisionPlaneBuilder(self, visionPlane: Features.VehicleDesign.VisionPlane) -> Features.VehicleDesign.VisionPlaneBuilder:
        ...
    def CreateWindshieldDatumBuilder(self, windshieldDatum: Features.VehicleDesign.WindshieldDatum) -> Features.VehicleDesign.WindshieldDatumBuilder:
        ...
    def CreateHeadImpactBuilder(self, headImpact: Features.VehicleDesign.HeadImpact) -> Features.VehicleDesign.HeadImpactBuilder:
        ...
    def CreateHeadImpactUpperRoofBuilder(self, headImpactUpperRoof: Features.VehicleDesign.HeadImpactUpperRoof) -> Features.VehicleDesign.HeadImpactUpperRoofBuilder:
        ...
    def CreateHeadImpactApillarBuilder(self, headImpactApillar: Features.VehicleDesign.HeadImpactAPillar) -> Features.VehicleDesign.HeadImpactAPillarBuilder:
        ...
    def CreateHeadImpactBpillarBuilder(self, headImpactBpillar: Features.VehicleDesign.HeadImpactBPillar) -> Features.VehicleDesign.HeadImpactBPillarBuilder:
        ...
    def CreateHeadImpactRpillarBuilder(self, headImpactRpillar: Features.VehicleDesign.HeadImpactRPillar) -> Features.VehicleDesign.HeadImpactRPillarBuilder:
        ...
    def CreateHeadImpactOpillarBuilder(self, headImpactOpillar: Features.VehicleDesign.HeadImpactOPillar) -> Features.VehicleDesign.HeadImpactOPillarBuilder:
        ...
    def CreateHeadImpactFrontHeaderBuilder(self, headImpactFrontHeader: Features.VehicleDesign.HeadImpactFrontHeader) -> Features.VehicleDesign.HeadImpactFrontHeaderBuilder:
        ...
    def CreateHeadImpactRearHeaderBuilder(self, headImpactRearHeader: Features.VehicleDesign.HeadImpactRearHeader) -> Features.VehicleDesign.HeadImpactRearHeaderBuilder:
        ...
    def CreateHeadImpactSideRailBuilder(self, headImpactSideRail: Features.VehicleDesign.HeadImpactSideRail) -> Features.VehicleDesign.HeadImpactSideRailBuilder:
        ...
    def CreateHeadImpactOtherRailBuilder(self, headImpactOtherRail: Features.VehicleDesign.HeadImpactOtherRail) -> Features.VehicleDesign.HeadImpactOtherRailBuilder:
        ...
    def CreateMirrorCertificationBuilder(self, mirrorCertification: Features.VehicleDesign.MirrorCertification) -> Features.VehicleDesign.MirrorCertificationBuilder:
        ...
    def CreateSeatBeltAnchorageBuilder(self, seatBeltAnchorage: Features.VehicleDesign.SeatBeltAnchorage) -> Features.VehicleDesign.SeatBeltAnchorageBuilder:
        ...
    def CreateReflectionDataBuilder(self, reflectionData: Features.VehicleDesign.ReflectionData) -> Features.VehicleDesign.ReflectionDataBuilder:
        ...
    def CreateHoodVisibilityBuilder(self, hoodVisibility: Features.VehicleDesign.HoodVisibility) -> Features.VehicleDesign.HoodVisibilityBuilder:
        ...
    def CreateVehicleCoordinateSystemBuilder(self, vehicleCoordinateSystem: Features.VehicleDesign.VehicleCoordinateSystem) -> Features.VehicleDesign.VehicleCoordinateSystemBuilder:
        ...
    def CreateBaseDataSourceBuilder(self) -> Features.VehicleDesign.BaseDataSourceBuilder:
        ...
    def Tag(self) -> Tag: ...



class VarsweepBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def NewListItem(self) -> GeometricUtilities.SecondarySectionData:
        ...
    AngularTolerance: float
    BooleanOperation: GeometricUtilities.BooleanOperation
    ConstantFittingSectionCount: int
    DistanceTolerance: float
    FeatureOptions: GeometricUtilities.FeatureOptions
    Limits: GeometricUtilities.Limits
    List: ObjectList
    MergeFacesOption: bool
    PathIncrement: GeometricUtilities.OnPathDimensionBuilder
    PlayButtons: GeometricUtilities.PlayButtonsBuilder
    ReProjectCurvesOption: bool
    ReviewSection: bool
    Section: Section
    SketchOnPathFeature: Features.Feature


class Varsweep(Features.BodyFeature):
    def __init__(self) -> None: ...


class VarOffsetFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateRegionListItem(self) -> Features.RegionListItemBuilder:
        ...
    def InsertPointBoundaryMap(self, regionPoint: NXObject, regionBoundaries: typing.List[NXObject]) -> None:
        ...
    def ErasePointBoundaryMap(self, regionPoint: NXObject) -> None:
        ...
    def InsertPointLaminarMap(self, regionPoint: NXObject, regionLaminarEdges: typing.List[NXObject]) -> None:
        ...
    def ErasePointLaminarMap(self, regionPoint: NXObject) -> None:
        ...
    BodyOutput: Features.VarOffsetFaceBuilder.Output
    BoundaryObject: SelectTaggedObjectList
    BridgeContinuity: Features.VarOffsetFaceBuilder.Continuity
    OffsetDirection: bool
    OffsetSolid: bool
    ProjectionDirection: GeometricUtilities.ProjectionOptions
    RegionList: Features.RegionListItemBuilderList
    TargetFace: ScCollector
    Type: Features.VarOffsetFaceBuilder.Types


    class Types(enum.Enum):
        Panel = 0
        Pad = 1
        Network = 2
    

    class Output(enum.Enum):
        OffsetasNewBody = 0
        OffsetOriginalBody = 1
    

    class Continuity(enum.Enum):
        Connected = 0
        Tangent = 1
    

class VarOffsetFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class VariableRadiusPointsBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.VariableRadiusPointsBuilder]) -> None:
        ...
    def Append(self, object: Features.VariableRadiusPointsBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.VariableRadiusPointsBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.VariableRadiusPointsBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.VariableRadiusPointsBuilder) -> None:
        ...
    def Erase(self, obj: Features.VariableRadiusPointsBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.VariableRadiusPointsBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.VariableRadiusPointsBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.VariableRadiusPointsBuilder, object2: Features.VariableRadiusPointsBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.VariableRadiusPointsBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class VariableRadiusPointsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Location: Point
    Radius: Expression


class VariableOffsetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DistanceTolerance: float
    Face: SelectFace
    IsApplyToAll: bool
    IsKeepParameterization: bool
    IsReverseDirection: bool
    Method: Features.VariableOffsetBuilder.MethodOptions
    OffsetAtA: Expression
    OffsetAtB: Expression
    OffsetAtC: Expression
    OffsetAtD: Expression
    PointA: Point
    PointB: Point
    PointC: Point
    PointD: Point


    class MethodOptions(enum.Enum):
        Linear = 0
        Cubic = 1
    

class VariableOffset(Features.BodyFeature):
    def __init__(self) -> None: ...


class UserDefinedObjectFeatureBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    UserDefinedClass: UserDefinedObjects.UserDefinedClass
    UserDefinedObject: UserDefinedObjects.UserDefinedObject


class UserDefinedObjectFeature(Features.Feature):
    def __init__(self) -> None: ...
    def LogUserDefinedObjectFeatureForUpdate(self) -> None:
        ...


class UserDefinedFeatureUpdateEvent(TaggedObject):
    def __init__(self) -> None: ...
    def GetExpressionData(self) -> typing.List[Features.UserDefinedFeatureExpressionData]:
        ...
    def GetReferenceData(self) -> typing.List[Features.UserDefinedFeatureReferenceData]:
        ...
    def GetComponentFeatures(self) -> typing.List[Features.Feature]:
        ...
    ApplicationData: Features.UserDefinedFeatureApplicationData
    ClassName: str
    ComponentFeature: Features.Feature
    Instantiation: Features.Feature


class UserDefinedFeatureReferenceData(TaggedObject):
    def __init__(self) -> None: ...
    Prompt: str
    Reference: TaggedObject


class UserDefinedFeatureIconEvent(TaggedObject):
    def __init__(self) -> None: ...
    ClassName: str
    IconName: str
    Instantiation: Features.Feature


class UserDefinedFeatureExpressionData(TaggedObject):
    def __init__(self) -> None: ...
    Expression: Expression
    Prompt: str


class UserDefinedFeatureEditEvent(TaggedObject):
    def __init__(self) -> None: ...
    ClassName: str
    Feature: Features.Feature
    Response: int


class UserDefinedFeatureCreateEvent(TaggedObject):
    def __init__(self) -> None: ...
    def GetExpressionData(self) -> typing.List[Features.UserDefinedFeatureExpressionData]:
        ...
    def GetReferenceData(self) -> typing.List[Features.UserDefinedFeatureReferenceData]:
        ...
    def GetComponentFeatures(self) -> typing.List[Features.Feature]:
        ...
    ApplicationData: Features.UserDefinedFeatureApplicationData
    ClassName: str
    CopiedFeature: Features.Feature
    Definition: Features.Feature
    OriginalFeature: Features.Feature


class UserDefinedFeatureCopyEvent(TaggedObject):
    def __init__(self) -> None: ...
    def GetExpressionData(self) -> typing.List[Features.UserDefinedFeatureExpressionData]:
        ...
    def GetReferenceData(self) -> typing.List[Features.UserDefinedFeatureReferenceData]:
        ...
    def GetComponentFeatures(self) -> typing.List[Features.Feature]:
        ...
    ApplicationData: Features.UserDefinedFeatureApplicationData
    ClassName: str
    CopiedFeature: Features.Feature
    OriginalFeature: Features.Feature
    OriginalInstantiation: Features.Feature


class UserDefinedFeatureClassManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateClass(self, className: str) -> Features.UserDefinedFeatureClass:
        ...
    def GetClassFromName(self, className: str) -> Features.UserDefinedFeatureClass:
        ...
    def GetClasses(self) -> typing.List[Features.UserDefinedFeatureClass]:
        ...
    def Tag(self) -> Tag: ...



class UserDefinedFeatureClass(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddEditHandler(self, editCallback: Features.UserDefinedFeatureClass.EditCallback) -> None:
        ...
    def AddCreateHandler(self, createCallback: Features.UserDefinedFeatureClass.CreateCallback) -> None:
        ...
    def AddUpdateHandler(self, updateCallback: Features.UserDefinedFeatureClass.UpdateCallback) -> None:
        ...
    def AddIconHandler(self, iconCallback: Features.UserDefinedFeatureClass.IconCallback) -> None:
        ...
    def AddCopyHandler(self, copyCallback: Features.UserDefinedFeatureClass.CopyCallback) -> None:
        ...
    ClassName: str


    

    

    

    

    

class UserDefinedFeatureApplicationField(TaggedObject):
    def __init__(self) -> None: ...
    def GetIntegers(self) -> int:
        ...
    def SetIntegers(self, integers: int) -> None:
        ...
    def GetDoubles(self) -> float:
        ...
    def SetDoubles(self, doubles: float) -> None:
        ...
    def GetStrings(self) -> str:
        ...
    def SetStrings(self, strings: str) -> None:
        ...
    def GetObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetObjects(self, objects: typing.List[TaggedObject]) -> None:
        ...
    Name: str


class UserDefinedFeatureApplicationData(TaggedObject):
    def __init__(self) -> None: ...
    def GetFields(self) -> typing.List[Features.UserDefinedFeatureApplicationField]:
        ...
    def AddField(self, name: str) -> Features.UserDefinedFeatureApplicationField:
        ...
    def GetField(self, name: str) -> Features.UserDefinedFeatureApplicationField:
        ...
    def RemoveField(self, field: Features.UserDefinedFeatureApplicationField) -> None:
        ...


class UntrimBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def RemoveParameter(self, untrimFeature: Features.Feature) -> None:
        ...
    Associative: bool
    FacesToUntrim: ScCollector
    HideOriginal: bool


class Untrim(Features.BodyFeature):
    def __init__(self) -> None: ...


class UnsewBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    EdgeCollector: ScCollector
    FaceCollector: ScCollector
    KeepOriginal: bool
    Output: Features.UnsewBuilder.UnsewOutput
    ToolOption: Features.UnsewBuilder.UnsewTool


    class UnsewTool(enum.Enum):
        Face = 0
        Edge = 1
    

    class UnsewOutput(enum.Enum):
        OneBodyForConnectedFaces = 0
        OneBodyForEachFace = 1
    

class Unsew(Features.BodyFeature):
    def __init__(self) -> None: ...


class UniversalUnform(Features.Feature):
    def __init__(self) -> None: ...




class Unbend(Features.Feature):
    def __init__(self) -> None: ...


class TubeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BooleanOption: GeometricUtilities.BooleanOperation
    InnerDiameter: Expression
    OuterDiameter: Expression
    OutputOption: Features.TubeBuilder.Output
    PathSection: Section
    Tolerance: float


    class Output(enum.Enum):
        MultipleSegments = 0
        SingleSegment = 1
    

class Tube(Features.BodyFeature):
    def __init__(self) -> None: ...


class TrimSheetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AllowTargetEdgesAsToolObjects: bool
    ApplyToCopyOfSheets: bool
    BoundaryObjects: SelectObjectList
    ExtendBoundaryObject: bool
    ImprintBothSide: bool
    KeepDiscardMethod: Features.TrimSheetBuilder.KeepDiscardOption
    OutputExactGeometry: bool
    ProjectionDirection: GeometricUtilities.ProjectionOptions
    Regions: RegionPointList
    TargetBodies: SelectBodyList
    Tolerance: float


    class KeepDiscardOption(enum.Enum):
        Keep = 0
        Discard = 1
    

class TrimSheet(Features.BodyFeature):
    def __init__(self) -> None: ...


class TrimLineDevelopment(Features.BodyFeature):
    def __init__(self) -> None: ...


class TrimFeatureCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def CreateExtendSheetBuilder(self, extendSheet: Features.ExtendSheet) -> Features.ExtendSheetBuilder:
        ...
    def CreateTrimAndExtendBuilder(self, trimAndExtendSheet: Features.TrimAndExtend) -> Features.TrimAndExtendBuilder:
        ...
    def CreateCombineSheetsBuilder(self, combineSheets: Features.CombineSheets) -> Features.CombineSheetsBuilder:
        ...
    def Tag(self) -> Tag: ...



class TrimExtendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ArrowSideOption: Features.TrimExtendBuilder.ArrowSideOptions
    ExtendNewFace: bool
    ExtensionMethod: Features.TrimExtendBuilder.ExtensionMethods
    TargetCollector: ScCollector
    TargetExtendDistance: Expression
    TargetReversed: bool
    Tolerance: float
    ToolCollector: ScCollector
    ToolExtendDistance: Expression
    ToolReversed: bool
    Type: Features.TrimExtendBuilder.CreationTypes


    class ExtensionMethods(enum.Enum):
        NaturalCurvature = 0
        NaturalTangent = 1
        Mirrored = 2
    

    class CreationTypes(enum.Enum):
        ByDistance = 0
        PercentOfMeasured = 1
        UntilSelected = 2
        MakeCorner = 3
    

    class ArrowSideOptions(enum.Enum):
        Retain = 0
        Delete = 1
    

class TrimExtend(Features.BodyFeature):
    def __init__(self) -> None: ...
    def IsolateToolBodies(self) -> None:
        ...


class TrimCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CurveEndOption: Features.TrimCurveBuilder.CurveEndOptions
    CurveExtensionType: Features.TrimCurveBuilder.CurveExtensionTypes
    CurveList: SelectObjectList
    CurveOptions: GeometricUtilities.CurveOptions
    CurveTrimRegionOption: Features.TrimCurveBuilder.CurveTrimRegionOptions
    CurvesToTrim: Section
    FirstBoundingObject: SelectObjectList
    FirstBoundingObjectEndOption: Features.TrimCurveBuilder.FirstBoundingObjectEndOptions
    FirstBoundingObjectOption: Features.TrimCurveBuilder.FirstBoundingObjectOptions
    FirstBoundingObjectPickPoint: Point3d
    FirstBoundingPlane: Plane
    FirstReferenceIntersection: SelectPoint
    InteresectionDirectionOption: Features.TrimCurveBuilder.InteresectionDirectionOptions
    InteresectionMethod: Features.TrimCurveBuilder.InteresectionMethods
    InteresectionOptionVector: Direction
    ReverseTrimEnd: SelectObjectList
    SecondBoundingObject: SelectObjectList
    SecondBoundingObjectEndOption: Features.TrimCurveBuilder.SecondBoundingObjectEndOptions
    SecondBoundingObjectOption: Features.TrimCurveBuilder.SecondBoundingObjectOptions
    SecondBoundingObjectPickPoint: Point3d
    SecondBoundingPlane: Plane
    SecondReferenceIntersection: SelectPoint
    TrimBoundingObjects: bool


    class SecondBoundingObjectOptions(enum.Enum):
        SelectObject = 0
        SpecifyPlane = 1
    

    class SecondBoundingObjectEndOptions(enum.Enum):
        Start = 0
        End = 1
    

    class InteresectionMethods(enum.Enum):
        Inferred = 0
        UserDefined = 1
    

    class InteresectionDirectionOptions(enum.Enum):
        Shortest3dDistance = 0
        RelativeToWcs = 1
        AlongAVector = 2
        AlongScreenNormal = 3
    

    class FirstBoundingObjectOptions(enum.Enum):
        SelectObject = 0
        SpecifyPlane = 1
    

    class FirstBoundingObjectEndOptions(enum.Enum):
        Start = 0
        End = 1
    

    class CurveTrimRegionOptions(enum.Enum):
        Inside = 0
        Outside = 1
    

    class CurveExtensionTypes(enum.Enum):
        Natural = 0
        Linear = 1
        Circular = 2
        None = 3
    

    class CurveEndOptions(enum.Enum):
        Start = 0
        End = 1
    

class TrimCurve2Builder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SelectTrimRegion(self, helpPoint: Point3d) -> None:
        ...
    def DeselectTrimRegion(self, helpPoint: Point3d) -> None:
        ...
    def ResetTrimRegions(self) -> None:
        ...
    def SelectDivideLocation(self, helpPoint: Point3d) -> None:
        ...
    def DeselectDivideLocation(self, helpPoint: Point3d) -> None:
        ...
    def UpdateTrimRegionsAndDivideLocations(self) -> None:
        ...
    def CreateTrimCurveBoundingObjectBuilder(self) -> GeometricUtilities.TrimCurveBoundingObjectBuilder:
        ...
    BoundingObjectList: GeometricUtilities.TrimCurveBoundingObjectBuilderList
    CurveExtensionOption: Features.TrimCurve2Builder.CurveExtension
    CurveOptions: GeometricUtilities.CurveOptions
    CurveToTrim: Section
    DirectionOption: Features.TrimCurve2Builder.Direction
    KeepOrDiscard: Features.TrimCurve2Builder.KeepDiscard
    MakeInputCurvesDashed: bool
    OperationOption: Features.TrimCurve2Builder.Operation
    PerformExtendedIntersectionCalculation: bool
    ProcessBoundingObjects: bool
    Vector: Direction


    class Operation(enum.Enum):
        Trim = 0
        Divide = 1
    

    class KeepDiscard(enum.Enum):
        Keep = 0
        Discard = 1
    

    class Direction(enum.Enum):
        Shortest3DDistance = 0
        AlongDirection = 1
    

    class CurveExtension(enum.Enum):
        Natural = 0
        Linear = 1
        Circular = 2
        None = 3
    

class TrimCurve2(Features.CurveFeature):
    def __init__(self) -> None: ...


class TrimCurve(Features.CurveFeature):
    def __init__(self) -> None: ...


class TrimCornerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetReferencePoint(self) -> Point3d:
        ...
    def SetReferencePoint(self, referencePoint: Point3d) -> None:
        ...
    Curve1: SelectObject
    Curve2: SelectObject


class TrimBodyBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetTargets(self) -> typing.List[Body]:
        ...
    def SetTargets(self, target: typing.List[Body]) -> None:
        ...
    def AddTarget(self, target: Body) -> None:
        ...
    def RemoveTarget(self, target: Body) -> None:
        ...
    def Reverse(self) -> None:
        ...
    Tool: NXObject
    TrimDirection: Features.TrimBodyBuilder.DirectionType


    class DirectionType(enum.Enum):
        PositiveNormal = 1
        NegativeNormal = -1
        Invalid = 0
    

class TrimBody2Builder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BooleanTool: GeometricUtilities.BooleanToolBuilder
    TargetBodyCollector: ScCollector
    Tolerance: float


class TrimBody2(Features.BodyFeature):
    def __init__(self) -> None: ...


class TrimBody(Features.Feature):
    def __init__(self) -> None: ...


class TrimAndExtendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ArrowSideOption: Features.TrimAndExtendBuilder.ArrowSideType
    BodyOutputOption: Features.ExtendSheetBuilder.BodyOutput
    CombineOption: bool
    CopyOriginalOption: bool
    DistanceTolerance: float
    Operation: Features.TrimAndExtendBuilder.OperationType
    ReverseTarget: bool
    ReverseTool: bool
    SurfaceShapeOption: Features.ExtendSheetBuilder.SurfaceShape
    TargetSelection: ScCollector
    ToolSelection: ScCollector


    class OperationType(enum.Enum):
        UntilSelected = 0
        MakeCorner = 1
    

    class ArrowSideType(enum.Enum):
        Retain = 0
        Delete = 1
    

class TrimAndExtend(Features.BodyFeature):
    def __init__(self) -> None: ...
    def IsolateToolBodies(self) -> None:
        ...


class TrackingData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetIntApplicationKey(self, applicationKey: int) -> None:
        ...
    def SetNXOpenObjectApplicationKey(self, applicationKey: NXObject) -> None:
        ...
    def AddTagSourceEntities(self, sourceEntities: typing.List[NXObject]) -> None:
        ...
    def AddIntSourceEntity(self, sourceEntity: int) -> None:
        ...
    def AddTagIntPairSourceEntity(self, tagSourceEntity: NXObject, intSourceEntity: int) -> None:
        ...


class ToolingFeatureCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def CreateToolingBoxBuilder(self, toolingBox: Features.ToolingBox) -> Features.ToolingBoxBuilder:
        ...
    def CreateOffsetFacetBodyBuilder(self, offsetfacetBody: Features.OffsetFacetBody) -> Features.OffsetFacetBodyBuilder:
        ...
    def Tag(self) -> Tag: ...



class ToolingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def CreateUniversalUnformBuilder(self, universalUnform: Features.UniversalUnform) -> Tooling.UniversalUnformBuilder:
        ...
    def CreatePrebendBuilder(self, prebend: Features.Prebend) -> Tooling.PrebendBuilder:
        ...
    def ToolingFindObject(self, journalIdentifier: str) -> Features.Feature:
        ...
    def Tag(self) -> Tag: ...



class ToolingBoxBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetBoxMatrixAndPosition(self, matrix: Matrix3x3, position: Point3d) -> None:
        ...
    def SetSelectedOccurrences(self, selections: typing.List[NXObject], deselections: typing.List[NXObject]) -> None:
        ...
    def CalculateBoxSize(self) -> None:
        ...
    AxisPoint: Point
    AxisVector: Direction
    BoundedObject: ScCollector
    BoxColor: NXColor
    BoxPosition: Point3d
    Clearance: Expression
    CsysAssociative: bool
    CsysSelection: SelectCoordinateSystem
    FacetBodies: SelectNXObjectList
    NonAlignedMinimumBox: bool
    OffsetNegativeX: Expression
    OffsetNegativeY: Expression
    OffsetNegativeZ: Expression
    OffsetPositiveX: Expression
    OffsetPositiveY: Expression
    OffsetPositiveZ: Expression
    PositionPrecisionValue: float
    PrecisionValue: float
    RadialOffset: Expression
    ReferenceCsysType: Features.ToolingBoxBuilder.RefCsysType
    ShowDimension: bool
    SingleOffset: bool
    Type: Features.ToolingBoxBuilder.Types
    XValue: Expression
    YValue: Expression
    ZValue: Expression


    class Types(enum.Enum):
        CenterAndLengths = 0
        BoundedBlock = 1
        BoundedCylinder = 2
    

    class RefCsysType(enum.Enum):
        Wcs = 0
        AbsoluteinDisplayedPart = 1
        SelectedCsys = 2
    

class ToolingBox(Features.BodyFeature):
    def __init__(self) -> None: ...


class ThroughCurvesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Alignment: GeometricUtilities.AlignmentMethodBuilder
    BodyPreference: Features.ThroughCurvesBuilder.BodyPreferenceTypes
    ClosedInV: bool
    Construction: Features.ThroughCurvesBuilder.ConstructionMethod
    CurvatureTolerance: float
    FirstSectionContinuity: GeometricUtilities.Continuity
    FlowDirection: GeometricUtilities.FlowDirection
    LastSectionContinuity: GeometricUtilities.Continuity
    LoftingSurfaceRebuildData: GeometricUtilities.Rebuild
    NormalToEndSections: bool
    PatchType: Features.ThroughCurvesBuilder.PatchTypes
    PositionTolerance: float
    PreserveShape: bool
    SectionSurfaceRebuildData: GeometricUtilities.Rebuild
    SectionTemplateString: Section
    SectionsList: SectionList
    TangentTolerance: float


    class PatchTypes(enum.Enum):
        Single = 0
        Multiple = 1
        MatchString = 2
    

    class ConstructionMethod(enum.Enum):
        Normal = 0
        SplinePoints = 1
        Simple = 2
    

    class BodyPreferenceTypes(enum.Enum):
        Solid = 0
        Sheet = 1
    

class ThroughCurves(Features.BodyFeature):
    def __init__(self) -> None: ...


class ThroughCurveMeshBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BodyPreference: Features.ThroughCurveMeshBuilder.BodyPreferenceTypes
    Construction: Features.ThroughCurveMeshBuilder.ConstructionMethod
    CrossCurvesList: SectionList
    CrossSurfaceRebuildData: GeometricUtilities.Rebuild
    CrossTemplateString: Section
    CurvatureTolerance: float
    Emphasis: Features.ThroughCurveMeshBuilder.EmphasisType
    FirstCrossContinuity: GeometricUtilities.Continuity
    FirstPrimaryContinuity: GeometricUtilities.Continuity
    IntersectionTolerance: float
    LastCrossContinuity: GeometricUtilities.Continuity
    LastPrimaryContinuity: GeometricUtilities.Continuity
    PositionTolerance: float
    PrimaryCurvesList: SectionList
    PrimarySurfaceRebuildData: GeometricUtilities.Rebuild
    PrimaryTemplateString: Section
    Spine: Section
    TangentTolerance: float


    class EmphasisType(enum.Enum):
        Both = 0
        Primary = 1
        Cross = 2
    

    class ConstructionMethod(enum.Enum):
        Normal = 0
        SplinePoints = 1
        Simple = 2
    

    class BodyPreferenceTypes(enum.Enum):
        Solid = 0
        Sheet = 1
    

class ThroughCurveMesh(Features.BodyFeature):
    def __init__(self) -> None: ...


class ThreeBendCorner(Features.Feature):
    def __init__(self) -> None: ...


class ThickenBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ApproximateOffset: bool
    BooleanOperation: GeometricUtilities.BooleanOperation
    FaceCollector: ScCollector
    FirstOffset: Expression
    RegionSectionList: GeometricUtilities.TwoExpressionsSectionSetList
    RegionToPierce: Section
    RemoveGashes: bool
    ReverseDirection: bool
    SecondOffset: Expression
    Tolerance: float


class Thicken(Features.BodyFeature):
    def __init__(self) -> None: ...


class TextBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SelectFont(self, fontName: str, script: Features.TextBuilder.ScriptOptions) -> None:
        ...
    def UpdateOnSectionPlane(self) -> None:
        ...
    def UpdateOnOrientationVectorReversal(self) -> None:
        ...
    CanCreateBoundingBox: bool
    CanJoinCurves: bool
    CanProjectCurves: bool
    CanReferenceText: bool
    CanReverseIntersectionCurve: bool
    CanUseKerningSpaces: bool
    Font: str
    FontStyle: Features.TextBuilder.FontStyleOptions
    FrameOnPath: GeometricUtilities.FrameOnPathBuilder
    IsAssociative: bool
    IsPrintMark: bool
    OnCurvePlacementProfile: Section
    OnFacePlacementMethod: Features.TextBuilder.OnFacePlacementMethodOptions
    OnFacePlacementProfile: Section
    OrientationMethod: Features.TextBuilder.OrientationMethodOptions
    OrientationVector: Direction
    PlacementFaces: ScCollector
    PlanarFrame: GeometricUtilities.RectangularFrameBuilder
    PrintMarkThickness: Expression
    PrintMarkUsageLabel: str
    Script: Features.TextBuilder.ScriptOptions
    SectionPlane: Plane
    Text: Expression
    TextString: str
    Type: Features.TextBuilder.Types


    class Types(enum.Enum):
        Planar = 0
        OnCurve = 1
        OnFace = 2
    

    class ScriptOptions(enum.Enum):
        Other = 0
        Western = 1
        Baltic = 2
        ChineseBig5 = 3
        CentralEuropean = 4
        Gb2312 = 5
        Greek = 6
        Hangul = 7
        Mac = 8
        Oem = 9
        Cyrillic = 10
        ShiftJIS = 11
        Symbol = 12
        Turkish = 13
        Vietnamese = 14
        Johab = 15
        Arabic = 16
        Hebrew = 17
        Thai = 18
    

    class OrientationMethodOptions(enum.Enum):
        Natural = 0
        Vector = 1
    

    class OnFacePlacementMethodOptions(enum.Enum):
        CurvesOnFaces = 0
        SectionPlane = 1
    

    class FontStyleOptions(enum.Enum):
        Regular = 0
        Italic = 1
        Bold = 2
        BoldItalic = 3
    

class Text(Features.Feature):
    def __init__(self) -> None: ...


class TangentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FaceChangeOverflowBehavior: GeometricUtilities.FaceChangeOverflowBehavior
    MotionFace: SelectFace
    MoveAlongFace: Features.FaceRecognitionBuilder
    StationaryFace: SelectISurface
    ThroughPoint: Point


class Tangent(Features.BodyFeature):
    def __init__(self) -> None: ...


class TabNoteCfgBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BlockOffset: float
    DeletePreviousDiagrams: bool
    InsertionPoint: Point
    NumberOfRows: int
    ReferencePlane: Features.TabNoteCfgBuilder.Refplane


    class Refplane(enum.Enum):
        Xy = 0
        Yz = 1
        Zx = 2
        NegXy = 3
        NegYz = 4
        NegZx = 5
    

class Tab(Features.Feature):
    def __init__(self) -> None: ...


class SynchronousEdgeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def CreateMoveEdgeBuilder(self, moveEdge: Features.MoveEdge) -> Features.MoveEdgeBuilder:
        ...
    def CreateOffsetEdgeBuilder(self, offsetEdge: Features.OffsetEdge) -> Features.OffsetEdgeBuilder:
        ...
    def Tag(self) -> Tag: ...



class SynchronousCurveCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def CreateMoveCurveBuilder(self, moveCurve: Features.MoveCurve) -> Features.MoveCurveBuilder:
        ...
    def CreateDeleteCurveBuilder(self, deleteCurve: Features.DeleteCurve) -> Features.DeleteCurveBuilder:
        ...
    def CreateOffsetMoveCurveBuilder(self, offsetMoveCurve: Features.OffsetMoveCurve) -> Features.OffsetMoveCurveBuilder:
        ...
    def CreateLocalScaleCurveBuilder(self, scaleCurve: Features.LocalScaleCurve) -> Features.LocalScaleCurveBuilder:
        ...
    def CreateResizeCurveBuilder(self, resizeCurve: Features.ResizeCurve) -> Features.ResizeCurveBuilder:
        ...
    def CreateResizeChamferCurveBuilder(self, resizeChamferCurve: Features.ResizeChamferCurve) -> Features.ResizeChamferCurveBuilder:
        ...
    def Tag(self) -> Tag: ...



class SymmetricBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ExistingSymmetryPlane: SelectISurface
    MotionFace: SelectFace
    MoveAlongFace: Features.FaceRecognitionBuilder
    NewSymmetryPlane: Plane
    StationaryFace: SelectFace
    SymmetryPlaneOption: Features.SymmetricBuilder.PlaneOptions


    class PlaneOptions(enum.Enum):
        Existing = 0
        New = 1
    

class Symmetric(Features.BodyFeature):
    def __init__(self) -> None: ...


class SweptVolumeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BooleanData: GeometricUtilities.BooleanOperation
    DistanceTolerance: float
    ForcedDirection: Direction
    ReferencePoint: Point
    SweepOrientation: Features.SweptVolumeBuilder.SweepOrient
    ToolBody: ScCollector
    ToolPath: Section


    class SweepOrient(enum.Enum):
        ParallelToBody = 0
        NormalToPath = 1
    

class SweptVolume(Features.BodyFeature):
    def __init__(self) -> None: ...


class SweptBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AlignmentMethod: GeometricUtilities.AlignmentMethodBuilder
    BodyPreference: GeometricUtilities.FeatureOptions
    G0Tolerance: float
    G1Tolerance: float
    GuideList: SectionList
    GuideRebuildData: GeometricUtilities.Rebuild
    InterpolationOption: Features.SweptBuilder.InterpolationOptions
    OrientationMethod: GeometricUtilities.OrientationMethodBuilder
    PreserveGuideShapeOption: bool
    PreserveShapeOption: bool
    ScalingMethod: GeometricUtilities.ScalingMethodBuilder
    SectionList: SectionList
    SectionLocation: Features.SweptBuilder.SectionLocationTypes
    SectionRebuildData: GeometricUtilities.Rebuild
    Spine: Section


    class SectionLocationTypes(enum.Enum):
        AnywhereAlongGuides = 0
        EndsOfGuides = 1
    

    class InterpolationOptions(enum.Enum):
        Linear = 0
        Cubic = 1
        Blend = 2
    

class Swept(Features.BodyFeature):
    def __init__(self) -> None: ...


class SweepFeatureCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def CreateSweptVolumeBuilder(self, sweptVolume: Features.SweptVolume) -> Features.SweptVolumeBuilder:
        ...
    def Tag(self) -> Tag: ...



class SweepAlongGuideBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BooleanOperation: GeometricUtilities.BooleanOperation
    ChainingTolerance: float
    DistanceTolerance: float
    FeatureOptions: GeometricUtilities.FeatureOptions
    FirstOffset: Expression
    Guide: Section
    SecondOffset: Expression
    Section: Section


class SweepAlongGuide(Features.BodyFeature):
    def __init__(self) -> None: ...




class StyledSweepBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreatePivotSet(self, value1: float, value2: float, path1: Curve, path2: Curve) -> GeometricUtilities.StyledSweepDoubleOnPathDimBuilder:
        ...
    def CreateRotationSet(self, value: float, pathPar: float, path: Curve) -> GeometricUtilities.RotationSetBuilder:
        ...
    def CreateScalingSet(self, valuePar: float, depthPar: float, pathPar: float, path: Curve) -> GeometricUtilities.ScalingSetBuilder:
        ...
    def StartInsertingSection(self, insertPnt: float) -> None:
        ...
    def EndInsertingSection(self) -> None:
        ...
    AlternateSolution: int
    FirstGuide: Section
    FixedStringOption: Features.StyledSweepBuilder.FixedStringOptions
    G0Tolerance: float
    G1Tolerance: float
    GuideRebuildData: GeometricUtilities.Rebuild
    InsertedSectionList: SectionList
    PivotSetList: GeometricUtilities.StyledSweepDoubleOnPathDimBuilderList
    ReferenceMethod: GeometricUtilities.StyledSweepReferenceMethodBuilder
    RotationSetList: GeometricUtilities.RotationSetBuilderList
    ScalingCurve: Section
    ScalingMethodOption: Features.StyledSweepBuilder.ScalingMethodOptions
    ScalingSetList: GeometricUtilities.ScalingSetBuilderList
    SecondGuide: Section
    SectionList: SectionList
    SectionOrientationOption: Features.StyledSweepBuilder.SectionOrientationOptions
    SectionRebuildData: GeometricUtilities.Rebuild
    SurfaceRange: GeometricUtilities.SurfaceRangeBuilder
    TransitionOption: Features.StyledSweepBuilder.TransitionOptions
    Type: Features.StyledSweepBuilder.Types


    class Types(enum.Enum):
        OneGuide = 0
        OneGuideOneTouch = 1
        OneGuideOneOrientation = 2
        TwoGuides = 3
    

    class TransitionOptions(enum.Enum):
        Linear = 0
        Cubic = 1
        Blend = 2
    

    class SectionOrientationOptions(enum.Enum):
        Translate = 0
        KeepAngle = 1
        MakeNormal = 2
        UserDefined = 3
        ArcLength = 4
    

    class ScalingMethodOptions(enum.Enum):
        Uniform = 0
        Nonuniform = 1
        ScalingCurve = 2
    

    class FixedStringOptions(enum.Enum):
        Guide = 0
        Section = 1
        GuideAndSection = 2
    

class StyledSweep(Features.BodyFeature):
    def __init__(self) -> None: ...


class StyledCornerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def UpdateOnPathDimPath(self, curveControlOption: Features.StyledCornerBuilder.CurveControlTypes, startEndIndex: int) -> None:
        ...
    def ResetToTriangularCorner(self) -> None:
        ...
    def SetNumCornerSides(self, numSides: int) -> None:
        ...
    def UpdateCornerData(self, inputFaceChanged: bool, resetToTriangleCorner: bool) -> None:
        ...
    BaseCurveRebuildData: GeometricUtilities.Rebuild
    BaseFaces: ScCollector
    BottomBridgeCurveContinuity: GeometricUtilities.Continuity
    BottomShapeControlMethods: Features.StyledCornerBuilder.ShapeControlMethodsTypes
    BottomTangentMagnitude: GeometricUtilities.TangentMagnitudeBuilder
    ChangeAllBoundaryConstraints: bool
    CurveControl: Features.StyledCornerBuilder.CurveControlTypes
    G0Tolerance: float
    G1Tolerance: float
    G2Tolerance: float
    InputBlend1: ScCollector
    InputBlend2: ScCollector
    InputBlend3: ScCollector
    InputChanged: bool
    InteriorCurveType: Features.StyledCornerBuilder.InteriorCurveTypes
    IsoUCurveEndPoint: GeometricUtilities.OnPathDimensionBuilder
    IsoUCurveStartPoint: GeometricUtilities.OnPathDimensionBuilder
    IsoUDepthSkew: GeometricUtilities.DepthSkewBuilder
    IsoUShapeControlMethods: Features.StyledCornerBuilder.ShapeControlMethodsTypes
    IsoUTangentMagnitude: GeometricUtilities.TangentMagnitudeBuilder
    IsoVCurveEndPoint: GeometricUtilities.OnPathDimensionBuilder
    IsoVCurveStartPoint: GeometricUtilities.OnPathDimensionBuilder
    IsoVDepthSkew: GeometricUtilities.DepthSkewBuilder
    IsoVShapeControlMethods: Features.StyledCornerBuilder.ShapeControlMethodsTypes
    IsoVTangentMagnitude: GeometricUtilities.TangentMagnitudeBuilder
    TopBaseCurveContinuity: GeometricUtilities.Continuity
    TopCurveEndPoint: GeometricUtilities.OnPathDimensionBuilder
    TopCurveStartPoint: GeometricUtilities.OnPathDimensionBuilder
    TopDepthSkew: GeometricUtilities.DepthSkewBuilder
    TopShapeControlMethods: Features.StyledCornerBuilder.ShapeControlMethodsTypes
    TopTangentMagnitude: GeometricUtilities.TangentMagnitudeBuilder
    TrimAndSewMethod: Features.StyledCornerBuilder.TrimAndSewMethodTypes
    TrimCurve1Continuity: GeometricUtilities.Continuity
    TrimCurve1Type: Features.StyledCornerBuilder.TrimCurveTypes
    TrimCurve2Continuity: GeometricUtilities.Continuity
    TrimCurve2Type: Features.StyledCornerBuilder.TrimCurveTypes
    TrimCurveRebuildData: GeometricUtilities.Rebuild


    class TrimCurveTypes(enum.Enum):
        TangentContinuous = 0
        LineProjection = 1
        Isoparametric = 2
    

    class TrimAndSewMethodTypes(enum.Enum):
        NoTrim = 0
        TrimBlends = 1
        TrimAll = 2
        TrimAndAttachBlends = 3
        TrimAndAttachAll = 4
    

    class ShapeControlMethodsTypes(enum.Enum):
        None = 0
        DepthAndSkew = 1
        TangentMagnitude = 2
        TemplateBridgeCurve = 3
    

    class InteriorCurveTypes(enum.Enum):
        None = 0
        IsoCurveU = 1
        IsoCurveV = 2
        IsoCurveUV = 3
    

    class CurveControlTypes(enum.Enum):
        TopBaseCurve = 0
        BottomBridgeCurve = 1
        IsoCurveU = 2
        IsoCurveV = 3
    

class StyledCorner(Features.BodyFeature):
    def __init__(self) -> None: ...
    def IsolateToolBodies(self) -> None:
        ...


class StyledBlendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ReverseBlend(self) -> None:
        ...
    def UpdateRadiusLawSpine(self) -> None:
        ...
    def UpdateShapeLawSpine(self, isDefaultSpine: bool) -> None:
        ...
    def ProcessInheritFeatureParameters(self, feature: Features.StyledBlend) -> None:
        ...
    def UpdateWall1(self) -> bool:
        ...
    def UpdateWall2(self) -> bool:
        ...
    def UpdateTangentCurve1(self) -> None:
        ...
    def UpdateTangentCurve2(self) -> None:
        ...
    def UpdateSpineCurve(self) -> None:
        ...
    def UpdateCenterCurve(self) -> None:
        ...
    def UpdateProfileCurve(self) -> None:
        ...
    def UpdateResetData(self) -> None:
        ...
    AdjacentBlend1: SelectEdge
    AdjacentBlend1TrimEnd: GeometricUtilities.OnPathDimensionBuilder
    AdjacentBlend1TrimStart: GeometricUtilities.OnPathDimensionBuilder
    AdjacentBlend2: SelectEdge
    AdjacentBlend2TrimEnd: GeometricUtilities.OnPathDimensionBuilder
    AdjacentBlend2TrimStart: GeometricUtilities.OnPathDimensionBuilder
    Blend1Continuity: GeometricUtilities.Continuity
    Blend2Continuity: GeometricUtilities.Continuity
    CenterCurve: Section
    CenterCurveEnd: GeometricUtilities.OnPathDimensionBuilder
    CenterCurveStart: GeometricUtilities.OnPathDimensionBuilder
    DepthLaw: GeometricUtilities.LawBuilder
    InheritFeatureParameters: Features.SelectFeature
    IsBlendExtended: bool
    IsCenterCurveDirectionReversed: bool
    IsCenterCurveUsedAsSpine: bool
    IsNormal1Reversed: bool
    IsNormal2Reversed: bool
    IsSingleTubeUsed: bool
    LinkHandles: bool
    PositionTolerance: float
    ProfileCurve: Section
    RadiusConstraintType: Features.StyledBlendBuilder.StyledBlendRadiusConstraintType
    RadiusConstraintValue: Expression
    RebuildGuide: GeometricUtilities.Rebuild
    ShapeControl: Features.StyledBlendBuilder.StyledBlendShapeControlType
    SkewLaw: GeometricUtilities.LawBuilder
    SpineCurve: Section
    TangentCurve1: Section
    TangentCurve2: Section
    TangentMagnitude1: GeometricUtilities.LawBuilder
    TangentMagnitude2: GeometricUtilities.LawBuilder
    TangentTolerance: float
    TrimMethod: Features.StyledBlendBuilder.StyledBlendTrimMethodType
    TubeRadius1: GeometricUtilities.LawBuilder
    TubeRadius2: GeometricUtilities.LawBuilder
    Type: Features.StyledBlendBuilder.Types
    Wall1: ScCollector
    Wall1Continuity: GeometricUtilities.Continuity
    Wall1Direction: GeometricUtilities.FlowDirection
    Wall2: ScCollector
    Wall2Continuity: GeometricUtilities.Continuity
    Wall2Direction: GeometricUtilities.FlowDirection


    class Types(enum.Enum):
        Law = 0
        Curve = 1
        Profile = 2
    

    class StyledBlendTrimMethodType(enum.Enum):
        NoTrim = 0
        TrimAndAttach = 1
        TrimInputWalls = 2
        TrimInputBlends = 3
    

    class StyledBlendShapeControlType(enum.Enum):
        TangentCurve1 = 0
        TangentCurve2 = 1
        Depth = 2
        Skew = 3
        TangentMagnitude = 4
    

    class StyledBlendRadiusConstraintType(enum.Enum):
        None = 0
        Peak = 1
        Minimum = 2
    

class StyledBlend(Features.BodyFeature):
    def __init__(self) -> None: ...
    def IsolateToolBodies(self) -> None:
        ...


class StudioXformBuilderEx(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ProportionalReset(self) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx.FallOffReset instead.")"""
        ...
    def FallOffReset(self) -> None:
        ...
    def InsertKnots(self) -> None:
        ...
    def RestoreParentFace(self) -> None:
        ...
    def ConvertParameters(self, xformObject: NXObject) -> None:
        ...
    def ChangeDegree(self, xformObject: NXObject) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx.ChangeDegreeWithParameters instead.")"""
        ...
    def ChangeDegreeWithParameters(self, xformObject: NXObject, uDegree: int, vDegree: int, uPatch: int, vPatch: int) -> None:
        ...
    def InsertKnot(self, xformObject: NXObject) -> None:
        ...
    def ChangeFlexibility(self, xformObject: NXObject) -> None:
        ...
    def UpdateLockRegionGeometry(self, xformObject: NXObject) -> None:
        ...
    def InsertPole(self, xformObject: NXObject, poleIndex: int, insertType: Features.StudioXformBuilderEx.InsertPoleType, direction: Features.StudioXformBuilderEx.SurfaceDirectionType, location: float) -> None:
        ...
    def RemovePole(self, xformObject: NXObject, poleIndex: int, direction: Features.StudioXformBuilderEx.SurfaceDirectionType) -> None:
        ...
    def SetPoleEditType(self, xformObject: NXObject, index: int, poleEditType: Features.StudioXformBuilderEx.PoleEditType) -> None:
        ...
    def RebaseOriginalGeometry(self, xformObject: NXObject) -> None:
        ...
    def LockRegionNextObject(self) -> None:
        ...
    def EndLockRegion(self, xformObject: NXObject) -> None:
        ...
    AdvancedMethod: Features.StudioXformBuilderEx.AdvancedMethodType
    AdvancedMethodOption: Features.StudioXformBuilderEx.AdvancedMethodOptionType
    CanUseFaceFinder: bool
    ContinuityUMax: GeometricUtilities.Continuity
    ContinuityUMin: GeometricUtilities.Continuity
    ContinuityVMax: GeometricUtilities.Continuity
    ContinuityVMin: GeometricUtilities.Continuity
    ControlPoleManager: GeometricUtilities.ControlPoleManagerData
    CurveRange: GeometricUtilities.CurveRangeBuilder
    DegreesAndSegmentsOrPatches: GeometricUtilities.DegreesAndSegmentsOrPatchesBuilder
    ExtractMethod: Features.StudioXformBuilderEx.ExtrationMethodType
    ExtractTolerance: float
    FaceFinder: Features.FaceRecognitionBuilder
    FallOffScale: float
    FeatureSaveMethod: Features.StudioXformBuilderEx.FeatureType
    InsertKnotDirection: Features.StudioXformBuilderEx.InsertKnotDirectionType
    InsertKnotParameter: int
    IsSingleSelection: bool
    KeepAllContinuity: bool
    LockPoles: bool
    LockRegionUEndFlexibility: int
    LockRegionUStartFlexibility: int
    LockRegionVEndFlexibility: int
    LockRegionVStartFlexibility: int
    MovementArbitraryPlane: Plane
    MovementArbitraryVector: Direction
    MovementMethod: Features.StudioXformBuilderEx.MovementMethodType
    PlanarizeArbitraryPlane: Plane
    PlanarizeDirection: Features.StudioXformBuilderEx.PlanarizeDirectionType
    PlanarizeMethod: Features.StudioXformBuilderEx.PlanarizeMethodType
    PlanarizeProjectionPlane: Features.StudioXformBuilderEx.PlanarizeProjectionPlaneType
    PrincipalMovementDirection: Features.StudioXformBuilderEx.PrincipalMovementDirectionType
    PrincipalRotatingAxis: Features.StudioXformBuilderEx.PrincipalRotatingAxisType
    PrincipalScalingDirection: Features.StudioXformBuilderEx.PrincipalScalingDirectionType
    ProportionalAllU: bool
    ProportionalAllV: bool
    ProportionalFallOffScale: float
    ProportionalMoveAfterU: int
    ProportionalMoveAfterV: int
    ProportionalMoveBeforeU: int
    ProportionalMoveBeforeV: int
    ProportionalPoleControlOption: Features.StudioXformBuilderEx.ProportionalPoleControlType
    RotatingArbitraryPlane: Plane
    RotatingArbitraryVector: Direction
    RotatingAxis: Features.StudioXformBuilderEx.RotatingAxisType
    RotatingPivot: Features.StudioXformBuilderEx.RotatingPivotType
    RotatingPivotPoint: Point
    ScalingArbitraryPlane: Plane
    ScalingArbitraryVector: Direction
    ScalingCenter: Features.StudioXformBuilderEx.ScalingCenterType
    ScalingCenterPoint: Point
    ScalingDirection: Features.StudioXformBuilderEx.ScalingDirectionType
    SurfaceRange: GeometricUtilities.SurfaceRangeBuilder
    Type: Features.StudioXformBuilderEx.Types
    XformOX: GeometricUtilities.OrientXpressBuilder
    XformObjects: SelectNXObjectList


    class Types(enum.Enum):
        Translate = 0
        Rotate = 1
        Scale = 2
        Planarize = 3
    

    class SurfaceDirectionType(enum.Enum):
        U = 0
        V = 1
    

    class ScalingDirectionType(enum.Enum):
        WCS = 0
        View = 1
        Vector = 2
        Plane = 3
        PlaneofCurve = 4
    

    class ScalingCenterType(enum.Enum):
        Scaleaboutobjectcenter = 0
        Scaleaboutselected = 1
        Scaleaboutpoint = 2
    

    class RotatingPivotType(enum.Enum):
        Rotateaboutobjectcenter = 0
        Rotateaboutselected = 1
        Rotateaboutpoint = 2
    

    class RotatingAxisType(enum.Enum):
        WCS = 0
        View = 1
        Vector = 2
        Plane = 3
    

    class ProportionalPoleControlType(enum.Enum):
        All = 0
        Selected = 1
        ByUV = 2
    

    class PrincipalScalingDirectionType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        YZ = 3
        XZ = 4
        XY = 5
    

    class PrincipalRotatingAxisType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class PrincipalMovementDirectionType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        YZ = 3
        XZ = 4
        XY = 5
        XYZ = 6
    

    class PoleEditType(enum.Enum):
        None = 0
        Constrained = 1
        Free = 2
    

    class PlanarizeProjectionPlaneType(enum.Enum):
        YZ = 0
        XZ = 1
        XY = 2
        Plane = 3
    

    class PlanarizeMethodType(enum.Enum):
        AtPlaneLocation = 0
        AtPoleLocation = 1
        OnaBestFitPlane = 2
    

    class PlanarizeDirectionType(enum.Enum):
        U = 0
        V = 1
    

    class MovementMethodType(enum.Enum):
        WCS = 0
        View = 1
        Vector = 2
        Plane = 3
        Normal = 4
        Polygon = 5
    

    class InsertPoleType(enum.Enum):
        Next = 0
        Previous = 1
    

    class InsertKnotDirectionType(enum.Enum):
        UDirection = 0
        VDirection = 1
    

    class FeatureType(enum.Enum):
        Relative = 0
        Absolute = 1
    

    class ExtrationMethodType(enum.Enum):
        Original = 0
        MinimumBounded = 1
        FittoBoundary = 2
    

    class AdvancedMethodType(enum.Enum):
        ProportionalMovement = 0
        Falloff = 1
        KeepContinuity = 2
        LockRegion = 3
        InsertKnot = 4
        AdvanceOff = 5
    

    class AdvancedMethodOptionType(enum.Enum):
        Proportional = 0
        LockRegion = 1
        InsertKnot = 2
        AdvancedOff = 3
    

class StudioXformBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def FallOffReset(self) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx instead..")"""
        ...
    def ProportionalReset(self) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx instead..")"""
        ...
    def InsertKnots(self) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx instead..")"""
        ...
    def ShapeReset(self) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx instead..")"""
        ...
    def UpdateXformObject(self, xformObject: NXObject) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx instead..")"""
        ...
    def ConvertParameters(self, xformObject: NXObject) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx instead..")"""
        ...
    def ChangeDegree(self, xformObject: NXObject) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx instead..")"""
        ...
    def InsertKnot(self, xformObject: NXObject) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx instead..")"""
        ...
    def ChangeFlexibility(self, xformObject: NXObject) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx instead..")"""
        ...
    def UpdateLockRegionGeometry(self, xformObject: NXObject) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.StudioXformBuilderEx instead..")"""
        ...
    AdvancedMethod: Features.StudioXformBuilder.AdvancedMethodType
    CenterPoint: Point
    ContinuityUMax: GeometricUtilities.Continuity
    ContinuityUMin: GeometricUtilities.Continuity
    ContinuityVMax: GeometricUtilities.Continuity
    ContinuityVMin: GeometricUtilities.Continuity
    ControlPoleManager: GeometricUtilities.ControlPoleManagerData
    CurveRange: GeometricUtilities.CurveRangeBuilder
    DegreesAndSegmentsOrPatches: GeometricUtilities.DegreesAndSegmentsOrPatchesBuilder
    FallOffScale: float
    FeatureSaveMethod: Features.StudioXformBuilder.FeatureType
    InsertKnotDirection: Features.StudioXformBuilder.InsertKnotDirectionType
    InsertKnotParameter: int
    IsSingleSelection: bool
    KeepAllContinuity: bool
    LockRegionUEndFlexibility: int
    LockRegionUStartFlexibility: int
    LockRegionVEndFlexibility: int
    LockRegionVStartFlexibility: int
    PivotPoint: Point
    PlanarizeArbitraryPlane: Plane
    PlanarizeDirection: Features.StudioXformBuilder.PlanarizeDirectionType
    PlanarizeMethod: Features.StudioXformBuilder.PlanarizeMethodType
    PlanarizePlaneOption: Features.StudioXformBuilder.PlanarizePlaneOptionType
    ProportionalAllU: bool
    ProportionalAllV: bool
    ProportionalFallOffScale: float
    ProportionalMoveAfterU: int
    ProportionalMoveAfterV: int
    ProportionalMoveBeforeU: int
    ProportionalMoveBeforeV: int
    RotatingPivot: Features.StudioXformBuilder.RotatingPivotType
    RotationArbitraryPlane: Plane
    RotationArbitraryVector: Direction
    RotationDirection: Features.StudioXformBuilder.RotationDirectionType
    ScalingArbitraryPlane: Plane
    ScalingArbitraryVector: Direction
    ScalingCenter: Features.StudioXformBuilder.ScalingCenterType
    ScalingDirection: Features.StudioXformBuilder.ScalingDirectionType
    SurfaceRange: GeometricUtilities.SurfaceRangeBuilder
    TranslationArbitraryPlane: Plane
    TranslationArbitraryVector: Direction
    TranslationDirection: Features.StudioXformBuilder.TranslationDirectionType
    Type: Features.StudioXformBuilder.Types
    XformObjects: SelectNXObjectList


    class Types(enum.Enum):
        Translate = 0
        Rotate = 1
        Scale = 2
        TranslateNormalToFaceOrCurve = 3
        TranlsateAlongControlPolygon = 4
        PlanarizeRowOfPoles = 5
    

    class TranslationDirectionType(enum.Enum):
        Xc = 0
        Yc = 1
        Zc = 2
        YcZc = 3
        XcZc = 4
        XcYc = 5
        ArbitraryDirection = 6
        ArbitraryPlane = 7
    

    class ScalingDirectionType(enum.Enum):
        ScaleUniformly = 0
        PlaneOfCurve = 1
        Xc = 2
        Yc = 3
        Zc = 4
        YcZc = 5
        XcZc = 6
        XcYc = 7
        ArbitraryDirection = 8
        ArbitraryPlane = 9
    

    class ScalingCenterType(enum.Enum):
        AboutObjectCenter = 0
        AboutSelectedObject = 1
        AboutPoint = 2
    

    class RotationDirectionType(enum.Enum):
        Xc = 0
        Yc = 1
        Zc = 2
        ArbitraryDirection = 3
        ArbitraryPlane = 4
    

    class RotatingPivotType(enum.Enum):
        AboutObjectCenter = 0
        AboutSelectedObject = 1
        AboutPoint = 2
    

    class PlanarizePlaneOptionType(enum.Enum):
        YcZc = 0
        XcZc = 1
        XcYc = 2
        ArbitraryPlane = 3
    

    class PlanarizeMethodType(enum.Enum):
        AtPlaneLocation = 0
        AtPoleLocation = 1
        OnABestFitPlane = 2
    

    class PlanarizeDirectionType(enum.Enum):
        U = 0
        V = 1
    

    class InsertKnotDirectionType(enum.Enum):
        UDirection = 0
        VDirection = 1
    

    class FeatureType(enum.Enum):
        Relative = 0
        Absolute = 1
    

    class AdvancedMethodType(enum.Enum):
        ChangeDegree = 0
        Falloff = 1
        ProportionalMovement = 2
        KeepContinuity = 3
        LockRegion = 4
        InsertKnot = 5
        AdvanceOff = 6
    

class StudioXform(Features.BodyFeature):
    def __init__(self) -> None: ...


class StudioSurfaceEx(Features.BodyFeature):
    def __init__(self) -> None: ...


class StudioSurfaceBuilderEx(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AlignmentMethod: GeometricUtilities.AlignmentMethodBuilder
    BodyPreference: GeometricUtilities.FeatureOptions
    CurvatureTolerance: float
    FirstGuideContinuity: GeometricUtilities.Continuity
    FirstSectionContinuity: GeometricUtilities.Continuity
    FlowDirection: GeometricUtilities.FlowDirection
    GuideCurveFitData: GeometricUtilities.CurveFitData
    GuideList: SectionList
    IntersectionTolerance: float
    LastGuideContinuity: GeometricUtilities.Continuity
    LastSectionContinuity: GeometricUtilities.Continuity
    LaydownCurve: bool
    PositionTolerance: float
    SectionCurveFitData: GeometricUtilities.CurveFitData
    SectionList: SectionList
    SplitSurfaces: bool
    TangentTolerance: float
    Transition: Features.StudioSurfaceBuilderEx.TransitionOptions


    class TransitionOptions(enum.Enum):
        NormalToEndSections = 0
        NormalToAllSections = 1
        Cubic = 2
        LinearAndBlend = 3
        NoEndConstraint = 4
    

class StudioSurfaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AlignmentMethod: GeometricUtilities.AlignmentMethodBuilder
    BodyPreference: GeometricUtilities.FeatureOptions
    CurvatureTolerance: float
    FirstGuideContinuity: GeometricUtilities.Continuity
    FirstSectionContinuity: GeometricUtilities.Continuity
    FlowDirection: GeometricUtilities.FlowDirection
    GuideList: SectionList
    GuideRebuild: GeometricUtilities.Rebuild
    IntersectionTolerance: float
    LastGuideContinuity: GeometricUtilities.Continuity
    LastSectionContinuity: GeometricUtilities.Continuity
    PositionTolerance: float
    SectionList: SectionList
    SectionRebuild: GeometricUtilities.Rebuild
    SplitOutputAlongBoundaryCurves: bool
    TangentTolerance: float
    Transition: Features.StudioSurfaceBuilder.TransitionOptions


    class TransitionOptions(enum.Enum):
        NormalToEndSections = 0
        NormalToAllSections = 1
        Cubic = 2
        LinearAndBlend = 3
        NoEndConstraint = 4
    

class StudioSurface(Features.BodyFeature):
    def __init__(self) -> None: ...


class StudioSplineBuilderEx(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetKnots(self) -> float:
        ...
    def SetKnots(self, knots: float) -> None:
        ...
    def GetParameters(self) -> float:
        ...
    def SetParameters(self, parameters: float) -> None:
        ...
    def EditSpline(self, spline: NXObject) -> None:
        ...
    def InsertKnot(self, point: Point3d) -> None:
        ...
    def InsertPole(self, afterIndex: int) -> None:
        ...
    def Evaluate(self) -> None:
        ...
    def UpdateOnConstraintPlane(self) -> None:
        ...
    CanUseOrientationTool: bool
    ConstraintManager: Features.GeometricConstraintDataManager
    ConstraintPlane: CoordinateSystem
    Curve: Spline
    Degree: int
    DrawingPlane: Plane
    DrawingPlaneOption: Features.StudioSplineBuilderEx.DrawingPlaneOptions
    Extender: GeometricUtilities.SplineExtensionBuilder
    HasPlaneConstraint: bool
    HasProportionalUpdate: bool
    InputCurveOption: Features.StudioSplineBuilderEx.InputCurveOptions
    IsAssociative: bool
    IsPeriodic: bool
    IsSingleSegment: bool
    MatchKnotsType: Features.StudioSplineBuilderEx.MatchKnotsTypes
    MovementMethod: Features.StudioSplineBuilderEx.MovementMethodType
    MovementPlane: Plane
    MovementVector: Direction
    OrientExpress: GeometricUtilities.OrientXpressBuilder
    Type: Features.StudioSplineBuilderEx.Types
    WCSOption: Features.StudioSplineBuilderEx.WCSOptionType


    class WCSOptionType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        YZ = 3
        XZ = 4
        XY = 5
    

    class Types(enum.Enum):
        ThroughPoints = 0
        ByPoles = 1
    

    class MovementMethodType(enum.Enum):
        WCS = 0
        View = 1
        Vector = 2
        Plane = 3
        Normal = 4
        Polygon = 5
    

    class MatchKnotsTypes(enum.Enum):
        None = 0
        Cubic = 1
        General = 2
    

    class InputCurveOptions(enum.Enum):
        Keep = 0
        Hide = 1
        Delete = 2
    

    class DrawingPlaneOptions(enum.Enum):
        View = 0
        XY = 1
        YZ = 2
        XZ = 3
        General = 4
    

class StudioSplineBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetKnots(self) -> float:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.Features.StudioSplineBuilderEx instead..")"""
        ...
    def SetKnots(self, knots: float) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.Features.StudioSplineBuilderEx instead..")"""
        ...
    def GetParameters(self) -> float:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.Features.StudioSplineBuilderEx instead..")"""
        ...
    def SetParameters(self, parameters: float) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.Features.StudioSplineBuilderEx instead..")"""
        ...
    def SetNonParametricSpline(self, spline: Spline, method: Features.StudioSplineBuilder.Method) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.Features.StudioSplineBuilderEx instead..")"""
        ...
    Associative: bool
    ConstraintManager: Features.GeometricConstraintDataManager
    Curve: Spline
    Degree: int
    InputCurveOption: Features.StudioSplineBuilder.CurveOption
    IsPeriodic: bool
    MatchKnots: Features.StudioSplineBuilder.MatchKnotsType
    SplineMethod: Features.StudioSplineBuilder.Method


    class Method(enum.Enum):
        ThroughPoints = 0
        ByPoles = 1
    

    class MatchKnotsType(enum.Enum):
        None = 0
        Cubic = 1
        General = 2
    

    class CurveOption(enum.Enum):
        Retain = 0
        Blank = 1
        Delete = 2
    

class StudioSpline(Features.Feature):
    def __init__(self) -> None: ...


class StepBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BeltFace: ScCollector
    BoundaryOffsetDim1: Expression
    BoundaryOffsetDim2: Expression
    ChangeWallThickness: bool
    DepthMethod: Features.StepBuilder.DepthMethods
    KeepWallThickness: bool
    ProjectionDirection1: GeometricUtilities.ProjectionOptions
    ProjectionDirection2: GeometricUtilities.ProjectionOptions
    RefObjectType1: Features.StepBuilder.ReferenceBoundaryTypes
    RefObjectType2: Features.StepBuilder.ReferenceBoundaryTypes
    ReverseBoundary1Direction: bool
    ReverseBoundary2Direction: bool
    ReverseDepthDirection: bool
    ReverseMotionSide: bool
    SelectBoundaryEdge1: ScCollector
    SelectBoundaryEdge2: ScCollector
    SelectBoundaryFace1: ScCollector
    SelectBoundaryFace2: ScCollector
    SelectBoundaryPlane1: Plane
    SelectBoundaryPlane2: Plane
    SelectBoundarySection1: Section
    SelectBoundarySection2: Section
    SelectReplacementFace: ScCollector
    SelectStepWallReplmFace1: ScCollector
    SelectStepWallReplmFace2: ScCollector
    SpecifiedWallThicknessDim: Expression
    StepBlendRadiusDim1: Expression
    StepBlendRadiusDim2: Expression
    StepDepthDim: Expression
    StepFaceMethod1: Features.StepBuilder.StepFaceMethods
    StepFaceMethod2: Features.StepBuilder.StepFaceMethods
    StepLocation: Features.StepBuilder.StepLocations
    StepNewType: Features.StepBuilder.StepNewTypes
    StepRampDim1: Expression
    StepRampDim2: Expression
    StepType: Features.StepBuilder.StepTypes
    StepWallBlendRadiusDim1: Expression
    StepWallBlendRadiusDim2: Expression
    StepWallMethod1: Features.StepBuilder.StepWallMethods
    StepWallMethod2: Features.StepBuilder.StepWallMethods
    StepWallRampDim1: Expression
    StepWallRampDim2: Expression
    StepWallThickDim1: Expression
    StepWallThickDim2: Expression
    Type: Features.StepBuilder.StepNewTypes


    class StepWallMethods(enum.Enum):
        Normal = 0
        OffsetofStepFace = 1
        RuledRamp = 2
        VariableOffsetRamp = 3
        Blend = 4
        ExtendtoNext = 5
        ExtendtoSelected = 6
    

    class StepTypes(enum.Enum):
        End = 0
        Middle = 1
        Chamfer = 2
    

    class StepNewTypes(enum.Enum):
        Thick = 0
        Thin = 1
        Jog = 2
        Chamfer = 3
    

    class StepLocations(enum.Enum):
        End = 0
        Middle = 1
    

    class StepFaceMethods(enum.Enum):
        Normal = 0
        AlignwithReferenceFace = 1
        RuledRamp = 2
        VariableOffsetRamp = 3
        Blend = 4
    

    class ReferenceBoundaryTypes(enum.Enum):
        Face = 0
        DatumPlane = 1
        Curve = 2
        Edge = 3
        ShareFirst = 4
    

    class DepthMethods(enum.Enum):
        OffsetFace = 0
        ToSelected = 1
    

class Step(Features.BodyFeature):
    def __init__(self) -> None: ...


class SplitBodyBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BooleanTool: GeometricUtilities.BooleanToolBuilder
    KeepImprintedEdges: bool
    TargetBody: SelectBodyList
    TargetBodyCollector: ScCollector
    Tolerance: float


class SplitBody(Features.BodyFeature):
    def __init__(self) -> None: ...


class SpineCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Evaluate(self) -> None:
        ...
    ArcSegmentsType: Features.SpineCurveBuilder.ArcSegmentsTypes
    Associative: bool
    Closed: bool
    ReverseStartDirection: bool
    StartPoint: Point
    ThroughPlanesList: GeometricUtilities.SpinePlaneBuilderList


    class ArcSegmentsTypes(enum.Enum):
        Simple = 0
        Smooth = 1
    

class SpineCurve(Features.CurveFeature):
    def __init__(self) -> None: ...


class SphericalCornerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTol: float
    DistanceTol: float
    HelpPoint: Point
    Radius: Expression
    Wall1: GeometricUtilities.FaceSetData
    Wall2: GeometricUtilities.FaceSetData
    Wall3: GeometricUtilities.FaceSetData


class SphericalCorner(Features.BodyFeature):
    def __init__(self) -> None: ...


class SphereBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Arc: SelectICurve
    BooleanOption: GeometricUtilities.BooleanOperation
    CenterPoint: Point
    Diameter: Expression
    ParentAssociativity: bool
    Type: Features.SphereBuilder.Types


    class Types(enum.Enum):
        CenterPointAndDiameter = 0
        Arc = 1
    

class Sphere(Features.BodyFeature):
    def __init__(self) -> None: ...


class SolidPunch(Features.Feature):
    def __init__(self) -> None: ...


class SoftBlend(Features.BodyFeature):
    def __init__(self) -> None: ...
    def IsolateToolBodies(self) -> None:
        ...


class SnipSurfaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetCreateNewCopy(self) -> bool:
        ...
    def SetCreateNewCopy(self, createNewCopy: bool) -> None:
        ...
    CutType: int
    DivideSurface: bool
    EditCopy: bool
    IsoparametricPosition: Expression
    KeepOppositeSurface: bool
    ProjectDirection: GeometricUtilities.ProjectionOptions
    RefitControl: GeometricUtilities.RefitControlBuilder
    RegionPickPoint: Point3d
    SelectUV: int
    SnippingCurve: Section
    SnippingObject: SelectTaggedObject
    SnippingPlane: Plane
    SurfacePointUV: Point3d
    TargetFace: SelectFace
    Type: Features.SnipSurfaceBuilder.Types


    class Types(enum.Enum):
        SnipCurve = 0
        SnipSurface = 1
        SnipAtPlane = 2
        IsoparamSnip = 3
    

class SnipSurface(Features.BodyFeature):
    def __init__(self) -> None: ...


class SmoothSplineBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Curve: SelectCurve
    CurveRange: GeometricUtilities.CurveRangeBuilder
    EndConstraint: GeometricUtilities.Continuity
    ModificationPercentage: int
    SmoothingFactor: int
    StartConstraint: GeometricUtilities.Continuity
    Type: Features.SmoothSplineBuilder.Types


    class Types(enum.Enum):
        Curvature = 0
        CurvatureVariation = 1
    

class SmoothSpline(Features.CurveFeature):
    def __init__(self) -> None: ...


class SmoothRangeBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.SmoothRangeBuilder]) -> None:
        ...
    def Append(self, object: Features.SmoothRangeBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.SmoothRangeBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.SmoothRangeBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.SmoothRangeBuilder) -> None:
        ...
    def Erase(self, obj: Features.SmoothRangeBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.SmoothRangeBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.SmoothRangeBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.SmoothRangeBuilder, object2: Features.SmoothRangeBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.SmoothRangeBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SmoothRangeBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    SmoothRangeFrom: Point
    SmoothRangeTo: Point


class SmoothCurveStringBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def UpdateOnExpressionChange(self) -> None:
        ...
    AddFillets: bool
    AngularThreshold: Expression
    CurveFitData: GeometricUtilities.CurveFitData
    CurveOptions: GeometricUtilities.CurveOptions
    Curves: Section
    DistanceThreshold: Expression
    FixedCurves: SelectCurveList
    LevelType: Features.SmoothCurveStringBuilder.LevelTypes
    MergeType: Features.SmoothCurveStringBuilder.MergeTypes
    Radius: Expression
    SupportFaces: ScCollector
    Tolerance: Expression
    Type: Features.SmoothCurveStringBuilder.Types


    class Types(enum.Enum):
        FreeCurves = 0
        CurvesOnSurfaces = 1
    

    class MergeTypes(enum.Enum):
        None = 0
        SameTypes = 1
        AllCurves = 2
    

    class LevelTypes(enum.Enum):
        G0 = 0
        G1 = 1
        G2 = 2
    

class SmoothCurveString(Features.Feature):
    def __init__(self) -> None: ...


class SketchSplineBuilder(Features.StudioSplineBuilderEx):
    def __init__(self) -> None: ...


class SketchFitCurveBuilder(Features.FitCurveBuilder):
    def __init__(self) -> None: ...


class SketchFeature(Features.Feature):
    def __init__(self) -> None: ...
    Sketch: Sketch


class SketchConversionStatus(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Feature: Features.Feature
    Reason: Features.SketchConversionStatus.ReasonType
    Status: Features.SketchConversionStatus.Type


    class Type(enum.Enum):
        Success = 0
        Failure = 1
        PartialSuccess = 2
    

    class ReasonType(enum.Enum):
        NoIssues = 0
        BrokenLink = 1
        OutOfDate = 2
        SourceNotLoaded = 3
        SourceSuppressed = 4
        Suppressed = 5
        NotPlanar = 6
        InvalidFeature = 7
        InvalidInput = 8
        MultipleCoplanarSketches = 9
        SomeConstraintsNotTransferred = 10
        BrokenLinkNullXform = 11
        MultipleXform = 12
        SingleSourceMultipleLinks = 13
        MultipleSketchesWithNonParallelNormals = 14
        MultipleCurvesJoinedIntoOneLinkedCurve = 15
        LinkedCurveDifferentFromSourceCurve = 16
        MultipleInstanceOfASourcePart = 17
        BrokenExtract = 18
        OutOfDateExtract = 19
        ExtractSourceSuppressed = 20
        ExtractSomeConstraintsNotTransferred = 21
    

class SketchConversionReport(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetStatuses(self) -> typing.List[Features.SketchConversionStatus]:
        ...
    def FreeResource(self) -> None:
        ...


class SilhouetteFlangeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def UpdateLawSpine(self) -> None:
        ...
    def GetIsDirectionFlipped(self) -> bool:
        ...
    def SetIsDirectionFlipped(self, flipDirection: bool) -> None:
        ...
    def GetIsSideFlipped(self) -> bool:
        ...
    def SetIsSideFlipped(self, flipSide: bool) -> None:
        ...
    def GetCenterCurve(self) -> Curve:
        ...
    def GetSilhouetteCurve(self) -> Curve:
        ...
    def CreatePipe(self) -> None:
        ...
    AngleLaw: GeometricUtilities.LawBuilder
    BaseCurves: Section
    BaseFaces: ScCollector
    BaseFactor: int
    BasePipeContinuity: GeometricUtilities.Continuity
    CreateCurves: bool
    ExtendFlange: bool
    FlangeFactor: int
    FlangePipeContinuity: GeometricUtilities.Continuity
    Gap: Expression
    LengthLaw: GeometricUtilities.LawBuilder
    MergeFacesIfPossible: bool
    OutputSurfaceOption: Features.SilhouetteFlangeBuilder.OutputSurfaceOptions
    ParentFeature: Features.SelectFeature
    PositionTolerance: float
    RadiusLaw: GeometricUtilities.LawBuilder
    ReferenceDirectionOption: Features.SilhouetteFlangeBuilder.ReferenceDirectionOptions
    ReferenceFaces: ScCollector
    ReferenceVector: Direction
    ShowPipe: bool
    TangentTolerance: float
    TrimBaseFaces: bool
    Type: Features.SilhouetteFlangeBuilder.Types


    class Types(enum.Enum):
        Basic = 0
        AbsoluteGap = 1
        VisualGap = 2
    

    class ReferenceDirectionOptions(enum.Enum):
        FaceNormal = 0
        Vector = 1
        NormalDraft = 2
        VectorDraft = 3
    

    class OutputSurfaceOptions(enum.Enum):
        BlendFlange = 0
        PipeOnly = 1
        FlangeOnly = 2
    

class SilhouetteFlange(Features.BodyFeature):
    def __init__(self) -> None: ...


class ShowRelatedFacesBuilder(Builder):
    def __init__(self) -> None: ...
    def LockConstraint(self, feature: Features.Feature) -> None:
        ...
    def UnlockConstraint(self, feature: Features.Feature) -> None:
        ...
    def DeleteConstraint(self, feature: Features.Feature) -> None:
        ...
    def DeleteOffsetRelation(self, offsetFaces: typing.List[NXObject]) -> None:
        ...
    def UnlockAllConstraints(self) -> None:
        ...
    def DeleteAllConstraints(self) -> None:
        ...
    def DeleteAllOffsetRelationOnBody(self) -> None:
        ...
    OffsetRelations: bool
    RelatedFace: SelectFace


class ShipCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def CreateProjectSetupBuilder(self) -> Features.ShipDesign.ProjectSetupBuilder:
        ...
    def CreateMainDimensionsBuilder(self, mainDimensions: Features.Feature) -> Features.ShipDesign.MainDimensionsBuilder:
        ...
    def CreateFrameBarOutBuilder(self, frameBarOut: Features.Feature) -> Features.ShipDesign.FrameBarOutBuilder:
        ...
    def CreateDecksBuilder(self, decks: Features.Feature) -> Features.ShipDesign.DecksBuilder:
        ...
    def CreateBulkHeadsBuilder(self, bulkHead: Features.Feature) -> Features.ShipDesign.BulkHeadsBuilder:
        ...
    def CreateItFramesBuilder(self, itFrame: Features.Feature) -> Features.ShipDesign.ItFramesBuilder:
        ...
    def CreateInsertSheetBodyBuilder(self, insertSheetBody: Features.ShipDesign.InsertSheetBody) -> Features.ShipDesign.InsertSheetBodyBuilder:
        ...
    def CreateReferenceLineBuilder(self, referenceLine: Features.Feature) -> Features.ShipDesign.ReferenceLineBuilder:
        ...
    def CreateTransFrameBuilder(self, transFrame: Features.Feature) -> Features.ShipDesign.TransFrameBuilder:
        ...
    def CreateInsertFramesBuilder(self, insertFrames: Features.Feature) -> Features.ShipDesign.InsertFramesBuilder:
        ...
    def CreateZFrameBuilder(self, transFrame: Features.Feature) -> Features.ShipDesign.ZFrameBuilder:
        ...
    def CreateYFrameBuilder(self, transFrame: Features.Feature) -> Features.ShipDesign.YFrameBuilder:
        ...
    def CreateMarkingLineBuilder(self, markingLine: Features.Feature) -> Features.ShipDesign.MarkingLineBuilder:
        ...
    def CreateMarkingLineDesignBuilder(self, markingLine: Features.Feature) -> Features.ShipDesign.MarkingLineDesignBuilder:
        ...
    def CreateSteelDistributionBuilder(self, steelDistribution: Features.Feature) -> Features.ShipDesign.SteelDistributionBuilder:
        ...
    def CreateShipFlatPatternBuilder(self, shipFlatPattern: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.Features.ShipDesign.PlatePreparationBuilder.CreatePlatePreparationBuilder() instead.")"""
        ...
    def CreatePlatePreparationBuilder(self, platePreparation: Features.Feature) -> Features.ShipDesign.PlatePreparationBuilder:
        ...
    def CreateProfileListBuilder(self, profileList: Features.Feature) -> Features.ShipDesign.ProfileListBuilder:
        ...
    def CreateManufacturingOutBuilder(self, frameBarOut: Features.Feature) -> Features.ShipDesign.ManufacturingOutBuilder:
        ...
    def CreateUpdateShipLibraryBuilder(self, updateShipLibrary: Features.Feature) -> Features.ShipDesign.UpdateShipLibraryBuilder:
        ...
    def CreateShipProfileCutoutBuilder(self, profileCutout: Features.Feature) -> Features.ShipDesign.ShipProfileCutoutBuilder:
        ...
    def CreateKnuckledProfilesBuilder(self, knuckledProfiles: Features.ShipDesign.KnuckledProfiles) -> Features.ShipDesign.KnuckledProfilesBuilder:
        ...
    def CreateVentHolesMarkingBuilder(self, ventHolesMarking: Features.ShipDesign.VentHolesMarking) -> Features.ShipDesign.VentHolesMarkingBuilder:
        ...
    def CreateCustomBracketBuilder(self, customBracket: Features.Feature) -> Features.ShipDesign.CustomBracketBuilder:
        ...
    def CreateWeldCutBuilder(self, weldCut: Features.Feature) -> Features.ShipDesign.WeldCutBuilder:
        ...
    def CreateShipCutoutBuilder(self, shipCutout: Features.ShipDesign.ShipCutout) -> Features.ShipDesign.ShipCutoutBuilder:
        ...
    def CreateShipEndCutBuilder(self, shipEndCut: Features.ShipDesign.ShipEndCut) -> Features.ShipDesign.ShipEndCutBuilder:
        ...
    def CreateSteelVentHolesBuilder(self, steelVentHoles: Features.ShipDesign.SteelVentHoles) -> Features.ShipDesign.SteelVentHolesBuilder:
        ...
    def CreateSteelCollarPlateBuilder(self, steelCollarPlate: Features.ShipDesign.SteelCollarPlate) -> Features.ShipDesign.SteelCollarPlateBuilder:
        ...
    def CreateExcessMaterialBuilder(self, excessMaterial: Features.ShipDesign.ExcessMaterial) -> Features.ShipDesign.ExcessMaterialBuilder:
        ...
    def CreateProfileBuilder(self, profile: Features.Feature) -> Features.ShipDesign.ProfileBuilder:
        ...
    def CreateTraceLinesBuilder(self, traceLines: Features.ShipDesign.TraceLines) -> Features.ShipDesign.TraceLinesBuilder:
        ...
    def CreateSteelSupportBuilder(self, steelSupport: Features.ShipDesign.SteelSupport) -> Features.ShipDesign.SteelSupportBuilder:
        ...
    def CreatePillarBuilder(self, pillar: Features.ShipDesign.Pillar) -> Features.ShipDesign.PillarBuilder:
        ...
    def CreateShipSectionBuilder(self, shipSection: Features.ShipDesign.ShipSection) -> Features.ShipDesign.ShipSectionBuilder:
        ...
    def CreateShipIntersectionsBuilder(self, intersectionSheets: Features.ShipDesign.ShipIntersections) -> Features.ShipDesign.ShipIntersectionsBuilder:
        ...
    def CreateShellExpansionBuilder(self, shellExpansion: Features.ShipDesign.ShellExpansion) -> Features.ShipDesign.ShellExpansionBuilder:
        ...
    def CreateShipFeatureConverter(self) -> Features.ShipDesign.ShipFeatureConverter:
        ...
    def CreateCuttingSideFacesBuilder(self) -> Features.ShipDesign.CuttingSideFacesBuilder:
        ...
    def CreateRollingLineBuilder(self, rollingLine: Features.ShipDesign.RollingLine) -> Features.ShipDesign.RollingLineBuilder:
        ...
    def CreateShipCoordinatesBuilder(self) -> Features.ShipDesign.ShipCoordinatesBuilder:
        ...
    def CreatePlateBuilder(self, plate: Features.ShipDesign.Plate) -> Features.ShipDesign.PlateBuilder:
        ...
    def CreateCopyPasteNewBuilder(self, userWorkOcc: Assemblies.Component) -> Features.ShipDesign.CopyPasteNewBuilder:
        ...
    def CreateShellTemplateBuilder(self, shellTemplate: Features.ShipDesign.ShellTemplate) -> Features.ShipDesign.ShellTemplateBuilder:
        ...
    def CreateSteelInsulationBuilder(self, steelInsulation: Features.ShipDesign.SteelInsulation) -> Features.ShipDesign.SteelInsulationBuilder:
        ...
    def CreateStandardPartFrameworkBuilder(self, stdPartOcc: Assemblies.Component) -> Features.ShipDesign.StandardPartFrameworkBuilder:
        ...
    def CreateSplitProfilePlateBuilder(self) -> Features.ShipDesign.SplitProfilePlateBuilder:
        ...
    def CreateQualifySketchBuilder(self) -> Features.ShipDesign.QualifySketchBuilder:
        ...
    def CreatePlateChamferBuilder(self, plateChamfer: Features.ShipDesign.PlateChamfer) -> Features.ShipDesign.PlateChamferBuilder:
        ...
    def CreateFeaturesToMarkBuilder(self) -> Features.ShipDesign.FeaturesToTagBuilder:
        ...
    def CreateCompareModeBuilder(self) -> Features.ShipDesign.CompareModeBuilder:
        ...
    def CreateRebaseBuilder(self) -> Features.ShipDesign.RebaseBuilder:
        ...
    def CreateInverseBendingLinesBuilder(self, inverseBendingLines: Features.ShipDesign.InverseBendingLines) -> Features.ShipDesign.InverseBendingLinesBuilder:
        ...
    def CreateEndCutBuilder(self, endCut: Features.ShipDesign.EndCut) -> Features.ShipDesign.EndCutBuilder:
        ...
    def CreateStiffenerBuilder(self, stiffener: Features.ShipDesign.Stiffener) -> Features.ShipDesign.StiffenerBuilder:
        ...
    def CreateRemoveSplitBuilder(self) -> Features.ShipDesign.RemoveSplitBuilder:
        ...
    def CreateShipAttributeHolder(self) -> Features.ShipDesign.ShipAttributeHolder:
        ...
    def CreateShipAttributeHolderWithFeature(self, featureType: str) -> Features.ShipDesign.ShipAttributeHolder:
        ...
    def CreateShipContainerBuilder(self) -> Features.ShipDesign.ShipContainerBuilder:
        ...
    def CreatePlateSystemBuilder(self, plateSystem: Features.ShipDesign.PlateSystem) -> Features.ShipDesign.PlateSystemBuilder:
        ...
    def CreateProfileSystemBuilder(self, profileSystem: Features.ShipDesign.ProfileSystem) -> Features.ShipDesign.ProfileSystemBuilder:
        ...
    def CreateStiffenerSystemBuilder(self, stiffenerSystem: Features.ShipDesign.StiffenerSystem) -> Features.ShipDesign.StiffenerSystemBuilder:
        ...
    def CreateHullBuilder(self, hull: Features.ShipDesign.Hull) -> Features.ShipDesign.HullBuilder:
        ...
    def CreateDeckBuilder(self, deck: Features.ShipDesign.Deck) -> Features.ShipDesign.DeckBuilder:
        ...
    def CreateTransverseBulkheadBuilder(self, transverseBulkhead: Features.ShipDesign.TransverseBulkhead) -> Features.ShipDesign.TransverseBulkheadBuilder:
        ...
    def CreateLongitudinalBulkheadBuilder(self, longitudinalBulkhead: Features.ShipDesign.LongitudinalBulkhead) -> Features.ShipDesign.LongitudinalBulkheadBuilder:
        ...
    def CreateGenericPlateSystemBuilder(self, genericPlateSystem: Features.ShipDesign.GenericPlateSystem) -> Features.ShipDesign.GenericPlateSystemBuilder:
        ...
    def CreateSeamBuilder(self, seam: Features.ShipDesign.Seam) -> Features.ShipDesign.SeamBuilder:
        ...
    def CreateSubSystemsBuilder(self, seam: Features.ShipDesign.SubSystems) -> Features.ShipDesign.SubSystemsBuilder:
        ...
    def CreateEdgeReinforcementBuilder(self, edgeReinforcement: Features.ShipDesign.EdgeReinforcement) -> Features.ShipDesign.EdgeReinforcementBuilder:
        ...
    def CreatePillarSystemBuilder(self, pillarSystem: Features.ShipDesign.PillarSystem) -> Features.ShipDesign.PillarSystemBuilder:
        ...
    def CreateEditWeldingBuilder(self) -> Features.ShipDesign.EditWeldingBuilder:
        ...
    def CreateEditStockBuilder(self) -> Features.ShipDesign.EditStockBuilder:
        ...
    def CreateShipDesignPreferencesBuilder(self) -> Features.ShipDesign.ShipDesignPreferencesBuilder:
        ...
    def CreateCutout2Builder(self, cutout2: Features.ShipDesign.Cutout2) -> Features.ShipDesign.Cutout2Builder:
        ...
    def CreateVentilationHoles2Builder(self, ventilationHoles2: Features.ShipDesign.VentilationHoles2) -> Features.ShipDesign.VentilationHoles2Builder:
        ...
    def CreateEdgeCutBuilder(self, edgeCut: Features.ShipDesign.EdgeCut) -> Features.ShipDesign.EdgeCutBuilder:
        ...
    def CreateDisplaySolidBuilder(self) -> Features.ShipDesign.DisplaySolidBuilder:
        ...
    def CreateReverseSplitBuilder(self) -> Features.ShipDesign.ReverseSplitBuilder:
        ...
    def CreateDeleteSeamBuilder(self) -> Features.ShipDesign.DeleteSeamBuilder:
        ...
    def CreateManufacturingDataBuilder(self) -> Features.ShipDesign.ManufacturingDataBuilder:
        ...
    def CreateSetModeBuilder(self) -> Features.ShipDesign.SetModeBuilder:
        ...
    def CreateSynchronizeDesignViewBuilder(self) -> Features.ShipDesign.SynchronizeDesignViewBuilder:
        ...
    def CreateManufacturingPreparationBuilder(self) -> Features.ShipDesign.ManufacturingPreparationBuilder:
        """[Obsolete("Deprecated in NX8.0.3.  Use NXOpen.Features.ShipDesign.ManufacturingPreparationBuilder instead.")"""
        ...
    def CreateManufacturingPreparationBuilder(self, manuPrep: Features.ShipDesign.ManufacturingPreparation) -> Features.ShipDesign.ManufacturingPreparationBuilder:
        ...
    def CreateProfileCutoutBuilder(self, profileCutout: Features.Feature) -> Features.ShipDesign.ProfileCutoutBuilder:
        ...
    def CreateWeldCut2Builder(self, weldCut2: Features.ShipDesign.WeldCut2) -> Features.ShipDesign.WeldCut2Builder:
        ...
    def CreateFeaturesBatchOperationBuilder(self) -> Features.ShipDesign.FeaturesBatchOperationBuilder:
        ...
    def CreateDvToMvMappingBuilder(self, mappingFeature: Features.Feature) -> Features.ShipDesign.DvToMvMappingBuilder:
        ...
    def CreateStandardPartFrameworkBuilder(self, stdPart: NXObject, createBasicDesignBuilder: bool) -> Features.ShipDesign.StandardPartFrameworkBuilder:
        ...
    def CreateTransitionBuilder(self) -> Features.ShipDesign.TransitionBuilder:
        ...
    def CreateCornerCutListitemBuilder(self) -> Features.ShipDesign.CornerCutListItemBuilder:
        ...
    def CreateCornerCutBuilder(self, cornerCut: Features.ShipDesign.CornerCut) -> Features.ShipDesign.CornerCutBuilder:
        ...
    def CreateAlongGuideCutBuilder(self, alongGuideCut: Features.ShipDesign.AlongGuideCut) -> Features.ShipDesign.AlongGuideCutBuilder:
        ...
    def CreateConceptFromSpreadsheetBuilder(self, conceptFromSpreadsheet: Features.ShipDesign.ConceptFromSpreadsheet) -> Features.ShipDesign.ConceptFromSpreadsheetBuilder:
        ...
    def CreateFilterBuilder(self) -> Features.ShipDesign.FilterBuilder:
        ...
    def CreateSmartRuleBuilder(self, smartRule: Features.ShipDesign.SmartRule) -> Features.ShipDesign.SmartRuleBuilder:
        ...
    def SetAppContextMode(self, mode: int) -> None:
        ...
    def CreateSplitStandardPartBuilder(self, splitStandardPart: Features.ShipDesign.SplitStandardPart) -> Features.ShipDesign.SplitStandardPartBuilder:
        ...
    def CreateOrientationDefinitionBuilder(self, orientation: Features.ShipDesign.OrientationDefinition) -> Features.ShipDesign.OrientationDefinitionBuilder:
        ...
    def CreateShipDesignVersionUpBuilder(self) -> Features.ShipDesign.ShipDesignVersionUpBuilder:
        ...
    def CreateBuiltUpManModeBuilder(self) -> Features.ShipDesign.BuiltUpManModeBuilder:
        ...
    def CreateProfileTransitionBuilder(self, profileTransition: Features.ShipDesign.ProfileTransition) -> Features.ShipDesign.ProfileTransitionBuilder:
        ...
    def CreateExamineSteelFeatureBuilder(self) -> Features.ShipDesign.ExamineSteelFeatureBuilder:
        ...
    def CreateShipTrimBodyBuilder(self, shipTrimBody: Features.ShipDesign.ShipTrimBody) -> Features.ShipDesign.ShipTrimBodyBuilder:
        ...
    def CreateCopyObjectsBuilder(self, userWorkOcc: Assemblies.Component) -> Features.ShipDesign.CopyObjectsBuilder:
        ...
    def CreatePinJigBuilder(self, pinJig: Features.ShipDesign.PinJig) -> Features.ShipDesign.PinJigBuilder:
        ...
    def CreateSectionDrawingBuilder(self) -> Features.ShipDesign.SectionDrawingBuilder:
        ...
    def CreateMirrorShipStructureBuilder(self) -> Features.ShipDesign.MirrorShipStructureBuilder:
        ...
    def CreateWeightAndCgBuilder(self) -> Features.ShipDesign.WeightAndCGBuilder:
        ...
    def CreateMaterialEstimationBuilder(self) -> Features.ShipDesign.MaterialEstimationBuilder:
        ...
    def CreateUnfoldedMinRecBuilder(self) -> Features.ShipDesign.UnfoldedMinRecBuilder:
        ...
    def CreateEditContextAttributesBuilder(self) -> Features.ShipDesign.EditContextAttributesBuilder:
        ...
    def CreateExpansionDrawingBuilder(self, expansionFeature: Features.ShipDesign.ExpansionDrawing) -> Features.ShipDesign.ExpansionDrawingBuilder:
        ...
    def CreateDrawingAnnotationBuilder(self) -> Features.ShipDesign.DrawingAnnotationBuilder:
        ...
    def CreateMaterialAllowanceBuilder(self) -> Features.ShipDesign.MaterialAllowanceBuilder:
        ...
    def RegisterCallbackFunctionsForMirrorCopy(self) -> None:
        ...
    def CreateShipPreparationBuilder(self) -> Features.ShipDesign.ShipPreparationBuilder:
        ...
    def UpdateShipManufacturingFeatures(self) -> None:
        ...
    def CreateSectionEditorBuilder(self, viewTag: Drawings.DraftingView) -> Features.ShipDesign.SectionEditorBuilder:
        ...
    def CreateInteractiveAnnotationBuilder(self) -> Features.ShipDesign.InteractiveAnnotationBuilder:
        ...
    def CreateBracketBuilder(self, bracket: Features.ShipDesign.Bracket) -> Features.ShipDesign.BracketBuilder:
        ...
    def CreateCollarPlateBuilder(self, collarPlate: Features.ShipDesign.CollarPlate) -> Features.ShipDesign.CollarPlateBuilder:
        ...
    def SetSteelFeatureApproach(self, steelFeatureApproach: Features.ShipCollection.SteelFeatureApproach) -> None:
        ...
    def CreatePlateDivideBuilder(self, plateDivide: Features.ShipDesign.PlateDivide) -> Features.ShipDesign.PlateDivideBuilder:
        ...
    def CreateDivideBuilder(self, divide: Features.ShipDesign.Divide) -> Features.ShipDesign.DivideBuilder:
        ...
    def CreateValidateModelBuilder(self) -> Features.ShipDesign.ValidateModelBuilder:
        ...
    def CreateRoomBuilder(self) -> Features.ShipDesign.RoomBuilder:
        ...
    def CreateRoomThicknessItemBuilder(self) -> Features.ShipDesign.RoomThicknessItemBuilder:
        ...
    def CreateRoomPanelBuilder(self) -> Features.ShipDesign.RoomPanelBuilder:
        ...
    def CreateRoomAttributesBuilder(self) -> Features.ShipDesign.RoomAttributesBuilder:
        ...
    def CreateRoomContainerBuilder(self) -> Features.ShipDesign.RoomContainerBuilder:
        ...
    def CreateGeneralArrangementViewBuilder(self, view: Drawings.BaseView) -> Features.ShipDesign.GeneralArrangementViewBuilder:
        ...
    def CreateLabellingRoomsBuilder(self) -> Features.ShipDesign.LabellingRoomsBuilder:
        ...
    def CreateFaceCharacteristicsBuilder(self) -> Features.ShipDesign.GeneralArrangement.FaceCharacteristicsBuilder:
        ...
    def CreateManufacturingAssemblyNavigatorBuilder(self) -> Features.ShipDesign.ManufacturingAssemblyNavigatorBuilder:
        ...
    def CreateEditBoundaryBuilder(self) -> Features.ShipDesign.EditBoundaryBuilder:
        ...
    def CreateAddDataSetBuilder(self) -> Features.ShipDesign.AddDataSetBuilder:
        ...
    def CreateMoveToContainerBuilder(self) -> Features.ShipDesign.MoveToContainerBuilder:
        ...
    def Tag(self) -> Tag: ...

    DelayShipManufacturingFeatureUpdate: bool


    class SteelFeatureApproach(enum.Enum):
        Normal = 0
        SketchSharing = 1
    

class ShellFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FacesToPierce: ScCollector
    FacesToShell: ScCollector
    Thickness: Expression


class ShellFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class ShellBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetDefaultThickness(self, defaultThicknessValue: str) -> None:
        ...
    Body: Body
    DefaultThickness: Expression
    DefaultThicknessFlip: bool
    FaceThicknessList: ObjectList
    FaceThicknesses: ExpressionCollectorSetList
    RemovedFacesCollector: ScCollector
    TgtPierceOption: bool
    Tolerance: float
    UseSurfaceApproximation: bool


class Shell(Features.BodyFeature):
    def __init__(self) -> None: ...


class ShelfBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DepthDimension: Expression
    DepthMethod: Features.ShelfBuilder.DepthMethods
    Length1: Expression
    Length2: Expression
    LengthDimension: Expression
    LengthMethod: Features.ShelfBuilder.LengthMethods
    LimitCurve1: Section
    LimitCurve2: Section
    LimitFace1: ScCollector
    LimitFace2: ScCollector
    LimitPlane1: Plane
    LimitPlane2: Plane
    LimitPoint1: Point
    LimitPoint2: Point
    OffsetDimension: Expression
    ProjectionDir1: GeometricUtilities.ProjectionOptions
    ProjectionDir2: GeometricUtilities.ProjectionOptions
    RampLength1: Expression
    RampLength2: Expression
    RefType1: Features.ShelfBuilder.ReferenceType
    RefType2: Features.ShelfBuilder.ReferenceType
    ReverseDepthDirection: bool
    ReverseWidthDirection: bool
    Selectface: ScCollector
    ShelfEdge: ScCollector
    ShelfEnd: bool
    ShelfType: Features.ShelfBuilder.Types
    StepMethod1: Features.ShelfBuilder.StepMethod
    StepMethod2: Features.ShelfBuilder.StepMethod
    Swap: bool
    Type: Features.ShelfBuilder.Types
    WidthDimension: Expression


    class Types(enum.Enum):
        End = 0
        Middle = 1
    

    class StepMethod(enum.Enum):
        Normal = 0
        AlignwithReferenceFace = 1
        Ramp = 2
    

    class ReferenceType(enum.Enum):
        Face = 0
        DatumPlane = 1
        Curve = 2
        Point = 3
    

    class LengthMethods(enum.Enum):
        Full = 0
        ShelfFromEnd = 1
        StepFromEnd = 2
        ToSelected = 3
    

    class DepthMethods(enum.Enum):
        Offset = 0
        ToNextWall = 1
    

class Shelf(Features.BodyFeature):
    def __init__(self) -> None: ...


class SheetMetalFromSolid(Features.BodyFeature):
    def __init__(self) -> None: ...


class SewBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetUnsewnBodies(self) -> typing.List[NXObject]:
        ...
    BodyPreference: Features.SewBuilder.BodyPreferenceTypes
    IsCommonFacesSearched: bool
    OutputMultipleSheets: bool
    SewAllInstances: bool
    TargetBodies: SelectDisplayableObjectList
    TargetFaces: SelectFaceList
    Tolerance: float
    ToolBodies: SelectDisplayableObjectList
    ToolFaces: SelectFaceList
    Type: Features.SewBuilder.Types


    class Types(enum.Enum):
        Sheet = 0
        Solid = 1
    

    class BodyPreferenceTypes(enum.Enum):
        Solid = 0
        Sheet = 1
    

class Sew(Features.CombineBodyFeature):
    def __init__(self) -> None: ...


class ServiceOrientedFeatureCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...


class ServiceOrientedFeatureCurve(Features.CurveFeature):
    def __init__(self) -> None: ...


class ServiceOrientedBodyFeatureBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...


class ServiceOrientedBodyFeature(Features.BodyFeature):
    def __init__(self) -> None: ...


class SelectPartModule(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Features.PartModule, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Features.PartModule, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Features.PartModule, view1: View, point1: Point3d, selection2: Features.PartModule, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Features.PartModule, view1: View, point1: Point3d, selection2: Features.PartModule, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Features.PartModule, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Features.PartModule:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Features.PartModule


class SelectFlatPattern(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Features.FlatPattern, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Features.FlatPattern, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Features.FlatPattern, view1: View, point1: Point3d, selection2: Features.FlatPattern, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Features.FlatPattern, view1: View, point1: Point3d, selection2: Features.FlatPattern, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Features.FlatPattern, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Features.FlatPattern:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Features.FlatPattern


class SelectFeatureList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Features.Feature) -> bool:
        ...
    def Add(self, objects: typing.List[Features.Feature]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Features.Feature, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Features.Feature) -> bool:
        ...
    def Remove(self, object: Features.Feature, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Features.Feature, view1: View, point1: Point3d, selection2: Features.Feature, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Features.Feature]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Features.Feature) -> bool:
        ...
    def SetArray(self, objects: typing.List[Features.Feature]) -> None:
        ...
    def GetArray(self) -> typing.List[Features.Feature]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Features.Feature, view1: View, point1: Point3d, selection2: Features.Feature, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Features.Feature, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectFeature(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Features.Feature, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Features.Feature, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Features.Feature, view1: View, point1: Point3d, selection2: Features.Feature, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Features.Feature, view1: View, point1: Point3d, selection2: Features.Feature, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Features.Feature, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Features.Feature:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Features.Feature


class SelectDatumCsysList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Features.DatumCsys) -> bool:
        ...
    def Add(self, objects: typing.List[Features.DatumCsys]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Features.DatumCsys, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Features.DatumCsys) -> bool:
        ...
    def Remove(self, object: Features.DatumCsys, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Features.DatumCsys, view1: View, point1: Point3d, selection2: Features.DatumCsys, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Features.DatumCsys]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Features.DatumCsys) -> bool:
        ...
    def SetArray(self, objects: typing.List[Features.DatumCsys]) -> None:
        ...
    def GetArray(self) -> typing.List[Features.DatumCsys]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Features.DatumCsys, view1: View, point1: Point3d, selection2: Features.DatumCsys, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Features.DatumCsys, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectBodyFeatureList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Features.BodyFeature) -> bool:
        ...
    def Add(self, objects: typing.List[Features.BodyFeature]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Features.BodyFeature, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Features.BodyFeature) -> bool:
        ...
    def Remove(self, object: Features.BodyFeature, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Features.BodyFeature, view1: View, point1: Point3d, selection2: Features.BodyFeature, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Features.BodyFeature]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Features.BodyFeature) -> bool:
        ...
    def SetArray(self, objects: typing.List[Features.BodyFeature]) -> None:
        ...
    def GetArray(self) -> typing.List[Features.BodyFeature]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Features.BodyFeature, view1: View, point1: Point3d, selection2: Features.BodyFeature, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Features.BodyFeature, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SectionSurfaceBuilderEx(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetSolutionHelpParams(self, params: float) -> None:
        ...
    def SetSolutionHelpPositions(self, points: typing.List[Point3d]) -> None:
        ...
    def SetHelpPointSupports(self, supports: typing.List[NXObject], supportSenses: bool) -> None:
        ...
    AlternateSolutions: int
    AngleLaw: GeometricUtilities.LawBuilder
    ApexCurve: Section
    BodyTypePreference: Features.SectionSurfaceBuilderEx.BodyType
    CircularTypeMode: Features.SectionSurfaceBuilderEx.CircularType
    ConicTypeMode: Features.SectionSurfaceBuilderEx.ConicType
    ControlRegion: Features.SectionSurfaceBuilderEx.ControlRegionType
    CreateApexCurve: bool
    CubicTypeMode: Features.SectionSurfaceBuilderEx.CubicType
    EndContinuity: GeometricUtilities.Continuity
    EndDepthSkew: GeometricUtilities.DepthSkewBuilder
    EndDirection: bool
    EndFace: ScCollector
    EndHighlightCurve: Section
    EndShapeCurve: Section
    EndSlopeCurve: Section
    EntireDepthSkew: GeometricUtilities.DepthSkewBuilder
    G0Tolerance: float
    G1Tolerance: float
    G2Tolerance: float
    LinearTypeMode: Features.SectionSurfaceBuilderEx.LinearType
    RadiusLaw: GeometricUtilities.LawBuilder
    Rebuild: GeometricUtilities.Rebuild
    RhoLaw: GeometricUtilities.LawBuilder
    SectionEndGuide: Section
    SectionInteriorGuide1: Section
    SectionInteriorGuide2: Section
    SectionInteriorGuide3: Section
    SectionMethodCircleTangent: Features.SectionSurfaceBuilderEx.SectionMethodCircleTangentType
    SectionMethodFilletBridge: Features.SectionSurfaceBuilderEx.SectionMethodFilletBridgeType
    SectionMethodRho: Features.SectionSurfaceBuilderEx.SectionMethodRhoType
    SectionOrientationGuide: Section
    SectionStartGuide: Section
    ShoulderCurve: Section
    SlopeControl: Features.SectionSurfaceBuilderEx.SlopeControlType
    SpineEndFlowDirection: Features.SectionSurfaceBuilderEx.SpineEndFlowType
    SpineSection: Section
    SpineStartFlowDirection: Features.SectionSurfaceBuilderEx.SpineStartFlowType
    SpineType: Features.SectionSurfaceBuilderEx.Spine
    SpineVector: Direction
    SplitAlongGuide: bool
    StartContinuity: GeometricUtilities.Continuity
    StartDepthSkew: GeometricUtilities.DepthSkewBuilder
    StartDirection: bool
    StartFace: ScCollector
    StartHighlightCurve: Section
    StartShapeCurve: Section
    StartSlopeCurve: Section
    Type: Features.SectionSurfaceBuilderEx.Types
    UDegree: Features.SectionSurfaceBuilderEx.UDegreeType


    class UDegreeType(enum.Enum):
        Conic = 0
        Cubic = 1
        Quintic = 2
    

    class Types(enum.Enum):
        Conic = 0
        Circular = 1
        Cubic = 2
        Linear = 3
    

    class SpineStartFlowType(enum.Enum):
        NotSpecified = 0
        Perpendicular = 1
        IsoLineU = 2
        IsoLineV = 3
    

    class SpineEndFlowType(enum.Enum):
        NotSpecified = 0
        Perpendicular = 1
        IsoLineU = 2
        IsoLineV = 3
    

    class Spine(enum.Enum):
        ByVector = 0
        ByCurve = 1
    

    class SlopeControlType(enum.Enum):
        ByApex = 0
        ByCurves = 1
        ByFaces = 2
    

    class SectionMethodRhoType(enum.Enum):
        Rho = 0
        LeastTension = 1
    

    class SectionMethodFilletBridgeType(enum.Enum):
        Continuity = 0
        InheritShape = 1
    

    class SectionMethodCircleTangentType(enum.Enum):
        FilletArc = 0
        CoverArc = 1
    

    class LinearType(enum.Enum):
        PointAngle = 0
        TangentTangent = 1
    

    class CubicType(enum.Enum):
        TwoSlopes = 0
        FilletBridge = 1
    

    class ControlRegionType(enum.Enum):
        Entire = 0
        Start = 1
        End = 2
    

    class ConicType(enum.Enum):
        Shoulder = 0
        Rho = 1
        Hilite = 2
        FourPointSlope = 3
        FivePoint = 4
    

    class CircularType(enum.Enum):
        ThreePoint = 0
        TwoPointRadius = 1
        TwoPointSlope = 2
        RadiusAngleArc = 3
        TangentpointTangent = 4
        CenterRadius = 5
        CenterPoint = 6
        CenterTangent = 7
        TangentRadius = 8
        TangentTangentRadius = 9
    

    class BodyType(enum.Enum):
        Solid = 0
        Sheet = 1
    

class SectionSurfaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AlternateMethod: int
    AngleLaw: GeometricUtilities.LawBuilder
    ApexCurve: Section
    ControlRegion: Features.SectionSurfaceBuilder.ControlRegionEnum
    CreateApexCurve: bool
    CurvatureTolerance: float
    EndContinuity: GeometricUtilities.Continuity
    EndDepthSkew: GeometricUtilities.DepthSkewBuilder
    EndFlowDirection: Features.SectionSurfaceBuilder.FlowDirectionEnum
    EndGuide: Section
    EndHighlightSection: Section
    EndShapeCurve: Section
    EndSlope: Section
    EndSurface: ScCollector
    EntireRegionDepthSkew: GeometricUtilities.DepthSkewBuilder
    InteriorGuide1: Section
    InteriorGuide2: Section
    InteriorGuide3: Section
    OrientationGuide: Section
    PositionTolerance: float
    RadiusLaw: GeometricUtilities.LawBuilder
    ReverseEndSurface: bool
    ReverseStartDirection: bool
    RhoLaw: GeometricUtilities.LawBuilder
    SectionMethodCircularTangent: Features.SectionSurfaceBuilder.SectionMethodCircularTangentEnum
    SectionMethodFilletBridge: Features.SectionSurfaceBuilder.SectionMethodFilletBridgeEnum
    SectionMethodRho: Features.SectionSurfaceBuilder.SectionMethodRhoEnum
    Shoulder: Section
    SpineCurve: Section
    StartContinuity: GeometricUtilities.Continuity
    StartDepthSkew: GeometricUtilities.DepthSkewBuilder
    StartFlowDirection: Features.SectionSurfaceBuilder.FlowDirectionEnum
    StartGuide: Section
    StartHighlightSection: Section
    StartShapeCurve: Section
    StartSlope: Section
    StartSurface: ScCollector
    TangentTolerance: float
    Type: Features.SectionSurfaceBuilder.Types
    UDegree: Features.SectionSurfaceBuilder.UDegreeEnum
    VDegree: GeometricUtilities.Rebuild


    class UDegreeEnum(enum.Enum):
        Conic = 0
        Cubic = 1
        Quintic = 2
    

    class Types(enum.Enum):
        EndsApexShoulder = 0
        EndsSlopeShoulder = 1
        FilletShoulder = 2
        EndsApexRho = 3
        EndsSlopeRho = 4
        FilletRho = 5
        EndsApexHilite = 6
        EndsSlopeHilite = 7
        FilletHilite = 8
        FourPointSlope = 9
        FivePoint = 10
        ThreePointArc = 11
        TwoPointRadius = 12
        EndSlopeArc = 13
        PointRadiusAngleArc = 14
        Circle = 15
        CircleTangent = 16
        EndsSlopeCubic = 17
        FilletBridge = 18
        LinearTangent = 19
    

    class SectionMethodRhoEnum(enum.Enum):
        Rho = 0
        LeastTension = 1
    

    class SectionMethodFilletBridgeEnum(enum.Enum):
        Continuity = 0
        InheritShape = 1
    

    class SectionMethodCircularTangentEnum(enum.Enum):
        FilletArc = 0
        CoverArc = 1
    

    class FlowDirectionEnum(enum.Enum):
        NotSpecified = 0
        Perpendicular = 1
        IsoLineU = 2
        IsoLineV = 3
    

    class ControlRegionEnum(enum.Enum):
        Entire = 0
        Start = 1
        End = 2
    

class SectionSurface(Features.BodyFeature):
    def __init__(self) -> None: ...


class SectionInertiaAnalysisBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ShowInfo(self) -> None:
        ...
    def RefreshScreen(self) -> None:
        ...
    def IsTempGraphics(self) -> bool:
        ...
    def GetAnnotation(self) -> typing.List[Annotations.PmiNote]:
        ...
    AnnoLayer: int
    CSys: Features.SectionInertiaAnalysisBuilder.CoordSys
    CenterOfGravity: bool
    CurveCollector: Section
    DatumPlaneLayer: int
    DatumPlanes: bool
    Distance: Expression
    FaceCollector: ScCollector
    MassPropertyType: Features.SectionInertiaAnalysisBuilder.PropertyType
    NSection: int
    PathCollector: Section
    PrincipalAxes: bool
    RectangleLayer: int
    RectangularSection: bool
    SecondPrincipleMi: bool
    SectionArea: bool
    SectionLayer: int
    SectionLength: bool
    SectionNormal: Features.SectionInertiaAnalysisBuilder.SectionAxisNormal
    SectioningMethod: Features.SectionInertiaAnalysisBuilder.SampleMethod
    Sections: bool
    ShearCenter: bool
    Thickness: Expression
    Type: Features.SectionInertiaAnalysisBuilder.Types
    Units: int
    ValidityFlag: bool


    class Types(enum.Enum):
        ParallelSections = 0
        SectionsAlongCurve = 1
        ExistingSection = 2
    

    class SectionAxisNormal(enum.Enum):
        Xc = 0
        Yc = 1
        Zc = 2
    

    class SampleMethod(enum.Enum):
        ByDistance = 0
        ByNumber = 1
    

    class PropertyType(enum.Enum):
        Hollow = 0
        Solid = 1
    

    class CoordSys(enum.Enum):
        Absolute = 0
        CurrentWCS = 1
    

class SectionInertiaAnalysis(Features.BodyFeature):
    def __init__(self) -> None: ...


class SectionEditBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Body: SelectBody
    IsNewPlane: bool
    Plane: ISurface
    Sketch: Sketch


class SectionEdit(NXObject):
    def __init__(self) -> None: ...
    def End(self) -> None:
        ...


class SectionCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetOutputGroups(self) -> typing.List[Group]:
        ...
    Associative: bool
    BasePlane: ISurface
    ChordalTolerance: float
    CurveFitData: GeometricUtilities.CurveFitData
    CurveFitJoinOptions: GeometricUtilities.CurveFitJoin
    CurveForPerpendicularPlane: SelectObject
    EndAngle: float
    EndDistance: float
    EndPercentage: float
    GroupObjects: bool
    Increment: float
    NumberOfCopies: int
    ObjectsToSection: SelectObjectList
    OutputPoints: bool
    RadialPlanePoint: Point
    RadialPlaneVector: Direction
    Ratio: float
    SampleDistance: float
    SectionPlane: Plane
    SectionPlanes: SelectObjectList
    SpacingAlongCurveType: Features.SectionCurveBuilder.SpacingType
    StartAngle: float
    StartDistance: float
    StartPercentage: float
    StepAngle: float
    StepDistance: float
    Tolerance: float
    Type: Features.SectionCurveBuilder.PlaneType


    class SpacingType(enum.Enum):
        EqualArcLength = 0
        EqualParameterSpacing = 1
        GeometricProgressionSpacing = 2
        ChordalToleranceSpacing = 3
        IncrementalArclengthSpacing = 4
    

    class PlaneType(enum.Enum):
        Selected = 0
        Parallel = 1
        Radial = 2
        PerpendicularToCurve = 3
    

class SectionCurve(Features.Feature):
    def __init__(self) -> None: ...


class ScaleCurveBuilder(Features.ServiceOrientedFeatureCurveBuilder):
    def __init__(self) -> None: ...
    CurveSettings: GeometricUtilities.CurveSettings
    ObjectsToScale: Section
    ReferenceCSYS: CoordinateSystem
    ReferencePoint: Point
    ScaleAlongXDirection: Expression
    ScaleAlongYDirection: Expression
    ScaleAlongZDirection: Expression
    ScaleType: Features.ScaleCurveBuilder.ScaleCurveType
    UniformScaleFactor: Expression


    class ScaleCurveType(enum.Enum):
        Uniform = 0
        NonUniform = 1
    

class ScaleCurve(Features.CurveFeature):
    def __init__(self) -> None: ...


class ScaleBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BodyCollector: ScCollector
    BodyToScale: SelectBodyList
    Csys: CoordinateSystem
    Point: Point
    ScaleAlongAxis: Expression
    ScaleOtherDirection: Expression
    ScaleXdirection: Expression
    ScaleYdirection: Expression
    ScaleZdirection: Expression
    Type: Features.ScaleBuilder.Types
    UniformFactor: Expression
    Vector: Direction


    class Types(enum.Enum):
        Uniform = 0
        Axisymmetric = 1
        General = 2
    

class Scale(Features.BodyFeature):
    def __init__(self) -> None: ...


class RuledBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AlignmentMethod: GeometricUtilities.AlignmentMethodBuilder
    BodyPreference: GeometricUtilities.FeatureOptions
    FirstSection: Section
    IsShapePreserved: bool
    PositionTolerance: float
    SecondSection: Section


class Ruled(Features.BodyFeature):
    def __init__(self) -> None: ...


class RPODimension(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def SetExpression(self, expression: str) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    Expression: Expression
    Subtype: PositioningDimension.Subtype
    Target: NXObject
    TargetAssociativity: Features.AssociativityType
    TargetPoint: Point3d
    Tool: NXObject
    ToolAssociativity: Features.AssociativityType
    ToolPoint: Point3d


class RPOBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetTargetAndTool(self, subtype: PositioningDimension.Subtype, target: NXObject, targetAssociativity: Features.RPOBuilder.AssociativityType, targetHelpPoint: Point3d, tool: NXObject, toolAssociativity: Features.RPOBuilder.AssociativityType, toolHelpPoint: Point3d) -> None:
        ...
    def SetExpression(self, expression: str) -> None:
        ...
    def CreatePositioningDimension(self) -> None:
        ...
    def ShowPositioningDimensions(self) -> None:
        ...
    def HidePositioningDimensions(self) -> None:
        ...
    def GetReferenceDirection(self, reference: IReferenceAxis, orientation: AxisOrientation) -> None:
        ...
    def SetReferenceDirection(self, reference: IReferenceAxis, orientation: AxisOrientation) -> None:
        ...
    def UndoLastDimension(self) -> None:
        ...
    def ApplyDimensions(self) -> None:
        ...
    def GetRpoDimensions(self) -> typing.List[Features.RPODimension]:
        ...
    def SetRpoDimensions(self, dimensions: typing.List[Features.RPODimension]) -> None:
        ...
    def CreateDimension(self) -> Features.RPODimension:
        ...


    class AssociativityType(enum.Enum):
        EndPoint = 0
        ArcCenter = 1
        Tangency = 2
        EndPoint1 = 3
        EndPoint2 = 4
        VerticalCenterline1 = 5
        VerticalCenterline2 = 6
        HorizontalCenterline1 = 7
        HorizontalCenterline2 = 8
    

class RPO(Features.BodyFeature):
    def __init__(self) -> None: ...


class Rotor(Features.BodyFeature):
    def __init__(self) -> None: ...


class RibBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CappingFaces: ScCollector
    CombineRibWithTarget: bool
    DraftAngle: Expression
    ReverseOffsetDirection: bool
    ReverseRibDirection: bool
    ReverseThicknessDirection: bool
    RibCapGeometryOption: Features.RibBuilder.RibCapGeometryOptions
    RibCapOffset: Expression
    RibDraftOption: Features.RibBuilder.RibDraftOptions
    RibThickness: Expression
    RibThicknessOffsetOption: Features.RibBuilder.RibThicknessOffsetOptions
    RibType: Features.RibBuilder.RibTypes
    Section: Section
    TargetBody: ScCollector


    class RibTypes(enum.Enum):
        PerpendiculartoSectionPlane = 0
        ParalleltoSectionPlane = 1
    

    class RibThicknessOffsetOptions(enum.Enum):
        Symmetric = 0
        Asymmetric = 1
    

    class RibDraftOptions(enum.Enum):
        None = 0
        FromCap = 1
    

    class RibCapGeometryOptions(enum.Enum):
        FromSection = 0
        FromSelected = 1
    

class RibbonBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Angle: Expression
    AngleTolerance: float
    DistanceTolerance: float
    OffsetDistance: Expression
    OffsetView: Direction
    Profile: Section
    ReverseOffset: bool


class Ribbon(Features.BodyFeature):
    def __init__(self) -> None: ...


class Rib(Features.BodyFeature):
    def __init__(self) -> None: ...


class RevolveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetStartLimitHelperPoint(self, startHelperPoint: float) -> None:
        ...
    def SetEndLimitHelperPoint(self, endHelperPoint: float) -> None:
        ...
    Axis: Axis
    BooleanOperation: GeometricUtilities.BooleanOperation
    FeatureOptions: GeometricUtilities.FeatureOptions
    Limits: GeometricUtilities.Limits
    Offset: GeometricUtilities.FeatureOffset
    Section: Section
    SmartVolumeProfile: GeometricUtilities.SmartVolumeProfileBuilder
    Tolerance: float


class Revolve(Features.BodyFeature):
    def __init__(self) -> None: ...


class ResizePlaneBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetCornerPoints(self, cornerPoints: typing.List[Point3d]) -> None:
        ...
    def GetCornerPoints(self, cornerPoints: typing.List[Point3d]) -> None:
        ...
    Plane: SelectDatumPlane
    ResizeDuringUpdate: bool


class ResizePlane(Features.Feature):
    def __init__(self) -> None: ...


class ResizeNeutralFactor(Features.Feature):
    def __init__(self) -> None: ...


class ResizeFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Angle: Expression
    BlendFace: ModlDirect.SelectBlend
    Diameter: Expression
    Face: SelectFaceList


class ResizeFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class ResizeCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CurveFinder: Features.CurveFinderBuilder
    DistanceTolerance: float
    KeepOrthogonal: bool
    Value: Expression
    ValueOption: Features.ResizeCurveBuilder.ValueType


    class ValueType(enum.Enum):
        Diameter = 0
        Radius = 1
    

class ResizeCurve(Features.BodyFeature):
    def __init__(self) -> None: ...


class ResizeChamferCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DistanceValue: float
    Section: ScCollector


class ResizeChamferCurve(Features.BodyFeature):
    def __init__(self) -> None: ...


class ResizeChamferBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Angle: Expression
    ChamferType: Features.ResizeChamferBuilder.SectionType
    Faces: ScCollector
    FlipChamferOffsets: bool
    Offset1: Expression
    Offset2: Expression


    class SectionType(enum.Enum):
        SymmetricOffset = 0
        AsymmetricOffset = 1
        OffsetandAngle = 2
    

class ResizeChamfer(Features.BodyFeature):
    def __init__(self) -> None: ...


class ResizeBlendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetBlendFaceRadius(self, blendFace: Face) -> float:
        ...
    BlendFace: ScCollector
    Radius: Expression


class ResizeBlend(Features.BodyFeature):
    def __init__(self) -> None: ...


class ResizeBendRadius(Features.Feature):
    def __init__(self) -> None: ...


class ResizeBendAngle(Features.Feature):
    def __init__(self) -> None: ...


class ReplaceFeatureBuilder(Builder):
    def __init__(self) -> None: ...
    def SetMatchingForIndex(self, indices: int, matchingTag: NXObject) -> None:
        ...
    def SetMatchingForParent(self, parentTag: NXObject, matchingTag: NXObject) -> None:
        ...
    def UpdateMap(self) -> None:
        ...
    def AutomatchMap(self) -> None:
        ...
    CopyReplacementFeature: bool
    DeleteOriginalFeature: bool
    DisplayUniqueInputsToMap: bool
    DoAutomaticGeomMatch: bool
    FeatureReferences: Features.FeatureReferencesBuilder
    IsMappingToleranceIncreased: bool
    KeepFeatureToReplace: bool
    MappingMethod: Features.ReplaceFeatureBuilder.MappingMethodType
    MappingTolerance: float
    ReplacementFeature: Features.SelectFeatureList
    SelectFeature: Features.SelectFeatureList


    class MappingMethodType(enum.Enum):
        MapOnlyObjectsWithModelingDependencies = 0
        MapAllObjects = 1
    

class ReplaceFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ResetReplaceFaceMethod(self) -> None:
        ...
    def ResetFreeEdgeProjectionOption(self) -> None:
        ...
    BlendFace: ModlDirect.SelectBlend
    FaceChangeOverflowBehavior: GeometricUtilities.FaceChangeOverflowBehavior
    FaceToReplace: ScCollector
    FaceToSimplify: SelectFaceList
    FreeEdgeProjection: GeometricUtilities.ProjectionOptions
    OffsetDistance: Expression
    OffsetReverseDirection: bool
    ReplaceFaces: ScCollector
    ReplacementFace: SelectFace
    ReplacementFaces: ScCollector
    ReverseDirection: bool
    Type: Features.ReplaceFaceBuilder.ReplaceTypes


    class ReplaceTypes(enum.Enum):
        Replace = 0
        Simplify = 1
    

class ReplaceFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class ReplaceBlendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ControlRadius: Expression
    FaceToReblend: ScCollector
    InheritRadiusFromFace: bool
    ShapeMatch: int


class ReplaceBlend(Features.BodyFeature):
    def __init__(self) -> None: ...


class ReorderBlendsBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetBlendface2Candidate(self, blendFace1: Face) -> Face:
        ...
    BlendFace1: ScCollector
    BlendFace2: ScCollector


class ReorderBlends(Features.BodyFeature):
    def __init__(self) -> None: ...


class RemoveParametersBuilder(Builder):
    def __init__(self) -> None: ...
    Objects: SelectNXObjectList


class RegionListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.RegionListItemBuilder]) -> None:
        ...
    def Append(self, object: Features.RegionListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.RegionListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.RegionListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.RegionListItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.RegionListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.RegionListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.RegionListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.RegionListItemBuilder, object2: Features.RegionListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.RegionListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class RegionListItemBuilder(Builder):
    def __init__(self) -> None: ...
    OffsetDistance: Expression
    Region: RegionPointList
    RegionType: int


    class Type(enum.Enum):
        Offset = 0
        Bridge = 1
    

class RefitFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ConstraintUMax: GeometricUtilities.Continuity
    ConstraintUMin: GeometricUtilities.Continuity
    ConstraintVMax: GeometricUtilities.Continuity
    ConstraintVMin: GeometricUtilities.Continuity
    Face: SelectTaggedObject
    FitDirection: Direction
    HasFitDirection: bool
    IsCreateCopy: bool
    MaxCheckingDist: float
    ModificationPercent: int
    RefitControl: GeometricUtilities.RefitControlBuilder
    SmoothFactor: int
    Targets: SelectTaggedObjectList
    Type: Features.RefitFaceBuilder.Types
    UseConstraintsAll: bool


    class Types(enum.Enum):
        Refit = 0
        FitToTarget = 1
    

class RefitFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class ReferenceMapperBuilder(Builder):
    def __init__(self) -> None: ...
    FeatureReferences: Features.FeatureReferencesBuilder


class Rebend(Features.Feature):
    def __init__(self) -> None: ...


class RasterImage(Features.Feature):
    def __init__(self) -> None: ...
    def Update(self, origin: Point3d, matrix: Matrix3x3, length: float, height: float, imageFileName: str, translucency: float, maximumTextureSize: Features.RasterImage.MaxTextureSize) -> None:
        ...
    Height: float
    ImageFileName: str
    Length: float
    Matrix: Matrix3x3
    MaximumTextureSize: Features.RasterImage.MaxTextureSize
    Origin: Point3d
    Translucency: float


    class MaxTextureSize(enum.Enum):
        N512 = 0
        N1024 = 1
        N2048 = 2
        N4096 = 3
        N8192 = 4
        N16384 = 5
        N32768 = 6
    

class RapidSurfaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def AcceptNewFacetBody(self) -> None:
        ...
    def ImportCurve(self) -> None:
        ...
    def AcceptSubdivision(self) -> None:
        ...
    def SetNumberOfDefiningPoints(self, number: int) -> None:
        ...
    def SetDefiningPoint(self, index: int, coordination: Point3d, facetID: int) -> None:
        ...
    def SetNumberOfDefinePoints(self, number: int) -> None:
        """[Obsolete("Deprecated in NX6.0.0.  Use NXOpen.Features.RapidSurfaceBuilder.SetNumberOfDefiningPoints instead.")"""
        ...
    def SetADefinePoint(self, index: int, xx: float, yy: float, zz: float, facetID: int) -> None:
        """[Obsolete("Deprecated in NX6.0.0.  Use NXOpen.Features.RapidSurfaceBuilder.SetDefiningPoint instead.")"""
        ...
    def ResetAnimationPolyline(self) -> None:
        ...
    def CreateAnimationPolyline(self) -> None:
        ...
    def CreateBoundaryCurve(self) -> None:
        ...
    def DrawCurve(self) -> None:
        ...
    def DrawBoundaryCurve(self) -> None:
        ...
    def DeleteCurve(self) -> None:
        ...
    def DeleteNode(self, point: Point) -> None:
        ...
    def DragCurvePoint(self) -> None:
        ...
    def MoveNode(self, point: Point, newPosition: Point3d) -> None:
        ...
    def ReprojectEdgesAfterMoveNode(self) -> None:
        ...
    def CreateNodePoints(self) -> typing.List[Point]:
        ...
    def AskEdgeCount(self) -> int:
        ...
    def AskEdge(self, edgeIndex: int) -> Spline:
        ...
    def GetNodeCount(self) -> int:
        ...
    def GetNode(self, nodeIndex: int) -> Point:
        ...
    def ConnectCurve(self) -> None:
        ...
    AttachmentType: Features.RapidSurfaceBuilder.AttachmentTypes
    Body: SelectDisplayableObject
    BoundaryPointSetManager: Features.GeometricConstraintDataSetManager
    ConnectCurves: SelectCurveList
    ConstraintSetManager: Features.GeometricConstraintDataSetManager
    Degree: int
    DeleteCurves: SelectCurveList
    DragCurve: SelectCurve
    DragCurvePointManager: Features.GeometricConstraintDataSetManager
    FacetBody: Facet.SelectFacetedBody
    ImportCurves: SelectCurveList
    LoopType: Features.RapidSurfaceBuilder.LoopTypes
    NodeTolerance: float
    OperationType: Features.RapidSurfaceBuilder.OperationTypes
    ProjectDirection: Direction
    Segments: int
    Smoothness: int
    ULoopCurve: SelectCurve
    UPatches: int
    VLoopCurve: SelectCurve
    VPatches: int


    class OperationTypes(enum.Enum):
        DrawOnFacetBody = 0
        DrawOnBoundary = 1
        ImportCurves = 2
        SubdivideLoop = 3
    

    class LoopTypes(enum.Enum):
        FourSided = 0
        ThreeSided = 1
    

    class AttachmentTypes(enum.Enum):
        FacetBody = 0
        None = 1
    

class RapidSurface(Features.Feature):
    def __init__(self) -> None: ...


class RadialDimensionBuilder(Features.DimensionBuilder):
    def __init__(self) -> None: ...
    DimensionPlane: GeometricUtilities.OrientXpressBuilder
    PickPoint: Point3d
    RadiusDiameterOption: Features.RadialDimensionBuilder.ValueOption


    class ValueOption(enum.Enum):
        Radius = 0
        Diameter = 1
    

class RadialDimension(Features.BodyFeature):
    def __init__(self) -> None: ...


class QuickBinder(Features.BodyFeature):
    def __init__(self) -> None: ...


class PullFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FaceToPull: ScCollector
    Motion: GeometricUtilities.ModlMotion


class PullFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class PromotionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    Body: SelectBodyList
    ConvertToLinkedBody: bool
    FaceDirection: bool


class Promotion(Features.BodyFeature):
    def __init__(self) -> None: ...


class ProjectCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleToProjectionVector: Expression
    BridgedGapSize: float
    CurveFitData: GeometricUtilities.CurveFitData
    CurveFitJoinData: GeometricUtilities.CurveFitJoin
    EqualArcLengthMethod: Features.ProjectCurveBuilder.ArcLengthType
    FaceToProjectTo: SelectObjectList
    GapOption: bool
    InputCurvesOption: GeometricUtilities.CurveOptions
    LineToProjectToward: SelectDisplayableObject
    NearestPointOption: bool
    PlaneToProjectTo: Plane
    PointToProjectToward: Point
    ProjectionDirectionMethod: Features.ProjectCurveBuilder.DirectionType
    ProjectionOption: Features.ProjectCurveBuilder.ProjectionOptionType
    ProjectionVector: Direction
    ReferencePointForEqualArcLength: Point
    SectionToProject: Section
    Tolerance: float
    XVectorForEqualArcLength: Direction


    class ProjectionOptionType(enum.Enum):
        None = 0
        ProjectBothSides = 1
        EqualArcLength = 2
    

    class DirectionType(enum.Enum):
        AlongFaceNormal = 0
        TowardPoint = 1
        TowardLine = 2
        AlongVector = 3
        AngleToVector = 4
    

    class ArcLengthType(enum.Enum):
        BothXY = 0
        FirstXThenY = 1
        FirstYThenX = 2
        XOnly = 3
        YOnly = 4
    

class ProjectCurve(Features.CurveFeature):
    def __init__(self) -> None: ...


class PrintCsysFeatureCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def CreatePrintCsysBuilder(self, printCsys: Features.Feature) -> Features.PrintCsysBuilder:
        ...
    def Tag(self) -> Tag: ...



class PrintCsysBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Bodies: ScCollector
    CoordinateSystem: CoordinateSystem
    Freedom: Features.PrintCsysBuilder.FreedomType
    MaxAngle: float
    Type: Features.PrintCsysBuilder.Types


    class Types(enum.Enum):
        UserDefined = 0
        MinimumHeight = 1
    

    class FreedomType(enum.Enum):
        Free = 0
        FixZDirection = 1
        FixBottomPlane = 2
        Rotate180 = 3
        FixBottomandXY = 4
        FixRotation = 5
        Fixed = 6
    

class Prebend(Features.Feature):
    def __init__(self) -> None: ...


class PolylineBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def EditPolyline(self, polyline: NXObject) -> None:
        ...
    def InsertPoint(self, afterIndex: int) -> None:
        ...
    def Evaluate(self) -> None:
        ...
    def UpdateOnConstraintPlane(self) -> None:
        ...
    CanUseOrientationTool: bool
    ConstraintManager: Features.GeometricConstraintDataManager
    ConstraintPlane: CoordinateSystem
    DrawingPlane: Plane
    DrawingPlaneOption: Features.PolylineBuilder.DrawingPlaneOptions
    HasPlaneConstraint: bool
    IsPeriodic: bool
    MovementMethod: Features.PolylineBuilder.MovementMethodType
    MovementPlane: Plane
    MovementVector: Direction
    Transformer: GeometricUtilities.TransformerData
    WCSOption: Features.PolylineBuilder.WCSOptionType


    class WCSOptionType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        YZ = 3
        XZ = 4
        XY = 5
    

    class MovementMethodType(enum.Enum):
        WCS = 0
        View = 1
        Vector = 2
        Plane = 3
        Segment = 4
    

    class DrawingPlaneOptions(enum.Enum):
        View = 0
        XY = 1
        YZ = 2
        XZ = 3
        General = 4
    

class PoleSmoothingBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetSelectedPolesIndex(self, selectedPolesIndex: int) -> None:
        ...
    def SetSelectedPolesIndex(self, selectedPolesIndex: int) -> None:
        ...
    def GetCreateNewCopy(self) -> bool:
        ...
    def SetCreateNewCopy(self, createNewCopy: bool) -> None:
        ...
    def RemoveFeatureParameters(self, face: Face) -> None:
        ...
    ApplyConstraintsToAll: bool
    ModificationPercentage: int
    MoveOnlySelectedPoles: bool
    MovementVector: Direction
    NumberPolesSelected: int
    Poles: GeometricUtilities.ControlPoleManagerData
    SmoothingFactor: int
    TargetFace: SelectFace
    UMaxConstraint: GeometricUtilities.Continuity
    UMinConstraint: GeometricUtilities.Continuity
    UseSpecificDirection: bool
    VMaxConstraint: GeometricUtilities.Continuity
    VMinConstraint: GeometricUtilities.Continuity


class PoleSmoothing(Features.BodyFeature):
    def __init__(self) -> None: ...


class PointSetFacePercentageBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.PointSetFacePercentageBuilder]) -> None:
        ...
    def Append(self, object: Features.PointSetFacePercentageBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.PointSetFacePercentageBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.PointSetFacePercentageBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.PointSetFacePercentageBuilder) -> None:
        ...
    def Erase(self, obj: Features.PointSetFacePercentageBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.PointSetFacePercentageBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.PointSetFacePercentageBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.PointSetFacePercentageBuilder, object2: Features.PointSetFacePercentageBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.PointSetFacePercentageBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PointSetFacePercentageBuilder(NXObject):
    def __init__(self) -> None: ...
    UPercentage: Expression
    VPercentage: Expression


class PointSetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateFacePercentageListItem(self) -> Features.PointSetFacePercentageBuilder:
        ...
    AngleTolerance: float
    ArcLength: Expression
    Associative: bool
    ChordalTolerance: Expression
    CurvePercentageList: NXObjectList
    CurvePointsBy: Features.PointSetBuilder.CurvePointsType
    DistanceTolerance: float
    EndPercentage: Expression
    EndPercentageSection: Section
    FacePercentageList: Features.PointSetFacePercentageBuilderList
    FacePointsBy: Features.PointSetBuilder.FacePointsType
    GroupPoints: bool
    IntersectionSection: Section
    IntersectionSelectedObjects: SelectDisplayableObjectList
    IntersectionSelectedObjectsSecond: SelectDisplayableObjectList
    MultipleCurveOrEdgeCollector: Section
    MultipleFaceCollector: ScCollector
    NumberOfPointsExpression: Expression
    NumberOfPointsInUDirectionExpression: Expression
    NumberOfPointsInVDirectionExpression: Expression
    PatternLimitsBy: Features.PointSetBuilder.PatternLimitsType
    PatternLimitsEndPoint: Point
    PatternLimitsEndingUValue: Expression
    PatternLimitsEndingVValue: Expression
    PatternLimitsStartPoint: Point
    PatternLimitsStartingUValue: Expression
    PatternLimitsStartingVValue: Expression
    ProjectionPointList: PointList
    Ratio: Expression
    SingleCurveOrEdgeCollector: Section
    SingleFaceObject: SelectFace
    SplineCollector: ScCollector
    SplinePointsBy: Features.PointSetBuilder.SplinePointsType
    StartPercentage: Expression
    StartPercentageSection: Section
    Type: Features.PointSetBuilder.Types


    class Types(enum.Enum):
        CurvePoints = 0
        SplinePoints = 1
        FacePoints = 2
        IntersectionPoints = 3
    

    class SplinePointsType(enum.Enum):
        DefiningPoints = 0
        Knots = 1
        Poles = 2
    

    class PatternLimitsType(enum.Enum):
        DiagonalPoints = 0
        Percentages = 1
    

    class FacePointsType(enum.Enum):
        Pattern = 0
        FacePercentage = 1
        BSurfacePoles = 2
    

    class CurvePointsType(enum.Enum):
        EqualArcLength = 0
        EqualParameters = 1
        GeometricProgression = 2
        ChordalTolerance = 3
        IncrementalArcLength = 4
        SpecifiedProjectionPoints = 5
        CurvePercentage = 6
    

class PointSet(Features.CurveFeature):
    def __init__(self) -> None: ...
    def GetPoints(self) -> typing.List[Point]:
        ...


class PointFeatureBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Point: Point


class PointFeature(Features.Feature):
    def __init__(self) -> None: ...


class PierceTask(Features.BodyFeature):
    def __init__(self) -> None: ...


class PerpendicularBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FaceChangeOverflowBehavior: GeometricUtilities.FaceChangeOverflowBehavior
    MotionFace: SelectFace
    MoveAlongFace: Features.FaceRecognitionBuilder
    StationaryFace: SelectISurface
    ThroughPoint: Point


class Perpendicular(Features.BodyFeature):
    def __init__(self) -> None: ...


class PatternGeometryBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CopyThreads: bool
    GeometryToPattern: SelectDisplayableObjectList
    HideOriginal: bool
    IsAssociative: bool
    PatternService: GeometricUtilities.PatternDefinition
    ReferencePoint: GeometricUtilities.PatternReferencePointServiceBuilder


class PatternGeometry(Features.Feature):
    def __init__(self) -> None: ...
    def GetImmediateContainedFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetAllContainedFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetAssociatedBodies(self) -> typing.List[Body]:
        ...
    def GetAssociatedFaces(self) -> typing.List[Face]:
        ...
    def GetAssociatedEdges(self) -> typing.List[Edge]:
        ...
    def GetAssociatedCurvesPointsDatums(self) -> typing.List[DisplayableObject]:
        ...


class PatternFeatureBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetReferencesToReuse(self, inputFeature: Features.Feature, referencesFromInputFeatures: typing.List[NXObject]) -> None:
        ...
    def ClearReferencesToReuse(self) -> None:
        ...
    def RemoveAllClocking(self) -> None:
        ...
    CreateReferencePattern: bool
    ExpressionOption: Features.PatternFeatureBuilder.ExpressionTransferOptions
    FeatureList: Features.SelectFeatureList
    OutputOption: Features.PatternFeatureBuilder.OutputOptions
    PatternMethod: Features.PatternFeatureBuilder.PatternMethodOptions
    PatternService: GeometricUtilities.PatternDefinition
    ReferencePoint: Point
    ReferencePointService: GeometricUtilities.PatternReferencePointServiceBuilder
    UseInferredReferencePoint: bool


    class PatternMethodOptions(enum.Enum):
        Variational = 1
        Simple = 2
    

    class OutputOptions(enum.Enum):
        PatternFeature = 0
        CopiesOfInputFeatures = 1
        CopiesOfInputFeaturesInGroup = 2
    

    class ExpressionTransferOptions(enum.Enum):
        CreateNew = 0
        LinkToOriginal = 1
        OriginalInstance = 2
    

class PatternFeature(Features.Feature):
    def __init__(self) -> None: ...
    def GetImmediateContainedFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetAllContainedFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetAssociatedBodies(self) -> typing.List[Body]:
        ...
    def GetAssociatedFaces(self) -> typing.List[Face]:
        ...
    def GetAssociatedEdges(self) -> typing.List[Edge]:
        ...
    def GetAssociatedCurvesPointsDatums(self) -> typing.List[DisplayableObject]:
        ...


class PatternFaceFeatureBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CopyChamferLabels: bool
    FaceCollector: ScCollector
    PatternDefinition: GeometricUtilities.PatternDefinition
    ReferencePoint: GeometricUtilities.PatternReferencePointServiceBuilder


class PatternFaceFeature(Features.BodyFeature):
    def __init__(self) -> None: ...


class PatternFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Angle: Expression
    Axis: Axis
    CircularCount: Expression
    Face: ScCollector
    Plane: SelectTaggedObject
    RestoreOption: bool
    Type: Features.PatternFaceBuilder.PatternTypes
    XCount: Expression
    XDistance: Expression
    XVector: Direction
    YCount: Expression
    YDistance: Expression
    YVector: Direction


    class PatternTypes(enum.Enum):
        Rectangular = 0
        Circular = 1
        Mirror = 2
    

class PatternFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class PatchOpeningsBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def FindOpenings(self, filterNoise: bool) -> None:
        ...
    def CreatePathFromOpening(self, objectArray: typing.List[NXObject], path: NXObject) -> None:
        ...
    CutoutLength: Expression
    CutoutRadius: Expression
    Distance: Expression
    DistanceTolerance: float
    DividingCurves: ScCollector
    Faces: ScCollector
    Limits: Die.DieLimitsBuilder
    Openings: ScCollector
    Output: Features.PatchOpeningsBuilder.OutputTypes
    ShelfLength: Expression
    ShelfPoint1: Point
    ShelfPoint2: Point
    ShelfRadius: Expression
    Type: Features.PatchOpeningsBuilder.Types


    class Types(enum.Enum):
        Quilted = 0
        NSided = 1
        Mesh = 2
        ByDeletingEdges = 3
        Extension = 4
        Notch = 5
        Joggle = 6
        MoldWizard = 7
        BySuppression = 8
    

    class OutputTypes(enum.Enum):
        SingleFeature = 0
        MultipleFeatures = 1
        Sew = 2
    

class PatchOpenings(Features.BodyFeature):
    def __init__(self) -> None: ...


class PatchBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CreateHolePatch: bool
    ReverseDirection: bool
    SeedFace: SelectFace
    Target: SelectBody
    Tolerance: float
    Tool: SelectDisplayableObject


class Patch(Features.CombineBodyFeature):
    def __init__(self) -> None: ...


class PasteFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    PasteOption: Features.PasteFaceBuilder.PasteOptionType
    ReverseTarget: bool
    ReverseTool: bool
    TargetBody: SelectBody
    ToolBody: SelectBodyList


    class PasteOptionType(enum.Enum):
        Automatic = 0
        Add = 1
        Subtract = 2
    

class PasteFace(Features.CombineBodyFeature):
    def __init__(self) -> None: ...


class PartModuleBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ActivatePartModule: bool
    InputReferences: GeometricUtilities.PartModuleReferencesBuilder
    IsDesignGroup: bool
    Name: str
    Name1: str
    ShowOnlyPartModule: bool


class PartModule(Features.Feature):
    def __init__(self) -> None: ...
    def CreateLinkedPartModule(self, createdPart: Part) -> Features.Feature:
        ...
    def CreatePartModuleOutputBuilder(self) -> GeometricUtilities.PartModuleOutputBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Please use NXOpen.Features.PartModule.CreatePartModuleOutputBuilder1 instead.")"""
        ...
    def ShowOnly(self) -> None:
        ...
    def UpdateInputReferences(self) -> None:
        ...
    def LoadInterpartData(self) -> None:
        ...
    def UpdateOutputReferences(self) -> None:
        ...
    def Activate(self, active: bool) -> None:
        ...
    def MakeLinkedWork(self) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Please use NXOpen.Features.PartModule.DisplayLinkedPart instead.")"""
        ...
    def MakeMainWork(self) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Please use NXOpen.Features.PartModule.DisplayMainPart instead.")"""
        ...
    def Merge(self) -> None:
        ...
    def BreakRelationship(self) -> None:
        ...
    def CreatePartModuleInputBuilder(self) -> GeometricUtilities.PartModuleInputBuilder:
        ...
    def CreatePartModuleOutputBuilder1(self) -> GeometricUtilities.PartModuleOutputBuilder1:
        ...
    def ProcessDeletePartModule(self) -> None:
        ...
    def DisplayMainPart(self) -> None:
        ...
    def DisplayLinkedPart(self) -> None:
        ...
    def LoadPartWithOption(self, partLoadOption: int) -> Part:
        ...
    def DisplayMainPartInNewWindow(self) -> None:
        ...
    def DisplayLinkedPartInNewWindow(self) -> None:
        ...
    AllowDeleteMembers: bool


    class PartLoadOption(enum.Enum):
        DontAllowSave = 1
        LoadInterpart = 2
    

class PartGeometryCopySelectBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.PartGeometryCopySelectBuilder]) -> None:
        ...
    def Append(self, object: Features.PartGeometryCopySelectBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.PartGeometryCopySelectBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.PartGeometryCopySelectBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.PartGeometryCopySelectBuilder) -> None:
        ...
    def Erase(self, obj: Features.PartGeometryCopySelectBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.PartGeometryCopySelectBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.PartGeometryCopySelectBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.PartGeometryCopySelectBuilder, object2: Features.PartGeometryCopySelectBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.PartGeometryCopySelectBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PartGeometryCopySelectBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetRelatedExpressions(self) -> typing.List[NXObject]:
        ...
    def SetRelatedExpressions(self, relatedExps: typing.List[NXObject]) -> None:
        ...
    def RemoveAllRelatedExpressions(self) -> None:
        ...
    def RemoveRelatedExpression(self, relatedExps: NXObject) -> None:
        ...
    BodyCollector: ScCollector
    BodyObject: SelectTaggedObject
    CompositeCurve: Section
    CompositeFace: ScCollector
    CurrentInterfaceUsageType: int
    CurrentInterfaceUsageTypeString: str
    CurrentObjectType: int
    Curve: SelectDisplayableObject
    CurveFeature: Features.SelectFeature
    Datum: SelectTaggedObject
    Expression: Expression
    Face: SelectFace
    ObjectDescription: str
    ObjectName: str
    ObjectType: str
    Pmi: SelectDisplayableObject
    Point: SelectTaggedObject
    ReverseDirection: bool
    RoutingObject: SelectDisplayableObject
    Sketch: SelectSketch


class PartGeometryCopyBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateSelectionBuilder(self, objectType: Features.PartGeometryCopyBuilder.Type) -> Features.PartGeometryCopySelectBuilder:
        ...
    InterfaceUsageType: int
    ObjectList: Features.PartGeometryCopySelectBuilderList
    ObjectType: Features.PartGeometryCopyBuilder.Type


    class Type(enum.Enum):
        Automatic = 0
        BodyCollector = 1
        BodyObject = 2
        CurveFeature = 3
        Sketch = 4
        Datum = 5
        Point = 6
        CompositeCurve = 7
        CompositeFace = 8
        Expression = 9
        Pmi = 10
        Curve = 11
        Face = 12
        RoutingObject = 13
    

class ParallelBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FaceChangeOverflowBehavior: GeometricUtilities.FaceChangeOverflowBehavior
    MotionFace: SelectFace
    MoveAlongFace: Features.FaceRecognitionBuilder
    StationaryFace: SelectISurface
    ThroughPoint: Point


class Parallel(Features.BodyFeature):
    def __init__(self) -> None: ...


class PaintParametersBuilder(Builder):
    def __init__(self) -> None: ...
    def IsSourcePaintableObjectContainer(self, containerObj: NXObject) -> bool:
        ...
    def GetCompatibleTargetObjectContainers(self, sourceContainer: NXObject, targetObjTag: NXObject) -> typing.List[NXObject]:
        ...
    SourceFeature: Features.SelectFeature
    SourceObject: SelectTaggedObject
    TargetComponentSelection: bool
    TargetComponents: Assemblies.SelectComponentList
    TargetFeatures: Features.SelectFeatureList
    TargetObjects: SelectTaggedObjectList


class OvercrownBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def InitData(self) -> None:
        ...
    def SetTargetFaces(self, faces: typing.List[NXObject]) -> None:
        ...
    def SetCenterPoint(self) -> None:
        ...
    def SetDefaultDirection(self) -> None:
        ...
    def GetTargetFaces(self) -> typing.List[NXObject]:
        ...
    AngularTolerance: float
    BaseSurface: Body
    BoundarySection: Section
    ControlSurface: Body
    Direction: Direction
    DistanceTolerance: float
    Height: str
    OperatorControlType: Features.OvercrownBuilder.ControlType
    OperatorOperationType: Features.OvercrownBuilder.OperationType
    OperatorOutputType: Features.OvercrownBuilder.OutputType
    OperatorTransitionType: Features.OvercrownBuilder.TransitionType
    PointInFormingRegion: NXObject
    ReverseNormal: int
    ShapeControl: float
    StretchDirection: Direction


    class TransitionType(enum.Enum):
        Curve1 = 0
        Curve2 = 1
        LawCurve = 2
    

    class OutputType(enum.Enum):
        Sheet = 0
        Solid = 1
    

    class OperationType(enum.Enum):
        Overcrown = 0
        Stretch = 1
        Offset = 2
    

    class ControlType(enum.Enum):
        ByFunction = 0
        BySurface = 1
    

class OutputFeatureData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFeature(self) -> Features.Feature:
        ...
    ShowInGraphicView: bool


class OptimizeFaceBuilder(Builder):
    def __init__(self) -> None: ...
    CleanBody: bool
    DistanceTolerance: float
    FacesToOptimize: ScCollector
    Report: bool


class OptimizeFace(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...


class OptimizeCurveBuilder(Builder):
    def __init__(self) -> None: ...
    AngleThreshold: float
    CreateSketch: bool
    CurvesToOptimize: SelectDisplayableObjectList
    DestinationCsys: CoordinateSystem
    DistanceThreshold: float
    IncludePoints: bool


class OffsetSurfaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetOrientationMethod(self, orientationMethod: Features.OffsetSurfaceBuilder.OrientationMethodType) -> None:
        ...
    def GetOrientationMethod(self) -> Features.OffsetSurfaceBuilder.OrientationMethodType:
        ...
    def SetInteriorPosition(self, point: Point3d) -> None:
        ...
    def GetInteriorPosition(self) -> Point3d:
        ...
    def GetFaceSetList(self) -> ObjectList:
        """[Obsolete("Deprecated in NX5.0.0.  Use NXOpen.Features.OffsetSurfaceBuilder.FaceSets instead.")"""
        ...
    def GetFaceSets(self) -> typing.List[GeometricUtilities.FaceSetOffset]:
        """[Obsolete("Deprecated in NX5.0.0.  Use NXOpen.Features.OffsetSurfaceBuilder.FaceSets instead.")"""
        ...
    def DeleteFaceSet(self, index: int) -> None:
        """[Obsolete("Deprecated in NX5.0.0.  Use NXOpen.Features.OffsetSurfaceBuilder.FaceSets instead.")"""
        ...
    def FindFaceSet(self, index: int) -> GeometricUtilities.FaceSetOffset:
        """[Obsolete("Deprecated in NX5.0.0.  Use NXOpen.Features.OffsetSurfaceBuilder.FaceSets instead.")"""
        ...
    def AddFaceSets(self, faceSets: typing.List[GeometricUtilities.FaceSetOffset]) -> None:
        """[Obsolete("Deprecated in NX5.0.0.  Use NXOpen.Features.OffsetSurfaceBuilder.FaceSets instead.")"""
        ...
    ApproxOption: bool
    FaceSets: GeometricUtilities.FaceSetOffsetList
    MaximumExcludedObjects: int
    OutputOption: Features.OffsetSurfaceBuilder.OutputOptionType
    PartialOption: bool
    Radius: Expression
    RemoveProblemVerticesOption: bool
    StepOption: bool
    Tolerance: float


    class OutputOptionType(enum.Enum):
        OneFeatureForConnectedFaces = 0
        OneFeatureForEachFace = 1
        OneFeatureForAllFaces = 2
    

    class OrientationMethodType(enum.Enum):
        UseExistingNormals = 0
        SpecifyInteriorPosition = 1
    

class OffsetSurface(Features.BodyFeature):
    def __init__(self) -> None: ...


class OffsetRegionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BlendFace: ModlDirect.SelectBlend
    Distance: Expression
    Face: ScCollector
    ReverseDirection: bool


class OffsetRegion(Features.BodyFeature):
    def __init__(self) -> None: ...


class OffsetMoveCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ReverseOffsetDirectionOfLoop(self, objectInLoop: NXObject) -> None:
        ...
    def AddCurveSenseToMap(self, curve: NXObject, curveSense: int) -> None:
        ...
    def RemoveCurveSenseFromMap(self, curve: NXObject) -> None:
        ...
    CurveFinder: Features.CurveFinderBuilder
    Distance: Expression
    DistanceTolerance: float
    KeepOrthogonal: bool
    KeepTangent: int
    ReverseOffsetDirection: bool


class OffsetMoveCurve(Features.BodyFeature):
    def __init__(self) -> None: ...


class OffsetFacetBodyBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetAllBoundaries(self) -> typing.List[Spline]:
        ...
    Boundaries: ScCollector
    Distance: Expression
    FacetBody: Facet.SelectFacetedBody
    ReverseDirection: bool
    Tolerance: float


class OffsetFacetBody(Features.BodyFeature):
    def __init__(self) -> None: ...


class OffsetFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Direction: bool
    Distance: Expression
    FaceCollector: ScCollector


class OffsetFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class OffsetEmbossBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    BottomDistance: Expression
    CenterLine: Section
    CenterPoint: Point
    DistanceTolerance: float
    HeightOffset: Expression
    LeftWidth: Expression
    ReverseDirection: bool
    RightWidth: Expression
    SideOffset: Expression
    Target: ScCollector
    TopDistance: Expression
    Type: Features.OffsetEmbossBuilder.Types


    class Types(enum.Enum):
        Curve = 0
        Point = 1
    

class OffsetEmboss(Features.BodyFeature):
    def __init__(self) -> None: ...


class OffsetEdgeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Distance: Expression
    EdgeToOffset: ScCollector
    EndFaceBehavior: Features.OffsetEdgeBuilder.EndFaceBehaviourType
    Method: Features.OffsetEdgeBuilder.OffsetEdgeMethod
    ReverseOffsetDirection: bool
    ReverseOffsetSide: bool


    class OffsetEdgeMethod(enum.Enum):
        AlongFace = 0
        AlongPlaneofEdge = 1
    

    class EndFaceBehaviourType(enum.Enum):
        Extend = 0
        Morph = 1
    

class OffsetEdge(Features.BodyFeature):
    def __init__(self) -> None: ...


class OffsetCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ComputeOffsetDirection(self, offsetDirection: Vector3d, startPoint: Point3d) -> None:
        ...
    def ComputeOffsetDirection(self, seedEntity: ICurve, seedPoint: Point3d, offsetDirection: Vector3d, startPoint: Point3d) -> None:
        ...
    AxialOffsetDirection: Direction
    CurveFitData: GeometricUtilities.CurveFitData
    CurveFitMethod: GeometricUtilities.CurveFitOptions
    CurvesToOffset: Section
    DraftAngle: Expression
    DraftHeight: Expression
    ExtendFactor: float
    GroupObjects: bool
    InputCurvesOptions: GeometricUtilities.CurveOptions
    LawControl: GeometricUtilities.LawBuilder
    NumberOfCopies: int
    Offset3dDistance: Expression
    OffsetDistance: Expression
    PointOnOffsetPlane: Point
    ReverseDirection: bool
    RoughOffset: bool
    Tolerance: float
    TrimMethod: Features.OffsetCurveBuilder.TrimOption
    Type: Features.OffsetCurveBuilder.Types


    class Types(enum.Enum):
        Distance = 0
        Draft = 1
        LawControl = 2
        Axial3d = 3
    

    class TrimOption(enum.Enum):
        None = 0
        ExtendTangents = 1
        Fillet = 2
    

class OffsetCurve(Features.CurveFeature):
    def __init__(self) -> None: ...


class Offset3DCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def FlipOffsetCurveDirection(self, inputCurve: ICurve, point: Point3d, reverseDirection: bool) -> None:
        ...
    Associative: bool
    CurveFitData: GeometricUtilities.CurveFitData
    OffsetCurves: Section
    OffsetDistance: Expression
    OffsetViewDirection: Direction
    ReverseSide: bool


class Offset3DCurve(Features.CurveFeature):
    def __init__(self) -> None: ...


class NSidedSurfaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CenterControlFlat: Expression
    CenterControlTiltX: Expression
    CenterControlTiltY: Expression
    CenterControlTrimFlat: Expression
    CenterControlX: Expression
    CenterControlY: Expression
    CenterControlZ: Expression
    ConstraintFaces: ScCollector
    Continuity: GeometricUtilities.Continuity
    CurvatureTolerance: float
    FlowDirection: Features.NSidedSurfaceBuilder.FlowDirectionType
    InteriorCurveList: SectionList
    MergeFaces: bool
    OrientationVector: Direction
    OuterLoop: Section
    PositionTolerance: float
    RectanglePointFirst: Point
    RectanglePointSecond: Point
    RectanglePointThird: Point
    SpineCurve: Section
    TangentTolerance: float
    TrimToBoundary: bool
    Type: Features.NSidedSurfaceBuilder.SurfaceType
    UVOrientation: Features.NSidedSurfaceBuilder.UVOrientationType


    class UVOrientationType(enum.Enum):
        Spine = 0
        Vector = 1
        Area = 2
    

    class SurfaceType(enum.Enum):
        TrimmedPatch = 0
        TriangularPatch = 1
    

    class FlowDirectionType(enum.Enum):
        NotSpecified = 0
        Perpendicular = 1
        IsoUVLine = 2
        AdjacentEdges = 3
    

    class CenterControlType(enum.Enum):
        Position = 0
        Tilting = 1
    

    class CenterControlAxisType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        Flat = 3
    

class NSidedSurface(Features.BodyFeature):
    def __init__(self) -> None: ...


class NormalCutout(Features.Feature):
    def __init__(self) -> None: ...


class MoveObjectBuilder(Builder):
    def __init__(self) -> None: ...
    Associative: bool
    CreateTraceLines: bool
    Divisions: int
    Layer: int
    LayerOption: Features.MoveObjectBuilder.LayerOptionType
    MoveObjectResult: Features.MoveObjectBuilder.MoveObjectResultOptions
    MoveParents: bool
    NumberOfCopies: int
    ObjectToMoveObject: SelectNXObjectList
    TransformMotion: GeometricUtilities.ModlMotion


    class MoveObjectResultOptions(enum.Enum):
        MoveOriginal = 0
        CopyOriginal = 1
    

    class LayerOptionType(enum.Enum):
        Original = 0
        Work = 1
        AsSpecified = 2
    

class MoveObject(Features.Feature):
    def __init__(self) -> None: ...


class MoveFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Angle: Expression
    Axis: Axis
    BlendFaces: ModlDirect.SelectBlend
    Copy: bool
    Direction: Direction
    Distance: Expression
    FromPoint: Point
    FromVector: Direction
    MoveFaceCollector: ScCollector
    PivotPoint: Point
    ToPoint: Point
    ToVector: Direction
    Type: Features.MoveFaceBuilder.Types


    class Types(enum.Enum):
        TranslateDirectionAndDistance = 0
        TranslateBetweenTwoPoints = 1
        RotateAboutAxis = 2
        RotateBetweenTwoAxes = 3
    

class MoveFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class MoveEdgeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    EdgeToMove: ScCollector
    EndFaceBehavior: Features.MoveEdgeBuilder.EndFaceBehaviorType
    Motion: GeometricUtilities.ModlMotion


    class EndFaceBehaviorType(enum.Enum):
        Extend = 0
        Morph = 1
    

class MoveEdge(Features.BodyFeature):
    def __init__(self) -> None: ...


class MoveCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CurveFinder: Features.CurveFinderBuilder
    DistanceTolerance: float
    KeepOrthogonal: bool
    KeepTangent: int
    SizeOption: int
    TransformMotion: GeometricUtilities.ModlMotion


class MoveCurve(Features.BodyFeature):
    def __init__(self) -> None: ...


class MirrorFeatureBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FeatureSet: Features.SelectFeatureList
    Plane: SelectISurface
    PlaneConstructor: Plane
    PlaneOption: Features.MirrorFeatureBuilder.PlaneOptions


    class PlaneOptions(enum.Enum):
        Existing = 0
        New = 1
    

class MirrorFeature(Features.BodyFeature):
    def __init__(self) -> None: ...


class MirrorFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ExistingMirrorPlane: SelectISurface
    FaceToMirror: Features.FaceRecognitionBuilder
    MirrorPlaneOption: Features.MirrorFaceBuilder.MirrorPlaneOptions
    NewMirrorPlane: Plane


    class MirrorPlaneOptions(enum.Enum):
        Existing = 0
        New = 1
    

class MirrorFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class MirrorCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Curve: Section
    ExistingPlane: SelectISurface
    InputCurvesOptions: GeometricUtilities.CurveOptions
    NewPlane: Plane
    PlaneOption: Features.MirrorCurveBuilder.PlaneOptions


    class PlaneOptions(enum.Enum):
        ExistingPlane = 0
        NewPlane = 1
    

class MirrorCurve(Features.Feature):
    def __init__(self) -> None: ...


class MirrorBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetReferencesToReuse(self, inputFeature: Features.Feature, referencesFromInputFeatures: typing.List[NXObject]) -> None:
        ...
    def ClearReferencesToReuse(self) -> None:
        ...
    CsysMirrorOption: Features.MirrorBuilder.CsysMirrorOptions
    FeatureList: Features.SelectFeatureList
    MaintainHelixHandedness: bool
    MaintainThreadHandedness: bool
    PatternService: GeometricUtilities.PatternDefinition
    ReferencePoint: Point
    ReferencePointService: GeometricUtilities.PatternReferencePointServiceBuilder
    UseInferredReferencePoint: bool


    class CsysMirrorOptions(enum.Enum):
        MirrorXAndY = 0
        MirrorYAndZ = 1
        MirrorZAndX = 2
    

class MirrorBodyBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetWaveLinkInformation(self, info: str, xformExists: bool, xformOrigin: Point3d, xformOrientation: Matrix3x3, xformScale: float) -> None:
        ...
    def GetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def SetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def GetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    def SetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    Associative: bool
    CopyThreads: bool
    FeatureOption: Features.MirrorBodyBuilder.FeatureOptionType
    FixAtCurrentTimestamp: bool
    FrecAtTimeStamp: Features.Feature
    InheritDisplayProperties: bool
    MakePositionIndependent: bool
    MirrorBodyCollector: ScCollector
    MirrorBodyList: SelectBodyList
    ParentPartType: Features.MirrorBodyBuilder.ParentPart
    Plane: SelectDatumPlane
    ReplacementAssistant: GeometricUtilities.ReplAsstBuilder
    ReverseDirection: bool
    SourcePartOccurrence: TaggedObject


    class ParentPart(enum.Enum):
        WorkPart = 0
        OtherPart = 1
    

    class FeatureOptionType(enum.Enum):
        OneFeatureForAllBodies = 0
        SeparateFeatureForEachBody = 1
    

class MirrorBody(Features.BodyFeature):
    def __init__(self) -> None: ...


class Mirror(Features.Feature):
    def __init__(self) -> None: ...
    def GetImmediateContainedFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetAllContainedFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetAssociatedBodies(self) -> typing.List[Body]:
        ...
    def GetAssociatedFaces(self) -> typing.List[Face]:
        ...
    def GetAssociatedEdges(self) -> typing.List[Edge]:
        ...
    def GetAssociatedCurvesPointsDatums(self) -> typing.List[DisplayableObject]:
        ...


class MidSurfaceUserDefinedBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    MaxThickness: Expression
    MinThickness: Expression
    OutsideThickness: Expression
    SheetBodySelection: SelectBodyList
    SolidBodySel: SelectBody


class MidSurfaceUserDefined(Features.BodyFeature):
    def __init__(self) -> None: ...


class MidSurfaceFacePair(Features.BodyFeature):
    def __init__(self) -> None: ...
    AverageThickness: float
    SheetBody: Body


class MidSurfaceByFacePairsBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def AutoPopulateSideTwo(self) -> None:
        ...
    def CreateFacePair(self) -> typing.List[Features.Feature]:
        ...
    def ReverseFacePair(self, facePairs: typing.List[NXObject]) -> None:
        ...
    def ModifyMidsurface(self, surfaceOption: Features.MidSurfaceByFacePairsBuilder.SurfaceType, facePairs: typing.List[NXObject]) -> None:
        ...
    def DeleteFacePair(self, facePairs: typing.List[NXObject]) -> None:
        ...
    def MergeFacePairs(self, facePairs: typing.List[NXObject]) -> None:
        ...
    def Trim(self, trimmingOption: Features.MidSurfaceByFacePairsBuilder.TrimmingOptionType, facePairs: typing.List[NXObject]) -> None:
        ...
    def SetupFacePairInContext(self, facePair: Features.Feature) -> None:
        ...
    def ValidateSelection(self, selectionType: int) -> None:
        ...
    AutoPopulateSideTwoOption: bool
    BodySelection: SelectBodyList
    HideBodyOption: bool
    IgnoreFaceSelection: ScCollector
    MergeAngleTolerance: float
    PairingStrategy: Features.MidSurfaceByFacePairsBuilder.PairingStrategyType
    SearchDistance: Expression
    SheetSelection: SelectBodyList
    SideOneSelection: ScCollector
    SideTwoSelection: ScCollector
    ThicknessRatio: float
    ThicknessValue: Expression
    TrimmingOption: Features.MidSurfaceByFacePairsBuilder.TrimmingOptionType
    UpdateOption: bool
    UserDefinedMidSurfaceSelection: SelectDisplayableObjectList


    class TrimmingOptionType(enum.Enum):
        AdvancedTrimming = 0
        BodyBasedTrimming = 1
        TrimtoSide1withNoExtension = 2
        SkipTrimming = 3
    

    class SurfaceType(enum.Enum):
        Standard = 0
        Side1 = 1
        Offset = 2
        CloudOfPoints = 3
        Large = 4
    

    class PairingStrategyType(enum.Enum):
        Progressive = 0
        Thickness = 1
        Manual = 2
    

class MidSurfaceByFacePairs(Features.BodyFeature):
    def __init__(self) -> None: ...
    def FindFacePairs(self) -> typing.List[Features.MidSurfaceFacePair]:
        ...


class Metaform(Features.BodyFeature):
    def __init__(self) -> None: ...


class MeshTransformerBuilder(Builder):
    def __init__(self) -> None: ...
    AsOriginalOption: bool
    ContinuityTypeOption: Features.MeshTransformerBuilder.ContinuityType
    DistanceTolerance: float
    EndFacetBody: Facet.SelectFacetedBody
    HideOriginal: bool
    MeshTopologyOption: Features.MeshTransformerBuilder.MeshTopologyType
    ShowTransformVectors: bool
    SmoothingOption: Features.MeshTransformerBuilder.SmoothingType
    StartFacetBody: Facet.SelectFacetedBody
    StepCount: Features.MeshTransformerBuilder.StepCountValue
    TransformCurves: Section
    TransformFaces: ScCollector
    TransformFactor: float


    class StepCountValue(enum.Enum):
        Number8 = 0
        Number16 = 1
        Number32 = 2
        Number64 = 3
        Number128 = 4
        Number256 = 5
        Number512 = 6
    

    class SmoothingType(enum.Enum):
        VeryLow = 0
        Low = 1
        Normal = 2
        High = 3
        VeryHigh = 4
    

    class MeshTopologyType(enum.Enum):
        Aligned = 0
        Unaligned = 1
        EndOnly = 2
    

    class ContinuityType(enum.Enum):
        C2 = 0
        C4 = 1
    

class MeshTransformer(Features.BodyFeature):
    def __init__(self) -> None: ...


class MeshSurfaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def NewProfile(self) -> MeshProfileString:
        ...
    def GetTolerances(self, tolLength: int) -> float:
        ...
    def SetTolerances(self, tol: float) -> None:
        ...
    def GetToleranceString(self, tolStrLength: int) -> str:
        ...
    def SetToleranceString(self, tolString: str) -> None:
        ...
    def GetProfilePointAlignment(self, stringIndex: int, arrayLength: int, alignIndex: int, alignParams: float) -> None:
        ...
    def SetProfilePointAlignment(self, stringIndex: int, alignIndex: int, alignParams: float) -> None:
        ...
    def GetFaceConstraintCollectors(self, nSides: int, facesCons: int, numCollectors: int, collectors: typing.List[ScCollector], numConsTypes: int, consTypes: typing.List[Features.MeshSurfaceBuilder.ConstraintType]) -> None:
        ...
    def SetFaceConstraintCollectors(self, facesCons: int, collectors: typing.List[ScCollector], consTypes: typing.List[Features.MeshSurfaceBuilder.ConstraintType]) -> None:
        ...
    def BuildProfileFromSections(self, conehead: bool, profileStringType: MeshProfileString.Type, skinType: MeshParameterData.FeatureType, stringPointType: MeshProfileString.SelectedPoint, sections: typing.List[Section], editInsertProfile: bool, profile: MeshProfileString) -> None:
        ...
    def GetProfile(self, index: int) -> MeshProfileString:
        ...
    def RemoveProfileString(self, profileIndex: int, stringIndex: int) -> None:
        ...
    def InsertProfileString(self, profileIndex: int, order: MeshProfileString.InsertOrder, stringIndex: int) -> None:
        ...
    def ReorderProfileStringCurves(self, stringIndex: int, stringStartCurve: Curve) -> None:
        ...
    def ValidateFeatureParameters(self) -> None:
        ...
    def NewRebuildData(self) -> SurfaceRebuildData:
        ...
    def GetFaceConstraintTypes(self, constraintSize: int) -> typing.List[Features.MeshSurfaceBuilder.ConstraintType]:
        ...
    def SetFaceConstraintTypes(self, constraintTypes: typing.List[Features.MeshSurfaceBuilder.ConstraintType]) -> None:
        ...
    def NewParametersData(self) -> MeshParameterData:
        ...
    def SetAngleAlignmentPoints(self, point1: Point3d, point2: Point3d) -> None:
        ...
    def GetAngleAlignmentPoints(self, point1: Point3d, point2: Point3d) -> None:
        ...
    def SetDistanceAlignmentVector(self, vector: Vector3d) -> None:
        ...
    def GetDistanceAlignmentVector(self) -> Vector3d:
        ...
    def RemovePointsAlignment(self) -> None:
        ...
    def RestorePointsAlignment(self) -> None:
        ...
    def RemoveSpineAlignment(self) -> None:
        ...
    FaceConstraintDirection: Features.MeshSurfaceBuilder.ConstraintDirection
    FeatureType: MeshParameterData.FeatureType
    NormalToEndSections: bool
    ParametersData: MeshParameterData
    RebuildData: SurfaceRebuildData
    SimpleConstruction: bool


    class ConstraintType(enum.Enum):
        None = 0
        Tangent = 1
        Curvature = 2
    

    class ConstraintDirection(enum.Enum):
        None = 0
        Isoparametric = 1
        Normal = 2
    

class MeshSurface(Features.BodyFeature):
    def __init__(self) -> None: ...


class MathIntegrationBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetExpressions(self) -> typing.List[Expression]:
        ...
    def SetExpressions(self, expressions: typing.List[Expression]) -> None:
        ...
    def GetMathNames(self) -> str:
        ...
    def SetMathNames(self, names: str) -> None:
        ...
    Associative: bool
    AssociativityType: Features.MathIntegrationBuilder.AssociativityTypes
    EmbedWorksheet: bool
    EmbeddedWorksheet: int
    FileBrowser: str
    Inputs: int
    Location: Features.MathIntegrationBuilder.LocationTypes
    NativeFileBrowser: str
    ShowInformationWindow: bool


    class LocationTypes(enum.Enum):
        OperatingSystem = 0
        Teamcenter = 1
        Embedded = 2
    

    class AssociativityTypes(enum.Enum):
        None = 0
        New = 1
        Existing = 2
    

class MathIntegration(Features.Feature):
    def __init__(self) -> None: ...


class MatchedReferenceBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    MatchedEntity: NXObject
    MatchedStatus: Features.MatchedReferenceBuilder.ResolvedStatus
    ParentEntity: NXObject
    ReverseDirection: bool
    Type: Features.MatchedReferenceBuilder.Types


    class Types(enum.Enum):
        Curve = 0
        Face = 1
        CurveCollector = 2
        FaceCollector = 3
        Section = 4
        Point = 5
        Vector = 6
        Object = 7
        BodyCollector = 8
        Csys = 9
        Plane = 10
        Axis = 11
        Undefined = 12
    

    class ResolvedStatus(enum.Enum):
        Initial = 0
        Unresolved = 1
        BySystem = 2
        ByUser = 3
    

class MatchEdgeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def LoadEditEdge(self) -> None:
        ...
    def SetupPoleEditing(self) -> None:
        ...
    def EditPoleUpdateSurface(self) -> None:
        ...
    def ResetEditPoles(self) -> None:
        ...
    def SetSelectedEditEdgeAndFace(self, edge: Edge, face: Face) -> None:
        ...
    def UpdateOriginalMatchSurface(self) -> None:
        ...
    Blend: Expression
    CanUseFaceFinder: bool
    ControlPoleManager: GeometricUtilities.ControlPoleManagerData
    DegreePatches: GeometricUtilities.DegreesAndSegmentsOrPatchesBuilder
    DepthSkew: GeometricUtilities.DepthSkewBuilder
    DistanceTolerance: float
    EdgeLimit: GeometricUtilities.CurveRangeBuilder
    EdgeOffsetPosition: GeometricUtilities.OnPathDimensionBuilder
    EndEdgeConstraint: Features.MatchEdgeBuilder.EdgeConstraintType
    FaceRecognizer: Features.FaceRecognitionBuilder
    FlipTargetCurveOrientation: bool
    IsBlendEnabled: bool
    IsCreateCopy: bool
    IsEditPoleEnabled: bool
    IsEndEdgeLocked: bool
    IsEndPoleFixed: bool
    IsG0Continuity: bool
    IsG1Continuity: bool
    IsG2Continuity: bool
    IsG3Continuity: bool
    IsKeepSelected: bool
    IsMatchEndToEnd: bool
    IsStartEdgeLocked: bool
    IsStartPoleFixed: bool
    MatchExactType: Features.MatchEdgeBuilder.MatchExact
    ObjectToEdit: SelectNXObject
    OppositeEdgeConstraint: GeometricUtilities.Continuity
    PartialMatch: int
    PoleMoveDirectionEnum: Features.MatchEdgeBuilder.PoleMoveDirection
    PoleMoveDirectionVector: Direction
    PoleMovementConstraintType: Features.MatchEdgeBuilder.PoleMovementConstraintEnumType
    StartEdgeConstraint: Features.MatchEdgeBuilder.EdgeConstraintType
    TangentDirectionVector: Direction
    TargetObjects: SelectDisplayableObjectList
    Type: Features.MatchEdgeBuilder.Types


    class Types(enum.Enum):
        MatchEdgeToEdge = 0
        MatchEdgeToFace = 1
        MatchEdgeToCurve = 2
        MatchEdgeToDatum = 3
    

    class PoleMovementConstraintEnumType(enum.Enum):
        WCS = 0
        View = 1
        Vector = 2
        Normal = 3
        Project = 4
        Inherit = 5
        FixStart = 6
        FixEnd = 7
        StartAndEnd = 8
    

    class PoleMoveDirection(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class MatchExact(enum.Enum):
        Exact = 0
        Align = 1
        None = 2
    

    class EdgeConstraintType(enum.Enum):
        Linked = 0
        Free = 1
        Perpendicular = 2
        IsoU = 3
        IsoV = 4
        Linear = 5
    

class MatchEdge(Features.BodyFeature):
    def __init__(self) -> None: ...


class MasterCutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def RecalculateLimits(self) -> None:
        ...
    def SetTargetComponents(self, targetComponents: typing.List[NXObject]) -> None:
        ...
    def GetTargetComponents(self) -> typing.List[DisplayableObject]:
        ...
    def CalcThroughLimits(self, direction: Direction, limit1: float, limit2: float) -> None:
        ...
    CutColor: int
    CutView: ModelingView
    Extrude: Features.ExtrudeBuilder
    HatchAngle: float
    HatchDistance: float
    MaterialOutsideLoop: bool
    SaveAsName: str
    TargetComponents: SelectDisplayableObjectList
    ToolBody: Body
    UseCutColor: bool
    UseCutHatch: bool
    UseSaveAs: bool


class MasterCut(Features.Feature):
    def __init__(self) -> None: ...


class MapleBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetExpressions(self) -> typing.List[Expression]:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Features.MathIntegrationBuilder instead..")"""
        ...
    def SetExpressions(self, expressions: typing.List[Expression]) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Features.MathIntegrationBuilder instead..")"""
        ...
    def GetMaplenames(self) -> str:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Features.MathIntegrationBuilder instead..")"""
        ...
    def SetMaplenames(self, names: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Features.MathIntegrationBuilder instead..")"""
        ...
    AssociativityEnumType: Features.MapleBuilder.AssociativityEnum
    AssociativityToggle: bool
    FileBrowser: str
    Inputs: int
    Location: Features.MapleBuilder.LocationType
    SettingsToggle: bool


    class LocationType(enum.Enum):
        OperatingSystem = 0
        Teamcenter = 1
    

    class AssociativityEnum(enum.Enum):
        None = 0
        New = 1
        Existing = 2
    

class Maple(Features.Feature):
    def __init__(self) -> None: ...


class MakeSolidBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    IsAssociative: bool
    SheetBodies: ScCollector


class MakeSolid(Features.BodyFeature):
    def __init__(self) -> None: ...


class MakeOffsetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FaceChangeOverflowBehavior: GeometricUtilities.FaceChangeOverflowBehavior
    MotionFace: SelectFace
    OffsetValue: Expression
    SaveRelation: bool
    StationaryFace: SelectFace


class MakeOffset(Features.BodyFeature):
    def __init__(self) -> None: ...


class Louver(Features.Feature):
    def __init__(self) -> None: ...


class LoftedFlange(Features.Feature):
    def __init__(self) -> None: ...


class LocalScaleCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CurveFinder: Features.CurveFinderBuilder
    Distance: Expression
    DistanceTolerance: float
    InputScaleFactor: Expression
    KeepOrthogonal: bool
    KeepTangent: int
    ScaleOrigin: Point3d
    SizeOption: int


class LocalScaleCurve(Features.BodyFeature):
    def __init__(self) -> None: ...


class LinkedFacetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BodySelect: SelectBody


class LinkedFacet(Features.BodyFeature):
    def __init__(self) -> None: ...


class LinearDimensionBuilder(Features.DimensionBuilder):
    def __init__(self) -> None: ...
    def SetFaceToMove(self, face: Face) -> None:
        ...
    DimensionOrientation: GeometricUtilities.OrientXpressBuilder
    DimensionOrientationVector: Direction
    MeasurementObject: SelectNXObject
    OrientationOption: Features.LinearDimensionBuilder.OrientationOptionType
    OriginObject: SelectNXObject


    class OrientationOptionType(enum.Enum):
        OrientXpress = 0
        Vector = 1
    

class LinearDimension(Features.BodyFeature):
    def __init__(self) -> None: ...


class LawExtensionEx(Features.BodyFeature):
    def __init__(self) -> None: ...


class LawExtensionBuilderEx(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleLaw: GeometricUtilities.LawBuilder
    AngleTolerance: float
    BaseProfile: Section
    CurveFitData: GeometricUtilities.CurveFitData
    DistanceTolerance: float
    Faces: ScCollector
    IsAngleCorrected: bool
    IsReferenceFaceNormalReversed: bool
    LaydownCurve: bool
    LengthLaw: GeometricUtilities.LawBuilder
    MaxCorrectionAngle: Expression
    MergeFacesIfPossible: bool
    MiterOption: Features.LawExtensionBuilderEx.MiterOptions
    MiterRadius: Expression
    OppositeSideExtensionOption: Features.LawExtensionBuilderEx.OppositeSideExtensionOptions
    OppositeSideLengthLaw: GeometricUtilities.LawBuilder
    SpineDefinition: GeometricUtilities.SpineDefinitionBuilder
    Type: Features.LawExtensionBuilderEx.Types
    Vector: Direction


    class Types(enum.Enum):
        Faces = 0
        Vector = 1
    

    class OppositeSideExtensionOptions(enum.Enum):
        None = 0
        Symmetric = 1
        Asymmetric = 2
    

    class MiterOptions(enum.Enum):
        None = 0
        Sharp = 1
        Blend = 2
        Radius = 3
    

class LawExtensionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleLaw: GeometricUtilities.LawBuilder
    AngleTolerance: float
    BaseProfile: Section
    DistanceTolerance: float
    Faces: ScCollector
    IsReferenceFaceNormalReversed: bool
    LengthLaw: GeometricUtilities.LawBuilder
    MergeFacesIfPossible: bool
    OppositeSideExtensionOption: Features.LawExtensionBuilder.OppositeSideExtensionOptions
    OppositeSideLengthLaw: GeometricUtilities.LawBuilder
    Rebuild: GeometricUtilities.Rebuild
    Spine: Section
    Type: Features.LawExtensionBuilder.Types
    Vector: Direction


    class Types(enum.Enum):
        Faces = 0
        Vector = 1
    

    class OppositeSideExtensionOptions(enum.Enum):
        None = 0
        Symmetric = 1
        Asymmetric = 2
    

class LawExtension(Features.BodyFeature):
    def __init__(self) -> None: ...


class LawCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CoordinateSystem: CoordinateSystem
    DistanceTolerance: float
    XLaw: GeometricUtilities.LawBuilder
    YLaw: GeometricUtilities.LawBuilder
    ZLaw: GeometricUtilities.LawBuilder


class LawCurve(Features.Feature):
    def __init__(self) -> None: ...


class LatticeFeatureCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def CreateLatticeBuilder(self, lattice: Features.Lattice) -> Features.LatticeBuilder:
        ...
    def Tag(self) -> Tag: ...



class LatticeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BaseFace: SelectDisplayableObjectList
    BoundaryBody: SelectBodyList
    CellTypeName: str
    ContourPoint1: Point
    ContourPoint2: Point
    ContourPoint3: Point
    ContourPoint4: Point
    EdgeLength: Expression
    FilterToolFace: SelectFaceList
    IsRandom: bool
    IsUniformCube: bool
    LatticeType: Features.LatticeBuilder.LatticeTypes
    LatticeVersion: Features.LatticeBuilder.Version
    Layers: int
    MaxDeviation: Expression
    MaxEdgeLength: Expression
    Offset: Expression
    Orientation: Matrix3x3
    OrientationPoint1: Point
    OrientationPoint2: Point
    Origin: Point3d
    Parameterization: Features.LatticeBuilder.ParameterizationType
    RemoveDanglingRods: bool
    RemoveDisconnectedRods: bool
    ReverseFaceDirection: bool
    RodDiameter: Expression
    SizeX: Expression
    SizeY: Expression
    SizeZ: Expression
    SplitCurve: Section
    TessellationFactor: float


    class Version(enum.Enum):
        V1 = 0
        V2 = 1
    

    class ParameterizationType(enum.Enum):
        Automatic = 0
        Planar = 1
        Contour = 2
        Cylindrical = 3
    

    class LatticeTypes(enum.Enum):
        UnitGraph = 0
        SurfaceGraph = 1
        TetrahedronGraph = 2
        ConformalGraph = 3
    

class Lattice(Features.BodyFeature):
    def __init__(self) -> None: ...


class LabelNotchBlendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DeleteLabel: bool
    FaceToLabel: ScCollector


class LabelNotchBlend(Features.BodyFeature):
    def __init__(self) -> None: ...


class LabelChamferBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ChamferFace: ScCollector
    ConstructionFace1: ScCollector
    ConstructionFace2: ScCollector
    DeleteChamferLabel: bool


    class ChamferType(enum.Enum):
        EdgeOffset = 0
        FaceOffset = 1
        EdgeAngleOffset = 2
        Vertex = 3
    

    class ChamferOrientType(enum.Enum):
        Convex = 0
        Concave = 1
    

class LabelChamfer(Features.BodyFeature):
    def __init__(self) -> None: ...


class JoinCurvesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    CurveOptions: GeometricUtilities.CurveOptions
    DistanceTolerance: float
    MaximumDegree: int
    MaximumSegments: int
    OutputCurveType: Features.JoinCurvesBuilder.OutputCurve
    Section: Section


    class OutputCurve(enum.Enum):
        General = 0
        Cubic = 1
        Quintic = 2
        Advanced = 3
    

class JoinCurves(Features.Feature):
    def __init__(self) -> None: ...


class Jog(Features.Feature):
    def __init__(self) -> None: ...


class IsoparametricCurvesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetActivePoints(self, points: typing.List[Point], masterPoint: Point) -> None:
        ...
    def UpdateIsoparametricCurves(self) -> None:
        ...
    Associative: bool
    ConstraintManager: Features.GeometricConstraintDataManager
    Direction: Features.IsoparametricCurvesBuilder.DirectionTypes
    IsSpacingEnabled: bool
    IsSwitchDirection: bool
    IsUEnabled: bool
    IsVEnabled: bool
    Number: int
    Placement: Features.IsoparametricCurvesBuilder.PlacementTypes
    SelectObject: SelectDisplayableObject
    Spacing: float


    class PlacementTypes(enum.Enum):
        Uniform = 0
        ThroughPoints = 1
        BetweenPoints = 2
    

    class DirectionTypes(enum.Enum):
        IsoU = 0
        IsoV = 1
        IsoUV = 2
    

class IsoparametricCurves(Features.CurveFeature):
    def __init__(self) -> None: ...


class IsolateFeatureBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Feature: Features.SelectFeature
    ProximityObject: SelectDisplayableObject


class IsolateFeature(Features.Feature):
    def __init__(self) -> None: ...


class IsoclineCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateIsocline(self) -> None:
        ...
    CanOptimizeCurve: bool
    CurveFitData: GeometricUtilities.CurveFitData
    DistanceThreshold: float
    EndAngle: Expression
    Face: ScCollector
    IntervalAngle: Expression
    IsAssociative: bool
    IsoclineAngle: Expression
    IsoclineTypes: Features.IsoclineCurveBuilder.CurveTypes
    ReferenceDirection: Direction
    StartAngle: Expression


    class CurveTypes(enum.Enum):
        Single = 0
        Multiple = 1
    

class IsoclineCurve(Features.CurveFeature):
    def __init__(self) -> None: ...


class IntersectionCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    CurveFitData: GeometricUtilities.CurveFitData
    CurveFitOptions: GeometricUtilities.CurveFitOptions
    FirstFace: ScCollector
    FirstPlane: Plane
    FirstSet: SelectObjectList
    SecondFace: ScCollector
    SecondPlane: Plane
    SecondSet: SelectObjectList
    Tolerance: float


class IntersectionCurve(Features.CurveFeature):
    def __init__(self) -> None: ...




class InstanceFeatureBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def RemoveClocking(self) -> None:
        ...
    EditedExpressionsList: GeometricUtilities.InstanceEditedExpressionsList
    InstanceClocking: GeometricUtilities.PatternClockingBuilder


class InstanceFeature(Features.Feature):
    def __init__(self) -> None: ...
    def GetImmediateContainedFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetAllContainedFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetAssociatedBodies(self) -> typing.List[Body]:
        ...
    def GetAssociatedFaces(self) -> typing.List[Face]:
        ...
    def GetAssociatedEdges(self) -> typing.List[Edge]:
        ...
    def GetAssociatedCurvesPointsDatums(self) -> typing.List[DisplayableObject]:
        ...


class IIsolateToolBodyOperation():
    def IsolateToolBodies(self) -> None:
        ...


class IFormBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def DeleteCurve(self, curve: Curve) -> None:
        ...
    def RemoveFeatureParameters(self, face: Face) -> None:
        ...
    BSurfaceExtractionOption: Features.IFormBuilder.BSurfaceExtractionOptions
    CanApplyToAll: bool
    CanCreateNewBody: bool
    CanKeepParameterization: bool
    CurveShaper: GeometricUtilities.CurveShapingBuilder
    ExtractTolerance: float
    FaceToDeform: Features.FaceRecognitionBuilder
    InsertionMethod: Features.IFormBuilder.InsertionMethodOptions
    Number: int
    ParameterDirection: Features.IFormBuilder.ParameterDirectionOptions
    SpecifyPoints: SelectPointList
    TransitionType: Features.IFormBuilder.TransitionTypes
    UMaxContinuity: GeometricUtilities.Continuity
    UMinContinuity: GeometricUtilities.Continuity
    VMaxContinuity: GeometricUtilities.Continuity
    VMinContinuity: GeometricUtilities.Continuity


    class TransitionTypes(enum.Enum):
        Local = 0
        Global = 1
    

    class ParameterDirectionOptions(enum.Enum):
        IsoU = 0
        IsoV = 1
    

    class InsertionMethodOptions(enum.Enum):
        Uniform = 0
        ThroughPoints = 1
        BetweenPoints = 2
    

    class GlobalTransitionTypes(enum.Enum):
        Blend = 0
        Bell = 1
    

    class BSurfaceExtractionOptions(enum.Enum):
        Original = 0
        MinimumBounded = 1
        FittedToBoundary = 2
    

class IForm(Features.BodyFeature):
    def __init__(self) -> None: ...


class IContainerFeature():
    def GetImmediateContainedFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetAllContainedFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetAssociatedBodies(self) -> typing.List[Body]:
        ...
    def GetAssociatedFaces(self) -> typing.List[Face]:
        ...
    def GetAssociatedEdges(self) -> typing.List[Edge]:
        ...
    def GetAssociatedCurvesPointsDatums(self) -> typing.List[DisplayableObject]:
        ...


class IBoolean():
    Target: Body
    Tool: Body


class HumanBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetName(self, name: str) -> None:
        ...
    def SetCustomHumanFileName(self, customFileName: str) -> None:
        ...
    def SetStatureData(self, statureType: HumanData.StatureType, stature: float, statureUnit: HumanData.StatureUnitType) -> None:
        ...
    def GetStatureData(self, statureType: HumanData.StatureType, stature: float, statureUnit: HumanData.StatureUnitType) -> None:
        ...
    def SetWeightData(self, weightType: HumanData.WeightType, weight: float, weightUnit: HumanData.WeightUnitType) -> None:
        ...
    def GetWeightData(self, weightType: HumanData.WeightType, weight: float, weightUnit: HumanData.WeightUnitType) -> None:
        ...
    def SetGender(self, gender: HumanData.GenderType) -> None:
        ...
    def SetAppearance(self, appearance: HumanData.AppearanceType) -> None:
        ...
    def SetDatabase(self, database: HumanData.DatabaseType) -> None:
        ...
    def SetPosition(self, location: Point3d) -> None:
        ...
    def SetOrientation(self, orientation: Matrix3x3) -> None:
        ...
    def SetExpressionStatureData(self, statureExpression: str) -> None:
        ...
    def SetExpressionWeightData(self, weightExpression: str) -> None:
        ...
    def SetReferencePoint(self, associative: bool, referencePointType: HumanData.ReferencePointType, referencePoint: Point) -> None:
        ...
    def SetReferencePointCoordinates(self, referencePointCoordinates: Point3d) -> None:
        ...
    def SetReferencePointType(self, referencePointType: HumanData.ReferencePointType) -> None:
        ...
    def SetHandShapeData(self, handType: int, handshapeName: str, neutralHandshapeName: str, handshapeLib: str, handshapeValue: float) -> None:
        ...
    def SetJointLimits(self, jointName: HumanData.JointType, jointXLowerLimit: float, jointXUpperLimit: float, jointYLowerLimit: float, jointYUpperLimit: float, jointZLowerLimit: float, jointZUpperLimit: float, isSymmetric: bool) -> None:
        ...
    def SetJointData(self, jointName: HumanData.JointType, jointXValue: float, jointYValue: float, jointZValue: float, isSymmetric: bool) -> None:
        ...
    def DoUpdate(self, updatePosturePrediction: bool, updateReferencePoint: bool, updateReachZone: bool) -> None:
        ...
    def SetResetPosture(self) -> None:
        ...
    def SetSegmentScalingData(self, segmentName: HumanData.SegmentScalingType, depthFactor: float, breadthFactor: float, lengthFactor: float) -> None:
        ...
    def SetResetSegment(self) -> None:
        ...
    def SetShowSkeleton(self, showSkeleton: bool) -> None:
        ...
    def SetAdvancedScalingData(self, dataName: HumanData.AdvancedScalingType, dataValue: float) -> None:
        ...
    def ExportCustomHumanFile(self, humanFileName: str) -> None:
        ...
    def ExportCustomPostureFile(self, postureFileName: str) -> None:
        ...
    def LoadCustomPostureFile(self, postureFileName: str) -> None:
        ...
    def SetPostureData(self, postureName: str, postureLib: str) -> None:
        ...
    def AddHandShapeLib(self, handshapeLib: str) -> None:
        ...
    def RemoveHandShapeLib(self, handshapeLib: str) -> None:
        ...
    def AddPostureLib(self, postureLib: str) -> None:
        ...
    def RemovePostureLib(self, postureLib: str) -> None:
        ...
    def GetHandGoalType(self, side: HumanData.SideType) -> HumanData.HandGoalType:
        ...
    def SetHandGoalType(self, side: HumanData.SideType, goalType: HumanData.HandGoalType) -> None:
        ...
    def GetHandGoalAllowNormal(self, side: HumanData.SideType) -> bool:
        ...
    def SetHandGoalAllowNormal(self, side: HumanData.SideType, allowNormal: bool) -> None:
        ...
    def GetHandGoalAllowRotate(self, side: HumanData.SideType) -> bool:
        ...
    def SetHandGoalAllowRotate(self, side: HumanData.SideType, allowRotate: bool) -> None:
        ...
    def GetHandGoalPosition(self, side: HumanData.SideType) -> Point3d:
        ...
    def SetHandGoalPosition(self, side: HumanData.SideType, goalPosition: Point3d) -> None:
        ...
    def GetHandGoalOrientation(self, side: HumanData.SideType) -> Matrix3x3:
        ...
    def SetHandGoalOrientation(self, side: HumanData.SideType, goalOrientation: Matrix3x3) -> None:
        ...
    def GetHandGoalPoint(self, side: HumanData.SideType) -> Point:
        ...
    def SetHandGoalPoint(self, side: HumanData.SideType, goalPoint: Point) -> None:
        ...
    def GetHandGoalCsys(self, side: HumanData.SideType) -> CoordinateSystem:
        ...
    def SetHandGoalCsys(self, side: HumanData.SideType, goalCsys: CoordinateSystem) -> None:
        ...
    def GetBarrierPoint(self) -> Point:
        ...
    def SetBarrierPoint(self, barrierPoint: Point) -> None:
        ...
    def GetBarrierNormal(self) -> Vector3d:
        ...
    def SetBarrierNormal(self, barrierNormal: Vector3d) -> None:
        ...
    def GetBarrierCsys(self) -> CoordinateSystem:
        ...
    def SetBarrierCsys(self, barrierCsys: CoordinateSystem) -> None:
        ...
    def GetBodySiteDisplayFlag(self, bodyPart: HumanData.EditDisplayBodyParts) -> bool:
        ...
    def SetBodySiteDisplayFlag(self, bodyPart: HumanData.EditDisplayBodyParts, displayFlag: bool) -> None:
        ...
    def GetSegmentSitesName(self) -> str:
        ...
    def SetSegmentSitesName(self, segmentSitesName: str) -> None:
        ...
    def GetPosturePrediction(self) -> HumanPosturePrediction:
        ...
    def CreateHumanHandsDialogBuilder(self) -> HumanHandsDialogBuilder:
        ...
    Appearance: HumanData.AppearanceType
    BalanceType: HumanData.InverseKinematicsBalanceType
    BodyParts: HumanData.InverseKinematicsBodyParts
    CurrentComfortStudyName: str
    CustomHumanFileName: str
    Database: HumanData.DatabaseType
    ExpressionStatureData: str
    ExpressionWeightData: str
    FollowFoot: bool
    Gender: HumanData.GenderType
    HeadEyeType: HumanData.InverseKinematicsHeadEyeType
    InitJoint: HumanData.InverseKinematicsInitJoint
    InverseKinematicsOrientation: Matrix3x3
    InverseKinematicsPosition: Point3d
    InverseKinematicsType: HumanData.InverseKinematicsType
    LockWrist: bool
    Name: str
    Orientation: Matrix3x3
    Position: Point3d
    ReferencePointCoordinates: Point3d
    ReferencePointType: HumanData.ReferencePointType


class Human(Features.Feature):
    def __init__(self) -> None: ...
    def CreateReachZone(self, index: int, reachZone: HumanReachZone) -> None:
        ...
    def FindSelectedReachZone(self, reachZoneGeom: NXObject) -> HumanReachZone:
        ...
    def DeleteNthReachZone(self, index: int) -> None:
        ...
    def GetNthReachZone(self, index: int) -> HumanReachZone:
        ...
    def GetNumReachZones(self) -> int:
        ...
    def FindNamedReachZone(self, reachZoneName: str) -> HumanReachZone:
        ...
    def CheckHuman(self, baseHuman: Features.Human, checkHumanData: bool, checkSegment: bool, checkExpression: bool, checkReachZone: bool) -> None:
        ...


class HolePackageBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BooleanOperation: GeometricUtilities.BooleanOperation
    DepthOption: Features.HolePackageBuilder.HoleDepthOptions
    DrillSize: str
    DrillSizeEndChamferAngle: Expression
    DrillSizeEndChamferEnabled: bool
    DrillSizeEndChamferOffset: Expression
    DrillSizeFitOption: str
    DrillSizeHoleDepth: Expression
    DrillSizeHoleDiameter: Expression
    DrillSizeStandard: str
    DrillSizeStartChamferAngle: Expression
    DrillSizeStartChamferEnabled: bool
    DrillSizeStartChamferOffset: Expression
    DrillSizeTipAngle: Expression
    EndHoleData: GeometricUtilities.EndHoleData
    GeneralCounterboreDepth: Expression
    GeneralCounterboreDiameter: Expression
    GeneralCounterboreHoleDepth: Expression
    GeneralCounterboreHoleDiameter: Expression
    GeneralCountersinkAngle: Expression
    GeneralCountersinkDiameter: Expression
    GeneralCountersinkHoleDepth: Expression
    GeneralCountersinkHoleDiameter: Expression
    GeneralHoleForm: Features.HolePackageBuilder.HoleForms
    GeneralSimpleHoleDepth: Expression
    GeneralSimpleHoleDiameter: Expression
    GeneralTaperAngle: Expression
    GeneralTaperedHoleDepth: Expression
    GeneralTaperedHoleDiameter: Expression
    GeneralTipAngle: Expression
    HoleDepthLimitOption: Features.HolePackageBuilder.HoleDepthLimitOptions
    HolePosition: Section
    MiddleHoleData: GeometricUtilities.MiddleHoleData
    NeckChamferEnabled: bool
    ProjectionDirection: GeometricUtilities.ProjectionOptions
    RadialEngageOption: str
    ReliefChamferEnabled: bool
    ScrewClearanceCounterboreDepth: Expression
    ScrewClearanceCounterboreDiameter: Expression
    ScrewClearanceCountersinkAngle: Expression
    ScrewClearanceCountersinkDiameter: Expression
    ScrewClearanceEndChamferAngle: Expression
    ScrewClearanceEndChamferEnabled: bool
    ScrewClearanceEndChamferOffset: Expression
    ScrewClearanceHoleDepth: Expression
    ScrewClearanceHoleDiameter: Expression
    ScrewClearanceHoleForm: Features.HolePackageBuilder.HoleForms
    ScrewClearanceNeckChamferAngle: Expression
    ScrewClearanceNeckChamferOffset: Expression
    ScrewClearanceReliefDepth: Expression
    ScrewClearanceReliefEnabled: bool
    ScrewClearanceStartChamferAngle: Expression
    ScrewClearanceStartChamferEnabled: bool
    ScrewClearanceStartChamferOffset: Expression
    ScrewClearanceTipAngle: Expression
    ScrewFitOption: str
    ScrewSize: str
    ScrewStandard: str
    ScrewType: str
    StartExtensionEnabled: bool
    StartHoleData: GeometricUtilities.StartHoleData
    TapDrillDiameter: Expression
    ThreadDepth: Expression
    ThreadLengthOption: Features.HolePackageBuilder.ThreadLengthOptions
    ThreadRotation: Features.HolePackageBuilder.ThreadRotationOptions
    ThreadSize: str
    ThreadStandard: str
    ThreadedEndChamferAngle: Expression
    ThreadedEndChamferDiameter: Expression
    ThreadedEndChamferEnabled: bool
    ThreadedHoleDepth: Expression
    ThreadedReliefAngle: Expression
    ThreadedReliefChamferAngle: Expression
    ThreadedReliefChamferOffset: Expression
    ThreadedReliefDepth: Expression
    ThreadedReliefDiameter: Expression
    ThreadedReliefEnabled: bool
    ThreadedStartChamferAngle: Expression
    ThreadedStartChamferDiameter: Expression
    ThreadedStartChamferEnabled: bool
    ThreadedTipAngle: Expression
    Tolerance: float
    Type: Features.HolePackageBuilder.Types
    UntilSelectedTarget: SelectDisplayableObject


    class Types(enum.Enum):
        GeneralHole = 0
        DrillSizeHole = 1
        ScrewClearanceHole = 2
        ThreadedHole = 3
        HoleSeries = 4
    

    class ThreadRotationOptions(enum.Enum):
        Right = 0
        Left = 1
    

    class ThreadLengthOptions(enum.Enum):
        Diameterx1 = 0
        Diameterx15 = 1
        Diameterx20 = 2
        Diameterx25 = 3
        Diameterx30 = 4
        Standard = 5
        Custom = 6
        Full = 7
    

    class HoleForms(enum.Enum):
        Simple = 0
        Counterbored = 1
        Countersink = 2
        Tapered = 3
    

    class HoleDepthOptions(enum.Enum):
        ToCylinderBottom = 0
        ToConeTip = 1
    

    class HoleDepthLimitOptions(enum.Enum):
        Value = 0
        UntilSelected = 1
        UntilNext = 2
        ThroughBody = 3
    

class HolePackage(Features.BodyFeature):
    def __init__(self) -> None: ...
    def GetOrigins(self, origins: typing.List[Point3d]) -> None:
        ...
    def GetDirections(self, directions: typing.List[Vector3d]) -> None:
        ...
    def GetHoleSeriesStartHoleFeature(self) -> Features.Feature:
        ...
    def GetHoleSeriesMiddleHoleFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetHoleSeriesEndHoleFeature(self) -> Features.Feature:
        ...


class HoleFeatureBuilder(Features.RPOBuilder):
    def __init__(self) -> None: ...
    def GetThruFace(self) -> ISurface:
        ...
    def SetThruFace(self, thruFace: ISurface) -> None:
        ...
    def GetTargetBody(self) -> Body:
        ...
    def SetTargetBody(self, targetBody: Body) -> None:
        ...
    def SetDepth(self, depth: str) -> None:
        ...
    def SetTipAngle(self, tipAngle: str) -> None:
        ...
    def SetDiameter(self, diameter: str) -> None:
        ...
    def SetCounterboreDiameter(self, diameter: str) -> None:
        ...
    def SetCounterboreDepth(self, depth: str) -> None:
        ...
    def SetCountersinkDiameter(self, diameter: str) -> None:
        ...
    def SetCountersinkAngle(self, angle: str) -> None:
        ...
    def CreateHole(self) -> None:
        ...
    def SetDepthAndTipAngle(self, depth: str, tipAngle: str) -> None:
        ...
    def SetSimpleHole(self, referencePoint: Point3d, reverseDirection: bool, placementFace: ISurface, diameter: str) -> None:
        ...
    def SetCounterboreHole(self, referencePoint: Point3d, reverseDirection: bool, placementFace: ISurface, diameter: str, counterboreDiameter: str, counterboreDepth: str) -> None:
        ...
    def SetCountersinkHole(self, referencePoint: Point3d, reverseDirection: bool, placementFace: ISurface, diameter: str, countersinkDiameter: str, countersinkAngle: str) -> None:
        ...
    CounterboreDepth: Expression
    CounterboreDiameter: Expression
    CountersinkAngle: Expression
    CountersinkDiameter: Expression
    Depth: Expression
    Diameter: Expression
    HoleLocation: Point3d
    PlacementFace: ISurface
    ReverseDirection: bool
    Subtype: Features.HoleFeatureBuilder.HoleSubtype
    TipAngle: Expression


    class HoleSubtype(enum.Enum):
        Simple = 0
        Counterbore = 1
        Countersink = 2
    

class Hole(Features.RPO):
    def __init__(self) -> None: ...
    def GetSubtype(self) -> Features.Hole.Subtype:
        ...
    def GetSimpleHole(self, diameter: Expression, depth: Expression, tipAngle: Expression) -> None:
        ...
    def GetCounterboreHole(self, diameter: Expression, depth: Expression, tipAngle: Expression, cboreDiameter: Expression, cboreDepth: Expression) -> None:
        ...
    def GetCountersinkHole(self, diameter: Expression, depth: Expression, tipAngle: Expression, csinkDiameter: Expression, csinkAngle: Expression) -> None:
        ...
    def GetPositioningDimensions(self) -> typing.List[PositioningDimension]:
        ...
    CounterboreDepth: Expression
    CounterboreDiameter: Expression
    CountersinkAngle: Expression
    CountersinkDiameter: Expression
    Depth: Expression
    Diameter: Expression
    PlacementFace: ISurface
    ThruFace: ISurface
    TipAngle: Expression


    class Subtype(enum.Enum):
        Simple = 0
        Counterbore = 1
        Countersink = 2
    

class HemFlange(Features.BodyFeature):
    def __init__(self) -> None: ...


class HelixBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Evaluate(self) -> None:
        ...
    AngleTolerance: float
    CoordinateSystem: CoordinateSystem
    DistanceTolerance: float
    EndLimit: GeometricUtilities.OnPathDimensionBuilder
    LengthMethod: Features.HelixBuilder.LengthMethods
    NumberOfTurns: str
    OrientationOption: Features.HelixBuilder.OrientationOptions
    PitchLaw: GeometricUtilities.LawBuilder
    SizeLaw: GeometricUtilities.LawBuilder
    SizeOption: Features.HelixBuilder.SizeOptions
    Spine: Section
    StartAngle: Expression
    StartLimit: GeometricUtilities.OnPathDimensionBuilder
    TurnDirection: Features.HelixBuilder.TurnDirections
    Turns: Expression
    Type: Features.HelixBuilder.Types


    class Types(enum.Enum):
        AlongVector = 0
        AlongSpine = 1
    

    class TurnDirections(enum.Enum):
        RightHand = 0
        LeftHand = 1
    

    class SizeOptions(enum.Enum):
        Diameter = 0
        Radius = 1
    

    class OrientationOptions(enum.Enum):
        Inferred = 0
        Specified = 1
    

    class LengthMethods(enum.Enum):
        Limits = 0
        Turns = 1
    

class Helix(Features.Feature):
    def __init__(self) -> None: ...


class Gusset(Features.Feature):
    def __init__(self) -> None: ...


class GuidedExtensionEx(Features.BodyFeature):
    def __init__(self) -> None: ...


class GuidedExtensionBuilderEx(Builder):
    def __init__(self) -> None: ...
    def ResetAllSegments(self) -> None:
        ...
    def UpdateSheetEdges(self) -> None:
        ...
    def UpdateExtendDirectionsAndGuideLines(self, typeChanged: bool) -> None:
        ...
    def SetSelectedSegmentType(self, segmentType: Features.GuidedExtensionBuilderEx.SegmentType) -> None:
        ...
    def MergeSegment(self) -> None:
        ...
    def SplitSegment(self) -> None:
        ...
    def RestoreSegments(self) -> None:
        ...
    def CreateGuideLine(self, assocEdge: Edge, guideLinePnt: Point3d, guideLineVector: Vector3d, guideLineLength: float) -> Curve:
        ...
    def UpdateAllGuideLinesLength(self) -> None:
        ...
    def ChangeGuideLineDirectionAndLength(self, guideLine: Curve, guideLineVector: Vector3d, guideLineLength: float) -> None:
        ...
    def SetReverseExtendDirection(self, reverseExtendDirection: bool) -> None:
        ...
    def ChangeFacesSideOption(self, flipFacesSideOption: bool) -> None:
        ...
    AngleTolerance: float
    CheckSurfaces: bool
    DistanceTolerance: float
    ExtendLength: Expression
    GuideLineAngle1: Expression
    GuideLineAngle2: Expression
    LastSelectedLoopIndex: int
    PlanarSurfacePreferred: bool
    ReferenceVector: Direction
    SegmentEdges: ScCollector
    SheetEdges: Section
    Type: Features.GuidedExtensionBuilderEx.Types
    VectorOrigin: Point


    class Types(enum.Enum):
        TangentFromFaces = 0
        Vector = 1
    

    class SegmentType(enum.Enum):
        Normal = 0
        Transition = 1
        Bypass = 2
    

class GroupFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FaceToGroup: Features.FaceRecognitionBuilder
    Rigid: bool


class GroupFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class GlobalShapingPointOffsetBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.GlobalShapingPointOffsetBuilder]) -> None:
        ...
    def Append(self, object: Features.GlobalShapingPointOffsetBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.GlobalShapingPointOffsetBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.GlobalShapingPointOffsetBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.GlobalShapingPointOffsetBuilder) -> None:
        ...
    def Erase(self, obj: Features.GlobalShapingPointOffsetBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.GlobalShapingPointOffsetBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.GlobalShapingPointOffsetBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.GlobalShapingPointOffsetBuilder, object2: Features.GlobalShapingPointOffsetBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.GlobalShapingPointOffsetBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class GlobalShapingPointOffsetBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Offset: Expression
    Point: Point


class GlobalShapingCurveOffsetBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.GlobalShapingCurveOffsetBuilder]) -> None:
        ...
    def Append(self, object: Features.GlobalShapingCurveOffsetBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.GlobalShapingCurveOffsetBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.GlobalShapingCurveOffsetBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.GlobalShapingCurveOffsetBuilder) -> None:
        ...
    def Erase(self, obj: Features.GlobalShapingCurveOffsetBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.GlobalShapingCurveOffsetBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.GlobalShapingCurveOffsetBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.GlobalShapingCurveOffsetBuilder, object2: Features.GlobalShapingCurveOffsetBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.GlobalShapingCurveOffsetBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class GlobalShapingCurveOffsetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Curve: Section
    Offset: GeometricUtilities.LawBuilder


class GlobalShapingBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def NewTargetPoint(self) -> Features.GlobalShapingPointOffsetBuilder:
        ...
    def NewTargetCurve(self) -> Features.GlobalShapingCurveOffsetBuilder:
        ...
    def SetBaseSheet(self, baseSheet: Body) -> None:
        ...
    def SetControlSheet(self, controlSheet: Body) -> None:
        ...
    def EnableMovePole(self, enable: bool) -> None:
        ...
    def UpdateDeformSheetType(self) -> None:
        ...
    AngleTolerance: float
    AssociatedObjects: SelectNXObjectList
    BaseCurve: Section
    BaseSheetSelection: SelectNXObject
    BendCurve: Section
    ControlCurve: Section
    ControlSheetSelection: SelectNXObject
    DeformationDirectionMethod: Features.GlobalShapingBuilder.DirectionMethodType
    DeformationDirectionReverse: bool
    DeformationDirectionVector: Direction
    DeformationType: Features.GlobalShapingBuilder.DeformationTypeValues
    DistanceTolerance: float
    FacetToDeform: SelectDisplayableObjectList
    FeatureOptions: GeometricUtilities.FeatureOptions
    FirstRegionLimitCurve: Section
    FirstRegionLimitCurveOffsetLaw: GeometricUtilities.LawBuilder
    FirstRegionOffsetCurve: ScCollector
    FirstTargetCurve: ScCollector
    FirstTargetCurveOffset: Expression
    FlipBaseNormalDirection: bool
    FlipBaseUDirection: bool
    FlipBaseVDirection: bool
    FlipControlNormalDirection: bool
    FlipControlUDirection: bool
    FlipControlVDirection: bool
    IterationCount: int
    KeepBaseLength: bool
    ModifyInputSheet: bool
    ModifyMethod: Features.GlobalShapingBuilder.ModifyMethodType
    MovePole: GeometricUtilities.MovePoleBuilder
    ProjectionDirection: Direction
    RadiusOptions: Features.GlobalShapingBuilder.RadiusType
    RadiusReductionPercent: Expression
    RegionEdgeCurve: ScCollector
    RegionLimitCurve: Section
    RegionToDeform: Section
    RegionToDeformOffset: Expression
    RotationAngle: Expression
    RotationAngleLaw: GeometricUtilities.LawBuilder
    RotationAngleReverseDirection: bool
    RotationAngleType: Features.GlobalShapingBuilder.RotationMethod
    RotationDistance: Expression
    RotationDistanceLaw: GeometricUtilities.LawBuilder
    RotationTargetCurve: Section
    RotationType: Features.GlobalShapingBuilder.RotationMethodType
    SecondRegionLimitCurve: Section
    SecondRegionLimitCurveOffsetLaw: GeometricUtilities.LawBuilder
    SecondRegionOffsetCurve: ScCollector
    SecondTargetCurve: ScCollector
    SecondTargetCurveOffset: Expression
    SheetToDeform: ScCollector
    StartLocation: GeometricUtilities.OnPathDimensionBuilder
    StretchDirection: Direction
    TaperEnd: Expression
    TaperStart: Expression
    TargetCurve: Section
    TargetCurveOffset: Expression
    TargetCurveOffsetLaw: GeometricUtilities.LawBuilder
    TargetCurveOffsetType: Features.GlobalShapingBuilder.OffsetMethod
    TargetCurveOrientation: Features.GlobalShapingBuilder.TargetCurveOrientationType
    TargetCurvesList: Features.GlobalShapingCurveOffsetBuilderList
    TargetPoint: Point
    TargetPointMethod: Features.GlobalShapingBuilder.PointMethodType
    TargetPointOffset: Expression
    TargetPointsList: Features.GlobalShapingPointOffsetBuilderList
    TargetSheet: ScCollector
    TransitionLaw: GeometricUtilities.LawBuilder
    TransitionOptions: Features.GlobalShapingBuilder.TransitionType
    TransitionShapeControl: float
    TwistAngleLaw: GeometricUtilities.LawBuilder
    TwistAngleReverseDirection: bool


    class TransitionType(enum.Enum):
        Function1 = 0
        Function2 = 1
        Law = 2
        G2 = 3
    

    class TargetCurveOrientationType(enum.Enum):
        Parallel = 0
        Perpendicular = 1
    

    class RotationMethodType(enum.Enum):
        Angle = 0
        Distance = 1
    

    class RotationMethod(enum.Enum):
        Constant = 0
        LawControlled = 1
        CurveDefined = 2
    

    class RadiusType(enum.Enum):
        Quintic = 0
        Radius = 1
    

    class PointMethodType(enum.Enum):
        OffsetFromSheet = 0
        PointDefined = 1
    

    class OffsetMethod(enum.Enum):
        Constant = 0
        LawControlled = 1
        CurveDefined = 2
    

    class ModifyMethodType(enum.Enum):
        Stretch = 0
        Overcrown = 1
    

    class DirectionMethodType(enum.Enum):
        SameAsProjection = 0
        NormalToSheet = 1
        NormalToBase = 2
        NormalToControl = 3
        SpecifiedDirection = 4
        None = 5
    

    class DeformBodyType(enum.Enum):
        SheetBodies = 0
        FacetBodies = 1
    

    class DeformationTypeValues(enum.Enum):
        ToPoint = 0
        ToCurves = 1
        OpenRegion = 2
        WallDeformation = 3
        Overbend = 4
        MatchToSheet = 5
        StretchToPoint = 6
        StretchToCurve = 7
        RadiusReduction = 8
        BySurface = 9
        ByCurve = 10
        Unknown = 11
    

    class BodyMethod(enum.Enum):
        Solid = 0
        Sheet = 1
    

class GlobalShaping(Features.BodyFeature):
    def __init__(self) -> None: ...


class GeometricConstraintDataSetManager(TaggedObject):
    def __init__(self) -> None: ...
    def CreateGeometricConstraintDataManager(self) -> Features.GeometricConstraintDataManager:
        ...
    def Append(self, manager: Features.GeometricConstraintDataManager) -> None:
        ...
    def Insert(self, insertBeforeIndex: int, manager: Features.GeometricConstraintDataManager) -> None:
        ...
    def Delete(self, manager: Features.GeometricConstraintDataManager) -> None:
        ...
    def Delete(self, managerIndex: int) -> None:
        ...
    def GetContents(self) -> typing.List[Features.GeometricConstraintDataManager]:
        ...
    def SetContents(self, managers: typing.List[Features.GeometricConstraintDataManager]) -> None:
        ...
    def GetIndex(self, manager: Features.GeometricConstraintDataManager) -> int:
        ...
    Length: int


class GeometricConstraintDataManager(TaggedObject):
    def __init__(self) -> None: ...
    def CreateGeometricConstraintData(self) -> Features.GeometricConstraintData:
        ...
    def Append(self, constraint: Features.GeometricConstraintData) -> None:
        ...
    def Insert(self, insertBeforeIndex: int, constraint: Features.GeometricConstraintData) -> None:
        ...
    def Delete(self, constraint: Features.GeometricConstraintData) -> None:
        ...
    def Delete(self, constraintIndex: int) -> None:
        ...
    def Clear(self) -> None:
        ...
    def GetContents(self) -> typing.List[Features.GeometricConstraintData]:
        ...
    def SetContents(self, constraints: typing.List[Features.GeometricConstraintData]) -> None:
        ...
    def FindItem(self, constraintIndex: int) -> Features.GeometricConstraintData:
        ...
    def GetIndex(self, constraint: Features.GeometricConstraintData) -> int:
        ...
    Length: int


class GeometricConstraintData(TaggedObject):
    def __init__(self) -> None: ...
    AutomaticConstraintDirection: Features.GeometricConstraintData.ParameterDirection
    AutomaticConstraintType: Features.GeometricConstraintData.AutoConstraintType
    CanInferConstraintFromAttachmentParent: bool
    Curvature: Offset
    CurvatureDerivative: Offset
    HasSymmetricModelingConstraint: bool
    Point: Point
    TangentDirection: Direction
    TangentMagnitude: Scalar


    class ParameterDirection(enum.Enum):
        Iso = 0
        Section = 1
        Normal = 2
        Perpendicular = 3
    

    class AutoConstraintType(enum.Enum):
        None = 0
        Tangent = 1
        Curvature = 2
        CurvatureDerivative = 3
    

class GeomcopyBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AlongPathAngle: Expression
    Associative: bool
    BetweenLocations: GeometricUtilities.BetweenLocationsData
    CopyThreads: bool
    CsysMirrorOption: Features.GeomcopyBuilder.CsysMirrorOptions
    FillPathLength: Features.GeomcopyBuilder.AlongPathDistanceOptions
    GeometryToInstance: SelectObjectList
    HideOriginal: bool
    MirrorPlane: Plane
    NumberOfCopies: Expression
    OnPathDistance: GeometricUtilities.OnPathDimensionBuilder
    Path: Section
    RotateAngle: Expression
    RotateDistance: Expression
    RotationAxis: Axis
    TranslateDistance: Expression
    TranslationVector: Direction
    Type: Features.GeomcopyBuilder.TransformTypes


    class TransformTypes(enum.Enum):
        BetweenLocations = 0
        Mirror = 1
        Translation = 2
        Rotation = 3
        AlongCurve = 4
        Offset = 5
    

    class CsysMirrorOptions(enum.Enum):
        MirrorXAndY = 0
        MirrorYAndZ = 1
        MirrorZAndX = 2
    

    class AlongPathDistanceOptions(enum.Enum):
        FillPathLength = 0
        ArcLength = 1
    

class Geomcopy(Features.Feature):
    def __init__(self) -> None: ...
    def GetBodies(self) -> typing.List[Body]:
        ...
    def GetFaces(self) -> typing.List[Face]:
        ...
    def GetEdges(self) -> typing.List[Edge]:
        ...


class GeodesicTrimBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Curve: Curve
    ExtentCurve: Curve
    Point: float


class GeodesicTrim(Features.CurveFeature):
    def __init__(self) -> None: ...


class GeodesicSketchCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def CreateGeodesicSketchBuilder(self, geodesicSketch: Features.GeodesicSketch) -> Features.GeodesicSketchBuilder:
        ...
    def EditGeodesicSketch(self, geodesicSketch: Features.GeodesicSketch) -> None:
        ...
    def CreateGeodesicIntersectBuilder(self, geodesicIntersect: Features.GeodesicIntersect) -> Features.GeodesicIntersectBuilder:
        ...
    def CreateGeodesicProjectBuilder(self, geodesicProject: Features.GeodesicProject) -> Features.GeodesicProjectBuilder:
        ...
    def CreateGeodesicOffsetBuilder(self, geodesicOffset: Features.GeodesicOffset) -> Features.GeodesicOffsetBuilder:
        ...
    def CreateGeodesicPointBuilder(self, geodesicPoint: Features.GeodesicPoint) -> Features.GeodesicPointBuilder:
        ...
    def CreateGeodesicLineBuilder(self, geodesicLine: Features.GeodesicLine) -> Features.GeodesicLineBuilder:
        ...
    def CreateGeodesicTrimBuilder(self, geodesicSketch: Features.GeodesicSketch) -> Features.GeodesicTrimBuilder:
        ...
    def CreateGeodesicFilletBuilder(self, geodesicFillet: Features.GeodesicFillet) -> Features.GeodesicFilletBuilder:
        ...
    def CreateGeodesicChamferBuilder(self, geodesicChamfer: Features.GeodesicChamfer) -> Features.GeodesicChamferBuilder:
        ...
    def CreateGeodesicResetBuilder(self) -> Features.GeodesicResetBuilder:
        ...
    def Tag(self) -> Tag: ...



class GeodesicSketchBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    SupportFaces: ScCollector


class GeodesicSketch(Features.CurveFeature):
    def __init__(self) -> None: ...


class GeodesicResetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Recipe: SelectCurve


class GeodesicProjectBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ProjectCurves: Section
    ProjectDirection: GeometricUtilities.ProjectionOptions
    ProjectPoint: Point
    ProjectType: Features.GeodesicProjectBuilder.Type


    class Type(enum.Enum):
        Curve = 0
        Point = 1
    

class GeodesicProject(Features.CurveFeature):
    def __init__(self) -> None: ...


class GeodesicPointBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Point: Point


class GeodesicPoint(Features.CurveFeature):
    def __init__(self) -> None: ...
    def DrivenByExpression(self, drivingExpression: Expression) -> None:
        ...


class GeodesicOffsetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    OffsetCurves: Section
    OffsetDirection: bool
    OffsetDistance: Expression


class GeodesicOffset(Features.CurveFeature):
    def __init__(self) -> None: ...


class GeodesicLineBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    EndPoint: Point
    StartPoint: Point


class GeodesicLine(Features.CurveFeature):
    def __init__(self) -> None: ...


class GeodesicIntersectBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    IntersectCurves: Section
    IntersectDatum: SelectDisplayableObject
    IntersectFaces: ScCollector
    IntersectType: Features.GeodesicIntersectBuilder.Type


    class Type(enum.Enum):
        Datum = 0
        Face = 1
        Curve = 2
    

class GeodesicIntersect(Features.CurveFeature):
    def __init__(self) -> None: ...


class GeodesicFilletBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FirstCurve: Curve
    FirstPoint: float
    FirstSection: Section
    Radius: Expression
    SecondCurve: Curve
    SecondPoint: float
    SecondSection: Section


class GeodesicFillet(Features.CurveFeature):
    def __init__(self) -> None: ...


class GeodesicChamferBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Distance: Expression
    FirstCurve: Curve
    FirstPoint: float
    FirstSection: Section
    SecondCurve: Curve
    SecondPoint: float
    SecondSection: Section


class GeodesicChamfer(Features.CurveFeature):
    def __init__(self) -> None: ...


class GeneralConicBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Evaluate(self) -> None:
        ...
    AnchorPoint: Point
    AssociativeToggle: bool
    CoefficientCSYS: CoordinateSystem
    ConstrainedPlaneCSYS: CoordinateSystem
    DrawingPlaneOption: Features.GeneralConicBuilder.DrawingPlaneOptions
    EndPoint: Point
    Extender: GeometricUtilities.CurveExtensionBuilder
    GeneralDrawingPlane: Plane
    InteriorPoint1: Point
    InteriorPoint2: Point
    InteriorPoint3: Point
    PlaneConstrainedToggle: bool
    RhoValue: float
    SlopeAtEndPoint: Direction
    SlopeAtStartPoint: Direction
    StartPoint: Point
    Type: Features.GeneralConicBuilder.Types
    ValueA: float
    ValueB: float
    ValueC: float
    ValueD: float
    ValueE: float
    ValueF: float


    class Types(enum.Enum):
        FivePoints = 0
        FourPointsOneSlope = 1
        ThreePointsTwoSlopes = 2
        ThreePointsAnchor = 3
        TwoPointsAnchorRho = 4
        TwoPointsTwoSlopesRho = 5
        Coefficients = 6
    

    class DrawingPlaneOptions(enum.Enum):
        View = 0
        XcYc = 1
        YcZc = 2
        ZcXc = 3
        General = 4
    

class GeneralConic(Features.Feature):
    def __init__(self) -> None: ...


class FreeTransformerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AsOriginalOption: bool
    ClassAOption: bool
    DistanceTolerance: float
    FixedCurvesList: GeometricUtilities.FtmFixedCurvesBuilderList
    Free2DOption: bool
    Free2DPlane: Plane
    HideOriginal: bool
    ShowTransformVectors: bool
    StepExpression: Expression
    TransformCurves: Section
    TransformCurvesList: GeometricUtilities.FtmTransformCurvesBuilderList
    TransformFaces: ScCollector
    TransformPointsList: GeometricUtilities.FtmTransformPointsBuilderList


class FreeTransformer(Features.BodyFeature):
    def __init__(self) -> None: ...


class FreeformSurfaceCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def CreateBlendCornerBuilder(self, cornerBlend: Features.BlendCorner) -> Features.BlendCornerBuilder:
        ...
    def CreateFillHoleBuilder(self, fillHole: Features.FillHole) -> Features.FillHoleBuilder:
        ...
    def CreateFlatteningAndFormingBuilder(self, flatteningAndForming: Features.FlatteningAndForming) -> Features.FlatteningAndFormingBuilder:
        ...
    def CreateStudioSurfaceBuilderEx(self, studioSurface: Features.Feature) -> Features.StudioSurfaceBuilderEx:
        ...
    def CreateFlatteningAndFormingBuilderEx(self, flatteningAndForming: Features.FlatteningAndForming) -> Features.FlatteningAndFormingBuilderEx:
        ...
    def Tag(self) -> Tag: ...



class FreeformCurveCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def CreateSmoothCurveStringBuilder(self, smoothCurveString: Features.SmoothCurveString) -> Features.SmoothCurveStringBuilder:
        ...
    def CreatePolylineBuilder(self, polyline: Polyline) -> Features.PolylineBuilder:
        ...
    def CreateSpineCurveBuilder(self, spineCurve: Features.SpineCurve) -> Features.SpineCurveBuilder:
        ...
    def CreateIsoclineCurveBuilder(self, isoclineCurve: Features.IsoclineCurve) -> Features.IsoclineCurveBuilder:
        ...
    def Tag(self) -> Tag: ...



class FlowBlendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def NewControlPoint(self) -> Features.VariableRadiusPointsBuilder:
        ...
    def NewSmoothRange(self) -> Features.SmoothRangeBuilder:
        ...
    ControlPoint: Features.VariableRadiusPointsBuilderList
    EdgeToBlend: ScCollector
    Patch: bool
    SmoothRange: Features.SmoothRangeBuilderList
    Tolerance: float
    Trim: bool
    TrimInputFacesToExtendedRail: bool


class FlowBlend(Features.BodyFeature):
    def __init__(self) -> None: ...


class FlexibleCable(Features.Feature):
    def __init__(self) -> None: ...


class FlatteningAndFormingBuilderEx(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AuxiliaryFaces: ScCollector
    ConstraintOptions: Features.FlatteningAndFormingBuilderEx.Constraints
    CutCurves: Section
    DestinationCoordinateSystem: CoordinateSystem
    DistortionMapOptions: Features.FlatteningAndFormingBuilderEx.DistortionMap
    FixedElementsList: NXObjectList
    FlatteningFeature: SelectNXObject
    OuterBoundary: SelectNXObject
    ReverseTransformation: bool
    SourceDirection: Direction
    SourceFaces: ScCollector
    SourceOrigin: Point
    SourceVDirection: Direction
    TabDetection: bool
    TransformationObjects: SelectNXObjectList
    Type: Features.FlatteningAndFormingBuilderEx.Types


    class Types(enum.Enum):
        Calculation = 0
        Reuse = 1
    

    class DistortionMap(enum.Enum):
        None = 0
        Length = 1
        Area = 2
        Angle = 3
    

    class Constraints(enum.Enum):
        NoConstraints = 0
        FixedElements = 1
    

class FlatteningAndFormingBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetDestinationFrame(self, manipulatorOrigin: Point3d, manipulatorMatrix: Matrix3x3) -> None:
        ...
    def SetDestinationFrame(self, manipulatorOrigin: Point3d, manipulatorMatrix: Matrix3x3) -> None:
        ...
    CutCurves: Section
    DistortionMapOptions: Features.FlatteningAndFormingBuilder.DistortionMap
    FlatteningFeature: SelectNXObject
    ReverseSecondaryDirection: bool
    ReverseTransformation: bool
    SourceDirection: Direction
    SourceFaces: ScCollector
    SourceOrigin: Point
    TabDetection: bool
    TransformationObjects: SelectNXObjectList
    Type: Features.FlatteningAndFormingBuilder.Types


    class Types(enum.Enum):
        Calculation = 0
        Reuse = 1
    

    class DistortionMap(enum.Enum):
        None = 0
        Length = 1
        Area = 2
        Angle = 3
    

class FlatteningAndForming(Features.BodyFeature):
    def __init__(self) -> None: ...


class FlatSolid(Features.Feature):
    def __init__(self) -> None: ...
    def GetToolMarkers(self, objects: typing.List[Features.FlatSolid.ObjectDataCsys]) -> None:
        ...
    def GetComponentTransformation(self, component: TaggedObject) -> ScalarMatrixValue:
        ...
    def MapInputGeomToFlattenedGeom(self, input: TaggedObject, flatGeom: typing.List[TaggedObject]) -> None:
        ...
    def MapFlattenedGeomToInputGeom(self, flatGeom: TaggedObject) -> TaggedObject:
        ...
    def GetEntityOnFlat(self, entity: TaggedObject) -> TaggedObject:
        ...
    def GetFaceTransformation(self, face: TaggedObject) -> ScalarMatrixValue:
        ...


    class FlatSolidObjectDataCsys():
        FlatSolidObject: TaggedObject
        FormedBodyObject: TaggedObject
        def ToString(self) -> str:
            ...
        def __init__(self, FlatSolidObject: TaggedObject, FormedBodyObject: TaggedObject) -> None: ...
    

class FlatPattern(Features.Feature):
    def __init__(self) -> None: ...
    def MakeFlatSolidInternal(self) -> None:
        ...
    def MakeFlatSolidExternal(self) -> None:
        ...
    def GetBendUpCenterLines(self, objects: typing.List[Features.FlatPattern.ObjectDataFace]) -> None:
        ...
    def GetBendDownCenterLines(self, objects: typing.List[Features.FlatPattern.ObjectDataFace]) -> None:
        ...
    def GetBendTangentLines(self, objects: typing.List[Features.FlatPattern.ObjectDataEdge]) -> None:
        ...
    def GetInnerMoldLines(self, objects: typing.List[Features.FlatPattern.ObjectDataFace]) -> None:
        ...
    def GetOuterMoldLines(self, objects: typing.List[Features.FlatPattern.ObjectDataFace]) -> None:
        ...
    def GetExteriorCurves(self, objects: typing.List[Features.FlatPattern.ObjectDataEdge]) -> None:
        ...
    def GetInteriorCutoutCurves(self, objects: typing.List[Features.FlatPattern.ObjectDataEdge]) -> None:
        ...
    def GetInteriorFeatureCurves(self, objects: typing.List[Features.FlatPattern.ObjectDataEdge]) -> None:
        ...
    def GetLighteningHoleCenters(self, objects: typing.List[Features.FlatPattern.ObjectDataFace]) -> None:
        ...
    def GetJoggleLines(self, objects: typing.List[Features.FlatPattern.ObjectDataEdge]) -> None:
        ...
    def GetAddedTopGeometry(self, objects: typing.List[Features.FlatPattern.ObjectDataGeneral]) -> None:
        ...
    def GetAddedBottomGeometry(self, objects: typing.List[Features.FlatPattern.ObjectDataGeneral]) -> None:
        ...
    def GetToolMarkers(self, objects: typing.List[Features.FlatPattern.ObjectDataCsys]) -> None:
        ...
    def GetCurves(self) -> typing.List[NXObject]:
        ...
    def GetAnnotations(self) -> typing.List[NXObject]:
        ...


    class FlatPatternObjectDataGeneral():
        FlatPatternObject: TaggedObject
        FlatSolidObject: TaggedObject
        FormedBodyObject: TaggedObject
        def ToString(self) -> str:
            ...
        def __init__(self, FlatPatternObject: TaggedObject, FlatSolidObject: TaggedObject, FormedBodyObject: TaggedObject) -> None: ...
    

    class FlatPatternObjectDataFace():
        FlatPatternObject: Curve
        FlatSolidObject: Face
        FormedBodyObject: Face
        def ToString(self) -> str:
            ...
        def __init__(self, FlatPatternObject: Curve, FlatSolidObject: Face, FormedBodyObject: Face) -> None: ...
    

    class FlatPatternObjectDataEdge():
        FlatPatternObject: Curve
        FlatSolidObject: Edge
        def ToString(self) -> str:
            ...
        def __init__(self, FlatPatternObject: Curve, FlatSolidObject: Edge) -> None: ...
    

    class FlatPatternObjectDataCsys():
        FlatPatternObject: Point
        FlatSolidObject: CartesianCoordinateSystem
        FormedBodyObject: Features.DatumCsys
        def ToString(self) -> str:
            ...
        def __init__(self, FlatPatternObject: Point, FlatSolidObject: CartesianCoordinateSystem, FormedBodyObject: Features.DatumCsys) -> None: ...
    

class Flange(Features.Feature):
    def __init__(self) -> None: ...


class FixedBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FaceToFix: Features.FaceRecognitionBuilder


class Fixed(Features.BodyFeature):
    def __init__(self) -> None: ...


class FitSurfaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def EditCSYS(self, originCsys: Point3d, matCsys: Matrix3x3) -> None:
        ...
    AngleValue: Expression
    CoordinateSystem: CoordinateSystem
    DirectionOption: Features.FitSurfaceBuilder.DirectionType
    IsAutomatic: bool
    IsBoundary: bool
    IsClosed: bool
    IsConstrained: bool
    IsHalfAngle: bool
    IsMultipleFeatures: bool
    IsRadius: bool
    IsUniformU: bool
    IsUniformV: bool
    Parameterization: GeometricUtilities.DegreesAndSegmentsOrPatchesBuilder
    Point1: Point
    Point2: Point
    Point3: Point
    Point4: Point
    RadiusValue: Expression
    RejectionThresholdValue: Expression
    SmoothFactor: int
    TargetObject: SelectNXObject
    TargetObjects: SelectNXObjectList
    TargetOption: Features.FitSurfaceBuilder.TargetType
    TargetRegion: GeometricUtilities.ColorCodedRegionBuilder
    Type: Features.FitSurfaceBuilder.Types
    Vector: Direction
    VectorConstraint: Direction


    class Types(enum.Enum):
        Fitfreeform = 0
        Fitplane = 1
        Fitsphere = 2
        Fitcylinder = 3
        Fitcone = 4
    

    class TargetType(enum.Enum):
        Object = 0
        ColorRegion = 1
    

    class DirectionType(enum.Enum):
        BestFit = 0
        Vector = 1
        Orientation = 2
        Csys = 3
    

class FitSurface(Features.BodyFeature):
    def __init__(self) -> None: ...


class FitCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ChainAllPoints(self) -> None:
        ...
    def GetFinalTargetPointsSize(self) -> int:
        ...
    def GetFinalTargetPoint(self, index: int) -> Point:
        ...
    def MakeConstraint(self, point: Point) -> None:
        ...
    def RemoveConstraint(self, point: Point) -> None:
        ...
    def DeleteTargetPoints(self, points: typing.List[Point]) -> None:
        ...
    def Evaluate(self) -> None:
        ...
    def UpdateTargetSelectionOnPointEditing(self) -> None:
        ...
    CanKeepTemplateSelected: bool
    CanRejectPointsAutomatically: bool
    CanUseAllPointsInPart: bool
    ConstraintManager: Features.GeometricConstraintDataManager
    Degree: int
    Extender: GeometricUtilities.CurveExtensionBuilder
    FittingParameters: Features.FitCurveBuilder.FittingParametersOptions
    HasRadius: bool
    HasReversedDirection: bool
    HasUniformSegments: bool
    IsAssociative: bool
    IsClosedBSpline: bool
    IsClosedCurve: bool
    ProjectionDirection: Direction
    ProjectionDirectionOption: Features.FitCurveBuilder.ProjectionDirectionOptions
    Radius: Expression
    RejectionThreshold: Expression
    Segments: int
    Target: SelectTaggedObjectList
    TargetSourceType: Features.FitCurveBuilder.TargetSourceTypes
    TemplateCurve: SelectSpline
    Tolerance: float
    Type: Features.FitCurveBuilder.Types


    class Types(enum.Enum):
        FitSpline = 0
        FitLine = 1
        FitCircle = 2
        FitEllipse = 3
    

    class TargetSourceTypes(enum.Enum):
        Infer = 0
        SpecifiedPoints = 1
        ChainedPoints = 2
        Curve = 3
        Face = 4
        FacetBody = 5
    

    class ProjectionDirectionOptions(enum.Enum):
        Xc = 0
        Yc = 1
        Zc = 2
        Normal = 3
        View = 4
        Vector = 5
    

    class FittingParametersOptions(enum.Enum):
        DegreeAndSegments = 0
        DegreeAndTolerance = 1
        TemplateCurve = 2
    

class FitCurve(Features.Feature):
    def __init__(self) -> None: ...


class FillHoleBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetBorderTypeItems(self) -> typing.List[Features.FillHoleBuilder.BorderContinuity]:
        ...
    def SetBorderTypeItems(self, markerToNodeListItem: typing.List[Features.FillHoleBuilder.BorderContinuity]) -> None:
        ...
    AreaControl: int
    Attraction: int
    CurveChain: Section
    DefaultEdgeContinuity: Features.FillHoleBuilder.ContinuityTypes
    FacetBody: Facet.SelectFacetedBody
    Fullness: Expression
    FullnessPoint: Point
    Patch: bool
    PickPoint: Point3d
    SelectPassThrougCurves: Section
    ShapeControlType: Features.FillHoleBuilder.ShapeControlTypes
    Tolerance: float


    class ShapeControlTypes(enum.Enum):
        None = 0
        Fullness = 1
        PassThroughCurves = 2
        FitToPoints = 3
        FitToFacet = 4
    

    class ContinuityTypes(enum.Enum):
        G0 = 0
        G1 = 1
        G2 = 2
    

    class FillHoleBuilderBorderContinuity():
        BorderObject: NXObject
        Continuity: Features.FillHoleBuilder.ContinuityTypes
        def ToString(self) -> str:
            ...
        def __init__(self, BorderObject: NXObject, Continuity: Features.FillHoleBuilder.ContinuityTypes) -> None: ...
    

class FillHole(Features.BodyFeature):
    def __init__(self) -> None: ...


class FeatureReplayBuilder(Builder):
    def __init__(self) -> None: ...
    def MakeFirstCurrent(self) -> None:
        ...
    def MakePreviousCurrent(self) -> None:
        ...
    def MakeNextCurrent(self) -> None:
        ...
    def MakeLastCurrent(self) -> None:
        ...
    def MakeNextBooleanCurrent(self) -> None:
        ...
    def Play(self) -> None:
        ...
    def Pause(self) -> None:
        ...
    ReplayTimestampNumber: int
    SecondsBetweenSteps: float


class FeatureReferencesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetMatchedReferences(self) -> typing.List[Features.MatchedReferenceBuilder]:
        ...
    def AutomaticMatch(self, matchBasedOnName: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...


class FeatureList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.Feature]) -> None:
        ...
    def Append(self, object: Features.Feature) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.Feature) -> int:
        ...
    def FindItem(self, index: int) -> Features.Feature:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.Feature) -> None:
        ...
    def Erase(self, obj: Features.Feature, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.Feature]:
        ...
    def SetContents(self, objects: typing.List[Features.Feature]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.Feature, object2: Features.Feature) -> None:
        ...
    def Insert(self, location: int, object: Features.Feature) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class FeatureGroup(Features.Feature):
    def __init__(self) -> None: ...
    def GetFeatureGroupType(self) -> Features.FeatureGroup.Type:
        ...
    def SetFeatureGroupType(self, type: Features.FeatureGroup.Type) -> None:
        ...
    def RemoveAllMembers(self) -> None:
        ...
    def NewRemoveMembers(self, members: typing.List[Features.Feature], reorderTimestamp: bool) -> None:
        ...
    def NewAddMembers(self, members: typing.List[Features.Feature], reorderTimestamp: bool) -> None:
        """[Obsolete("Deprecated in NX8.5.1.  Use NXOpen.Features.FeatureGroup.AddMembersWithRelocation instead.")"""
        ...
    def AddMembersWithRelocation(self, members: typing.List[Features.Feature], reorderTimestamp: bool, updateRelocatedFeatures: bool) -> None:
        ...
    def GetMembers(self, members: typing.List[Features.Feature]) -> None:
        ...
    def MakeTimestampsConsecutive(self) -> None:
        """[Obsolete("Deprecated in NX8.5.1.  Use NXOpen.Features.FeatureGroup.MakeTimestampsSequential instead.")"""
        ...
    def MakeTimestampsSequential(self, updateRelocatedFeatures: bool) -> None:
        ...
    AllowDeleteMembers: bool


    class Type(enum.Enum):
        NonEmbeddFeatureGroup = 0
        EmbeddFeatureGroup = 1
    

class FeatureCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateMeshSurfaceBuilder(self, meshSurf: Features.Feature) -> Features.MeshSurfaceBuilder:
        ...
    def CreateBlockFeatureBuilder(self, block: Features.Feature) -> Features.BlockFeatureBuilder:
        ...
    def CreateCopyPasteBuilder(self, features: typing.List[NXObject]) -> Features.CopyPasteBuilder:
        ...
    def CreateReferenceMapperBuilder(self, booleanBuilderTag: Features.FeatureBuilder) -> Features.ReferenceMapperBuilder:
        ...
    def CreateExtrudeBuilder(self, extrude: Features.Feature) -> Features.ExtrudeBuilder:
        ...
    def CreateUserDefinedObjectFeatureBuilder(self, udoFeature: Features.Feature) -> Features.UserDefinedObjectFeatureBuilder:
        ...
    def CreateRevolveBuilder(self, revolve: Features.Feature) -> Features.RevolveBuilder:
        ...
    def CreateEmbossBuilder(self, emboss: Features.Feature) -> Features.EmbossBuilder:
        ...
    def CreateOffsetEmbossBuilder(self, offsetEmboss: Features.Feature) -> Features.OffsetEmbossBuilder:
        ...
    def CreateDividefaceBuilder(self, divideface: Features.Feature) -> Features.DividefaceBuilder:
        ...
    def CreateOvercrownFeatureBuilder(self, overcrown: Features.Feature) -> Features.OvercrownBuilder:
        ...
    def CreateCurvelengthBuilder(self, curvelength: Features.Feature) -> Features.CurveLengthBuilder:
        ...
    def CreateDatumAxisBuilder(self, datumAxis: Features.Feature) -> Features.DatumAxisBuilder:
        ...
    def CreateDatumPlaneBuilder(self, dplane: Features.Feature) -> Features.DatumPlaneBuilder:
        ...
    def CreateResizePlaneBuilder(self, resizePlane: Features.Feature) -> Features.ResizePlaneBuilder:
        ...
    def CreateHoleFeatureBuilder(self, hole: Features.Feature) -> Features.HoleFeatureBuilder:
        ...
    def CreateRpoBuilder(self, rpo: Features.Feature) -> Features.RPOBuilder:
        ...
    def CreateChamferBuilder(self, chamfer: Features.Feature) -> Features.ChamferBuilder:
        ...
    def CreateEdgeBlendBuilder(self, edgeblend: Features.Feature) -> Features.EdgeBlendBuilder:
        ...
    def CreateUniteFeature(self, targetBody: Body, retainTargetBody: bool, toolBodies: typing.List[Body], retainToolBodies: bool, allowNonAssociativeBoolean: bool, nonAssociativeBoolean: bool, unparameterizedSolids: bool) -> typing.List[Features.BooleanFeature]:
        ...
    def CreateSubtractFeature(self, targetBody: Body, retainTargetBody: bool, toolBodies: typing.List[Body], retainToolBodies: bool, allowNonAssociativeBoolean: bool, nonAssociativeBoolean: bool, unparameterizedSolids: bool) -> typing.List[Features.BooleanFeature]:
        ...
    def CreateIntersectFeature(self, targetBody: Body, retainTargetBody: bool, toolBodies: typing.List[Body], retainToolBodies: bool, allowNonAssociativeBoolean: bool, nonAssociativeBoolean: bool, unparameterizedSolids: bool) -> typing.List[Features.BooleanFeature]:
        ...
    def CreateVarsweepBuilder(self, varsweep: Features.Feature) -> Features.VarsweepBuilder:
        ...
    def CreateFaceBlendBuilder(self, faceBlend: Features.Feature) -> Features.FaceBlendBuilder:
        ...
    def GetFeatures(self) -> typing.List[Features.Feature]:
        ...
    def FindObject(self, journalIdentifier: str) -> Features.Feature:
        ...
    def SuppressFeatures(self, features: typing.List[Features.Feature]) -> None:
        ...
    def UnsuppressFeatures(self, features: typing.List[Features.Feature]) -> typing.List[Features.Feature]:
        ...
    def GetAssociatedFeature(self, object: NXObject) -> Features.Feature:
        ...
    def CreateHumanBuilder(self, human: Features.Feature) -> Features.HumanBuilder:
        ...
    def CreateHumanPosturePredictionBuilder(self, posturePrediction: HumanPosturePrediction) -> HumanPosturePredictionBuilder:
        ...
    def CreateOffsetSurfaceBuilder(self, offsetSurface: Features.Feature) -> Features.OffsetSurfaceBuilder:
        ...
    def CreateRibbonBuilder(self, ribbon: Features.Feature) -> Features.RibbonBuilder:
        ...
    def CreatePatchBuilder(self, patch: Features.Feature) -> Features.PatchBuilder:
        ...
    def CreateBooleanBuilder(self, booleanFeature: Features.BooleanFeature) -> Features.BooleanBuilder:
        ...
    def CreateBooleanBuilderUsingCollector(self, booleanFeature: Features.BooleanFeature) -> Features.BooleanBuilder:
        ...
    def CreateTrimBodyBuilder(self, trimbodyFeat: Features.Feature) -> Features.TrimBodyBuilder:
        ...
    def CreateShellBuilder(self, shell: Features.Feature) -> Features.ShellBuilder:
        ...
    def CreateDatumCsysBuilder(self, datumCsys: Features.Feature) -> Features.DatumCsysBuilder:
        ...
    def CreateDraftBuilder(self, draft: Features.Feature) -> Features.DraftBuilder:
        ...
    def CreateRasterImage(self, origin: Point3d, matrix: Matrix3x3, length: float, height: float, imageFileName: str, translucency: float, maximumTextureSize: Features.RasterImage.MaxTextureSize) -> Features.RasterImage:
        ...
    def CreateMasterCutBuilder(self, masterCut: Features.Feature) -> Features.MasterCutBuilder:
        ...
    def CreateAocsBuilder(self, aocs: Features.Feature) -> Features.AOCSBuilder:
        ...
    def CreateOffsetFaceBuilder(self, offsetface: Features.Feature) -> Features.OffsetFaceBuilder:
        ...
    def CreateTubeBuilder(self, tube: Features.Feature) -> Features.TubeBuilder:
        ...
    def CreateMirrorFeatureBuilder(self, mirrorFea: Features.Feature) -> Features.MirrorFeatureBuilder:
        ...
    def CreateMirrorBuilder(self, mirrorFeature: Features.Mirror) -> Features.MirrorBuilder:
        ...
    def CreateScaleBuilder(self, scale: Features.Feature) -> Features.ScaleBuilder:
        ...
    def CreateSewBuilder(self, sew: Features.Feature) -> Features.SewBuilder:
        ...
    def CreateSectionCurveBuilder(self, sectionCurves: Features.Feature) -> Features.SectionCurveBuilder:
        ...
    def CreateIntersectionCurveBuilder(self, intersectionCurve: Features.Feature) -> Features.IntersectionCurveBuilder:
        ...
    def CreateThickenBuilder(self, thicken: Features.Feature) -> Features.ThickenBuilder:
        ...
    def CreateTrimExtendBuilder(self, trimExtend: Features.Feature) -> Features.TrimExtendBuilder:
        ...
    def CreateGeomcopyBuilder(self, geomcopy: Features.Feature) -> Features.GeomcopyBuilder:
        ...
    def CreateProjectCurveBuilder(self, projectCurve: Features.Feature) -> Features.ProjectCurveBuilder:
        ...
    def CreateExtractFaceBuilder(self, copyFace: Features.Feature) -> Features.ExtractFaceBuilder:
        ...
    def CreateJoinCurvesBuilder(self, joinCurves: Features.Feature) -> Features.JoinCurvesBuilder:
        ...
    def CreateStudioSplineBuilder(self, splineFeature: Features.StudioSpline) -> Features.StudioSplineBuilder:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.Features.FeatureCollection.CreateStudioSplineBuilderEx instead.")"""
        ...
    def CreateCurveOnSurfaceBuilder(self, cosFeature: Features.CurveOnSurface) -> Features.CurveOnSurfaceBuilder:
        ...
    def CreateUntrimBuilder(self, untrim: Features.Feature) -> Features.UntrimBuilder:
        ...
    def CreateWaveDatumBuilder(self, wavedatum: Features.Feature) -> Features.WaveDatumBuilder:
        ...
    def CreateWaveSketchBuilder(self, wavesketch: Features.Feature) -> Features.WaveSketchBuilder:
        ...
    def CreateWaveRoutingBuilder(self, waverouting: Features.Feature) -> Features.WaveRoutingBuilder:
        ...
    def CreateWavePointBuilder(self, wavepoint: Features.Feature) -> Features.WavePointBuilder:
        ...
    def CreateTrimsheetBuilder(self, trimSheet: Features.Feature) -> Features.TrimSheetBuilder:
        ...
    def CreateCircularBlendCurveBuilder(self, circularBlendCurve: Features.CircularBlendCurve) -> Features.CircularBlendCurveBuilder:
        ...
    def CreateRapidSurfaceBuilder(self, rapidSurface: Features.RapidSurface) -> Features.RapidSurfaceBuilder:
        ...
    def CreateUnsewBuilder(self, unsew: Features.Unsew) -> Features.UnsewBuilder:
        ...
    def CreateMirrorBodyBuilder(self, mirrorBody: Features.Feature) -> Features.MirrorBodyBuilder:
        ...
    def CreateDraftBodyBuilder(self, draftBody: Features.Feature) -> Features.DraftBodyBuilder:
        ...
    def GetPartFeaturesWithNewAlerts(self) -> typing.List[Features.Feature]:
        ...
    def GetAllPartFeaturesWithAlerts(self) -> typing.List[Features.Feature]:
        ...
    def CreateGlobalShapingBuilder(self, globalShaping: Features.GlobalShaping) -> Features.GlobalShapingBuilder:
        ...
    def CreateTrimCurveBuilder(self, trimCurve: Features.TrimCurve) -> Features.TrimCurveBuilder:
        ...
    def CreateTrimCurveBuilder(self, trimCurve: Spline) -> Features.TrimCurveBuilder:
        ...
    def CreateOffsetCurveBuilder(self, offsetCurve: Features.Feature) -> Features.OffsetCurveBuilder:
        ...
    def DeleteAllPartInformationalFeatureAlerts(self) -> None:
        ...
    def CreateThroughCurveMeshBuilder(self, throughCurveMesh: Features.Feature) -> Features.ThroughCurveMeshBuilder:
        ...
    def CreateBridgeCurveBuilder(self, bridgeCurve: Features.Feature) -> Features.BridgeCurveBuilder:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.FeatureCollection.CreateBridgeCurveBuilderEx instead.")"""
        ...
    def CreateSweptBuilder(self, swept: Features.Swept) -> Features.SweptBuilder:
        ...
    def CreateCylinderBuilder(self, cylinder: Features.Feature) -> Features.CylinderBuilder:
        ...
    def CreateCompositeCurveBuilder(self, compositeCurve: Features.Feature) -> Features.CompositeCurveBuilder:
        ...
    def CreateThroughCurvesBuilder(self, throughCurves: Features.Feature) -> Features.ThroughCurvesBuilder:
        ...
    def CreateStudioSurfaceBuilder(self, studioSurface: Features.Feature) -> Features.StudioSurfaceBuilder:
        ...
    def CreateSectionInertiaAnalysisBuilder(self, sectionInertiaAnalysis: Features.SectionInertiaAnalysis) -> Features.SectionInertiaAnalysisBuilder:
        ...
    def GetIsMasterCutVisibleInView(self, masterCut: Features.Feature, view: CutView) -> bool:
        ...
    def CreateDeleteFaceBuilder(self, deleteFace: Features.Feature) -> Features.DeleteFaceBuilder:
        ...
    def CreateResizeBlendBuilder(self, resizeBlend: Features.Feature) -> Features.ResizeBlendBuilder:
        ...
    def CreatePatchOpeningsBuilder(self, patchOpenings: Features.Feature) -> Features.PatchOpeningsBuilder:
        ...
    def CreateMoveFaceBuilder(self, moveFace: Features.Feature) -> Features.MoveFaceBuilder:
        ...
    def CreateOffsetRegionBuilder(self, offsetRegion: Features.Feature) -> Features.OffsetRegionBuilder:
        ...
    def CreatePatternFaceBuilder(self, patternFace: Features.Feature) -> Features.PatternFaceBuilder:
        ...
    def CreateResizeFaceBuilder(self, resizeFace: Features.Feature) -> Features.ResizeFaceBuilder:
        ...
    def CreateReplaceFaceBuilder(self, replaceFace: Features.Feature) -> Features.ReplaceFaceBuilder:
        ...
    def CreateRuledBuilder(self, ruled: Features.Feature) -> Features.RuledBuilder:
        ...
    def CreateNSidedSurfaceBuilder(self, nsidedSurface: Features.NSidedSurface) -> Features.NSidedSurfaceBuilder:
        ...
    def CreateSectionSurfaceBuilder(self, sectionSurface: Features.SectionSurface) -> Features.SectionSurfaceBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Features.FeatureCollection.CreateSectionSurfaceBuilderEx instead.")"""
        ...
    def CreateCoplanarBuilder(self, coplanar: Features.Feature) -> Features.CoplanarBuilder:
        ...
    def CreateSnipSurfaceBuilder(self, snipSurface: Features.SnipSurface) -> Features.SnipSurfaceBuilder:
        ...
    def CreateLinearDimensionBuilder(self, linearDimension: Features.LinearDimension) -> Features.LinearDimensionBuilder:
        ...
    def CreateEnlargeBuilder(self, enlargeFeature: Features.Enlarge) -> Features.EnlargeBuilder:
        ...
    def CreateLawExtensionBuilder(self, lawExtension: Features.LawExtension) -> Features.LawExtensionBuilder:
        ...
    def CreateLawExtensionBuilderEx(self, lawExtension: Features.Feature) -> Features.LawExtensionBuilderEx:
        ...
    def CreateGuidedExtensionBuilderEx(self, guidedExtension: Features.Feature) -> Features.GuidedExtensionBuilderEx:
        ...
    def CreateFreeTransformerBuilder(self, freeTransformer: Features.Feature) -> Features.FreeTransformerBuilder:
        ...
    def CreateMeshTransformerBuilder(self, meshTransformer: Features.Feature) -> Features.MeshTransformerBuilder:
        ...
    def CreateCombinedProjectionBuilder(self, combinedProjection: Features.CombinedProjection) -> Features.CombinedProjectionBuilder:
        ...
    def CreateStyledSweepBuilder(self, styledSweep: Features.Feature) -> Features.StyledSweepBuilder:
        ...
    def CreateCutFaceBuilder(self, cutFace: Features.Feature) -> Features.CutFaceBuilder:
        ...
    def CreateConeBuilder(self, cone: Features.Cone) -> Features.ConeBuilder:
        ...
    def CreateSphereBuilder(self, sphere: Features.Sphere) -> Features.SphereBuilder:
        ...
    def CreateCopyFaceBuilder(self, copyFace: Features.Feature) -> Features.CopyFaceBuilder:
        ...
    def CreatePasteFaceBuilder(self, pasteFace: Features.Feature) -> Features.PasteFaceBuilder:
        ...
    def CreatePoleSmoothingBuilder(self, poleSmoothing: Features.PoleSmoothing) -> Features.PoleSmoothingBuilder:
        ...
    def CreateAdmMoveFaceBuilder(self, admMoveFace: Features.AdmMoveFace) -> Features.AdmMoveFaceBuilder:
        ...
    def CreateWrapGeometryBuilder(self, wrapGeometry: Features.WrapGeometry) -> Features.WrapGeometryBuilder:
        ...
    def CreateGroupFaceBuilder(self, groupFace: Features.GroupFace) -> Features.GroupFaceBuilder:
        ...
    def CreateColorFaceBuilder(self) -> Features.ColorFaceBuilder:
        ...
    def CreateSeatBeltAnchorageBuilder(self, seatBeltAnchorage: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateSeatBeltAnchorageBuilder instead.")"""
        ...
    def CreateBoundedPlaneBuilder(self, boundedPlane: Features.BoundedPlane) -> Features.BoundedPlaneBuilder:
        ...
    def CreateAssemblyCutBuilder(self, assemblyCut: Features.AssemblyCut) -> Features.AssemblyCutBuilder:
        ...
    def CreateReflectionDataBuilder(self, reflectionData: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Features.VehicleDesignCollection.CreateReflectionDataBuilder instead.")"""
        ...
    def CreateWrapBuilder(self, wrap: Features.WrapUnwrap) -> Features.WrapBuilder:
        ...
    def CreateRemoveParametersBuilder(self) -> Features.RemoveParametersBuilder:
        ...
    def CreateMatchEdgeBuilder(self, matchEdge: Features.MatchEdge) -> Features.MatchEdgeBuilder:
        ...
    def CreateRadialDimensionBuilder(self, radialDimension: Features.RadialDimension) -> Features.RadialDimensionBuilder:
        ...
    def CreateStyledBlendBuilder(self, styledBlend: Features.StyledBlend) -> Features.StyledBlendBuilder:
        ...
    def CreateHolePackageBuilder(self, holePackage: Features.HolePackage) -> Features.HolePackageBuilder:
        ...
    def CreateStudioXformBuilder(self, studioXform: Features.StudioXform) -> Features.StudioXformBuilder:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Features.FeatureCollection.CreateStudioXformBuilderEx instead.")"""
        ...
    def CreateStudioXformBuilderEx(self, studioXform1: Features.StudioXform) -> Features.StudioXformBuilderEx:
        ...
    def CreateSweepAlongGuideBuilder(self, sweepAlongGuide: Features.SweepAlongGuide) -> Features.SweepAlongGuideBuilder:
        ...
    def CreateParallelBuilder(self, parallel: Features.Parallel) -> Features.ParallelBuilder:
        ...
    def CreateCoaxialBuilder(self, coaxial: Features.Coaxial) -> Features.CoaxialBuilder:
        ...
    def CreatePerpendicularBuilder(self, perpendicular: Features.Perpendicular) -> Features.PerpendicularBuilder:
        ...
    def CreateTangentBuilder(self, tangent: Features.Tangent) -> Features.TangentBuilder:
        ...
    def CreateAdmResizeFaceBuilder(self, admResizeFace: Features.AdmResizeFace) -> Features.AdmResizeFaceBuilder:
        ...
    def CreateStyledCornerBuilder(self, styledCorner: Features.StyledCorner) -> Features.StyledCornerBuilder:
        ...
    def CreateAdmOffsetRegionBuilder(self, offsetRegion: Features.AdmOffsetRegion) -> Features.AdmOffsetRegionBuilder:
        ...
    def CreateMirrorFaceBuilder(self, mirrorFace: Features.Feature) -> Features.MirrorFaceBuilder:
        ...
    def CreatePointSetBuilder(self, pointSet: Features.PointSet) -> Features.PointSetBuilder:
        ...
    def CreateWindshieldDatumBuilder(self, windshieldDatum: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Features.VehicleDesignCollection.CreateWindshieldDatumBuilder  instead.")"""
        ...
    def CreateVisionPlaneBuilder(self, visionPlane: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Features.VehicleDesignCollection.CreateVisionPlaneBuilder instead.")"""
        ...
    def CreateHoodVisibilityBuilder(self, hoodVisibility: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Features.VehicleDesignCollection.CreateHoodVisibilityBuilder instead.")"""
        ...
    def CreatePedestrianProtectionBuilder(self, pedestrianProtection: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Features.VehicleDesignCollection.CreatePedestrianProtectionBuilder  instead.")"""
        ...
    def ReorderFeature(self, features: typing.List[Features.Feature], target: Features.Feature, beforeOrAfter: Features.FeatureCollection.ReorderType) -> None:
        ...
    def CreateMirrorCurveBuilder(self, mirrorCurve: Features.Feature) -> Features.MirrorCurveBuilder:
        ...
    def CreatePromotionBuilder(self, promotion: Features.Promotion) -> Features.PromotionBuilder:
        ...
    def CreateRefitFaceBuilder(self, refitFace: Features.RefitFace) -> Features.RefitFaceBuilder:
        ...
    def CreateEditDimensionBuilder(self) -> Features.EditDimensionBuilder:
        ...
    def CreateAdaptiveShellBuilder(self, shellFace: Features.AdaptiveShell) -> Features.AdaptiveShellBuilder:
        ...
    def CreateShellFaceBuilder(self, shellFace: Features.ShellFace) -> Features.ShellFaceBuilder:
        ...
    def CreateChangeShellThicknessBuilder(self, shellFace: Features.ChangeShellThickness) -> Features.ChangeShellThicknessBuilder:
        ...
    def CreateLinkedFacetBuilder(self, linkedFacet: Features.LinkedFacet) -> Features.LinkedFacetBuilder:
        ...
    def CreateSilhouetteFlangeBuilder(self, silhouetteFlange: Features.SilhouetteFlange) -> Features.SilhouetteFlangeBuilder:
        ...
    def CreateReplaceFeatureBuilder(self) -> Features.ReplaceFeatureBuilder:
        ...
    def CreatePaintParametersBuilder(self) -> Features.PaintParametersBuilder:
        ...
    def CreateSmoothSplineBuilder(self, smoothSpline: Features.SmoothSpline) -> Features.SmoothSplineBuilder:
        ...
    def CreateSymmetricBuilder(self, symmetric: Features.Symmetric) -> Features.SymmetricBuilder:
        ...
    def CreateFeatureReplayBuilder(self) -> Features.FeatureReplayBuilder:
        ...
    def CreateSplitBodyBuilder(self, splitBody: Features.SplitBody) -> Features.SplitBodyBuilder:
        ...
    def CreateSplitBodyBuilderUsingCollector(self, splitBody: Features.SplitBody) -> Features.SplitBodyBuilder:
        ...
    def CreateTrimBody2Builder(self, trimBody2: Features.TrimBody2) -> Features.TrimBody2Builder:
        ...
    def CreateAngularDimensionBuilder(self, angularDimension: Features.AngularDim) -> Features.AngularDimBuilder:
        ...
    def CreateSectionEditBuilder(self, sectionEdit: Features.SectionEdit) -> Features.SectionEditBuilder:
        ...
    def CreatePullFaceBuilder(self, pullFace: Features.PullFace) -> Features.PullFaceBuilder:
        ...
    def CreateMidSurfaceByFacePairsBuilder(self, midSurfaceByFacePairs: Features.Feature) -> Features.MidSurfaceByFacePairsBuilder:
        ...
    def CreateMidSurfaceUserDefinedBuilder(self, midsurfaceUserDefined: Features.MidSurfaceUserDefined) -> Features.MidSurfaceUserDefinedBuilder:
        ...
    def CreatePatternFeatureBuilder(self, patternFeature: Features.Feature) -> Features.PatternFeatureBuilder:
        ...
    def CreateInstanceFeatureBuilder(self, instanceFeature: Features.InstanceFeature) -> Features.InstanceFeatureBuilder:
        ...
    def CreateInstanceFeatureBuilder(self, instanceFeatures: typing.List[Features.InstanceFeature], forClocking: bool) -> Features.InstanceFeatureBuilder:
        ...
    def CreateVehicleCoordinateSystemBuilder(self, vehicleCoordinateSystem: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateHoodVisibilityBuilder instead.")"""
        ...
    def CreateAestheticFaceBlendBuilder(self, aestheticFaceBlend: Features.AestheticFaceBlend) -> Features.AestheticFaceBlendBuilder:
        ...
    def CreateEdgeSymmetryBuilder(self, edgeSymmetry: Features.Feature) -> Features.EdgeSymmetryBuilder:
        ...
    def CreateReplaceBlendBuilder(self, replaceBlend: Features.ReplaceBlend) -> Features.ReplaceBlendBuilder:
        ...
    def ReplaceWithIndependentSketch(self, features: typing.List[Features.Feature]) -> Features.SketchConversionReport:
        ...
    def CreateMakeOffsetBuilder(self, makeOffset: Features.MakeOffset) -> Features.MakeOffsetBuilder:
        ...
    def CreateOptimizeFaceBuilder(self) -> Features.OptimizeFaceBuilder:
        ...
    def CreateShowRelatedFacesBuilder(self) -> Features.ShowRelatedFacesBuilder:
        ...
    def CreateFixedBuilder(self, makeFix: Features.Fixed) -> Features.FixedBuilder:
        ...
    def CreateLabelChamferBuilder(self, labelChamfer: Features.LabelChamfer) -> Features.LabelChamferBuilder:
        ...
    def CreateResizeChamferBuilder(self, resizeChamfer: Features.ResizeChamfer) -> Features.ResizeChamferBuilder:
        ...
    def CreateMapleBuilder(self, maple: Features.Maple) -> Features.MapleBuilder:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Features.FeatureCollection.CreateMathIntegrationBuilder instead.")"""
        ...
    def CreateMathIntegrationBuilder(self, mathIntegration: Features.MathIntegration) -> Features.MathIntegrationBuilder:
        ...
    def CreateConcaveFacesBuilder(self, concaveFaces: Features.ConcaveFaces) -> Features.ConcaveFacesBuilder:
        ...
    def CreateVirtualCurveBuilder(self, virtualCurve: Features.VirtualCurve) -> Features.VirtualCurveBuilder:
        ...
    def CreateVirtualBlendEdgeBuilder(self) -> Features.VirtualBlendEdgeBuilder:
        ...
    def CreateIformBuilder(self, iform: Features.IForm) -> Features.IFormBuilder:
        ...
    def CreateLawCurveBuilder(self, lawCurve: Features.LawCurve) -> Features.LawCurveBuilder:
        ...
    def CreateTextBuilder(self, text: Features.Text) -> Features.TextBuilder:
        ...
    def CreateDeleteEdgeBuilder(self, deleteEdge: Features.DeleteEdge) -> Features.DeleteEdgeBuilder:
        ...
    def CreateCopyPasteBuilder2(self, features: typing.List[NXObject]) -> Features.CopyPasteBuilder:
        ...
    def CreateReorderBlendsBuilder(self, reorderBlends: Features.ReorderBlends) -> Features.ReorderBlendsBuilder:
        ...
    def CreateIsoparametricCurvesBuilder(self, isoparametricCurves: Features.IsoparametricCurves) -> Features.IsoparametricCurvesBuilder:
        ...
    def ConvertToNewFeatureGroups(self) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.Features.FeatureCollection.ConvertToSequentialFeatureGroups or NXOpen.Features.FeatureCollection.ConvertToFloatingFeatureGroups instead.")"""
        ...
    def ConvertToFloatingFeatureGroups(self) -> None:
        ...
    def ConvertToSequentialFeatureGroups(self) -> None:
        ...
    def CreateVariableOffsetBuilder(self, variableOffset: Features.VariableOffset) -> Features.VariableOffsetBuilder:
        ...
    def CreateExtensionBuilder(self, extension: Features.Extension) -> Features.ExtensionBuilder:
        ...
    def CreateStudioSplineBuilderEx(self, spline: NXObject) -> Features.StudioSplineBuilderEx:
        ...
    def CreateSketchSplineBuilder(self, spline: Spline) -> Features.SketchSplineBuilder:
        ...
    def CreateDraftingSplineBuilder(self, spline: Spline) -> Features.DraftingSplineBuilder:
        ...
    def CreateBridgeSurfaceBuilder(self, bridgeSurface: Features.BridgeSurface) -> Features.BridgeSurfaceBuilder:
        ...
    def CreateEditCrossSectionBuilder(self, editCrossSection: Features.EditCrossSection) -> Features.EditCrossSectionBuilder:
        ...
    def CreateLabelNotchBlendBuilder(self, labelNotchBlend: Features.LabelNotchBlend) -> Features.LabelNotchBlendBuilder:
        ...
    def SetEditWithRollbackFeature(self, feature: Features.Feature) -> None:
        ...
    def SetCanResetMcf(self, canResetMcf: bool) -> None:
        ...
    def CreatePartModuleBuilder(self, partModule: Features.PartModule) -> Features.PartModuleBuilder:
        ...
    def CreatePartModuleRelationshipBuilder(self, partModule: Features.PartModule) -> GeometricUtilities.PartModuleRelationshipBuilder:
        ...
    def CreateDeleteBodyBuilder(self, deleteBody: Features.DeleteBody) -> Features.DeleteBodyBuilder:
        ...
    def CreateIsolateFeatureBuilder(self, isolateFeature: Features.IsolateFeature) -> Features.IsolateFeatureBuilder:
        ...
    def CreateHelixBuilder(self, helix: Features.Helix) -> Features.HelixBuilder:
        ...
    def CreateColorFeatureBuilder(self) -> Features.ColorFeatureBuilder:
        ...
    def CreateColorFeatureGroupBuilder(self) -> Features.ColorFeatureGroupBuilder:
        ...
    def CreateBridgeCurveBuilderEx(self, bridgeCurve: Features.BridgeCurve) -> Features.BridgeCurveBuilderEx:
        ...
    def CreateFitCurveBuilder(self, fitCurve: Features.FitCurve) -> Features.FitCurveBuilder:
        ...
    def CreateSketchFitCurveBuilder(self, fitCurve: Curve) -> Features.SketchFitCurveBuilder:
        ...
    def CreateEmbossBodyBuilder(self, embossBody: Features.EmbossBody) -> Features.EmbossBodyBuilder:
        ...
    def CreateGeneralConicBuilder(self, generalConic: Features.GeneralConic) -> Features.GeneralConicBuilder:
        ...
    def CreateFitSurfaceBuilder(self, fitSurface: Features.FitSurface) -> Features.FitSurfaceBuilder:
        ...
    def CreateSphericalCornerBuilder(self, sphericalCorner: Features.SphericalCorner) -> Features.SphericalCornerBuilder:
        ...
    def GetParentFeatureOfFace(self, face: Face) -> Features.Feature:
        ...
    def GetAssociatedFeaturesOfFace(self, face: Face) -> typing.List[Features.Feature]:
        ...
    def GetParentFeaturesOfEdge(self, edge: Edge) -> typing.List[Features.Feature]:
        ...
    def GetAssociatedFeaturesOfEdge(self, edge: Edge) -> typing.List[Features.Feature]:
        ...
    def GetParentFeatureOfBody(self, body: Body) -> Features.Feature:
        ...
    def GetAssociatedFeaturesOfBody(self, body: Body) -> typing.List[Features.Feature]:
        ...
    def CreateSectionSurfaceBuilderEx(self, sectionSurfaceEx: Features.SectionSurface) -> Features.SectionSurfaceBuilderEx:
        ...
    def CreatePatternFaceFeatureBuilder(self, patternFaceFeature: Features.PatternFaceFeature) -> Features.PatternFaceFeatureBuilder:
        ...
    def CreateRenameLinkedPartModulePartBuilder(self) -> GeometricUtilities.RenameLinkedPartModulePartBuilder:
        ...
    def CreateConvertFeatureGroupsToModulesBuilder(self) -> GeometricUtilities.ConvertFeatureGroupsToModulesBuilder:
        ...
    def CreateConvertFeatureGroupsToDesignGroupsBuilder(self) -> GeometricUtilities.ConvertFeatureGroupsToDesignGroupsBuilder:
        ...
    def CreateNestModuleBuilder(self) -> GeometricUtilities.NestModuleBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Please use NXOpen.Features.FeatureCollection instead.")"""
        ...
    def CreatePatternGeometryBuilder(self, patternGeometry: Features.PatternGeometry) -> Features.PatternGeometryBuilder:
        ...
    def CreateUnnestModuleBuilder(self) -> GeometricUtilities.UnnestModuleBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Please use NXOpen.Features.FeatureCollection instead.")"""
        ...
    def CreateBlendPocketBuilder(self, blendPocket: Features.BlendPocket) -> Features.BlendPocketBuilder:
        ...
    def CreateAnalyzePocketBuilder(self, analyzePocket: Features.AnalyzePocket) -> Features.AnalyzePocketBuilder:
        ...
    def CreateOptimizeCurveBuilder(self) -> Features.OptimizeCurveBuilder:
        ...
    def ReorganizeFeature(self, features: typing.List[Features.Feature], target: Features.Feature, beforeOrAfter: Features.FeatureCollection.ReorderType) -> None:
        ...
    def DeleteInformationalAlerts(self, feature: typing.List[NXObject]) -> None:
        ...
    def DeleteWarningAlerts(self, feature: typing.List[NXObject]) -> None:
        ...
    def CreateFlowBlendBuilder(self, flowBlend: Features.FlowBlend) -> Features.FlowBlendBuilder:
        ...
    def CreateCustomFeatureBuilder(self, customFeature: Features.Feature) -> Features.CustomFeatureBuilder:
        ...
    def CreateVarOffsetFaceBuilder(self, varOffsetFace: Features.VarOffsetFace) -> Features.VarOffsetFaceBuilder:
        ...
    def CreateRenewFeatureBuilder(self) -> GeometricUtilities.RenewFeatureBuilder:
        ...
    def StartEditWithRollbackManager(self, featureToEdit: Features.Feature, featureEditMark: Session.UndoMarkId) -> Features.EditWithRollbackManager:
        ...
    def CreateTrimCurve2FeatureBuilder(self, trimCurve2Feature: Features.TrimCurve2) -> Features.TrimCurve2Builder:
        ...
    def CreateEmbedManagerBuilder(self) -> Features.EmbedManagerBuilder:
        ...
    def CreateBodyByEquationBuilder(self, facetBodyByEquation: Features.BodyByEquation) -> Features.BodyByEquationBuilder:
        ...
    def InsertNewDesignGroup(self, referenceDesignGroup: Features.Feature) -> Features.Feature:
        ...
    def CreateDeformDefinitionBuilder(self) -> Features.DeformDefinitionBuilder:
        ...
    def Tag(self) -> Tag: ...

    SheetmetalManager: Features.SheetMetal.SheetmetalManager
    AeroSheetmetalManager: Features.SheetMetal.AeroSheetmetalManager
    Dies: Die.DieCollection
    WeldManager: Weld.WeldManager
    AutomotiveCollection: Features.AutomotiveCollection
    ShipCollection: Features.ShipCollection
    ToolingCollection: Features.ToolingCollection
    SynchronousEdgeCollection: Features.SynchronousEdgeCollection
    SweepFeatureCollection: Features.SweepFeatureCollection
    SynchronousCurveCollection: Features.SynchronousCurveCollection
    VehicleDesignCollection: Features.VehicleDesignCollection
    DesignFeatureCollection: Features.DesignFeatureCollection
    FreeformCurveCollection: Features.FreeformCurveCollection
    FreeformSurfaceCollection: Features.FreeformSurfaceCollection
    TrimFeatureCollection: Features.TrimFeatureCollection
    ToolingFeatureCollection: Features.ToolingFeatureCollection
    CustomAttributeCollection: Features.CustomAttributeCollection
    AeroCollection: Features.AeroCollection
    CurveFeatureCollection: Features.CurveFeatureCollection
    GeodesicSketchCollection: Features.GeodesicSketchCollection
    CustomFeatureDataCollection: Features.CustomFeatureDataCollection
    LatticeFeatureCollection: Features.LatticeFeatureCollection
    PrintCsysFeatureCollection: Features.PrintCsysFeatureCollection
    ActiveGroup: Features.FeatureGroup


    class ReorderType(enum.Enum):
        Into = 0
        Before = 1
        After = 2
    

class FeatureBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitFeature(self) -> Features.Feature:
        ...
    def GetFeature(self) -> Features.Feature:
        ...
    def SetParentFeatureInternal(self, parentFeature: Features.Feature) -> None:
        ...
    def UnsetParentFeatureInternal(self, parentFeature: Features.Feature) -> None:
        ...
    def ShowInternalParentFeatureForEdit(self, parentFeature: Features.Feature) -> None:
        ...
    def HideInternalParentFeatureAfterEdit(self, parentFeature: Features.Feature) -> None:
        ...
    ParentFeatureInternal: bool
    PatchSolutionFlag: bool
    PatchSurfaceFilename: str
    SurroundingPatchSurfaceFilename: str


class Feature(NXObject):
    def __init__(self) -> None: ...
    def GetExpressions(self) -> typing.List[Expression]:
        ...
    def GetParents(self) -> typing.List[Features.Feature]:
        ...
    def GetChildren(self) -> typing.List[Features.Feature]:
        ...
    def GetAllChildren(self) -> typing.List[Features.Feature]:
        ...
    def Highlight(self) -> None:
        ...
    def Unhighlight(self) -> None:
        ...
    def MakeCurrentFeature(self) -> None:
        ...
    def ShowBody(self, moveCurves: bool) -> None:
        ...
    def ShowParents(self, moveCurves: bool) -> None:
        ...
    def HideBody(self) -> None:
        ...
    def HideParents(self) -> None:
        ...
    def Suppress(self) -> None:
        ...
    def Unsuppress(self) -> None:
        ...
    def GetEntities(self) -> typing.List[NXObject]:
        ...
    def GetFeatureErrorMessages(self) -> str:
        ...
    def GetFeatureInformationalMessages(self) -> str:
        ...
    def DeleteInformationalAlerts(self) -> None:
        ...
    def DeleteWarningAlerts(self) -> None:
        ...
    def GetFeatureWarningMessages(self) -> str:
        ...
    def GetFeatureClueMessages(self) -> str:
        ...
    def DeleteClueAlerts(self) -> None:
        ...
    def GetFeatureClueHintMessages(self) -> str:
        ...
    def GetFeatureHintMessages(self) -> str:
        ...
    def DeleteHintAlerts(self) -> None:
        ...
    def MakeSketchInternal(self) -> None:
        ...
    def MakeSketchExternal(self) -> None:
        ...
    def RemoveForEdit(self, dependent: bool) -> None:
        ...
    def RemoveParameters(self) -> None:
        ...
    def ShowDimensions(self) -> None:
        ...
    def GetFeatureName(self) -> str:
        ...
    def GetSections(self) -> typing.List[Section]:
        ...
    def SetGroupActive(self, active: bool) -> None:
        ...
    def LogDiagnostic(self, errorCode: int, message: str, diagnosticType: Features.Feature.DiagnosticType) -> None:
        ...
    def ChangeBooleanType(self) -> None:
        ...
    def GetFeatureColor(self) -> NXColor:
        ...
    def BreakWaveLink(self) -> bool:
        ...
    AlgorithmVersion: int
    ContainerFeature: Features.IContainerFeature
    FeatureType: str
    IsContainedFeature: bool
    IsInternal: bool
    Location: Point3d
    Suppressed: bool
    Timestamp: int


    class DiagnosticType(enum.Enum):
        Information = 1
        Warning = 2
    

    class BooleanType(enum.Enum):
        Create = 0
        Unite = 1
        Subtract = 2
        Intersect = 3
        EmbossNormalSide = 8
        EmbossOppositeNormalSide = 9
    

class FaceSheet(Features.BodyFeature):
    def __init__(self) -> None: ...


class FaceRecognitionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SelectEntities(self, entities: typing.List[NXObject]) -> None:
        ...
    def DeselectEntities(self, entities: typing.List[NXObject]) -> None:
        ...
    def RecognizeCoplanar(self, isNear: bool) -> None:
        ...
    def UnrecognizeCoplanar(self, isNear: bool) -> None:
        ...
    def RecognizeCoplanarAxes(self, isNear: bool) -> None:
        ...
    def UnrecognizeCoplanarAxes(self, isNear: bool) -> None:
        ...
    def RecognizeCoaxial(self, isNear: bool) -> None:
        ...
    def UnrecognizeCoaxial(self, isNear: bool) -> None:
        ...
    def RecognizeTangent(self, isNear: bool) -> None:
        ...
    def UnrecognizeTangent(self, isNear: bool) -> None:
        ...
    def RecognizeSymmetric(self, isNear: bool) -> None:
        ...
    def UnrecognizeSymmetric(self, isNear: bool) -> None:
        ...
    def RecognizeThicknessChain(self, isNear: bool) -> None:
        ...
    def UnrecognizeThicknessChain(self, isNear: bool) -> None:
        ...
    def RecognizeEqualDiameter(self, isNear: bool) -> None:
        ...
    def UnrecognizeEqualDiameter(self, isNear: bool) -> None:
        ...
    def RecognizeParallel(self, isNear: bool) -> None:
        ...
    def UnrecognizeParallel(self, isNear: bool) -> None:
        ...
    def RecognizePerpendicular(self, isNear: bool) -> None:
        ...
    def UnrecognizePerpendicular(self, isNear: bool) -> None:
        ...
    def RecognizeOffset(self, isNear: bool) -> None:
        ...
    def UnrecognizeOffset(self, isNear: bool) -> None:
        ...
    def LockConstraint(self, feature: Features.Feature) -> None:
        ...
    def UnlockConstraint(self, feature: Features.Feature) -> None:
        ...
    def DeleteConstraint(self, feature: Features.Feature) -> None:
        ...
    def DeleteOffsetRelation(self, offsetFaces: typing.List[NXObject]) -> None:
        ...
    def ReplaceRules(self, rules: typing.List[SelectionIntentRule], createRulesWoUpdate: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CoaxialEnabled: bool
    CoplanarAxesEnabled: bool
    CoplanarEnabled: bool
    EqualDiameterEnabled: bool
    FaceCollector: ScCollector
    OffsetEnabled: bool
    ParallelEnabled: bool
    PerpendicularEnabled: bool
    ReferenceCoordinateSystem: GeometricUtilities.OrientXpressBuilder
    RelationScope: int
    SymmetricEnabled: bool
    TangentEnabled: bool
    ThicknessChainEnabled: bool
    UseFaceBrowse: bool


class FaceBlendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetLimitPlanes(self, startLimitPlane: Plane, endLimitPlane: Plane) -> None:
        ...
    def SetLimitPlanes(self, startLimitPlane: Plane, endLimitPlane: Plane) -> None:
        ...
    def UpdateConstantLawProfiles(self) -> None:
        ...
    AddTangentFaces: bool
    BlendType: Features.FaceBlendBuilder.Type
    BlendWidthMethod: Features.FaceBlendBuilder.WidthMethod
    CircularCrossSection: GeometricUtilities.CircularCrossSection
    CliffProjectOntoSecondWall: bool
    CoincidentEdgeCollector: ScCollector
    ConicCrossSection: GeometricUtilities.ConicCrossSection
    CrossSectionType: Features.FaceBlendBuilder.CrossSectionOption
    EdgeChainCollector: ScCollector
    EndCapLimitPlaneOption: bool
    EndLimitFaceNormalFlag: bool
    EndLimitFacesetCollector: ScCollector
    EndLimitPoint: Point
    FaceBlendDefineType: Features.FaceBlendBuilder.DefiningType
    FirstFaceCollector: ScCollector
    HelpPoint: Point
    IsIsoparameterLineOriented: bool
    LimitsListData: GeometricUtilities.BlendLimitsData
    MiddleFaceCollector: ScCollector
    MiddleFaceNormFlag: bool
    OverflowOption: Features.FaceBlendBuilder.OverflowMethod
    ProjectToSecondWall: bool
    PropagatePastSharpEdges: bool
    PropagationAngle: float
    RemoveSelfIntersections: bool
    ReverseFirstFaceNormal: bool
    ReverseSecondFaceNormal: bool
    ReverseThirdFaceNormal: bool
    RhoType: Features.FaceBlendBuilder.RhoMethod
    SecondFaceCollector: ScCollector
    SewAllFaces: bool
    Spine: Section
    StartCapLimitPlaneOption: bool
    StartLimitFaceNormalFlag: bool
    StartLimitFacesetCollector: ScCollector
    StartLimitPoint: Point
    TangencyCollector: ScCollector
    TangentSurface: ISurface
    ThirdFaceEndParameter: float
    ThirdFaceStartParameter: float
    Tolerance: float
    TrimInputFacesToBlendFaces: bool
    TrimLongInputFacesToExtendedRail: bool
    TrimmingOption: Features.FaceBlendBuilder.TrimmingMethod
    UseLimitsListFlag: bool


    class WidthMethod(enum.Enum):
        NaturallyVarying = 0
        ForcedConstant = 1
        TwoConstraintCurves = 2
    

    class Type(enum.Enum):
        RollingBall = 0
        Swept = 1
    

    class TrimmingMethod(enum.Enum):
        ToAllFaces = 0
        Short = 1
        Long = 2
        None = 3
    

    class RhoMethod(enum.Enum):
        Absolute = 0
        Relative = 1
    

    class OverflowMethod(enum.Enum):
        None = 0
        Notch = 1
    

    class DefiningType(enum.Enum):
        BlendTwoFace = 0
        BlendThreeFace = 1
        BlendFromEdges = 2
    

    class CrossSectionOption(enum.Enum):
        Circular = 0
        Conic = 1
        ConicSymmetric = 2
        CurvatureSymmetric = 3
        CurvatureAsymmetric = 4
    

class FaceBlend(Features.BodyFeature):
    def __init__(self) -> None: ...
    def IsolateToolBodies(self) -> None:
        ...


class ExtrudeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetToleranceValues(self, distanceTolerance: float, chainingTolerance: float, planarTolerance: float, angularTolerance: float) -> None:
        ...
    def AllowSelfIntersectingSection(self, allowSelfIntersectingSection: bool) -> None:
        ...
    AngularTolerance: float
    BooleanOperation: GeometricUtilities.BooleanOperation
    ChainingTolerance: float
    Direction: Direction
    DistanceTolerance: float
    Draft: GeometricUtilities.MultiDraft
    FeatureOptions: GeometricUtilities.FeatureOptions
    Limits: GeometricUtilities.Limits
    Offset: GeometricUtilities.FeatureOffset
    PlanarTolerance: float
    Section: Section
    SmartVolumeProfile: GeometricUtilities.SmartVolumeProfileBuilder


class Extrude(Features.BodyFeature):
    def __init__(self) -> None: ...


class ExtractFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetFaceChainDirectionSense(self, face: Face) -> bool:
        ...
    def FlipFaceChainDirectionSense(self, face: Face) -> None:
        ...
    def CommitCreateOnTheFly(self) -> Features.Feature:
        ...
    def GetWaveLinkInformation(self, info: str, xformExists: bool, xformOrigin: Point3d, xformOrientation: Matrix3x3, xformScale: float) -> None:
        ...
    def RecreateVectorOfHelpDirVector(self) -> None:
        ...
    def GetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def SetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def GetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    def SetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    AngleTolerance: float
    Associative: bool
    BodyReverseDirection: bool
    BodyToExtract: SelectObjectList
    BoundaryFaces: SelectFaceList
    CopyThreads: bool
    DeleteHoles: bool
    ExtractBodyCollector: ScCollector
    FaceChain: ScCollector
    FaceOption: Features.ExtractFaceBuilder.FaceOptionType
    FaceReverseDirection: bool
    FacesToExtract: SelectFaceList
    FeatureOption: Features.ExtractFaceBuilder.FeatureOptionType
    FixAtCurrentTimestamp: bool
    FrecAtTimeStamp: Features.Feature
    HideOriginal: bool
    InheritDisplayProperties: bool
    IsPsmOutputBody: bool
    MakePositionIndependent: bool
    ObjectToExtract: SelectDisplayableObjectList
    ParentPart: Features.ExtractFaceBuilder.ParentPartType
    ReplacementAssistant: GeometricUtilities.ReplAsstBuilder
    SeedFace: SelectFace
    SeedReverseDirection: bool
    SourcePartOccurrence: TaggedObject
    SurfaceType: Features.ExtractFaceBuilder.FaceSurfaceType
    TraverseInteriorEdges: bool
    Type: Features.ExtractFaceBuilder.ExtractType
    UseTangentEdgeAngles: bool


    class ParentPartType(enum.Enum):
        WorkPart = 0
        OtherPart = 1
        PositionIndependent = 2
    

    class FeatureOptionType(enum.Enum):
        OneFeatureForAllBodies = 0
        SeparateFeatureForEachBody = 1
    

    class FaceSurfaceType(enum.Enum):
        SameAsOriginal = 0
        PolynomialCubic = 1
        GeneralBSurface = 2
    

    class FaceOptionType(enum.Enum):
        SingleFace = 0
        AdjacentFaces = 1
        AllBodyFaces = 2
        FaceChain = 3
    

    class ExtractType(enum.Enum):
        Face = 0
        RegionOfFaces = 1
        Body = 2
    

class ExtractFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class ExtensionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DistanceType: Features.ExtensionBuilder.Distance
    ExtendType: Features.ExtensionBuilder.Extension
    Length: Expression
    Percent: Expression
    PercentU: Expression
    PercentV: Expression
    Selection: SelectNXObject
    Tolerance: float
    Type: Features.ExtensionBuilder.Types


    class Types(enum.Enum):
        Edge = 0
        Corner = 1
    

    class Extension(enum.Enum):
        Tangential = 0
        Circular = 1
    

    class Distance(enum.Enum):
        ByLength = 0
        ByPercentage = 1
    

class Extension(Features.BodyFeature):
    def __init__(self) -> None: ...


class ExtendSheetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ReverseExtensionSide(self) -> None:
        ...
    BodyOutputOption: Features.ExtendSheetBuilder.BodyOutput
    CopyOriginal: bool
    DistanceTolerance: float
    LimitMethod: Features.ExtendSheetBuilder.Limit
    LimitTools: ScCollector
    Offset: Expression
    SideEdgeShapeOption: Features.ExtendSheetBuilder.SideEdgeShape
    SurfaceShapeOption: Features.ExtendSheetBuilder.SurfaceShape
    TargetBoundaryEdges: ScCollector


    class SurfaceShape(enum.Enum):
        NaturalCurvature = 0
        NaturalTangent = 1
        Mirrored = 2
    

    class SideEdgeShape(enum.Enum):
        Automatic = 0
        Tangent = 1
        Orthogonal = 2
    

    class Limit(enum.Enum):
        Offset = 0
        UntilSelected = 1
    

    class BodyOutput(enum.Enum):
        ExtendOriginalSheet = 0
        ExtendasNewFace = 1
        ExtendasNewSheet = 2
    

class ExtendSheet(Features.BodyFeature):
    def __init__(self) -> None: ...


class EnlargeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ExtensionType: Features.EnlargeBuilder.ExtensionTypes
    Face: SelectFace
    IsCopy: bool
    ResizeParameters: GeometricUtilities.SurfaceRangeBuilder


    class ExtensionTypes(enum.Enum):
        Linear = 0
        Natural = 1
    

class Enlarge(Features.BodyFeature):
    def __init__(self) -> None: ...


class EmbossTarget(TaggedObject):
    def __init__(self) -> None: ...
    def SetDistance(self, distance: str) -> None:
        ...
    Distance: Expression
    EndcapFace: ScCollector
    EndcapPlane: ISurface
    FlipDirection: bool
    TargetFace: ScCollector


class EmbossTaper(TaggedObject):
    def __init__(self) -> None: ...
    def SetAngle(self, taperAngle: str) -> None:
        ...
    Angle: Expression
    BackAngle: Expression


class EmbossSidewall(TaggedObject):
    def __init__(self) -> None: ...
    def SetAngle(self, angle: str) -> None:
        ...
    def SetNewAngle(self, angle: float) -> None:
        ...
    def SetTapers(self, tapers: typing.List[Features.EmbossTaper]) -> None:
        ...
    def GetTapers(self) -> typing.List[Features.EmbossTaper]:
        ...
    def AddNewTaper(self) -> Features.EmbossTaper:
        ...
    def RemoveTaper(self, index: int) -> None:
        ...
    Angle: Expression
    Direction: Direction
    Joggle: Features.EmbossJoggle
    SidewallOption: Features.EmbossSidewall.SidewallMethod


    class SidewallMethod(enum.Enum):
        IsoclineTapered = 0
        CurveTapered = 1
        Ruled = 2
        Swept = 3
        Normal = 4
        TwoSection = 5
        Offset = 6
    

class EmbossRegion(TaggedObject):
    def __init__(self) -> None: ...
    def SetLimits(self, limits: typing.List[Features.EmbossLimit]) -> None:
        ...
    def GetLimits(self) -> typing.List[Features.EmbossLimit]:
        ...
    Convexity: Features.EmbossRegion.ConvexityOption
    Direction: Direction
    Projection: Features.EmbossProjection
    Section: Section
    Sidewall: Features.EmbossSidewall


    class ConvexityOption(enum.Enum):
        Above = 0
        Below = 1
        Mixed = 2
    

class EmbossProjection(TaggedObject):
    def __init__(self) -> None: ...
    Face: ScCollector
    Option: Features.EmbossProjection.ProjectionOption
    Plane: ISurface


    class ProjectionOption(enum.Enum):
        Endcap = 0
        Target = 1
        Face = 2
        Plane = 3
        None = 4
    

class EmbossLimit(TaggedObject):
    def __init__(self) -> None: ...
    def SetTargets(self, targets: typing.List[Features.EmbossTarget]) -> None:
        ...
    def GetTargets(self) -> typing.List[Features.EmbossTarget]:
        ...
    def SetDistance(self, distance: str) -> None:
        ...
    Direction: Direction
    Distance: Expression
    EndcapOption: Features.EmbossLimit.EndcapMethod
    EndcapSource: Features.EmbossLimit.EndcapSourceOption


    class EndcapSourceOption(enum.Enum):
        Target = 0
        Plane = 1
        Section = 2
        Face = 3
    

    class EndcapMethod(enum.Enum):
        Translation = 0
        OffsetExact = 1
        OffsetApproximation = 2
        None = 3
    

class EmbossJoggle(TaggedObject):
    def __init__(self) -> None: ...
    Direction: Direction
    DirectionOption: Features.EmbossJoggle.JoggleDirectionMethod


    class JoggleDirectionMethod(enum.Enum):
        Sidewall = 0
        Normal = 1
        Specify = 2
    

class EmbossBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetRegions(self, regions: typing.List[Features.EmbossRegion]) -> None:
        ...
    def GetRegions(self) -> typing.List[Features.EmbossRegion]:
        ...
    def MakeParentSketchInternal(self, internalizeParentSketch: bool) -> None:
        ...
    Tolerance: float


class EmbossBodyBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CapFace: ScCollector
    Clearance: Expression
    KeepTargets: bool
    KeepTools: bool
    RegionObject: SelectNXObjectList
    TargetBody: ScCollector
    TargetMaterialSide: bool
    ThickenOption: bool
    Thickness: Expression
    ToolBody: ScCollector
    ToolEmbossDirection: bool
    TrimOption: bool


class EmbossBody(Features.CombineBodyFeature):
    def __init__(self) -> None: ...


class Emboss(Features.BodyFeature):
    def __init__(self) -> None: ...


class EmbedManagerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetEmbeddedFile(self) -> int:
        ...
    def SetEmbeddedFile(self, embeddedFileIndex: int) -> None:
        ...
    def GetEmbeddedFileNames(self) -> str:
        ...
    Area: Features.EmbedManagerBuilder.UsageAreaTypes
    EmbedFileBrowser: str
    EmbedNativeFileBrowser: str
    Location: Features.EmbedManagerBuilder.LocationTypes
    NewNameFile: str
    ReplaceFileBrowser: str
    ReplaceNativeFileBrowser: str
    Task: Features.EmbedManagerBuilder.TaskTypes


    class UsageAreaTypes(enum.Enum):
        MathWorksheet = 0
    

    class TaskTypes(enum.Enum):
        Embed = 0
        Replace = 1
        Rename = 2
        Delete = 3
    

    class LocationTypes(enum.Enum):
        OperatingSystem = 0
        Teamcenter = 1
    

class EmbeddedOperationBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitOperation(self) -> Features.Feature:
        ...
    def GetOperation(self) -> Features.Feature:
        ...


class EditWithRollbackManager(TaggedObject):
    def __init__(self) -> None: ...
    def UpdateFeature(self, errorDuringFeatureEdit: bool) -> None:
        ...
    def Stop(self) -> None:
        ...
    def Destroy(self) -> None:
        ...


class EditDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    def AttachToNewGeometry(self, dimTag: Annotations.Annotation, newGeometry: DisplayableObject) -> None:
        ...
    Dimension: Annotations.SelectAnnotation
    DisplayAsPmi: bool
    FeatureSet: Features.SelectFeatureList


class EditCrossSectionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateSectionCurve(self) -> None:
        ...
    def RecreateSectionCurve(self) -> None:
        ...
    def ChangeSectionCurve(self) -> None:
        ...
    def IncludeBlendFaces(self) -> None:
        ...
    def IncludeHoleFaces(self) -> None:
        ...
    def RemoveData(self) -> None:
        ...
    def DeleteSectionSketch(self, sectionSketch: Sketch) -> None:
        ...
    Face: ScCollector
    FaceChangeOverflowBehavior: GeometricUtilities.FaceChangeOverflowBehavior
    IncludeBlends: bool
    IncludeHoles: bool
    Plane: SelectISurface
    SectionSketch: Sketch


class EditCrossSection(Features.BodyFeature):
    def __init__(self) -> None: ...


class EditBend(Features.BodyFeature):
    def __init__(self) -> None: ...


class EdgeSymmetryBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ResetPoleEditing(self) -> None:
        ...
    def UpdateSurfacePostPoleEditing(self) -> None:
        ...
    Blend: Expression
    CanBlend: bool
    CanCreateNewBody: bool
    DepthSkew: GeometricUtilities.DepthSkewBuilder
    IsEditPolesEnabled: bool
    IsEndLocked: bool
    IsG0: bool
    IsG1: bool
    IsG2: bool
    IsG3: bool
    IsStartLocked: bool
    MovementDirection: Features.EdgeSymmetryBuilder.MovementDirections
    MovementMethod: Features.EdgeSymmetryBuilder.MovementMethods
    ObjectToEdit: SelectNXObject
    Offset: Expression
    OppositeEdgeContinuity: GeometricUtilities.Continuity
    Parameterization: GeometricUtilities.DegreesAndSegmentsOrPatchesBuilder
    PoleManager: GeometricUtilities.ControlPoleManagerData
    SymmetryPlane: Plane
    SymmetryPlaneOption: Features.EdgeSymmetryBuilder.SymmetryPlaneOptions


    class SymmetryPlaneOptions(enum.Enum):
        YZ = 0
        XZ = 1
        XY = 2
        Arbitrary = 3
    

    class MovementMethods(enum.Enum):
        Normal = 0
        Project = 1
        WCS = 2
    

    class MovementDirections(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

class EdgeSymmetry(Features.BodyFeature):
    def __init__(self) -> None: ...


class EdgeRip(Features.Feature):
    def __init__(self) -> None: ...


class EdgeBlendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def AddChainset(self, collector: ScCollector, radius: str) -> int:
        ...
    def AddChainset(self, collector: ScCollector, sectionType: Features.EdgeBlendBuilder.Section, conicMethod: Features.EdgeBlendBuilder.Conic, rhoType: Features.EdgeBlendBuilder.Rhotype, radius: str, center: str, rho: str) -> int:
        ...
    def GetChainsetIndex(self, collector: ScCollector) -> int:
        ...
    def GetNumberOfValidChainsets(self) -> int:
        ...
    def GetChainset(self, csIndex: int, collector: ScCollector, radius: Expression) -> None:
        ...
    def GetChainsetAndSectionValue(self, csIndex: int, collector: ScCollector, sectionType: Features.EdgeBlendBuilder.Section, conicMethod: Features.EdgeBlendBuilder.Conic, rhoType: Features.EdgeBlendBuilder.Rhotype, radius: Expression, centerValueTAG: Expression, rhoValueTAG: Expression) -> None:
        ...
    def GetChainsetAndStatus(self, csIndex: int, collector: ScCollector, radius: Expression, isValid: bool) -> None:
        ...
    def RemoveChainset(self, csIndex: int) -> None:
        ...
    def RemoveChainsetByCollector(self, collector: ScCollector) -> None:
        ...
    def GetSetbackData(self, sbIndex: int, fromStart: bool, distanceExp: typing.List[Expression]) -> typing.List[Edge]:
        ...
    def AddSetbackData(self, edgeArray: typing.List[Edge], fromStart: bool, distance: str) -> int:
        ...
    def RemoveSetbackData(self, sbIndex: int) -> None:
        ...
    def GetNewStopshortData(self, ssIndex: int) -> GeometricUtilities.BlendStopshortBuilder:
        ...
    def GetStopshortData(self, ssIndex: int, edge: Edge, fromStart: bool) -> Expression:
        """[Obsolete("Deprecated in NX5.0.0.  Use Features.EdgeBlendBuilder.GetNewStopshortData instead.")"""
        ...
    def AddNewStopshortData(self, builder: GeometricUtilities.BlendStopshortBuilder) -> int:
        ...
    def AddStopshortData(self, edge: Edge, fromStart: bool, distance: str) -> int:
        """[Obsolete("Deprecated in NX5.0.0.  Use Features.EdgeBlendBuilder.AddNewStopshortData instead.")"""
        ...
    def RemoveStopshortData(self, edge: Edge, fromStart: bool) -> None:
        """[Obsolete("Deprecated in NX5.0.0.  Use Features.EdgeBlendBuilder.RemoveNewStopshortData instead.")"""
        ...
    def RemoveStopshortDataByType(self, edge: Edge, fromStart: bool, type: GeometricUtilities.BlendStopshortBuilder.Choices) -> None:
        ...
    def RemoveNewStopshortData(self, builder: GeometricUtilities.BlendStopshortBuilder) -> None:
        ...
    def RemoveStopshortData(self, ssIndex: int) -> None:
        """[Obsolete("Deprecated in NX5.0.0.  Use Features.EdgeBlendBuilder.RemoveNewStopshortData instead.")"""
        ...
    def GetVariableRadiusData(self, edge: Edge, radiiExp: typing.List[Expression], smartPoints: typing.List[Point], isExternalFlagArray: bool) -> float:
        """[Obsolete("Deprecated in NX6.0.0.  Use Features.EdgeBlendBuilder.GetVariableRadiusDataNew instead.")"""
        ...
    def GetVariableRadiusDataNew(self, edge: Edge, parameterExp: typing.List[Expression], radiiExp: typing.List[Expression], smartPoints: typing.List[Point], isExternalFlagArray: bool) -> None:
        ...
    def AddVariableRadiusData(self, edge: Edge, parameter: float, radius: str, smartPoint: Point, isExternal: bool) -> int:
        """[Obsolete("Deprecated in NX6.0.0.  Use Features.EdgeBlendBuilder.AddVariableRadiusDataNew instead.")"""
        ...
    def AddVariableRadiusDataNew(self, edge: Edge, parameter: str, radius: str, smartPoint: Point, isExternal: bool) -> int:
        ...
    def AddVariableRadiusDataNew(self, edge: Edge, parameter: str, radius: str, smartPoint: Point, isExternal: bool, isArclength: bool) -> int:
        ...
    def AddVariablePointData(self, edge: Edge, parameter: str, radius: str, centerValue: str, rhoValue: str, smartPoint: Point, isExternal: bool, isArclength: bool) -> int:
        ...
    def EditVariableRadiusData(self, edge: Edge, vrIndex: int, parameter: float, radius: str, smartPoint: Point, isExternal: bool) -> None:
        """[Obsolete("Deprecated in NX6.0.0.  Use Features.EdgeBlendBuilder.EditVariableRadiusDataNew instead.")"""
        ...
    def EditVariableRadiusDataNew(self, edge: Edge, vrIndex: int, parameter: str, radius: str, smartPoint: Point, isExternal: bool) -> None:
        ...
    def EditVariableRadiusDataNew(self, edge: Edge, vrIndex: int, parameter: str, radius: str, smartPoint: Point, isExternal: bool, isArclength: bool) -> None:
        ...
    def EditVariablePointData(self, edge: Edge, vrIndex: int, parameter: str, radius: str, centerValue: str, rhoValue: str, smartPoint: Point, isExternal: bool, isArclength: bool) -> None:
        ...
    def RemoveVariableRadiusData(self, edge: Edge, parameter: float) -> None:
        ...
    def RemoveVariableRadiusDataByIndex(self, edge: Edge, index: int) -> None:
        ...
    def RemoveVariableRadiusData(self, edge: Edge) -> None:
        ...
    def AddEdgeChainData(self, edgeArray: typing.List[Edge], edgeAlongChainDirectionArray: bool, isChainClosed: bool, isChainPartOfNetwork: bool) -> None:
        ...
    def AddPointOnEdgeChainData(self, edgeArray: typing.List[Edge], parameterOnChain: float, isArclength: bool, radius: float, centerValue: float, rhoValue: float, smartPoint: Point, isExternal: bool) -> None:
        ...
    def RemoveEdgeChainAndPointOnEdgeChainData(self) -> None:
        ...
    AllInstancesOption: bool
    BlendFaceContinuity: Features.EdgeBlendBuilder.FaceContinuity
    BlendOrder: Features.EdgeBlendBuilder.OrderOfBlending
    CliffEdges: ScCollector
    ConvexConcaveY: bool
    LimitFailingAreas: bool
    LimitsListData: GeometricUtilities.BlendLimitsData
    MoveSharpEdge: bool
    NonCliffEdges: ScCollector
    OverlapOption: Features.EdgeBlendBuilder.Overlap
    PatchComplexGeometryAreas: bool
    RemoveSelfIntersection: bool
    RollOntoEdge: bool
    RollOverSmoothEdge: bool
    SegmentBlendFaces: bool
    SetbackOption: Features.EdgeBlendBuilder.Setback
    Tolerance: float
    TrimmingOption: bool
    ZeroSlopeRadiusFunctionAtChainEnds: bool


    class Setback(enum.Enum):
        IncludeWithCorner = 0
        SeparateFromCorner = 1
    

    class Section(enum.Enum):
        Circular = 0
        Conic = 1
    

    class Rhotype(enum.Enum):
        Relative = 0
        Absolute = 1
    

    class Overlap(enum.Enum):
        MaintainAndIntersect = 0
        DifferentConvexityRollOver = 1
        AnyConvexityRollOver = 2
    

    class OrderOfBlending(enum.Enum):
        ConvexFirst = 0
        ConcaveFirst = 1
    

    class FaceContinuity(enum.Enum):
        Tangent = 0
        Curvature = 1
    

    class Conic(enum.Enum):
        BoundaryPlusCenter = 0
        BoundaryPlusRho = 1
        CenterPlusRho = 2
    

class EdgeBlend(Features.BodyFeature):
    def __init__(self) -> None: ...


class DrawnCutout(Features.Feature):
    def __init__(self) -> None: ...


class DrawDiePunch(Features.BodyFeature):
    def __init__(self) -> None: ...


class DraftingSplineBuilder(Features.StudioSplineBuilderEx):
    def __init__(self) -> None: ...


class DraftBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetVariableAngleOption(self) -> None:
        ...
    AngleTolerance: float
    Direction: Direction
    DistanceTolerance: float
    DraftAllInstances: bool
    DraftBothSides: bool
    DraftIsoclineOrTruedraft: Features.DraftBuilder.Method
    DraftReferencesMethod: Features.DraftBuilder.DraftReferencesMethods
    EdgeSetAngleExpressionList: ExpressionCollectorSetList
    FaceSetAngleExpressionList: ExpressionCollectorSetList
    PartingReference: ScCollector
    StationaryEntity: NXObject
    StationaryPartingReference: ScCollector
    StationaryReference: ScCollector
    SymmetricAngle: bool
    TwoDimensionFaceSetsData: GeometricUtilities.TwoExpressionsCollectorSetList
    TypeOfDraft: Features.DraftBuilder.Type
    VariableAngleData: GeometricUtilities.DraftVariableAngleData


    class Type(enum.Enum):
        Face = 0
        Edge = 1
        Tangent = 2
        PartingEdge = 3
    

    class Method(enum.Enum):
        Isocline = 0
        TrueDraft = 1
    

    class DraftReferencesMethods(enum.Enum):
        StationaryFace = 0
        PartingFace = 1
        StationaryAndPartingFace = 2
    

class DraftBodyBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DraftAngle: Expression
    DraftMethod: Features.DraftBodyBuilder.Method
    DrawDirection: Direction
    EdgesToMoveToDraftedFace: ScCollector
    ExtremeFacePointOverridesStationary: bool
    FacesToDraft: ScCollector
    FacesToMoveToDraftedFace: ScCollector
    FilletRadius: Expression
    MatchScope: Features.DraftBodyBuilder.MatchingScope
    MatchType: Features.DraftBodyBuilder.MatchingType
    MatchingOption: Features.DraftBodyBuilder.MatchOption
    PartingObject: SelectDisplayableObject
    RepairPartingEdge: Features.DraftBodyBuilder.RepairingPartingEdgeOption
    RepairRadius: Expression
    RepairingOption: Features.DraftBodyBuilder.RepairOption
    StationaryEdgesAboveParting: ScCollector
    StationaryEdgesBelowParting: ScCollector
    Tolerance: float
    Type: Features.DraftBodyBuilder.Types
    UnmatchedEdges: ScCollector
    UnmatchedFaces: ScCollector
    UseDraftedBodyAsPartingObject: bool


    class Types(enum.Enum):
        Edges = 0
        Faces = 1
    

    class RepairOption(enum.Enum):
        None = 0
        Blends = 1
        Planes = 2
        Both = 3
    

    class RepairingPartingEdgeOption(enum.Enum):
        None = 0
        WithFillet = 1
        WithLineAndFillet = 2
    

    class Method(enum.Enum):
        Isocline = 0
        TrueDraft = 1
    

    class MatchOption(enum.Enum):
        None = 0
        All = 1
        AllButSelected = 2
    

    class MatchingType(enum.Enum):
        None = 0
        ToIsocline = 1
        TangentToFace = 2
        FromEdges = 3
    

    class MatchingScope(enum.Enum):
        All = 0
        AllButSelected = 1
    

class DraftBody(Features.BodyFeature):
    def __init__(self) -> None: ...


class Draft(Features.BodyFeature):
    def __init__(self) -> None: ...


class DividefaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BlankOption: bool
    DividingObjectsList: SelectDisplayableObjectList
    ExtendOption: bool
    FacesToDivide: ScCollector
    ProjectCurvesThatLieOnFaceOption: bool
    ProjectionOption: GeometricUtilities.ProjectionOptions
    SelectDividingObject: GeometricUtilities.SelectDividingObjectBuilder
    Tolerance: float


class Divideface(Features.BodyFeature):
    def __init__(self) -> None: ...


class DivideCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ArcLength: float
    BoundingObjects: GeometricUtilities.BoundingObjectBuilderList
    CornerMethod: Features.DivideCurveBuilder.CornerOption
    CornerNumber: int
    CornerPoint: SelectPointList
    DirectionFlag: Features.DivideCurveBuilder.InputArcLengthDirectionFlag
    DividingCurve: SelectCurve
    EqualArcLengthSegments: int
    EqualParameterSegments: int
    EqualSegmentMethod: Features.DivideCurveBuilder.EqualSegmentOption
    KnotPoint: SelectPointList
    KnotPointMethod: Features.DivideCurveBuilder.KnotPointOption
    KnotPointNumber: int
    Type: Features.DivideCurveBuilder.Types


    class Types(enum.Enum):
        EqualSegments = 0
        ByBoundingObjects = 1
        InputArcLengthSegments = 2
        AtKnotpoints = 3
        AtCorners = 4
    

    class KnotPointOption(enum.Enum):
        ByNumber = 0
        SelectPoint = 1
        AllKnotpoints = 2
    

    class InputArcLengthDirectionFlag(enum.Enum):
        Start = 0
        End = 1
    

    class EqualSegmentOption(enum.Enum):
        EqualParameter = 0
        EqualArcLength = 1
    

    class CornerOption(enum.Enum):
        ByNumber = 0
        SelectPoint = 1
        AllCornerpoints = 2
    

class Dimple(Features.Feature):
    def __init__(self) -> None: ...


class DimensionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetDimension(self) -> Annotations.Dimension:
        ...
    DimensionLocation: Annotations.OriginBuilder
    FaceChangeOverflowBehavior: GeometricUtilities.FaceChangeOverflowBehavior
    FacesToMove: Features.FaceRecognitionBuilder
    SaveConstraints: GeometricUtilities.SaveConstraintsBuilder
    Value: Expression


class DesignFeatureCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def CreateRibBuilder(self, ribFeature: Features.Rib) -> Features.RibBuilder:
        ...
    def CreateMakesolidBuilder(self, makeSolid: Features.MakeSolid) -> Features.MakeSolidBuilder:
        ...
    def Tag(self) -> Tag: ...



class DeleteFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BlendCollector: ScCollector
    CapFace: SelectISurface
    CapOption: Features.DeleteFaceBuilder.CapOptionValues
    CapPlane: Plane
    DeletePartialBlend: bool
    FaceCollector: ScCollector
    FaceEdgeBlendPreference: Features.DeleteFaceBuilder.FaceEdgeBlendPreferenceOptions
    Heal: bool
    HealPlanar: bool
    MaxBlendRadius: Expression
    MaxHoleDiameter: Expression
    Setback: Features.DeleteFaceBuilder.SetbackOptions
    SpecifyBlend: bool
    Type: Features.DeleteFaceBuilder.SelectTypes
    UseHoleDiameter: bool


    class SetbackOptions(enum.Enum):
        SelectedBlend = 0
        NeighborBlend = 1
    

    class SelectTypes(enum.Enum):
        Face = 0
        Hole = 1
        Blend = 2
        FaceEdgeBlend = 3
    

    class FaceEdgeBlendPreferenceOptions(enum.Enum):
        Notch = 0
        Cliff = 1
    

    class CapOptionValues(enum.Enum):
        FaceOrPlane = 0
        NewPlane = 1
    

class DeleteFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class DeleteEdgeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    SimplyEdges: ScCollector


class DeleteEdge(Features.BodyFeature):
    def __init__(self) -> None: ...


class DeleteCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Heal: bool
    Section: ScCollector


class DeleteCurve(Features.BodyFeature):
    def __init__(self) -> None: ...


class DeleteBodyBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BodyToDelete: ScCollector
    BodyToKeep: ScCollector


class DeleteBody(Features.BodyFeature):
    def __init__(self) -> None: ...


class DeformDefinitionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetMemberFeatures(self, memberFrecs: typing.List[Features.Feature]) -> None:
        ...
    def SetExpressionsData(self, expData: Features.DeformDefinitionBuilder.JaDeformDefinitionExpData, defineValues: str) -> None:
        ...
    def SetExternalReferences(self, extRefs: typing.List[DisplayableObject], refPrompts: str) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    def SetHelpUrl(self, helpUrl: str) -> None:
        ...
    def SetDeleteExistingDefinition(self, deleteExistingDef: bool) -> None:
        ...


    class RangeType(enum.Enum):
        Int = 0
        Real = 1
    

    class DeformDefinitionBuilderJaDeformDefinitionExpData():
        Type: int
        Exp: Expression
        ExpName: str
        LowEnd: str
        HighEnd: str
        ScaleType: int
        def ToString(self) -> str:
            ...
    

    class ExpressionType(enum.Enum):
        Exp = 0
        Range = 1
        Option = 2
    

class DatumPlaneFeature(Features.DatumFeature):
    def __init__(self) -> None: ...
    DatumPlane: DatumPlane


class DatumPlaneBuilder(Features.DatumBuilder):
    def __init__(self) -> None: ...
    def SetPointAndDirection(self, point: Point, direction: Direction) -> None:
        ...
    def SetPointOnCurve(self, arcLength: float, constraint: str, alternateSolution: Features.DatumPlaneBuilder.AlternateSolution, option: Features.DatumPlaneBuilder.CurveOption, curve: ICurve) -> None:
        ...
    def SetPointOnCurve(self, arcLength: float, constraint: str, alternateSolution: Features.DatumPlaneBuilder.AlternateSolution, option: Features.DatumPlaneBuilder.CurveOption, curve: ICurve, direction: Direction) -> None:
        ...
    def SetPointOnCurve(self, arcLength: float, constraint: str, option: Features.DatumPlaneBuilder.CurveOption, curve: ICurve, secondGeometry: DisplayableObject) -> None:
        ...
    def SetThreePoints(self, point1: Point, point2: Point, point3: Point, useArcLength: Features.DatumPlaneBuilder.UseArcLength) -> None:
        ...
    def SetFaceAndOffset(self, face: Face, offsetValue: float, expression: str) -> None:
        ...
    def SetCornerPoints(self, corner1: Point3d, corner2: Point3d, corner3: Point3d, corner4: Point3d) -> None:
        ...
    def SetGeometryAndConstraints(self, geometry1: DisplayableObject, geometryConstraintType1: Features.DatumPlaneBuilder.ConstraintType, constraintAttribute1: int, constraintValue1: float, constraint1: str, geometry2: DisplayableObject, geometryConstraintType2: Features.DatumPlaneBuilder.ConstraintType, constraintAttribute2: int, constraintValue2: float, constraint2: str) -> None:
        ...
    def SetFixedDatumPlane(self, type: Features.DatumPlaneBuilder.FixedType) -> None:
        ...
    def GetPlane(self) -> Plane:
        ...
    def UpdateFeature(self) -> Features.Feature:
        ...
    def GetDatum(self) -> DatumPlane:
        ...
    OffsetInstance: bool
    ResizeDuringUpdate: bool


    class UseArcLength(enum.Enum):
        NoPoint = 0
        FirstPoint = 1
        SecondPoint = 2
        ThirdPoint = 3
        FirstAndSecondPoint = 4
        FirstAndThirdPoint = 5
        SecondAndThirdPoint = 6
        AllPoints = 7
    

    class FixedType(enum.Enum):
        All = 0
        Xy = 1
        Yz = 2
        Zx = 3
    

    class CurveOption(enum.Enum):
        Distance = 0
        Percent = 1
    

    class ConstraintType(enum.Enum):
        Undefined = 0
        Coincident = 1
        Parallel = 2
        Perpendicular = 3
        Center = 4
        Tangent = 5
        Distance = 6
        Angle = 7
        Frenet = 8
    

    class AlternateSolution(enum.Enum):
        Tangent = 0
        Normal = 1
        Binormal = 2
        OppositeTangent = 3
        OppositeNormal = 4
        OppositeBinormal = 5
        Project = 6
        ProjectView = 7
    

class DatumFeature(Features.Feature):
    def __init__(self) -> None: ...


class DatumCsysBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetWaveLinkInformation(self, info: str, xformExists: bool, xformOrigin: Point3d, xformOrientation: Matrix3x3, xformScale: float) -> None:
        ...
    ComponentsCreation: bool
    Csys: CartesianCoordinateSystem
    DisplayScaleFactor: float
    FixedSizeDatum: bool


class DatumCsys(Features.Feature):
    def __init__(self) -> None: ...
    def SetWcsAtCsys(self) -> None:
        ...


class DatumBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateConstraint(self) -> DatumConstraint:
        ...
    def GetConstraints(self) -> typing.List[DatumConstraint]:
        ...
    def SetConstraints(self, constraints: typing.List[DatumConstraint]) -> None:
        ...


class DatumAxisFeature(Features.DatumFeature):
    def __init__(self) -> None: ...
    DatumAxis: DatumAxis


class DatumAxisBuilder(Features.DatumBuilder):
    def __init__(self) -> None: ...
    def SetPointAndDirection(self, point: Point, direction: Direction) -> None:
        ...
    def SetTwoPoints(self, point1: Point, point2: Point, useArcLength: Features.DatumAxisBuilder.UseArcLength) -> None:
        ...
    def SetPointOnCurve(self, arcLength: float, constraint: str, alternateSolution: Features.DatumAxisBuilder.AlternateSolution, option: Features.DatumAxisBuilder.CurveOption, curve: ICurve) -> None:
        ...
    def SetPointOnCurve(self, arcLength: float, constraint: str, option: Features.DatumAxisBuilder.CurveOption, curve: ICurve, secondGeometry: DisplayableObject) -> None:
        ...
    def SetPointOnCurve(self, arcLength: float, constraint: str, option: Features.DatumAxisBuilder.CurveOption, secondGeometry: DisplayableObject, curve: ICurve) -> None:
        ...
    def SetGeometryAndConstraints(self, geometry1: DisplayableObject, geometryConstraintType1: Features.DatumAxisBuilder.ConstraintType, constraintAttribute1: int, constraintValue1: float, constraint1: str, geometry2: DisplayableObject, geometryConstraintType2: Features.DatumAxisBuilder.ConstraintType, constraintAttribute2: int, constraintValue2: float, constraint2: str, direction: Sense) -> None:
        ...
    def SetFixedDatumAxis(self, type: Features.DatumAxisBuilder.FixedType) -> None:
        ...
    def EvaluatePath(self, section: Section) -> None:
        ...
    AlternateSolutionType: Features.DatumAxisBuilder.AlternateSolution
    ArcLength: GeometricUtilities.OnPathDimensionBuilder
    Curve: SelectICurve
    CurveOrFace: SelectNXObject
    CurveOrientation: Features.DatumAxisBuilder.CurveOrientations
    DirectionOrientation: Features.DatumAxisBuilder.DirectionOrientations
    IsAssociative: bool
    IsAxisReversed: bool
    Object1: SelectNXObject
    Object2: SelectNXObject
    Objects: SelectNXObjectList
    OrientationObject: SelectNXObject
    Point: Point
    Point1: Point
    Point2: Point
    ResizedEndDistance: float
    ReverseDirection: bool
    Section: Section
    Type: Features.DatumAxisBuilder.Types
    Vector: Direction


    class UseArcLength(enum.Enum):
        NoPoint = 0
        FirstPoint = 1
        SecondPoint = 2
        AllPoints = 3
    

    class Types(enum.Enum):
        Inferred = 0
        Intersection = 1
        CurveOrFaceAxis = 2
        OnCurveVector = 3
        XcAxis = 4
        YcAxis = 5
        ZcAxis = 6
        PointAndDir = 7
        TwoPoints = 8
        Fixed = 9
    

    class FixedType(enum.Enum):
        All = 0
        X = 1
        Y = 2
        Z = 3
    

    class DirectionOrientations(enum.Enum):
        ParallelToVector = 0
        PerpendicularToVector = 1
    

    class CurveOrientations(enum.Enum):
        Tangent = 0
        Normal = 1
        Binormal = 2
        PerpendicularToObject = 3
        ParallelToObject = 4
    

    class CurveOption(enum.Enum):
        Distance = 0
        Percent = 1
    

    class ConstraintType(enum.Enum):
        Undefined = 0
        Coincident = 1
        Parallel = 2
        Perpendicular = 3
        Center = 4
        Tangent = 5
        Distance = 6
        Angle = 7
        Frenet = 8
    

    class AlternateSolution(enum.Enum):
        Undefined = 0
        Tangent = 1
        Normal = 2
        Binormal = 3
        OppositeTangent = 4
        OppositeNormal = 5
        OppositeBinormal = 6
        Project = 7
    

class CylinderBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Arc: SelectICurve
    Axis: Axis
    BooleanOption: GeometricUtilities.BooleanOperation
    Diameter: Expression
    Direction: Vector3d
    Height: Expression
    Origin: Point3d
    ParentAssociativity: bool
    ReverseDirection: bool
    Type: Features.CylinderBuilder.Types


    class Types(enum.Enum):
        AxisDiameterAndHeight = 0
        ArcAndHeight = 1
    

class Cylinder(Features.BodyFeature):
    def __init__(self) -> None: ...


class CutFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DoPaste: bool
    FaceToCut: Features.FaceRecognitionBuilder
    Motion: GeometricUtilities.ModlMotion
    ReverseDirection: bool
    TargetBody: SelectBody


class CutFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class CustomTagAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    Value: TaggedObject


class CustomTagArrayAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    def SetValues(self, tagValues: typing.List[TaggedObject]) -> typing.List[TaggedObject]:
        ...
    def GetValues(self) -> typing.List[TaggedObject]:
        ...


class CustomStringAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    Value: str


class CustomStringArrayAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    def SetValues(self, stringValues: str) -> None:
        ...
    def GetValues(self) -> str:
        ...


class CustomLogicalAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    Value: bool


class CustomLogicalArrayAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    def SetValues(self, logicalValues: bool) -> None:
        ...
    def GetValues(self) -> bool:
        ...


class CustomIntegerAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    Value: int


class CustomIntegerArrayAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    def SetValues(self, intValues: int) -> None:
        ...
    def GetValues(self) -> int:
        ...


class CustomFeatureSelectionFilter(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def Filter(self, objectToFilter: NXObject) -> int:
        ...


class CustomFeaturePreUpdateEvent(Features.CustomFeatureEvent):
    def __init__(self) -> None: ...
    def SetConstructionFeatures(self, constructionFeaturesTags: typing.List[Features.ConstructionFeatureData]) -> None:
        ...
    def CreateConstructionFeatureData(self, feature: Features.Feature) -> Features.ConstructionFeatureData:
        ...


class CustomFeaturePostUpdateEvent(Features.CustomFeatureEvent):
    def __init__(self) -> None: ...
    def SetOutputFeatures(self, outputFeatureData: typing.List[Features.OutputFeatureData]) -> None:
        ...
    def CreateOutputFeatureData(self, feature: Features.Feature) -> Features.OutputFeatureData:
        ...


class CustomFeatureModifyFeatureGeometryEvent(Features.CustomFeatureEvent):
    def __init__(self) -> None: ...
    def Getbodies(self) -> typing.List[Features.CustomFeatureEvent.ParasolidId]:
        """[Obsolete("Deprecated in NX12.0.1.  Please use CustomFeatureModifyFeatureGeometryEvent.GetCreatedBodies instead, this api will not return any bodies.")"""
        ...
    def GetCreatedBodies(self) -> typing.List[Features.CustomFeatureEvent.ParasolidId]:
        ...
    def CreateTrackingDataForNXObject(self, nxObject: TaggedObject) -> Features.TrackingData:
        ...
    def AppendOutputTrackingData(self, trackingData: typing.List[Features.TrackingData]) -> None:
        ...


class CustomFeatureInternalFeaturePreUpdateEvent(Features.CustomFeatureEvent):
    def __init__(self) -> None: ...
    def GetFeature(self) -> Features.Feature:
        ...


class CustomFeatureInformationEvent(Features.CustomFeatureEvent):
    def __init__(self) -> None: ...
    def SetInformation(self, information: str) -> None:
        ...


class CustomFeatureHighlightEvent(Features.CustomFeatureEvent):
    def __init__(self) -> None: ...
    def ObjectsToHighlightUnhighlight(self, objectsToHighlight: typing.List[DisplayableObject]) -> None:
        ...
    def GetHighlightFlag(self) -> bool:
        ...
    def GetHighlightOnlySuppliedObjectsOption(self) -> bool:
        ...
    def SetHighlightOnlySuppliedObjectsOption(self, highlightOption: bool) -> None:
        ...


class CustomFeatureEvent(TaggedObject):
    def __init__(self) -> None: ...
    def GetParasolidId(self, solidTag: DisplayableObject) -> Features.CustomFeatureEvent.ParasolidId:
        ...
    def GetNXObject(self, parasolidId: Features.CustomFeatureEvent.ParasolidId) -> DisplayableObject:
        ...
    def GetConstructionFeatures(self) -> typing.List[Features.ConstructionFeatureData]:
        ...
    def GetOutputFeatures(self) -> typing.List[Features.OutputFeatureData]:
        ...
    def GetCustomFeature(self) -> Features.CustomFeature:
        ...
    ErrorCode: int


    

class CustomFeatureDataCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def CreateData(self, cfclass: Features.CustomFeatureClass, attrs: typing.List[Features.CustomAttribute]) -> Features.CustomFeatureData:
        ...
    def Tag(self) -> Tag: ...



class CustomFeatureData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetAllCustomAttributeNameAndTypes(self, attributeNames: str, attributeType: typing.List[Features.CustomAttribute.Type]) -> None:
        ...
    def AddCustomAttributes(self, attributes: typing.List[Features.CustomAttribute]) -> None:
        ...
    def CustomTagAttributeByName(self, attributeName: str) -> Features.CustomTagAttribute:
        ...
    def CustomTagArrayAttributeByName(self, attributeName: str) -> Features.CustomTagArrayAttribute:
        ...
    def CustomStringAttributeByName(self, attributeName: str) -> Features.CustomStringAttribute:
        ...
    def CustomStringArrayAttributeByName(self, attributeName: str) -> Features.CustomStringArrayAttribute:
        ...
    def CustomLogicalAttributeByName(self, attributeName: str) -> Features.CustomLogicalAttribute:
        ...
    def CustomLogicalArrayAttributeByName(self, attributeName: str) -> Features.CustomLogicalArrayAttribute:
        ...
    def CustomIntegerAttributeByName(self, attributeName: str) -> Features.CustomIntegerAttribute:
        ...
    def CustomIntegerArrayAttributeByName(self, attributeName: str) -> Features.CustomIntegerArrayAttribute:
        ...
    def CustomExpressionAttributeByName(self, attributeName: str) -> Features.CustomExpressionAttribute:
        ...
    def CustomExpressionArrayAttributeByName(self, attributeName: str) -> Features.CustomExpressionArrayAttribute:
        ...
    def CustomDoubleAttributeByName(self, attributeName: str) -> Features.CustomDoubleAttribute:
        ...
    def CustomDoubleArrayAttributeByName(self, attributeName: str) -> Features.CustomDoubleArrayAttribute:
        ...
    def HasCustomAttribute(self, attributeName: str, type: Features.CustomAttribute.Type) -> bool:
        ...
    ClassName: str


class CustomFeatureCreateFeatureGeometryEvent(Features.CustomFeatureEvent):
    def __init__(self) -> None: ...
    def GetBodies(self) -> typing.List[Features.CustomFeatureEvent.ParasolidId]:
        ...
    def SetBodies(self, bodies: typing.List[Features.CustomFeatureEvent.ParasolidId]) -> None:
        ...
    def CreateTrackingDataForParasolidEntity(self, parasolidId: Features.CustomFeatureEvent.ParasolidId) -> Features.TrackingData:
        ...
    def CreateTrackingDataForNXObject(self, nxObject: TaggedObject) -> Features.TrackingData:
        ...
    def AppendOutputTrackingData(self, trackingData: typing.List[Features.TrackingData]) -> None:
        ...
    def CopyNXBody(self, solidTag: Body, parasolidBodyId: Features.CustomFeatureEvent.ParasolidId, sourceFaces: typing.List[Face], parasolidFaceIds: typing.List[Features.CustomFeatureEvent.ParasolidId], sourceEdges: typing.List[Edge], parasolidEdgeId: typing.List[Features.CustomFeatureEvent.ParasolidId]) -> None:
        ...


class CustomFeatureClassManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetClassFromName(self, className: str) -> Features.CustomFeatureClass:
        ...
    def GetEditedCustomFeature(self) -> Features.CustomFeature:
        ...
    def CreateCustomFeatureSelectionFilter(self) -> Features.CustomFeatureSelectionFilter:
        ...
    def Tag(self) -> Tag: ...



class CustomFeatureClass(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddInternalFeaturePreUpdateHandler(self, internalFeaturePreUpdateCallback: Features.CustomFeatureClass.InternalFeaturePreUpdateCallback) -> None:
        ...
    def AddPreUpdateHandler(self, preUpdateCallback: Features.CustomFeatureClass.PreUpdateCallback) -> None:
        ...
    def AddCreateFeatureGeometryHandler(self, createFeatureGeometryCallback: Features.CustomFeatureClass.CreateFeatureGeometryCallback) -> None:
        ...
    def AddModifyFeatureGeometryHandler(self, modifyFeatureGeometryCallback: Features.CustomFeatureClass.ModifyFeatureGeometryCallback) -> None:
        ...
    def AddPostUpdateHandler(self, postUpdateCallback: Features.CustomFeatureClass.PostUpdateCallback) -> None:
        ...
    def AddInformationHandler(self, informationCallback: Features.CustomFeatureClass.InformationCallback) -> None:
        ...
    def AddHighlightHandler(self, highlightCallback: Features.CustomFeatureClass.HighlightCallback) -> None:
        ...


    

    

    

    

    

    

    

class CustomFeatureBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FeatureData: Features.CustomFeatureData


class CustomFeature(Features.Feature):
    def __init__(self) -> None: ...
    def GetBodies(self) -> typing.List[Body]:
        ...
    def GetConstructionFeatures(self) -> typing.List[Features.ConstructionFeatureData]:
        ...
    def GetOutputFeatures(self) -> typing.List[Features.OutputFeatureData]:
        ...
    FeatureData: Features.CustomFeatureData


class CustomExpressionAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    Value: Expression


class CustomExpressionArrayAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    def SetValues(self, expressionValues: typing.List[Expression]) -> None:
        ...
    def GetValues(self) -> typing.List[Expression]:
        ...


class CustomDoubleAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    Value: float


class CustomDoubleArrayAttribute(Features.CustomAttribute):
    def __init__(self, ptr: int) -> None: ...
    def SetValues(self, doubleValues: float) -> None:
        ...
    def GetValues(self) -> float:
        ...


class CustomAttributeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def CreateCustomTagAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomTagAttribute:
        ...
    def CreateCustomTagArrayAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomTagArrayAttribute:
        ...
    def CreateCustomStringAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomStringAttribute:
        ...
    def CreateCustomStringArrayAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomStringArrayAttribute:
        ...
    def CreateCustomLogicalAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomLogicalAttribute:
        ...
    def CreateCustomLogicalArrayAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomLogicalArrayAttribute:
        ...
    def CreateCustomIntegerAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomIntegerAttribute:
        ...
    def CreateCustomIntegerArrayAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomIntegerArrayAttribute:
        ...
    def CreateCustomExpressionAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomExpressionAttribute:
        ...
    def CreateCustomExpressionArrayAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomExpressionArrayAttribute:
        ...
    def CreateCustomDoubleAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomDoubleAttribute:
        ...
    def CreateCustomDoubleArrayAttribute(self, attributeName: str, attributeProperties: typing.List[Features.CustomAttribute.Property]) -> Features.CustomDoubleArrayAttribute:
        ...
    def Tag(self) -> Tag: ...



class CustomAttribute(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddProperty(self, attributeProperty: Features.CustomAttribute.Property) -> None:
        ...
    def RemoveProperty(self, attributeProperty: Features.CustomAttribute.Property) -> None:
        ...
    def HasProperty(self, attributeProperty: Features.CustomAttribute.Property) -> bool:
        ...
    def GetProperties(self) -> typing.List[Features.CustomAttribute.Property]:
        ...
    Name: str
    TypeValue: Features.CustomAttribute.Type


    class Type(enum.Enum):
        Unknown = 0
        Expression = 1
        ExpressionVla = 2
        Tag = 3
        TagVla = 4
        Bool = 5
        BoolVla = 6
        Integer = 7
        IntegerVla = 8
        Double = 9
        DoubleVla = 10
        String = 11
        StringVla = 12
    

    class Property(enum.Enum):
        IsOutputAttribute = 1
        IsOwnedAttribute = 2
        IsReferencingTargetBody = 4
        MandatoryInput = 8
    

class CurveOnSurfaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    ConstraintManager: Features.GeometricConstraintDataManager
    CurveFitData: GeometricUtilities.CurveFitData
    CurveFitProperties: GeometricUtilities.CurveFitOptions
    DistanceTolerance: float
    Faces: ScCollector
    IsPeriodic: bool


class CurveOnSurface(Features.Feature):
    def __init__(self) -> None: ...


class CurveLengthBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CurveOptions: GeometricUtilities.CurveOptions
    CurvelengthData: GeometricUtilities.CurveLengthData
    DistanceTolerance: float
    Section: Section


class CurveLength(Features.Feature):
    def __init__(self) -> None: ...


class CurveFinderBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SelectCurves(self, curves: typing.List[NXObject]) -> None:
        ...
    def DeselectCurves(self, curves: typing.List[NXObject]) -> None:
        ...
    def SelectSymmetryReference(self, symmetryReference: NXObject) -> None:
        ...
    def DeselectSymmetryReference(self, symmetryReference: NXObject) -> None:
        ...
    def AddTangent(self) -> None:
        ...
    def RemoveTangent(self) -> None:
        ...
    def AddTangentSketchGroup(self) -> None:
        ...
    def RemoveTangentSketchGroup(self) -> None:
        ...
    def AddTangent2dComponent(self) -> None:
        ...
    def RemoveTangent2dComponent(self) -> None:
        ...
    def AddParallel(self) -> None:
        ...
    def RemoveParallel(self) -> None:
        ...
    def AddParallelSketchGroup(self) -> None:
        ...
    def RemoveParallelSketchGroup(self) -> None:
        ...
    def AddParallel2dComponent(self) -> None:
        ...
    def RemoveParallel2dComponent(self) -> None:
        ...
    def AddOffset(self) -> None:
        ...
    def RemoveOffset(self) -> None:
        ...
    def AddOffsetSketchGroup(self) -> None:
        ...
    def RemoveOffsetSketchGroup(self) -> None:
        ...
    def AddOffset2dComponent(self) -> None:
        ...
    def RemoveOffset2dComponent(self) -> None:
        ...
    def AddCoincident(self) -> None:
        ...
    def RemoveCoincident(self) -> None:
        ...
    def AddCoincidentSketchGroup(self) -> None:
        ...
    def RemoveCoincidentSketchGroup(self) -> None:
        ...
    def AddCoincident2dComponent(self) -> None:
        ...
    def RemoveCoincident2dComponent(self) -> None:
        ...
    def AddVertexOnCurve(self) -> None:
        ...
    def RemoveVertexOnCurve(self) -> None:
        ...
    def AddVertexOnCurveSketchGroup(self) -> None:
        ...
    def RemoveVertexOnCurveSketchGroup(self) -> None:
        ...
    def AddVertexOnCurve2dComponent(self) -> None:
        ...
    def RemoveVertexOnCurve2dComponent(self) -> None:
        ...
    def AddChamfer(self) -> None:
        ...
    def RemoveChamfer(self) -> None:
        ...
    def AddConlinear(self) -> None:
        ...
    def RemoveConlinear(self) -> None:
        ...
    def AddConlinearSketchGroup(self) -> None:
        ...
    def RemoveConlinearSketchGroup(self) -> None:
        ...
    def AddConlinear2dComponent(self) -> None:
        ...
    def RemoveConlinear2dComponent(self) -> None:
        ...
    def AddConcentric(self) -> None:
        ...
    def RemoveConcentric(self) -> None:
        ...
    def AddConcentricSketchGroup(self) -> None:
        ...
    def RemoveConcentricSketchGroup(self) -> None:
        ...
    def AddConcentric2dComponent(self) -> None:
        ...
    def RemoveConcentric2dComponent(self) -> None:
        ...
    def AddEqualRadius(self) -> None:
        ...
    def RemoveEqualRadius(self) -> None:
        ...
    def AddEqualRadiusSketchGroup(self) -> None:
        ...
    def RemoveEqualRadiusSketchGroup(self) -> None:
        ...
    def AddEqualRadius2dComponent(self) -> None:
        ...
    def RemoveEqualRadius2dComponent(self) -> None:
        ...
    def AddSymmetric(self, planeType: int) -> None:
        ...
    def RemoveSymmetric(self, planeType: int) -> None:
        ...
    def FindRelationCurve(self, selectedCurves: typing.List[NXObject]) -> None:
        ...
    def FindScopeCurve(self, selectedCurves: typing.List[NXObject]) -> None:
        ...
    def RemoveEngineNodes(self) -> None:
        ...
    def RestoreEngineNodes(self) -> None:
        ...
    def SetDistanceTolerance(self, distanceTolerance: float) -> None:
        ...
    def RemoveIncludedConstraints(self) -> None:
        ...
    def RecognizeRigid(self, constraintTag: NXObject) -> None:
        ...
    def UnrecognizeRigid(self, constraintTag: NXObject) -> None:
        ...
    def SelectSnapPoint(self, selectedCurve: TaggedObject, point: Point3d) -> None:
        ...
    def DeselectSnapPoint(self, selectedCurve: TaggedObject, point: Point3d) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ChamferEnabled: bool
    CoincidentVertex2dComponentEnabled: bool
    CoincidentVertexEnabled: bool
    CoincidentVertexSketchGroupEnabled: bool
    Collinear2dComponentEnabled: bool
    CollinearEnabled: bool
    CollinearSketchGroupEnabled: bool
    CompoundGeometryRelationScope: int
    Concentric2dComponentEnabled: bool
    ConcentricEnabled: bool
    ConcentricSketchGroupEnabled: bool
    CurvePointList: SelectDisplayableObjectList
    CurveSection: ScCollector
    EqualRadius2dComponentEnabled: bool
    EqualRadiusEnabled: bool
    EqualRadiusSketchGroupEnabled: bool
    FindScopeOption: int
    Offset2dComponentEnabled: bool
    OffsetEnabled: bool
    OffsetSketchGroupEnabled: bool
    Parallel2dComponentEnabled: bool
    ParallelEnabled: bool
    ParallelSketchGroupEnabled: bool
    RelationScope: int
    SketchGroupRelationScope: int
    SymmetricEnabled: bool
    SymmetryOption: int
    SymmetryReference: SelectNXObject
    Tangent2dComponentEnabled: bool
    TangentEnabled: bool
    TangentSketchGroupEnabled: bool
    UseCurveFinder: bool
    VertexOnCurve2dComponentEnabled: bool
    VertexOnCurveEnabled: bool
    VertexOnCurveSketchGroupEnabled: bool


class CurveFeatureCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def CreateOffset3dCurveBuilder(self, offset3DCurve: Features.Offset3DCurve) -> Features.Offset3DCurveBuilder:
        ...
    def CreateScaleCurveBuilder(self, scaleCurve: Features.ScaleCurve) -> Features.ScaleCurveBuilder:
        ...
    def Tag(self) -> Tag: ...



class CurveFeature(Features.Feature):
    def __init__(self) -> None: ...
    Color: int
    Font: DisplayableObject.ObjectFont
    Layer: int
    SuppressChildren: bool
    Width: DisplayableObject.ObjectWidth


class CopyPasteBuilder(Builder):
    def __init__(self) -> None: ...
    def GetFeatureReferences(self) -> Features.FeatureReferencesBuilder:
        ...
    def UpdateBuilder(self) -> None:
        ...
    def GetBuilderVersion(self) -> Features.CopyPasteBuilder.BuilderVersion:
        ...
    def SetBuilderVersion(self, version: Features.CopyPasteBuilder.BuilderVersion) -> None:
        ...
    Associative: bool
    CopyResolveGeometry: bool
    ExpressionOption: Features.CopyPasteBuilder.ExpressionTransferOption
    ParentOption: Features.CopyPasteBuilder.ParentTransferOption
    SelectOption: Features.CopyPasteBuilder.ParentSelectOption


    class ParentTransferOption(enum.Enum):
        PromptForNew = 0
        CopyOriginalCurve = 1
        OriginalInstance = 2
    

    class ParentSelectOption(enum.Enum):
        SmartObject = 0
        InputForOriginalParent = 1
    

    class ExpressionTransferOption(enum.Enum):
        CreateNew = 0
        LinkToOriginal = 1
        OriginalInstance = 2
    

    class BuilderVersion(enum.Enum):
        Original = 0
        ExposeOnflySo = 1
        ExposeBody = 2
        ShowParentSelectOption = 4
    

class CopyFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DoPaste: bool
    FaceToCopy: Features.FaceRecognitionBuilder
    Motion: GeometricUtilities.ModlMotion
    ReverseDirection: bool
    TargetBody: SelectBody


class CopyFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class CoplanarBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ConstraintFace: SelectFace
    FaceChangeOverflowBehavior: GeometricUtilities.FaceChangeOverflowBehavior
    RigidFace: Features.FaceRecognitionBuilder
    StationaryFace: SelectISurface


class Coplanar(Features.BodyFeature):
    def __init__(self) -> None: ...


class ConvertToSheetmetal(Features.Feature):
    def __init__(self) -> None: ...


class ContourFlange(Features.Feature):
    def __init__(self) -> None: ...


class ConstructionFeatureData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFeature(self) -> Features.Feature:
        ...
    ShowInGraphicView: bool


class ConeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Axis: Axis
    BaseArc: SelectICurve
    BaseDiameter: Expression
    BooleanOption: GeometricUtilities.BooleanOperation
    HalfAngle: Expression
    Height: Expression
    ParentAssociativity: bool
    TopArc: SelectICurve
    TopDiameter: Expression
    Type: Features.ConeBuilder.Types


    class Types(enum.Enum):
        DiametersAndHeight = 0
        DiametersAndHalfAngle = 1
        BaseDiameterHeightAndHalfAngle = 2
        TopDiameterHeightAndHalfAngle = 3
        TwoCoaxialArcs = 4
    

class Cone(Features.BodyFeature):
    def __init__(self) -> None: ...


class ConcaveFacesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CalculatePointCurvature(self, faceId: Face, point: Point3d, radius: float, minRadius: float, maxRadius: float) -> None:
        ...
    def UpdateRadiusFaces(self) -> None:
        ...
    def UpdateLocationLabel(self, edit: bool, point: Point) -> None:
        ...
    def SetFaceAttributeColor(self, attributeColor: NXColor) -> None:
        ...
    def UpdateSelectedFacesColor(self) -> None:
        ...
    def SetTreeSelectedIndex(self, indexArray: int) -> None:
        ...
    def SetFaceGroupAttributeTitle(self, grpAttributeTitle: str) -> None:
        ...
    def SetFaceGroupAttributeValue(self, grpAttributeValue: str) -> None:
        ...
    AngleTolerance: float
    AttributeColor: NXColor
    AttributeTitle: str
    AttributeValue: str
    DistanceTolerance: float
    DrawDirection: Direction
    Faces: ScCollector
    GroupInterval: float
    Lower: Expression
    ReverseNormalDirection: bool
    SamplePoints: int
    Upper: Expression
    UseSurfaceNormal: bool


class ConcaveFaces(Features.BodyFeature):
    def __init__(self) -> None: ...


class CompositeCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CommitCreateOnTheFly(self) -> Features.Feature:
        ...
    def GetWaveLinkInformation(self, info: str, xformExists: bool, xformOrigin: Point3d, xformOrientation: Matrix3x3, xformScale: float) -> None:
        ...
    def GetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def SetProductInterfaceObjects(self, selectedObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def GetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    def SetSourcePartOccurrences(self, sourcePartOccurrences: typing.List[TaggedObject]) -> None:
        ...
    AllowSelfIntersection: bool
    Associative: bool
    CurveFitData: GeometricUtilities.CurveFitData
    FixAtCurrentTimestamp: bool
    FrecAtTimeStamp: Features.Feature
    HideOriginal: bool
    InheritDisplayProperties: bool
    JoinOption: Features.CompositeCurveBuilder.JoinMethod
    MakePositionIndependent: bool
    ParentPart: Features.CompositeCurveBuilder.PartType
    ReverseDirection: bool
    Section: Section
    SourcePartOccurrence: TaggedObject
    Tolerance: float


    class PartType(enum.Enum):
        WorkPart = 0
        OtherPart = 1
    

    class JoinMethod(enum.Enum):
        No = 0
        Cubic = 1
        Genernal = 2
        Quintic = 3
    

class CompositeCurve(Features.Feature):
    def __init__(self) -> None: ...


class CompensateRoughData(Features.BodyFeature):
    def __init__(self) -> None: ...


class CombineSheetsBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Bodies: ScCollector
    Regions: GeometricUtilities.BooleanRegionSelect


class CombineSheets(Features.BodyFeature):
    def __init__(self) -> None: ...


class CombinedProjectionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Curve1: Section
    Curve2: Section
    CurveFit: GeometricUtilities.CurveFitOptions
    CurveFitData: GeometricUtilities.CurveFitData
    CurveOptions: GeometricUtilities.CurveOptions
    Direction1: GeometricUtilities.ProjectionOptions
    Direction2: GeometricUtilities.ProjectionOptions


class CombinedProjection(Features.Feature):
    def __init__(self) -> None: ...


class CombineBodyFeature(Features.BodyFeature):
    def __init__(self) -> None: ...
    def IsolateToolBodies(self) -> None:
        ...


class ColorFeatureGroupBuilder(Builder):
    def __init__(self) -> None: ...
    Color: NXColor
    Operation: Features.ColorFeatureGroupBuilder.OperationType
    Process: Features.ColorFeatureGroupBuilder.ProcessType
    SelectFeature: Features.SelectFeatureList


    class ProcessType(enum.Enum):
        NewFeatures = 0
        AllMembers = 1
        FirstLevelMembers = 2
    

    class OperationType(enum.Enum):
        SpecifyColor = 0
        NoColor = 1
    

class ColorFeatureBuilder(Builder):
    def __init__(self) -> None: ...
    Color: NXColor
    SelectFeature: Features.SelectFeatureList
    SpecifyColor: Features.ColorFeatureBuilder.OperationType
    StoreColor: bool


    class OperationType(enum.Enum):
        SpecifyColor = 0
        NoColor = 1
    

class ColorFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Color: NXColor
    Face: ScCollector


class CoaxialBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FaceChangeOverflowBehavior: GeometricUtilities.FaceChangeOverflowBehavior
    MotionFace: SelectFace
    MoveAlongFace: Features.FaceRecognitionBuilder
    StationaryFace: SelectDisplayableObject


class Coaxial(Features.BodyFeature):
    def __init__(self) -> None: ...


class ClosedCorner(Features.Feature):
    def __init__(self) -> None: ...


class CircularBlendCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ComplementArc(self) -> None:
        ...
    def Evaluate(self) -> None:
        ...
    Associative: bool
    CurveFitMethod: GeometricUtilities.CurveFitOptions
    CylinderRadius: Expression
    DirectionOption: Features.CircularBlendCurveBuilder.CylinderDirectionOption
    DistanceTolerance: float
    FirstCurve: Section
    PointArclength: GeometricUtilities.OnPathDimensionBuilder
    RadiusOption: Features.CircularBlendCurveBuilder.CylinderRadiusOption
    SecondCurve: Section
    ShapeControlFirstCurve: float
    ShapeControlSecondCurve: float
    Vector: Direction


    class CylinderRadiusOption(enum.Enum):
        PointOnFirstCurve = 0
        PointOnSecondCurve = 1
        Value = 2
    

    class CylinderDirectionOption(enum.Enum):
        BestFit = 0
        Variable = 1
        Vector = 2
        CurrentView = 3
    

class CircularBlendCurve(Features.Feature):
    def __init__(self) -> None: ...


class ChangeShellThicknessBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def AddEntities(self, entities: typing.List[NXObject]) -> None:
        ...
    def RemoveEntities(self, entities: typing.List[NXObject]) -> None:
        ...
    FacesToChangeThickness: Features.FaceRecognitionBuilder
    NeighborsEnabled: bool
    WallThickness: Expression


class ChangeShellThickness(Features.BodyFeature):
    def __init__(self) -> None: ...


class ChamferBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreatePreview(self) -> int:
        ...
    AllInstances: bool
    Angle: str
    AngleExp: Expression
    FirstOffset: str
    FirstOffsetExp: Expression
    Method: Features.ChamferBuilder.OffsetMethod
    Option: Features.ChamferBuilder.ChamferOption
    ReverseOffsets: bool
    SecondOffset: str
    SecondOffsetExp: Expression
    SmartCollector: ScCollector
    Tolerance: float


    class OffsetMethod(enum.Enum):
        EdgesAlongFaces = 0
        FacesAndTrim = 1
    

    class ChamferOption(enum.Enum):
        SymmetricOffsets = 0
        TwoOffsets = 1
        OffsetAndAngle = 2
    

class Chamfer(Features.BodyFeature):
    def __init__(self) -> None: ...


class BridgeTransition(Features.CombineBodyFeature):
    def __init__(self) -> None: ...


class BridgeSurfaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ConstructSurfaceBoundaryCurve(self, startBoundary: bool) -> None:
        ...
    EdgeFlowDirection: GeometricUtilities.FlowDirection
    EdgeTangentMagnitude: GeometricUtilities.TangentMagnitudeBuilder
    FirstEdgeContinuity: GeometricUtilities.Continuity
    FirstEdgeOffset: GeometricUtilities.OnPathDimensionBuilder
    FirstEdgeRange: GeometricUtilities.CurveRangeBuilder
    FirstEdgeSelection: SelectNXObject
    G0Tolerance: float
    G1Tolerance: float
    G2Tolerance: float
    IsEndHandlesLinked: bool
    IsFirstEdgeContinuityReversed: bool
    IsFirstEdgeLimitEndToEnd: bool
    IsFirstEdgeReversed: bool
    IsSecondEdgeContinuityReversed: bool
    IsSecondEdgeLimitEndToEnd: bool
    IsSecondEdgeReversed: bool
    IsStartHandlesLinked: bool
    Rebuild: GeometricUtilities.Rebuild
    SecondEdgeContinuity: GeometricUtilities.Continuity
    SecondEdgeOffset: GeometricUtilities.OnPathDimensionBuilder
    SecondEdgeRange: GeometricUtilities.CurveRangeBuilder
    SecondEdgeSelection: SelectNXObject


class BridgeSurface(Features.BodyFeature):
    def __init__(self) -> None: ...


class BridgeCurveBuilderEx(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def UpdateOnEndVectorReversal(self) -> None:
        ...
    def Evaluate(self) -> None:
        ...
    ConstraintFaces: ScCollector
    ConstraintRadius: Expression
    CurveFitData: GeometricUtilities.CurveFitData
    DepthSkew: GeometricUtilities.DepthSkewBuilder
    EndConnectivity: GeometricUtilities.BridgeCurveConnectivity
    EndObject: SelectNXObject
    EndObjectType: Features.BridgeCurveBuilderEx.EndObjectTypes
    EndSection: Section
    EndVector: Direction
    IsAssociative: bool
    RadiusConstraintMethod: Features.BridgeCurveBuilderEx.RadiusConstraintMethods
    Rho: Expression
    ShapeControlMethod: Features.BridgeCurveBuilderEx.ShapeControlMethods
    StartConnectivity: GeometricUtilities.BridgeCurveConnectivity
    StartObject: SelectNXObject
    StartObjectType: Features.BridgeCurveBuilderEx.StartObjectTypes
    StartSection: Section
    TangentMagnitude: GeometricUtilities.TangentMagnitudeBuilder
    TemplateCurve: SelectCurve
    UseNearestPointOnSection: bool


    class StartObjectTypes(enum.Enum):
        Section = 0
        Object = 1
    

    class ShapeControlMethods(enum.Enum):
        TangentMagnitude = 0
        DepthSkew = 1
        Conic = 2
        TemplateCurve = 3
    

    class RadiusConstraintMethods(enum.Enum):
        None = 0
        Minimum = 1
        Peak = 2
    

    class EndObjectTypes(enum.Enum):
        Section = 0
        Object = 1
        Datum = 2
        Vector = 3
    

class BridgeCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ConstraintFaces: ScCollector
    CurveFitData: GeometricUtilities.CurveFitData
    CurveFitOption: Features.BridgeCurveBuilder.CurveFitTypes
    Depth: Expression
    EndContinuityOption: Features.BridgeCurveBuilder.ConstraintTypes
    EndCurveDirectionOption: Features.BridgeCurveBuilder.CurveDirectionTypes
    EndDirectionAngle: Expression
    EndObject: SelectObject
    EndObjectOption: Features.BridgeCurveBuilder.EndObjectTypes
    EndPerpendicularFace: SelectObject
    EndPointDirection: Direction
    EndReferencePoint: Point
    EndSurfaceDirectionOption: Features.BridgeCurveBuilder.SurfaceDirectionTypes
    EndTangentMagnitude: Expression
    EndVectorObject: Direction
    IsAssociative: bool
    MaximumDegree: int
    MaximumSegment: int
    MinimumRadiusOption: Features.BridgeCurveBuilder.MinRadiusTypes
    MinimumRadiusValue: Expression
    ObjectSelectionOption: Features.BridgeCurveBuilder.SelectedObject
    ReverseEndDirection: bool
    ReverseStartDirection: bool
    Rho: Expression
    ShapeControlOption: Features.BridgeCurveBuilder.ShapeControlTypes
    ShapeCurve: SelectObject
    Skew: Expression
    StartContinuityOption: Features.BridgeCurveBuilder.ConstraintTypes
    StartCurveDirectionOption: Features.BridgeCurveBuilder.CurveDirectionTypes
    StartDirectionAngle: Expression
    StartObject: SelectObject
    StartPerpendicularFace: SelectObject
    StartPointDirection: Direction
    StartReferencePoint: Point
    StartSurfaceDirectionOption: Features.BridgeCurveBuilder.SurfaceDirectionTypes
    StartTangentMagnitude: Expression
    Tolerance: float
    UPercentEnd: Expression
    UPercentStart: Expression
    VPercentEnd: Expression
    VPercentStart: Expression


    class SurfaceDirectionTypes(enum.Enum):
        Sectional = 0
        IsoU = 1
        IsoV = 2
    

    class ShapeControlTypes(enum.Enum):
        EndPoint = 0
        PeakPoint = 1
        Conic = 2
        ShapeCurve = 3
    

    class SelectedObject(enum.Enum):
        One = 0
        Two = 1
    

    class MinRadiusTypes(enum.Enum):
        None = 0
        Minimum = 1
        Peak = 2
    

    class EndObjectTypes(enum.Enum):
        Object = 0
        Vector = 1
    

    class CurveFitTypes(enum.Enum):
        Cubic = 0
        Quintic = 1
        Advanced = 2
    

    class CurveDirectionTypes(enum.Enum):
        Tangent = 0
        Perpendicular = 1
    

    class ConstraintTypes(enum.Enum):
        G0 = 0
        G1 = 1
        G2 = 2
        G3 = 3
    

class BridgeCurve(Features.CurveFeature):
    def __init__(self) -> None: ...


class Brep(Features.BodyFeature):
    def __init__(self) -> None: ...
    def ConvertToLinkedBody(self) -> None:
        ...


class BreakCorner(Features.Feature):
    def __init__(self) -> None: ...


class BoundedPlaneBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BoundingCurves: Section


class BoundedPlane(Features.BodyFeature):
    def __init__(self) -> None: ...


class BooleanFeature(Features.CombineBodyFeature):
    def __init__(self) -> None: ...
    Target: Body
    Tool: Body


class BooleanBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BooleanRegionSelect: GeometricUtilities.BooleanRegionSelect
    ConvertToSew: bool
    CopyTargets: bool
    CopyTools: bool
    Operation: Features.Feature.BooleanType
    RetainTarget: bool
    RetainTool: bool
    Target: Body
    Targets: SelectBodyList
    Tolerance: float
    Tool: DisplayableObject
    ToolBodyCollector: ScCollector
    Tools: SelectDisplayableObjectList


class BodyFeature(Features.Feature):
    def __init__(self) -> None: ...
    def GetBodies(self) -> typing.List[Body]:
        ...
    def GetFaces(self) -> typing.List[Face]:
        ...
    def GetEdges(self) -> typing.List[Edge]:
        ...


class BodyByEquationBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    EmbedWorksheet: bool
    EmbeddedWorksheet: int
    FileBrowser: str
    Location: Features.BodyByEquationBuilder.LocationTypes
    NativeFileBrowser: str
    PlotVariableName: int
    StlFileUnits: Features.BodyByEquationBuilder.StlFileUnitTypes


    class StlFileUnitTypes(enum.Enum):
        Meters = 0
        Millimeters = 1
        Inches = 2
    

    class LocationTypes(enum.Enum):
        OperatingSystem = 0
        Teamcenter = 1
        Embedded = 2
    

class BodyByEquation(Features.BodyFeature):
    def __init__(self) -> None: ...


class BlockFeatureBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetOrientation(self, xAxis: Vector3d, yAxis: Vector3d) -> None:
        ...
    def SetLength(self, length: str) -> None:
        ...
    def SetWidth(self, width: str) -> None:
        ...
    def SetHeight(self, height: str) -> None:
        ...
    def SetOrientation(self, xAxis: Vector3d, yAxis: Vector3d) -> None:
        ...
    def SetOriginAndLengths(self, originPoint: Point3d, lengthExpression: str, widthExpression: str, heightExpression: str) -> None:
        ...
    def SetTwoPointsAndHeight(self, originPoint: Point3d, cornerPoint: Point3d, heightExpression: str) -> None:
        ...
    def SetTwoDiagonalPoints(self, originPoint: Point3d, cornerPoint: Point3d) -> None:
        ...
    def SetBooleanOperationAndTarget(self, booleanOperation: Features.Feature.BooleanType, targetBody: Body) -> None:
        ...
    BooleanOption: GeometricUtilities.BooleanOperation
    BooleanType: Features.Feature.BooleanType
    Height: Expression
    Length: Expression
    Origin: Point3d
    OriginPoint: Point
    ParentAssociativity: bool
    PointFromOrigin: Point
    Target: Body
    Type: Features.BlockFeatureBuilder.Types
    Width: Expression


    class Types(enum.Enum):
        OriginAndEdgeLengths = 0
        TwoPointsAndHeight = 1
        DiagonalPoints = 2
    

class Block(Features.BodyFeature):
    def __init__(self) -> None: ...


class BlendPocketBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngledWallSolution: Features.BlendPocketBuilder.AngledWallSolutions
    AutoInferWall: bool
    CornerClearance: Expression
    Diameter: Expression
    FloorFaces: ScCollector
    FluteLength: Expression
    LowerRadius: Expression
    NeckDiameter: Expression
    ToolType: Features.BlendPocketBuilder.ToolTypes
    UpperRadius: Expression
    WallFaces: ScCollector


    class ToolTypes(enum.Enum):
        Unknown = 0
        EndMill = 1
        TCutter = 2
        SphericalMill = 3
    

    class AngledWallSolutions(enum.Enum):
        Unknown = 0
        SwarfCutWall = 1
        CutFloorAndSwarfCutWall = 2
        CutFloor = 3
        SwarfCutWallAndFloor = 4
    

class BlendPocket(Features.BodyFeature):
    def __init__(self) -> None: ...


class BlendCornerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateBlendSetbackBuilder(self) -> GeometricUtilities.BlendSetbackBuilder:
        ...
    def CreateTransitionCurveBuilder(self) -> GeometricUtilities.TransitionCurveBuilder:
        ...
    AllowTransitionCurveOnBlends: bool
    AngleTolerance: float
    CenterPoint: Point
    Continuity: Features.BlendCornerBuilder.ContinuityTypes
    DistanceTolerance: float
    Fullness: Expression
    LimitCurveList: GeometricUtilities.BlendSetbackBuilderList
    SewToBody: bool
    TransitionCurveList: GeometricUtilities.TransitionCurveBuilderList
    UseCenterPoint: bool


    class ContinuityTypes(enum.Enum):
        G1 = 0
        G2 = 1
    

class BlendCorner(Features.BodyFeature):
    def __init__(self) -> None: ...


class BendTaper(Features.BodyFeature):
    def __init__(self) -> None: ...


class Bend(Features.Feature):
    def __init__(self) -> None: ...


class Bead(Features.Feature):
    def __init__(self) -> None: ...


class BaseFeatureCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateTrimCornerBuilder(self, trimCorner: Features.Feature) -> Features.TrimCornerBuilder:
        ...
    def CreateDivideCurveBuilder(self, divideCurve: Features.Feature) -> Features.DivideCurveBuilder:
        ...
    def CreateAssociativeLineBuilder(self, associativeLine: Features.AssociativeLine) -> Features.AssociativeLineBuilder:
        ...
    def CreateAssociativeLineBuilder(self, nonAssociativeLine: Line) -> Features.AssociativeLineBuilder:
        ...
    def CreateAssociativeArcBuilder(self, associativeArc: Features.AssociativeArc) -> Features.AssociativeArcBuilder:
        ...
    def CreateAssociativeArcBuilder(self, nonAssociativeArc: Arc) -> Features.AssociativeArcBuilder:
        ...
    def CreatePointFeatureBuilder(self, point: Features.Feature) -> Features.PointFeatureBuilder:
        ...
    def CreateWaveLinkBuilder(self, wavelink: Features.Feature) -> Features.WaveLinkBuilder:
        ...
    def CreateWaveInterfaceLinkerBuilder(self, waveInterfaceLinker: Features.Feature) -> Features.WaveInterfaceLinkerBuilder:
        ...
    def CreateMoveObjectBuilder(self, moveObject: Features.MoveObject) -> Features.MoveObjectBuilder:
        ...
    def Tag(self) -> Tag: ...



class AutomotiveCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def CreateManikinBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateManikinBuilder instead.")"""
        ...
    def CreateTireEnvelopeBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateTireEnvelopeBuilder instead.")"""
        ...
    def CreateAllAroundVisionBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateAllAroundVisionBuilder instead.")"""
        ...
    def CreateBaseDataImportExportBuilder(self) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateBaseDataImportExportBuilder instead.")"""
        ...
    def CreateOilPanBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateOilPanBuilder instead.")"""
        ...
    def CreateBaseDataBuilder(self) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateBaseDataBuilder instead.")"""
        ...
    def CreateWheelCoveringBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateWheelCoveringBuilder instead.")"""
        ...
    def CreateStaticCurbBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateStaticCurbBuilder instead.")"""
        ...
    def CreateDynamicCurbBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateDynamicCurbBuilder instead.")"""
        ...
    def CreateSlopeBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateSlopeBuilder instead.")"""
        ...
    def CreateCrashBarrierBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateCrashBarrierBuilder instead.")"""
        ...
    def CreateWheelFixingBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateWheelFixingBuilder instead.")"""
        ...
    def CreateBumperPendulumBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateBumperPendulumBuilder instead.")"""
        ...
    def CreateInnerAngleBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateInnerAngleBuilder instead.")"""
        ...
    def CreateGroundClearanceBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateGroundClearanceBuilder instead.")"""
        ...
    def CreateCloseRangeVisibilityBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateCloseRangeVisibilityBuilder instead.")"""
        ...
    def CreatePedestrianProtectionBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreatePedestrianProtectionBuilder instead.")"""
        ...
    def CreateVisionPlaneBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateVisionPlaneBuilder instead.")"""
        ...
    def CreateWindshieldDatumBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateWindshieldDatumBuilder instead.")"""
        ...
    def CreateHeadImpactBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateHeadImpactBuilder instead.")"""
        ...
    def CreateHeadImpactUpperRoofBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateHeadImpactUpperRoofBuilder instead.")"""
        ...
    def CreateHeadImpactApillarBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateHeadImpactApillarBuilder instead.")"""
        ...
    def CreateHeadImpactBpillarBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateHeadImpactBpillarBuilder instead.")"""
        ...
    def CreateHeadImpactRpillarBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateHeadImpactRpillarBuilder instead.")"""
        ...
    def CreateHeadImpactOpillarBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateHeadImpactOpillarBuilder instead.")"""
        ...
    def CreateHeadImpactFrontHeaderBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateHeadImpactFrontHeaderBuilder instead.")"""
        ...
    def CreateHeadImpactRearHeaderBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateHeadImpactRearHeaderBuilder instead.")"""
        ...
    def CreateHeadImpactSideRailBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateHeadImpactSideRailBuilder instead.")"""
        ...
    def CreateHeadImpactOtherRailBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateHeadImpactOtherRailBuilder instead.")"""
        ...
    def CreateMirrorCertificationBuilder(self, feature: Features.Feature) -> Features.FeatureBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use Features.VehicleDesignCollection.CreateMirrorCertificationBuilder instead.")"""
        ...
    def Tag(self) -> Tag: ...



class AssociativityType(enum.Enum):
    EndPoint = 0
    ArcCenter = 1
    Tangency = 2
    EndPoint1 = 3
    EndPoint2 = 4
    VerticalCenterline1 = 5
    VerticalCenterline2 = 6
    HorizontalCenterline1 = 7
    HorizontalCenterline2 = 8


class AssociativeLineBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    EndAngle: Expression
    EndAtAngle: SelectDisplayableObject
    EndInferredConstraint: SelectObject
    EndNormal: SelectDisplayableObject
    EndPoint: SelectPoint
    EndPointOptions: Features.AssociativeLineBuilder.EndOption
    EndPointReference: Features.AssociativeLineBuilder.EndReference
    EndReferenceCsys: SelectCartesianCoordinateSystem
    EndTangent: SelectICurve
    Limits: GeometricUtilities.CurveLimitsData
    LineEndNormal: SelectDisplayableObjectList
    LineStartNormal: SelectDisplayableObjectList
    StartAngle: Expression
    StartAtAngle: SelectDisplayableObject
    StartInferredConstraint: SelectObject
    StartNormal: SelectDisplayableObject
    StartPoint: SelectPoint
    StartPointOptions: Features.AssociativeLineBuilder.StartOption
    StartPointReference: Features.AssociativeLineBuilder.StartReference
    StartReferenceCsys: SelectCartesianCoordinateSystem
    StartTangent: SelectICurve
    SupportPlaneData: GeometricUtilities.SupportPlaneData


    class StartReference(enum.Enum):
        Wcs = 0
        Absolute = 1
        CordinatesSystem = 2
    

    class StartOption(enum.Enum):
        Inferred = 0
        Point = 1
        Tangent = 2
        AtAngle = 3
        AlongXc = 4
        AlongYc = 5
        AlongZc = 6
        Normal = 7
    

    class EndReference(enum.Enum):
        Wcs = 0
        Absolute = 1
        CordinatesSystem = 2
    

    class EndOption(enum.Enum):
        Inferred = 0
        Point = 1
        Tangent = 2
        AtAngle = 3
        AlongXc = 4
        AlongYc = 5
        AlongZc = 6
        Normal = 7
    

class AssociativeLine(Features.Feature):
    def __init__(self) -> None: ...


class AssociativeArcBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    CenterPoint: SelectPoint
    CenterPointReference: Features.AssociativeArcBuilder.CenterReference
    CenterPointReferenceCsys: SelectCartesianCoordinateSystem
    CenterRadiusLockedPlaneDirection: Vector3d
    Diameter: Expression
    EndInferredConstraint: SelectObject
    EndPoint: SelectPoint
    EndPointOptions: Features.AssociativeArcBuilder.EndOption
    EndPointReference: Features.AssociativeArcBuilder.EndReference
    EndReferenceCsys: SelectCartesianCoordinateSystem
    EndTangent: SelectDisplayableObject
    Limits: GeometricUtilities.CurveLimitsData
    MidInferredConstraint: SelectObject
    MidPoint: SelectPoint
    MidPointOptions: Features.AssociativeArcBuilder.MidOption
    MidPointReference: Features.AssociativeArcBuilder.MidReference
    MidReferenceCsys: SelectCartesianCoordinateSystem
    MidTangent: SelectDisplayableObject
    Radius: Expression
    StartInferredConstraint: SelectObject
    StartPoint: SelectPoint
    StartPointOptions: Features.AssociativeArcBuilder.StartOption
    StartPointReference: Features.AssociativeArcBuilder.StartReference
    StartReferenceCsys: SelectCartesianCoordinateSystem
    StartTangent: SelectDisplayableObject
    SupportPlaneData: GeometricUtilities.SupportPlaneData
    Type: Features.AssociativeArcBuilder.Types
    ZonePoint: Point3d


    class Types(enum.Enum):
        ThreePointArc = 0
        ArcFromCenter = 1
    

    class StartReference(enum.Enum):
        Wcs = 0
        Absolute = 1
        CordinatesSystem = 2
    

    class StartOption(enum.Enum):
        Inferred = 0
        Point = 1
        Tangent = 2
    

    class MidReference(enum.Enum):
        Wcs = 0
        Absolute = 1
        CordinatesSystem = 2
    

    class MidOption(enum.Enum):
        Inferred = 0
        Point = 1
        Tangent = 2
        Radius = 3
        Diameter = 4
    

    class EndReference(enum.Enum):
        Wcs = 0
        Absolute = 1
        CordinatesSystem = 2
    

    class EndOption(enum.Enum):
        Inferred = 0
        Point = 1
        Tangent = 2
        Radius = 3
        Diameter = 4
    

    class CenterReference(enum.Enum):
        Wcs = 0
        Absolute = 1
        CordinatesSystem = 2
    

class AssociativeArc(Features.Feature):
    def __init__(self) -> None: ...


class AssemblyCutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetOperationFailures(self) -> ErrorList:
        ...
    ContextComponent: Assemblies.Component
    HideToolBodyFlag: bool
    TargetBody: SelectBodyList
    ToolBody: SelectBodyList


class AssemblyCut(Features.BodyFeature):
    def __init__(self) -> None: ...
    def GetPromotionFeatures(self) -> typing.List[Features.Promotion]:
        ...
    def GetBooleanBodyFeatures(self) -> typing.List[Features.BodyFeature]:
        ...


class AOCSBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def FlipAllOffsetsOfSection(self, section: Section) -> None:
        ...
    def FlipOffset(self, seldimitem: NXObject) -> None:
        ...
    def UpdatePostStatusFlag(self, postStatusChanged: bool) -> None:
        ...
    def UpdateCurvesStatus(self, updateLawParm: bool) -> None:
        ...
    def CloneSection(self, constToVariable: bool, sectionFrom: Section) -> Section:
        ...
    def SynchronizeSections(self, constToVariable: bool, firstSection: Section, secondSection: Section) -> None:
        ...
    def UpdateFaces(self) -> None:
        ...
    def UpdateSectionData(self, section: Section) -> bool:
        ...
    def SynchronizeSectionForValueOrPoint(self, pointType: bool) -> None:
        ...
    AngularTolerance: float
    AssociativeOutputOption: bool
    CurveFitData: GeometricUtilities.CurveFitData
    CurveFitJoinData: GeometricUtilities.CurveFitJoin
    CurveOffsetType: Features.AOCSBuilder.CurveOffsetTypes
    DirectionVector: Direction
    DistanceTolerance: float
    ExtendMethod: Features.AOCSBuilder.Extend
    ExtendToFaceOption: Features.AOCSBuilder.ExtendToFace
    FaceCollector: ScCollector
    FilletDirectionVector: Direction
    FilletOption: Features.AOCSBuilder.FilletOptions
    FilletRadius: Expression
    Law: GeometricUtilities.LawBuilder
    LawString: Section
    LawStringFlip: bool
    OffsetDirectionOption: Features.AOCSBuilder.OffsetDirection
    OffsetDistType: Features.AOCSBuilder.OffsetDistanceType
    OffsetMode: Features.AOCSBuilder.OffsetType
    Offsets: ExpressionSectionSetList
    PointString: Section
    ProjectPlaneNormal: Direction
    RemoveSelfIntersections: bool
    SplitCurveOption: bool
    ThroughPoint: Point
    TrimMethod: Features.AOCSBuilder.Trim
    TrimToFaceEdgesOption: bool


    class Trim(enum.Enum):
        None = 0
        WithinSection = 1
    

    class OffsetType(enum.Enum):
        Chordal = 0
        Arclength = 1
        Geodesic = 2
        Tangential = 3
        Projectdistance = 4
    

    class OffsetDistanceType(enum.Enum):
        Constant = 0
        Variable = 1
    

    class OffsetDirection(enum.Enum):
        NormalToCurve = 0
        NormalToVector = 1
    

    class FilletOptions(enum.Enum):
        NoFillet = 0
        Vector = 1
        BestFit = 2
        ProjectedVector = 3
    

    class ExtendToFace(enum.Enum):
        None = 0
        Boundary = 1
    

    class Extend(enum.Enum):
        None = 0
        WithinSection = 1
    

    class CurveOffsetTypes(enum.Enum):
        Value = 0
        ThroughPoint = 1
    

class AOCS(Features.Feature):
    def __init__(self) -> None: ...


class AngularDimBuilder(Features.DimensionBuilder):
    def __init__(self) -> None: ...
    def GetIsComplementAngle(self, dimensionLocation: Point3d) -> bool:
        ...
    def SetInterpartSourceEdge(self, interpartSourceEdge: Edge) -> None:
        ...
    AlternativeAngle: bool
    ComplementAngleFlag: bool
    MeasurementObject: SelectNXObject
    OriginObject: SelectNXObject


class AngularDim(Features.BodyFeature):
    def __init__(self) -> None: ...


class AnalyzePocketBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AcutelyAngledWallsChecker: bool
    Diameter: Expression
    FloorFaces: ScCollector
    FluteLength: Expression
    InaccessibleAreasChecker: bool
    LowerRadius: Expression
    NeckDiameter: Expression
    ToolType: Features.AnalyzePocketBuilder.ToolTypes
    UndercutsChecker: bool
    UpperRadius: Expression
    WallFaces: ScCollector


    class ToolTypes(enum.Enum):
        Unknown = 0
        EndMill = 1
        TCutter = 2
        SphericalMill = 3
    

    class AngledWallSolutions(enum.Enum):
        Unknown = 0
        SwarfCutWall = 1
        CutFloorAndSwarfCutWall = 2
        CutFloor = 3
        SwarfCutWallAndFloor = 4
    

class AnalyzePocket(Features.BodyFeature):
    def __init__(self) -> None: ...


class AestheticFaceBlendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AlignmentOption: Features.AestheticFaceBlendBuilder.AlignmentType
    BaseRadiusLaw: GeometricUtilities.LawBuilder
    BlendFacesOption: Features.AestheticFaceBlendBuilder.BlendFacesType
    BlendOption: Features.AestheticFaceBlendBuilder.BlendType
    CenterChordLaw: GeometricUtilities.LawBuilder
    CenterOption: Features.AestheticFaceBlendBuilder.CenterType
    CenterRadiusLaw: GeometricUtilities.LawBuilder
    Chain1Continuity: GeometricUtilities.Continuity
    Chain2Continuity: GeometricUtilities.Continuity
    ChordLength: Expression
    ChordLengthLaw: GeometricUtilities.LawBuilder
    ConstrainedEndPoint1: Point
    ConstrainedEndPoint2: Point
    ConstrainedStartPoint1: Point
    ConstrainedStartPoint2: Point
    Continuity: GeometricUtilities.Continuity
    CurvatureTolerance: float
    Degrees: GeometricUtilities.DegreesAndSegmentsOrPatchesBuilder
    FaceChain1: ScCollector
    FaceChain2: ScCollector
    IsAccelerated: bool
    IsBezier: bool
    IsCenterlineCurve: bool
    IsMinimumRadius: bool
    IsMinimumSubtendedAngle: bool
    IsRationalOutput: bool
    IsSameTransition: bool
    IsSewAllFaces: bool
    IsTrimInputFaces: bool
    IsWashout1: bool
    IsWashout2: bool
    LimitsList: GeometricUtilities.BlendLimitsData
    MinimumEdgeLength: float
    MinimumRadius: Expression
    MinimumSubtendedAngle: float
    ParameterSpine: Section
    PositionTolerance: float
    RelativeEndBlendEndPoint: float
    RelativeEndBlendStartPoint: float
    RelativeStartBlendEndPoint: float
    RelativeStartBlendStartPoint: float
    ReverseNormal1: bool
    ReverseNormal2: bool
    RhoOption: Features.AestheticFaceBlendBuilder.RhoType
    RhoValue: float
    SectionAlignmentVector: Direction
    SectionScaling1: Expression
    SectionScaling2: Expression
    SegmentationOption: Features.AestheticFaceBlendBuilder.SegmentationType
    ShapeOption: Features.AestheticFaceBlendBuilder.ShapeType
    TangentMagnitude: GeometricUtilities.TangentMagnitudeBuilder
    TangentTolerance: float


    class StartTrimObjectType(enum.Enum):
        None = 0
        Plane = 1
        Face = 2
    

    class ShapeType(enum.Enum):
        Accelerated = 0
        Circular = 1
    

    class SegmentationType(enum.Enum):
        AtAllTransitions = 0
        AtTransitionsonFaceChain1 = 1
        AtTransitionsonFaceChain2 = 2
        AtAllTransitionsandMergeSmallBlendFaces = 3
    

    class RhoType(enum.Enum):
        Relative = 0
        Absolute = 1
    

    class EndTrimObjectType(enum.Enum):
        None = 0
        Plane = 1
        Face = 2
    

    class CenterType(enum.Enum):
        CenterRadius = 0
        Rho = 1
    

    class BlendType(enum.Enum):
        Radius = 0
        ChordLength = 1
    

    class BlendFacesType(enum.Enum):
        TrimtoAllInputFaces = 0
        TrimtoShortInputFaces = 1
        TrimtoLongInputFaces = 2
        DoNotTrimBlendFaces = 3
    

    class AlignmentType(enum.Enum):
        RollingBall = 0
        SpineCurve = 1
        Vector = 2
    

class AestheticFaceBlend(Features.BodyFeature):
    def __init__(self) -> None: ...
    def IsolateToolBodies(self) -> None:
        ...


class AeroRibBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ConstructGuidecurves(self, deleteGuideCurves: bool, showGuideCurves: bool) -> None:
        ...
    AlignRefType0: Features.AeroRibBuilder.AlignReferenceType
    AlignRefType1: Features.AeroRibBuilder.AlignReferenceType
    BooleanOperation: GeometricUtilities.BooleanOperation
    CurveLength: GeometricUtilities.CurveLengthBuilder
    GuideFaces: ScCollector
    GuideObjectType: Features.AeroRibBuilder.GuideObjectTypes
    Height: Expression
    HeightDimensionType: Features.AeroRibBuilder.HeightDimensionOptions
    HeightOffset: Expression
    IsLimit1MeasureExpressionUsed: bool
    IsLimit2MeasureExpressionUsed: bool
    Limit1Offset: Expression
    Limit1Point: GeometricUtilities.OnPathDimensionBuilder
    Limit1Selection: ScCollector
    Limit1Type: Features.AeroRibBuilder.LimitObjectTypes
    Limit2Offset: Expression
    Limit2Point: GeometricUtilities.OnPathDimensionBuilder
    Limit2Selection: ScCollector
    Limit2Type: Features.AeroRibBuilder.LimitObjectTypes
    Plane: Plane
    ProjectDirection: GeometricUtilities.ProjectionOptions
    ReverseHeightDirection: bool
    ReverseHeightOffsetDirection: bool
    ReverseLimit1OffsetDirection: bool
    ReverseLimit2OffsetDirection: bool
    ReverseThicknessDirection: bool
    ReverseThicknessOffsetDirection: bool
    RibForm: Features.AeroRibBuilder.RibForms
    Section: Section
    SkinFaceCollector: ScCollector
    Thickness: Expression
    ThicknessDimensionType: Features.AeroRibBuilder.ThicknessDimensionOptions
    ThicknessOffset: Expression


    class ThicknessDimensionOptions(enum.Enum):
        Simple = 0
        Symmetric = 1
    

    class RibForms(enum.Enum):
        NormalToSkin = 0
        AlignWithGuideFace = 1
    

    class PointOption(enum.Enum):
        ArcLength = 0
        PercentArcLength = 1
        ParameterArcLength = 2
        ThroughPoint = 3
    

    class LimitObjectTypes(enum.Enum):
        FromGuideCurve = 0
        FromSelected = 1
    

    class HeightDimensionOptions(enum.Enum):
        Simple = 0
        Symmetric = 1
    

    class GuideObjectTypes(enum.Enum):
        Face = 0
        DatumPlane = 1
        Curve = 2
    

    class AlignReferenceType(enum.Enum):
        None = 0
        LengthFace = 1
        Skin = 2
        GuideFace = 3
    

class AeroRib(Features.BodyFeature):
    def __init__(self) -> None: ...


class AeroFlangeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ConstructGuidecurves(self, deleteGuideCurves: bool, showGuideCurves: bool) -> None:
        ...
    AlignRefType0: Features.AeroFlangeBuilder.AlignReferenceType
    AlignRefType1: Features.AeroFlangeBuilder.AlignReferenceType
    BooleanOperation: GeometricUtilities.BooleanOperation
    CurveLength: GeometricUtilities.CurveLengthBuilder
    GuideFaces: ScCollector
    GuideObjectType: Features.AeroFlangeBuilder.GuideObjectTypes
    IsLimit1MeasureExpressionUsed: bool
    IsLimit2MeasureExpressionUsed: bool
    Limit1Offset: Expression
    Limit1Point: GeometricUtilities.OnPathDimensionBuilder
    Limit1Selection: ScCollector
    Limit1Type: Features.AeroFlangeBuilder.LimitObjectTypes
    Limit2Offset: Expression
    Limit2Point: GeometricUtilities.OnPathDimensionBuilder
    Limit2Selection: ScCollector
    Limit2Type: Features.AeroFlangeBuilder.LimitObjectTypes
    Plane: Plane
    ProjectDirection: GeometricUtilities.ProjectionOptions
    ReverseLimit1OffsetDirection: bool
    ReverseLimit2OffsetDirection: bool
    ReverseThicknessDirection: bool
    ReverseThicknessOffsetDirection: bool
    ReverseWidth1Direction: bool
    ReverseWidth2Direction: bool
    ReverseWidthOffsetDirection: bool
    Section: Section
    SkinFaceCollector: ScCollector
    Thickness: Expression
    ThicknessDimensionType: Features.AeroFlangeBuilder.ThicknessDimensionOptions
    ThicknessOffset: Expression
    Width1: Expression
    Width2: Expression
    WidthDimensionType: Features.AeroFlangeBuilder.WidthDimensionOptions
    WidthMethod: Features.AeroFlangeBuilder.WidthMethods
    WidthOffset: Expression


    class WidthMethods(enum.Enum):
        OffsetGuideFace = 0
        OffsetGuideCurveAlongSkin = 1
    

    class WidthDimensionOptions(enum.Enum):
        Simple = 0
        Symmetric = 1
        Asymmetric = 2
    

    class ThicknessDimensionOptions(enum.Enum):
        Simple = 0
        Symmetric = 1
    

    class PointOption(enum.Enum):
        ArcLength = 0
        PercentArcLength = 1
        ParameterArcLength = 2
        ThroughPoint = 3
    

    class LimitObjectTypes(enum.Enum):
        FromGuideCurve = 0
        FromSelected = 1
    

    class GuideObjectTypes(enum.Enum):
        Face = 0
        DatumPlane = 1
        Curve = 2
    

    class AlignReferenceType(enum.Enum):
        None = 0
        LengthFace = 1
        Skin = 2
        GuideFace = 3
    

class AeroFlange(Features.BodyFeature):
    def __init__(self) -> None: ...


class AeroCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def CreateAeroFlangeBuilder(self, aeroFlange: Features.AeroFlange) -> Features.AeroFlangeBuilder:
        ...
    def CreateAeroRibBuilder(self, aeroRib: Features.AeroRib) -> Features.AeroRibBuilder:
        ...
    def CreateStepBuilder(self, stepFrec: Features.Step) -> Features.StepBuilder:
        ...
    def CreateShelfBuilder(self, shelf: Features.Shelf) -> Features.ShelfBuilder:
        ...
    def Tag(self) -> Tag: ...



class AdmResizeFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Angle: Expression
    Diameter: Expression
    FaceToResize: Features.FaceRecognitionBuilder


class AdmResizeFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class AdmOffsetRegionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Distance: Expression
    FaceChangeOverflowBehavior: GeometricUtilities.FaceChangeOverflowBehavior
    FaceToOffset: Features.FaceRecognitionBuilder
    ReverseDirection: bool


class AdmOffsetRegion(Features.BodyFeature):
    def __init__(self) -> None: ...


class AdmMoveFaceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FaceChangeOverflowBehavior: GeometricUtilities.FaceChangeOverflowBehavior
    FaceToMove: Features.FaceRecognitionBuilder
    HealOption: bool
    Motion: GeometricUtilities.ModlMotion
    MoveOption: Features.AdmMoveFaceBuilder.MoveOptionType
    PasteOption: bool
    StepOption: GeometricUtilities.StepOptionBehavior


    class MoveOptionType(enum.Enum):
        MoveAndAdapt = 0
        CutAndPaste = 1
    

class AdmMoveFace(Features.BodyFeature):
    def __init__(self) -> None: ...


class AddendumSurface(Features.BodyFeature):
    def __init__(self) -> None: ...


class AddendumSection(Features.CurveFeature):
    def __init__(self) -> None: ...


class AdaptiveShellBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FacesToExclude: ScCollector
    FacesToPierce: ScCollector
    ReverseDirection: bool
    Thickness: Expression


class AdaptiveShell(Features.BodyFeature):
    def __init__(self) -> None: ...


