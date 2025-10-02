from . import SectionAnalysis
from ...NXOpen import *
from ..GeometricAnalysis import *

import typing
import enum

class SurfaceIntersectionBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateWorkView(self) -> None:
        ...
    CalculationMethod: GeometricAnalysis.SurfaceIntersectionBuilder.CalculationTypes
    CombOptions: GeometricUtilities.CombOptionsBuilder
    DynamicProjection: bool
    FirstFaceSet: ScCollector
    NeedleDirection: GeometricAnalysis.SurfaceIntersectionBuilder.DirectionTypes
    ProjectionNormalFace: GeometricAnalysis.SurfaceIntersectionBuilder.NormalTypes
    ProjectionOption: GeometricAnalysis.SurfaceIntersectionBuilder.ProjectionTypes
    ProjectionXYZ: GeometricAnalysis.SurfaceIntersectionBuilder.XyzTypes
    ScalingMethod: GeometricAnalysis.SurfaceIntersectionBuilder.ScalingTypes
    SecondFaceSet: ScCollector
    Vector: Direction


    class XyzTypes(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class ScalingTypes(enum.Enum):
        Linear = 0
        Logarithmic = 1
    

    class ProjectionTypes(enum.Enum):
        None = 0
        Normal = 1
        Vector = 2
        View = 3
        Xyz = 4
    

    class NormalTypes(enum.Enum):
        FaceSet1 = 0
        FaceSet2 = 1
    

    class LabelValues(enum.Enum):
        Curvature = 0
        RadiusOfCurvature = 1
    

    class DirectionTypes(enum.Enum):
        Inside = 0
        Outside = 1
    

    class CalculationTypes(enum.Enum):
        Curvature = 0
        RadiusofCurvature = 1
    

class SurfaceIntersection(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class SurfaceContinuityAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateFirstEdgeFace(self, edgeOrFace: DisplayableObject, selectionPoint: Point3d) -> None:
        ...
    def UpdateSecondEdgeFace(self, edgeOrFace: DisplayableObject, selectionPoint: Point3d) -> None:
        ...
    def UpdateFace(self, face: Face, selectionPoint: Point3d) -> None:
        ...
    def GetFace1Array(self) -> typing.List[Face]:
        ...
    def DeselectFirstEdgeFace(self, edge: DisplayableObject, face: DisplayableObject) -> None:
        ...
    def SelectFirstEdgeFace(self, edge: DisplayableObject, face: DisplayableObject) -> None:
        ...
    def DeselectSecondEdgeFace(self, edge: DisplayableObject, face: DisplayableObject) -> None:
        ...
    def SelectSecondEdgeFace(self, edge: DisplayableObject, face: DisplayableObject) -> None:
        ...
    AngularThreshold: Expression
    CombOptions: GeometricUtilities.CombOptionsBuilder
    CurvatureCheck: GeometricAnalysis.SurfaceContinuityAnalysisBuilder.CurvatureType
    DistanceThreshold: Expression
    DynamicLabel: Features.GeometricConstraintDataManager
    Face: SelectNXObjectList
    FirstEdge: SelectNXObjectList
    G0: bool
    G0Tolerance: float
    G1: bool
    G1Tolerance: float
    G2: bool
    G2Tolerance: float
    G3: bool
    G3Tolerance: float
    MultiFace: SelectNXObjectList
    ReportPer: int
    SecondEdge: SelectNXObjectList
    ShowOutOfTolerance: bool
    ToleranceMarkup: bool
    Type: GeometricAnalysis.SurfaceContinuityAnalysisBuilder.Types


    class Types(enum.Enum):
        EdgeToEdge = 0
        EdgeToFace = 1
        MultiFace = 2
    

    class ReportingType(enum.Enum):
        Analysis = 0
        Pair = 1
    

    class CurvatureType(enum.Enum):
        Sectional = 0
        Gaussian = 1
        Mean = 2
        Absolute = 3
    

class SurfaceContinuityAnalysis(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class SurfaceAnalysisDisplay(Utilities.NXRemotableObject):
    def __init__(self, owner: GeometricAnalysis.AnalysisObjectCollection) -> None: ...
    def SetShowFlag(self, surface: DisplayableObject, choice: GeometricAnalysis.SurfaceAnalysisDisplay.ShowFlagType, on: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



    class ShowFlagType(enum.Enum):
        Pole = 0
        Knot = 1
    

class SolidDensity(Builder):
    def __init__(self) -> None: ...
    Density: float
    Solids: SelectObjectList
    Units: GeometricAnalysis.SolidDensity.UnitsType


    class UnitsType(enum.Enum):
        PoundsPerCubicInches = 0
        PoundsPerCubicFeet = 1
        GramsPerCubicCentimeters = 2
        KilogramsPerCubicMeters = 3
    

class SlopeAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def CreatePMILabel(self, location: Point3d, face: DisplayableObject) -> None:
        ...
    def StartSlopeAnalysis(self) -> None:
        ...
    DataRange: GeometricAnalysis.FaceAnalysisDataRangeBuilder
    DisplayMode: GeometricAnalysis.SlopeAnalysisBuilder.DisplayModes
    DisplaySettings: GeometricAnalysis.FaceAnalysisDisplayBuilder
    Faces: SelectDisplayableObjectList
    Normals: GeometricAnalysis.FaceAnalysisNormalsBuilder
    NumberOfContourLines: int
    PmiPoint: SelectNXObjectList
    SpikeLength: float
    Vector: Direction


    class DisplayModes(enum.Enum):
        Fringe = 0
        Hedgehog = 1
        ContourLines = 2
    

class SimpleInterference(Builder):
    def __init__(self) -> None: ...
    def PerformCheck(self) -> GeometricAnalysis.SimpleInterference.Result:
        ...
    def HighlightNextPair(self) -> bool:
        ...
    def GetInterferenceResults(self) -> typing.List[NXObject]:
        ...
    def Reset(self) -> None:
        ...
    FaceInterferenceType: GeometricAnalysis.SimpleInterference.FaceInterferenceMethod
    FirstBody: SelectObject
    InterferenceType: GeometricAnalysis.SimpleInterference.InterferenceMethod
    SecondBody: SelectObject


    class Result(enum.Enum):
        NoInterference = 0
        OnlyEdgesOrFacesInterfere = 1
        InterferenceExists = 2
        CanNotPerformCheck = 3
    

    class InterferenceMethod(enum.Enum):
        InterferingFaces = 0
        InterferenceSolid = 1
    

    class FaceInterferenceMethod(enum.Enum):
        FirstPairOnly = 0
        AllPairs = 1
    

class SheetBoundaryAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    Bodies: ScCollector
    EmphasisColor: NXColor


class SheetBoundaryAnalysis(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class SectionAnalysisObject(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class ReflectionAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def StartReflectionAnalysis(self) -> None:
        ...
    DisplayResolution: GeometricUtilities.DisplayResolutionBuilder
    FaceReflectivityScale: int
    Faces: SelectDisplayableObjectList
    FileName: str
    ImageMovementType: GeometricAnalysis.ReflectionAnalysisBuilder.ImageMovementTypes
    ImagePosition: int
    ImageSizeSetting: GeometricAnalysis.ReflectionAnalysisBuilder.ImageSizeOption
    LineImageType: GeometricAnalysis.ReflectionAnalysisBuilder.LineImageTypes
    LineNumber: GeometricAnalysis.ReflectionAnalysisBuilder.NumberOfLinesOptions
    LineOrientation: GeometricAnalysis.ReflectionAnalysisBuilder.LineOrientationType
    LineThickness: GeometricAnalysis.ReflectionAnalysisBuilder.LineThicknessType
    Normals: GeometricAnalysis.FaceAnalysisNormalsBuilder
    SceneImageOption: GeometricAnalysis.ReflectionAnalysisBuilder.SceneImageType
    ShowFacetEdge: bool
    Type: GeometricAnalysis.ReflectionAnalysisBuilder.Types


    class Types(enum.Enum):
        LineImages = 0
        SceneImages = 1
        ImageFromFile = 2
    

    class SceneImageType(enum.Enum):
        SimulatedHorizon = 0
        PhotoHorizon = 1
        SphericalRoom = 2
        SphericalLightTubesRoom = 3
        DaytimeHorizon = 4
        MagentaSunset = 5
        SphericalHorizon = 6
        CylindricalRoom = 7
        MonochromeHorizon = 8
        SmoothGrayScale = 9
        SharpGrayScale = 10
        SphericalTubes = 11
    

    class NumberOfLinesOptions(enum.Enum):
        One = 0
        Two = 1
        Four = 2
        Eight = 3
        Sixteen = 4
        ThirtyTwo = 5
        SixtyFour = 6
        OneTwoEight = 7
        TwoFiveSix = 8
    

    class LineThicknessType(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
    

    class LineOrientationType(enum.Enum):
        Horizontal = 0
        Vertical = 1
        Both = 2
    

    class LineImageTypes(enum.Enum):
        BlackLines = 0
        BlackandWhiteLines = 1
        ColoredLines = 2
    

    class ImageSizeOption(enum.Enum):
        KeepCurrent = 0
        ReduceScale = 1
    

    class ImageMovementTypes(enum.Enum):
        Horizontal = 0
        Vertical = 1
        Rotate = 2
    

class RadiusAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateDisplayOnPlaneChange(self) -> None:
        ...
    def StartRadiusAnalysis(self) -> None:
        ...
    DataRange: GeometricAnalysis.FaceAnalysisDataRangeBuilder
    DisplayMode: GeometricAnalysis.RadiusAnalysisBuilder.DisplayModes
    DisplaySettings: GeometricAnalysis.FaceAnalysisDisplayBuilder
    Faces: SelectDisplayableObjectList
    Normals: GeometricAnalysis.FaceAnalysisNormalsBuilder
    NumberOfContourLines: int
    Plane: Plane
    SpikeLength: float
    Type: GeometricAnalysis.RadiusAnalysisBuilder.Types
    Vector: Direction


    class Types(enum.Enum):
        Gaussian = 0
        Minimum = 1
        Maximum = 2
        Mean = 3
        Normal = 4
        Sectional = 5
        U = 6
        V = 7
    

    class DisplayModes(enum.Enum):
        Fringe = 0
        Hedgehog = 1
        ContourLines = 2
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class LocalRadiusAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def ButtonOpenInformationWindow(self) -> None:
        ...
    SelectionPoint: Features.GeometricConstraintDataManager
    VisibilityCoordinates: bool
    VisibilityMaxRadius: bool
    VisibilityMinMaxRadiusTangent: bool
    VisibilityMinRadius: bool
    VisibilityRadius: bool
    VisibilityURadius: bool
    VisibilityUV: bool
    VisibilityUVTangent: bool
    VisibilityVRadius: bool


class LocalRadiusAnalysis(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class HighlightLinesAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDarkColor(self) -> float:
        ...
    def SetDarkColor(self, darkColor: float) -> None:
        ...
    def GetBrightColor(self) -> float:
        ...
    def SetBrightColor(self, brightColor: float) -> None:
        ...
    def ReinitializePlane(self) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  This call currently does not do anything.  Calls to this method can be safely removed.")"""
        ...
    def SetLightPlaneOrigin(self, origin: Point3d) -> None:
        ...
    def SetLightPlaneXAxis(self, xAxis: Vector3d) -> None:
        ...
    def SetLightPlaneYAxis(self, yAxis: Vector3d) -> None:
        ...
    BetweenPoints: SelectPointList
    DisplayMethod: GeometricAnalysis.HighlightLinesAnalysisBuilder.DisplayMethods
    EndIsoAngle: Expression
    Faces: SelectDisplayableObjectList
    IsReflectionLocked: bool
    IsoclineVector: Direction
    LightDiffuseness: float
    LightNumber: int
    LightPlacement: GeometricAnalysis.HighlightLinesAnalysisBuilder.LightPlacements
    LightPlaneOrigin: Point3d
    LightPlaneXAxis: Vector3d
    LightPlaneYAxis: Vector3d
    LightSpacing: float
    LightWidth: float
    Resolution: GeometricAnalysis.HighlightLinesAnalysisBuilder.Resolutions
    StartIsoAngle: Expression
    ThroughPoints: SelectPointList
    Type: GeometricAnalysis.HighlightLinesAnalysisBuilder.Types
    Type2: GeometricAnalysis.HighlightLinesAnalysisBuilder.Types2


    class Types2(enum.Enum):
        Reflection = 0
        Projection = 1
        Isoclines = 2
        Zebra = 3
    

    class Types(enum.Enum):
        Uniform = 0
        ThroughPoints = 1
        BetweenPoints = 2
    

    class Resolutions(enum.Enum):
        Coarse = 0
        Standard = 1
        Fine = 2
        ExtraFine = 3
        SuperFine = 4
        UltraFine = 5
    

    class LightPlaneOptions(enum.Enum):
        YZ = 0
        ZX = 1
        XY = 2
        Arbitrary = 3
    

    class LightPlacements(enum.Enum):
        Uniform = 0
        ThroughPoints = 1
        BetweenPoints = 2
    

    class DisplayMethods(enum.Enum):
        Reflection = 0
        Projection = 1
    

class HighlightLinesAnalysis(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class GeometricProperties(Builder):
    def __init__(self) -> None: ...
    def GetFaceProperties(self, entityTag: NXObject, absPoint: Point3d, face: GeometricAnalysis.GeometricProperties.Face) -> GeometricAnalysis.GeometricProperties.Status:
        ...
    def GetEdgeProperties(self, entityTag: NXObject, absPoint: Point3d, edge: GeometricAnalysis.GeometricProperties.Edge) -> GeometricAnalysis.GeometricProperties.Status:
        ...
    def GetCaeFaceProperties(self, entityTag: NXObject, absPoint: Point3d, caeFace: GeometricAnalysis.GeometricProperties.CaeFace) -> GeometricAnalysis.GeometricProperties.Status:
        ...
    def GetCaeCurveProperties(self, entityTag: NXObject, absPoint: Point3d, caeCurve: GeometricAnalysis.GeometricProperties.CaeCurve) -> GeometricAnalysis.GeometricProperties.Status:
        ...
    def ListProperties(self, entityTag: NXObject, absPoint: Point3d) -> GeometricAnalysis.GeometricProperties.Status:
        ...
    def ListProperties(self, absPoint: Point3d) -> GeometricAnalysis.GeometricProperties.Status:
        ...
    def Reset(self) -> None:
        ...
    ObjectsForAnalysis: SelectObjectList
    OutputMethod: GeometricAnalysis.GeometricProperties.OutputType


    class Status(enum.Enum):
        Success = 0
        InvalidInput = 1
        Failed = 2
    

    class OutputType(enum.Enum):
        Dynamic = 0
        Static = 1
    

    class GeometricPropertiesFace():
        UParamater: float
        VParamater: float
        PositionInWcs: Point3d
        UDerivativeInWcs: Vector3d
        VDerivativeInWcs: Vector3d
        NormalInWcs: Vector3d
        Position: Point3d
        UDerivative: Vector3d
        VDerivative: Vector3d
        Normal: Vector3d
        InvOfMinRadiusOfCurvature: float
        InvOfMaxRadiusOfCurvature: float
        def ToString(self) -> str:
            ...
    

    class Entity(enum.Enum):
        Face = 0
        Edge = 1
        CaeFace = 2
        CaeCurve = 3
    

    class GeometricPropertiesEdge():
        ParameterPercentage: float
        Parameter: float
        PositionInWcs: Point3d
        Position: Point3d
        TangentInWcs: Vector3d
        Tangent: Vector3d
        NormalInWcs: Vector3d
        Normal: Vector3d
        BinormalInWcs: Vector3d
        Binormal: Vector3d
        Torsion: float
        Curvature: float
        def ToString(self) -> str:
            ...
    

    class GeometricPropertiesCaeFace():
        ClosestPoint: Vector3d
        UParameter: float
        VParameter: float
        Normal: Vector3d
        ClosestPointInWcs: Point3d
        NormalInWcs: Vector3d
        UDerivative: Vector3d
        VDerivative: Vector3d
        UDerivativeInWcs: Vector3d
        VDerivativeInWcs: Vector3d
        def ToString(self) -> str:
            ...
    

    class GeometricPropertiesCaeCurve():
        ArcLengthParameter: float
        UnitArcLengthParameter: float
        ClosestPointInWcs: Point3d
        NormalInWcs: Vector3d
        TangentInWcs: Vector3d
        Tangent: Vector3d
        Normal: Vector3d
        ClosestPoint: Point3d
        def ToString(self) -> str:
            ...
    

class GapFlushnessBuilder(Builder):
    def __init__(self) -> None: ...
    BasePanelFaces: ScCollector
    BasePanelInnerContactCurves: Section
    BasePanelOuterContactCurves: Section
    BasePanelType: GeometricAnalysis.GapFlushnessBuilder.PanelTypes
    CrossSectionCurveOption: GeometricAnalysis.GapFlushnessBuilder.SectionCurveOptions
    CrossSectionCurves: Section
    EvaluationMode: GeometricAnalysis.GapFlushnessBuilder.EvaluationModes
    EvaluationPoint: Point
    EvaluationType: GeometricAnalysis.GapFlushnessBuilder.EvaluationTypes
    IsNegativeToleranceLabelDisplayed: bool
    IsNominalLabelDisplayed: bool
    IsPositiveToleranceLabelDisplayed: bool
    LabelDisplayOption: GeometricAnalysis.GapFlushnessBuilder.DisplayOptions
    NegativeFlushnessTolerance: float
    NegativeGapTolerance: float
    NominalFlushness: float
    NominalGap: float
    PositiveFlushnessTolerance: float
    PositiveGapTolerance: float
    PreviewOption: bool
    SampleDistance: Expression
    SampleNumber: int
    SecondPanelFaces: ScCollector
    SecondPanelInnerContactCurves: Section
    SecondPanelOuterContactCurves: Section
    SecondPanelType: GeometricAnalysis.GapFlushnessBuilder.PanelTypes
    SectionAlignment: GeometricAnalysis.GapFlushnessBuilder.SectionAlignments
    SectionAlignmentDirection: Direction
    ShowOutRangeLabels: bool


    class SectionCurveOptions(enum.Enum):
        ContactCurve = 0
        UserDefined = 1
    

    class SectionAlignments(enum.Enum):
        Curve = 0
        CurveView = 1
        SpecifiedDirection = 2
    

    class PanelTypes(enum.Enum):
        Hem = 0
        Flange = 1
        Wall = 2
    

    class EvaluationTypes(enum.Enum):
        Absolute = 0
        Visual = 1
    

    class EvaluationModes(enum.Enum):
        Point = 0
        CurveNumber = 1
        Curve = 2
    

    class DisplayOptions(enum.Enum):
        GapOnly = 0
        FlushnessOnly = 1
        Both = 2
    

class GapFlushness(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class FaceCurvatureAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def ReverseAllNormals(self) -> None:
        ...
    def ReverseIndividualNormal(self, face: DisplayableObject) -> None:
        ...
    def UpdateReverseMap(self) -> None:
        ...
    def DeselectFaces(self, faces: typing.List[DisplayableObject]) -> None:
        ...
    ContourRefinement: int
    ContourShift: float
    CurvatureSectionPlane: Plane
    CurvatureType: GeometricAnalysis.FaceCurvatureAnalysisBuilder.CurvatureTypes
    DisplayType: GeometricAnalysis.FaceCurvatureAnalysisBuilder.DisplayTypes
    MapCenter: float
    MapRange: float
    NormalOption: GeometricAnalysis.FaceCurvatureAnalysisBuilder.DirectionTypes
    NormalOrientation: Matrix3x3
    NormalOrigin: Point3d
    NormalVector: Direction
    NumberOfContours: int
    Resolution: GeometricUtilities.DisplayResolutionBuilder
    ReverseIndividual: SelectDisplayableObject
    ScaleType: GeometricAnalysis.FaceCurvatureAnalysisBuilder.ScaleTypes
    SectionOption: GeometricAnalysis.FaceCurvatureAnalysisBuilder.DirectionTypes
    SectionOrientation: Matrix3x3
    SectionOrigin: Point3d
    SelectObject: SelectDisplayableObjectList
    ShowZeroContour: bool


    class ScaleTypes(enum.Enum):
        Linear = 0
        Log = 1
        Area = 2
    

    class DisplayTypes(enum.Enum):
        Colormap = 0
        Contours = 1
        ColormapAndContours = 2
    

    class DirectionTypes(enum.Enum):
        Primitive = 0
        Manipulator = 1
    

    class CurvatureTypes(enum.Enum):
        Gaussian = 0
        Absolute = 1
        Minimum = 2
        Maximum = 3
        Mean = 4
        Normal = 5
        Sectional = 6
        U = 7
        V = 8
        Radius = 9
    

class FaceCurvatureAnalysis(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class FaceAnalysisNormalsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def RestoreAll(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    FaceToReverseNormal: SelectNXObject
    Point: Point


class FaceAnalysisDisplayBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CanShowFacet: bool
    ColorLegendOption: GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorLegendOptions
    DisplayResolution: GeometricUtilities.DisplayResolutionBuilder
    NumberOfColors: GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorsOptions


    class ColorsOptions(enum.Enum):
        Two = 0
        Three = 1
        Four = 2
        Five = 3
        Six = 4
        Seven = 5
        Eight = 6
        Nine = 7
        Ten = 8
        Eleven = 9
        Twelve = 10
    

    class ColorLegendOptions(enum.Enum):
        Blend = 0
        Sharp = 1
    

class FaceAnalysisDataRangeBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def ResetData(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    IsFixed: bool
    Max: float
    Middle: float
    MiddleScale: float
    Min: float
    ZoomScale: float


class FaceAnalysis(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class ExamineGeometry(Builder):
    def __init__(self) -> None: ...
    def SetAllChecks(self) -> None:
        ...
    def ClearAllChecks(self) -> None:
        ...
    def SetCheck(self, check: GeometricAnalysis.ExamineGeometry.Check) -> None:
        ...
    def ClearCheck(self, check: GeometricAnalysis.ExamineGeometry.Check) -> None:
        ...
    def Examine(self) -> None:
        ...
    def GetResults(self) -> int:
        ...
    def GetFailedObjects(self, check: GeometricAnalysis.ExamineGeometry.Check) -> typing.List[NXObject]:
        ...
    def HighlightResult(self, check: GeometricAnalysis.ExamineGeometry.Check) -> bool:
        ...
    def UnhighlightResult(self, check: GeometricAnalysis.ExamineGeometry.Check) -> None:
        ...
    def UnhighlightAllResults(self) -> None:
        ...
    def DisplayResultsAsInfo(self) -> None:
        ...
    CheckCriteriaAngle: float
    CheckCriteriaDistance: float
    ObjectsToExamine: SelectObjectList


    class Check(enum.Enum):
        ObjectTiny = 0
        ObjectMisaligned = 1
        BodyDataStructures = 2
        BodyConsistency = 3
        BodyFaceIntersections = 4
        BodySheetBoundaries = 5
        FaceSmoothness = 6
        FaceSelfIntersection = 7
        FaceSpikesCuts = 8
        EdgeSmoothness = 9
        EdgeTolerances = 10
        NumChecks = 11
    

class DupinBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def ResetAnalysisPoint(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AnalysisPoint: Point
    Angle: float
    FlatnessTolerance: float
    Scale: float


class DraftAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def ReverseAllNormals(self) -> None:
        ...
    def GetColorOutsidePositive(self) -> float:
        ...
    def SetColorOutsidePositive(self, colorOutsidePos: float) -> None:
        ...
    def GetColorInsidePositive(self) -> float:
        ...
    def SetColorInsidePositive(self, colorInsidePos: float) -> None:
        ...
    def GetColorOutsideNegative(self) -> float:
        ...
    def SetColorOutsideNegative(self, colorOutsideNeg: float) -> None:
        ...
    def GetColorInsideNegative(self) -> float:
        ...
    def SetColorInsideNegative(self, colorInsideNeg: float) -> None:
        ...
    def AddDynamicPoints(self) -> None:
        ...
    def SetTotalDynamicNormals(self, total: int) -> None:
        ...
    def SetDynamicNormal(self, index: int, normal: Vector3d) -> None:
        ...
    def SetDynamicParent(self, index: int, parent: DisplayableObject) -> None:
        ...
    def ReverseNormal(self, face: DisplayableObject) -> None:
        ...
    def DeselectFaces(self, faces: typing.List[DisplayableObject]) -> None:
        ...
    def UpdateReverseMap(self) -> None:
        ...
    def RemoveLabelParents(self, parents: typing.List[DisplayableObject]) -> None:
        ...
    def DeleteDynamicLabels(self, deletedLabels: bool) -> None:
        ...
    CoupleLimit: bool
    CreateCSYS: bool
    DrawOption: GeometricAnalysis.DraftAnalysisBuilder.DrawDirection
    DrawOrientation: Matrix3x3
    DrawOrigin: Point3d
    DrawVector: Direction
    DynamicLabel: Features.GeometricConstraintDataManager
    JoinIsocline: bool
    LimitAngleNegative: float
    LimitAnglePositive: float
    OutputOption: GeometricAnalysis.DraftAnalysisBuilder.SelectOutput
    Resolution: GeometricUtilities.DisplayResolutionBuilder
    ReverseIndividual: SelectDisplayableObject
    SelectObject: SelectDisplayableObjectList
    ShowIsoclineNegative: bool
    ShowIsoclinePositive: bool
    ShowPartingLine: bool
    SwitchDisplayMode: bool
    TranslucencyInsideNegative: int
    TranslucencyInsidePositive: int
    TranslucencyOutsideNegative: int
    TranslucencyOutsidePositive: int


    class SelectOutput(enum.Enum):
        AnalysisObject = 0
        Isoclines = 1
        Both = 2
    

    class DrawDirection(enum.Enum):
        Vector = 0
        Orientation = 1
    

class DraftAnalysis(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class DistanceAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateDisplayOnPlaneChange(self) -> None:
        ...
    def StartDistanceAnalysis(self) -> None:
        ...
    DataRange: GeometricAnalysis.FaceAnalysisDataRangeBuilder
    DisplayMode: GeometricAnalysis.DistanceAnalysisBuilder.DisplayModes
    DisplaySettings: GeometricAnalysis.FaceAnalysisDisplayBuilder
    Faces: SelectDisplayableObjectList
    Normals: GeometricAnalysis.FaceAnalysisNormalsBuilder
    NumberOfContourLines: int
    Plane: Plane
    SpikeLength: float


    class DisplayModes(enum.Enum):
        Fringe = 0
        Hedgehog = 1
        ContourLines = 2
    

class DeviationGaugeBuilder(Builder):
    def __init__(self) -> None: ...
    def AddDynamicPoints(self) -> None:
        ...
    def AddPMILabel(self, snappedObject: NXObject) -> None:
        ...
    ColorPlotType: GeometricAnalysis.DeviationGaugeBuilder.ColorPlotTypes
    ConstraintManager: Features.GeometricConstraintDataManager
    CurveRangeControl: GeometricUtilities.CurveRangeBuilder
    DeviationIntervals: int
    HasAbsoluteColorPlot: bool
    HasAdditionalValuesLabel: GeometricAnalysis.DeviationGaugeBuilder.AdditionalValuesLabelType
    HasCrossCurveDeviationLabel: bool
    HasInfoLabel: bool
    HasInnerToleranceLabel: bool
    HasMaximumValueLabel: bool
    HasMinimumValueLabel: bool
    InnerTolerance: float
    IsColorMapDisplayed: bool
    IsDirectionReversed: bool
    IsLabelDisplayed: bool
    IsMarkerDisplayed: bool
    IsNeedlePlotDisplayed: bool
    MaxCheckingAngle: float
    MaxCheckingDistance: float
    MeasurementMethod: GeometricAnalysis.DeviationGaugeBuilder.MeasurementMethodType
    MeasurementSamples: int
    MinMaxOption: GeometricAnalysis.DeviationGaugeBuilder.MinMaxType
    NeedleScale: float
    NegativeInnerTolerance: float
    NegativeOuterTolerance: float
    OuterTolerance: float
    Plane: Plane
    PositiveInnerTolerance: float
    PositiveOuterTolerance: float
    ReferenceObjects: SelectNXObjectList
    ReportingPerType: GeometricAnalysis.DeviationGaugeBuilder.ReportingPerTypes
    SpatialResolution: float
    SuggestScaleFactor: bool
    SurfaceRangeControl: GeometricUtilities.SurfaceRangeBuilder
    TargetObjects: SelectNXObjectList
    UseDefiningPoints: bool
    VectorComponentDirection: Direction
    XyzDirection: GeometricAnalysis.DeviationGaugeBuilder.XyzDirectionType


    class XyzDirectionType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class ReportingPerTypes(enum.Enum):
        AnalysisObject = 0
        Target = 1
        Reference = 2
    

    class MinMaxType(enum.Enum):
        Minmax = 0
        Minimum = 1
        Maximum = 2
        None = 3
    

    class MeasurementMethodType(enum.Enum):
        ThreeDim = 0
        XyzDirection = 1
        WorkView = 2
        VectorComponent = 3
        Plane = 4
        AlongVector = 5
    

    class ColorPlotTypes(enum.Enum):
        Blend = 0
        Stepped = 1
        None = 2
    

    class AdditionalValuesLabelType(enum.Enum):
        UserDefined = 0
        Intermediate = 1
        All = 2
        None = 3
    

class DeviationGauge(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class DeviationChecking(Builder):
    def __init__(self) -> None: ...
    def Check(self) -> None:
        ...
    AngleTolerance: float
    Curve: SelectIBaseCurve
    DeviationOption: GeometricAnalysis.DeviationChecking.DeviationOptions
    DistanceTolerance: float
    FaceOfFirstEdge: SelectIParameterizedSurface
    FaceOfSecondEdge: SelectIParameterizedSurface
    FirstCurve: SelectIBaseCurve
    FirstEdge: SelectIBaseCurve
    FirstFace: SelectIParameterizedSurface
    NumberCheckPoints: int
    NumberUcheckPoints: int
    NumberVcheckPoints: int
    SecondCurve: SelectIBaseCurve
    SecondEdge: SelectIBaseCurve
    SecondFace: SelectIParameterizedSurface
    Type: GeometricAnalysis.DeviationChecking.Types


    class Types(enum.Enum):
        CurveToCurve = 0
        CurveToFace = 1
        EdgeToFace = 2
        FaceToFace = 3
        EdgeToEdge = 4
    

    class DeviationOptions(enum.Enum):
        NoDeviations = 0
        AllDeviations = 1
        MaximumDistance = 2
        MinimumDistance = 3
        MaximumAngle = 4
        MinimumAngle = 5
    

class CurveCurvatureAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateWorkView(self) -> None:
        ...
    def CreateDumbPeakPoints(self) -> typing.List[Point]:
        ...
    def CreateDumbInflectionPoints(self) -> typing.List[Point]:
        ...
    def GetCurveRange(self, index: int) -> GeometricUtilities.CurveRangeBuilder:
        ...
    def GetCurveRangeListLength(self) -> int:
        ...
    CombOptions: GeometricUtilities.CombOptionsBuilder
    CombRange: GeometricUtilities.CurveRangeBuilder
    DynamicProjection: bool
    Method: GeometricAnalysis.CurveCurvatureAnalysisBuilder.CalculationMethod
    Projection: GeometricAnalysis.CurveCurvatureAnalysisBuilder.ProjectionTypes
    ReverseDirection: int
    SelectedCurves: ScCollector
    ShowCombs: bool
    ShowInflections: bool
    ShowMaxLabels: bool
    ShowMinLabels: bool
    ShowPeaks: bool
    Style: GeometricAnalysis.CurveCurvatureAnalysisBuilder.DisplayStyle
    Vector: Direction
    Xyz: GeometricAnalysis.CurveCurvatureAnalysisBuilder.XyzTypes


    class XyzTypes(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class ProjectionTypes(enum.Enum):
        None = 0
        CurvePlane = 1
        Vector = 2
        View = 3
        Xyz = 4
    

    class NeedleDirection(enum.Enum):
        Inside = 0
        Outside = 1
    

    class LabelValues(enum.Enum):
        Curvature = 0
        RadiusofCurvature = 1
    

    class DisplayStyle(enum.Enum):
        Linear = 0
        Logarithmic = 1
    

    class CalculationMethod(enum.Enum):
        Curvature = 0
        RadiusofCurvature = 1
    

class CurveCurvatureAnalysis(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class CurveContinuityBuilder(Builder):
    def __init__(self) -> None: ...
    def ResetShowDeviation(self) -> None:
        ...
    AngularThreshold: Expression
    ContinuityType: GeometricAnalysis.CurveContinuityBuilder.Type
    DistanceThreshold: Expression
    DynamicLabel: SelectNXObject
    EndPointX: float
    EndPointY: float
    EndPointZ: float
    G0Check: bool
    G0Check2: bool
    G0Tolerance: float
    G1Check: bool
    G1Check2: bool
    G1Tolerance: float
    G2Check: bool
    G2Check2: bool
    G2Tolerance: float
    G3Check: bool
    G3Check2: bool
    G3Tolerance: float
    MultiCurve: SelectDisplayableObjectList
    SelectCurve: SelectNXObject
    SelectObject: SelectNXObject
    ShowDeviation: bool
    ShowMarkup: bool
    ShowMaximum: bool
    ShowMinimum: bool
    ShowNeedle: bool
    ShowOutOfTolerance: bool


    class Type(enum.Enum):
        CurvetoObject = 0
        Multicurve = 1
    

class CurveContinuity(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class CurveAnalysisRecord(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.GeometricAnalysis.CurveAnalysisDisplay.")"""
        ...
    CombDensity: int
    CombInterneedleDensity: int
    CombMaxLength: float
    CombScaleFactor: float
    Direction: Vector3d
    DirectionOption: GeometricAnalysis.CurveAnalysisRecord.DirectionOptionType
    End: float
    ShowComb: bool
    ShowInflection: bool
    ShowKnot: bool
    ShowPeak: bool
    ShowPole: bool
    Start: float
    UseMaxLength: bool


    class DirectionOptionType(enum.Enum):
        None = 0
        PlaneOfCurve = 1
        SpecifyVector = 2
        WorkView = 3
    

class CurveAnalysisDisplay(Utilities.NXRemotableObject):
    def __init__(self, owner: GeometricAnalysis.AnalysisObjectCollection) -> None: ...
    def SetAnalysisRecord(self, curve: Curve, record: GeometricAnalysis.CurveAnalysisRecord) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.GeometricAnalysis.CurveCurvatureAnalysis.")"""
        ...
    def GetAnalysisRecord(self, curve: Curve) -> GeometricAnalysis.CurveAnalysisRecord:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.GeometricAnalysis.CurveCurvatureAnalysis.")"""
        ...
    def NewRecord(self) -> GeometricAnalysis.CurveAnalysisRecord:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.GeometricAnalysis.CurveCurvatureAnalysis.")"""
        ...
    def SetShowFlag(self, curve: Curve, choice: GeometricAnalysis.CurveAnalysisDisplay.ShowFlagType, on: bool) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.GeometricAnalysis.CurveCurvatureAnalysis.")"""
        ...
    def SetShowPole(self, curve: Curve, show: bool) -> None:
        ...
    def GetShowPole(self, curve: Curve) -> bool:
        ...
    def SetShowKnot(self, curve: Curve, show: bool) -> None:
        ...
    def GetShowKnot(self, curve: Curve) -> bool:
        ...
    def SetShowEndPoints(self, curve: Curve, show: bool) -> None:
        ...
    def GetShowEndPoints(self, curve: Curve) -> bool:
        ...
    def Tag(self) -> Tag: ...



    class ShowFlagType(enum.Enum):
        Pole = 0
        Comb = 1
        Inflection = 2
        Peak = 3
        Knot = 4
        Endpoint = 5
    

class ContactAnalysisSectionCurveBuilder(Display.DynamicSectionBuilder):
    def __init__(self) -> None: ...
    def OrientToPlane(self) -> None:
        ...
    BallDiameter: float
    DisplaySlice: bool
    PointToPlaceSphere: Point
    SectionBoundary: Expression
    SectionCurveColor: NXColor


class ContactAnalysisResult(Validate.AnalysisResult):
    def __init__(self) -> None: ...


class ContactAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateCheckPoints(self) -> None:
        ...
    def CreateSectionCurves(self) -> GeometricAnalysis.ContactAnalysisSectionCurveBuilder:
        ...
    def SaveContourCurves(self) -> None:
        ...
    def Update(self) -> None:
        ...
    def AddGCPoint(self, face: Face, point: Point) -> None:
        ...
    def SetGCPoint(self, face: Face, point: Point) -> None:
        ...
    def DeleteGCPoint(self, point: Point) -> None:
        ...
    def ClearGConstraintPointData(self) -> None:
        ...
    AreasNotTouchedByBall: NXColor
    AreasTouchedByBall: NXColor
    AutomaticUpdate: bool
    BallDiameter: Expression
    BodySelection: ScCollector
    CreateMinRadiusPoints: bool
    CreatePointsAtStepDist: bool
    DisplayContourCurves: bool
    DisplayResolution: GeometricUtilities.DisplayResolutionBuilder
    EnableRadiusAnalysis: bool
    ExternalBallDiameter: Expression
    GeometricConstraintDataManager: Features.GeometricConstraintDataManager
    HemishpericalBallDiameter: Expression
    IntermediateAreas: NXColor
    InternalBallDiameter: Expression
    MaximumRadius: Expression
    MinimumRadius: Expression
    Normals: GeometricAnalysis.FaceAnalysisNormalsBuilder
    ProtrusionLimit: Expression
    RamDiameter: Expression
    SharpAreas: NXColor
    ShowOnlyContactAnalysisAreas: bool
    ShowOnlySharpAreas: bool
    SmoothAreas: NXColor
    StepDistance: Expression


class AnalysisResultCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Validate.AnalysisResult]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateContactAnalysisBuilder(self, persistentResult: Validate.AnalysisResult) -> GeometricAnalysis.ContactAnalysisBuilder:
        ...
    def CreateContactAnalysisSectionCurveBuilder(self, view: ModelingView, contactAnalysisBuilder: GeometricAnalysis.ContactAnalysisBuilder) -> GeometricAnalysis.ContactAnalysisSectionCurveBuilder:
        ...
    def Tag(self) -> Tag: ...



class AnalysisObjectCollectionEx(Utilities.NXRemotableObject):
    def __init__(self, owner: GeometricAnalysis.AnalysisObjectCollection) -> None: ...
    def CreateRadiusAnalysisBuilder(self, radiusAO: DisplayableObject) -> GeometricAnalysis.RadiusAnalysisBuilder:
        ...
    def CreateSlopeAnalysisBuilder(self, slopeAO: DisplayableObject) -> GeometricAnalysis.SlopeAnalysisBuilder:
        ...
    def CreateDistanceAnalysisBuilder(self, distanceAO: DisplayableObject) -> GeometricAnalysis.DistanceAnalysisBuilder:
        ...
    def CreateReflectionAnalysisBuilder(self, reflectionAO: DisplayableObject) -> GeometricAnalysis.ReflectionAnalysisBuilder:
        ...
    def CreateSheetBoundaryAnalysisBuilder(self, sheetBoundaryAnalysisAO: GeometricAnalysis.SheetBoundaryAnalysis) -> GeometricAnalysis.SheetBoundaryAnalysisBuilder:
        ...
    def Tag(self) -> Tag: ...



class AnalysisObjectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[GeometricAnalysis.AnalysisObject]:
        ...
    def __init__(self, owner: GeometricAnalysis.AnalysisManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateGapFlushnessBuilder(self, gfaoObject: GeometricAnalysis.GapFlushness) -> GeometricAnalysis.GapFlushnessBuilder:
        ...
    def CreateSurfaceContinuityAnalysisBuilder(self, scaoObject: DisplayableObject) -> GeometricAnalysis.SurfaceContinuityAnalysisBuilder:
        ...
    def CreateCurveCurvatureAnalysisBuilder(self, caaoObject: DisplayableObject) -> GeometricAnalysis.CurveCurvatureAnalysisBuilder:
        ...
    def CreateHighlightLinesAnalysisBuilder(self, hpaoObject: DisplayableObject) -> GeometricAnalysis.HighlightLinesAnalysisBuilder:
        ...
    def CreateSectionAnalysisBuilder(self, msaoObject: GeometricAnalysis.SectionAnalysisObject) -> GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder:
        ...
    def CreateSectionAnalysisExBuilder(self, csaoObject: GeometricAnalysis.SectionAnalysis.SectionAnalysisExObject) -> GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder:
        ...
    def CreateDeviationGaugeBuilder(self, ddaoObject: DisplayableObject) -> GeometricAnalysis.DeviationGaugeBuilder:
        ...
    def CreateCurveContinuityBuilder(self, ccaoObject: DisplayableObject) -> GeometricAnalysis.CurveContinuityBuilder:
        ...
    def CreateSurfaceIntersectionBuilder(self, siaoObject: DisplayableObject) -> GeometricAnalysis.SurfaceIntersectionBuilder:
        ...
    def CreateDraftAnalysisBuilder(self, daoObject: DisplayableObject) -> GeometricAnalysis.DraftAnalysisBuilder:
        ...
    def CreateLocalRadiusAnalysisBuilder(self, lrao: GeometricAnalysis.LocalRadiusAnalysis) -> GeometricAnalysis.LocalRadiusAnalysisBuilder:
        ...
    def CreateFaceCurvatureAnalysisBuilder(self, fcaoObject: DisplayableObject) -> GeometricAnalysis.FaceCurvatureAnalysisBuilder:
        ...
    def Tag(self) -> Tag: ...

    CurveAnalysisDisplayObject: GeometricAnalysis.CurveAnalysisDisplay
    SurfaceAnalysisDisplayObject: GeometricAnalysis.SurfaceAnalysisDisplay
    AnalysisObjectsEx: GeometricAnalysis.AnalysisObjectCollectionEx


class AnalysisObject(DisplayableObject):
    def __init__(self) -> None: ...


class AnalysisManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def CreateExamineGeometryObject(self) -> GeometricAnalysis.ExamineGeometry:
        ...
    def CreateSimpleInterferenceObject(self) -> GeometricAnalysis.SimpleInterference:
        ...
    def CreateGeometricPropertiesObject(self) -> GeometricAnalysis.GeometricProperties:
        ...
    def CreateSolidDensityObject(self) -> GeometricAnalysis.SolidDensity:
        ...
    def CreateDeviationCheckingObject(self) -> GeometricAnalysis.DeviationChecking:
        ...
    def Tag(self) -> Tag: ...

    AnalysisObjects: GeometricAnalysis.AnalysisObjectCollection


