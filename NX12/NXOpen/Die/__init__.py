from ...NXOpen import *
from ..Die import *

import typing
import enum

class WearPlateLocParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetWearPlateWidth(self, width: str) -> None:
        ...
    def SetWearPlateLength(self, length: str) -> None:
        ...
    def SetLocatorWidth(self, width: str) -> None:
        ...
    def SetLocatorDepth(self, depth: str) -> None:
        ...
    def SetRibSupportWidth(self, ribSupportWidth: str) -> None:
        ...
    def GetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetReliefAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetReliefAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetRecessAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetRecessAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def CreateChild(self) -> Die.WearPlateLocChildBuilder:
        ...
    def DeleteChild(self, diewearplatelocchild: Die.WearPlateLocChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.WearPlateLocChildBuilder]:
        ...
    BuildStatus: Die.DieBuildStatusOption
    DesignStatus: bool
    DisplayStatus: bool
    LocatorDepth: Expression
    LocatorPosition: Die.WearPlateLocParentBuilder.PositionType
    LocatorWidth: Expression
    ReverseNormal: int
    RibSupportWidth: Expression
    WearPlateLength: Expression
    WearPlateWidth: Expression


    class PositionType(enum.Enum):
        Left = 0
        Right = 1
        Both = 2
        Neither = 3
    

class WearPlateLocChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetPoint(self, pointLocation: str) -> None:
        ...
    def SetWearPlateWidth(self, width: str) -> None:
        ...
    def SetWearPlateLength(self, length: str) -> None:
        ...
    def SetLocatorWidth(self, width: str) -> None:
        ...
    def SetLocatorDepth(self, depth: str) -> None:
        ...
    def SetRibSupportWidth(self, ribSupportWidth: str) -> None:
        ...
    def GetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetReliefAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetReliefAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetRecessAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetRecessAttributes(self, title: str, value: str, color: int) -> None:
        ...
    BuildStatus: Die.DieBuildStatusOption
    DesignStatus: bool
    DisplayStatus: bool
    LocatorDepth: Expression
    LocatorPosition: Die.WearPlateLocChildBuilder.PositionType
    LocatorWidth: Expression
    Orientation: ISurface
    Point: Expression
    ReverseNormal: int
    RibSupportWidth: Expression
    WearPlateLength: Expression
    WearPlateWidth: Expression


    class PositionType(enum.Enum):
        Left = 0
        Right = 1
        Both = 2
        Neither = 3
    

class UncutRegionsBuilder(Builder):
    def __init__(self) -> None: ...
    def ReverseSide(self) -> None:
        ...
    Curves: Section
    Results: Die.UncutRegionsBuilder.ResultsType
    ToolAxis: Direction
    ToolSize: Expression


    class ResultsType(enum.Enum):
        OneSide = 0
        BothSides = 1
    

class TrimTaskBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CheckAndMovePlanes(self, origTip: Features.Feature, targetTip: Features.Feature, origStartPlaneTag: ISurface, origEndPlaneTag: ISurface, targetStartPlaneTag: ISurface, targetEndPlaneTag: ISurface) -> None:
        ...
    def SetTrimBounds(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetTrimBounds(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetScrapCutters(self, planes: typing.List[ISurface]) -> None:
        ...
    def GetScrapCutters(self) -> typing.List[ISurface]:
        ...
    def SetAssociativeObjects(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def GetAssociativeObjects(self) -> typing.List[DisplayableObject]:
        ...
    def SetCameraViews(self, objects: typing.List[View]) -> None:
        ...
    def GetCameraViews(self) -> typing.List[View]:
        ...
    def SetDetails(self, strings: str) -> None:
        ...
    def GetDetails(self) -> str:
        ...
    def GetCameraLayerAndXmlp(self, xmlpData: str) -> str:
        ...
    def SetCameraLayerAndXmlp(self, layerSettings: str, xmlpData: str) -> None:
        ...
    def SetCameraNames(self, strings: str) -> None:
        ...
    def GetCameraNames(self) -> str:
        ...
    AngleTolerance: float
    CamDirection: ILocation
    CamType: Die.TrimTaskBuilder.CamTypes
    CreateScrap: bool
    DistanceTolerance: float
    EndPlane: ISurface
    FinishOperation: bool
    LayoutFlange: bool
    MatchCutExtensionAngle: float
    MatchCutFirstRadius: float
    MatchCutNotchOffset: float
    MatchCutOffsetFromPlane: float
    MatchCutOffsetLength: float
    MatchCutScrapCutterLength: float
    MatchCutSecondRadius: float
    MatchCutThirdRadius: float
    MatchCutType: Die.TrimTaskBuilder.MatchCutTypes
    ReverseTrimSide: bool
    StartPlane: ISurface
    TippedProduct: Features.Feature
    TrimNewDieFace: bool


    class MatchCutTypes(enum.Enum):
        None = 0
        AtStart = 1
        AtEnd = 2
        AtBoth = 3
    

    class CamTypes(enum.Enum):
        Direct = 2
        Aerial = 0
        BaseMounted = 1
    

class TrimLineDevelopmentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def DefaultDraw(self) -> None:
        ...
    def CreateDefaultSpine(self) -> None:
        ...
    def Mesh(self) -> None:
        ...
    def Calculation(self) -> None:
        ...
    Addendum: ScCollector
    Associative: bool
    BendAllowance: Expression
    ConstraintCurveFromTargetRegion: Section
    ConstraintCurveFromUnformRegion: Section
    DistanceTolerance: float
    DrawDirection: Direction
    Faces: ScCollector
    FormingBoundary: ScCollector
    InferElementSize: bool
    InferThickness: bool
    LimitPoint1: Point
    LimitPoint2: Point
    Limits: Die.DieLimitsBuilder
    MaterialPropertyDensity: float
    MaterialPropertyE: float
    MaterialPropertyF: float
    MaterialPropertyInitialStrain: float
    MaterialPropertyK: float
    MaterialPropertyN: float
    MaterialPropertyPoisson: float
    MaterialPropertyR0: float
    MaterialPropertyR45: float
    MaterialPropertyR90: float
    MaterialPropertyYieldStress: float
    MaterialType: Die.TrimLineDevelopmentBuilder.MaterialTypeName
    MeshAttemptMapping: bool
    MeshElementSize: float
    MeshElementType: Die.TrimLineDevelopmentBuilder.MeshElement
    MeshMaxJacobian: float
    MeshMaxWarp: float
    MeshProcessFillet: bool
    MeshSizeVariation: int
    MeshSmallFeature: float
    MeshSplitQuad: bool
    OutputMethod: Die.TrimLineDevelopmentBuilder.OutputMethodName
    RegionPoint: Point
    RemoveLoops: bool
    ReverseSide: bool
    SampleDensityIndex: int
    SheetThickness: float
    Smoothing: Die.TrimLineDevelopmentBuilder.SmoothingName
    SolverConvergencyLevel: Die.TrimLineDevelopmentBuilder.Convergency
    SolverJoinOutputCurves: bool
    SolverMaxIterationSteps: int
    SolverSaveAnalysisResultsIntoFeature: bool
    Spine: ScCollector
    SpineRadius: float
    SurfaceType: Die.TrimLineDevelopmentBuilder.Surface
    Thickness: Expression


    class Surface(enum.Enum):
        Inner = 0
        Middle = 1
        Outer = 2
    

    class SmoothingName(enum.Enum):
        Linear = 0
        Cubic = 1
        Quintic = 2
    

    class OutputMethodName(enum.Enum):
        Geometric = 0
        Corrected = 1
        Both = 2
    

    class MeshElement(enum.Enum):
        Triangle = 0
        Quadrate = 1
    

    class MaterialTypeName(enum.Enum):
        Steel = 0
        Aluminum = 1
    

    class Convergency(enum.Enum):
        Low = 0
        Medium = 1
        High = 2
    

class TrimFlangeDieAssistantBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def NewTrimProfile(self) -> Die.DieAssistantTrimProfile:
        ...
    def NewFlangeProfile(self) -> Die.DieAssistantFlangeProfile:
        ...
    def AutoGen(self) -> None:
        ...
    def TrimSteelParms(self) -> None:
        ...
    def FlangeSteelWipeParms(self) -> None:
        ...
    def FlangeSteelRestrikeParms(self) -> None:
        ...
    def UpperPadParms(self) -> None:
        ...
    def LowerPostParms(self) -> None:
        ...
    def LowerScrapCutterParms(self) -> None:
        ...
    def LowerScrapCutterBaseParms(self) -> None:
        ...
    Clearance: float
    FlangeProfile: ScCollector
    FlangeProfileSet: Die.DieAssistantFlangeProfileList
    LowerBase: Plane
    PierceLocations: SelectPointList
    SheetMetal: SelectBody
    Thickness: float
    TrimProfileSet: Die.DieAssistantTrimProfileList
    UpperBase: Plane


class TrimFlangeDieAssistant(Features.BodyFeature):
    def __init__(self) -> None: ...


class Tip(Features.Feature):
    def __init__(self) -> None: ...
    def CreateDieData(self, allTips: bool) -> None:
        ...
    def DeleteDieData(self) -> None:
        ...
    def DisplayDieData(self) -> None:
        ...
    def UndisplayDieData(self) -> None:
        ...
    def TransformDiePoint(self, point: Point) -> None:
        ...
    def TransformDieDirection(self, vector: Direction) -> None:
        ...
    def SetReferenceCurves(self, objects: typing.List[Curve]) -> None:
        ...
    def MapCollectorToPart(self, collector: ScCollector) -> None:
        ...
    def MapCollectorToDie(self, collector: ScCollector) -> None:
        ...
    def MapEdge(self, inEdge: IProfile, partEdge: IProfile, dieEdge: IProfile) -> None:
        ...
    def GetUnprocessedHoles(self) -> typing.List[Edge]:
        ...
    def AddToDieData(self, objects: typing.List[Curve]) -> None:
        ...


class ThroatParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetExtensionAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetExtensionAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetCavityAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetCavityAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def CreateChild(self) -> Die.ThroatChildBuilder:
        ...
    def DeleteChild(self, diethroatchild: Die.ThroatChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.ThroatChildBuilder]:
        ...
    BuildStatus: Die.DieBuildStatusOption
    DesignStatus: bool
    DisplayStatus: bool
    Radius: float
    Step: float
    Type: Die.ThroatParentBuilder.TypeOption


    class TypeOption(enum.Enum):
        Wipe = 0
        Restrike = 1
    

class ThroatChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetSectionPlacement(self, sectionPlacement: str) -> None:
        ...
    def GetExtensionAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetExtensionAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetCavityAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetCavityAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetExtensionLength(self, extensionLength: str) -> None:
        ...
    def SetStepDistance(self, stepDistance: str) -> None:
        ...
    def SetUpperRadius(self, upperRadius: str) -> None:
        ...
    def SetLowerRadius(self, lowerRadius: str) -> None:
        ...
    def SetCavityOffset(self, cavityOffset: str) -> None:
        ...
    def SetCavityDepth(self, cavityDepth: str) -> None:
        ...
    BuildStatus: Die.DieBuildStatusOption
    CavityDepth: Expression
    CavityOffset: Expression
    DesignStatus: bool
    DisplayStatus: bool
    ExtensionLength: Expression
    LowerRadius: Expression
    Radius: float
    SectionPlacement: Expression
    Step: float
    StepDistance: Expression
    UpperRadius: Expression


    class TypeOption(enum.Enum):
        Wipe = 0
        Restrike = 1
    

class SteelInsertSegmentParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetBeltThickness(self, beltThickness: str) -> None:
        ...
    def SetReliefAngle(self, reliefAngle: str) -> None:
        ...
    def SetProfileRelief(self, profileRelief: str) -> None:
        ...
    def SetExtensionDistance(self, extensionDistance: str) -> None:
        ...
    def CreateChild(self) -> Die.SteelInsertSegmentChildBuilder:
        ...
    def DeleteChild(self, diesisegchild: Die.SteelInsertSegmentChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.SteelInsertSegmentChildBuilder]:
        ...
    AddEndPointsSwitch: int
    BeltThickness: Expression
    BuildStatus: Die.DieBuildStatusOption
    DesignStatus: bool
    DisplayStatus: bool
    ExtensionDistance: Expression
    ExtensionType: Die.SteelInsertSegmentParentBuilder.ExtensionTypeOption
    InsertType: Die.SteelInsertSegmentParentBuilder.InsertTypeOption
    ProfileRelief: Expression
    ProfileReliefToggle: bool
    ReliefAngle: Expression


    class InsertTypeOption(enum.Enum):
        Trim = 0
        Flange = 1
        OffsetFlange = 2
    

    class ExtensionTypeOption(enum.Enum):
        Constant = 0
        MaxdistPlusConst = 1
        Law = 2
    

class SteelInsertSegmentChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetBeltThickness(self, beltThickness: str) -> None:
        ...
    def SetReliefAngle(self, reliefAngle: str) -> None:
        ...
    def SetProfileRelief(self, profileRelief: str) -> None:
        ...
    def SetExtensionDistance(self, extensionDistance: str) -> None:
        ...
    BeltThickness: Expression
    BuildStatus: Die.DieBuildStatusOption
    DesignStatus: bool
    DisplayStatus: bool
    ExtensionDistance: Expression
    ExtensionType: Die.SteelInsertSegmentChildBuilder.ExtensionTypeOption
    InsertType: Die.SteelInsertSegmentChildBuilder.InsertTypeOption
    ProfileRelief: Expression
    ProfileReliefToggle: bool
    ReliefAngle: Expression
    SegDirection: Direction
    SegPoint: IOrientation


    class InsertTypeOption(enum.Enum):
        Trim = 0
        Flange = 1
        OffsetFlange = 2
    

    class ExtensionTypeOption(enum.Enum):
        Constant = 0
        MaxdistPlusConst = 1
        Law = 2
    

class SteelInsertSectionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetBackSideReliefDistance(self, backSideReliefDistance: str) -> None:
        ...
    def SetProductContactWidth(self, productContactWidth: str) -> None:
        ...
    def SetProductContactRelief(self, productContactRelief: str) -> None:
        ...
    def SetPlanarOffsetHeight(self, planarOffsetHeight: str) -> None:
        ...
    def SetOffsetProfileToTop(self, offsetProfileToTop: str) -> None:
        ...
    def SetBeltThickness(self, beltThickness: str) -> None:
        ...
    def SetReliefAngle(self, reliefAngle: str) -> None:
        ...
    def SetProfileRelief(self, profileRelief: str) -> None:
        ...
    def SetExtensionDistance(self, extensionDistance: str) -> None:
        ...
    def GetFormingAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetFormingAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetTrimWallAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetTrimWallAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetFlangeWallAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetFlangeWallAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetEndAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetEndAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetBackAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetBackAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetBaseAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetBaseAttributes(self, title: str, value: str, color: int) -> None:
        ...
    BackSideReliefDistance: Expression
    BeltThickness: Expression
    ExtensionDistance: Expression
    ExtensionType: Die.SteelInsertSectionBuilder.ExtensionTypeOption
    MassLimit: float
    OffsetProfileToTop: Expression
    PlanarOffsetHeight: Expression
    ProductContactRelief: Expression
    ProductContactWidth: Expression
    ProfileRelief: Expression
    ReliefAngle: Expression


    class ExtensionTypeOption(enum.Enum):
        Constant = 0
        MaxdistPlusConst = 1
        Law = 2
    

class SteelInsertBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetMainProfile(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetMainProfile(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetFlangeEndProfile(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetFlangeEndProfile(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetBackShape(self, backEntries: typing.List[ISurface]) -> None:
        ...
    def GetBackShape(self) -> typing.List[ISurface]:
        ...
    def GetHoleGridOrientation(self, gridOrigin: Point3d, gridMatrix: Matrix3x3) -> None:
        ...
    def SetHoleGridOrientation(self, gridOrigin: Point3d, gridMatrix: Matrix3x3) -> None:
        ...
    AngleTolerance: float
    BackReliefToggle: int
    BaseOrientation: ISurface
    BoltHoleParent: Die.HoleParentBuilder
    CamDirection: IReferenceAxis
    ConnectProfilesParent: Die.ConnectProfileParentBuilder
    DisplayHoles: bool
    DistanceTolerance: float
    DowelHoleParent: Die.HoleParentBuilder
    EndOrientation: ISurface
    InsertType: Die.SteelInsertBuilder.InsertTypeOption
    PierceHoleParent: Die.PierceHoleParentBuilder
    ProfileReliefToggle: int
    ReverseTrimSide: bool
    RibsParent: Die.FlangeSteelRibParentBuilder
    Section: Die.SteelInsertSectionBuilder
    SegmentsParent: Die.SteelInsertSegmentParentBuilder
    SheetMetal: Body
    StartOrientation: ISurface


    class InsertTypeOption(enum.Enum):
        Trim = 0
        Flange = 1
        OffsetFlange = 2
    

class SpringbackCompensationBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetProductPoints(self, productPoints: typing.List[Point3d]) -> None:
        ...
    def SetProductPoints(self, productPoints: typing.List[Point3d]) -> None:
        ...
    def GetSprungPoints(self, sprungPoints: typing.List[Point3d]) -> None:
        ...
    def SetSprungPoints(self, sprungPoints: typing.List[Point3d]) -> None:
        ...
    AngleTolerance: float
    CalculateMaxDeviation: bool
    ConvexityDirection: Direction
    ConvexityEnabled: bool
    CreateFacets: bool
    DefinedBy: Die.SpringbackCompensationBuilder.DefinedByType
    DeformationFactor: float
    Degree: Die.SpringbackCompensationBuilder.DegreeType
    DistanceTolerance: float
    Divisions: int
    DrawVector: Direction
    InnerCurve: Section
    IsGlobalDeformation: bool
    OneStep: Features.SelectFeature
    OuterCurve: Section
    ProductFacets: Facet.SelectFacetedBody
    ProductPointsFile: str
    ProductSheet: SelectBody
    ResultType: Die.SpringbackCompensationBuilder.ResultSheetType
    ShapeValue: float
    SmoothingFactor: float
    SprungFacets: Facet.SelectFacetedBody
    SprungPointsFile: str
    StepSize: float


    class ResultSheetType(enum.Enum):
        Compensated = 0
        Sprung = 1
    

    class DegreeType(enum.Enum):
        Two = 0
        Three = 1
        Five = 2
        Seven = 3
    

    class DefinedByType(enum.Enum):
        OneStepFeature = 0
        FacetedBodies = 1
        Points = 2
    

class SpringbackCompensation(Features.BodyFeature):
    def __init__(self) -> None: ...


class RotorSectionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetMinimumExtensionLength(self, minimumExtensionLength: str) -> None:
        ...
    def SetMinimumCavityDepth(self, minimumCavityDepth: str) -> None:
        ...
    def GetRotorAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetRotorAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetFormingAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetFormingAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetFlangeWallAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetFlangeWallAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetEndAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetEndAttributes(self, title: str, value: str, color: int) -> None:
        ...
    BuildStatus: Die.DieBuildStatusOption
    DesignStatus: bool
    DisplayStatus: bool
    MinimumCavityDepth: Expression
    MinimumExtensionLength: Expression


class RotorBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetFlangeBendProfile(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetFlangeBendProfile(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetEndOfFlangeProfile(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetEndOfFlangeProfile(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetStartOrientation(self, startEntries: typing.List[ISurface]) -> None:
        ...
    def GetStartOrientation(self) -> typing.List[ISurface]:
        ...
    def SetEndOrientation(self, endEntries: typing.List[ISurface]) -> None:
        ...
    def GetEndOrientation(self) -> typing.List[ISurface]:
        ...
    def SetRotorRotationAngle(self, degrees: str) -> None:
        ...
    AirCylinderParent: Die.PadParentBuilder
    AngleTolerance: float
    BoltHoleParent: Die.HoleParentBuilder
    DisplayHoles: bool
    DistanceTolerance: float
    DowelHoleParent: Die.HoleParentBuilder
    EndStopsParent: Die.PadParentBuilder
    HandlingHoleParent: Die.HoleParentBuilder
    PressDirection: IReferenceAxis
    RotorRotationAngle: Expression
    RotorSolid: Body
    Section: Die.RotorSectionBuilder
    SensorParent: Die.PadParentBuilder
    SetupBlocksParent: Die.PadParentBuilder
    SheetMetal: Body
    TbarHoleParent: Die.HoleParentBuilder
    ThroatDefinitionParent: Die.ThroatParentBuilder
    ThroatOrientation: CartesianCoordinateSystem
    WearPlateLocatorsParent: Die.WearPlateLocParentBuilder


class RibParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateChild(self) -> Die.RibChildBuilder:
        ...
    def DeleteChild(self, dieribchild: Die.RibChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.RibChildBuilder]:
        ...
    AdjustedThickness: float
    Angle: float
    BottomHorizontalOffset: float
    BottomLimitOffset: float
    BottomVerticalOffset: float
    BuildStatus: Die.DieBuildStatusOption
    CenterlineXyOffset: float
    DesignStatus: bool
    DisplayStatus: bool
    Height: float
    LccMinWidth: float
    LighteningCore: bool
    LighteningCoreClearance: float
    Rectangular: bool
    Thickness: float
    TopHorizontalOffset: float
    TopLimitOffset: float
    TopVerticalOffset: float
    XDistance: float
    XOffset: float
    YDistance: float
    YOffset: float


class RibChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetCenterline(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetCenterline(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetStart(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetStart(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetTopEnd(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetTopEnd(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetBottomEnd(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetBottomEnd(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    AdjustedThickness: float
    Angle: float
    Bottom: IOrientation
    BottomEnd: IOrientation
    BottomHorizontalOffset: float
    BottomLimitOffset: float
    BottomVerticalOffset: float
    BuildStatus: Die.DieBuildStatusOption
    CenterlineXyOffset: float
    DesignStatus: bool
    DisplayStatus: bool
    Height: float
    LccMinWidth: float
    LighteningCore: bool
    LighteningCoreClearance: float
    Rectangular: bool
    Start: IOrientation
    Thickness: float
    Top: IOrientation
    TopEnd: IOrientation
    TopHorizontalOffset: float
    TopLimitOffset: float
    TopVerticalOffset: float


class QuickBinderWrapBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Button: SelectBodyList
    ChangeRadius: Expression
    EditSizeChoice: Die.QuickBinderWrapBuilder.EditSizeType
    Matrix: Matrix3x3
    Origin: Point3d
    Type: Die.QuickBinderWrapBuilder.Types
    UMaximum: Expression
    UMinimum: Expression
    VMaximum: Expression
    VMinimum: Expression


    class Types(enum.Enum):
        Planar = 0
        Cylindrical = 1
        Conical = 2
    

    class EditSizeType(enum.Enum):
        Radius = 0
        Scale = 1
    

class QuickBinderBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateAnchorFace(self) -> int:
        ...
    def EditFace(self) -> None:
        ...
    def AddFace(self, type: Die.QuickBinderBuilder.Types) -> int:
        ...
    def RemoveFace(self) -> None:
        ...
    def SetReferencePoint(self, location: Point3d) -> None:
        ...
    def GetEdgesOfFace(self, faceIndex: int, edgeIndex: int, referencePoints: typing.List[Point3d]) -> None:
        ...
    AnchorBaseRadius: Expression
    AnchorRadius: Expression
    AnchorTopRadius: Expression
    BaseRadius: Expression
    CentralAngle: Expression
    EdgeIndexToEdit: int
    EditType: Die.QuickBinderBuilder.EditTypes
    End: Expression
    EndAngle: Expression
    Extend: Expression
    FaceIndexToEdit: int
    Faces: ScCollector
    Limits: GeometricUtilities.Limits
    OriginAnchorOrigin: Point3d
    Radius: Expression
    Start: Expression
    StartAngle: Expression
    TopRadius: Expression
    TransformMatrix: Matrix3x3
    TransformOrigin: Point3d
    Type: Die.QuickBinderBuilder.Types
    UMaximum: Expression
    UMinimum: Expression
    VMaximum: Expression
    VMinimum: Expression


    class Types(enum.Enum):
        Planar = 0
        Cylindrical = 1
        Conical = 2
        MonoArc = 3
    

    class EditTypes(enum.Enum):
        EdgeExtend = 0
        EdgeExtendStart = 1
        EdgeExtendEnd = 2
        EdgeAngleStart = 3
        EdgeAngleEnd = 4
        FaceRadius = 5
        FaceCentralAngle = 6
        FaceReverseConvexity = 7
        Transform = 8
        ExtendUMinimum = 9
        ExtendUMaximum = 10
        ExtendVMinimum = 11
        ExtendVMaximum = 12
    

class PressureSystemParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateChild(self) -> Die.PressureSystemChildBuilder:
        ...
    def DeleteChild(self, diepressuresystemchild: Die.PressureSystemChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.PressureSystemChildBuilder]:
        ...
    BuildStatus: Die.DieBuildStatusOption
    Clearance: float
    DesignStatus: bool
    Diameter: float
    DisplayStatus: bool
    Height: float
    XCount: int
    XDistance: float
    XOffset: float
    YCount: int
    YDistance: float
    YOffset: float


class PressureSystemChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BuildStatus: Die.DieBuildStatusOption
    Clearance: float
    Csys: CartesianCoordinateSystem
    DesignStatus: bool
    Diameter: float
    DisplayStatus: bool
    Height: float
    Point: Point


class PressModelRoot(TaggedObject):
    def __init__(self) -> None: ...
    def IsActive(self) -> bool:
        ...


class PressModel(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNumOperations(self) -> int:
        ...
    def SetOperationSlideHeight(self, operation: int, slideHeight: float) -> None:
        ...
    def SetOperationCushionSettings(self, operation: int, liftStartAngle: float, liftStopAngle: float, liftToDist: float, lockAtDist: float) -> None:
        ...
    def SetOperationUserTransportCurves(self, operation: int, vals: float) -> None:
        ...
    def SetOperationTransportCurveSet(self, operation: int, curveSet: int) -> None:
        ...
    def SetOperationCushionSettings2(self, operation: int, ventilationLiftDistance: float, ventilationLiftStay: int, binderWayLiftDistance: float, binderWayLiftDuration: int, upperLimit: float, lowerLimit: float) -> None:
        ...


class PointParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateChild(self) -> Die.PointChildBuilder:
        ...
    def DeleteChild(self, diepointchild: Die.PointChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.PointChildBuilder]:
        ...
    BuildStatus: Die.DieBuildStatusOption
    DesignStatus: bool
    DisplayStatus: bool


class PointChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BuildStatus: Die.DieBuildStatusOption
    DesignStatus: bool
    DisplayStatus: bool
    Point: Point


class PierceTaskBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetPierceBounds(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetPierceBounds(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetAssociativeObjects(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def GetAssociativeObjects(self) -> typing.List[DisplayableObject]:
        ...
    def SetCameraViews(self, objects: typing.List[View]) -> None:
        ...
    def GetCameraViews(self) -> typing.List[View]:
        ...
    def SetDetails(self, strings: str) -> None:
        ...
    def GetDetails(self) -> str:
        ...
    def GetCameraLayerAndXmlp(self, xmlpData: str) -> str:
        ...
    def SetCameraLayerAndXmlp(self, layerSettings: str, xmlpData: str) -> None:
        ...
    def SetCameraNames(self, strings: str) -> None:
        ...
    def GetCameraNames(self) -> str:
        ...
    def NewPierceHole(self, holeShape: Die.PierceItemBuilder.HoleShapeType) -> Die.PierceItemBuilder:
        ...
    AngleTolerance: float
    AssociatedObjects: SelectNXObjectList
    CamDirection: ILocation
    CamType: Die.PierceTaskBuilder.CamTypes
    CenterPointOption: Die.PierceTaskBuilder.CenterPointOptionTypes
    CreateScrap: bool
    DistanceTolerance: float
    FinishOperation: bool
    LayoutFlange: bool
    PierceHoles: ScCollector
    PierceHolesList: Die.PierceItemBuilderList
    PrecisionType: Die.PierceTaskBuilder.PrecisionTypes
    TipFeature: Features.SelectFeature
    TippedProduct: Features.Feature
    TrimNewDieFace: bool
    WithoutWorkflowSheet: Body


    class PrecisionTypes(enum.Enum):
        Gage = 0
        Critical = 1
        Standard = 2
    

    class CenterPointOptionTypes(enum.Enum):
        None = 0
        Die = 1
        Product = 2
        Both = 3
    

    class CamTypes(enum.Enum):
        Direct = 2
        Aerial = 0
        BaseMounted = 1
    

class PierceItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Die.PierceItemBuilder]) -> None:
        ...
    def Append(self, object: Die.PierceItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Die.PierceItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Die.PierceItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Die.PierceItemBuilder) -> None:
        ...
    def Erase(self, obj: Die.PierceItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Die.PierceItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Die.PierceItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Die.PierceItemBuilder, object2: Die.PierceItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Die.PierceItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PierceItemBuilder(NXObject):
    def __init__(self) -> None: ...
    def SetPierceObjects(self, objects: typing.List[IProfile]) -> None:
        ...
    def GetPierceObjects(self) -> typing.List[IProfile]:
        ...
    HoleShape: Die.PierceItemBuilder.HoleShapeType
    PunchDiameter: Expression
    PunchLength: Expression
    PunchRadius: Expression
    PunchWidth: Expression
    ReferenceVector: ILocation
    SizingMethod: Die.PierceItemBuilder.SizingMethodOption


    class SizingMethodOption(enum.Enum):
        Auto = 0
        Manual = 1
    

    class HoleShapeType(enum.Enum):
        Circular = 0
        Oblong = 1
        Square = 2
        Rectangular = 3
        RoundedRectangular = 4
        ChordRectangular = 5
        Hexagonal = 6
        Other = 7
    

class PierceHoleParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetProfileBlendRadius(self, profileBlendRadius: str) -> None:
        ...
    def SetDieClearance(self, dieClearance: str) -> None:
        ...
    def SetDiameter(self, diameter: str) -> None:
        ...
    def SetDepth(self, depth: str) -> None:
        ...
    def SetLength(self, length: str) -> None:
        ...
    def SetWidth(self, pierceHoleWidth: str) -> None:
        ...
    def SetSlugHoleDiameterIncrement(self, slugHoleDiameterIncrement: str) -> None:
        ...
    def SetSlugHoleOffset(self, slugHoleOffset: str) -> None:
        ...
    def SetBreakerHoleFactor(self, breakerHoleFactor: str) -> None:
        ...
    def SetBreakerHoleOffset(self, breakerHoleOffset: str) -> None:
        ...
    def SetBreakerHoleDepth(self, breakerHoleDepth: str) -> None:
        ...
    def GetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def SetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def GetSlugHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def SetSlugHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def GetBreakerHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def SetBreakerHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def CreateChild(self) -> Die.PierceHoleChildBuilder:
        ...
    def DeleteChild(self, dieholechild: Die.PierceHoleChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.PierceHoleChildBuilder]:
        ...
    BreakerHoleDepth: Expression
    BreakerHoleFactor: Expression
    BreakerHoleOffset: Expression
    BuildStatus: Die.DieBuildStatusOption
    CircularSlugHole: bool
    CommonSlugHole: bool
    Depth: Expression
    DesignStatus: bool
    Diameter: Expression
    DieClearance: Expression
    DisplayHoles: bool
    DisplayStatus: bool
    Length: Expression
    ProfileBlendRadius: Expression
    SlugHoleDiameterIncrement: Expression
    SlugHoleOffset: Expression
    Width: Expression


class PierceHoleChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetPierceHoleLocation(self, pierceHoleLocations: typing.List[ILocation]) -> None:
        ...
    def GetPierceHoleLocation(self) -> typing.List[ILocation]:
        ...
    def SetPierceHoleShape(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetPierceHoleShape(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetSlugHoleShape(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetSlugHoleShape(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetBreakerHoleShape(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetBreakerHoleShape(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetProfileBlendRadius(self, profileBlendRadius: str) -> None:
        ...
    def SetDieClearance(self, dieClearance: str) -> None:
        ...
    def SetDiameter(self, diameter: str) -> None:
        ...
    def SetDepth(self, depth: str) -> None:
        ...
    def SetLength(self, length: str) -> None:
        ...
    def SetWidth(self, width: str) -> None:
        ...
    def SetSlugHoleDiameterIncrement(self, slugHoleDiameterIncrement: str) -> None:
        ...
    def SetSlugHoleOffset(self, slugHoleOffset: str) -> None:
        ...
    def SetBreakerHoleFactor(self, breakerHoleFactor: str) -> None:
        ...
    def SetBreakerHoleOffset(self, breakerHoleOffset: str) -> None:
        ...
    def SetBreakerHoleDepth(self, breakerHoleDepth: str) -> None:
        ...
    def GetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def SetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def GetSlugHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def SetSlugHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def GetBreakerHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def SetBreakerHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def TranslatePierceHoleLocation(self, translateDist: Vector3d) -> None:
        ...
    BreakerHoleDepth: Expression
    BreakerHoleDirection: ILocation
    BreakerHoleFactor: Expression
    BreakerHoleLocation: ILocation
    BreakerHoleOffset: Expression
    BuildStatus: Die.DieBuildStatusOption
    CircularSlugHole: bool
    Depth: Expression
    DesignStatus: bool
    Diameter: Expression
    DieClearance: Expression
    DisplayHoles: bool
    DisplayStatus: bool
    Length: Expression
    PierceHoleDirection: ILocation
    ProfileBlendRadius: Expression
    ShapeType: Die.PierceHoleChildBuilder.ShapeTypeOption
    SlugHoleDiameterIncrement: Expression
    SlugHoleOffset: Expression
    Width: Expression


    class ShapeTypeOption(enum.Enum):
        Circular = 0
        Rectangular = 1
        Curve = 2
    

class PadParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def SetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def GetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetReliefAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetReliefAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def CreateChild(self) -> Die.PadChildBuilder:
        ...
    def DeleteChild(self, diepadchild: Die.PadChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.PadChildBuilder]:
        ...
    BuildStatus: Die.DieBuildStatusOption
    CenterHole: bool
    DesignStatus: bool
    Diameter: float
    DisplayStatus: bool
    Height: float
    HoleDiameter: float
    Length: float
    LocationOffset: float
    Relief: bool
    ReliefDepth: float
    ReliefWidth: float
    ShapeType: Die.PadParentBuilder.ShapeTypeOption
    SurfaceOffset: float
    Width: float


    class ShapeTypeOption(enum.Enum):
        Rectangular = 0
        Circular = 1
        Curve = 2
    

class PadChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetShape(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetShape(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def TranslateLocation(self, translateDist: Vector3d) -> None:
        ...
    def SetHoleCenters(self, holes: typing.List[Point]) -> None:
        ...
    def GetHoleCenters(self) -> typing.List[Point]:
        ...
    def GetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def SetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str) -> None:
        ...
    def GetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetReliefAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetReliefAttributes(self, title: str, value: str, color: int) -> None:
        ...
    BuildStatus: Die.DieBuildStatusOption
    CenterHole: bool
    DesignStatus: bool
    Diameter: float
    DisplayStatus: bool
    Height: float
    HoleDiameter: float
    Length: float
    LimitingSurface: IOrientation
    Location: ILocation
    LocationOffset: float
    LocationOffsetDirection: IReferenceAxis
    OrientationPlane: IOrientation
    Relief: bool
    ReliefDepth: float
    ReliefWidth: float
    ReverseOrientation: bool
    ShapeType: Die.PadChildBuilder.ShapeTypeOption
    SurfaceOffset: float
    Width: float


    class ShapeTypeOption(enum.Enum):
        Rectangular = 0
        Circular = 1
        Curve = 2
    

class OutputCurvesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateNonAssociative(self) -> typing.List[ICurve]:
        ...
    AngleTolerance: float
    DistanceTolerance: float
    FirstLimitPoint: Point3d
    LastLimitPoint: Point3d
    OffsetDistance: float
    ReferenceFeature: Features.Feature
    ReferencePoint: Point3d
    SmoothTolerance: float
    SmoothType: Die.OutputCurvesBuilder.SmoothTypes
    TrimCurveCreateType: Die.OutputCurvesBuilder.TrimCurveCreateTypes
    TrimCurveType: Die.OutputCurvesBuilder.TrimCurveTypes
    TrimOutputCurveType: Die.OutputCurvesBuilder.TrimOutputCurveTypes


    class TrimOutputCurveTypes(enum.Enum):
        Geometric = 0
        Corrected = 1
        Both = 2
    

    class TrimCurveTypes(enum.Enum):
        Trim = 0
        Extended = 1
        None = 2
    

    class TrimCurveCreateTypes(enum.Enum):
        Section = 0
        Surface = 1
    

    class SmoothTypes(enum.Enum):
        None = 0
        Cubic = 1
        Quintic = 2
    

class MachineReliefBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    BaseOffset: Expression
    BaseOrientation: Die.DiePlaneBuilder
    BeltAttributes: Die.DieAttributesBuilder
    BeltFaceThickness: Expression
    CamDirection: Die.DieDirectionBuilder
    DistanceTolerance: float
    End: Die.DieLocationBuilder
    InsideWallProfile: Section
    JogWall: bool
    MainProfile: Section
    MainProfileType: Die.MachineReliefBuilder.MainProfileTypes
    Offset: Expression
    ProfileOffset: Expression
    Relief: Expression
    ReliefOffset: Expression
    Start: Die.DieLocationBuilder
    SwitchTrimSide: bool
    Target: SelectBody
    TopOffset: Expression
    TrimOffset: Expression
    TrimSheet: SelectBody
    TrimSheetFace: ScCollector
    TrimSheetOffset: Expression
    TrimSheetType: Die.MachineReliefBuilder.TrimSheetTypes
    Type: Die.MachineReliefBuilder.Types
    WallOffset: Expression
    WallThickness: Expression


    class Types(enum.Enum):
        Cam = 0
        Relief = 1
        Thicken = 2
    

    class TrimSheetTypes(enum.Enum):
        Sheet = 0
        Face = 1
    

    class MainProfileTypes(enum.Enum):
        Exterior = 0
        Interior = 1
    

class MachineRelief(Features.BodyFeature):
    def __init__(self) -> None: ...


class LineupBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetProductBodies(self, objects: typing.List[Body]) -> None:
        ...
    def GetProductBodies(self) -> typing.List[Body]:
        ...
    def SetDetails(self, strings: str) -> None:
        ...
    def GetDetails(self) -> str:
        ...
    FlowDirection: Vector3d
    Origin: Point3d
    PressDirection: Vector3d


class KeywayParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetSlotAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetSlotAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def CreateChild(self) -> Die.KeywayChildBuilder:
        ...
    def DeleteChild(self, diekeywaychild: Die.KeywayChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.KeywayChildBuilder]:
        ...
    BuildStatus: Die.DieBuildStatusOption
    Depth: float
    DesignStatus: bool
    DisplayStatus: bool
    Length: float
    MinimumRibHeight: float
    PadHeight: float
    PadWidth: float
    PlacementOffset: float
    RunoffDepth: float
    RunoffDiameter: float
    RunoffLength: float
    RunoffType: Die.KeywayParentBuilder.RunoffTypeOption
    RunoffWidth: float
    Width: float


    class RunoffTypeOption(enum.Enum):
        Rectangular = 0
        Circular = 1
    

class KeywayChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetSlotAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetSlotAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    BuildStatus: Die.DieBuildStatusOption
    Depth: float
    DesignStatus: bool
    DisplayStatus: bool
    Length: float
    Location: Die.KeywayChildBuilder.LocationOption
    MinimumRibHeight: float
    Offset: float
    PadHeight: float
    PadWidth: float
    PlacementOffset: float
    Plane: IOrientation
    ReverseOrientation: bool
    RunoffDepth: float
    RunoffDiameter: float
    RunoffLength: float
    RunoffType: Die.KeywayChildBuilder.RunoffTypeOption
    RunoffWidth: float
    Width: float


    class RunoffTypeOption(enum.Enum):
        Rectangular = 0
        Circular = 1
    

    class LocationOption(enum.Enum):
        PositiveX = 0
        NegativeX = 1
        PositiveY = 2
        NegativeY = 3
    

class KeywayBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    BaseFlange: Section
    BaseOrientation: Die.DiePlaneBuilder
    CreateWithPad: bool
    DeckThickness: Expression
    DieCenterlineCoordinateSystem: SelectCartesianCoordinateSystem
    DistanceTolerance: float
    InteriorProfile: Section
    Location: Die.KeywayBuilder.LocationType
    MinimumRibHeight: Expression
    Offset: Expression
    PadAttributes: Die.DieAttributesBuilder
    PadHeight: Expression
    PadWidth: Expression
    PlacementOffset: Expression
    RunoffDepth: Expression
    RunoffLength: Expression
    RunoffRadius: Expression
    RunoffWidth: Expression
    SheetMetal: SelectNXObject
    SlotAttributes: Die.DieAttributesBuilder
    SlotDepth: Expression
    SlotLength: Expression
    SlotWidth: Expression
    Target: SelectNXObject
    Type: Die.KeywayBuilder.Types


    class Types(enum.Enum):
        Rectangular = 0
        Circular = 1
    

    class LocationType(enum.Enum):
        PositiveX = 0
        NegativeX = 1
        PositiveY = 2
        NegativeY = 3
    

class Keyway(Features.BodyFeature):
    def __init__(self) -> None: ...


class HoleParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str, depthTitle: str, counterBoreDiameterTitle: str) -> None:
        ...
    def SetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str, depthTitle: str, counterBoreDiameterTitle: str) -> None:
        ...
    def GetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def CreateChild(self) -> Die.HoleChildBuilder:
        ...
    def DeleteChild(self, dieholechild: Die.HoleChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.HoleChildBuilder]:
        ...
    BuildStatus: Die.DieBuildStatusOption
    CounterBoreDiameter: float
    CreateWithPad: bool
    Depth: float
    DesignStatus: bool
    Diameter: float
    DisplayHoles: bool
    DisplayStatus: bool
    DropThruDiameter: float
    PadDiameter: float
    PadHeight: float
    PlaneOffset: float


class HoleChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def TranslateCenter(self, translateDist: Vector3d) -> None:
        ...
    def GetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str, depthTitle: str, counterBoreDiameterTitle: str) -> None:
        ...
    def SetHoleAttributes(self, title: str, value: str, color: int, diameterTitle: str, depthTitle: str, counterBoreDiameterTitle: str) -> None:
        ...
    def GetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        ...
    BuildStatus: Die.DieBuildStatusOption
    Center: ILocation
    CounterBoreDiameter: float
    CreateWithPad: bool
    Depth: float
    DesignStatus: bool
    Diameter: float
    DisplayHoles: bool
    DisplayStatus: bool
    DropThruDiameter: float
    PadDiameter: float
    PadHeight: float
    Plane: ISurface
    PlaneOffset: float


class HeelpostBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    BaseOffset: Expression
    BaseOrientation: Die.DiePlaneBuilder
    Center: Die.DieLocationBuilder
    CreateFloor: bool
    Diameter: Expression
    DieCenterlineCoordinateSystem: SelectCoordinateSystem
    DistanceTolerance: float
    FloorThickness: Expression
    Height: Expression
    HoleAttributes: Die.DieAttributesBuilder
    HoleDiameterAttributes: Die.DieAttributesBuilder
    Length: Expression
    LocationOffset: Expression
    OffsetDirection: Die.DieDirectionBuilder
    PadAttributes: Die.DieAttributesBuilder
    PadOffset: Expression
    PadOrientation: Die.DiePlaneBuilder
    PadThickness: Expression
    ReliefAttributes: Die.DieAttributesBuilder
    ReliefDepth: Expression
    ReliefWidth: Expression
    Target: SelectNXObject
    Type: Die.HeelpostBuilder.Types
    UsePercent: bool
    WallACreate: bool
    WallAOffset: Expression
    WallARelief: bool
    WallAThickness: Expression
    WallBCreate: bool
    WallBOffset: Expression
    WallBRelief: bool
    WallBThickness: Expression
    WallCCreate: bool
    WallCOffset: Expression
    WallCRelief: bool
    WallCThickness: Expression
    WallDCreate: bool
    WallDOffset: Expression
    WallDRelief: bool
    WallDThickness: Expression
    WallPercentage: Expression
    Width: Expression
    XOffset: Expression
    YOffset: Expression


    class Types(enum.Enum):
        GuidepostWearplate = 0
        StorageBlock = 1
        SafetyBlock = 2
    

class Heelpost(Features.BodyFeature):
    def __init__(self) -> None: ...


class HandlingCoreParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateChild(self) -> Die.HandlingCoreChildBuilder:
        ...
    def DeleteChild(self, diehandlingcorechild: Die.HandlingCoreChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.HandlingCoreChildBuilder]:
        ...
    BuildStatus: Die.DieBuildStatusOption
    Clearance: float
    Depth: float
    DesignStatus: bool
    DisplayStatus: bool
    Height: float
    Width: float


class HandlingCoreChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def TranslateCenter(self, translateDist: Vector3d) -> None:
        ...
    BuildStatus: Die.DieBuildStatusOption
    Center: ILocation
    Clearance: float
    CoreOrientation: ISurface
    Depth: float
    DesignStatus: bool
    DisplayStatus: bool
    Height: float
    ReverseOrientation: bool
    Width: float


class HandlingCoreBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    BaseOrientation: Die.DiePlaneBuilder
    Clearance: Expression
    CoreOrientation: Die.DiePlaneBuilder
    Depth: Expression
    DistanceTolerance: float
    Height: Expression
    Location: Die.DieLocationsBuilder
    Target: SelectBody
    Type: Die.HandlingCoreBuilder.Types
    Width: Expression


    class Types(enum.Enum):
        AtLocation = 0
        FromBase = 1
        MapFromBase = 2
    

class HandlingCore(Features.BodyFeature):
    def __init__(self) -> None: ...


class FormTaskBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetRegionBounds(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetRegionBounds(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetShapeDetail(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetShapeDetail(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetShapeDetail(self, bodies: typing.List[Body]) -> None:
        ...
    def GetShapeDetail(self) -> typing.List[Body]:
        ...
    def SetDetails(self, strings: str) -> None:
        ...
    def GetDetails(self) -> str:
        ...
    AngleTolerance: float
    CamDirection: ILocation
    DistanceTolerance: float
    FinishOperation: bool
    PointInRegion: Point
    TippedProduct: Features.Feature


class FlangeTaskBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetRegionBounds(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetRegionBounds(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetShapeDetail(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetShapeDetail(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetShapeDetail(self, bodies: typing.List[Body]) -> None:
        ...
    def GetShapeDetail(self) -> typing.List[Body]:
        ...
    def SetAssociativeObjects(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def GetAssociativeObjects(self) -> typing.List[DisplayableObject]:
        ...
    def SetCameraViews(self, objects: typing.List[View]) -> None:
        ...
    def GetCameraViews(self) -> typing.List[View]:
        ...
    def SetDetails(self, strings: str) -> None:
        ...
    def GetDetails(self) -> str:
        ...
    def GetCameraLayerAndXmlp(self, xmlpData: str) -> str:
        ...
    def SetCameraLayerAndXmlp(self, layerSettings: str, xmlpData: str) -> None:
        ...
    def SetCameraNames(self, strings: str) -> None:
        ...
    def GetCameraNames(self) -> str:
        ...
    AngleTolerance: float
    CamDirection: ILocation
    CamType: Die.FlangeTaskBuilder.CamTypes
    DisplayRotatedItems: bool
    DistanceTolerance: float
    FinishOperation: bool
    PierceAndExtrude: bool
    PierceType: Die.FlangeTaskBuilder.PierceTypes
    PointInRegion: Point
    SpringbackAngle: str
    SpringbackType: Die.FlangeTaskBuilder.SpringbackTypes
    TippedProduct: Features.Feature


    class SpringbackTypes(enum.Enum):
        Constant = 0
        Law = 1
    

    class PierceTypes(enum.Enum):
        Gage = 0
        Critical = 1
        Standard = 2
    

    class CamTypes(enum.Enum):
        Direct = 0
        AerialConventional = 1
        BaseConventional = 2
        AerialRotary = 3
        BellCrank = 4
    

class FlangeSteelRibParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateChild(self) -> Die.FlangeSteelRibChildBuilder:
        ...
    def DeleteChild(self, diefsribchild: Die.FlangeSteelRibChildBuilder) -> None:
        ...
    def GetChildren(self) -> typing.List[Die.FlangeSteelRibChildBuilder]:
        ...
    Angle: float
    BackDistance: float
    BuildStatus: Die.DieBuildStatusOption
    ChamferDistance: float
    DesignStatus: bool
    DisplayStatus: bool
    Offset: float
    SheetMetalDistance: float
    Thickness: float
    UseAngle: int


class FlangeSteelRibChildBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Angle: float
    BackDistance: float
    BuildStatus: Die.DieBuildStatusOption
    ChamferDistance: float
    DesignStatus: bool
    DisplayStatus: bool
    Offset: float
    Plane: ISurface
    SheetMetalDistance: float
    Thickness: float
    UseAngle: int


class FingerClearanceNotchBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    Attributes: Die.DieAttributesBuilder
    BaseOrientation: Die.DiePlaneBuilder
    ClearanceDirection: Die.DieDirectionBuilder
    Depth: Expression
    DistanceTolerance: float
    ExtrudeWidth: Expression
    Geometry: SelectNXObjectList
    ReverseDirection: bool
    Section: Section
    Target: SelectBody
    Type: Die.FingerClearanceNotchBuilder.Types
    Width: Expression


    class Types(enum.Enum):
        Section = 0
        Face = 1
        SheetBody = 2
    

class FingerClearanceNotch(Features.BodyFeature):
    def __init__(self) -> None: ...


class FillBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetFillShape(self, bodies: typing.List[Body]) -> None:
        ...
    def GetFillShape(self) -> typing.List[Body]:
        ...
    def SetRegionBounds(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetRegionBounds(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    AngleTolerance: float
    CopyAndMirror: bool
    DistanceTolerance: float
    FillForAddendum: bool
    MirrorPlane: ISurface
    PointInRegion: Point
    TippedProduct: Features.Feature


class FillAreaBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    BaseOrientation: Die.DiePlaneBuilder
    Boundary: Section
    DistanceTolerance: float
    LowerLimitOffset: Expression
    LowerLimitSheet: SelectBody
    Target: SelectBody
    Type: Die.FillAreaBuilder.Types
    UpperLimitPlane: Die.DiePlaneBuilder
    UpperLimitSheet: SelectBody
    UpperLimitType: Die.FillAreaBuilder.UpperLimitTypes


    class UpperLimitTypes(enum.Enum):
        Sheet = 0
        Plane = 1
    

    class Types(enum.Enum):
        BaseFlange = 0
        ProductContact = 1
        ScrapArea = 2
        UserDefined = 3
    

class FillArea(Features.BodyFeature):
    def __init__(self) -> None: ...


class FaceSheetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    StampingOutput: Features.Feature


class DrawDiePunchSectionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetReliefDistance(self, reliefDistance: float) -> None:
        ...
    def SetDeckThickness(self, deckThickness: float) -> None:
        ...
    def SetWallThickness(self, wallThickness: float) -> None:
        ...
    def SetBaseThickness(self, baseThickness: float) -> None:
        ...
    def SetBaseWidth(self, baseWidth: float) -> None:
        ...
    def SetPartialRibHeight(self, partialRibHeight: float) -> None:
        ...
    def SetOffsetProfileToTop(self, offsetProfileToTop: float) -> None:
        ...
    def SetReliefAngle(self, reliefAngle: float) -> None:
        ...
    def SetBeltThickness(self, beltThickness: str) -> None:
        ...
    def SetDesignStatus(self, designStatus: bool) -> None:
        ...
    def SetDisplayStatus(self, displayStatus: bool) -> None:
        ...
    def GetFormingAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetFormingAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetBeltWallAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetBeltWallAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetBaseAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def SetBaseAttributes(self, title: str, value: str, color: int) -> None:
        ...
    def GetPunchProfileAttributes(self, title: str, value: str) -> None:
        ...
    def SetPunchProfileAttributes(self, title: str, value: str) -> None:
        ...
    BaseThickness: float
    BaseWidth: float
    BeltThickness: Expression
    BuildStatus: Die.DieBuildStatusOption
    DeckThickness: float
    DesignStatus: bool
    DisplayStatus: bool
    OffsetProfileToTop: float
    PartialRibHeight: float
    ReliefAngle: float
    ReliefDistance: float
    WallThickness: float


class DrawDiePunchBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetPunchProfile(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetPunchProfile(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    AlignStartOrientation: bool
    AngleTolerance: float
    BaseOrientation: ISurface
    BoltHoleParent: Die.HoleParentBuilder
    CastReliefParent: Die.CastReliefParentBuilder
    ClosedStartOrientation: IOrientation
    CoordinatingHoleParent: Die.HoleParentBuilder
    CorePunch: bool
    DeckParent: Die.DeckParentBuilder
    DieCenterlineCsys: CartesianCoordinateSystem
    DisplayHoles: bool
    DistanceTolerance: float
    DowelHoleParent: Die.HoleParentBuilder
    HandlingCoreParent: Die.HandlingCoreParentBuilder
    KeywayParent: Die.KeywayParentBuilder
    PartialRibbingParent: Die.RibParentBuilder
    PreliminaryBuild: bool
    PressureSystemParent: Die.PressureSystemParentBuilder
    PressureSystemReversalParent: Die.PointParentBuilder
    RibbingParent: Die.RibParentBuilder
    Section: Die.DrawDiePunchSectionBuilder
    SheetMetal: Body
    StrengtheningRibbingParent: Die.RibParentBuilder
    VentHoleParent: Die.HoleParentBuilder
    WearPlateParent: Die.PadParentBuilder


class DrawBeadTaperBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    TaperPoint: Point
    TaperRadius: Expression
    TaperType: Die.DrawBeadTaperBuilder.TaperTypes
    TaperWashoutHeight: Expression
    TaperWashoutLength: Expression


    class TaperTypes(enum.Enum):
        Spherical = 0
        Washout = 1
        Point = 2
    

class DrawBeadSegmentBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Die.DrawBeadSegmentBuilder]) -> None:
        ...
    def Append(self, object: Die.DrawBeadSegmentBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Die.DrawBeadSegmentBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Die.DrawBeadSegmentBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Die.DrawBeadSegmentBuilder) -> None:
        ...
    def Erase(self, obj: Die.DrawBeadSegmentBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Die.DrawBeadSegmentBuilder]:
        ...
    def SetContents(self, objects: typing.List[Die.DrawBeadSegmentBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Die.DrawBeadSegmentBuilder, object2: Die.DrawBeadSegmentBuilder) -> None:
        ...
    def Insert(self, location: int, object: Die.DrawBeadSegmentBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DrawBeadSegmentBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    EndLocation: GeometricUtilities.OnPathDimensionBuilder
    FemaleLeftRadius: Expression
    FemaleRightRadius: Expression
    Flow: bool
    MaleBeadHeight: Expression
    MaleBeadWidthType: Die.DrawBeadSegmentBuilder.MaleBeadWidthTypes
    MaleLeftSheetRadius: Expression
    MaleLeftTopRadius: Expression
    MaleLeftWallAngle: Expression
    MaleLeftWidth: Expression
    MaleRightSheetRadius: Expression
    MaleRightTopRadius: Expression
    MaleRightWallAngle: Expression
    MaleRightWidth: Expression
    MaleTransitionLength: Expression
    StartLocation: GeometricUtilities.OnPathDimensionBuilder
    Symmetry: bool


    class MaleBeadWidthTypes(enum.Enum):
        Constant = 0
        Derived = 1
    

class DrawBeadBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateSegmentsFromCenterlineCurves(self) -> None:
        ...
    def CreateDrawBeadSegment(self) -> Die.DrawBeadSegmentBuilder:
        ...
    def SetDefaultDrawDirection(self) -> None:
        ...
    def SetMoreDetails(self, strings: str) -> None:
        ...
    def GetMoreDetails(self) -> str:
        ...
    AngleTolerance: float
    BaseOrientation: Die.DrawBeadBuilder.OrientationTypes
    BuildEndTaper: bool
    BuildStartTaper: bool
    Centerline: Section
    CenterlineProjection: Die.DrawBeadBuilder.ProjectionDirectionTypes
    Clearance: Expression
    DistanceTolerance: float
    DrawDirection: Die.DieDirectionBuilder
    EndPoint: Die.DieLocationBuilder
    EndTaper: Die.DrawBeadTaperBuilder
    FemaleDepthType: Die.DrawBeadBuilder.FemaleDepthTypes
    FemaleDepthValue: Expression
    FemaleFaceAttribute: Die.DieAttributesBuilder
    FemaleSheetAttribute: Die.DieAttributesBuilder
    FemaleWidthType: Die.DrawBeadBuilder.FemaleWidthTypes
    FemaleWidthValue: Expression
    GenerateHeightCurve: bool
    MachineOffset: bool
    MachiningOffsetTitleAttribute: Die.DieAttributesBuilder
    MaleBeadPosition: Die.DrawBeadBuilder.MaleBeadPositionTypes
    MaleFaceAttribute: Die.DieAttributesBuilder
    MaleSheetAttribute: Die.DieAttributesBuilder
    MetalThickness: Expression
    OrientSectionToDraw: Die.DrawBeadBuilder.OrientSectionToDrawTypes
    Output: Die.DrawBeadBuilder.OutputTypes
    PlacementFace: ScCollector
    ReferenceDirection: bool
    ReverseMetalThickness: bool
    SegmentList: Die.DrawBeadSegmentBuilderList
    SheetMetalFaceAttribute: Die.DieAttributesBuilder
    SheetMetalSheetAttribute: Die.DieAttributesBuilder
    StartPoint: Die.DieLocationBuilder
    StartTaper: Die.DrawBeadTaperBuilder
    TaperBead: bool
    TransitionDefinition: Die.DrawBeadBuilder.TransitionDefinitionTypes


    class TransitionDefinitionTypes(enum.Enum):
        Automatic = 0
        Manual = 1
    

    class ProjectionDirectionTypes(enum.Enum):
        DrawDirection = 0
        NormalToPlacementFace = 1
    

    class OutputTypes(enum.Enum):
        None = 0
        Male = 1
        PlusFemale = 2
        PlusSheetMetal = 3
    

    class OrientSectionToDrawTypes(enum.Enum):
        DrawDirection = 0
        SheetMetalNormal = 1
    

    class OrientationTypes(enum.Enum):
        Orthogonal = 0
        Vertical = 1
    

    class MaleBeadPositionTypes(enum.Enum):
        Upper = 0
        Lower = 1
    

    class FemaleWidthTypes(enum.Enum):
        Derived = 0
        Constant = 1
    

    class FemaleDepthTypes(enum.Enum):
        Derived = 0
        Constant = 1
    

class DrawBead(Features.BodyFeature):
    def __init__(self) -> None: ...


class DirectionOption(enum.Enum):
    FromEnd = -1
    FromStart = 1


class DieSimCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Die.PressModelRoot]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def FindActivePressModel(self) -> Die.PressModel:
        ...
    def Tag(self) -> Tag: ...



class DieShoeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    BaseAttributes: Die.DieAttributesBuilder
    BaseFlangeSection: Section
    BaseOrientation: Die.DiePlaneBuilder
    CenterlineSlotAttributes: Die.DieAttributesBuilder
    CenterlineSlotCreate: bool
    CenterlineSlotDepth: Expression
    CenterlineSlotDirection: Die.DieDirectionBuilder
    CenterlineSlotWidth: Expression
    DeckCutoutsSection: Section
    DeckThickness: Expression
    DieBooleansList: Die.DieBooleanBuilderList
    DistanceTolerance: float
    FlangeThickness: Expression
    MainDeckAttributes: Die.DieAttributesBuilder
    MainDeckOffset: Expression
    MainDeckPlane: Die.DiePlaneBuilder
    MainDeckSection: Section
    WallThickness: Expression


class DieShoe(Features.BodyFeature):
    def __init__(self) -> None: ...


class DiePlaneBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CoordinateSystemMatrix: Matrix3x3
    CoordinateSystemOrigin: Point3d
    InputType: Die.DiePlaneBuilder.PlaneType
    ReverseSourceDirection: bool
    SelectPlane: SelectNXObject
    SpecifyPlane: Plane


    class PlaneType(enum.Enum):
        Selection = 0
        Plane = 1
        CoordinateSystem = 2
    

class DieLocationsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    List: Die.DieLocationBuilderList


class DieLocationBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Die.DieLocationBuilder]) -> None:
        ...
    def Append(self, object: Die.DieLocationBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Die.DieLocationBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Die.DieLocationBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Die.DieLocationBuilder) -> None:
        ...
    def Erase(self, obj: Die.DieLocationBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Die.DieLocationBuilder]:
        ...
    def SetContents(self, objects: typing.List[Die.DieLocationBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Die.DieLocationBuilder, object2: Die.DieLocationBuilder) -> None:
        ...
    def Insert(self, location: int, object: Die.DieLocationBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DieLocationBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CoordinateSystemMatrix: Matrix3x3
    CoordinateSystemOrigin: Point3d
    InputType: Die.DieLocationBuilder.LocationType
    Location: SelectNXObject
    Plane: Plane
    Point: Point
    Vector: Direction


    class LocationType(enum.Enum):
        SelectLocation = 0
        NewPoint = 1
        NewCoordinateSystem = 2
        NewVector = 3
        NewPlane = 4
    

class DieLimitsBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Die.DieLimitsBuilder]) -> None:
        ...
    def Append(self, object: Die.DieLimitsBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Die.DieLimitsBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Die.DieLimitsBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Die.DieLimitsBuilder) -> None:
        ...
    def Erase(self, obj: Die.DieLimitsBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Die.DieLimitsBuilder]:
        ...
    def SetContents(self, objects: typing.List[Die.DieLimitsBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Die.DieLimitsBuilder, object2: Die.DieLimitsBuilder) -> None:
        ...
    def Insert(self, location: int, object: Die.DieLimitsBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DieLimitsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetPathObjects(self, objectArray: typing.List[NXObject]) -> None:
        ...
    def SetPathObjects(self, objectArray: typing.List[NXObject]) -> None:
        ...
    def SetPath(self, path: Curve) -> None:
        ...
    def SetLimitsFromCurve(self, curve: Curve) -> None:
        ...
    def GetPath(self) -> Curve:
        ...
    def Validate(self) -> bool:
        ...
    Curve: ScCollector
    Point1: GeometricUtilities.OnPathDimensionBuilder
    Point2: GeometricUtilities.OnPathDimensionBuilder
    RemoveLimitPoints: bool
    Reverse: int


class DieDirectionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CoordinateSystemMatrix: Matrix3x3
    CoordinateSystemOrigin: Point3d
    Direction: SelectNXObject
    InputType: Die.DieDirectionBuilder.DirectionType
    ReverseSourceDirection: bool
    Vector: Direction


    class DirectionType(enum.Enum):
        Selection = 0
        CoordinateSystem = 1
        Vector = 2
    

class DieCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def DrawDiePunch(self, drawDiePunch: Features.Feature) -> Die.DrawDiePunchBuilder:
        ...
    def FormTask(self, formTask: Features.Feature) -> Die.FormTaskBuilder:
        ...
    def Rotor(self, rotor: Features.Feature) -> Die.RotorBuilder:
        ...
    def FlangeTask(self, flangeTask: Features.Feature) -> Die.FlangeTaskBuilder:
        ...
    def TrimTask(self, trimTask: Features.Feature) -> Die.TrimTaskBuilder:
        ...
    def PierceTask(self, pierceTask: Features.Feature) -> Die.PierceTaskBuilder:
        ...
    def CreateAddendumSectionUserDefinedBuilder(self) -> Die.AddendumSectionUserDefinedBuilder:
        ...
    def CreateAddendumSectionBuilder(self, addSection: Features.Feature) -> Die.AddendumSectionBuilder:
        ...
    def Fill(self, fill: Features.Feature) -> Die.FillBuilder:
        ...
    def Lineup(self, lineup: Features.Feature) -> Die.LineupBuilder:
        ...
    def OutputCurves(self, outcurves: Features.Feature) -> Die.OutputCurvesBuilder:
        ...
    def Steelinsert(self, steelInsert: Features.Feature) -> Die.SteelInsertBuilder:
        ...
    def CreateQuickBinderBuilder(self, quickBinder: Features.QuickBinder) -> Die.QuickBinderBuilder:
        ...
    def CreateQuickBinderWrapBuilder(self, quickBinderWrap: Features.Feature) -> Die.QuickBinderWrapBuilder:
        ...
    def CreateTrimLineDevelopmentBuilder(self, trimLineDevelopment: Features.Feature) -> Die.TrimLineDevelopmentBuilder:
        ...
    def CreateAddSurfBuilder(self, addSurf: Features.Feature) -> Die.AddSurfBuilder:
        ...
    def FaceSheet(self, faceSheet: Features.Feature) -> Die.FaceSheetBuilder:
        ...
    def TrimFlangeDieAssistant(self, nullFeature: Features.Feature) -> Die.TrimFlangeDieAssistantBuilder:
        ...
    def DieShoe(self, dieShoe: Die.DieShoe) -> Die.DieShoeBuilder:
        ...
    def CreateDieAttribute(self) -> Die.DieAttributesBuilder:
        ...
    def CreateDieBoolean(self) -> Die.DieBooleanBuilder:
        ...
    def CreateDieDirection(self, feature: Features.Feature) -> Die.DieDirectionBuilder:
        ...
    def CreateDiePlane(self, feature: Features.Feature) -> Die.DiePlaneBuilder:
        ...
    def ClampingSlot(self, clampingSlot: Die.ClampingSlot) -> Die.ClampingSlotBuilder:
        ...
    def CompensateRoughData(self, compensateRoughData: Features.CompensateRoughData) -> Die.CompensateRoughDataBuilder:
        ...
    def Keyway(self, keyway: Die.Keyway) -> Die.KeywayBuilder:
        ...
    def Heelpost(self, heelpost: Die.Heelpost) -> Die.HeelpostBuilder:
        ...
    def CastRelief(self, castRelief: Die.CastRelief) -> Die.CastReliefBuilder:
        ...
    def CreateUncutRegionsBuilder(self) -> Die.UncutRegionsBuilder:
        ...
    def CreateDieLocation(self) -> Die.DieLocationBuilder:
        ...
    def CreateDieLimits(self) -> Die.DieLimitsBuilder:
        ...
    def CreateDieLocations(self, feature: Features.Feature, allowSelection: bool, allowNewPoint: bool, allowNewCoordinateSystem: bool, allowNewVector: bool, allowNewPlane: bool, isRequired: bool, allowMultipleSelection: bool) -> Die.DieLocationsBuilder:
        ...
    def CreateFillAreaBuilder(self, fillArea: Die.FillArea) -> Die.FillAreaBuilder:
        ...
    def CreateFingerClearanceNotchBuilder(self, fingerClearanceNotch: Die.FingerClearanceNotch) -> Die.FingerClearanceNotchBuilder:
        ...
    def CreateClearanceBuilder(self, clearance: Die.Clearance) -> Die.ClearanceBuilder:
        ...
    def CreateHandlingCoreBuilder(self, handlingCore: Die.HandlingCore) -> Die.HandlingCoreBuilder:
        ...
    def CreateMachineReliefBuilder(self, machineRelief: Die.MachineRelief) -> Die.MachineReliefBuilder:
        ...
    def CreateDrawBeadBuilder(self, drawBead: Die.DrawBead) -> Die.DrawBeadBuilder:
        ...
    def CreateSpringbackCompensationBuilder(self, springbackCompensation: Die.SpringbackCompensation) -> Die.SpringbackCompensationBuilder:
        ...
    def Tag(self) -> Tag: ...



class DieBuildStatusOption(enum.Enum):
    Indeterminant = 0
    Unknown = 1
    Fail = 2
    Valid = 3


class DieBooleanBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Die.DieBooleanBuilder]) -> None:
        ...
    def Append(self, object: Die.DieBooleanBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Die.DieBooleanBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Die.DieBooleanBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Die.DieBooleanBuilder) -> None:
        ...
    def Erase(self, obj: Die.DieBooleanBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Die.DieBooleanBuilder]:
        ...
    def SetContents(self, objects: typing.List[Die.DieBooleanBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Die.DieBooleanBuilder, object2: Die.DieBooleanBuilder) -> None:
        ...
    def Insert(self, location: int, object: Die.DieBooleanBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DieBooleanBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BooleanOptions: Die.DieBooleanBuilder.BooleanType
    SelectBodies: SelectNXObjectList


    class BooleanType(enum.Enum):
        Unite = 0
        Subtract = 1
        Intersect = 2
    

class DieAttributesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AttributeColor: NXColor
    AttributeTitle: str
    AttributeValue: str


class DieAssistantTrimProfileList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Die.DieAssistantTrimProfile]) -> None:
        ...
    def Append(self, object: Die.DieAssistantTrimProfile) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Die.DieAssistantTrimProfile) -> int:
        ...
    def FindItem(self, index: int) -> Die.DieAssistantTrimProfile:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Die.DieAssistantTrimProfile) -> None:
        ...
    def Erase(self, obj: Die.DieAssistantTrimProfile, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Die.DieAssistantTrimProfile]:
        ...
    def SetContents(self, objects: typing.List[Die.DieAssistantTrimProfile]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Die.DieAssistantTrimProfile, object2: Die.DieAssistantTrimProfile) -> None:
        ...
    def Insert(self, location: int, object: Die.DieAssistantTrimProfile) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DieAssistantTrimProfile(NXObject):
    def __init__(self) -> None: ...
    def DefineBases(self) -> None:
        ...
    TrimDirection: Direction
    TrimProfile: ScCollector
    TrimProfileDirection: Die.DirectionOption
    TrimSide: bool


class DieAssistantFlangeProfileType(enum.Enum):
    Wipe = 0
    FormAndRestrike = 1


class DieAssistantFlangeProfileList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Die.DieAssistantFlangeProfile]) -> None:
        ...
    def Append(self, object: Die.DieAssistantFlangeProfile) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Die.DieAssistantFlangeProfile) -> int:
        ...
    def FindItem(self, index: int) -> Die.DieAssistantFlangeProfile:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Die.DieAssistantFlangeProfile) -> None:
        ...
    def Erase(self, obj: Die.DieAssistantFlangeProfile, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Die.DieAssistantFlangeProfile]:
        ...
    def SetContents(self, objects: typing.List[Die.DieAssistantFlangeProfile]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Die.DieAssistantFlangeProfile, object2: Die.DieAssistantFlangeProfile) -> None:
        ...
    def Insert(self, location: int, object: Die.DieAssistantFlangeProfile) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DieAssistantFlangeProfile(NXObject):
    def __init__(self) -> None: ...
    def DefineBases(self) -> None:
        ...
    FlangeDirection: Direction
    FlangeEndProfile: ScCollector
    FlangeProfile: ScCollector
    FlangeProfileDirection: Die.DirectionOption
    FlangeSide: bool
    FlangeType: Die.DieAssistantFlangeProfileType


class DeckParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetMainDeck(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetMainDeck(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetBinderEdge(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetBinderEdge(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetMainWallCenterline(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetMainWallCenterline(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetBaseFlange(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetBaseFlange(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    def SetIntermediateDeck(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetIntermediateDeck(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    BuildStatus: Die.DieBuildStatusOption
    DesignStatus: bool
    DisplayStatus: bool
    InnerDeckSheet: Body
    IntermediateDeckOrientation: ISurface


class ConnectProfileParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetProfile(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetProfile(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    BuildStatus: Die.DieBuildStatusOption
    DesignStatus: bool
    DisplayStatus: bool


class CompensateRoughDataBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    Approximation: Die.CompensateRoughDataBuilder.ApproximationType
    CurveCollector: Section
    DistanceTolerance: float
    JoinOutputCurves: bool
    MaximumGap: float
    ModifyInputSheet: bool
    ProjectToFaces: ScCollector
    SheetBodies: SelectBodyList
    Type: Die.CompensateRoughDataBuilder.Types


    class Types(enum.Enum):
        SheetBody = 0
        Curve = 1
    

    class ApproximationType(enum.Enum):
        Coarse = 0
        Rough = 1
        Fine = 2
        Exact = 3
    

class ClearanceBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    Attributes: Die.DieAttributesBuilder
    ClearanceDirection: Die.DieDirectionBuilder
    ClearanceGeometryType: Die.ClearanceBuilder.ClearanceGeometryTypes
    Distance: Expression
    DistanceTolerance: float
    Geometry: SelectBodyList
    Offset: Expression
    Orientation: Die.DiePlaneBuilder
    Section: Section
    Target: SelectBody
    Type: Die.ClearanceBuilder.Types


    class Types(enum.Enum):
        Gage = 0
        Gripper = 1
        Lifter = 2
    

    class ClearanceGeometryTypes(enum.Enum):
        Solid = 0
        Section = 1
    

class Clearance(Features.BodyFeature):
    def __init__(self) -> None: ...


class ClampingSlotBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    BasePlane: Die.DiePlaneBuilder
    CenterlineLength: Expression
    DieCenterlineCoordinateSystem: SelectCartesianCoordinateSystem
    DistanceTolerance: float
    FlangeBaseProfile: Section
    FlangeThickness: Expression
    InnerWidth: Expression
    LocationOffset: Expression
    LocationOffsetDirection: Die.DieDirectionBuilder
    LocationOnFlange: bool
    Locations: Die.DieLocationsBuilder
    NotchAngle: Expression
    NotchFacesAttributes: Die.DieAttributesBuilder
    NotchHeight: Expression
    NotchWidth: Expression
    OffsetWidth: Expression
    OrientationPlane: Die.DiePlaneBuilder
    Overhang: Expression
    OverhangFacesAttributes: Die.DieAttributesBuilder
    PadFacesAttributes: Die.DieAttributesBuilder
    PadHeight: Expression
    PadLength: Expression
    PadOffset: Expression
    PadRadius: Expression
    PadWidth: Expression
    SlotEndFacesAttributes: Die.DieAttributesBuilder
    SlotFacesAttributes: Die.DieAttributesBuilder
    SlotLength: Expression
    SlotRadius: Expression
    SlotWidth: Expression
    Target: SelectNXObject
    TopLength: Expression
    Type: Die.ClampingSlotBuilder.Types


    class Types(enum.Enum):
        Hydraulic = 0
        Traveling = 1
        Automatic = 2
    

class ClampingSlot(Features.BodyFeature):
    def __init__(self) -> None: ...


class CastReliefParentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetCastRelief(self, direction: Die.DirectionOption, profileEntries: typing.List[IProfile]) -> None:
        ...
    def GetCastRelief(self, direction: Die.DirectionOption) -> typing.List[IProfile]:
        ...
    BuildStatus: Die.DieBuildStatusOption
    DesignStatus: bool
    DisplayStatus: bool
    ReliefDepth: float
    ReliefSheet: Body


class CastReliefBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    BaseOrientation: Die.DiePlaneBuilder
    CreateSupportCasting: bool
    DistanceTolerance: float
    ReliefDepth: Expression
    ReliefProfile: Section
    ReliefSheet: SelectNXObject
    SheetMetal: SelectNXObject
    Target: SelectNXObject
    Thickness: Expression


class CastRelief(Features.BodyFeature):
    def __init__(self) -> None: ...


class AddSurfBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateDefaultSpine(self) -> None:
        ...
    Associative: bool
    ConcaveCornerRadius: Expression
    DistanceTolerance: float
    Limits: Die.DieLimitsBuilder
    Method: Die.AddSurfBuilder.Methods
    RefPoint: Point
    SelectSection: SelectNXObjectList
    Sewn: bool
    Spine: ScCollector
    SpineRadius: float
    TrimBound: ScCollector


    class Methods(enum.Enum):
        Sectional = 0
        CurveMesh = 1
        ChannelTunnelCap = 2
        MultiFaceBlend = 3
        WallsOnly = 4
        DiskFaceBlend = 5
        SphereFaceBlend = 6
    

class AddendumSectionUserDefinedBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateUserDefinedSection(self) -> Curve:
        ...
    ReverseAnchorPoint: bool
    Section: Section


class AddendumSectionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CutSection(self, section: Curve, copyPlaneData: bool) -> None:
        ...
    def TrimExtendConstraintCurve(self, constraintCurve: Section) -> None:
        ...
    def DeleteExtendSection(self) -> Section:
        ...
    def CopySection(self, section: Curve, copyPlaneData: bool) -> None:
        ...
    def InitializeEditParameters(self, section: Curve) -> None:
        ...
    def UpdateSegment(self, temporary: bool, section: Curve, segment: Die.AddendumSectionBuilder.SegmentType, lengthRadius: float, angle: float) -> float:
        ...
    def LockSegment(self, section: Curve, segment: Die.AddendumSectionBuilder.SegmentType, type: Die.AddendumSectionBuilder.SegmentParameterType) -> None:
        ...
    def UnlockSegment(self, section: Curve, segment: Die.AddendumSectionBuilder.SegmentType, type: Die.AddendumSectionBuilder.SegmentParameterType) -> None:
        ...
    def ResetSection(self, section: Curve) -> None:
        ...
    def EditBlendSection(self, section: Curve, radius: float) -> None:
        ...
    def ReplaceSectionCurve(self, section: Curve) -> None:
        ...
    def TerminateEditParameters(self, section: Curve) -> None:
        ...
    def UpdateSection(self, section: Curve) -> None:
        ...
    def CreateExtendSection(self) -> Section:
        ...
    def ReplaceConstraintCurve(self, editedCurve: Curve) -> None:
        ...
    def MoveSectionOrigin(self, section: Curve, newOrigin: Point3d, useSectionPlane: int) -> None:
        ...
    def ChangeSectionPlane(self, section: Curve, plane: Direction) -> None:
        ...
    def UpdateSectionAttributes(self, section: Curve) -> None:
        ...
    def PasteSectionFromCurve(self, curve: Curve) -> None:
        ...
    def CreateSectionFromReuse(self, fileName: str) -> None:
        ...
    def UpdateSectionsAfterConstraintChange(self) -> None:
        ...
    def MirrorSections(self) -> None:
        ...
    def DeleteSections(self) -> None:
        ...
    def CreateSection(self) -> None:
        ...
    def RecreateSections(self) -> None:
        ...
    def PasteSection(self) -> None:
        ...
    def Reinitialize(self) -> None:
        ...
    def DefaultDraw(self) -> None:
        ...
    def TranslateWall(self) -> None:
        ...
    def SmoothCurve(self) -> None:
        ...
    AngleTolerance: float
    Attributes: Die.DieAttributesBuilder
    ByCurves: Section
    ConstraintCurve: ScCollector
    ConstraintCurveToEdit: Curve
    ConstraintFaces: ScCollector
    CurveToExtend: Curve
    DistanceTolerance: float
    DrawDirection: Direction
    EditedConstraintCurve: Curve
    ExtendData: GeometricUtilities.CurveLengthData
    ExtendEndDistance: Expression
    ExtendStartDistance: Expression
    FacetDensity: float
    Limits: Die.DieLimitsBuilder
    LocationType: Die.AddendumSectionBuilder.SectionLocationType
    MaximumPositive: Expression
    MinimumDraftAngle: Expression
    MinimumNegative: Expression
    MinimumRadius: Expression
    MinimumTrimLedge: Expression
    MirrorPlane: Plane
    NeutralCurve: Section
    PlusLength: Expression
    Product: ScCollector
    SectionOrientation: Die.AddendumSectionBuilder.SectionOrientationType
    SectionPlane: Plane
    SectionPoint: Point
    SectionShape: Die.AddendumSectionBuilder.SectionShapeType
    Sections: SelectDisplayableObjectList
    SmoothRadius: Expression
    SurfaceBuildMethod: Die.AddendumSectionBuilder.SurfaceBuildType
    TranslateDistance: Expression


    class SurfaceBuildType(enum.Enum):
        NoSurface = 0
        Sectional = 1
        CurveMesh = 2
        ChannelTunnelCap = 3
        MultipleFaceBlend = 4
        WallsOnly = 5
        DiskFaceBlend = 6
        SphereFaceBlend = 7
    

    class SegmentType(enum.Enum):
        Plus = 0
        Punch = 1
        FirstStretchWall = 2
        Reverse = 3
        TrimLedge = 4
        DiePunch = 5
        SecondStretchWall = 6
        DieReverse = 7
        FlatToBead = 8
    

    class SegmentParameterType(enum.Enum):
        Length = 0
        Angle = 1
        Radius = 2
        ArcLength = 3
    

    class SectionShapeType(enum.Enum):
        Basic = 0
        DrawBar = 1
        Simple = 2
        Channel = 3
        Blend = 4
        Extension = 5
        System = 6
        UserDefined = 7
        Reuse = 8
        Blank = 9
    

    class SectionOrientationType(enum.Enum):
        Default = 0
        ThreeDPerpendicular = 1
        Conjugate = 2
        Isoparametric = 3
        IncidentEdge = 4
        Blank = 5
    

    class SectionLocationType(enum.Enum):
        AtPoint = 0
        AtPlane = 1
        WithCurve = 2
    

