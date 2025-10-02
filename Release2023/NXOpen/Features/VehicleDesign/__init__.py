from ....NXOpen import *
from ...Features import *
from ..VehicleDesign import *

import typing
import enum

class WindshieldVisionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Imagebutton(self) -> None:
        ...
    def WsRevertButton(self) -> None:
        ...
    def WipeIllustration(self) -> None:
        ...
    def ValidationButton(self) -> None:
        ...
    AnalysisPrecision: float
    ArmLengthC: float
    ArmLengthL: float
    ArmLengthR: float
    BladeAngleC: float
    BladeAngleL: float
    BladeAngleR: float
    BladeLengthC: float
    BladeLengthL: float
    BladeLengthR: float
    CenterDefinitionPoint: Point
    Configuration: Features.VehicleDesign.ConfigurationBuilder
    CurvesSelect: ScCollector
    DefineSelect: Features.VehicleDesign.WindshieldVisionBuilder.EnumWsWipe
    DefinitionMethod: Features.VehicleDesign.WindshieldVisionBuilder.EnumWsDefinitionMethod
    EnlargedTestA: bool
    EnlargedTestAColor: NXColor
    EyellipsePercentile: Features.VehicleDesign.WindshieldVisionBuilder.EyePercentile
    FaceSelect: ScCollector
    FacetBodies: SelectNXObjectList
    FlatColorPicker: NXColor
    FlatPattern: bool
    GenerateValidationLogFile: bool
    H70value: float
    L31value: float
    LeftDefinitionP: Point
    OffsetCurves: bool
    OffsetCurvesColorPicker: NXColor
    OffsetValue: float
    ParkAngleC: float
    ParkAngleL: float
    ParkAngleR: float
    PatternType: Features.VehicleDesign.WindshieldVisionBuilder.EnumWsPatternType
    ReducedTestB: bool
    ReducedTestBColor: NXColor
    RightDefinitionP: Point
    SelectEyellipse: Features.SelectFeature
    SelectV1: Point
    SelectV2: Point
    Sgrp: Point
    TestA: bool
    TestAColorPicker: NXColor
    TestASurface: bool
    TestASurfaceColor: NXColor
    TestB: bool
    TestBColorPicker: NXColor
    TestBSurface: bool
    TestBSurfaceColor: NXColor
    TestC: bool
    TestCColorPicker: NXColor
    TestCSurface: bool
    TestCSurfaceColor: NXColor
    VehicleClassification: Features.VehicleDesign.WindshieldVisionBuilder.EnumWsVehicleClassification
    VehicleOW: int
    ViewValidationResults: bool
    W20value: float
    WBackangle: float
    WindshieldType: Features.VehicleDesign.WindshieldVisionBuilder.EnumWsWipe
    WipeAngleC: float
    WipeAngleL: float
    WipeAngleR: float
    WipeCurvesSelect: ScCollector
    WipedA: bool
    WiperAreaColorPicker: NXColor


    class EyePercentile(enum.Enum):
        Per95 = 0
        Per99 = 1
    

    class EnumWsWipe(enum.Enum):
        DefineWiperSystem = 0
        SelectWipedAera = 1
    

    class EnumWsVehicleOverall(enum.Enum):
        OW1520Mm = 0
        OW1520Mm1630Mm = 1
        OW1630Mm1730Mm = 2
        OW1730Mm = 3
    

    class EnumWsVehicleClassification(enum.Enum):
        TRUCK1020MUTruckCBEandCAE01020mm = 0
        TRUCK1270MUTruckCBEandCAE10201270mm = 1
        TRUCKUPMUTruckCBEandCAE1270Upmm = 2
        BUSESCBEMUBusesCBESchoolandCommercial12701520mm = 3
        BUSESFORWARDMUBusesForwardControlSchoolandCommercial12701520mm = 4
        FORWARDCONTROLMUForwardControlorMultipurposeAll = 5
        LIGHTDUTYMULightDutyUtilityVehicleAll = 6
        VANOPENMUVanMultistopOpen = 7
        TRUCKSCOEMUTrucksCOE1020Upmm = 8
    

    class EnumWsPatternType(enum.Enum):
        Tandem = 0
        Oppssite = 1
        SingleArm = 2
        ThreeArms = 3
    

    class EnumWsDefinitionMethod(enum.Enum):
        HipPoinUseHipPointandTorsoAngleECER432014 = 0
        UseExistingVPoints = 1
        UseExistingECEPointsFeatureECER125 = 2
    

class WindshieldVision(Features.BodyFeature):
    def __init__(self) -> None: ...


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
    SDistance: Expression
    SPlane: bool
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


class SeatLinesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Legend(self) -> None:
        ...
    def ReverseData(self) -> None:
        ...
    def CreatePointWithBaseDataSGRPExpression(self) -> Point:
        ...
    AhpHeight: Expression
    AhpLength: Expression
    BofrpLength: Expression
    BofrpSwcLength: Expression
    EntityLayer: int
    GridLineColorPicker: NXColor
    GridOffset: float
    Loading: str
    NoteColorPicker: NXColor
    NoteLayer: int
    NoteOffsetX: float
    NoteOffsetZ: float
    Point95Offset: float
    Population: Features.VehicleDesign.SeatLinesBuilder.PopulationRatio
    ReferencePoint: Point
    RiseAngle: Expression
    SeatHeight: Expression
    SeatLineColorPicker: NXColor
    SgrpPoint: Point
    SgrpWidth: Expression
    Standard: Features.VehicleDesign.SeatLinesBuilder.StandardOption
    TextSize: float
    TransmissionType: Features.VehicleDesign.SeatLinesBuilder.TransmissionOption
    UseStandardLoading: bool
    VehicleType: Features.VehicleDesign.SeatLinesBuilder.VehicleOption


    class VehicleOption(enum.Enum):
        ClassAVehicleOnlyforstudy = 0
        ClassBVehicle = 1
    

    class TransmissionOption(enum.Enum):
        Manual = 0
        Automatic = 1
    

    class StandardOption(enum.Enum):
        SAEJ1516Oct2011 = 0
        SAEJ4004Aug2008 = 1
    

    class PopulationRatio(enum.Enum):
        R5050 = 0
        R7525 = 1
        R9010to955 = 2
    

class SeatLines(Features.Feature):
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
    AngularTolerance: float
    DashSurface: ScCollector
    DistanceTolerance: float
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
    AdultHic1000AngleWindscreen: Expression
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
    ChildHic1000AngleForwardBle: Expression
    ChildHic1000AngleWindscreen: Expression
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
    CyclistGtrUntranslateOutputColor: NXColor
    CyclistGtrUntranslateOutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    CyclistGtrUntranslateOutputLayer: int
    CyclistGtrUntranslateOutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    CyclistHic1000Angle: Expression
    CyclistHic1000OutputColor: NXColor
    CyclistHic1000OutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    CyclistHic1000OutputLayer: int
    CyclistHic1000OutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    CyclistHic1700OutputColor: NXColor
    CyclistHic1700OutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    CyclistHic1700OutputLayer: int
    CyclistHic1700OutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    DeletedPointsColor: NXColor
    DisplayConstructionGeometry: bool
    DisplayDeletedGridPoints: bool
    DisplayInterferenceResult: bool
    EnableMlsStandard: bool
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
    RearRefAngle: Expression
    RearReferenceStepDistance: Expression
    ReferenceOutputColor: NXColor
    ReferenceOutputFont: Features.VehicleDesign.PedestrianProtectionBuilder.Font
    ReferenceOutputLayer: int
    ReferenceOutputWidth: Features.VehicleDesign.PedestrianProtectionBuilder.Width
    RodDiameter: Expression
    Roof: SelectDisplayableObjectList
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
    WadAdultCyclistBoundaryValue: Features.VehicleDesign.PedestrianProtectionBuilder.Wad
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
        Seventh = 6
        Eighth = 7
        Ninth = 8
        Tenth = 9
        Eleventh = 10
        Twelfth = 11
    

    class Types(enum.Enum):
        HeadAndLegImpact = 0
        HeadImpact = 1
        LegImpact = 2
    

    class TransformMethods(enum.Enum):
        Translation = 0
        Rotation = 1
    

    class StandardType(enum.Enum):
        NorthAmerican = 0
        GtrMls = 1
        European = 2
        EuropeanMls = 3
        Japanese = 4
        Korean = 5
        KoreanMls = 6
        Chinese = 7
        GtrTangentBasin = 8
    

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
        Eight = 8
        Nine = 9
        Ten = 10
        Eleven = 11
    

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


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MirrorCertificationBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetUserRemarks(self) -> str:
        ...
    def SetUserRemarks(self, userRemarks: str) -> None:
        ...
    def CreatePointWithBaseDataSGRPExpression(self) -> Point:
        ...
    def CreateGroundWidePointWithBaseData(self, sideToCreate: int) -> Point:
        ...
    def CreateGroundRearwardPointWithBaseData(self) -> Point:
        ...
    AllowHeadAndEyeRotation: bool
    BackliteWindshieldFace: ScCollector
    BackliteWindshieldFacetBodies: SelectNXObjectList
    BezelCurve: Section
    Calotte: Expression
    ChangeOfCurvature: Expression
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
    GroundForwardPoint: Point
    GroundRearwardPoint: Point
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
    TargetRadius: Expression
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
        EuropeEceR46Class2 = 9
        EuropeEceR46Class4 = 10
        EuropeEceR46Class5Close = 11
        EuropeEceR46Class5Large = 12
        EuropeEceR46Class6 = 13
        EuropeEceR46Class7 = 14
    

    class MirrorSurfaceType(enum.Enum):
        Planar = 0
        Spherical = 1
        Aspherical = 2
    

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
        EuropeEceR46Class2 = 7
        EuropeEceR46Class4 = 8
        EuropeEceR46Class7 = 9
    

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
    AHPToGCPHeight: Expression
    AHPToGCPHeightSecond: Expression
    AHPToGCPLength: Expression
    AHPToGCPLengthSecond: Expression
    AHPToSWCHeight: Expression
    AHPToSWCLength: Expression
    ActiveStickSecondLever: bool
    AlignmentMethod: Features.VehicleDesign.ManikinBuilder.AlignmentMethods
    AllowPostureValueOutOfRange: bool
    ArmLength: Expression
    BackAngle: Expression
    Classification: Features.VehicleDesign.ManikinBuilder.ClassificationType
    CreateFootComfort: bool
    CreateFootReach: bool
    CreateHandComfort: bool
    CreateHandReach: bool
    CreateSteeringWheel: bool
    CreateStickLever: bool
    CreateStickSecondLever: bool
    CurrentManikinSize: str
    DirectionControl: Features.VehicleDesign.ManikinBuilder.DirectionControlType
    DrivingPostureCheck: bool
    FRPToHCPHeight: Expression
    FRPToHCPLength: Expression
    ForearmLength: Expression
    GripDiameter: Expression
    GripForwardAngle: Expression
    GripForwardAngleSecondLever: Expression
    GripSidewaysAngle: Expression
    GripSidewaysAngleSecondLever: Expression
    HandGripLength: Expression
    HandLength: Expression
    HandPointActive: bool
    HideEnvelope: bool
    JointAngleReport: bool
    LegLength: Expression
    OccupantPosture: Features.VehicleDesign.ManikinBuilder.PostureType
    OperatorSize: Features.VehicleDesign.ManikinBuilder.OperatorSizeType
    Passenger: str
    PedalPlaneAngle: Expression
    Position: Features.VehicleDesign.ManikinBuilder.PositionType
    SAEPercentile: Features.VehicleDesign.ManikinBuilder.SAEPercentileType
    SRPToAHPHeightDistance: Expression
    SRPToAHPLengthDistance: Expression
    SRPToAHPWidth: Expression
    SRPToGCPHeightDistance: Expression
    SRPToGCPHeightDistanceSecond: Expression
    SRPToGCPLengthDistance: Expression
    SRPToGCPLengthDistanceSecond: Expression
    SRPToGCPWidth: Expression
    SRPToGCPWidthSecond: Expression
    SRPToHCPHeightDistance: Expression
    SRPToHCPLengthDistance: Expression
    SRPToHCPWidth: Expression
    SRPToSWCHeightDistance: Expression
    SRPToSWCLengthDistance: Expression
    SRPToSWCWidth: Expression
    SeatAngle: Expression
    SeatDirection: Features.VehicleDesign.ManikinBuilder.SeatDirectionOption
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
        SAEJ826Nov2015 = 4
        Iso34112007 = 5
        Iso66821986 = 6
        Milstd1333 = 7
    

    class SeatDirectionOption(enum.Enum):
        Frontward = 0
        Backward = 1
        Left = 2
        Right = 3
        Custom = 4
    

    class SAEPercentileType(enum.Enum):
        J826Type95thPercentile = 0
        J826Type50thPercentile = 1
        J826Type10thPercentile = 2
        J833LargeHuman95thMale = 3
        J833MediumHumanHalfwayPosition = 4
        J833SmallHuman5thFemale = 5
        J826TypeFMVSS208 = 6
        MIL1333Type95thPercentileMale = 7
        MIL1333Type95thPercentileFemale = 8
        MIL1333Type5thPercentileMale = 9
        MIL1333Type5thPercentileFemale = 10
    

    class PostureType(enum.Enum):
        Sitting = 0
        Standing = 1
    

    class PositionType(enum.Enum):
        Driver = 0
        Passenger = 1
    

    class OperatorSizeType(enum.Enum):
        Small = 0
        Medium = 1
        Large = 2
    

    class DirectionControlType(enum.Enum):
        Wheel = 0
        Stick = 1
        Handlebar = 2
    

    class ClassificationType(enum.Enum):
        ClassA = 0
        ClassB = 1
        ClassHE = 2
        ClassAS = 3
    

    class AlignmentMethods(enum.Enum):
        ProjectPerpendicular = 0
        ProjectAlongY = 1
        RotateAboutSgRP = 2
        DistanceFromSgRP = 3
    

class Manikin(Features.Feature):
    def __init__(self) -> None: ...


class InstrumentPanelVisibilityBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AnalysisType: Features.VehicleDesign.InstrumentPanelVisibilityBuilder.AnalysisTypeEnum
    DefinitionMode: Features.VehicleDesign.InstrumentPanelVisibilityBuilder.DefinitionModeEnum
    ModelType: Features.VehicleDesign.InstrumentPanelVisibilityBuilder.ModelTypeEnum
    PanelObstructionColor: NXColor
    PanelObstructionLayer: int
    PanelObstructionToggle: bool
    PercentileUsed: Features.VehicleDesign.InstrumentPanelVisibilityBuilder.PercentileUsedEnum
    SelectCenterPoint: Point
    SelectEyellipse: Features.SelectFeature
    SelectFaceCurves: ScCollector
    SelectFaces: ScCollector
    SelectHubCurves: ScCollector
    SelectHubOpenings: ScCollector
    SelectInnerRim: ScCollector
    SelectOuterRim: ScCollector
    SelectPlanarCurves: ScCollector
    SelectRimSection: ScCollector
    SelectSolidHub: ScCollector
    SelectSolidRim: ScCollector
    SelectSwitchFace: ScCollector
    SelectSwitchSolid: ScCollector
    SpecifyPlane: Plane
    SwitchObstructionColor: NXColor
    SwitchObstructionLayer: int
    SwitchObstructionToggle: bool
    SwitchType: Features.VehicleDesign.InstrumentPanelVisibilityBuilder.SwitchTypeEnum
    SwitchVisionColor: NXColor
    SwitchVisionLayer: int
    SwitchVisionToggle: bool
    WheelVisionColor: NXColor
    WheelVisionLayer: int
    WheelVisionToggle: bool


    class SwitchTypeEnum(enum.Enum):
        PlanarCurves = 0
        CurvesonaFace = 1
        Solid = 2
    

    class PercentileUsedEnum(enum.Enum):
        Per95 = 0
        Per99 = 1
    

    class ModelTypeEnum(enum.Enum):
        Curves = 0
        Solids = 1
    

    class DefinitionModeEnum(enum.Enum):
        Plane = 0
        Faces = 1
    

    class AnalysisTypeEnum(enum.Enum):
        SteeringWheelObstructionAnalysis = 0
        SmartSwitchesLeversObstructionAnalysis = 1
        CombinedObstructionAnalysis = 2
    

class InstrumentPanelVisibility(Features.BodyFeature):
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


class GlazingShadeBandsBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    EyeFeature: Features.Feature
    Eyellipse: Features.SelectFeature
    EyellipsePercentile: Features.VehicleDesign.GlazingShadeBandsBuilder.EyePercentile
    FixedSideGlazing: bool
    ForwardGlazing: bool
    ForwardGlazingGeometry: ScCollector
    Loading: str
    RearGlazing: bool
    RearGlazingGeometry: ScCollector
    SideGlazingGeometry: ScCollector
    UpperPoint: Point
    UseStandardLoading: bool
    UseViewHeight: bool
    ViewHeight: float


    class EyePercentile(enum.Enum):
        Per95 = 0
        Per99 = 1
    

class GlazingShadeBands(Features.CurveFeature):
    def __init__(self) -> None: ...


class EyellipseBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def VehicleARevertButton(self) -> None:
        ...
    def VehicleA2ImageButton(self) -> None:
        ...
    def VehicleA2RevertButton(self) -> None:
        ...
    def ClearanceImageButton(self) -> None:
        ...
    def Clearance2Image(self) -> None:
        ...
    def VehicleBImage(self) -> None:
        ...
    def UIllustrationButton(self) -> None:
        ...
    def URevertButton(self) -> None:
        ...
    def AssignStatusForClassA(self, index: Features.VehicleDesign.EyellipseBuilder.EnumLinkClassA, linkStatus: bool) -> None:
        ...
    def AssignStatusForClassB(self, index: Features.VehicleDesign.EyellipseBuilder.EnumLinkClassB, linkStatus: bool) -> None:
        ...
    AAlignmentMethod: Features.VehicleDesign.EyellipseBuilder.AlignmentMethods
    ABackAngle: Expression
    AH17Value: float
    AH1Value: float
    AH30Value: float
    AH70Value: float
    AH8Value: float
    AL1Value: float
    AL31Value: float
    AL6Value: float
    AL8Value: float
    APassenger: str
    ASRPToAHPHeightDistance: float
    ASRPToAHPLengthDistance: float
    ASRPToAHPWidth: float
    ASRPToBOFRPHeightDistance: float
    ASRPToBOFRPLengthDistance: float
    ASRPToBOFRPWidth: float
    ASRPToSWCHeightDistance: float
    ASRPToSWCLengthDistance: float
    ASRPToSWCWidth: float
    AScpXValue: float
    AScpZValue: float
    ASeatAngle: Expression
    ASeatDirection: Features.VehicleDesign.EyellipseBuilder.SeatDirectionOption
    ASeatPosition: Features.VehicleDesign.EyellipseBuilder.SeatPositionOption
    ASeatTrackTravel: Features.VehicleDesign.EyellipseBuilder.SeatTrackTravelOption
    AW20Value: float
    AhpPoint: Point
    BAlignmentMethod: Features.VehicleDesign.EyellipseBuilder.AlignmentMethods
    BBackAngle: float
    BH70Value: float
    BH8Value: float
    BL31Value: float
    BL8Value: float
    BMaleRatio: Features.VehicleDesign.EyellipseBuilder.EnumMaleRatio
    BPassenger: str
    BPostureType: Features.VehicleDesign.EyellipseBuilder.EnumPostureType
    BSRPToAHPHeightDistance: float
    BSRPToAHPLengthDistance: float
    BSRPToAHPWidth: float
    BScpPoint: Point
    BScpXValue: float
    BScpZValue: float
    BSeatAngle: Expression
    BSeatDirection: Features.VehicleDesign.EyellipseBuilder.SeatDirectionOption
    BSeatPosition: Features.VehicleDesign.EyellipseBuilder.SeatPositionType
    BSeatTrackTravel: Features.VehicleDesign.EyellipseBuilder.EnumBSeatType
    BSgrpPoint: Point
    BW20Value: float
    BofrpPoint: Point
    Clearance2DColorPicker: NXColor
    Clearance2DLayer: int
    Clearance3DColorPicker: NXColor
    Clearance3DLayer: int
    ClearanceRearAxisLayer: int
    ClearanceRearColorPicker: NXColor
    ContourAxisColorPicker: NXColor
    ContourAxisLayer: int
    ContourCentroidColorPicker: NXColor
    ContourCentroidLayer: int
    ContourColorPicker: NXColor
    ContourLayer: int
    ContourRearColorPicker: NXColor
    ContourRearLayer: int
    ContourSurfaceColorPicker: NXColor
    ContourSurfaceLayer: int
    CreateAxis: bool
    CreateClearance2D: bool
    CreateClearance3D: bool
    CreateClearanceRear: bool
    CreateContour: bool
    CreateContourAxis: bool
    CreateContourCentroid: bool
    CreateContourRear: bool
    CreateContourSurface: bool
    CreateEPoint: bool
    CreateH35Value: bool
    CreateH41Value: bool
    CreateH61Value: bool
    CreateL38Value: bool
    CreateL39Value: bool
    CreatePPoint: bool
    CreateUserEye: bool
    CreateUserHead: bool
    CreateVPoint: bool
    CreateW27Value: bool
    CreateW35Value: bool
    DefineEyeLocation: Features.VehicleDesign.EyellipseBuilder.EnumDefineEyeLocation
    DefineEyeOption: Features.VehicleDesign.EyellipseBuilder.EnumDefineEyeOption
    DisplayLeftAxis: bool
    DisplayLeftCentroid: bool
    DisplayLeftContour: bool
    DisplayLeftSurface: bool
    DisplayMiddleAxis: bool
    DisplayMiddleCentroid: bool
    DisplayMiddleContour: bool
    DisplayMiddleSurface: bool
    DisplayRightAxis: bool
    DisplayRightCentroid: bool
    DisplayRightContour: bool
    DisplayRightSurface: bool
    DisplaySaeEyePoint: bool
    DisplaySaePivotPoint: bool
    EPointAxisLayer: int
    EPointColorPicker: NXColor
    EceLoadingSpecified: bool
    EceLoadings: Features.VehicleDesign.EyellipseBuilder.EceLoadingsOption
    EceStandard: Features.VehicleDesign.EyellipseBuilder.EceStandardOption
    EceVisionPoints: bool
    EnumMethod: Features.VehicleDesign.EyellipseBuilder.EnumEyellipseMethod
    EyeDefinedPointL: Point
    EyeDefinedPointM: Point
    EyeDefinedPointR: Point
    Eyellipse: bool
    EyellipseLoadingSpecified: bool
    EyellipseLoadings: Features.VehicleDesign.EyellipseBuilder.EyellipseLoadingsOption
    EyellipsePercentile: Features.VehicleDesign.EyellipseBuilder.EyellipsePercentileOption
    EyellipseStandard: Features.VehicleDesign.EyellipseBuilder.EyellipseStandardOption
    H35Value: float
    H41Point: Point
    H41Value: float
    H61Value: float
    HCrossAft: float
    HForeAft: float
    HHeadContourCentroid: Point
    HVertical: float
    HalfAxis: float
    HeadContourPercentile: Features.VehicleDesign.EyellipseBuilder.HeadContourPercentileOption
    HeadLoadingSpecified: bool
    HeadLoadings: Features.VehicleDesign.EyellipseBuilder.HeadLoadingsOption
    HeadMoveToggle: bool
    HeadPositionContour: bool
    HeadStandard: Features.VehicleDesign.EyellipseBuilder.HeadStandardOption
    HumanFeature: Features.Feature
    L38Point: Point
    L38Value: float
    L39Point: Point
    L39Value: float
    LeanToggle: bool
    LeanW3: float
    LeanW7: float
    LeftAxisColorPicker: NXColor
    LeftAxisLayer: int
    LeftCentroidColorPicker: NXColor
    LeftCentroidLayer: int
    LeftContourColorPicker: NXColor
    LeftContourLayer: int
    LeftSurfaceColorPicker: NXColor
    LeftSurfaceLayer: int
    Loading: str
    MajorAxis: float
    MidAxisColorPicker: NXColor
    MidAxisLayer: int
    MidCentroidColorPicker: NXColor
    MidCentroidLayer: int
    MidContourColorPicker: NXColor
    MidContourLayer: int
    MidSurfaceColorPicker: NXColor
    MidSurfaceLayer: int
    MinorAxis: float
    MoveAngle: float
    MoveDirection: Features.VehicleDesign.EyellipseBuilder.EnumDirectionType
    MoveDistance: float
    NonAsso: bool
    PPointColorPicker: NXColor
    PPointLayer: int
    RightAxisColorPicker: NXColor
    RightAxisLayer: int
    RightCentroidColorPicker: NXColor
    RightCentroidLayer: int
    RightContourColorPicker: NXColor
    RightContourLayer: int
    RightSurfaceColorPicker: NXColor
    RightSurfaceLayer: int
    SAhpPoint: Point
    SaeEyeLayer: int
    SaeEyecolorPicker: NXColor
    SaePivotLayer: int
    SaePivotcolorPicker: NXColor
    ScpPoint: Point
    SeatPosition: Features.VehicleDesign.EyellipseBuilder.SeatPositionType
    SeatRiseAngle: Expression
    SelectEyellipse: Features.SelectFeature
    SelectHuman: Features.SelectFeature
    SgrpPoint: Point
    SipPoint: Point
    SnapH41Point: bool
    SnapL38Point: bool
    SnapL39Point: bool
    SpecifyPoint: bool
    SwcPoint: Point
    TransmissionType: Features.VehicleDesign.EyellipseBuilder.TransmissionTypeOption
    UAhpPoint: Point
    UCentroidPoint: Point
    UCrossCab: float
    UForceArt: float
    UH17Value: float
    UH8Value: float
    UL11Value: float
    UL8Value: float
    UMaleRatio: Features.VehicleDesign.EyellipseBuilder.EnumRatioType
    USRPToAHPHeightDistance: float
    USRPToAHPLengthDistance: float
    USRPToSWCHeightDistance: float
    USRPToSWCLengthDistance: float
    USpecifyPoint: bool
    USwcPoint: Point
    UVertical: float
    UW20Value: float
    UW8Value: float
    UserEUD2: float
    UserEUD3: float
    VPointColorPicker: NXColor
    VPointLayer: int
    VehicleClass: Features.VehicleDesign.EyellipseBuilder.ClassOption
    W27Value: float
    W35Value: float
    XEyeDefinedL: float
    XEyeDefinedM: float
    XEyeDefinedR: float
    XHCentroid: float
    XHHeadAxis: Direction
    XUAxis: Direction
    XUCentroid: float
    YEyeDefinedL: float
    YEyeDefinedM: float
    YEyeDefinedR: float
    YHCentroid: float
    YHHeadAxis: Direction
    YUAxis: Direction
    YUCentroid: float
    ZEyeDefinedL: float
    ZEyeDefinedM: float
    ZEyeDefinedR: float
    ZHCentroid: float
    ZUCentroid: float


    class TransmissionTypeOption(enum.Enum):
        WithClutchPedal = 0
        WithoutClutchPedal = 1
    

    class SeatTrackTravelOption(enum.Enum):
        OPTL23158mm = 0
        OP146mmTL23158mm = 1
        OP133mmTL23145mm = 2
        OPTL23133mm = 3
        OP121mmTL23132mm = 4
        OP108mmTL23120mm = 5
        OP1mmTL23108mm = 6
        Fixed = 7
    

    class SeatPositionType(enum.Enum):
        Driver = 0
        Passenger = 1
    

    class SeatPositionOption(enum.Enum):
        Driver = 0
        DriverandFrontOutboardPassenger = 1
        FrontOutboardPassenger = 2
        FrontCenterPassenger = 3
        AllOtherRows = 4
    

    class SeatDirectionOption(enum.Enum):
        Frontward = 0
        Backward = 1
        Left = 2
        Right = 3
        Custom = 4
    

    class HeadStandardOption(enum.Enum):
        Saej1052oct2017 = 0
        Saej1052sep2010 = 1
        Saej1052aug2002 = 2
        Saej1052apr1997 = 3
        UserDefinedheadgear = 4
    

    class HeadLoadingsOption(enum.Enum):
        EmptyweightJapancodriver = 0
        EmptyweightML1 = 1
        Vehiclegridparallel = 2
    

    class HeadContourPercentileOption(enum.Enum):
        PO95headpositioncontour = 0
        PO99headpositioncontour = 1
        POBoth = 2
    

    class EyellipseStandardOption(enum.Enum):
        Saej1052oct2017 = 0
        Saej1052oct2017JP = 1
        Saej1052oct2017NL = 2
        Saej941mar2010 = 3
        Saej941sep2002 = 4
        Saej941jun1997 = 5
        Saej941oct1985 = 6
        Umtri2005 = 7
        UserDefined = 8
    

    class EyellipsePercentileOption(enum.Enum):
        TangentCutoffEyellipse95 = 0
        TangentCutoffEyellipse99 = 1
        BothTangentCutoffEyellipse = 2
        InclusiveEyellipse95 = 3
        InclusiveEyellipse99 = 4
        BothInclusiveEyellipse = 5
    

    class EyellipseLoadingsOption(enum.Enum):
        EmptyweightJapancodriver = 0
        EmptyweightML1 = 1
        Vehiclegridparallel = 2
    

    class EnumRatioType(enum.Enum):
        U5050 = 0
        U9010 = 1
    

    class EnumPostureType(enum.Enum):
        Sitting = 0
        Standing = 1
    

    class EnumMaleRatio(enum.Enum):
        R5050 = 0
        R7525 = 1
        R9010or955 = 2
    

    class EnumLinkClassB(enum.Enum):
        L31 = 0
        W20 = 1
        H70 = 2
        L8 = 3
        H8 = 4
        BackAngle = 5
        Ul8 = 6
        Uw8 = 7
        Uh8 = 8
        Ul11 = 9
        Uh17 = 10
        Uw20 = 11
        Stt = 12
        SgRPToAHPWidth = 13
        SeatDirection = 14
        SeatAngle = 15
        SeatAlignment = 16
        SgrpToFrp = 17
    

    class EnumLinkClassA(enum.Enum):
        L1 = 0
        H1 = 1
        L31 = 2
        W20 = 3
        L8 = 4
        H8 = 5
        H30 = 6
        L6 = 7
        H17 = 8
        BackAngle = 9
        Stt = 10
        H70 = 11
        Transmission = 12
        SeatDirection = 13
        SeatAngle = 14
        SeatAlignment = 15
        SgrpToFrp = 16
        SgrpToAhp = 17
        SgrpToSwc = 18
        SwcToAhp = 19
        RiseAngle = 20
    

    class EnumEyellipseMethod(enum.Enum):
        Copy = 0
        Input = 1
    

    class EnumDirectionType(enum.Enum):
        Left = 0
        Right = 1
    

    class EnumDefineEyeOption(enum.Enum):
        Monocular = 0
        Binocular = 1
    

    class EnumDefineEyeLocation(enum.Enum):
        Left = 0
        Right = 1
    

    class EnumBSeatType(enum.Enum):
        OPTL23158mm = 0
        OP146mmTL23158mm = 1
        OP133mmTL23145mm = 2
        OPTL23133mm = 3
        OP121mmTL23132mm = 4
        OP108mmTL23120mm = 5
        OP100mmTL23108mm = 6
    

    class EceStandardOption(enum.Enum):
        R125 = 0
    

    class EceLoadingsOption(enum.Enum):
        EmptyweightJapancodriver = 0
        EmptyweightML1 = 1
        Vehiclegridparallel = 2
    

    class ClassOption(enum.Enum):
        ClassAVehicle = 0
        ClassBVehicle = 1
        ClassHEVehicle = 2
    

    class AlignmentMethods(enum.Enum):
        ProjectPerpendicular = 0
        ProjectAlongY = 1
        RotateAboutSgRP = 2
        DistanceFromSgRP = 3
    

class Eyellipse(Features.Feature):
    def __init__(self) -> None: ...


class EyeDefinitionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def EyeIllustration(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    EyeDefinitionType: Features.VehicleDesign.EyeDefinitionBuilder.EyeDefinition
    EyeFeature: Features.Feature
    EyellipsePercentile: Features.VehicleDesign.EyeDefinitionBuilder.EyePercentile
    PivotPoint: Point
    PointV1: Point
    PointV2: Point
    SelectEyellipse: Features.SelectFeature


    class EyePercentile(enum.Enum):
        Per95 = 0
        Per99 = 1
    

    class EyeDefinition(enum.Enum):
        EyeFeature = 0
        BySelectingPivotPoint = 1
        ClosestPointtoAPillarSection = 2
        V1Point = 3
        V2Point = 4
    

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


class DirectFieldViewBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ValidationButton(self) -> None:
        ...
    AllowExtension: bool
    BoundaryCurve: ScCollector
    BoundaryFace: ScCollector
    BoundaryFilter: Features.VehicleDesign.DirectFieldViewBuilder.BoundaryFilterType
    CurveColor: NXColor
    CurveLayer: int
    Driver: Features.VehicleDesign.DirectFieldViewBuilder.DriverType
    EnableValidationChecker: bool
    ExtensionLength: float
    EyeFeature: Features.Feature
    EyeRotateAngleDown: float
    EyeRotateAngleLeft: float
    EyeRotateAngleRight: float
    EyeRotateAngleUp: float
    EyeRotationType: Features.VehicleDesign.DirectFieldViewBuilder.EyeRotation
    Eyellipse: Features.SelectFeature
    EyellipsePercentile: Features.VehicleDesign.DirectFieldViewBuilder.EyePercentile
    FaceColor: NXColor
    FaceLayer: int
    GenerateLogFile: bool
    HeadTurnAngleLeft: float
    HeadTurnAngleRight: float
    HeadTurnType: Features.VehicleDesign.DirectFieldViewBuilder.HeadTurn
    LeftEye: Point
    LimitationType: Features.VehicleDesign.DirectFieldViewBuilder.LimitType
    Loading: str
    OutputBoundaryCurves: bool
    OutputVisionFace: bool
    RightEye: Point
    UseStandardLoading: bool
    ViewResults: bool


    class LimitType(enum.Enum):
        ByanApertureThroughAWindow = 0
        ByHeadTurnandEyeRotation = 1
    

    class HeadTurn(enum.Enum):
        Maximum = 0
        Easy = 1
        Customize = 2
        No = 3
    

    class EyeRotation(enum.Enum):
        Maximum = 0
        Easy = 1
        Customize = 2
    

    class EyePercentile(enum.Enum):
        Per95 = 0
        Per99 = 1
    

    class DriverType(enum.Enum):
        AGroupofDrivers = 0
        AnIndividualDriver = 1
    

    class BoundaryFilterType(enum.Enum):
        CurvesEdges = 0
        Faces = 1
    

class DirectFieldView(Features.BodyFeature):
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


class ConfigurationBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Loading: str
    StandardType: str
    UseStandardLoading: bool


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
    FovReverse: bool
    FovSheetBody: ScCollector
    HorizontalLength: Expression
    HorizontalViewAngle: Expression
    InitialRadius: Expression
    UseCamera: bool
    VerticalLength: Expression
    VerticalViewAngle: Expression
    ViewAngle: Expression


    class Types(enum.Enum):
        Round = 0
        Rectangle = 1
        Face = 2
        Fov = 3
    

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
    BogieWheelbase: float
    Camber: float
    CoordinateX: float
    CoordinateY: float
    CoordinateZ: float
    Diameter: float
    FlangeDiameter: float
    FlangeWidth: float
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
    UpdateBaseDataSourcePartAttr: bool


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
    AlignmentMethod: Features.VehicleDesign.BaseDataPassengerBuilder.AlignmentMethods
    BackAngleExp: Expression
    Description: str
    HandCenterPoint: Point
    HandCenterPointActive: bool
    HeelReferencePoint: Point
    HeelReferencePointActive: bool
    HorizontalPointTravelExp: Expression
    PassengerType: Features.VehicleDesign.BaseDataPassengerBuilder.PassengerTypeOptions
    SeatAngleExp: Expression
    SeatDirection: Features.VehicleDesign.BaseDataPassengerBuilder.SeatDirectionOptions
    SeatReferencePoint: Point
    SeatReferencePointActive: bool
    TypeStateActive: bool


    class SeatDirectionOptions(enum.Enum):
        Frontward = 0
        Backward = 1
        Left = 2
        Right = 3
        Custom = 4
    

    class PassengerTypeOptions(enum.Enum):
        Seating = 0
        Standing = 1
    

    class AlignmentMethods(enum.Enum):
        ProjectPerpendicular = 0
        ProjectAlongY = 1
        RotateAboutSgRP = 2
        DistanceFromSgRP = 3
    

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
    ShipDraft: float
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
    ControlType: str
    DriverSide: str
    DriverType: Features.VehicleDesign.BaseDataDriverBuilder.DriverTypeOptions
    FrontShoulderRoom: Expression
    GripDiameter: Expression
    GripSidewayLevelAngle: Expression
    HeelReferencePoint: Point
    HeelReferencePointActive: bool
    HorizontalPointTravel: Expression
    PedalReferencePoint: Point
    PedalReferencePointActive: bool
    RearShoulderRoom: Expression
    SeatReferencePoint: Point
    SeatReferencePointActive: bool
    SeatTrackRiseAngle: Expression
    SecondLeverActive: bool
    SecondLeverForwardAngle: Expression
    SecondLeverGripCenterPoint: Point
    SecondLeverGripCenterPointActive: bool
    SecondLeverSidewaysAngle: Expression
    SteeringWheelAngle: Expression
    SteeringWheelCenterPoint: Point
    SteeringWheelCenterPointActive: bool
    SteeringWheelDiameter: Expression
    ThrottleControlGripCenterPoint: Point
    ThrottleControlGripCenterPointActive: bool
    ThrottleForwardAngle: Expression
    ThrottleSidewaysAngle: Expression
    Transmission: str


    class DriverTypeOptions(enum.Enum):
        Seating = 0
        Standing = 1
        Autonomous = 2
    

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
    AfterPerpendicular: Expression
    BodyWidthExp: Expression
    Driver: Features.VehicleDesign.BaseDataDriverBuilder
    ForwardPerpendicular: Expression
    FrontOverhangExp: Expression
    LengthBetweenPerpendicular: Expression
    LoadingDefinition: Features.VehicleDesign.BaseDataLoadingBuilder
    PassengerDefinition: Features.VehicleDesign.BaseDataPassengerBuilder
    RearOverhangExp: Expression
    ScaleOfModel: float
    ShipForwardSet: bool
    ShowSurface: bool
    ShowWireframe: bool
    SingleWheelFront: bool
    VehicleCategory: str
    VehicleDescription: str
    VehicleHeight: Expression
    VehicleWidthExp: Expression
    WaterLineDraft: Expression
    WheelPositionDefinition: Features.VehicleDesign.BaseDataWheelBuilder.PositionDefinitionOptions


class APillarObstructionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Illustration(self) -> None:
        ...
    def ValidationButton(self) -> None:
        ...
    APillarGeometry: ScCollector
    APillarSide: Features.VehicleDesign.APillarObstructionBuilder.APillarSideType
    AdditionalGeometry: SelectNXObjectList
    AnalysisMethod: Features.VehicleDesign.APillarObstructionBuilder.AnalysisType
    Configuration: Features.VehicleDesign.ConfigurationBuilder
    EyeDefinition: Features.VehicleDesign.EyeDefinitionBuilder
    EyeRotationAngle: float
    GenerateValidationLogFile: bool
    HeadTurnAngle: float
    OuterEdge: ScCollector
    OuterPoint: Point
    PositionType: Features.VehicleDesign.APillarObstructionBuilder.Position
    TargetObstructionAngle: float
    ViewValidationResults: bool


    class Position(enum.Enum):
        OuterPointofAPillarSection = 0
        OuterEdgeofAPillar = 1
        EyeHeadTurnAngle = 2
    

    class APillarSideType(enum.Enum):
        LeftSide = 0
        RightSide = 1
    

    class AnalysisType(enum.Enum):
        APillarGeometry = 0
        CreateCriteriaGeometry = 1
    

class APillarObstruction(Features.CurveFeature):
    def __init__(self) -> None: ...


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


