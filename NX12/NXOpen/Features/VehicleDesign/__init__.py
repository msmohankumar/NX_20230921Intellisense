from ....NXOpen import *
from ...Features import *
from ..VehicleDesign import *

import typing
import enum

class WindshieldDatumBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AssoToggle: bool
    BottomAngle: Expression
    EyeFeature: Features.SelectFeature
    EyeType: Features.VehicleDesign.WindshieldDatumBuilder.EnumEyeType
    HorizontalAngle: Expression
    LoadingName: str
    PointV1: Point
    PointV2: Point
    RayLength: Expression
    SelectWindshield: ScCollector
    ShowPoints: bool
    ShowRays: bool
    TopAngle: Expression
    UseStandardLoading: bool
    VisionType: Features.VehicleDesign.WindshieldDatumBuilder.CustomVisionAngle


    class EnumEyeType(enum.Enum):
        EyeFeature = 0
        V1Point = 1
        V2Point = 2
    

    class CustomVisionAngle(enum.Enum):
        Standard = 0
        Custom = 1
    

class WindshieldDatum(Features.Feature):
    def __init__(self) -> None: ...


class WheelFixingBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    HeightZ: Expression
    LengthX: Expression
    LevelZ: Expression
    Loading: str
    ObjectPosition: Features.VehicleDesign.WheelFixingBuilder.ObjectPositionType
    Position: Features.VehicleDesign.WheelFixingBuilder.PositionType
    Radius: Expression
    RequirementsControl: Features.VehicleDesign.WheelFixingBuilder.RequirementsControlType
    Shape: Features.VehicleDesign.WheelFixingBuilder.ShapeType
    Standard: str
    WheelSize: Features.VehicleDesign.WheelFixingBuilder.WheelSizeType
    WidthY: Expression


    class WheelSizeType(enum.Enum):
        StaticRadius = 0
        Diameter = 1
    

    class ShapeType(enum.Enum):
        Block = 0
        CircleSegment = 1
    

    class RequirementsControlType(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

    class PositionType(enum.Enum):
        Front = 0
        Rear = 1
        Both = 2
    

    class ObjectPositionType(enum.Enum):
        WheelExtents = 0
        WheelContact = 1
    

class WheelFixing(Features.BodyFeature):
    def __init__(self) -> None: ...


class WheelCoveringBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DisplayIntersectionCurves: bool
    FrontBottomOffset: Expression
    FrontClearance: Expression
    FrontFrontAngle: Expression
    FrontFrontOffset: Expression
    FrontHeight: Expression
    FrontHubcapSelection: ScCollector
    FrontObjectSelection: ScCollector
    FrontRadius: Expression
    FrontRearAngle: Expression
    FrontRearOffset: Expression
    FrontSurfacePlane: Features.VehicleDesign.WheelCoveringBuilder.SurfacePlaneType
    FrontSurfaceSection: Features.VehicleDesign.WheelCoveringBuilder.SurfaceSectionType
    Loading: str
    Position: Features.VehicleDesign.WheelCoveringBuilder.PositionType
    RearBottomOffset: Expression
    RearClearance: Expression
    RearDisToWheelCenter: Expression
    RearFrontAngle: Expression
    RearFrontOffset: Expression
    RearHeight: Expression
    RearHubcapSelection: ScCollector
    RearObjectSelection: ScCollector
    RearRadius: Expression
    RearRearAngle: Expression
    RearRearOffset: Expression
    RearSurfacePlane: Features.VehicleDesign.WheelCoveringBuilder.SurfacePlaneType
    RearSurfaceSection: Features.VehicleDesign.WheelCoveringBuilder.SurfaceSectionType
    RequirementsControl: Features.VehicleDesign.WheelCoveringBuilder.RequirementsControlType
    Standard: str


    class SurfaceSectionType(enum.Enum):
        CircleSection = 0
        Adr42 = 1
        ExtrudeSection = 2
    

    class SurfacePlaneType(enum.Enum):
        WheelPlane = 0
        PerpendiculartoLoading = 1
    

    class RequirementsControlType(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

    class PositionType(enum.Enum):
        Front = 0
        Rear = 1
        Both = 2
    

class WheelCovering(Features.BodyFeature):
    def __init__(self) -> None: ...


class VisionPlaneBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AssoToggle: bool
    BaseDim: Expression
    DriverPlane: Expression
    EyeFeature: Features.SelectFeature
    EyeType: Features.VehicleDesign.VisionPlaneBuilder.EnumEyeType
    FrontDim: Expression
    FrontPlane: Expression
    LoadingName: str
    LowerPlane: bool
    MidPlane: Expression
    MiddlePlane: bool
    PassengerPlane: Expression
    PointV1: Point
    PointV2: Point
    UpperPlane: bool
    UseStandardLoading: bool
    VisionType: Features.VehicleDesign.VisionPlaneBuilder.CustomVisionAngle


    class EnumEyeType(enum.Enum):
        EyeFeature = 0
        V1Point = 1
        V2Point = 2
    

    class CustomVisionAngle(enum.Enum):
        Standard = 0
        Custom = 1
    

class VisionPlane(Features.BodyFeature):
    def __init__(self) -> None: ...


class VehicleCoordinateSystemBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    OriginPoint: Point
    Type: Features.VehicleDesign.VehicleCoordinateSystemBuilder.Types
    XAxis: Direction
    ZAxis: Direction


    class Types(enum.Enum):
        LengthWidthHeight = 0
        WidthLengthHeight = 1
        UserDefined = 2
    

class VehicleCoordinateSystem(Features.Feature):
    def __init__(self) -> None: ...


class TireEnvelopeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetSessionNotes(self) -> str:
        ...
    def SetSessionNotes(self, sessionNotes: str) -> None:
        ...
    def SwitchDrivers(self) -> None:
        ...
    def SetVehicleCoordinateSystem(self, type: int, origin: Point3d, matrix: Matrix3x3) -> None:
        ...
    def AddMasterPart(self, partName: str) -> None:
        ...
    def AddMasterPart(self, partObject: Part) -> None:
        ...
    def SetTireProfileSketch(self, partname: str, sketchname: str) -> None:
        ...
    def SetTireProfileSketch(self, sketchObject: Sketch) -> None:
        ...
    def CreateLinkedProfiles(self) -> None:
        ...
    def CalculateProfilePoints(self) -> None:
        ...
    def ProcessFromSpindleLines(self) -> None:
        ...
    def ReadSuspensionTemplate(self, fileName: str) -> str:
        ...
    def SetSuspentionTemplatePoint(self, templateType: Features.VehicleDesign.TireEnvelopeBuilder.SuspensionTemplateType, jointIndex: int, pnt: Point3d) -> None:
        ...
    def SetDriverJoints(self, steerJoint: NXObject, jounceJoint: NXObject) -> None:
        ...
    def BuildMotionTemplate(self) -> None:
        ...
    def RunMotionArticulation(self) -> None:
        ...
    def SetOffsetSections(self, sectionAngle: float) -> None:
        ...
    def SetOffsetValues(self, sectionIndex: int, offsetValues: float) -> None:
        ...
    def UpdateTireBodyFeature(self) -> None:
        ...
    def ReassembleTireBodyComponent(self) -> None:
        ...
    def SetClearanceValues(self, clearanceValues: float) -> None:
        ...
    def PerformClearanceAnalysis(self) -> None:
        ...
    AddMasterComponentPart: bool
    ApplyOffset: bool
    BushingJointAsymmetric: bool
    ClearanceAnalysisBodies: SelectBodyList
    ClearanceAnalysisComponents: Assemblies.SelectComponentList
    ClearanceValue: Expression
    CreateTireEnvelopeFeature: bool
    DesignPositionSpindle: SelectCurve
    DistanceTolerance: Expression
    DownOffsetValue: Expression
    DriverGraph: Features.VehicleDesign.TireEnvelopeBuilder.DriverGraphOption
    DriverGraphSketch: SelectSketch
    EnvelopeConcavity: float
    EnvelopeOffset: Features.VehicleDesign.TireEnvelopeBuilder.EnvelopeOffsetMethod
    FirstDriverJointLowerLimit: float
    FirstDriverJointSteps: int
    FirstDriverJointUpperLimit: float
    FixedLocationPercentage: float
    FrontOffsetValue: Expression
    InboardOffsetValue: Expression
    InnerJointAsymmetric: bool
    JounceDistance: float
    LeftStabilizerBar: SelectDisplayableObjectList
    MirrorProfile: bool
    Motion: Features.VehicleDesign.TireEnvelopeBuilder.MotionMethod
    OffsetFileName: str
    OutboardOffsetValue: Expression
    ProfileName: str
    ProfilePointFile: str
    ProfileSplineLayer: int
    RadialEndAngle: Expression
    RadialStartAngle: Expression
    RearOffsetValue: Expression
    ReboundDistance: float
    RightStabilizerBar: SelectCurveList
    RollAngle: Expression
    RunClearanceAnalysis: bool
    SaveMasterPart: bool
    SaveScenario: bool
    ScenarioName: str
    SecondDriverJointLowerLimit: float
    SecondDriverJointSteps: int
    SecondDriverJointUpperLimit: float
    SectionLayer: int
    SheetBodyLayer: int
    ShockDriverJointSteps: int
    SpindleEndPoint: Point
    SpindleFileLocation: Features.VehicleDesign.TireEnvelopeBuilder.SpindleFileLocationOption
    SpindleFileName: str
    SpindleLines: SelectCurveList
    SpindleLinesLayer: int
    SuspensionTemplate: Features.VehicleDesign.TireEnvelopeBuilder.SuspensionTemplateType
    SuspensionTemplateFileName: str
    TaperLocationAY: float
    TaperLocationBX: float
    TaperLocationXAxis: float
    TaperLocationYAxis: float
    TireBodyOutputFileName: str
    TireDefinition: Features.VehicleDesign.TireEnvelopeBuilder.TireDefinitionOption
    TireDefinitionBody: SelectBodyList
    TireDefinitionProfile: SelectCurveList
    TracedSpindleLine: SelectCurve
    TrimRadius: Expression
    UpOffsetValue: Expression
    UseStabilizerBar: bool
    WheelCenterlineShift: Expression
    WheelCsys: CoordinateSystem
    WheelRimDiameter: Expression


    class TireDefinitionOption(enum.Enum):
        SolidBody = 0
        ProfileCurves = 1
        SketchfromOtherPart = 2
        ProfilePointFile = 3
    

    class SuspensionTemplateType(enum.Enum):
        MacPhersonStrut = 0
        ShortLongArmwithSteering = 1
        ShortLongArmwithoutSteering = 2
        FiveLinkSolidAxlewithoutSteering = 3
    

    class SpindleFileLocationOption(enum.Enum):
        InNative = 0
        InTeamcenter = 1
    

    class MotionMethod(enum.Enum):
        ExistingSpindleFile = 0
        FromSpindleLines = 1
        ExistingScenarioMotionModel = 2
        SuspensionTemplate = 3
    

    class EnvelopeOffsetMethod(enum.Enum):
        FixedSections = 0
        CustomerDefinedData = 1
        FromOffsetFile = 2
    

    class DriverGraphOption(enum.Enum):
        RectangularJounceRebound = 0
        RectangularTaperedY = 1
        RectangularTaperedX = 2
        TaperedOneSide = 3
        BySketch = 4
        TwoDriversOneFixed = 5
    

class TireEnvelope(Features.BodyFeature):
    def __init__(self) -> None: ...


class StaticCurbBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FrontAngle: Expression
    FrontLoading: str
    FrontMeasuredFaces: ScCollector
    FrontOffset: Expression
    Position: Features.VehicleDesign.StaticCurbBuilder.PositionType
    RearAngle: Expression
    RearLoading: str
    RearMeasuredFaces: ScCollector
    RearOffset: Expression
    RequirementsControl: Features.VehicleDesign.StaticCurbBuilder.RequirementsControlType
    ShowDistanceMeasurement: bool
    Standard: str
    Visualization: Features.VehicleDesign.StaticCurbBuilder.VisualizationType


    class VisualizationType(enum.Enum):
        Curve = 0
        Surface = 1
        CurveandSurface = 2
    

    class RequirementsControlType(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

    class PositionType(enum.Enum):
        Front = 0
        Rear = 1
        Both = 2
    

class StaticCurb(Features.BodyFeature):
    def __init__(self) -> None: ...


class SlopeBuilder(Builder):
    def __init__(self) -> None: ...
    FrontAngle: Expression
    FrontLoading: str
    FrontObjects: ScCollector
    Position: Features.VehicleDesign.SlopeBuilder.PositionType
    RearAngle: Expression
    RearLoading: str
    RearObjects: ScCollector
    RequirementsControl: Features.VehicleDesign.SlopeBuilder.RequirementsControlType
    ShowDistanceMeasurement: bool
    Standard: str
    Visualization: Features.VehicleDesign.SlopeBuilder.VisualizationType
    WheelSize: Features.VehicleDesign.SlopeBuilder.WheelSizeType


    class WheelSizeType(enum.Enum):
        StaticRadius = 0
        Diameter = 1
    

    class VisualizationType(enum.Enum):
        Curve = 0
        Surface = 1
        CurveandSurface = 2
    

    class RequirementsControlType(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

    class PositionType(enum.Enum):
        Front = 0
        Rear = 1
        Both = 2
    

class Slope(Features.BodyFeature):
    def __init__(self) -> None: ...


class SeatBeltAnchorageBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def J383Illu(self) -> None:
        ...
    def J1369Illu(self) -> None:
        ...
    def Ece14SafeIllu(self) -> None:
        ...
    def Ece14Isofix(self) -> None:
        ...
    def CreatePointWithBaseDataSGRPExpression(self) -> Point:
        ...
    AnchorageLocation: Features.VehicleDesign.SeatBeltAnchorageBuilder.AnchorageLocationTypes
    Atl: Features.VehicleDesign.SeatBeltAnchorageBuilder.ATLType
    BackAngleDbl: float
    BackAngleDim: Expression
    BeltRouting: Features.VehicleDesign.SeatBeltAnchorageBuilder.RoutingTypes
    FloorHeightDim: Expression
    L1Limit: Features.VehicleDesign.SeatBeltAnchorageBuilder.LOneLimitType
    L2Limit: Features.VehicleDesign.SeatBeltAnchorageBuilder.LTwoLimitType
    LowerArea: Features.VehicleDesign.SeatBeltAnchorageBuilder.LowerAreaType
    LowerLimit: Features.VehicleDesign.SeatBeltAnchorageBuilder.LowerLimitType
    SDimension: Expression
    SeatPosition: Features.VehicleDesign.SeatBeltAnchorageBuilder.SeatPositionTypes
    SeatType: Features.VehicleDesign.SeatBeltAnchorageBuilder.SeatTypes
    SgrpPoint: Point
    SgrpXvalDim: Expression
    SgrpYvalDim: Expression
    SgrpZvalDim: Expression
    Standard: Features.VehicleDesign.SeatBeltAnchorageBuilder.StandardTypes
    StringLimit1: str
    StringLimit2: str
    UpArea: Features.VehicleDesign.SeatBeltAnchorageBuilder.UpperAreaType


    class UpperAreaType(enum.Enum):
        Yes = 0
        No = 1
    

    class StandardTypes(enum.Enum):
        J383SeatBeltAnchorage = 0
        J1369ChildRestraintTetherStraps = 1
        BothJ383AndJ1369 = 2
        ECE14SafetyBeltAnchorage = 3
        Ece14isofix = 4
    

    class SeatTypes(enum.Enum):
        MovableFront = 0
        MovableRear = 1
        Fixed = 2
    

    class SeatPositionTypes(enum.Enum):
        Left = 0
        Right = 1
        NotOutboard = 2
    

    class RoutingTypes(enum.Enum):
        OutsideSeatThruSeatSpring = 0
        ToAnchorage = 1
    

    class LTwoLimitType(enum.Enum):
        Degree45And80 = 0
        Degree50And70 = 1
    

    class LowerLimitType(enum.Enum):
        Length450 = 0
        Length500 = 1
    

    class LowerAreaType(enum.Enum):
        Yes = 0
        No = 1
    

    class LOneLimitType(enum.Enum):
        Degree30And80 = 0
        Degree50And70 = 1
    

    class ATLType(enum.Enum):
        Yes = 0
        No = 1
    

    class AnchorageLocationTypes(enum.Enum):
        VehicleStructure = 0
        SeatAssembly = 1
    

class SeatBeltAnchorage(Features.Feature):
    def __init__(self) -> None: ...


class ReflectionDataBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DashSurface: ScCollector
    EyePoint: Point
    IsReflectData: bool
    IsReflectTraceCurve: bool
    IsRefractData: bool
    IsRefractTraceCurve: bool
    IsReverseReflectData: bool
    IsReverseReflectTraceCurve: bool
    ReflectAccuracy: int
    ReflectMethod: Features.VehicleDesign.ReflectionDataBuilder.ReflectMethodType
    ReflectionObject: ScCollector
    RefractionIndex: float
    Resolution: Features.VehicleDesign.ReflectionDataBuilder.ResolutionType
    ReverseDir: bool
    TargetObject: Section
    Thickness: float


    class ResolutionType(enum.Enum):
        Low = 0
        Medium = 1
        High = 2
        Customized = 3
    

    class ReflectMethodType(enum.Enum):
        DirectReflect = 0
        ReverseReflection = 1
    

class ReflectionData(Features.CurveFeature):
    def __init__(self) -> None: ...


class PendulumPlacementBuilder(Builder):
    def __init__(self) -> None: ...
    Angle: Expression
    Color: NXColor
    Level: Expression
    Loading: str
    Location: Features.VehicleDesign.PendulumPlacementBuilder.LocationType
    Name: str
    Offset: Expression
    PendulumProfile: Features.VehicleDesign.PendulumPlacementBuilder.PendulumProfileType
    PositionMethod: Features.VehicleDesign.PendulumPlacementBuilder.PositionMethodType
    Shift: Expression
    ShowPendulum: bool
    ShowPoint: bool
    Side: Features.VehicleDesign.PendulumPlacementBuilder.SideType


    class SideType(enum.Enum):
        Left = 0
        Right = 1
    

    class PositionMethodType(enum.Enum):
        MiddleBaseData = 0
        MiddleVehicle = 1
        RotatedBaseData = 2
        RotatedPlane = 3
        RotatedPlaneX = 4
        RotatedPlaneNormal = 5
        RotatedContact = 6
        ShiftedBaseData = 7
        ShiftedVehicle = 8
        ShiftedFromRotated = 9
    

    class PendulumProfileType(enum.Enum):
        Eu = 0
        Us = 1
    

    class LocationType(enum.Enum):
        Front = 0
        Rear = 1
    

class PedestrianProtectionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    APillar: SelectDisplayableObjectList
    AdultGtrUntranslateOutputColor: NXColor
    AdultGtrUntranslateOutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    AdultGtrUntranslateOutputLayer: int
    AdultGtrUntranslateOutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    AdultHic1000Angle: Expression
    AdultHic1000Offset: Expression
    AdultHic1000OutputColor: NXColor
    AdultHic1000OutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    AdultHic1000OutputLayer: int
    AdultHic1000OutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    AdultHic1700Angle: Expression
    AdultHic1700Offset: Expression
    AdultHic1700OutputColor: NXColor
    AdultHic1700OutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    AdultHic1700OutputLayer: int
    AdultHic1700OutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    BlackoutPointsColor: NXColor
    BlackoutZone: SelectDisplayableObjectList
    BonnetTop: SelectDisplayableObjectList
    BonnetTopNotMirrored: SelectDisplayableObjectList
    BumperBeam: SelectDisplayableObjectList
    BumperPlane: Plane
    ChildGtrUntranslateOutputColor: NXColor
    ChildGtrUntranslateOutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    ChildGtrUntranslateOutputLayer: int
    ChildGtrUntranslateOutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    ChildHic1000Angle: Expression
    ChildHic1000Offset: Expression
    ChildHic1000OutputColor: NXColor
    ChildHic1000OutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    ChildHic1000OutputLayer: int
    ChildHic1000OutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    ChildHic1700Angle: Expression
    ChildHic1700Offset: Expression
    ChildHic1700OutputColor: NXColor
    ChildHic1700OutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    ChildHic1700OutputLayer: int
    ChildHic1700OutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    Component: SelectDisplayableObjectList
    ConstructGeometryColor: NXColor
    ConstructGeometryFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    ConstructGeometryLayer: int
    ConstructGeometryWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    CornerBumperAngle: Expression
    CornerBumperAngleMarginal: Expression
    CornerBumperAngleSecondMarginal: Expression
    CreateBasins: bool
    CreateHeadImpactZones: bool
    CreateImpactGrid: bool
    CreateLegImpact: bool
    CreateNcapCircles: bool
    CreateNcapSheets: bool
    CreateOffsetData: bool
    CreateReferenceLines: bool
    CreateWrapAroundDistanceLines: bool
    DeletedPointsColor: NXColor
    DisplayConstructionGeometry: bool
    DisplayDeletedGridPoints: bool
    DisplayInterferenceResult: bool
    FrontRefAngle: Expression
    FrontRefAngleMarginal: Expression
    FrontRefAngleNcap: Expression
    FrontRefAngleNcapMarginal: Expression
    FrontReferenceAngleNcapSecondMarginal: Expression
    FrontReferenceAngleSecondMarginal: Expression
    GridAdultFullOutputLayer: int
    GridAdultPartialOutputLayer: int
    GridChildFullOutputLayer: int
    GridChildPartialOutputLayer: int
    GridFailColor: NXColor
    GridNCAP1000OutputColor: NXColor
    GridNCAP1000OutputLayer: int
    GridNCAP1350OutputColor: NXColor
    GridNCAP1350OutputLayer: int
    GridNCAP1700OutputColor: NXColor
    GridNCAP1700OutputLayer: int
    GridNCAP650OutputColor: NXColor
    GridNCAP650OutputLayer: int
    GridNCAPUntranslatedOutputColor: NXColor
    GridNcap1000OffsetScore: float
    GridNcap1350OffsetScore: float
    GridNcap1700OffsetScore: float
    GridNcap650OffsetScore: float
    GridNcapUntranslatedScore: float
    GridOutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    GridOutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    GridPassColor: NXColor
    GridPointsColor: NXColor
    GridUntranslatedOutputLayer: int
    GridWarningColor: NXColor
    HeadDiameter: Expression
    HeadDiameterMarginal: Expression
    HingeDistance: Expression
    HingePoint: Point
    Hood: SelectDisplayableObjectList
    InterferenceColor: NXColor
    InterferenceFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    InterferenceLayer: int
    InterferenceWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    InternalBumperLineMethod: Features.VehicleDesign.PedestrianProtectionBuilder.InternalBumperType
    IpFaces: SelectDisplayableObjectList
    LegImpactCurveOutputLayer: int
    LegSpreadsheet: str
    LegZonesOutputColor: NXColor
    LegZonesOutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    LegZonesOutputLayer: int
    LegZonesOutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    Loading: str
    LowerBumperAngle: Expression
    MirrorFaces: bool
    Plane: Plane
    PopupDistance: Expression
    PopupPoint: Point
    ProcessActiveHood: bool
    RearReferenceStepDistance: Expression
    ReferenceOutputColor: NXColor
    ReferenceOutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    ReferenceOutputLayer: int
    ReferenceOutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    RodDiameter: Expression
    SideRefAngle: Expression
    SideRefAngleMarginal: Expression
    SideRefAngleNcap: Expression
    SideRefAngleNcapMarginal: Expression
    SideReferenceAngleNcapSecondMarginal: Expression
    SideReferenceAngleSecondMarginal: Expression
    Standard: Features.VehicleDesign.PedestrianProtectionBuilder.StandardType
    StepDistance: Expression
    TransformMethod: Features.VehicleDesign.PedestrianProtectionBuilder.TransformMethods
    Type: Features.VehicleDesign.PedestrianProtectionBuilder.Types
    UpperBumperAngle: Expression
    UpperLegPositions: Section
    UpperLegZonesOutputLayer: int
    UseLoadingSpecifiedByStandard: bool
    UseMarginal: bool
    UseWindshieldEdge: bool
    WadBoundaryValue: Features.VehicleDesign.PedestrianProtectionBuilder.Wad
    WadEndValue: Features.VehicleDesign.PedestrianProtectionBuilder.Wad
    WadOutputColor: NXColor
    WadOutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    WadOutputLayer: int
    WadOutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    WadStartValue: Features.VehicleDesign.PedestrianProtectionBuilder.Wad
    Windshield: SelectDisplayableObjectList


    class Width(enum.Enum):
        Default = -1
        Normal = 0
        Thick = 1
        Thin = 2
        One = 5
        Two = 6
        Three = 7
        Four = 8
        Five = 9
        Six = 10
        Seven = 11
        Eight = 12
        Nine = 13
    

    class Wad(enum.Enum):
        First = 0
        Second = 1
        Third = 2
        Fourth = 3
        Fifth = 4
        Sixth = 5
    

    class Types(enum.Enum):
        HeadAndLegImpact = 0
        HeadImpact = 1
        LegImpact = 2
    

    class TransformMethods(enum.Enum):
        Translation = 0
        Rotation = 1
    

    class StandardType(enum.Enum):
        NorthAmerican = 0
        European = 1
        Japanese = 2
        Korean = 3
        Chinese = 4
    

    class InternalBumperType(enum.Enum):
        BumperTopPlane = 0
        BumperBeamFaces = 1
    

    class Font(enum.Enum):
        Default = 0
        Solid = 1
        Dashed = 2
        Phantom = 3
        Centerline = 4
        Dotted = 5
        LongDashed = 6
        DottedDashed = 7
    

class PedestrianProtection(Features.BodyFeature):
    def __init__(self) -> None: ...


class OilPanBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CarBodyFaces: ScCollector
    InnerAngle: Expression
    InnerOffset: Expression
    Loading: str
    OuterAngle: Expression
    OuterOffset: Expression
    Position: Features.VehicleDesign.OilPanBuilder.PositionType
    RequirementsControl: Features.VehicleDesign.OilPanBuilder.RequirementsControlType
    ShowDistanceMeasurement: bool
    Standard: str
    Visualization: Features.VehicleDesign.OilPanBuilder.VisualizationType


    class VisualizationType(enum.Enum):
        Curve = 0
        Surface = 1
        CurveandSurface = 2
    

    class RequirementsControlType(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

    class PositionType(enum.Enum):
        Front = 0
        Rear = 1
        Middle = 2
    

class OilPan(Features.BodyFeature):
    def __init__(self) -> None: ...


class MirrorCertificationBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetUserRemarks(self) -> str:
        ...
    def SetUserRemarks(self, userRemarks: str) -> None:
        ...
    def CreatePointWithBaseDataSGRPExpression(self) -> Point:
        ...
    AllowHeadAndEyeRotation: bool
    BackliteWindshieldFace: ScCollector
    BackliteWindshieldFacetBodies: SelectNXObjectList
    BezelCurve: Section
    ConvexRadius: Expression
    DeviateFromStandard: bool
    DriverSideFacetBodies: SelectNXObjectList
    DriverSideMirrorFace: ScCollector
    DriverSideStandard: Features.VehicleDesign.MirrorCertificationBuilder.DriverSideStandardsType
    EyeComponent: Assemblies.SelectComponent
    EyeMethod: Features.VehicleDesign.MirrorCertificationBuilder.EyeMethodType
    EyeMirrorRestrictions: ScCollector
    EyeMirrorRestrictionsFacetBodies: SelectNXObjectList
    EyePointMethod: Features.VehicleDesign.MirrorCertificationBuilder.EyePointMethodType
    Eyellipse: str
    EyellipsePercentile: Features.VehicleDesign.MirrorCertificationBuilder.EyellipsePercentileType
    GeneralColor: NXColor
    GenerateValidationLogFile: bool
    GroundWidePoint: Point
    HipPoint: Point
    InfiniteDistance: Expression
    InsideStandard: Features.VehicleDesign.MirrorCertificationBuilder.InsideStandardsType
    InstructionFieldPosition: Features.VehicleDesign.MirrorCertificationBuilder.InstructionFieldPositionType
    InstructionFieldType: Features.VehicleDesign.MirrorCertificationBuilder.InstructionFieldsType
    LeftEyeColor: NXColor
    LeftEyeDownColor: NXColor
    LeftEyeUpColor: NXColor
    Loading: str
    Location: Features.VehicleDesign.MirrorCertificationBuilder.LocationType
    MirrorFacetBodies: SelectNXObjectList
    MirrorOrientation: Features.VehicleDesign.MirrorCertificationBuilder.MirrorOrientationType
    MirrorSurface: ScCollector
    MirrorTargetRestrictions: ScCollector
    MirrorTargetRestrictionsFacetBodies: SelectNXObjectList
    MirrorType: Features.VehicleDesign.MirrorCertificationBuilder.MirrorSurfaceType
    PassengerSideStandard: Features.VehicleDesign.MirrorCertificationBuilder.PassengerSideStandardsType
    PivotPoint: Point
    PrimePoint: Point
    RightEyeColor: NXColor
    RightEyeDownColor: NXColor
    RightEyeUpColor: NXColor
    RotatedAngleY: Expression
    RotatedAngleZ: Expression
    ShowRays: bool
    ShowVisionCone: Features.VehicleDesign.MirrorCertificationBuilder.ShowVisionConeType
    TargetDistance: Expression
    TargetDistanceFar: Expression
    TargetWidthAngular: Expression
    TargetWidthLength: Expression
    TargetWidthLengthFar: Expression
    UseEyeFrom: Features.VehicleDesign.MirrorCertificationBuilder.EyeFromOptionType
    UseLoadingSpecifiedByStandard: bool
    ViewValidationResults: bool
    WheelProtrusionPoint: Point


    class ShowVisionConeType(enum.Enum):
        None = 0
        All = 1
        EyeToMirror = 2
        MirrorToTarget = 3
    

    class PassengerSideStandardsType(enum.Enum):
        UsaCanadaFmvss111Cmvsss111 = 0
        EuropeM1n1ClassiiiMirror200397EcEcer4602 = 1
        EuropeM1n1Only71127EuEcer4601Superceded = 2
        EuropeNotM1n171127EuEcer4601Superceded = 3
        JapanArticle44Trias29Trias39 = 4
        AustraliaAdr1402 = 5
        SaudiArabiaGulfStatesSsa770771Gs421442 = 6
        ChinaM1n1OnlyGb150842006 = 7
        ChinaNotM1n1Gb150842006 = 8
    

    class MirrorSurfaceType(enum.Enum):
        Planar = 0
        Spherical = 1
    

    class MirrorOrientationType(enum.Enum):
        AutoRotation = 0
        InteractiveAdjustment = 1
    

    class LocationType(enum.Enum):
        Inside = 0
        DriverSide = 1
        PassengerSide = 2
    

    class InstructionFieldsType(enum.Enum):
        Triangle = 0
        Rectangle = 1
    

    class InstructionFieldPositionType(enum.Enum):
        OnTargetWall = 0
        OnRoadSurface = 1
    

    class InsideStandardsType(enum.Enum):
        UsaCanadaFmvss111Cmvsss111 = 0
        Europe200397EcEcer4602 = 1
        JapanArticle44Trias29Trias39 = 2
        AustraliaAdr1402 = 3
        SaudiArabiaGulfStatesSsa770771Gs421442 = 4
        ChinaGb150842006 = 5
    

    class EyePointMethodType(enum.Enum):
        ByEceVisionPointsFeature = 0
        ByHipPoint = 1
    

    class EyeMethodType(enum.Enum):
        MaximumDistance = 0
        MinimumDistance = 1
        MeanDistance = 2
    

    class EyellipsePercentileType(enum.Enum):
        Percentile95 = 0
        Percentile99 = 1
    

    class EyeFromOptionType(enum.Enum):
        WorkPart = 0
        RootPart = 1
        OtherComponent = 2
    

    class DriverSideStandardsType(enum.Enum):
        UsaCanadaFmvss111Cmvsss111 = 0
        EuropeM1n1ClassiiiMirror200397EcEcer4602 = 1
        Europe71127EuEcer4601Superceded = 2
        JapanArticle44Trias29Trias39 = 3
        AustraliaAdr1402 = 4
        SaudiArabiaGulfStatesSsa770771Gs421442 = 5
        ChinaGb150842006 = 6
    

class MirrorCertification(Features.BodyFeature):
    def __init__(self) -> None: ...


class ManikinBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SaveToFile(self, filename: str) -> None:
        ...
    def OpenFromFile(self, filename: str) -> None:
        ...
    AHPHeight: Expression
    AHPLength: Expression
    AHPToSWCHeight: Expression
    AHPToSWCLength: Expression
    AllowPostureValueOutOfRange: bool
    ArmLength: Expression
    BackAngle: Expression
    Classification: Features.VehicleDesign.ManikinBuilder.ClassificationType
    CurrentManikinSize: str
    DrivingPostureCheck: bool
    ForearmLength: Expression
    HandGripLength: Expression
    HandLength: Expression
    JointAngleReport: bool
    LegLength: Expression
    PedalPlaneAngle: Expression
    Position: Features.VehicleDesign.ManikinBuilder.PositionType
    SAEPercentile: Features.VehicleDesign.ManikinBuilder.SAEPercentileType
    SgRPHeight: Expression
    SgRPLength: Expression
    SgRPWidth: Expression
    ShoulderToHipLength: Expression
    Standard: Features.VehicleDesign.ManikinBuilder.StandardType
    ThighLength: Expression
    TorsoLength: Expression
    WheelAngle: Expression
    WheelDiameter: Expression


    class StandardType(enum.Enum):
        SAEJ826Jul1995 = 0
        Saej833 = 1
        UserDefined = 2
        SAEJ826Nov2008 = 3
    

    class SAEPercentileType(enum.Enum):
        J826Type95thPercentile = 0
        J826Type50thPercentile = 1
        J826Type10thPercentile = 2
        J833LargeHuman95thMale = 3
        J833MediumHumanHalfwayPosition = 4
        J833SmallHuman5thFemale = 5
    

    class PositionType(enum.Enum):
        Driver = 0
        Passenger = 1
    

    class ClassificationType(enum.Enum):
        ClassA = 0
        ClassB = 1
    

class Manikin(Features.Feature):
    def __init__(self) -> None: ...


class InnerAngleBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CalculationMethod: Features.VehicleDesign.InnerAngleBuilder.CalculationMethodType
    CarBodyFaces: ScCollector
    InnerAngle: Expression
    Loading: str
    RequirementsControl: Features.VehicleDesign.InnerAngleBuilder.RequirementsControlType
    ShowDistanceMeasurement: bool
    Standard: str
    Visualization: Features.VehicleDesign.InnerAngleBuilder.VisualizationType
    WheelSize: Features.VehicleDesign.InnerAngleBuilder.WheelSizeType


    class WheelSizeType(enum.Enum):
        StaticRadius = 0
        Diameter = 1
    

    class VisualizationType(enum.Enum):
        Curve = 0
        Surface = 1
        CurveandSurface = 2
    

    class RequirementsControlType(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

    class CalculationMethodType(enum.Enum):
        Circular = 0
        Interpolated = 1
    

class InnerAngle(Features.BodyFeature):
    def __init__(self) -> None: ...


class HoodVisibilityBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AssoToggle: bool
    EyePoint: Point
    FacetBodies: SelectNXObjectList
    PitchAngle: float
    SelectFace: ScCollector


class HoodVisibility(Features.CurveFeature):
    def __init__(self) -> None: ...


class HeadImpactUpperRoofWizardBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    PlaneAPoint: Point
    PlaneBPoint: Point
    PlaneCPoint: Point
    PlaneDPoint: Point
    RearWindowTrim: ScCollector
    UpperRoofExterior: ScCollector
    UpperRoofInterior: ScCollector
    WindshieldTrim: ScCollector


class HeadImpactUpperRoofDetailBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CreateGeometry: bool
    D1: Expression
    D2: Expression
    PointA: Point
    PointAFlag: bool
    PointB: Point
    PointBFlag: bool
    PointC: Point
    PointCFlag: bool
    PointD: Point
    PointDFlag: bool
    PointM: Point
    PointMFlag: bool
    ReqVerticalMax: Expression
    ReqVerticalMin: Expression
    RoofOffset: Expression
    RoofRatio: Expression


class HeadImpactUpperRoofBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Initialize(self, parent: Features.VehicleDesign.HeadImpactBuilder) -> None:
        ...
    Geometry: Features.VehicleDesign.HeadImpactUpperRoofWizardBuilder
    Parameters: Features.VehicleDesign.HeadImpactUpperRoofDetailBuilder


class HeadImpactUpperRoof(Features.BodyFeature):
    def __init__(self) -> None: ...


class HeadImpactSideRailWizardBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DaylightOpeningLeft: ScCollector
    DaylightOpeningRight: ScCollector
    DoorOpeningLeft: ScCollector
    DoorOpeningRight: ScCollector
    UpperRoofInterior: ScCollector


class HeadImpactSideRailDetailBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CreateGeometry: bool
    PT11Left: Point
    PT11LeftFlag: bool
    PT11Right: Point
    PT11RightFlag: bool
    PT12Left: Point
    PT12LeftFlag: bool
    PT12Right: Point
    PT12RightFlag: bool
    PT14Left: Point
    PT14LeftFlag: bool
    PT14Right: Point
    PT14RightFlag: bool
    ReqHorizontalLeftExact: Expression
    ReqHorizontalRightExact: Expression
    ReqVerticalMax: Expression
    ReqVerticalMin: Expression
    SR1Left: Point
    SR1LeftFlag: bool
    SR1Offset: Expression
    SR1Right: Point
    SR1RightFlag: bool
    SR2ALeft: Point
    SR2ALeftFlag: bool
    SR2ARight: Point
    SR2ARightFlag: bool
    SR2BLeft: Point
    SR2BLeftFlag: bool
    SR2BRight: Point
    SR2BRightFlag: bool
    SR2Left: Point
    SR2LeftFlag: bool
    SR2Offset: Expression
    SR2Right: Point
    SR2RightFlag: bool


class HeadImpactSideRailBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Initialize(self, parent: Features.VehicleDesign.HeadImpactBuilder) -> None:
        ...
    Geometry: Features.VehicleDesign.HeadImpactSideRailWizardBuilder
    Parameters: Features.VehicleDesign.HeadImpactSideRailDetailBuilder


class HeadImpactSideRail(Features.BodyFeature):
    def __init__(self) -> None: ...


class HeadImpactRPillarWizardBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    RP2Left: Point
    RP2Right: Point
    RPillarLeft: ScCollector
    RPillarRight: ScCollector
    UpperRoofInterior: ScCollector


class HeadImpactRPillarDetailBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CreateGeometry: bool
    PT7Left: Point
    PT7LeftFlag: bool
    PT7Right: Point
    PT7RightFlag: bool
    RP1Left: Point
    RP1LeftFlag: bool
    RP1Ratio: Expression
    RP1Right: Point
    RP1RightFlag: bool
    RP2Left: Point
    RP2LeftFlag: bool
    RP2Offset: Expression
    RP2Right: Point
    RP2RightFlag: bool
    ReqHorizontalLeftMax: Expression
    ReqHorizontalLeftMin: Expression
    ReqHorizontalRightMax: Expression
    ReqHorizontalRightMin: Expression
    ReqVerticalMax: Expression
    ReqVerticalMin: Expression


class HeadImpactRPillarBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Initialize(self, parent: Features.VehicleDesign.HeadImpactBuilder) -> None:
        ...
    Geometry: Features.VehicleDesign.HeadImpactRPillarWizardBuilder
    Parameters: Features.VehicleDesign.HeadImpactRPillarDetailBuilder


class HeadImpactRPillar(Features.BodyFeature):
    def __init__(self) -> None: ...


class HeadImpactRearHeaderWizardBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    RearshieldEdge: ScCollector
    UpperRoofInterior: ScCollector


class HeadImpactRearHeaderDetailBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CreateGeometry: bool
    RHLeft: Point
    RHLeftFlag: bool
    RHOffsetMax: Expression
    RHRight: Point
    RHRightFlag: bool
    ReqHorizontalExact: Expression
    ReqVerticalMax: Expression
    ReqVerticalMin: Expression


class HeadImpactRearHeaderBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Initialize(self, parent: Features.VehicleDesign.HeadImpactBuilder) -> None:
        ...
    Geometry: Features.VehicleDesign.HeadImpactRearHeaderWizardBuilder
    Parameters: Features.VehicleDesign.HeadImpactRearHeaderDetailBuilder


class HeadImpactRearHeader(Features.BodyFeature):
    def __init__(self) -> None: ...


class HeadImpactOtherRailWizardBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DaylightOpeningLeft: ScCollector
    DaylightOpeningRight: ScCollector
    DoorOpeningLeft: ScCollector
    DoorOpeningRight: ScCollector
    SR3Left: Point
    SR3Right: Point
    UpperRoofInterior: ScCollector


class HeadImpactOtherRailDetailBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CreateGeometry: bool
    PT15Left: Point
    PT15LeftFlag: bool
    PT15Right: Point
    PT15RightFlag: bool
    PT16Left: Point
    PT16LeftFlag: bool
    PT16Right: Point
    PT16RightFlag: bool
    ReqHorizontalLeftExact: Expression
    ReqHorizontalRightExact: Expression
    ReqVerticalMax: Expression
    ReqVerticalMin: Expression
    SR3Left: Point
    SR3LeftFlag: bool
    SR3Offset: Expression
    SR3Right: Point
    SR3RightFlag: bool


class HeadImpactOtherRailBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Initialize(self, parent: Features.VehicleDesign.HeadImpactBuilder, row: int) -> None:
        ...
    Geometry: Features.VehicleDesign.HeadImpactOtherRailWizardBuilder
    Parameters: Features.VehicleDesign.HeadImpactOtherRailDetailBuilder


class HeadImpactOtherRail(Features.BodyFeature):
    def __init__(self) -> None: ...


class HeadImpactOPillarWizardBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CenterlineLeft: ScCollector
    CenterlineRight: ScCollector
    DaylightBottomLeft: Point
    DaylightBottomRight: Point
    DaylightOpeningLeft: ScCollector
    DaylightOpeningRight: ScCollector
    DoorOpeningLeft: ScCollector
    DoorOpeningRight: ScCollector
    DoorTopLeft: Point
    DoorTopRight: Point
    OP1Left: Point
    OP1Right: Point
    OPillarLeft: ScCollector
    OPillarRight: ScCollector
    UpperRoofInterior: ScCollector


class HeadImpactOPillarDetailBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CreateGeometry: bool
    DaylightBottomLeft: Point
    DaylightBottomLeftFlag: bool
    DaylightBottomRight: Point
    DaylightBottomRightFlag: bool
    DoorTopLeft: Point
    DoorTopLeftFlag: bool
    DoorTopRight: Point
    DoorTopRightFlag: bool
    OP1Left: Point
    OP1LeftFlag: bool
    OP1Right: Point
    OP1RightFlag: bool
    OP2Left: Point
    OP2LeftFlag: bool
    OP2Right: Point
    OP2RightFlag: bool
    PT6Left: Point
    PT6LeftFlag: bool
    PT6Right: Point
    PT6RightFlag: bool
    ReqHorizontalLeftExact: Expression
    ReqHorizontalRightExact: Expression
    ReqVerticalMax: Expression
    ReqVerticalMin: Expression


class HeadImpactOPillarBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Initialize(self, parent: Features.VehicleDesign.HeadImpactBuilder, row: int) -> None:
        ...
    Geometry: Features.VehicleDesign.HeadImpactOPillarWizardBuilder
    Parameters: Features.VehicleDesign.HeadImpactOPillarDetailBuilder


class HeadImpactOPillar(Features.BodyFeature):
    def __init__(self) -> None: ...


class HeadImpactFrontHeaderWizardBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    InteriorTrim: ScCollector
    SunRoof: ScCollector
    UpperRoofInterior: ScCollector
    WindshieldEdge: ScCollector


class HeadImpactFrontHeaderDetailBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CreateGeometry: bool
    FH1Left: Point
    FH1LeftFlag: bool
    FH1Offset: Expression
    FH1Right: Point
    FH1RightFlag: bool
    FH2Left: Point
    FH2LeftFlag: bool
    FH2Offset: Expression
    FH2Right: Point
    FH2RightFlag: bool
    ReqHorizontalExact: Expression
    ReqVerticalMax: Expression
    ReqVerticalMin: Expression


class HeadImpactFrontHeaderBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Initialize(self, parent: Features.VehicleDesign.HeadImpactBuilder) -> None:
        ...
    Geometry: Features.VehicleDesign.HeadImpactFrontHeaderWizardBuilder
    Parameters: Features.VehicleDesign.HeadImpactFrontHeaderDetailBuilder


class HeadImpactFrontHeader(Features.BodyFeature):
    def __init__(self) -> None: ...


class HeadImpactBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def AddAdditionalPillarFeature(self, feature: Features.VehicleDesign.HeadImpactOPillar) -> None:
        ...
    def AddAdditionalRailFeature(self, feature: Features.VehicleDesign.HeadImpactOtherRail) -> None:
        ...
    APillarFeature: Features.VehicleDesign.HeadImpactAPillar
    ActiveZone: bool
    BPillarFeature: Features.VehicleDesign.HeadImpactBPillar
    COGFrontXOffset: Expression
    COGFrontZOffset: Expression
    COGRearXOffset: Expression
    COGRearZOffset: Expression
    Calculation: Features.VehicleDesign.HeadImpactBuilder.CalculationType
    FrontHeaderFeature: Features.VehicleDesign.HeadImpactFrontHeader
    Loading: str
    RPillarFeature: Features.VehicleDesign.HeadImpactRPillar
    RearHeaderFeature: Features.VehicleDesign.HeadImpactRearHeader
    RequirementsControl: Features.VehicleDesign.HeadImpactBuilder.RequirementsControlType
    SideRailFeature: Features.VehicleDesign.HeadImpactSideRail
    Standard: str
    UpperRoofFeature: Features.VehicleDesign.HeadImpactUpperRoof
    VisualizeZone: bool
    ZoneDistance: Expression


    class RequirementsControlType(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

    class CalculationType(enum.Enum):
        BothSides = 0
        RightSide = 1
        LeftSide = 2
    

class HeadImpactBPillarWizardBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BP2Left: Point
    BP2Right: Point
    BPillarLeft: ScCollector
    BPillarRight: ScCollector
    CenterlineLeft: ScCollector
    CenterlineRight: ScCollector
    DaylightBottomLeft: Point
    DaylightBottomRight: Point
    DaylightOpeningLeft: ScCollector
    DaylightOpeningRight: ScCollector
    DoorOpeningLeft: ScCollector
    DoorOpeningRight: ScCollector
    DoorTopLeft: Point
    DoorTopRight: Point
    UpperRoofInterior: ScCollector


class HeadImpactBPillarDetailBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BP1Left: Point
    BP1LeftFlag: bool
    BP1Right: Point
    BP1RightFlag: bool
    BP2Left: Point
    BP2LeftFlag: bool
    BP2Right: Point
    BP2RightFlag: bool
    BP3Left: Point
    BP3LeftFlag: bool
    BP3Right: Point
    BP3RightFlag: bool
    BP4Left: Point
    BP4LeftFlag: bool
    BP4Right: Point
    BP4RightFlag: bool
    CreateGeometry: bool
    DaylightBottomLeft: Point
    DaylightBottomLeftFlag: bool
    DaylightBottomRight: Point
    DaylightBottomRightFlag: bool
    DoorTopLeft: Point
    DoorTopLeftFlag: bool
    DoorTopRight: Point
    DoorTopRightFlag: bool
    HorizontalLeftMax: Expression
    HorizontalLeftMin: Expression
    HorizontalRightMax: Expression
    HorizontalRightMin: Expression
    PT4Left: Point
    PT4LeftFlag: bool
    PT4Right: Point
    PT4RightFlag: bool
    ReqHorizontalLeftMax: Expression
    ReqHorizontalLeftMin: Expression
    ReqHorizontalRightMax: Expression
    ReqHorizontalRightMin: Expression
    ReqVerticalMax: Expression
    ReqVerticalMin: Expression


class HeadImpactBPillarBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Initialize(self, parent: Features.VehicleDesign.HeadImpactBuilder) -> None:
        ...
    Geometry: Features.VehicleDesign.HeadImpactBPillarWizardBuilder
    Parameters: Features.VehicleDesign.HeadImpactBPillarDetailBuilder


class HeadImpactBPillar(Features.BodyFeature):
    def __init__(self) -> None: ...


class HeadImpactAPillarWizardBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    APillarLeft: ScCollector
    APillarRight: ScCollector
    Dashboard: ScCollector
    Line1PointLeft: Point
    Line1PointRight: Point
    Plane1PointLeft: Point
    Plane1PointRight: Point
    Plane5PointLeft: Point
    Plane5PointRight: Point
    UpperRoofExterior: ScCollector
    UpperRoofInterior: ScCollector
    WindshieldTrim: ScCollector


class HeadImpactAPillarDetailBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AP1Left: Point
    AP1LeftFlag: bool
    AP1Right: Point
    AP1RightFlag: bool
    AP2Left: Point
    AP2LeftFlag: bool
    AP2Offset: Expression
    AP2Right: Point
    AP2RightFlag: bool
    AP3Left: Point
    AP3LeftFlag: bool
    AP3Right: Point
    AP3RightFlag: bool
    CreateGeometry: bool
    HorizontalLeftMax: Expression
    HorizontalLeftMin: Expression
    HorizontalRightMax: Expression
    HorizontalRightMin: Expression
    Line1Left: Point
    Line1LeftFlag: bool
    Line1Right: Point
    Line1RightFlag: bool
    MeasurementMethod: Features.VehicleDesign.HeadImpactAPillarDetailBuilder.MeasurementMethodType
    Plane1Left: Point
    Plane1LeftFlag: bool
    Plane1Right: Point
    Plane1RightFlag: bool
    Plane5Left: Point
    Plane5LeftFlag: bool
    Plane5Right: Point
    Plane5RightFlag: bool
    Point1Offset: Expression
    Point2Offset: Expression
    ReqHorizontalLeftMax: Expression
    ReqHorizontalLeftMin: Expression
    ReqHorizontalRightMax: Expression
    ReqHorizontalRightMin: Expression
    ReqVerticalMax: Expression
    ReqVerticalMin: Expression


    class MeasurementMethodType(enum.Enum):
        WrapAround = 0
        OnSurface = 1
        NotSpecified = 2
    

class HeadImpactAPillarBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Initialize(self, parent: Features.VehicleDesign.HeadImpactBuilder) -> None:
        ...
    Geometry: Features.VehicleDesign.HeadImpactAPillarWizardBuilder
    Parameters: Features.VehicleDesign.HeadImpactAPillarDetailBuilder


class HeadImpactAPillar(Features.BodyFeature):
    def __init__(self) -> None: ...


class HeadImpact(Features.BodyFeature):
    def __init__(self) -> None: ...


class GroundClearanceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DistanceToRoadGeneral: Expression
    DistanceToRoadUnderAxle: Expression
    ExtendSurface: bool
    ExtensionFactor: Expression
    FrontUnderAxleFace: ScCollector
    GeneralClearanceFace: ScCollector
    Loading: str
    Position: Features.VehicleDesign.GroundClearanceBuilder.PositionType
    RearUnderAxleFace: ScCollector
    RequirementsControl: Features.VehicleDesign.GroundClearanceBuilder.RequirementControls
    SectionCurve: Features.VehicleDesign.GroundClearanceBuilder.SectionCurveType
    ShowDistanceMeasurement: bool
    Standard: str
    SurfaceLength: Features.VehicleDesign.GroundClearanceBuilder.SurfaceLengthType
    UseGeneralSurface: bool
    UseUnderAxleSurface: bool
    Visualization: Features.VehicleDesign.GroundClearanceBuilder.VisualizationTypes
    WheelSize: Features.VehicleDesign.GroundClearanceBuilder.WheelType


    class WheelType(enum.Enum):
        StaticRadius = 0
        Diameter = 1
    

    class VisualizationTypes(enum.Enum):
        Curve = 0
        Surface = 1
        CurveandSurface = 2
    

    class SurfaceLengthType(enum.Enum):
        FrontToRear = 0
        FullVehicle = 1
    

    class SectionCurveType(enum.Enum):
        HorizontalLine = 0
        CircularArc = 1
    

    class RequirementControls(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

    class PositionType(enum.Enum):
        Front = 0
        Rear = 1
        Both = 2
    

class GroundClearance(Features.BodyFeature):
    def __init__(self) -> None: ...


class DynamicCurbBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FrontInnerLength: Expression
    FrontInnerOffset: Expression
    FrontOuterOffset: Expression
    FrontSelector: ScCollector
    InnerLineType: Features.VehicleDesign.DynamicCurbBuilder.MethodType
    Loading: str
    Position: Features.VehicleDesign.DynamicCurbBuilder.PositionType
    RearInnerLength: Expression
    RearInnerOffset: Expression
    RearOuterOffset: Expression
    RearSelector: ScCollector
    RequirementsControl: Features.VehicleDesign.DynamicCurbBuilder.RequirementsControlType
    ShowClearance: bool
    Standard: str
    Visualization: Features.VehicleDesign.DynamicCurbBuilder.VisualizationType
    WheelSize: Features.VehicleDesign.DynamicCurbBuilder.WheelType


    class WheelType(enum.Enum):
        StaticRadius = 0
        Diameter = 1
    

    class VisualizationType(enum.Enum):
        Curve = 0
        Surface = 1
        CurveSurface = 2
    

    class RequirementsControlType(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

    class PositionType(enum.Enum):
        Front = 0
        Rear = 1
        Both = 2
    

    class MethodType(enum.Enum):
        Horizontal = 0
        VerticalTangent = 1
        ParallelTangent = 2
    

class DynamicCurb(Features.BodyFeature):
    def __init__(self) -> None: ...


class CrashBarrierBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ActiveFront: bool
    ActiveRear: bool
    ActiveSide: bool
    FrontCrossPosition: Features.VehicleDesign.CrashBarrierBuilder.CrossPositionType
    FrontHeightAboveRoad: Expression
    FrontLoading: str
    FrontOverlapPercentage: Expression
    FrontOverlapSide: Features.VehicleDesign.CrashBarrierBuilder.OverlapSideType
    FrontPositionObject: Features.VehicleDesign.CrashBarrierBuilder.PositionObjectType
    FrontSelectPositioningFacetBodies: SelectNXObjectList
    FrontSelectPositioningObject: ScCollector
    FrontShape: Features.VehicleDesign.CrashBarrierBuilder.ShapeType
    FrontShift: Expression
    FrontUserDefineWidth: bool
    FrontUserDefineWidthValue: Expression
    LeftSideSelectPositioningFacetBodies: SelectNXObjectList
    LeftSideSelectPositioningObject: ScCollector
    RearCrossPosition: Features.VehicleDesign.CrashBarrierBuilder.CrossPositionType
    RearHeightAboveRoad: Expression
    RearLoading: str
    RearOverlapPercentage: Expression
    RearOverlapSide: Features.VehicleDesign.CrashBarrierBuilder.OverlapSideType
    RearPositionObject: Features.VehicleDesign.CrashBarrierBuilder.PositionObjectType
    RearSelectPositioningFacetBodies: SelectNXObjectList
    RearSelectPositioningObject: ScCollector
    RearShape: Features.VehicleDesign.CrashBarrierBuilder.ShapeType
    RearShift: Expression
    RearUserDefineWidth: bool
    RearUserDefineWidthValue: Expression
    RequirementsControl: Features.VehicleDesign.CrashBarrierBuilder.RequirementsControlsControlType
    RightSideSelectPositioningFacetBodies: SelectNXObjectList
    RightSideSelectPositioningObject: ScCollector
    SideCrossPosition: Features.VehicleDesign.CrashBarrierBuilder.CrossPositionType
    SideHeightAboveRoad: Expression
    SideLoading: str
    SideOverlapPercentage: Expression
    SideOverlapSide: Features.VehicleDesign.CrashBarrierBuilder.SideOverlapSideType
    SidePosition: Features.VehicleDesign.CrashBarrierBuilder.SidePositionType
    SidePositionObject: Features.VehicleDesign.CrashBarrierBuilder.PositionObjectType
    SideShape: Features.VehicleDesign.CrashBarrierBuilder.ShapeType
    SideShift: Expression
    SideUserDefineLength: bool
    SideUserDefineLengthValue: Expression
    Standard: str


    class SidePositionType(enum.Enum):
        Left = 0
        Right = 1
        Both = 2
    

    class SideOverlapSideType(enum.Enum):
        Front = 0
        Rear = 1
    

    class ShapeType(enum.Enum):
        RCAR2004Front = 0
        RCAR2004Rear = 1
        Rcar2006 = 2
        Iihs2009 = 3
        IIHS2009MultiDomain = 4
        RCAR2006MultiDomain = 5
    

    class RequirementsControlsControlType(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

    class PositionObjectType(enum.Enum):
        BaseData = 0
        VehicleObject = 1
    

    class OverlapSideType(enum.Enum):
        Right = 0
        Left = 1
    

    class CrossPositionType(enum.Enum):
        Centered = 0
        Overlap = 1
    

class CrashBarrier(Features.BodyFeature):
    def __init__(self) -> None: ...


class CloseRangeVisibilityBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ValidateBlindVolumes(self) -> None:
        ...
    def CreateCameraListItemBuilder(self) -> Features.VehicleDesign.CloseRangeCameraListItemBuilder:
        ...
    def CreateDemoCylinderListItemBuilder(self) -> Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder:
        ...
    CameraList: Features.VehicleDesign.CloseRangeCameraListItemBuilderList
    CylinderHeight: Expression
    CylinderRadius: Expression
    DemoCylinderList: Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilderList
    DistanceFromVehicle: Expression
    DriverSideExtension: Expression
    EyePointOffsetType: Features.VehicleDesign.CloseRangeVisibilityBuilder.EyePointOffsetTypes
    EyePointType: Features.VehicleDesign.CloseRangeVisibilityBuilder.EyePointTypes
    K1Coefficient: Expression
    K2Coefficient: Expression
    Loading: str
    MirrorBoundary: Section
    MirrorFaces: ScCollector
    MirrorFacetBodies: SelectNXObjectList
    MirrorRotationPoint: Point
    MirrorRotationYAngle: Expression
    MirrorRotationZAngle: Expression
    ObstructionFaces: ScCollector
    ObstructionFacetBodies: SelectNXObjectList
    PassengerSideExtension: Expression
    PathPositionType: Features.VehicleDesign.CloseRangeVisibilityBuilder.PathPositionTypes
    PositionMethod: Features.VehicleDesign.CloseRangeVisibilityBuilder.PositionMethods
    PositionPath: Features.VehicleDesign.CloseRangeVisibilityBuilder.PositionPaths
    RequirementsControl: Features.VehicleDesign.CloseRangeVisibilityBuilder.RequirementsControlType
    RotateMirrorFace: bool
    ShowBlindVolume: bool
    ShowExtendedEyes: bool
    ShowEyeLabels: bool
    ShowEyePoints: bool
    ShowPath: bool
    ShowPathPoints: bool
    ShowSightRays: bool
    ShowTorsoLine: bool
    Standard: str
    StepValue: float
    UseMirror: bool
    VehicleBodies: ScCollector
    VehicleFacetBodies: SelectNXObjectList
    WindowFaces: ScCollector
    WindowFacetBodies: SelectNXObjectList


    class RequirementsControlType(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

    class PositionPaths(enum.Enum):
        BaseData = 0
        VehicleObject = 1
    

    class PositionMethods(enum.Enum):
        TangentArea = 0
        VehicleContact = 1
        FrontView = 2
    

    class PathPositionTypes(enum.Enum):
        Both = 0
        Top = 1
        Bottom = 2
    

    class EyePointTypes(enum.Enum):
        Binocular = 0
        Monocular = 1
    

    class EyePointOffsetTypes(enum.Enum):
        NoOffset = 0
        AllOffsets = 1
        ForwardOffset = 2
        SidewaysOffset = 3
        UpwardOffset = 4
    

class CloseRangeVisibility(Features.Feature):
    def __init__(self) -> None: ...


class CloseRangeDemoCylinderListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder]) -> None:
        ...
    def Append(self, object: Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder, object2: Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class CloseRangeDemoCylinderListItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    PositionOnPath: Expression
    ShowDemoCylinder: bool
    ShowDemoCylinderRay: bool
    ValidateType: Features.VehicleDesign.CloseRangeDemoCylinderListItemBuilder.ValidateTypes


    class ValidateTypes(enum.Enum):
        Simple = 0
        Detailed = 1
    

class CloseRangeCameraListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.VehicleDesign.CloseRangeCameraListItemBuilder]) -> None:
        ...
    def Append(self, object: Features.VehicleDesign.CloseRangeCameraListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.VehicleDesign.CloseRangeCameraListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.VehicleDesign.CloseRangeCameraListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.VehicleDesign.CloseRangeCameraListItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.VehicleDesign.CloseRangeCameraListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.VehicleDesign.CloseRangeCameraListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.VehicleDesign.CloseRangeCameraListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.VehicleDesign.CloseRangeCameraListItemBuilder, object2: Features.VehicleDesign.CloseRangeCameraListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.VehicleDesign.CloseRangeCameraListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class CloseRangeCameraListItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CameraAxis: Axis
    CameraCsys: CoordinateSystem
    CameraFace: ScCollector
    CameraFacetBodies: SelectNXObjectList
    CameraType: Features.VehicleDesign.CloseRangeCameraListItemBuilder.Types
    FaceReverse: bool
    HorizontalLength: Expression
    InitialRadius: Expression
    UseCamera: bool
    VerticalLength: Expression
    ViewAngle: Expression


    class Types(enum.Enum):
        Round = 0
        Rectangle = 1
        Face = 2
    

class CloseRangeBlindVolumeListItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    EndParameter: float
    MaximumLength: float
    MeasuredLength: float
    StartParameter: float
    Status: bool


class BumperPendulumBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetPendulum(self, index: int) -> Features.VehicleDesign.PendulumPlacementBuilder:
        ...
    def GetPendulum(self, description: str) -> Features.VehicleDesign.PendulumPlacementBuilder:
        ...
    FrontCollector: ScCollector
    FrontFacetBodies: SelectNXObjectList
    RearCollector: ScCollector
    RearFacetBodies: SelectNXObjectList
    RequirementsControl: Features.VehicleDesign.BumperPendulumBuilder.RequirementsControlType
    Standard: str
    Visualization: Features.VehicleDesign.BumperPendulumBuilder.VisualizationType


    class VisualizationType(enum.Enum):
        Curve = 0
        Surface = 1
        CurveandSurface = 2
    

    class RequirementsControlType(enum.Enum):
        StandardDriven = 0
        UserDefined = 1
    

class BumperPendulum(Features.BodyFeature):
    def __init__(self) -> None: ...


class BaseDataWheelBuilder(Builder):
    def __init__(self) -> None: ...
    Camber: float
    CoordinateX: float
    CoordinateY: float
    CoordinateZ: float
    Diameter: float
    Name: str
    PositionDefinition: Features.VehicleDesign.BaseDataWheelBuilder.PositionDefinitionOptions
    RimOffset: float
    ShowSurface: bool
    ShowWireframe: bool
    StaticRadius: float
    Toe: float
    Track: float
    Width: float


    class PositionDefinitionOptions(enum.Enum):
        WheelCenterPoint = 0
        AttachmentPointRimOffset = 1
    

class BaseDataSourceBuilder(Builder):
    def __init__(self) -> None: ...
    BaseDataSource: Assemblies.SelectComponent
    BaseDataSourceMethod: Features.VehicleDesign.BaseDataSourceBuilder.BaseDataSourceOption
    DelayUpdate: bool
    RemoveBaseDataAttr: bool
    RemoveBaseDataSourceAttr: bool


    class BaseDataSourceOption(enum.Enum):
        SelectComponent = 0
        DisplayPart = 1
    

class BaseDataPassengerBuilder(Builder):
    def __init__(self) -> None: ...
    def Assign(self, other: Features.VehicleDesign.BaseDataPassengerBuilder) -> None:
        ...
    def SetSeatAngle(self, dValue: float) -> None:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataPassengerBuilder.SeatAngleExp to query or edit it.")"""
        ...
    def GetSeatAngle(self) -> float:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataPassengerBuilder.SeatAngleExp to query or edit it.")"""
        ...
    def SetBackAngle(self, dValue: float) -> None:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataPassengerBuilder.BackAngleExp to query or edit it.")"""
        ...
    def GetBackAngle(self) -> float:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataPassengerBuilder.BackAngleExp to query or edit it.")"""
        ...
    def SetHorizontalPointTravel(self, dValue: float) -> None:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataPassengerBuilder.HorizontalPointTravelExp to query or edit it.")"""
        ...
    def GetHorizontalPointTravel(self) -> float:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataPassengerBuilder.HorizontalPointTravelExp to query or edit it.")"""
        ...
    Active: bool
    BackAngleExp: Expression
    Description: str
    HeelReferencePoint: Point
    HeelReferencePointActive: bool
    HorizontalPointTravelExp: Expression
    SeatAngleExp: Expression
    SeatDirection: Features.VehicleDesign.BaseDataPassengerBuilder.SeatDirectionOptions
    SeatReferencePoint: Point
    SeatReferencePointActive: bool


    class SeatDirectionOptions(enum.Enum):
        Frontward = 0
        Backward = 1
        Left = 2
        Right = 3
        Custom = 4
    

class BaseDataLoadingWheelBuilder(Builder):
    def __init__(self) -> None: ...
    Camber: float
    CoordinateX: float
    CoordinateY: float
    CoordinateZ: float
    DataDefinition: Features.VehicleDesign.BaseDataLoadingWheelBuilder.DataDefinitionOptions
    DeltaCamber: float
    DeltaStaticRadius: float
    DeltaToe: float
    DeltaWidth: float
    DeltaX: float
    DeltaY: float
    DeltaZ: float
    DesignData: Features.VehicleDesign.BaseDataWheelBuilder
    StaticRadius: float
    Toe: float
    Width: float


    class DataDefinitionOptions(enum.Enum):
        Relative = 0
        Absolute = 1
    

class BaseDataLoadingBuilder(Builder):
    def __init__(self) -> None: ...
    def Assign(self, other: Features.VehicleDesign.BaseDataLoadingBuilder) -> None:
        ...
    def SetReferencePlane(self, referencePlane: DatumPlane) -> None:
        ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    Active: bool
    Color: NXColor
    DataDefinition: Features.VehicleDesign.BaseDataLoadingWheelBuilder.DataDefinitionOptions
    FrontWheel: Features.VehicleDesign.BaseDataLoadingWheelBuilder
    Name: str
    RearWheel: Features.VehicleDesign.BaseDataLoadingWheelBuilder
    Type: Features.VehicleDesign.BaseDataLoadingBuilder.LoadingType


    class LoadingType(enum.Enum):
        Standard = 0
        UserDefined = 1
    

class BaseDataImportExportBuilder(Builder):
    def __init__(self) -> None: ...
    def AssignItemNumber(self, itemId: str, itemName: str, itemRevision: str, idSensitivity: bool, revSensitivity: bool) -> None:
        ...
    def AssignItemRevision(self, itemId: str, itemRevision: str, revSensitivity: bool) -> None:
        ...
    def SetObjectCreateBuilder(self, objectCreateBuilder: PDM.ObjectCreateBuilder) -> None:
        ...
    DatasetName: str
    ExportOption: Features.VehicleDesign.BaseDataImportExportBuilder.ExportOptions
    OperateOption: Features.VehicleDesign.BaseDataImportExportBuilder.OperateOptions
    OverrideExistingExpressions: bool
    SpreadSheetFileName: str
    SpreadsheetItemID: str
    SpreadsheetItemName: str
    SpreadsheetItemRevision: str


    class OperateOptions(enum.Enum):
        Import = 0
        Export = 1
    

    class ExportOptions(enum.Enum):
        NewItem = 0
        ExistingItem = 1
    

class BaseDataDriverBuilder(Builder):
    def __init__(self) -> None: ...
    BackAngle: Expression
    BackAngleFixed: bool
    DriverSide: str
    FrontShoulderRoom: Expression
    HeelReferencePoint: Point
    HeelReferencePointActive: bool
    HorizontalPointTravel: Expression
    PedalReferencePoint: Point
    PedalReferencePointActive: bool
    RearShoulderRoom: Expression
    SeatReferencePoint: Point
    SeatReferencePointActive: bool
    SteeringWheelCenterPoint: Point
    SteeringWheelCenterPointActive: bool
    Transmission: str


class BaseDataBuilder(Builder):
    def __init__(self) -> None: ...
    def GetWheelbase(self) -> float:
        ...
    def GetFrontOverhang(self) -> float:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataBuilder.FrontOverhangExp to query or edit it.")"""
        ...
    def SetFrontOverhang(self, overhangFront: float) -> None:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataBuilder.FrontOverhangExp to query or edit it.")"""
        ...
    def GetRearOverhang(self) -> float:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataBuilder.RearOverhangExp to query or edit it.")"""
        ...
    def SetRearOverhang(self, overhangBack: float) -> None:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataBuilder.RearOverhangExp to query or edit it.")"""
        ...
    def GetVehicleLength(self) -> float:
        ...
    def GetVehicleWidth(self) -> float:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataBuilder.VehicleWidthExp to query or edit it.")"""
        ...
    def SetVehicleWidth(self, vehicleWidth: float) -> None:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataBuilder.VehicleWidthExp to query or edit it.")"""
        ...
    def GetBodyWidth(self) -> float:
        ...
    def SetBodyWidth(self, bodyWidth: float) -> None:
        """[Obsolete("Deprecated in NX9.0.1.  Obtain the expression using NXOpen.Features.VehicleDesign.BaseDataBuilder.BodyWidthExp to query or edit it.")"""
        ...
    def GetNthWheel(self, nWheelIndex: int) -> Features.VehicleDesign.BaseDataWheelBuilder:
        ...
    def CreatePassenger(self, pOther: Features.VehicleDesign.BaseDataPassengerBuilder) -> Features.VehicleDesign.BaseDataPassengerBuilder:
        ...
    def AddPassenger(self, passenger: Features.VehicleDesign.BaseDataPassengerBuilder) -> None:
        ...
    def RemovePassenger(self, passenger: Features.VehicleDesign.BaseDataPassengerBuilder) -> None:
        ...
    def GetPassengerCount(self) -> int:
        ...
    def GetNthPassenger(self, nIndex: int) -> Features.VehicleDesign.BaseDataPassengerBuilder:
        ...
    def CreateLoading(self, pOther: Features.VehicleDesign.BaseDataLoadingBuilder) -> Features.VehicleDesign.BaseDataLoadingBuilder:
        ...
    def AddLoading(self, loading: Features.VehicleDesign.BaseDataLoadingBuilder) -> None:
        ...
    def RemoveLoading(self, loading: Features.VehicleDesign.BaseDataLoadingBuilder) -> None:
        ...
    def GetLoadingCount(self) -> int:
        ...
    def GetNthLoading(self, nIndex: int) -> Features.VehicleDesign.BaseDataLoadingBuilder:
        ...
    BodyWidthExp: Expression
    Driver: Features.VehicleDesign.BaseDataDriverBuilder
    FrontOverhangExp: Expression
    LoadingDefinition: Features.VehicleDesign.BaseDataLoadingBuilder
    PassengerDefinition: Features.VehicleDesign.BaseDataPassengerBuilder
    RearOverhangExp: Expression
    ShowSurface: bool
    ShowWireframe: bool
    VehicleCategory: str
    VehicleDescription: str
    VehicleWidthExp: Expression
    WheelPositionDefinition: Features.VehicleDesign.BaseDataWheelBuilder.PositionDefinitionOptions


class AllAroundVisionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreatePointWithBaseDataSGRPExpression(self) -> Point:
        ...
    CarGeometry: ScCollector
    CreateIntersectionGeometry: bool
    DistanceTolerance: float
    FrontHeadRestGeometry: ScCollector
    ObstructedColor: NXColor
    RearHeadRestGeometry: ScCollector
    SeatReferencePoint: Point
    Translucency: int
    Type: Features.VehicleDesign.AllAroundVisionBuilder.Types
    UseFrontHeadRests: bool
    UseRearHeadRests: bool
    UseWireFrameOnly: bool
    VisibleColor: NXColor
    VisionAreaRadius: Expression
    WindowCurveGeometry: Section
    WindowFaceGeometry: ScCollector
    WindowType: Features.VehicleDesign.AllAroundVisionBuilder.WindowTypes


    class WindowTypes(enum.Enum):
        Face = 0
        Curve = 1
    

    class Types(enum.Enum):
        Pillars = 0
        Windows = 1
    

class AllAroundVision(Features.BodyFeature):
    def __init__(self) -> None: ...


