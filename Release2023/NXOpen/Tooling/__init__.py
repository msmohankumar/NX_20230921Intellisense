from ...NXOpen import *
from ..Tooling import *

import typing
import enum

class WorkPieceData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetSessionDelay(self, isDelay: bool) -> None:
        ...
    def SetOneProdDim(self, num: int, dimension: float) -> None:
        ...
    def SetDimOffset(self, dimOffset: float) -> None:
        ...
    def SetOneDimOffset(self, num: int, dimOffset: float) -> None:
        ...
    def SetDim(self, dimension: float) -> None:
        ...
    def SetZLength(self, dimensionZ: float) -> None:
        ...
    def SetOneDim(self, num: int, dimension: float) -> None:
        ...
    def SetOriginPointCoord(self, num: int, originPoint: float) -> None:
        ...
    def SetDataChanged(self, isChanged: bool) -> None:
        ...


class WorkpieceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.WorkpieceBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateWorkpieceBuilder(self) -> Tooling.WorkpieceBuilder:
        ...
    def Tag(self) -> Tag: ...



class WorkpieceBuilder(Builder):
    def __init__(self) -> None: ...
    def ResetSizes(self) -> None:
        ...
    def GetWorkPieceData(self) -> Tooling.WorkPieceData:
        ...
    def CreateWorkPieceData(self) -> Tooling.WorkPieceData:
        ...
    def SetWorkpiecePartBlankStatus(self, partTag: NXObject, blank: int) -> None:
        ...
    def InitWorkPieceData(self, type: Tooling.WorkpieceBuilder.MethodType, workpiecetype: Tooling.WorkpieceBuilder.WorkPieceType) -> None:
        ...
    def SetLayoutInfo(self) -> None:
        ...
    def UpdateSketchCurves(self, workpiece: NXObject) -> None:
        ...
    def UpdateSketchCurvesWhenUsingRefPoint(self, sketchTag: NXObject, offset: float) -> None:
        ...
    def LinkSketchWorkpieceToShrinkPart(self, createType: Tooling.WorkpieceBuilder.WorkPieceType, body: NXObject) -> None:
        ...
    def SetExtrudeBuilder(self, extrude: Features.FeatureBuilder) -> None:
        ...
    def SetCombinedExtrudeBuilder(self, combinedExtrude: Features.FeatureBuilder) -> None:
        ...
    def MoveStandardWorkpieceToLayer(self, newLayer: int) -> None:
        ...
    def MoveWorkpieceSketchToLayer(self, newLayer: int) -> None:
        ...
    def EditWorkpieceUdo(self, body: NXObject, boxSize: float) -> None:
        ...
    def InsertBlock(self) -> None:
        ...
    BlockType: Tooling.WorkpieceBuilder.WorkPieceType
    GenerateMethod: Tooling.WorkpieceBuilder.MethodType
    ReferencePoint: Point
    RoundDimensionValue: bool
    RoundPrecision: float
    RoundTotalDimension: bool
    RoundTotalDimensionPrecision: float
    SelectWorkPieceBody: SelectBodyList
    ShowBoundbox: bool
    Type: Tooling.WorkpieceBuilder.Types


    class WorkPieceType(enum.Enum):
        UserDefinedBlock = 0
        CavityCore = 1
        CavityOnly = 2
        CoreOnly = 3
    

    class Types(enum.Enum):
        ProductWorkPiece = 0
        CombinedWorkPiece = 1
    

    class MethodType(enum.Enum):
        DistanceAllowance = 0
        ReferencePoint = 1
        Sketch = 2
        KfBox = 3
    

class WorkflowManagementCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ChangeoverManagementBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateChangeoverManagementBuilder(self) -> Tooling.ChangeoverManagementBuilder:
        ...
    def CreateConcurrentDesignManagementBuilder(self) -> Tooling.ConcurrentDesignManagementBuilder:
        ...
    def Tag(self) -> Tag: ...



class WireHoleCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.WireHoleBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateWireHoleBuilder(self) -> Tooling.WireHoleBuilder:
        ...
    def Tag(self) -> Tag: ...



class WireHoleBuilder(Builder):
    def __init__(self) -> None: ...
    CenterlineLength: str
    CircleCenter: Point
    DistanceToEdgeMidpoint: float
    HoleDepth: float
    HoleDiameter: float
    SelectEdge: SelectEdgeList
    SketchOrientation: Direction
    SketchPlane: ScCollector
    Type: Tooling.WireHoleBuilder.Types


    class Types(enum.Enum):
        SpecifyPoint = 0
        SelectEdge = 1
    

class WallThicknessCheckerManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def CreateBuilder(self) -> Tooling.WallThicknessCheckerBuilder:
        ...
    def Tag(self) -> Tag: ...



class WallThicknessCheckerBuilder(Builder):
    def __init__(self) -> None: ...
    def Calculate(self) -> None:
        ...
    def SaveResults(self) -> None:
        ...
    def DeleteSavedResults(self) -> None:
        ...
    def InitThicknessData(self, changeBody: int) -> None:
        ...
    def UpdateSelectedFacesInfo(self) -> None:
        ...
    def CreateThicknessGraphicObjects(self, startPoint: Point3d, directionVector: Vector3d, length: float, color: NXColor) -> None:
        ...
    def RecordTransientMeshes(self) -> None:
        ...
    def KeepTransientMeshes(self, keepMeshes: int) -> None:
        ...
    def SaveThicknessUDO(self, saveThicknessUDO: bool) -> None:
        ...
    def SaveSelectedWTAnalysisResultsAO(self, selectedWTAnalysisResultsAO: TaggedObject) -> None:
        ...
    def GetWallThicknessResultsData(self, bodyOrFaceTag: TaggedObject, averageThickness: float, minimumThickness: float, maximumThickness: float) -> None:
        ...
    def GetThicknessAtPointOnFace(self, pntOnFace: Point3d, thickness: float, faceTag: Face) -> None:
        ...
    def GetFacetsAndThicknessWithinRange(self, lowerLimit: float, upperLimit: float, facetIDs: int, facetFaceTags: typing.List[Face], vertexCoords: typing.List[Point3d], thicknesses: float) -> None:
        ...
    def UpdateMaximumThicknessToleranceAndMaximumSpacingOnSamplePointsSettingsValueChange(self, samplePointsSettingsValue: int) -> None:
        ...
    def ApplyAllDefaultParametersAfterInit(self) -> None:
        ...
    def ApplyDefaultDisplayParametersAfterCalculate(self) -> None:
        ...
    def ExecuteApply(self) -> None:
        ...
    def CleanupDataAndDisplay(self) -> None:
        ...
    def GetLegendColorRGBs(self, colorRGBs: typing.List[NXColor.Rgb]) -> None:
        ...
    def GetLegendColorLabels(self, colorLabels: str) -> None:
        ...
    def GetLegendLowerAndUpperRangeLimits(self, lowerRangeLimits: float, upperRangeLimits: float) -> None:
        ...
    def CreatePMIAtPointOnFace(self, pointOnFace: Point3d) -> None:
        ...
    def GetRayVectorsAndColorsWithinRange(self, lowerLimit: float, upperLimit: float, rayStartPnts: typing.List[Point3d], rayEndPnts: typing.List[Point3d], rayColorRGBs: typing.List[NXColor.Rgb]) -> None:
        ...
    def CheckThicknessAnalysisResultsAvailableInPartFile(self, bodyTag: Body, resultsAvailable: int, bodyWithResults: Body, bodyWithNoResults: Body) -> None:
        ...
    def SaveThicknessAnalysisResultsToPartFile(self) -> None:
        ...
    def DeleteThicknessAnalysisResultsOfCurrentBodyFromPartFile(self) -> None:
        ...
    def GetThicknessCalculationParametersByBody(self, bodyTag: Body, resultsAvailable: int, elemSizeScale: int, elemSize: float, chordDistTol: float) -> None:
        ...
    def GetThicknessCalculationParametersAndMethodByBody(self, bodyTag: Body, resultsAvailable: int, elemSizeScale: int, elemSize: float, chordDistTol: float, calculateMethod: int) -> None:
        ...
    def CheckResultsAvailableAndUpToDate(self, bodyTag: Body, resultsAvailable: int, resultsUpToDate: int) -> None:
        ...
    def IdentifyAndGroupBodies(self, bodyTags: typing.List[Body], bodyResults: typing.List[Body], bodyNoResults: typing.List[Body]) -> None:
        ...
    def UpdateColorDisplayOnSelectedRangeLimitsChange(self, lowerRangeLimit: float, upperRangeLimit: float) -> None:
        ...
    def UpdateFullColorDisplayOnRangeLimitsChange(self, lowerRangeLimit: float, upperRangeLimit: float) -> None:
        ...
    def UpdateAboveLimitColorDisplayOnAboveLimitChange(self, aboveLimit: float) -> None:
        ...
    def UpdateBelowLimitColorDisplayOnBelowLimitChange(self, belowLimit: float) -> None:
        ...
    def CreateConnectedFacetsSets(self) -> None:
        ...
    def FreeConnectedFacetsSets(self) -> None:
        ...
    def GetOrCreateRangeAreasSetConvergentBodies(self, areaNodeID: int, convergentBodies: typing.List[Body]) -> None:
        ...
    def DeleteAllConnectedAreasConvergentBodies(self) -> None:
        ...
    def DrawRangeAreaRaysTemporaryDisplay(self, areaNodeID: int) -> None:
        ...
    CalPageNormalVector: Direction
    CalculationBody: SelectBody
    CalculationCalculateMethod: Tooling.WallThicknessCheckerBuilder.CalculateMethod
    CalculationMaximumSpacing: float
    CalculationMaximumThicknessTolerance: float
    CalculationProjectToFace: bool
    CalculationSamplePointsIntervalScale: int
    InApplyStatus: int
    InspectDisplayVolumeFillers: bool
    InspectDisplayWithExcludeColor: bool
    InspectExcludeColor: NXColor
    InspectExcludeDistance: float
    InspectExcludeSharpEdgeResultsDisplay: bool
    InspectionChangeFacesColor: bool
    InspectionDisplayFringeColorPlot: bool
    InspectionDisplayRayVectors: bool
    InspectionDynamicPointOnFace: SelectFace
    InspectionFaces: SelectFaceList
    InspectionIncludeAllFaces: bool
    InspectionSelectedFacesColor: NXColor
    InspectionThicknessFilterRangeHighLimit: float
    InspectionThicknessFilterRangeLowLimit: float
    InspectionTranslucency: int
    InspectionUseThicknessRangeSelect: bool
    InvokedFromPartNavigator: bool
    OptionsColor01: NXColor
    OptionsColor02: NXColor
    OptionsColor03: NXColor
    OptionsColor04: NXColor
    OptionsColor05: NXColor
    OptionsColor06: NXColor
    OptionsColor07: NXColor
    OptionsColor08: NXColor
    OptionsColor09: NXColor
    OptionsColor10: NXColor
    OptionsColor11: NXColor
    OptionsColor12: NXColor
    OptionsCreateBall: bool
    OptionsCreateThicknessText: bool
    OptionsDisplayDynamicBall: bool
    OptionsDisplayMeshElements: bool
    OptionsDisplayOppositeMeshElements: bool
    OptionsDisplayThicknessVectors: bool
    OptionsDynamicSnapToVertex: bool
    OptionsLegendControl: Tooling.WallThicknessCheckerBuilder.LegendControl
    OptionsLowerLimit01: float
    OptionsLowerLimit02: float
    OptionsLowerLimit03: float
    OptionsLowerLimit04: float
    OptionsLowerLimit05: float
    OptionsLowerLimit06: float
    OptionsLowerLimit07: float
    OptionsLowerLimit08: float
    OptionsLowerLimit09: float
    OptionsLowerLimit10: float
    OptionsLowerLimit11: float
    OptionsLowerLimit12: float
    OptionsNumDecimals: int
    OptionsNumberOfColors: int
    OptionsRangeHighLimit: float
    OptionsRangeLowLimit: float
    OptionsRangeType: Tooling.WallThicknessCheckerBuilder.RangeType
    OptionsSaveThicknessVectorsAsLines: bool
    OptionsUpperLimit01: float
    OptionsUpperLimit02: float
    OptionsUpperLimit03: float
    OptionsUpperLimit04: float
    OptionsUpperLimit05: float
    OptionsUpperLimit06: float
    OptionsUpperLimit07: float
    OptionsUpperLimit08: float
    OptionsUpperLimit09: float
    OptionsUpperLimit10: float
    OptionsUpperLimit11: float
    OptionsUpperLimit12: float


    class RangeType(enum.Enum):
        Uniform = 0
        UserDefined = 1
    

    class LegendControl(enum.Enum):
        Blend = 0
        Sharp = 1
    

    class CalculateMethod(enum.Enum):
        Ray = 0
        RollingBall = 1
        VectorProject = 2
    

class VentingDesignBuilder(Builder):
    def __init__(self) -> None: ...
    def GetEditFeatureGroup(self) -> NXObject:
        ...
    def SetEditFeatureGroup(self, featureGroup: NXObject) -> None:
        ...
    def SetVentGuideObjects(self, selObjects: typing.List[NXObject]) -> None:
        ...
    def SetVentPointsObjects(self, selPoints: typing.List[Point]) -> None:
        ...
    def EditRegisterFile(self) -> None:
        ...
    def EditDataBase(self) -> None:
        ...
    def GetDataFromSpreadsheet(self, sheetData: Tooling.SpreadsheetData) -> None:
        ...
    def UpdateVentingGuideDataFromUDO(self, featureGroupTag: NXObject, ventUdo: NXObject) -> None:
        ...
    def CreateReliefLoops(self) -> None:
        ...
    def UpdateGuideLoops(self) -> None:
        ...
    def UpdateAGuideLoop(self, editedCurve: NXObject) -> None:
        ...
    def CreateVentCurvesByEndPoint(self, selPoints: typing.List[Point], deselPoints: typing.List[Point]) -> None:
        ...
    def EditReliefLoopPosition(self, selectBoundary: typing.List[Curve], point: Point3d, crvTangent: Vector3d, newOrigin2: Point3d) -> Point:
        ...
    def RemoveAllVentCurves(self) -> None:
        ...
    def DisplayVentCurves(self) -> None:
        ...
    def RemoveSelectedVentCurves(self, selectBoundary: typing.List[Curve]) -> None:
        ...
    def ReadActionLevelDataFromDatabase(self, levelTypes: str) -> None:
        ...
    def SetParameterTreeData(self, paraNames: str, paraValues: str) -> None:
        ...
    def ReadSelectedActionLevelData(self, type: Tooling.VentingDesignBuilder.Action) -> None:
        ...
    def UpdateClearanceBoundary(self) -> None:
        ...
    AlignmentInside: bool
    AlignmentOutside: bool
    ConnectType: Tooling.VentingDesignBuilder.GuideConnectType
    DrawDirection: Direction
    EditLoopPosition: SelectCurveList
    GuideLines: ScCollector
    ResultStyle: Tooling.VentingDesignBuilder.ResultType
    ReverseDirection: bool
    ReverseSimpleDirection: bool
    SelectedFaces: SelectFaceList
    ShowInfoWindow: bool
    ThirdLevelPoints: ScCollector
    TrimSurface: SelectBodyList
    Type: Tooling.VentingDesignBuilder.Action


    class Section(enum.Enum):
        Circular = 0
        Block = 1
        None = 2
    

    class ResultType(enum.Enum):
        Default = 0
        OnlyCurve = 1
        NoSubtract = 2
    

    class GuideConnectType(enum.Enum):
        Default = 0
        Connect = 1
        Enclose = 2
    

    class Action(enum.Enum):
        StandardVent = 0
        SimpleVent = 1
        None = 2
    

class ValidDFMCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ValidDFMBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateValidDfmBuilder(self) -> Tooling.ValidDFMBuilder:
        ...
    def Tag(self) -> Tag: ...



class ValidDFMBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSelectedCheckerIds(self, selectedCheckerIds: str) -> None:
        ...
    def GetSelectedCheckerIds(self) -> str:
        ...
    def SetSelectedCheckerIndicies(self, selectedCheckerIndicies: int) -> None:
        ...
    def GetSelectedCheckerIndicies(self) -> int:
        ...
    def SetRecognizeSheetMetalFeatures(self, recognize: bool) -> None:
        ...
    def GetRecognizeSheetMetalFeatures(self) -> bool:
        ...
    def RegisterCheckers(self) -> None:
        ...
    def SetCheckSheetMetalFeatures(self, check: bool) -> None:
        ...
    def GetCheckSheetMetalFeatures(self) -> bool:
        ...
    def UpdateValidationResult(self, validationResultTag: TaggedObject) -> None:
        ...
    BendClearance: float
    CreatePersistentResult: bool
    CutoutCornerAngle: float
    CutoutCornerRadius: float
    CutoutSizeDoubleDLength: float
    CutoutSizeDoubleDWidth: float
    CutoutSizeHexagonLength: float
    CutoutSizeHexagonLengthMin: float
    CutoutSizeOblongLength: float
    CutoutSizeOblongLengthMin: float
    CutoutSizeOblongRadius: float
    CutoutSizeOblongRadiusMin: float
    CutoutSizePartialCircularDiameter: str
    CutoutSizePartialCircularWidth: float
    CutoutSizeRectangleLength: float
    CutoutSizeRectangleLengthMin: float
    CutoutSizeRectangleRadius: float
    CutoutSizeRectangleRadiusMin: float
    CutoutSizeRectangleWidth: float
    CutoutSizeRectangleWidthMin: float
    CutoutSizeRoundRadius: str
    CutoutSizeRoundRadiusMin: str
    CutoutSizeSquareLength: float
    CutoutSizeSquareLengthMin: float
    CutoutSizeSquareRadius: float
    CutoutSizeSquareRadiusMin: float
    DeviationBendBreakRadius: str
    DisplayInCheckMate: bool
    DistBendToBend: str
    DistCutoutToBend: str
    DistCutoutToCutout: str
    DoubleMaxBendAngle: float
    DoubleMinBendAngle: float
    EqThicknessTol: float
    FaceSelect: ScCollector
    HemAngleTol: float
    HemClearance: float
    HemFactor: str
    HemLength: str
    MaxThickness: float
    MinBendHeight: str
    MinThickness: float
    NBendHeight: str
    ShowResult: bool
    StandardBendBreakRadius: str
    TangentAngleTol: float


    class CheckerType(enum.Enum):
        CheckBendAngle = 0
        CheckBendRadius = 1
        CheckBendHeight = 2
        CheckBendDirection = 3
        CheckCutoutCorner = 4
        CheckCutoutShape = 5
        CheckCutoutSize = 6
        CheckBendToBendDistance = 7
        CheckCutoutToBendDistance = 8
        CheckCutoutToCutoutDistance = 9
        CheckCylindricalBendFace = 10
        CheckCoaxisForMultipleBends = 11
        CheckTangentBetweenBendAndTab = 12
        CheckBendThickness = 13
        CheckInvalidAdjFaceToBend = 14
        CheckHemClearance = 15
        CheckBendSharpCorner = 16
        CheckPartThickness = 17
        CheckPartVolume = 18
        Count = 19
        CheckNBend = 20
        CheckZBend = 21
        CheckVBend = 22
    

    class CategoryType(enum.Enum):
        Manufacturability = 0
        Unformability = 1
        FeatureCheck = 2
        Count = 3
    

class ValidCheckCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ValidCheckBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateValidCheckBuilder(self) -> Tooling.ValidCheckBuilder:
        ...
    def Tag(self) -> Tag: ...



class ValidCheckBuilder(Builder):
    def __init__(self) -> None: ...
    def StdAddUserSets(self) -> None:
        ...
    def StdLoadFile(self) -> None:
        ...
    def RemoveDataSet(self, dataSetName: str) -> None:
        ...
    AnalyMode: Tooling.ValidCheckBuilder.AnalysisMode
    BlankBody: bool
    CheckType: Tooling.ValidCheckBuilder.CheckingType
    ClrSetName: str
    ClrZone: float
    ObjSelectTarget: SelectNXObjectList
    ObjSelectTool: SelectNXObjectList
    ObjSelectType: Tooling.ValidCheckBuilder.SelMode
    ScrewCheck: bool
    SelectDatasetsName: str
    SelectStandardSetsSpreadsheet: str
    SubAssembly: bool


    class SelMode(enum.Enum):
        Component = 0
        Body = 1
    

    class CheckingType(enum.Enum):
        TrueBody = 0
        FalseBody = 1
        Both = 2
    

    class AnalysisMode(enum.Enum):
        SolidBased = 0
        FacetBased = 1
    

class UserDefinedMotionBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteUserDefinedMotion(self, motionName: str) -> None:
        ...
    AssemblyComponentName: str
    CreateKinematicComponent: bool
    ExportMotion: str
    ImportMotion: str
    LinearCurveType: Tooling.UserDefinedMotionBuilder.LinearCurveTypes
    LinearMotionVector: Direction
    MotionBody: SelectDisplayableObjectList
    MotionName: str
    MotionType: Tooling.UserDefinedMotionBuilder.MotionTypes
    MoveDistance: float
    PressStartAngle: float
    PressStopAngle: float
    ReturnStartAngle: float
    ReturnStopAngle: float
    RotaryCurveType: Tooling.UserDefinedMotionBuilder.RotaryCurveTypes
    RotaryMotionAxis: Axis
    RotationAngle: float
    UseControlData: bool


    class RotaryCurveTypes(enum.Enum):
        Rotary = 0
        FromFile = 1
    

    class MotionTypes(enum.Enum):
        Linear = 0
        Rotary = 1
    

    class LinearCurveTypes(enum.Enum):
        Linear = 0
        FromFile = 1
    

class UnusedFileManagementCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.UnusedFileManagementBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateUnusedFileManagementBuilder(self) -> Tooling.UnusedFileManagementBuilder:
        ...
    def Tag(self) -> Tag: ...



class UnusedFileManagementBuilder(Builder):
    def __init__(self) -> None: ...
    ListDir: Tooling.UnusedFileManagementBuilder.FileDirectory
    SelectAll: bool


    class FileDirectory(enum.Enum):
        ProjectDirectory = 0
        RecycleBin = 1
    

class UniversalUnformBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BendFaces: ScCollector
    BendType: Tooling.UniversalUnformBuilder.BendTypes
    BlendFaces: ScCollector
    DefineNeutralFactor: Tooling.DefineNeutralFactorBuilder
    ReferenceFaceEdge: SelectNXObject
    UnformNeutralFactor: float


    class BendTypes(enum.Enum):
        StraightBend = 0
        ContourFlange = 1
        Burring = 2
    

class UnfoldingSimulationBuilder(Builder):
    def __init__(self) -> None: ...
    def StepBackward(self) -> None:
        ...
    def Play(self) -> None:
        ...
    def Pause(self) -> None:
        ...
    def StepForward(self) -> None:
        ...
    def CreateStepBody(self) -> None:
        ...
    AngleValue: float
    BendFaces: SelectFaceList
    CheckedBody: ScCollector
    ReferenceFaceEdge: ScCollector
    Speed: int
    State: int
    StepAngle: int


class UndersizeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.UndersizeBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateUndersizeBuilder(self) -> Tooling.UndersizeBuilder:
        ...
    def Tag(self) -> Tag: ...



class UndersizeBuilder(Builder):
    def __init__(self) -> None: ...
    Angle: Expression
    ElectrodeBodies: SelectBodyList
    OrbitPointList: SelectPointList
    OrbitSize: Expression
    OrbitType: Tooling.UndersizeBuilder.Orbit
    PointSpecify: Point
    SelectElectrodeBlock: SelectBodyList
    SelectPoints: SelectPointList
    SparkGap: Expression


    class Orbit(enum.Enum):
        Circular = 0
        Square = 1
        Triangle = 2
        Spherical = 3
        Points = 4
    

class UnderCutData(Tooling.CostDataObject):
    def __init__(self) -> None: ...
    def AskChildrenFeatures(self, undercuts: typing.List[Tooling.UnderCutData]) -> None:
        ...


class TrimSolidCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.TrimSolidBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTrimSolidBuilder(self) -> Tooling.TrimSolidBuilder:
        ...
    def Tag(self) -> Tag: ...



class TrimSolidBuilder(Builder):
    def __init__(self) -> None: ...
    def InsideBoundBox(self) -> None:
        ...
    def InsideCrossBoundBox(self) -> None:
        ...
    def SetBoundBox(self, block: Body) -> None:
        ...
    def SetManualBody(self, block: Body) -> None:
        ...
    def CreateBoundBox(self) -> None:
        ...
    def CreateToolingBox(self) -> Body:
        ...
    ActionType: Tooling.TrimSolidBuilder.TrimSolidAction
    ChangeBoxSize: bool
    Clearance: Expression
    RegionFaces: ScCollector
    RemoveParameter: bool
    SelectBoundBox: SelectBody
    SelectLinkTarget: Assemblies.SelectComponent
    SheetBody: SelectBodyList
    TaggedFaces: SelectFaceList
    TrimDirection: bool
    Type: Tooling.TrimSolidBuilder.Types


    class Types(enum.Enum):
        Face = 0
        SheetBody = 1
        ManufacturingRegion = 2
    

    class TrimSolidAction(enum.Enum):
        Trim = 0
        Subtract = 1
        KeepBoxandRegion = 2
    

class TrimRegionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.TrimRegionBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTrimRegionBuilder(self) -> Tooling.TrimRegionBuilder:
        ...
    def Tag(self) -> Tag: ...



class TrimRegionBuilder(Builder):
    def __init__(self) -> None: ...
    def GetColorValue(self, redValue: float, greenValue: float, blueValue: float) -> None:
        ...
    def SetColorValue(self, redValue: float, greenValue: float, blueValue: float) -> None:
        ...
    def SetTraverseEdges(self, traverseEdges: typing.List[NXObject]) -> None:
        ...
    AsPatchSurface: bool
    BodyColor: NXColor
    BoundaryBody: SelectNXObjectList
    BoundaryType: Tooling.TrimRegionBuilder.BoundaryOption
    ConvertType: Tooling.TrimRegionBuilder.ConvertTypeOption
    LoopCollector: ScCollector
    RegionPoint: RegionPointList
    RegionType: Tooling.TrimRegionBuilder.RegionOption
    TargetBody: SelectBody


    class RegionOption(enum.Enum):
        Keep = 0
        Discard = 1
    

    class ConvertTypeOption(enum.Enum):
        WithCopies = 0
        NoCopies = 1
    

    class BoundaryOption(enum.Enum):
        BodyCurve = 0
        Traverse = 1
    

class TrimMoldComponentsCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.TrimMoldComponentsBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTrimMoldComponentsBuilder(self) -> Tooling.TrimMoldComponentsBuilder:
        ...
    def Tag(self) -> Tag: ...



class TrimMoldComponentsBuilder(Builder):
    def __init__(self) -> None: ...
    def SetTrimDataDetails(self, surfaceType: int, trimDirection: int, targets: typing.List[NXObject], tools: typing.List[NXObject]) -> None:
        ...
    ActionType: Tooling.TrimMoldComponentsBuilder.TrimMethod
    TargetBodies: SelectBodyList
    TargetSelectScope: Tooling.TrimMoldComponentsBuilder.TargetScope
    ToolFace: ScCollector
    ToolSheetBody: SelectBody
    TrimDirection: bool
    TrimPart: Tooling.TrimMoldComponentsBuilder.TrimPartName
    TrimSurface: Tooling.TrimMoldComponentsBuilder.TrimSurfaceName


    class TrimSurfaceName(enum.Enum):
        SelectFaces = 0
        SelectSheetBody = 1
    

    class TrimPartName(enum.Enum):
        Notrimpart = 0
    

    class TrimMethod(enum.Enum):
        Trim = 0
        Untrim = 1
    

    class TargetScope(enum.Enum):
        Product = 0
        Any = 1
    

class TraverseLoopCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.TraverseLoopBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.TraverseLoopBuilder:
        ...
    def Tag(self) -> Tag: ...



class TraverseLoopBuilder(Builder):
    def __init__(self) -> None: ...
    def ActBack(self) -> None:
        ...
    def ActAccept(self) -> None:
        ...
    def ActCycle(self) -> None:
        ...
    def ActClose(self) -> None:
        ...
    def ActExit(self) -> None:
        ...
    def ActEdgeSelection(self, pTolSelObject: typing.List[NXObject], selections: typing.List[NXObject], deselections: typing.List[NXObject], cpoint: Point3d, selectEndEdge: bool) -> None:
        ...
    def ResetTraverseData(self) -> None:
        ...
    def MoveCurves(self, pPartingLines: typing.List[NXObject]) -> None:
        ...
    def SwitchToPartinglineLayer(self) -> None:
        ...
    def SetTraverseStartEndPoint(self, candidate: NXObject, pointCloseCursor: Point3d, selections: typing.List[NXObject]) -> None:
        ...
    def CheckGap(self, selections: typing.List[NXObject], nearPoint: Point3d) -> float:
        ...
    BridgeGap: bool
    ByColor: bool
    EndEdge: bool
    ExitLoop: bool
    SelectEdge: ScCollector
    TolSetting: float


class TrackingCurveBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateTrackingCurves(self) -> None:
        ...
    def ClearTrackingCurve(self) -> None:
        ...
    IntervalDouble: float
    KeepCurve: bool
    ShowAllComponentsToggle: bool
    ShowCurve: bool
    TrackEndDouble: float
    TrackPoint: Point
    TrackStartDouble: float


class ToolingSession(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateSpreadsheetData(self) -> Tooling.SpreadsheetData:
        ...
    def CreateCloneObject(self, applicationType: Tooling.ToolingApplication, cloneActionType: Tooling.ToolingCloneaction) -> Tooling.CloneObject:
        ...
    def GetReusableComponent(self) -> typing.List[Assemblies.Component]:
        ...
    def GetReusableObjects(self, part: NXObject, reusableObjects: typing.List[NXObject]) -> None:
        ...
    def LoadReusablePart(self, filename: str, isNativePart: bool) -> BasePart:
        ...
    def ClosePart(self, part: NXObject, wholeTree: BasePart.CloseWholeTree, closeModified: BasePart.CloseModified) -> None:
        ...
    def CreateComponentPattern(self, component: NXObject, targetEntity: NXObject) -> None:
        ...
    def SetWizardType(self, type: int) -> None:
        ...
    def SetWizardTypeStatus(self, statusType: Tooling.ToolingApplicationstatus) -> None:
        ...
    def SetEntryIdentifier(self, entryIdentifier: str) -> None:
        ...
    def AssignAttribute(self, objectTag: NXObject, attributeName: str, attributeValue: str) -> None:
        ...
    def ResetShrinkageAttribute(self, objectTag: NXObject, recalculateValue: bool, scaleType: int, expressionValues: str) -> None:
        ...
    def LoadInterpartData(self, objectTag: NXObject) -> None:
        ...
    def DeleteToolingComponents(self, reuseComponents: typing.List[Assemblies.Component]) -> None:
        ...
    def RemoveAllShrinkageAttributes(self, objectTag: NXObject) -> None:
        ...
    def GetLibraries(self, category: str, appName: str, runEnv: str, libNames: str, libPaths: str) -> None:
        ...
    def Tag(self) -> Tag: ...



class ToolingManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateReusableObject(self) -> Tooling.ReusableObject:
        ...
    def CreateSelectReuseLibraryListBuilder(self) -> Tooling.SelectReuseLibraryListBuilder:
        ...
    def DestroySelectReuseLibraryListBuilder(self, reuseListBuilder: Tooling.SelectReuseLibraryListBuilder) -> None:
        ...
    def Tag(self) -> Tag: ...

    MWSearchRegions: Tooling.MWSearchRegionCollection
    MWDefineRegions: Tooling.MWDefineRegionsCollection
    MWDefineSheets: Tooling.MWDefineSheetsCollection
    MWCopySheets: Tooling.MWCopySheetsCollection
    MWPartingManager: Tooling.MWPartingManagerCollection
    MWDesignPartingSurface: Tooling.MWDesignPartingSurfaceCollection
    MWTraversePartingLines: Tooling.MWTraversePartingLinesCollection
    MWDesignGuideLines: Tooling.MWDesignGuideLinesCollection
    MWMoldedPartValidation: Tooling.MWMoldedPartValidationManager
    WallThicknessChecker: Tooling.WallThicknessCheckerManager
    GuidedExtension: Tooling.GuidedExtensionManager
    ValidCheck: Tooling.ValidCheckCollection
    DirectUnfold: Tooling.DirectUnfoldCollection
    StockSizes: Tooling.StockSizeCollection
    MoldCsys: Tooling.MoldCsysCollection
    FamilyMolds: Tooling.FamilyMoldCollection
    Pockets: Tooling.PocketCollection
    ProfileSplits: Tooling.ProfileSplitCollection
    InitializeProjects: Tooling.InitProjectCollection
    PiercingInsert: Tooling.PiercingInsertCollection
    StripLayout: Tooling.StripLayoutCollection
    Layouts: Tooling.MWLayoutCollection
    SubInserts: Tooling.SubInsertCollection
    ScrapDesign: Tooling.ScrapDesignCollection
    Undersizes: Tooling.UndersizeCollection
    Workpieces: Tooling.WorkpieceCollection
    ElectrodeCopys: Tooling.ElectrodeCopyCollection
    InitProj: Tooling.InitProjCollection
    ConceptPositions: Tooling.ConceptPositionCollection
    WireHole: Tooling.WireHoleCollection
    HoleReport: Tooling.HoleReportCollection
    ReliefDesign: Tooling.ReliefDesignCollection
    ForceCalculation: Tooling.ForceCalculationCollection
    BendInsertDesign: Tooling.BendInsertDesignCollection
    UnusedFileManagement: Tooling.UnusedFileManagementCollection
    CornerDesign: Tooling.CornerDesignCollection
    MoldInserts: Tooling.MoldInsertCollection
    MoldProcesses: Tooling.MoldProcessCollection
    FastenerAssembly: Tooling.FastenerAssyCollection
    FastenerAssemConfig: Tooling.FastenerAssemConfigCollection
    ReferenceBlends: Tooling.ReferenceBlendCollection
    CalculateAreas: Tooling.CalculateAreaCollection
    FaceSplits: Tooling.FaceSplitCollection
    TraverseLoops: Tooling.TraverseLoopCollection
    EnlargeSurfaces: Tooling.EnlargeSurfaceCollection
    SolidPatchs: Tooling.SolidPatchCollection
    SplitSolids: Tooling.SplitSolidCollection
    EdgePatchs: Tooling.EdgePatchCollection
    AssignPatchs: Tooling.AssignPatchCollection
    TrimRegions: Tooling.TrimRegionCollection
    CoolingPattern: Tooling.CoolingPatternCollection
    CoolingDefineChannel: Tooling.CoolingDefineChannelCollection
    ChannelAdjust: Tooling.ChannelAdjustCollection
    CoolingConnect: Tooling.CoolingConnectCollection
    BlankGenerator: Tooling.BlankGeneratorCollection
    BlankLayout: Tooling.BlankLayoutCollection
    DieDesignSetting: Tooling.DieDesignSettingCollection
    EWMultiPositions: Tooling.EWMultiPositionCollection
    FormingInsert: Tooling.FormingInsertCollection
    InsertAuxiliary: Tooling.InsertAuxiliaryCollection
    EjectorPostProcessings: Tooling.EjectorPostProcessingCollection
    TrimMoldComponents: Tooling.TrimMoldComponentsCollection
    DesignTrimTools: Tooling.DesignTrimToolCollection
    CoolingExtend: Tooling.CoolingExtendCollection
    SIZER: Tooling.SIZERCollection
    Runner: Tooling.RunnerCollection
    MotionSimulation: Tooling.MotionSimulationCollection
    ReusablePocket: Tooling.ReusablePocketCollection
    ChannelFitting: Tooling.ChannelFittingCollection
    AutoDie: Tooling.AutoDieCollection
    ManufacturingGeometry: Tooling.ManufacturingGeometryCollection
    BurringInsert: Tooling.BurringInsertCollection
    ClearanceManagement: Tooling.ClearanceManagementCollection
    WorkflowManagement: Tooling.WorkflowManagementCollection
    LayoutManagement: Tooling.LayoutManagementCollection
    ReusableObjectManager: Tooling.ReusableObjectManager
    ToolingDrawing: Tooling.ToolingDrawingCollection
    TrimSolid: Tooling.TrimSolidCollection
    DieBase: Tooling.DieBaseCollection
    SpecifyBaffle: Tooling.SpecifyBaffleCollection
    ElectrodeDesign: Tooling.ElectrodeDesignCollection
    FastenerAssyCustomization: Tooling.FastenerAssyCustomizationCollection
    CreateBox: Tooling.CreateBoxCollection
    ReplaceSolid: Tooling.ReplaceSolidCollection
    SpecifyCircuit: Tooling.SpecifyCircuitCollection
    StandardPart: Tooling.StandardPartCollection
    QuickQuotation: Tooling.QuickQuotationCollection
    FastenerRemoveNode: Tooling.FastenerRemoveNodeCollection
    MoldDesign: Tooling.MoldDesignCollection
    IntermediateStage: Tooling.IntermediateStageCollection
    BendOperation: Tooling.BendOperationCollection
    StandardPartPosition: Tooling.StandardPartPositionCollection
    ProgressiveDie: Tooling.ProgressiveDieManager
    BlankNesting: Tooling.BlankNestingCollection
    Moldwizard: Tooling.MoldwizardManager
    ObjectAttributeManagement: Tooling.ObjectAttributeManagementCollection
    FaceColorManagement: Tooling.FaceColorManagementCollection
    HoleManufacturingNote: Tooling.HoleManufacturingNoteCollection
    HoleTable: Tooling.HoleTableCollection
    ConformalCooling: Tooling.ConformalCoolingManager
    ValidDFM: Tooling.ValidDFMCollection


class ToolingDrawingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.CompDrawingBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateComponentDrawingBuilder(self) -> Tooling.CompDrawingBuilder:
        ...
    def CreateAssemblyDrawingBuilder(self) -> Tooling.AssemblyDrawingBuilder:
        ...
    def CreateSectionLineCreationBuilder(self) -> Tooling.SectionLineCreationBuilder:
        ...
    def CreateAutoDimensionBuilder(self) -> Tooling.AutoDimensionBuilder:
        ...
    def CreateDrawingSheetNameBuilder(self) -> Tooling.DrawingSheetNameBuilder:
        ...
    def Tag(self) -> Tag: ...



class ToolingCloneparttype(enum.Enum):
    PrtType = 0
    SimType = 1
    FemType = 2
    FemIdealizedType = 3
    DrawingType = 4


class ToolingClonemethod(enum.Enum):
    UseLogFile = 0
    Rename = 2
    SaveAs = 3


class ToolingCloneaction(enum.Enum):
    InNative = 0
    ImportToTeamcenter = 1
    ExportToNative = 2
    InTeamcenter = 3


class ToolingApplicationstatus(enum.Enum):
    MoldwizardAndPdcwOff = 0
    MoldwizardOn = 1
    PdcastingWizardOn = 2


class ToolingApplication(enum.Enum):
    ReuseLibrary = 0
    MoldWizard = 1
    PdieWizard = 2
    StampingDie = 3
    ElectrodeWizard = 4
    EdieWizard = 5
    PdcastingWizard = 6


class SwapPartBuilder(Builder):
    def __init__(self) -> None: ...
    def SelectNewPartAsComponentButton(self) -> None:
        ...
    SelectBodyAndMakeLinkedBody: SelectNXObjectList
    SelectBodyInNewComponent: SelectNXObjectList


class SubInsertCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.SubInsertBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSubInsertBuilder(self) -> Tooling.SubInsertBuilder:
        ...
    def Tag(self) -> Tag: ...



class SubInsertBuilder(Builder):
    def __init__(self) -> None: ...
    def EditRegFile(self) -> None:
        ...
    def EditDatabase(self) -> None:
        ...
    InputParm: float
    Rename: bool
    SelFootType: Tooling.SubInsertBuilder.Shape
    SelectBotFace: SelectBodyList
    SelectHead: SelectBodyList
    Type: Tooling.SubInsertBuilder.Types


    class Types(enum.Enum):
        ParentOfSolidOwningPart = 0
        ProdPart = 1
        SolidOwningPart = 2
        CurrentWorkPart = 3
    

    class Shape(enum.Enum):
        Box = 0
        Cylinder = 1
    

class StripperVentingBuilder(Builder):
    def __init__(self) -> None: ...
    Length: Expression
    Radius: Expression
    SelectEdge: SelectEdgeList
    SelectObject: SelectNXObjectList
    Width: Expression
    WizardType: int


    class Types(enum.Enum):
        Create = 0
        Edit = 1
    

class StripLayoutStationInformationBuilder(Builder):
    def __init__(self) -> None: ...
    ColorPicker: NXColor
    ScaleFactor: float
    StationInformation: str
    StationNumber: Tooling.StripLayoutStationInformationBuilder.StationItem


    class StationItem(enum.Enum):
        One = 0
        Two = 1
        Three = 2
    

class StripLayoutCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.StripLayoutBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateStripLayoutBuilder(self) -> Tooling.StripLayoutBuilder:
        ...
    def CreateStripLayoutStationInformationBuilder(self) -> Tooling.StripLayoutStationInformationBuilder:
        ...
    def Tag(self) -> Tag: ...



class StripLayoutBuilder(Builder):
    def __init__(self) -> None: ...
    FromStation: Tooling.StripLayoutBuilder.FromStationType
    ToStation: Tooling.StripLayoutBuilder.ToStationType


    class ToStationType(enum.Enum):
        One = 0
        Two = 1
        Three = 2
    

    class FromStationType(enum.Enum):
        One = 0
        Two = 1
        Three = 2
    

class StockSizeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.StockSizeBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateStocksizeBuilder(self) -> Tooling.StockSizeBuilder:
        ...
    def Tag(self) -> Tag: ...



class StockSizeBuilder(Builder):
    def __init__(self) -> None: ...
    def ModifyRefCsys(self, inputOrigin: Point3d, inputMatrix: Matrix3x3) -> None:
        ...
    def CreateRefCsys(self, inputOrigin: Point3d, inputMatrix: Matrix3x3) -> None:
        ...
    def EditStockSizeAttr(self, workPart: NXObject) -> None:
        ...
    def UpdateBlankSizeString(self) -> None:
        ...
    def UpdateStockSizeString(self) -> None:
        ...
    def CalculateBoxSize(self, minPoint: Point3d, edgeLength: float, cysMatrix: Matrix3x3) -> None:
        ...
    def SetManipulatorOrientation(self, cysMatrix: Matrix3x3) -> None:
        ...
    def SetFitFaceStatus(self, fitFace: bool) -> None:
        ...
    def SetStockSizeObject(self, stock: NXObject) -> None:
        ...
    def ConvertStockDataToBuilder(self, stock: NXObject) -> None:
        ...
    Associative: bool
    AxisVector: Direction
    BlankPrecisionValue: float
    BlankSize: str
    Clearance: Expression
    ConnectionString: str
    CylinderType: Tooling.StockSizeBuilder.Cylinder
    InputSymmetricValue: bool
    IsClearanceAutoSet: bool
    OffsetNegativeX: float
    OffsetNegativeY: float
    OffsetNegativeZ: float
    OffsetPositiveX: float
    OffsetPositiveY: float
    OffsetPositiveZ: float
    RadialOffset: float
    RefCsys: CoordinateSystem
    RefCsysSelection: SelectCoordinateSystem
    ReferenceCsysType: Tooling.StockSizeBuilder.RefCsysType
    SelectBody: SelectBodyList
    ShowDiameterSymbol: bool
    SizePrecision: int
    StockType: Tooling.StockSizeBuilder.Shape
    StringStock: str
    Type: Tooling.StockSizeBuilder.Types


    class Types(enum.Enum):
        Block = 0
        Cylinder = 1
    

    class Shape(enum.Enum):
        Block = 0
        Cylinder = 1
    

    class RefCsysType(enum.Enum):
        Wcs = 0
        AbsoluteDisplayedPart = 1
        SelectedCSYS = 2
    

    class Cylinder(enum.Enum):
        Circumscribed = 0
        InscribedCircle = 1
    

class StandardPartPositionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.StandardPartPositionBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateStandardPartPositionBuilder(self) -> Tooling.StandardPartPositionBuilder:
        ...
    def Tag(self) -> Tag: ...



class StandardPartPositionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetOffsetPosition(self, position: Point3d) -> None:
        ...
    def SetFaceCenter(self) -> None:
        ...
    def PlaneView(self) -> None:
        ...
    def ReadStandardPartRecordFromConceptObject(self, conceptObject: NXObject) -> None:
        ...
    def InsertConceptObject(self, offsetPoint: Point3d, positionMatrix: Matrix3x3) -> None:
        ...
    def EditPositionOfConceptObject(self, offsetPoint: Point3d) -> None:
        ...
    def RepositionComponentOrSymbol(self, toPoint: Point3d, toMatrix: Matrix3x3) -> None:
        ...
    def SetStandardPartClientData(self, pClietData: Tooling.StandardPartData) -> None:
        ...
    def CreateLinkedPositionFace(self) -> None:
        ...
    def AddStandardPart(self) -> None:
        ...
    def UpdateAddedComponent(self, addedOcc: Assemblies.Component, offsetPoint: Point3d) -> None:
        ...
    def PerformCloneSetting(self, installationType: int, clonePartName: str) -> None:
        ...
    def GetConceptPartData(self) -> Tooling.ConceptStandardPartRecord:
        ...
    def SetConceptPartData(self, conceptPartData: Tooling.ConceptStandardPartRecord) -> None:
        ...
    AssociativePosition: bool
    DxIncrement: float
    DyIncrement: float
    OffsetPositionDx: Expression
    OffsetPositionDy: Expression
    ReferencePosition: Point


class StandardPartData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetSelectedStandardPartData(self, libName: str, libPath: str) -> None:
        ...
    def SetLastAccessedObject(self, catalogName: str, className: str, registerName: str) -> None:
        ...
    def GetRootStandardPartOccurrence(self) -> Assemblies.Component:
        ...
    def SetRootStandardPartOccurrence(self, partOccurrence: Assemblies.Component) -> None:
        ...
    def SetCreatedPartInstance(self, component: Assemblies.Component) -> None:
        ...
    def SetReferenceSetName(self, refsetName: str) -> None:
        ...
    def SetPositionMethod(self, positionMethod: str) -> None:
        ...
    def SetParentPart(self, parentPart: Part) -> None:
        ...
    def AnalyzePositionMethods(self, positionMethod: str) -> int:
        ...
    def SetDropData(self, entity: NXObject, position: Point3d) -> None:
        ...
    def SetReferenceSet(self, refsetIndex: int) -> None:
        ...
    def GetConceptStandardPartRecord(self, sheetData: Tooling.SpreadsheetData, fileContainer: str, assemblyName: str, assemblyPartNumber: str, assemblyItemType: str, childrenNames: str) -> Tooling.ConceptStandardPartRecord:
        ...
    def AssignConceptMoldBaseAttributes(self, moldBasePart: Part, fileContainer: str, assemblyName: str, assemblyPartNumber: str, assemblyItemType: str, childrenNames: str) -> None:
        ...
    def SetCurrentStandardPart(self, catalogName: str, className: str, registeredName: str) -> None:
        ...
    def SetIsToUseSymbol(self, useSymbol: bool) -> None:
        ...
    def SetIsToAddPocketToolBody(self, addPocketToolBody: bool) -> None:
        ...
    def SetDataToVersioned(self, partOccurrence: Assemblies.Component) -> None:
        ...
    def SetInitialWorkPart(self, initialWorkPart: Part) -> None:
        ...
    def GetCurrentConceptObject(self) -> NXObject:
        ...
    def SetCurrentConceptObject(self, conceptObject: NXObject) -> None:
        ...


class StandardPartCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.StandardPartBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateStandardPartBuilder(self) -> Tooling.StandardPartBuilder:
        ...
    def Tag(self) -> Tag: ...



class StandardPartBuilder(Builder):
    def __init__(self) -> None: ...
    def Help(self) -> None:
        ...
    def Reposition(self) -> None:
        ...
    def Flip(self) -> None:
        ...
    def RemoveComponent(self) -> None:
        ...
    def EditRegister(self) -> None:
        ...
    def EditDataBase(self) -> None:
        ...
    def ReadStandardPartClientDataFromLibrary(self, isFromMemberView: bool, dataType: int, libName: str, libPath: str) -> None:
        ...
    def ResetStandardPartClientData(self, dataType: int, libName: str, libPath: str) -> None:
        ...
    def ResetStandardPartClientDataWithLibraryName(self, libName: str) -> None:
        ...
    def GetStandardPartClientData(self) -> Tooling.StandardPartData:
        ...
    def SetStandardPartClientData(self, standardClientData: Tooling.StandardPartData) -> None:
        ...
    def GetSpreadsheetData(self) -> Tooling.SpreadsheetData:
        ...
    def SetSpreadsheetData(self, sheetData: Tooling.SpreadsheetData) -> None:
        ...
    def UpdateSpreadsheetDataWithObject(self, objectWithParameters: NXObject, isConcpetObject: bool, sheetData: Tooling.SpreadsheetData) -> None:
        ...
    def EditStandardPartDimensions(self, component: Assemblies.Component) -> None:
        ...
    def PerformPostProcessToAddedStandardPart(self, component: Assemblies.Component) -> None:
        ...
    def ChangeReferenceSet(self, component: Assemblies.Component, addToExtraRefset: bool, refsetName: str) -> None:
        ...
    def AddStandardPartsToPattern(self, patternPart: Part, fileName: str, refsetName: str, instanceName: str) -> typing.List[Assemblies.Component]:
        ...
    def EditConceptSymbols(self, conceptRecord: Tooling.ConceptStandardPartRecord, entities: typing.List[NXObject]) -> None:
        ...
    def AddConceptObjectsQuietly(self, positionMethod: str, conceptRecord: Tooling.ConceptStandardPartRecord) -> None:
        ...
    def RemoveComponent(self, component: Assemblies.Component) -> None:
        ...
    def RemoveMoldBase(self, component: Assemblies.Component) -> None:
        ...
    def RotateMoldBase(self, component: Assemblies.Component, angle: float) -> None:
        ...
    def UpdateConceptMoldBaseExpressions(self, conceptMoldBasePart: Part) -> None:
        ...
    def FlipComponent(self, component: Assemblies.Component) -> None:
        ...
    def InsertAddedStandardPartOccsItem(self, component: Assemblies.Component) -> None:
        ...
    def GetAddedStandardPartOccurrencesNumber(self) -> int:
        ...
    def GetAddedStandardPartOccurrenceItem(self, partOccIndex: int) -> Assemblies.Component:
        ...
    def RecommendMoldBaseSize(self) -> None:
        ...
    def RecommendMoldBasePlateHeight(self) -> None:
        ...
    def SetIsToAddNewMoldBase(self, isAddMoldBase: bool) -> None:
        ...
    def MateForPDWPunchInsert(self, positionType: int) -> None:
        ...
    def RepositionStandardPartSetForEDW(self) -> None:
        ...
    def ReadStandardPartDataFromConceptObject(self, conceptObject: NXObject) -> None:
        ...
    def GetAllConceptObjectInstances(self, conceptObject: NXObject, pInstanceObjects: typing.List[NXObject]) -> None:
        ...
    def BuildCloneObject(self, installationType: int, clonePartName: str) -> Tooling.CloneObject:
        ...
    def InitializePositionData(self, actionType: int) -> None:
        ...
    def FreePositionData(self) -> None:
        ...
    def GetConceptPartData(self) -> Tooling.ConceptStandardPartRecord:
        ...
    def SetConceptPartData(self, conceptPartData: Tooling.ConceptStandardPartRecord) -> None:
        ...
    def RemoveConceptObject(self, conceptObject: NXObject) -> None:
        ...
    def AnalyzePostionType(self, positionType: str, isReorientView: bool, positionPlane: NXObject, positionPoint: Point3d, positionMatrix: Matrix3x3) -> int:
        ...
    def PreparePositionDataForSmartPosition(self, acttionType: int) -> int:
        ...
    def AskPositionFace(self) -> NXObject:
        ...
    AssociativePosition: bool
    CompPattern: bool
    ConceptDesign: bool
    PointPattern: SelectNXObject
    PositioningFeature: SelectNXObject
    PositioningPlane: SelectNXObject
    ReferenceSet: Tooling.StandardPartBuilder.RefsetName
    RenameComponents: bool
    ShowInfoWindow: bool
    StandardPartComponent: SelectNXObject
    StandardPartEditType: Tooling.StandardPartBuilder.EditType


    class RefsetName(enum.Enum):
        True = 0
        False = 1
        EntirePart = 2
        Model = 3
    

    class EditType(enum.Enum):
        AddInstance = 0
        NewComponent = 1
        Modify = 2
    

class StandardPartBatchData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def Initialize(self) -> None:
        ...
    def SetCurrentSymbolOwningPart(self, owningPart: Part) -> None:
        ...
    def SetIncludeChildComponents(self, includeChildren: bool) -> None:
        ...
    def UpdateRecordValues(self, recordIndex: int, conceptObject: NXObject, instanceObjects: typing.List[NXObject]) -> None:
        ...
    def DeleteRecord(self, recordIndex: int) -> None:
        ...
    def ClearStandardPartRecords(self) -> None:
        ...
    def ClearConceptObjectsSet(self) -> None:
        ...


class StampingProcessRecognitionBuilder(Builder):
    def __init__(self) -> None: ...
    def AnalyzeBody(self) -> None:
        ...
    def ExportResult(self) -> None:
        ...
    def SetProductOrientation(self, matrix: Matrix3x3) -> None:
        ...
    def GetProductOrientation(self) -> Matrix3x3:
        ...
    def InitCostingData(self) -> None:
        ...
    def AskDefaultXmlFileName(self) -> str:
        ...
    def GetActivePage(self) -> int:
        ...
    def SetActivePage(self, activeTableIndex: int) -> None:
        ...
    def AskCurrentActiveDataProvider(self) -> Tooling.CostTableDataProvider:
        ...
    def UpdateProviderData(self, pDataProvider: Tooling.CostTableDataProvider, pCostObjects: typing.List[Tooling.CostDataObject]) -> None:
        ...
    def CollectCutoutObjects(self, pCostObjects: typing.List[Tooling.StampingProcessCutoutAreaData]) -> None:
        ...
    def CollectDrawingObjects(self, pCostObjects: typing.List[Tooling.StampingProcessDrawingAreaData]) -> None:
        ...
    def CollectBendingObjects(self, pCostObjects: typing.List[Tooling.StampingProcessBendingAreaData]) -> None:
        ...
    def CollectEmbossingObjects(self, pCostObjects: typing.List[Tooling.StampingProcessEmbossingAreaData]) -> None:
        ...
    def GroupStampingFeatures(self, costObject: typing.List[Tooling.CostDataObject]) -> Tooling.CostDataObject:
        ...
    def UngroupStampingFeature(self, costObjects: typing.List[Tooling.CostDataObject], ungroupedObjects: typing.List[Tooling.CostDataObject]) -> None:
        ...
    def DeleteStampingFeatures(self, costObjects: typing.List[Tooling.CostDataObject]) -> None:
        ...
    def AddStampingFeature(self) -> Tooling.CostDataObject:
        ...
    def CollectStageObjects(self, pCostObjects: typing.List[Tooling.StampingProcessInformationData]) -> None:
        ...
    BandFeed: float
    BandWidth: float
    BendingDataProvider: Tooling.CostTableDataProvider
    BodySurfaceArea: float
    CavityRotationVertical: bool
    CutoutDataProvider: Tooling.CostTableDataProvider
    CuttingLength: float
    DrawingDataProvider: Tooling.CostTableDataProvider
    EmbossingDataProvider: Tooling.CostTableDataProvider
    LeftRight: bool
    MinimumXDimension: float
    MinimumYDimension: float
    MinimumZDimension: float
    NumberX: int
    NumberY: int
    OverLapX: float
    OverLapY: float
    Paired: bool
    PartFolderBrowser: str
    PartVolume: float
    ProcessDataProvider: Tooling.CostTableDataProvider
    SaveAndExportStatus: bool
    SelectionBaseFace: SelectFace
    SheetMetalThickness: float
    ToolHeight: float
    ToolLength: float
    ToolName: str
    ToolWidth: float
    TypeOfCavityRotationVertical: int
    TypeOfLeftRight: int
    TypeOfPaired: int
    UnfoldedLength: float
    UnfoldedWidth: float
    XDimension: float
    XmlFileName: str
    XmlFolderBrowser: str
    YDimension: float
    ZDimension: float


class StampingProcessInformationData(Tooling.CostDataObject):
    def __init__(self) -> None: ...


class StampingProcessEmbossingAreaData(Tooling.CostDataObject):
    def __init__(self) -> None: ...


class StampingProcessDrawingAreaData(Tooling.CostDataObject):
    def __init__(self) -> None: ...


class StampingProcessCutoutAreaData(Tooling.CostDataObject):
    def __init__(self) -> None: ...


class StampingProcessBendingAreaData(Tooling.CostDataObject):
    def __init__(self) -> None: ...


class SpreadsheetDataParameter(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetValueList(self, paraValues: str) -> None:
        ...
    def HasStatus(self, parameterStatus: Tooling.SpreadsheetDataParameter.Status) -> bool:
        ...
    DescriptiveName: str
    ParameterName: str
    ParameterStatus: int
    ParameterValue: str


    class Status(enum.Enum):
        Lock = 1
        SystemKey = 2
        UserKey = 4
        HideStatus = 8
        ScaleItem = 16
        ReadOnly = 32
        Modified = 64
        ForceColor = 128
        HiddenValue = 256
        OptionValue = 512
        NonStandardValue = 1024
        ShipRule = 2048
    

class SpreadsheetData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def Close(self) -> None:
        ...
    def ReadData(self, spreadsheetFileName: str) -> None:
        ...
    def ReadData(self, familyPart: NXObject) -> None:
        ...
    def GetParameterValue(self, parameters: typing.List[Tooling.SpreadsheetDataParameter]) -> None:
        ...
    def SelectPrimaryParameter(self, parameterName: str, parameterValue: str) -> None:
        ...
    def EditParameter(self, parameterName: str, parameterValue: str) -> None:
        ...
    def SetParameterStatus(self, parameterName: str, parameterStatus: int, isAdd: bool) -> None:
        ...
    def SearchRecords(self, searchConditions: str) -> None:
        ...
    def AddAssociatedObject(self, associatedObject: NXObject) -> None:
        ...
    def Update(self) -> None:
        ...
    def UpdateModel(self, doUpdateImmediately: bool, updatePartAttribute: bool) -> None:
        ...
    def GetDefinedAttributesExpressions(self, keywordType: Tooling.SpreadsheetData.KeywordType, objOrPartAttrNames: str, attrNames: str, attrValues: str) -> None:
        ...
    def GetParameterValueList(self, parameterName: str, paraValues: str) -> None:
        ...
    def SelectPrimaryParameterWithResult(self, parameterName: str, parameterValue: str) -> str:
        ...


    class ParameterStatus(enum.Enum):
        Lock = 1
        SystemKey = 2
        UserKey = 4
        HideStatus = 8
        ScaleItem = 16
        ReadOnly = 32
        Modified = 64
        ForceColor = 128
        HiddenValue = 256
        OptionValue = 512
    

    class KeywordType(enum.Enum):
        ObjectAttribute = 1
        PartAttribute = 2
        Expression = 4
    

class SplitSolidCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.SplitSolidBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSplitSolidBuilder(self) -> Tooling.SplitSolidBuilder:
        ...
    def Tag(self) -> Tag: ...



class SplitSolidBuilder(Builder):
    def __init__(self) -> None: ...
    def SetEnlargedSurfaceData(self, enlargedSurfaceData: float) -> None:
        ...
    IsEnlarge: bool
    ReverseTrimDirection: bool
    SplitObject: SelectNXObject
    SplitPlane: Plane
    SplitTarget: SelectBody
    SurfaceRange: GeometricUtilities.SurfaceRangeBuilder
    ToolOption: Tooling.SplitSolidBuilder.ToolObjectOption
    Type: Tooling.SplitSolidBuilder.OperationType


    class ToolObjectOption(enum.Enum):
        ExistingObject = 0
        NewPlane = 1
    

    class OperationType(enum.Enum):
        Split = 0
        Trim = 1
    

class SplitInsertBuilder(Builder):
    def __init__(self) -> None: ...
    def SaveAndGetComponentParent(self, componentTag: NXObject) -> NXObject:
        ...
    def GetComponentFullName(self, componentTag: NXObject) -> str:
        ...
    def GetComponentOrigin(self, componentTag: NXObject) -> Point3d:
        ...
    def GetComponentTransform(self, componentTag: NXObject) -> Matrix3x3:
        ...
    def PrepairToSplitInsert(self) -> None:
        ...
    def FindLinkedBodyFeatureAndSource(self, featureType: str, featureNameSubString: str) -> None:
        ...
    def FindLinkedBodyFeatureAndSourceForAll(self) -> None:
        ...
    def ReverseTrimAndRelinkSourceAndCreateUDOForAll(self, sourceObjects: typing.List[NXObject]) -> None:
        ...
    def SetLinkFeatureAndSourceObject(self, sourceObjectsOld: typing.List[NXObject]) -> None:
        ...
    KeepOriginal: bool
    RenameComponent: bool
    SelectComponent: Assemblies.SelectComponentList
    SplittingCurves: Section
    SplittingDirection: bool
    WizardType: int


class SpindleSliderBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteSpindleSlider(self, spindleSliderName: str) -> None:
        ...
    DriveBody: SelectNXObjectList
    DriveVector: Direction
    SpindleSliderBody: SelectNXObjectList
    SpindleSliderName: str
    SpindleSliderVector: Direction


class SpecifyCircuitCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.SpecifyCircuitBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.SpecifyCircuitBuilder:
        ...
    def Tag(self) -> Tag: ...



class SpecifyCircuitBuilder(Builder):
    def __init__(self) -> None: ...
    def CheckStatus(self) -> None:
        ...
    def GetCircuitColor(self) -> float:
        ...
    def SetCircuitColor(self, circuitColor: float) -> None:
        ...
    def GetOneCircuit(self, channels: typing.List[Body]) -> None:
        ...
    def InitializeCircuitSetData(self) -> None:
        ...
    def CreateCoolingFittingData(self) -> Tooling.CoolingFittingData:
        ...
    def GetCoolingFittingData(self) -> Tooling.CoolingFittingData:
        ...
    def AddADeselectedFittingPoint(self, aFittingPoint: Point) -> None:
        ...
    def RemoveADeselectedFittingPoint(self, aFittingPoint: Point) -> None:
        ...
    def SetCoolingNodeInfo(self) -> None:
        ...
    def CreateManualLinkList(self, arrowList: int) -> None:
        ...
    def SetIntersectionAndInletInfo(self, selectedChannel: Body, arrowList: Point3d) -> None:
        ...
    def CreateStartArrow(self, nodeId: int, radius: float, closestPoint: Point3d, faceVec: Vector3d) -> None:
        ...
    def SetCircuitTreeNodeUpdate(self, nodeIndex: int, isUpdate: bool) -> None:
        ...
    def SetSpecifiedCircuitColor(self, nodeIndex: int, nodeColor: int) -> None:
        ...
    def SetChannelType(self, channelType: str) -> None:
        ...
    def RemoveOneFittingPoint(self, nodeIndex: int, aPoint: Point) -> None:
        ...
    def SetExistingFittingPointDataDetails(self, fittingPts: typing.List[Point], channelDiameters: str, currentNames: str, currentTypes: str, currentFitTypes: str, baffleLengths: str, fittingPointModified: bool, partNumbersTc: str) -> None:
        ...
    def SetCircuitSelNode(self, circuitSelNode: int) -> None:
        ...
    def RemoveParametersInLinkList(self, removeArrowAtIntersect: bool, removeStartArrow: bool, removeCreateBody: bool, removeFittingPoint: bool, emptyStartStructure: bool, doUpdate: bool) -> None:
        ...
    def EmptyNewFittingPoint(self, nodeIndex: int) -> None:
        ...
    def SetCircuitTreeNodeName(self, nodeIndex: int, nodeName: str) -> None:
        ...
    def RemoveLabel(self, nodeIndex: int, labelTag: NXObject) -> None:
        ...
    def RemoveOneCoolingArrow(self, nodeIndex: int, arrowTag: NXObject) -> None:
        ...
    def BlankArrowsAtEachIntersection(self, nodeIndex: int) -> None:
        ...
    def BlankArrows(self, nodeIndex: int, isBlank: bool) -> None:
        ...
    def CreateArrowAtIntersection(self, nodeIndex: int) -> None:
        ...
    def RemoveAttributesAndTemporaryData(self, nodeTag: typing.List[NXObject]) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use RemoveTemporaryData instead.")"""
        ...
    def ClearStartCollectorData(self) -> None:
        ...
    def AddAttachedChannelToChannelList(self, attachedChannel: Body) -> None:
        ...
    def AddDeletePointToDelPointList(self, deleteFitPoint: Point) -> None:
        ...
    def RedisplayArrow(self, circuitNode: int) -> None:
        ...
    def SetBlindEnd(self, isBlind: bool) -> None:
        ...
    def RemoveTemporaryData(self, nodeIds: int) -> None:
        ...
    def AddInstance(self, coolingPart: Assemblies.Component, fittingPoint: Point) -> None:
        ...
    def SetAllBodies(self, bodies: typing.List[Body]) -> None:
        ...
    def CreatePointsWithBoundary(self) -> None:
        ...
    BoundaryBody: SelectBodyList
    ChannelColor: NXColor
    CircuitColor: NXColor
    CoolingStandardPart: SelectNXObject
    CreateFittings: bool
    InletChannel: SelectBodyList
    KeepCircuit: bool
    Layer: int
    OutletChannel: SelectBody
    SearchBoundaryBodies: bool
    UseSymbol: bool


class SpecifyBaffleCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.SpecifyBaffleBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.SpecifyBaffleBuilder:
        ...
    def Tag(self) -> Tag: ...



class SpecifyBaffleBuilder(Builder):
    def __init__(self) -> None: ...
    def GetChannelColor(self, redValue: float, greenValue: float, blueValue: float) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use Tooling.SpecifyBaffleBuilder.ChannelColor instead.")"""
        ...
    def SetChannelColor(self, redValue: float, greenValue: float, blueValue: float) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use Tooling.SpecifyBaffleBuilder.ChannelColor instead.")"""
        ...
    def SetColorModified(self, modified: bool) -> None:
        ...
    AttributeType: Tooling.SpecifyBaffleBuilder.AttributeTypes
    ChannelColor: NXColor
    ChannelType: str
    Channels: SelectBodyList
    Layer: int


    class AttributeTypes(enum.Enum):
        BodyAsChannel = 0
        BodyAsBaffle = 1
    

class SpecialPiercingInsertBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateDatumPlane(self) -> None:
        ...
    def SetWCSForSpecialPiercingInsert(self, needPrecisionValue: bool) -> None:
        ...
    def WaveFacesOfSelectedCurves(self, rootPart: Part, instanceTag: NXObject) -> None:
        ...
    def WaveSelectedCurves(self) -> None:
        ...
    def GetWaveLinkedCurves(self, linkedCurves: typing.List[Curve]) -> None:
        ...
    def CreateOffsetDatumPlane(self) -> None:
        ...
    def GetProfile(self, sectionTag: Section, profiles: typing.List[Curve]) -> None:
        ...
    def GetCorrectEdgeInNewPart(self, partTag: Part, sourceEdge: Edge) -> Edge:
        ...
    def WaveFacesAndFillHole(self, rootPart: Part, instanceTag: NXObject) -> None:
        ...
    def GetCorrectFacesOfExtractRegionFeature(self, faces: typing.List[Face]) -> None:
        ...
    def SetBoxMatrixAndPosition(self, matrix: Matrix3x3, position: Point3d) -> None:
        ...
    def CalculateBoxSize(self) -> None:
        ...
    def AddInsertPartIntoAssembly(self, parentPart: NXObject, templatePartName: str, origin: Point3d) -> NXObject:
        ...
    def GetHoleBoundaryFaceAndCreatePatchOpenings(self, edges: typing.List[NXObject]) -> NXObject:
        ...
    def CreateKFBoundBox(self, wcsMatrix: Matrix3x3, clearance: float, faces: typing.List[NXObject]) -> NXObject:
        ...
    def CreateIntersect(self, targetBody: NXObject, bodyOfKFBoundBox: NXObject) -> None:
        ...
    def WaveIntersectBodyToNewDieInsertPart(self, bodies: typing.List[NXObject]) -> None:
        ...
    def DeleteSelectedInsertAndWaveLinkedSource(self) -> None:
        ...
    def SuppressAllFeatureAfter(self, featureTag: NXObject, suppressChildren: bool) -> None:
        ...
    BoundBox: Tooling.SpecialPiercingInsertBuilder.BoundBoxType
    BoxPosition: Point3d
    EndLimit: Expression
    InsertPosition: Tooling.SpecialPiercingInsertBuilder.InsertPositionTypes
    Is3DCurves: bool
    NormalBbpslug: Tooling.SpecialPiercingInsertBuilder.NormalBottomBackingPlateSlugType
    NormalCavity: Tooling.SpecialPiercingInsertBuilder.NormalCavityType
    NormalClearance: float
    NormalDsslug: Tooling.SpecialPiercingInsertBuilder.NormalDieShoeSlugType
    NormalOffsetSide: Tooling.SpecialPiercingInsertBuilder.NormalOffsetSideType
    NormalSlugPara1: float
    NormalSlugPara2: float
    NormalSlugPara3: float
    NormalSlugPara4: float
    OffsetLinearDimension: Expression
    OffsetValueLinearDimensionNegativeX: Expression
    OffsetValueLinearDimensionNegativeY: Expression
    OffsetValueLinearDimensionNegativeZ: Expression
    OffsetValueLinearDimensionPositiveX: Expression
    OffsetValueLinearDimensionPositiveY: Expression
    OffsetValueLinearDimensionPositiveZ: Expression
    ParentPart: Tooling.SpecialPiercingInsertBuilder.ParentPartTypes
    ParentPartName: str
    PlateClearanceFirst: float
    PlateClearanceFourth: float
    PlateClearanceSecond: float
    PlateClearanceThird: float
    PunchOrDie: Tooling.SpecialPiercingInsertBuilder.PunchOrDieTypes
    RadialOffset: Expression
    RenameComponent: bool
    SelectCurves: Section
    SelectEdges: SelectEdgeList
    SelectFace: SelectFaceList
    SelectInsert: SelectNXObjectList
    SelectVector: Direction
    SlugHoleHeightLinearDimension: Expression
    StandardOrUserDefined: Tooling.SpecialPiercingInsertBuilder.StandardOrUserDefinedTypes
    StartLimit: Expression
    Type: Tooling.SpecialPiercingInsertBuilder.Types
    UsePlateClearanceFirst: bool
    UsePlateClearanceFourth: bool
    UsePlateClearanceSecond: bool
    UsePlateClearanceThird: bool
    WizardType: int


    class Types(enum.Enum):
        Create = 0
        Edit = 1
        Delete = 2
    

    class StandardOrUserDefinedTypes(enum.Enum):
        Standard = 0
        UserDefined = 1
    

    class PunchOrDieTypes(enum.Enum):
        Punch = 0
        Die = 1
        DieCavityAndSlugHole = 2
    

    class ParentPartTypes(enum.Enum):
        ProjectDie = 0
        ProjectDieBase = 1
        ProjectSubDieBase = 2
    

    class NormalOffsetSideType(enum.Enum):
        PunchSide = 0
        DieSide = 1
    

    class NormalDieShoeSlugType(enum.Enum):
        Fillet = 0
        Rectangle = 1
        Circle = 2
        Mickey = 3
        Clearance = 4
        SlotVer = 5
        SlotHor = 6
        None = 7
    

    class NormalCavityType(enum.Enum):
        TaperAngle = 0
        Step = 1
    

    class NormalBottomBackingPlateSlugType(enum.Enum):
        Fillet = 0
        Rectangle = 1
        Circle = 2
        Mickey = 3
        Clearance = 4
        SlotVer = 5
        SlotHor = 6
        None = 7
    

    class InsertPositionTypes(enum.Enum):
        Top = 0
        Bottom = 1
    

    class BoundBoxType(enum.Enum):
        BoundedBlock = 0
        BoundedCylinder = 1
    

class SpecialFormingBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateFormingInsert(self) -> None:
        ...
    def SetBoxMatrixAndPosition(self, matrix: Matrix3x3, position: Point3d) -> None:
        ...
    def CalculateBoxSize(self) -> None:
        ...
    def SewWaveLinkedFaceAndGuidedExtensionSheet(self) -> None:
        ...
    def CreateBoundBox(self) -> None:
        ...
    def EditBoundBox(self) -> None:
        ...
    def ExtrudeCurvesToTrueBodyAndFalseBody(self) -> None:
        ...
    def EditExtrudeCurves(self) -> None:
        ...
    def TrimTrueBodyWithSewedSheet(self) -> None:
        ...
    def MoveObjectsToUndisplayableLayer(self) -> None:
        ...
    def AssignClearance(self) -> None:
        ...
    def AddInsertPartIntoAssembly(self, parentPart: NXObject, templatePartName: str, origin: Point3d) -> NXObject:
        ...
    def SetFormingRegion(self, faces: typing.List[NXObject]) -> None:
        ...
    def WaveFormingRegion(self) -> None:
        ...
    def CreateOffsetDatumPlaneForSketch(self) -> None:
        ...
    def AssignAttributeForSketchFeature(self, sketchFeatureTag: NXObject) -> None:
        ...
    def DeleteSelectedInsert(self) -> None:
        ...
    BoundedBlockOrUserDefined: Tooling.SpecialFormingBuilder.BlockType
    BoxClearance: float
    BoxPosition: Point3d
    EndLimit: Expression
    FirstClearance: float
    InsertType: Tooling.SpecialFormingBuilder.PunchOrDie
    IsEditGuidedExtension: bool
    NeedFirstClearance: bool
    NeedSecondClearance: bool
    NeedThirdClearance: bool
    OffsetValueLinearDimensionNegativeX: Expression
    OffsetValueLinearDimensionNegativeY: Expression
    OffsetValueLinearDimensionNegativeZ: Expression
    OffsetValueLinearDimensionPositiveX: Expression
    OffsetValueLinearDimensionPositiveY: Expression
    OffsetValueLinearDimensionPositiveZ: Expression
    Parent: Tooling.SpecialFormingBuilder.ParentValue
    RenameComponent: bool
    SecondClearance: float
    SelectCurves: Section
    SelectFace: ScCollector
    SelectFormingBlock: SelectBody
    SelectInsertToDelete: SelectNXObjectList
    SelectSheetBody: SelectBody
    StartLimit: Expression
    ThirdClearance: float
    Type: Tooling.SpecialFormingBuilder.Types
    UseExistingSheetBody: bool
    WithoutFalseBody: bool
    WizardType: int


    class Types(enum.Enum):
        CreateBasicInsert = 0
        ExtendCurveAndCreateBox = 1
        TrimInsert = 2
        ModifyInsert = 3
        DeleteInsert = 4
    

    class PunchOrDie(enum.Enum):
        Punch = 0
        Die = 1
    

    class ParentValue(enum.Enum):
        PrjDie = 0
        PrjDb = 1
        PrjSub = 2
    

    class BlockType(enum.Enum):
        BoundedBlock = 0
        UserDefined = 1
    

class SolidPatchCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.SolidPatchBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.SolidPatchBuilder:
        ...
    def Tag(self) -> Tag: ...



class SolidPatchBuilder(Builder):
    def __init__(self) -> None: ...
    def ShowResult(self) -> None:
        ...
    def AddListPartToPatchData(self, selectedListString: str) -> None:
        ...
    Patch: SelectBodyList
    PatchType: Tooling.SolidPatchBuilder.SolidPatchType
    Product: SelectBody
    Subtract: bool


    class SolidPatchType(enum.Enum):
        SolidPatch = 0
        LinkBody = 1
    

class SmartScrewUpdateBuilder(Builder):
    def __init__(self) -> None: ...
    ParentNode: Tooling.SmartScrewUpdateBuilder.ParentOption
    Type: Tooling.SmartScrewUpdateBuilder.Types


    class Types(enum.Enum):
        UpdateSmartScrew = 0
        CopyPartFamilyPart = 1
        DeletePartFamilyPart = 2
    

    class ParentOption(enum.Enum):
        NoParent = 0
    

class SlugRetentionBuilder(Builder):
    def __init__(self) -> None: ...
    AngularDimension: Expression
    CuttingClearance: Expression
    CuttingDistance: Expression
    OffsetDirection: Direction
    OffsetDistance: float
    PreviousWorkPart: Part
    RadiusDimension: Expression
    RotateDirection: Direction
    SelectComponent: Assemblies.SelectComponent
    SelectDataFile: str
    SelectObject: SelectNXObjectList
    SelectPoint: Point
    SlugEdgeForTypeTwo: Edge
    SlugRetentionBooleanData: GeometricUtilities.BooleanOperation
    SlugRetentionEdge: SelectEdge
    SlugRetentionFeature: Features.Feature
    TargetBodyForSubtract: Body
    Type: Tooling.SlugRetentionBuilder.Types


    class Types(enum.Enum):
        TypeFirst = 0
        TypeSecond = 1
        Edit = 2
    

class SIZERImportBuilder(Builder):
    def __init__(self) -> None: ...
    def GenerateMotorModel(self, motorType: str) -> BasePart:
        ...
    def CreateMcdLogical(self, referenceDesignator: str) -> Mechatronics.LogicObject:
        """[Obsolete("Deprecated in NX1926.0.0.  Use NXOpen.Mechatronics.ImportSelectedMotorsBuilder.CreateMcdLogical instead. Please remember to remove Mechatronics including header files when deleting this method.")"""
        ...
    def EditMcdLogical(self, logicalNode: Mechatronics.LogicObject, newPartOccs: typing.List[Assemblies.Component], parameterData: typing.List[Mechatronics.LogicObjectBuilder.ParameterData]) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  Use NXOpen.Mechatronics.ImportSelectedMotorsBuilder.EditMcdLogical instead. Please remember to remove Mechatronics including header files when deleting this method.")"""
        ...
    InputFile: str
    PositionMethod: Tooling.SIZERImportBuilder.PositionMode


    class PositionMode(enum.Enum):
        InferredOnly = 0
        AbsoluteOrigin = 1
        SelectOrigin = 2
        ByConstraints = 3
        Move = 4
    

class SIZERExportBuilder(Builder):
    def __init__(self) -> None: ...
    def GetRunMode(self) -> Tooling.SIZERExportBuilder.RunMode:
        """[Obsolete("Deprecated in NX1926.0.0.  This method has no replacement. It is no longer supported anymore.")"""
        ...
    def SetRunMode(self, runMode: Tooling.SIZERExportBuilder.RunMode) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  This method has no replacement. It is no longer supported anymore.")"""
        ...
    def GetMechanicalData(self, mechanicalData: typing.List[Tooling.SIZERExportBuilder.MechanicalData]) -> None:
        ...
    def SetMechanicalData(self, mechanicalData: typing.List[Tooling.SIZERExportBuilder.MechanicalData]) -> None:
        ...
    def GetMcdMechanicalData(self, mechanicalData: typing.List[Tooling.SIZERExportBuilder.MCDMechanicalData]) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  Use NXOpen.Mechatronics.ExportLoadCurveBuilder.GetMcdMechanicalData instead")"""
        ...
    def SetMcdMechanicalData(self, mechanicalData: typing.List[Tooling.SIZERExportBuilder.MCDMechanicalData]) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  Use NXOpen.Mechatronics.ExportLoadCurveBuilder.SetMcdMechanicalData instead")"""
        ...
    def ProcessMcdSimulationData(self, startTime: float, endTime: float) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  Use NXOpen.Mechatronics.ExportLoadCurveBuilder.ProcessMcdSimulationData instead")"""
        ...
    OutputFile: str


    class RunMode(enum.Enum):
        None = 0
        Motion = 1
        Mcd = 2
    

    class SIZERExportBuilderMechanicalData():
        Id: int
        Name: str
        Solution: Motion.MotionSolution
        TorqueGraph: Motion.Graph
        SpeedGraph: Motion.Graph
        FrictionTorque: float
        SystemEfficiency: float
        LoadInertia: float
        AdditionalInertia: float
        def ToString(self) -> str:
            ...
    

    class SIZERExportBuilderMCDMechanicalData():
        Id: int
        Name: str
        AxisControl: Mechatronics.PhysicsConstraint
        ReferenceDesignator: str
        FrictionTorque: float
        SystemEfficiency: float
        LoadInertia: float
        AdditionalInertia: float
        def ToString(self) -> str:
            ...
    

    class SIZERExportBuilder_MechanicalData():
        id: int
        name: int
        solution: Tag
        torqueGraph: Tag
        speedGraph: Tag
        frictionTorque: float
        systemEfficiency: float
        loadInertia: float
        additionalInertia: float
    

    class SIZERExportBuilder_MCDMechanicalData():
        id: int
        name: int
        axisControl: Tag
        referenceDesignator: int
        frictionTorque: float
        systemEfficiency: float
        loadInertia: float
        additionalInertia: float
    

class SIZERCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.SIZERExportBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateExportBuilder(self) -> Tooling.SIZERExportBuilder:
        ...
    def CreateImportBuilder(self) -> Tooling.SIZERImportBuilder:
        ...
    def Tag(self) -> Tag: ...



class ShimInnerProfileSetBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Tooling.ShimInnerProfileSetBuilder]) -> None:
        ...
    def Append(self, object: Tooling.ShimInnerProfileSetBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Tooling.ShimInnerProfileSetBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Tooling.ShimInnerProfileSetBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Tooling.ShimInnerProfileSetBuilder) -> None:
        ...
    def Erase(self, obj: Tooling.ShimInnerProfileSetBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Tooling.ShimInnerProfileSetBuilder]:
        ...
    def SetContents(self, objects: typing.List[Tooling.ShimInnerProfileSetBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Tooling.ShimInnerProfileSetBuilder, object2: Tooling.ShimInnerProfileSetBuilder) -> None:
        ...
    def Insert(self, location: int, object: Tooling.ShimInnerProfileSetBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ShimInnerProfileSetBuilder(Builder):
    def __init__(self) -> None: ...
    RoughOffset: bool
    SlugHoleProfile: ScCollector
    SlugHoleProfileOffset: Expression


class ShimBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateInnerProfileSetBuilder(self) -> Tooling.ShimInnerProfileSetBuilder:
        ...
    def GetItemName(self, itemName: int) -> None:
        ...
    def SetItemName(self, itemName: int) -> None:
        ...
    Height: Expression
    InsertToDelete: Assemblies.SelectComponentList
    InsertToEdit: Assemblies.SelectComponent
    OffsetOuterDistance: Expression
    OuterRoughOffset: bool
    ParentNode: Tooling.ShimBuilder.ParentOption
    ParentPartName: str
    RenameToggle: bool
    ShimFace: SelectFaceList
    SideAttributeValue: Tooling.ShimBuilder.SideAttributeValues
    SlugholeProfile: Tooling.ShimInnerProfileSetBuilderList
    Type: Tooling.ShimBuilder.Types
    WizardType: int


    class Types(enum.Enum):
        AddInsert = 0
        EditInsert = 1
        DeleteInsert = 2
    

    class SideAttributeValues(enum.Enum):
        None = 0
        Top = 1
        Middle = 2
        Bottom = 3
    

    class ParentOption(enum.Enum):
        NoParent = 0
    

class SheetMetalFeatureRecognitionBuilder(Builder):
    def __init__(self) -> None: ...
    def AnalyzeBody(self) -> None:
        ...
    def ExportResult(self) -> None:
        ...
    def SetProductOrientation(self, matrix: Matrix3x3) -> None:
        ...
    def GetProductOrientation(self) -> Matrix3x3:
        ...
    def InitCostingData(self) -> None:
        ...
    def AskDefaultXmlFileName(self) -> str:
        ...
    def GetActivePage(self) -> int:
        ...
    def SetActivePage(self, activeTableIndex: int) -> None:
        ...
    def AskCurrentActiveDataProvider(self) -> Tooling.CostTableDataProvider:
        ...
    def UpdateProviderData(self, pDataProvider: Tooling.CostTableDataProvider, pCostObjects: typing.List[Tooling.CostDataObject]) -> None:
        ...
    def CollectCutoutObjects(self, pCostObjects: typing.List[Tooling.CutoutAreaData]) -> None:
        ...
    def CollectDrawingObjects(self, pCostObjects: typing.List[Tooling.DrawingAreaData]) -> None:
        ...
    def CollectBendingObjects(self, pCostObjects: typing.List[Tooling.BendingAreaData]) -> None:
        ...
    def CollectEmbossingObjects(self, pCostObjects: typing.List[Tooling.EmbossingAreaData]) -> None:
        ...
    def GroupStampingFeatures(self, costObject: typing.List[Tooling.CostDataObject]) -> Tooling.CostDataObject:
        ...
    def UngroupStampingFeature(self, costObjects: typing.List[Tooling.CostDataObject], ungroupedObjects: typing.List[Tooling.CostDataObject]) -> None:
        ...
    def DeleteStampingFeatures(self, costObjects: typing.List[Tooling.CostDataObject]) -> None:
        ...
    def AddStampingFeature(self) -> Tooling.CostDataObject:
        ...
    def PerformQuickAnalysis(self) -> None:
        ...
    def AssignFeatureFaceColor(self, assignOrRestore: bool) -> None:
        ...
    def ReleaseAllProductFeatureData(self) -> None:
        ...
    def DeleteAllCostRelatedUDO(self) -> None:
        ...
    def CheckBodyFacesNumber(self, numberFaces: int) -> bool:
        ...
    BendingDataProvider: Tooling.CostTableDataProvider
    BodySurfaceArea: float
    CutoutDataProvider: Tooling.CostTableDataProvider
    CuttingLength: float
    DrawingDataProvider: Tooling.CostTableDataProvider
    EmbossingDataProvider: Tooling.CostTableDataProvider
    MinimumXDimension: float
    MinimumYDimension: float
    MinimumZDimension: float
    PartFolderBrowser: str
    PartVolume: float
    SaveAndExportStatus: bool
    SelectionBaseFace: SelectFace
    SheetMetalThickness: float
    TypeOfStampingPart: int
    UnfoldedLength: float
    UnfoldedWidth: float
    XDimension: float
    XmlFileName: str
    XmlFolderBrowser: str
    YDimension: float
    ZDimension: float


class SetPressModelBuilder(Builder):
    def __init__(self) -> None: ...
    def SetPressModelName(self, pressModelName: str) -> None:
        ...
    def InitializeAvailablePressModels(self, pressModelPath: str) -> None:
        ...
    NameSuffix: str
    PressModelPath: str
    StrokesPerMinute: float
    TargetDirectory: str


class SelectReuseLibraryListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Tooling.SelectReuseLibraryListItemBuilder]) -> None:
        ...
    def Append(self, object: Tooling.SelectReuseLibraryListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Tooling.SelectReuseLibraryListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Tooling.SelectReuseLibraryListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Tooling.SelectReuseLibraryListItemBuilder) -> None:
        ...
    def Erase(self, obj: Tooling.SelectReuseLibraryListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Tooling.SelectReuseLibraryListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Tooling.SelectReuseLibraryListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Tooling.SelectReuseLibraryListItemBuilder, object2: Tooling.SelectReuseLibraryListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Tooling.SelectReuseLibraryListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SelectReuseLibraryListItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    SelectReuseItem: Tooling.SelectReuseLibraryItemBuilder


class SelectReuseLibraryListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateListItem(self) -> Tooling.SelectReuseLibraryListItemBuilder:
        ...
    ItemName: str
    ReuseItemList: Tooling.SelectReuseLibraryListItemBuilderList


class SelectReuseLibraryItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    DescriptiveName: str
    FamilyMemberName: str
    Selection: str


class SectionLineCreationBuilder(Builder):
    def __init__(self) -> None: ...
    def ReverseVector(self) -> None:
        ...
    def PointSubFunction(self) -> None:
        ...
    def RemoveLast(self, curveTag: Line) -> None:
        ...
    def RemoveAll(self, curveList: typing.List[Line]) -> None:
        ...
    def CreateTemporaryLine(self, pointData: Point3d, direction: Vector3d) -> Line:
        ...
    SelectPoint: Point
    VectorDefineDirection: Direction


class ScrapDesignCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ScrapDesignBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateScrapDesignBuilder(self) -> Tooling.ScrapDesignBuilder:
        ...
    def Tag(self) -> Tag: ...



class ScrapDesignBuilder(Builder):
    def __init__(self) -> None: ...
    def GetOvercutPosition(self) -> Point3d:
        ...
    def SetOvercutPosition(self, overcutPosition: Point3d) -> None:
        ...
    def ScrapDesignCreate(self) -> None:
        ...
    def ScrapDesignEdit(self) -> None:
        ...
    def ScrapDesignAddon(self) -> None:
        ...
    def ScrapDesignGroup(self) -> None:
        ...
    AddonOperation: Tooling.ScrapDesignBuilder.AddonType
    ApplyColor: bool
    AssignColor: NXColor
    AttachEdge: SelectEdgeList
    AttachScrap: SelectBody
    BoundaryList: ScCollector
    ChangeColScrap: SelectBodyList
    CurveList: Section
    DefStationNum: int
    DoubleA: float
    DoubleAngle: float
    DoubleB: float
    DoubleH: float
    DoubleR: float
    DoubleRf: float
    EditMethod: Tooling.ScrapDesignBuilder.EditScrapType
    EditStationNum: int
    ExistScrap: SelectBodyList
    HoleColor: NXColor
    MinRad: float
    OvercutColor: NXColor
    OvercutEdge: SelectEdge
    OvercutOperation: Tooling.ScrapDesignBuilder.OvercutType
    OverlapColor: NXColor
    OverlapWidth: float
    PierceType: Tooling.ScrapDesignBuilder.DefScrapType
    PiercingColor: NXColor
    PilotingColor: NXColor
    ProcessFive: float
    ProcessFour: float
    ProcessOne: float
    ProcessThree: float
    ProcessTwo: float
    RemoveFilter: Tooling.ScrapDesignBuilder.RemoveType
    ScrapMethod: Tooling.ScrapDesignBuilder.ScrapDefType
    ScrapPosition: Tooling.ScrapDesignBuilder.ScrapDefPosition
    ScrapTol: float
    ScrapTypeEnum: Tooling.ScrapDesignBuilder.Body
    SecondScrap: SelectBodyList
    SplitCurve: Section
    SplitScrap: SelectBodyList
    TrimNum: Tooling.ScrapDesignBuilder.TrimNumType
    TrimmingColor: NXColor
    Update: bool
    UserAddonCurve: Section


    class TrimNumType(enum.Enum):
        One = 0
        Two = 1
        Three = 2
        Four = 3
        Five = 4
    

    class ScrapDefType(enum.Enum):
        BlankBoundarySketch = 0
        HoleBoundary = 1
        ClosedCurves = 2
        BoundaryLines = 3
        ExistedSheetBody = 4
        ChangeType = 5
    

    class ScrapDefPosition(enum.Enum):
        ProjectToStrip = 0
        KeepOrigin = 1
    

    class RemoveType(enum.Enum):
        InferScrap = 0
        Overlap = 1
        Overcut = 2
        Trimming = 3
        Hole = 4
        Scrap = 5
        All = 6
    

    class OvercutType(enum.Enum):
        NormalType = 0
        TangentType = 1
        CircularType = 2
        RectangularType = 3
        FilletType = 4
    

    class EditScrapType(enum.Enum):
        Split = 0
        Merge = 1
        ApplyMinimumRadius = 2
        ChangeStation = 3
        Delete = 4
        Update = 5
    

    class DefScrapType(enum.Enum):
        Piercing = 0
        Piloting = 1
    

    class Body(enum.Enum):
        Create = 0
        Edit = 1
        Addon = 2
        Grouping = 3
    

    class AddonType(enum.Enum):
        Overlap = 0
        Overcut = 1
        Trimming = 2
        UserDefined = 3
    

class RunSimulationBuilder(Builder):
    def __init__(self) -> None: ...
    def GotoStart(self) -> None:
        ...
    def Previous(self) -> None:
        ...
    def PlayBackwards(self) -> None:
        ...
    def Play(self) -> None:
        ...
    def Next(self) -> None:
        ...
    def GotoEnd(self) -> None:
        ...
    def Stop(self) -> None:
        ...
    def CollisionConfiguration(self) -> None:
        ...
    def CollisionInformation(self) -> None:
        ...
    def ResetIgnoredCollision(self) -> None:
        ...
    AngleExpression: Expression
    CheckCollision: bool
    ClearanceCollision: float
    CollisionCheckOption: Tooling.RunSimulationBuilder.CollisionCheckOptions
    EndAngle: float
    GotoRun: float
    HighlightCollision: bool
    IgnoreTouching: bool
    IntervalDimension: Expression
    StartAngle: float
    StopCheckCollision: bool
    TimeExpression: Expression


    class CollisionCheckOptions(enum.Enum):
        FacetBodyDistance = 0
        MeshTriangleIntersection = 1
        SolidBodyIntersection = 2
    

class RunnerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.RunnerBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateRunnerBuilder(self) -> Tooling.RunnerBuilder:
        ...
    def CreateRunnerBuilder(self, runnerFeature: Features.BodyFeature) -> Tooling.RunnerBuilder:
        ...
    def Tag(self) -> Tag: ...



class RunnerBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteRunner(self) -> None:
        ...
    def EditRegisterFile(self) -> None:
        ...
    def EditDataBase(self) -> None:
        ...
    def GetDataFromRunnerFeature(self, sheetData: Tooling.SpreadsheetData) -> None:
        ...
    def ImportTemplate(self) -> None:
        ...
    def UpdateGuideLoops(self) -> None:
        ...
    def ReadSectionDataFromDatabase(self, sectionTypes: str) -> None:
        ...
    def SetParameterTreeData(self, sheetData: Tooling.SpreadsheetData) -> None:
        ...
    def ReadSelectedSectionData(self, sectionName: str) -> None:
        ...
    def StoreSectionParameters(self) -> None:
        ...
    def EditTemplateExpression(self) -> None:
        ...
    def UpdateTemplatePart(self) -> None:
        ...
    def UpdateGuideOrientation(self) -> None:
        ...
    BooleanOperation: GeometricUtilities.BooleanOperation
    EndShape: Tooling.RunnerBuilder.GuideEndType
    GuideLines: Section
    RunnerBodies: SelectBodyList
    SectionOffset: Expression
    SectionShape: Tooling.RunnerBuilder.SectionType
    SectionVector: Direction
    TransMotion: GeometricUtilities.ModlMotion


    class SectionType(enum.Enum):
        Circular = 0
        Parabolic = 1
        Trapezoidal = 2
        Hexagonal = 3
        SemiCircular = 4
    

    class GuideEndType(enum.Enum):
        Both = 0
        StartOnly = 1
        EndOnly = 2
        None = 3
    

class Runner(Features.BodyFeature):
    def __init__(self) -> None: ...


class RibsData(Tooling.CostDataObject):
    def __init__(self) -> None: ...
    def AskChildrenFeatures(self, ribs: typing.List[Tooling.RibsData]) -> None:
        ...


class ReusePositioningObjectBuilder(Builder):
    def __init__(self) -> None: ...
    def LoadPart(self, partFileName: str) -> None:
        ...
    def RepositionBody(self, target: Point3d, orient: Matrix3x3, twoPickPositionMode: bool, onlyMovePoints: bool) -> None:
        ...
    def CreateSketch(self, dropFace: NXObject, position: Point3d) -> None:
        ...
    def GetSketchFromFeatureSet(self) -> None:
        ...
    def DeletePoint(self, point: Point) -> None:
        ...
    def EditPoint(self, point: Point, value: float, isXValue: bool) -> None:
        ...
    def EditPoint(self, point: Point, xvalue: float, yvalue: float) -> None:
        ...
    def AddPoints(self) -> None:
        ...
    def AddPoint(self, pointCoords: Point3d) -> Point:
        ...
    def CreatePointInSketch(self) -> None:
        ...
    def GetFeatureSetAttributes(self) -> bool:
        ...
    def SetPointsInSketch(self) -> None:
        ...
    def GetNonStandardPoints(self, points: typing.List[Point3d]) -> bool:
        ...
    def SetNonStandardPoints(self, points: typing.List[Point3d], isAbsolute: bool) -> None:
        ...
    def SetSketchActive(self, sketch: Sketch) -> None:
        ...
    def AddPointOnNonPlanar(self, pointCoords: Point3d) -> Point:
        ...
    def EditPointOnPlanar(self, point: Point, value: float, isUValue: bool) -> Point:
        ...
    def CreateCsysOnNonPlanar(self) -> None:
        ...
    def EditPointOnPlanar(self, point: Point, uValue: float, vValue: float) -> Point:
        ...
    def SetTrimToFaceEdgesOption(self, trimToFaceEdges: bool) -> None:
        ...
    def SetExtendToFaceEdgesOption(self, extendToFaceEdges: Tooling.ReusePositioningObjectBuilder.CurveExtendToFace) -> None:
        ...
    def TrimCurveFaceEdges(self, trimToFaceEdges: bool) -> None:
        ...
    def ExtendCurveFaceEdges(self, extendToFaceEdges: bool) -> None:
        ...
    def SetBaseFaceForSection(self, collTag: ScCollector) -> None:
        ...
    def FlipOffsetCurveDirection(self) -> None:
        ...
    def OffsetCurveOnFace(self, offsetValue: str) -> None:
        ...
    def FreeOcfApplicationData(self) -> None:
        ...
    def SetSelectedCurveCollector(self, section: Section) -> None:
        ...
    def GetOffsetCsysPattern(self) -> NXObject:
        ...
    def GetAllDatumCsys(self, datumCsys: typing.List[CoordinateSystem]) -> None:
        ...
    def FindSeedCsysFromPattern(self, csysPattern: NXObject) -> CoordinateSystem:
        ...
    def GetCsysFromFeatureSet(self) -> None:
        ...
    def CreateOffsetCsysFromSeed(self) -> Features.Feature:
        ...
    def UpdateQuickCsysPattern(self) -> None:
        ...
    def UpdateDatumCsysByType(self) -> None:
        ...
    def DeselectNonPlanarObject(self, delselectedObjs: typing.List[NXObject]) -> None:
        ...
    def AddNewPoint(self, pointCoords: Point3d) -> None:
        ...
    def DeletePointCoordinates(self, type: int, pointCoords: typing.List[Point3d]) -> None:
        ...
    def EditPointCoordinates(self, type: int, oldPoint: Point3d, newPoint: Point3d) -> None:
        ...
    def RepositionSketchPoints(self, target: Point3d, orient: Matrix3x3) -> None:
        ...
    def InitializeWcsLocation(self, saveOldCsys: bool) -> None:
        ...
    def SetAllPointCoordinates(self) -> None:
        ...
    def SelectBaseFace(self, collTag: ScCollector) -> None:
        ...
    def FlipCurveDirection(self) -> None:
        ...
    def TrimCurve(self, trimToFaceEdges: bool) -> None:
        ...
    def ExtendCurve(self, extendToFaceEdges: bool) -> None:
        ...
    def OffsetDistance(self, offsetValue: str) -> None:
        ...
    def NonPlanarDeselect(self, delselectedObjs: typing.List[NXObject]) -> None:
        ...
    def SyncSectionData(self, section: Section) -> None:
        ...
    Angle: str
    ColumnNumber: str
    CurvePercentage: str
    DataFile: str
    DialogOption: Tooling.ReusePositioningObjectBuilder.DialogOptions
    Distribution: bool
    DropObject: NXObject
    DynamicCsysOrientation: Matrix3x3
    DynamicCsysOrigin: Point3d
    EditFeatureGroup: Features.Feature
    EndingUValue: str
    EndingVValue: str
    ExtendToFaceEdgesOption: Tooling.ReusePositioningObjectBuilder.CurveExtendToFace
    ImportedSketch: Sketch
    InitialPasteLocation: Point3d
    Length: str
    LibraryName: str
    MultipleFaceCollector: ScCollector
    NewPoint: Point
    OffsetCsysData: Tooling.OffsetDatumCsysBuilder
    OffsetCsysFromQuick: CoordinateSystem
    OffsetDatumCsys: Features.Feature
    OffsetValue: str
    QuickCsysData: Tooling.QuickDatumCsysBuilder
    ReferenceCsysPattern: NXObject
    RowNumber: str
    SeedDatumCsys: CoordinateSystem
    SelectedCurve: bool
    SelectedCurveCollector: Section
    SelectedNonPlanarFace: bool
    SketchPoint: Section
    StartingUValue: str
    StartingVValue: str
    SubType: Tooling.ReusePositioningObjectBuilder.SubTypes
    TrimToFaceEdgesOption: bool
    Type: Tooling.ReusePositioningObjectBuilder.Types
    UPercentage: str
    UpdatedParameter: bool
    UseFaceCenterAsLocation: bool
    UseOnePickPositionMethod: bool
    UseProjectPoint: bool
    VPercentage: str
    Width: str


    class Types(enum.Enum):
        PatternLinear = 0
        PatternCircular = 1
        ImportedData = 2
        EditSketch = 3
        EditMode = 9
        QuickCsys = 7
        OffsetCsysPattern = 8
        PlanarPattern = 4
        NonPlanarPattern = 5
        CurvePattern = 6
    

    class SubTypes(enum.Enum):
        PlanarPatternLinear = 0
        PlanarPatternCircular = 1
        EditSketch = 2
        NonPlanarPattern = 3
        NonPlanarGeneral = 4
    

    class DialogOptions(enum.Enum):
        FromToolbar = 0
        FromDialog = 1
        ImportPart = 2
        ToolingTemplate = 3
        FromExpression = 4
        ReusableObject = 5
    

    class CurveTrim(enum.Enum):
        None = 0
        WithinSection = 1
    

    class CurveExtendToFace(enum.Enum):
        None = 0
        Boundary = 1
    

class ReusablePocketCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ReusablePocketBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateReusablePocketBuilder(self) -> Tooling.ReusablePocketBuilder:
        ...
    def Tag(self) -> Tag: ...



class ReusablePocketBuilder(Builder):
    def __init__(self) -> None: ...
    def AddToolComponent(self, component: NXObject) -> None:
        ...
    def DeletePocket(self, component: NXObject) -> None:
        ...
    def BreakLink(self, component: NXObject) -> None:
        ...
    def CreatePocket(self, component: NXObject) -> None:
        ...
    def RemoveToolComponent(self, component: NXObject) -> None:
        ...
    def SetHoleType(self, component: NXObject, holeType: Tooling.ReusablePocketBuilder.Hole) -> None:
        ...
    def AddTargetBody(self, component: NXObject, targetBody: NXObject) -> None:
        ...
    def RemoveTargetBody(self, component: NXObject, targetBody: NXObject) -> None:
        ...
    def SetStandard(self, component: NXObject, standard: str) -> None:
        ...
    def SetForm(self, component: NXObject, form: str) -> None:
        ...
    def SetScrewType(self, component: NXObject, screwType: str) -> None:
        ...
    def SetFit(self, component: NXObject, fit: str) -> None:
        ...
    def SetReference(self, component: NXObject, reference: str) -> None:
        ...
    def SetCounterboreDiameter(self, component: NXObject, counterboreDiameter: float) -> None:
        ...
    def SetCountersunkDiameter(self, component: NXObject, countersunkDiameter: float) -> None:
        ...
    def SetDiameter(self, component: NXObject, diameter: float) -> None:
        ...
    def VerifyHoleSeries(self, component: NXObject) -> None:
        ...
    def RecreateHoleSeries(self, component: NXObject, feature: NXObject) -> None:
        ...
    def HandleHolePackageBuilderInReset(self) -> None:
        ...
    AutoTarget: bool
    ThreadHole: bool


    class Hole(enum.Enum):
        Series = 0
        Subtract = 1
        None = 2
    

class ReusableObjectPasteBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSpreadsheetData(self) -> Tooling.SpreadsheetData:
        ...
    def SetSpreadsheetData(self, spreadsheetData: Tooling.SpreadsheetData) -> None:
        ...
    def UpdateSpreadsheetData(self) -> None:
        ...
    def RepositionBody(self, target: Point3d, orient: Matrix3x3, twoPickPositionMode: bool) -> None:
        ...
    def SetLibraryInformation(self, feature: NXObject, libraryName: str, relativePath: str) -> None:
        ...
    def LoadPart(self, partFileName: str, dropEntity: NXObject, loadedObjects: typing.List[NXObject]) -> None:
        ...
    def GetCreatedObjects(self, createdObjects: typing.List[NXObject]) -> None:
        ...
    def CreatePatternObjects(self, createPattern: bool) -> None:
        ...
    def UpdateLocation(self) -> None:
        ...
    def LoadReusableObject(self, partFileName: str, spreadsheetFileName: str, dropEntity: NXObject, dropLocation: Point3d, pasteMethod: Tooling.ReusableObjectPasteBuilder.PasteMethods, spreadsheetData: Tooling.SpreadsheetData, loadedObjects: typing.List[NXObject]) -> None:
        ...
    def UpdatePullFace(self) -> None:
        ...
    Associative: bool
    DropFace: NXObject
    DynamicCsysOrientation: Matrix3x3
    DynamicCsysOrigin: Point3d
    EditFeatureGroup: NXObject
    ImportedSketch: NXObject
    InitialPasteLocation: Point3d
    LibraryName: str
    PasteMethod: Tooling.ReusableObjectPasteBuilder.PasteMethods
    PatternFeature: NXObject
    PatternSketch: Sketch
    PositioningFeatSet: Features.Feature
    TargetBody: NXObject
    TargetFace: NXObject
    UseOnePickPositionMethod: bool


    class PasteMethods(enum.Enum):
        None = 0
        Add = 1
        Subtract = 2
        Userdefined = 3
        Solidpunch = 4
    

class ReusableObjectManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def CreatePasteBuilder(self) -> Tooling.ReusableObjectPasteBuilder:
        ...
    def CreatePositioningBuilder(self) -> Tooling.ReusePositioningObjectBuilder:
        ...
    def CreatePositioningBuilder(self, positioningObject: Features.Feature) -> Tooling.ReusePositioningObjectBuilder:
        ...
    def CreateQuickDatumCsysBuilder(self) -> Tooling.QuickDatumCsysBuilder:
        ...
    def CreateOffsetDatumCsysBuilder(self) -> Tooling.OffsetDatumCsysBuilder:
        ...
    def Tag(self) -> Tag: ...



class ReusableObject(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetObjects(self) -> typing.List[NXObject]:
        ...
    def SetObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    ContainerFile: str
    DescriptiveName: str
    IsSavedInOriginalPart: bool
    ObjectGroupName: str
    PartFile: str
    PreviewImageFile: str


class ReplaceSolidCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ReplaceSolidBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateReplaceSolidBuilder(self) -> Tooling.ReplaceSolidBuilder:
        ...
    def Tag(self) -> Tag: ...



class ReplaceSolidBuilder(Builder):
    def __init__(self) -> None: ...
    def EditBox(self) -> None:
        ...
    def ReverseFaceDirectionCallBack(self, faceEid: NXObject, state: int) -> None:
        ...
    def UpdateForFaceChange(self) -> None:
        ...
    def UpdateFaceListState(self, faceEid: NXObject, reverse: int, faceForBoxFlag: int, action: int) -> None:
        ...
    def GetBoundedBoxBuilder(self) -> Features.ToolingBoxBuilder:
        ...
    def SetBoundedBoxBuilder(self, boxBuilder: Features.ToolingBoxBuilder) -> None:
        ...
    BoundingBoxBuilder: Tooling.CreateBoxBuilder
    BoxFaceToggle: bool
    Clearance: Expression
    FaceReverseDirection: bool
    RemoveParameter: bool
    SelFace: SelectFaceList


class RenameAndExportComponentBuilder(Builder):
    def __init__(self) -> None: ...
    def RenameComponents(self, partTag: NXObject, dirName: str, newPartName: str) -> None:
        ...
    def SetSearchFolderListForExportDrawingFiles(self, folderList: str) -> None:
        ...
    def ExportComponents(self, partTag: NXObject, assemblyInFolderWithPath: str, outputDir: str) -> None:
        ...
    def ExportSingleComponent(self, assemblyPartNameWithPath: str, outputDir: str) -> None:
        ...
    def GetDrawingFilesInFolder(self, assemblyPartToExport: NXObject, assemblyInFolderWithPath: str, outputDir: str, onlyGetDrawingFilesNotExport: bool, drawingFilesNeedExport: str) -> None:
        ...
    def ReplaceComponent(self, componentTag: NXObject, newComponentNameWithPath: str) -> None:
        ...
    AddFolderToSearch: str
    DefineBy: Tooling.RenameAndExportComponentBuilder.DefinitionType
    DeleteOldComponentsToggle: bool
    ExportDrawingFile: bool
    ListChildrenComponents: bool
    LoadOption: Tooling.RenameAndExportComponentBuilder.LoadOptionType
    NeedChangeDisplayPartBack: bool
    NewNameRule: Tooling.RenameAndExportComponentBuilder.NamingRuleType
    NewStringInName: str
    NextPartNameNumber: int
    OldStringInName: str
    OutputDiretory: str
    PartDirectory: str
    PrefixOrSuffixString: str
    SelectAssemblyInFolder: str
    SelectAssemblyToExport: SelectNXObject
    SelectComponentToRename: SelectNXObjectList
    ToolingNameRule: str
    Type: Tooling.RenameAndExportComponentBuilder.Types
    WizardType: int


    class Types(enum.Enum):
        RenameCompoent = 0
        ExportAssembly = 1
    

    class NamingRuleType(enum.Enum):
        None = 0
        Prefix = 1
        Suffix = 2
        ReplaceString = 3
        ToolingNameRule = 4
    

    class NameRuleType(enum.Enum):
        Default = 0
    

    class LoadOptionType(enum.Enum):
        FromFolder = 0
        FromSearchFolder = 1
    

    class DefinitionType(enum.Enum):
        Directory = 0
        RootPart = 1
        Selection = 2
    

class RemoveHolesBuilder(Builder):
    def __init__(self) -> None: ...
    def AddHolesData(self, edges: typing.List[Edge], faces: typing.List[Face]) -> None:
        ...
    def SetHighlight(self, object: NXObject, highlight: bool) -> None:
        ...
    def RemoveHoleData(self, holeName: str) -> None:
        ...
    def ClearHoleData(self) -> None:
        ...
    BodySelection: ScCollector
    FaceToPatch: ScCollector
    HoleFace: ScCollector
    MergeOutput: bool
    SelectionType: Tooling.RemoveHolesBuilder.SelectionTypes


    class SelectionTypes(enum.Enum):
        Body = 0
        Face = 1
    

class ReliefDesignCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ReliefDesignBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateReliefDesignBuilder(self) -> Tooling.ReliefDesignBuilder:
        ...
    def Tag(self) -> Tag: ...



class ReliefDesignBuilder(Builder):
    def __init__(self) -> None: ...
    def SetFaces(self, faceOccs: typing.List[Face]) -> None:
        ...
    def WaveFaces(self) -> None:
        ...
    def DeleteLinkedFace(self) -> None:
        ...
    Clearance: float
    Clearance1: Expression
    Clearance2: Expression
    Clearance3: Expression
    Clearance4: Expression
    Clearance5: Expression
    Clearance6: Expression
    CopyRelief: SelectBodyList
    CreateEditMethod: Tooling.ReliefDesignBuilder.Method
    CreateLocation: bool
    CurveSuperSelect: Section
    DeleteMethod: Tooling.ReliefDesignBuilder.MethodOfDelete
    HideReliefStatus: bool
    NumberOfCopy: int
    Pitch: float
    ReliefFace: ScCollector
    ReliefHeight: Expression
    ReliefRadius: Expression
    ReliefStart: Expression
    SelectionReliefToEdit: SelectNXObject
    Type: Tooling.ReliefDesignBuilder.Types


    class Types(enum.Enum):
        Create = 0
        Edit = 1
        Copy = 2
        Delete = 3
    

    class MethodOfDelete(enum.Enum):
        DeleteSelectedInstance = 0
        DeleteAllInstances = 1
    

    class Method(enum.Enum):
        BBox = 0
        UDef = 1
    

class ReferenceCopyBuilder(Builder):
    def __init__(self) -> None: ...
    def BeginDrag(self) -> None:
        ...
    def Drag(self) -> None:
        ...
    def EndDrag(self) -> None:
        ...
    BodyMotionType: Tooling.ReferenceCopyBuilder.BodyMotionTypes
    CloneObject: Tooling.CloneObject
    ComponentMotionType: Tooling.ReferenceCopyBuilder.ComponentMotionTypes
    CopyBodySelection: SelectBody
    CopyComponentSelection: Assemblies.SelectComponent
    DestinationCsys: CoordinateSystem
    DestinationFace: SelectFace
    FromCsys: CoordinateSystem
    FromFace: SelectFace
    ManipulatorMatrix: Matrix3x3
    ManipulatorOrigin: Point3d
    MoveHandlesOnly: bool
    NewComponent: bool
    NumberOfBodies: int
    NumberOfComponents: int
    RotateAngle: float
    RotateVector: Axis
    Type: Tooling.ReferenceCopyBuilder.Types


    class Types(enum.Enum):
        Component = 0
        Body = 1
    

    class ComponentMotionTypes(enum.Enum):
        Dynamic = 0
        CSYSToCSYS = 1
        Angle = 2
        FaceToFace = 3
    

    class BodyMotionTypes(enum.Enum):
        Dynamic = 0
        CSYSToCSYS = 1
        Angle = 2
        FaceToFace = 3
    

class ReferenceBlendCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ReferenceBlendBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateReferenceBlendBuilder(self) -> Tooling.ReferenceBlendBuilder:
        ...
    def Tag(self) -> Tag: ...



class ReferenceBlendBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateReferenceBlend(self) -> TaggedObject:
        ...
    SelectionEdge: ScCollector
    SelectionFace: ScCollector


class RasterImageBuilder(Display.RasterImageBuilder):
    def __init__(self) -> None: ...
    def UpdateBuilderDataFromImage(self, annotImageTag: Annotations.DraftingImage) -> None:
        ...
    def SetViewOfAnchorPoint(self, insertPointView: View) -> None:
        ...


class RasterImage(Display.ImageBase):
    def __init__(self) -> None: ...


class QuickQuotationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.QuickQuotationBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateQuickQuotationBuilder(self) -> Tooling.QuickQuotationBuilder:
        ...
    def Tag(self) -> Tag: ...



class QuickQuotationBuilder(Builder):
    def __init__(self) -> None: ...
    def DatumPlane(self) -> None:
        ...
    def TemplateConfig(self) -> None:
        ...
    BendingColor: NXColor
    BlankSize: float
    BurringColor: NXColor
    CamunitColor: NXColor
    CompFactor: float
    Customer: str
    DesignHours: float
    DesignPrice: float
    DistanceX: float
    DistanceY: float
    FormingColor: NXColor
    InsertGroupMaterial: Tooling.QuickQuotationBuilder.InsertGroupMaterials
    ManageTemporaryObjectsType: Tooling.QuickQuotationBuilder.ManageTemporaryObjectsTypes
    MaterialUtil: str
    ObjectType: Tooling.QuickQuotationBuilder.ObjectTypes
    OutlineEnlargeTimes: float
    PartNo: int
    PartsAmout: int
    PiercingColor: NXColor
    Pitch: float
    QuoteDate: str
    QuoteNo: str
    Quoter: str
    SelOutline: Section
    SelSheetBody: SelectBodyList
    StationsNo: int
    StripLength: float
    StripMaterial: str
    StripThickness: float
    Type: Tooling.QuickQuotationBuilder.Types
    Width: float
    WorkAreaLength: float
    WorkAreaWidth: float


    class Types(enum.Enum):
        JobInformation = 0
        ProjectDefinition = 1
        ConceptDesign = 2
        Grouping = 3
        Quoting = 4
    

    class ObjectTypes(enum.Enum):
        Piercing = 0
        Bending = 1
        Forming = 2
        Burring = 3
        Cam = 4
    

    class ManageTemporaryObjectsTypes(enum.Enum):
        Hide = 0
        Display = 1
        Delete = 2
    

    class InsertGroupMaterials(enum.Enum):
        Cr12 = 0
        Cr12MoV = 1
    

    class DesignTypes(enum.Enum):
        NewDesign = 0
        Changeover = 1
        AdditionalDie = 2
    

class QuickDatumCsysBuilder(Builder):
    def __init__(self) -> None: ...
    def GetAlignVector(self) -> Tooling.QuickDatumCsysBuilder.AlignVectors:
        ...
    def SetAlignVector(self, alignVector: Tooling.QuickDatumCsysBuilder.AlignVectors) -> None:
        ...
    def GetReferenceDiameter(self) -> float:
        ...
    def SetReferenceDiameter(self, referenceDiameter: float) -> None:
        ...
    def GetOffset(self) -> float:
        ...
    def SetOffset(self, offset: float) -> None:
        ...
    def GetSeedCsys(self) -> CoordinateSystem:
        ...
    def SetSeedCsys(self, seedCsys: CoordinateSystem) -> None:
        ...
    def GetOffsetCsys(self) -> CoordinateSystem:
        ...
    def SetOffsetCsys(self, offsetCsys: CoordinateSystem) -> None:
        ...
    def GetCsys(self) -> typing.List[CoordinateSystem]:
        ...
    def RemoveEdges(self, edges: typing.List[Edge]) -> None:
        ...
    def SetEdges(self, edges: typing.List[Edge]) -> None:
        ...
    def SetCsys(self, csys: typing.List[CoordinateSystem]) -> None:
        ...
    def UpdateOffsetCsys(self) -> None:
        ...


    class AlignVectors(enum.Enum):
        X = 0
        NegativeX = 1
        Y = 2
        NegativeY = 3
        Z = 4
        NegativeZ = 5
    

class PunchInsertBuilder(Builder):
    def __init__(self) -> None: ...
    def StandardPunchInsert(self) -> None:
        ...
    def PunchEditOffsetValueTable(self) -> None:
        ...
    def NormalCreateUDP(self) -> None:
        ...
    def AddStandardPunchInsert(self) -> None:
        ...
    def EditOffsetSpreadsheet(self) -> None:
        ...
    AutomaticFitToggle: bool
    DifferentPenetration: bool
    IncludePilotScrap: bool
    InsertPunchType: Tooling.PunchInsertBuilder.InsertPunchTypeEnum
    MinimumLength: float
    MinimumRadius: float
    NewPartNames: str
    NormalClearance: float
    NormalClearanceOption: Tooling.PunchInsertBuilder.NormalClearanceOptionTypeItems
    NormalOffsetSide: Tooling.PunchInsertBuilder.NormalOffsetSideTypeItems
    NormalOnePunchToggle: bool
    NormalPunchLength: str
    NormalRenameDialog: bool
    NormalSelectPiercePunch: SelectBodyList
    OffsetSpreadsheet: str
    ParentPartName: str
    Position: Tooling.PunchInsertBuilder.InsertPositionItems
    PunchInsertTag: TaggedObject
    PunchOffsetValue: float
    PunchPocketClearanceForBackingPlate: float
    PunchPocketClearanceForPunchPlate: float
    PunchPocketClearanceForStripperPlate: float
    PunchPocketHeightInStripperPlate: float
    PunchPocketToggleForBackingPlate: bool
    PunchPocketToggleForPunchPlate: bool
    PunchPocketToggleForStripperPlate: bool
    PunchPocketTypeInBackingPlate: Tooling.PunchInsertBuilder.PunchPocketTypeItemsBackingPlate
    PunchPocketTypeInPunchPlate: Tooling.PunchInsertBuilder.PunchPocketTypeItemsPunchPlate
    PunchPocketTypeInStripperPlate: Tooling.PunchInsertBuilder.PunchPocketTypeItemsStripperPlate
    PunchSameOffsetValue: bool
    SelectAllScrapsToggle: bool
    SelectAttributeSpreadsheet: str
    SelectScrap: SelectBodyList
    SelectSketch: SelectSketch
    StandardBPToggle: bool
    StandardClearanceBP: float
    StandardClearancePP: float
    StandardClearanceSP: float
    StandardPPToggle: bool
    StandardPartClassificationName: str
    StandardPunchTag: TaggedObject
    StandardSPToggle: bool
    UserDefinedPunchEnd: Expression
    UserDefinedPunchPenetration: float
    UserDefinedPunchStart: Expression


    class PunchPocketTypeItemsStripperPlate(enum.Enum):
        Clearance = 0
        Fillet = 1
        Circle = 2
        SuperOffset = 3
    

    class PunchPocketTypeItemsPunchPlate(enum.Enum):
        Clearance = 0
        Fillet = 1
        Circle = 2
        SuperOffset = 3
    

    class PunchPocketTypeItemsBackingPlate(enum.Enum):
        Clearance = 0
        Fillet = 1
        Circle = 2
        SuperOffset = 3
    

    class NormalOffsetSideTypeItems(enum.Enum):
        DieSide = 0
        PunchSide = 1
    

    class NormalClearanceOptionTypeItems(enum.Enum):
        Constant = 0
        Variable = 1
        SuperOffset = 2
    

    class InsertPunchTypeEnum(enum.Enum):
        Standard = 0
        UserDesign = 1
    

    class InsertPositionItems(enum.Enum):
        Top = 0
        Bottom = 1
    

class ProgressiveDieManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def CreateRemoveHolesBuilder(self) -> Tooling.RemoveHolesBuilder:
        ...
    def CreateRunSimulationBuilder(self) -> Tooling.RunSimulationBuilder:
        ...
    def CreateDefineCamBuilder(self) -> Tooling.DefineCamBuilder:
        ...
    def CreateDefineLifterBuilder(self) -> Tooling.DefineLifterBuilder:
        ...
    def CreateBackingPadBuilder(self) -> Tooling.BackingPadBuilder:
        ...
    def CreateSlugRetentionBuilder(self, featureSet: Features.FeatureGroup) -> Tooling.SlugRetentionBuilder:
        ...
    def CreateGeneralInsertBuilder(self) -> Tooling.GeneralInsertBuilder:
        ...
    def CreateChamferingInsertBuilder(self) -> Tooling.ChamferingInsertBuilder:
        ...
    def CreateLetteringInsertBuilder(self) -> Tooling.LetteringInsertBuilder:
        ...
    def CreateHemFixerBuilder(self, featureSet: Features.FeatureGroup) -> Tooling.HemFixerBuilder:
        ...
    def CreateShimBuilder(self) -> Tooling.ShimBuilder:
        ...
    def CreateShimInnerProfileSetBuilder(self) -> Tooling.ShimInnerProfileSetBuilder:
        ...
    def CreateStripperVentingBuilder(self, featureSet: Features.FeatureGroup) -> Tooling.StripperVentingBuilder:
        ...
    def CreateUnfoldingSimulationBuilder(self) -> Tooling.UnfoldingSimulationBuilder:
        ...
    def CreateDieInsertBuilder(self) -> Tooling.DieInsertBuilder:
        ...
    def CreateDieCavityAndSlugHoleBuilder(self) -> Tooling.DieCavityAndSlugHoleBuilder:
        ...
    def CreatePunchInsertBuilder(self) -> Tooling.PunchInsertBuilder:
        ...
    def CreateInsertBlockBuilder(self) -> Tooling.InsertBlockBuilder:
        ...
    def CreatePiercingInsertMiniToolsBuilder(self) -> Tooling.PiercingInsertMiniToolsBuilder:
        ...
    def CreateSmartScrewUpdateBuilder(self) -> Tooling.SmartScrewUpdateBuilder:
        ...
    def CreateSpecialPiercingInsertBuilder(self) -> Tooling.SpecialPiercingInsertBuilder:
        ...
    def CreateSpecialFormingBuilder(self) -> Tooling.SpecialFormingBuilder:
        ...
    def CreateHoleDatumSymbolBuilder(self) -> Tooling.HoleDatumSymbolBuilder:
        ...
    def CreateRenameAndExportComponentBuilder(self) -> Tooling.RenameAndExportComponentBuilder:
        ...
    def CreateInsertEditToolsBuilder(self) -> Tooling.InsertEditToolsBuilder:
        ...
    def CreateUserDefinedMotionBuilder(self) -> Tooling.UserDefinedMotionBuilder:
        ...
    def CreateSplitInsertBuilder(self) -> Tooling.SplitInsertBuilder:
        ...
    def CreateConceptDieBaseBuilder(self) -> Tooling.ConceptDieBaseBuilder:
        ...
    def CreateSwapPartBuilder(self) -> Tooling.SwapPartBuilder:
        ...
    def CreateAddCommentBuilder(self) -> Tooling.AddCommentBuilder:
        ...
    def CreateTrackingCurveBuilder(self) -> Tooling.TrackingCurveBuilder:
        ...
    def CreateProcessSimulationBuilder(self) -> Tooling.ProcessSimulationBuilder:
        ...
    def CreateFormingSimulationResultDisplayBuilder(self) -> Tooling.FormingSimulationResultDisplayBuilder:
        ...
    def Tag(self) -> Tag: ...



class ProfileSplitCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ProfileSplitBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateProfileSplitBuilder(self) -> Tooling.ProfileSplitBuilder:
        ...
    def Tag(self) -> Tag: ...



class ProfileSplitBuilder(Builder):
    def __init__(self) -> None: ...
    def StTraverse(self) -> None:
        ...
    DefAssociative: bool
    DefVector: Direction
    ExtDist1: Expression
    ExtDist2: Expression
    SelectBody: SelectBodyList
    SelectProfile: Section


class ProcessSimulationBuilder(Builder):
    def __init__(self) -> None: ...
    def InitRunSimulation(self) -> None:
        ...
    def OnCheckCollision(self) -> None:
        ...
    def SimulationPlay(self) -> None:
        ...
    def ClearRunSimulation(self) -> None:
        ...
    def StopSimulation(self) -> None:
        ...
    def GotoStart(self) -> None:
        ...
    def GotoEnd(self) -> None:
        ...
    def DisplayIntervalUpdate(self) -> float:
        ...
    def GotoToAngle(self) -> float:
        ...
    def InitCollisionCheck(self) -> None:
        ...
    def ExportSimControlData(self) -> None:
        ...
    AngleExpression: Expression
    CheckPrecision: Tooling.ProcessSimulationBuilder.CollisionCheckPrecision
    ClearanceCollision: float
    CollisionCheckOption: Tooling.ProcessSimulationBuilder.CollisionCheckOptions
    CurrentAngleIndex: int
    EndAngle: float
    ExportControlData: str
    GotoRun: float
    IntervalDimension: Expression
    IsDone: bool
    IsInitCheck: bool
    IsSingleStep: bool
    IsStepForward: bool
    IsValidExportPath: bool
    LoadCollisions: str
    NeedCheckCollision: bool
    PreviousAngleIndex: int
    SecondsPerStroke: float
    StartAngle: float
    TimeExpression: Expression


    class CollisionCheckPrecision(enum.Enum):
        One = 0
        Two = 1
        Three = 2
        Four = 3
        DefaultValue = 4
        Fiv = 5
        Ten = 6
    

    class CollisionCheckOptions(enum.Enum):
        FacetBodyDistance = 0
        MeshTriangleIntersection = 1
        SolidBodyIntersection = 2
    

class PrebendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Angle01: float
    Angle02: float
    Angle03: float
    Angle04: float
    Angle05: float
    BendFace: ScCollector
    NeutralFactor: str
    NumberBends: Tooling.PrebendBuilder.NumberBendsOption
    StartEdge: ScCollector


    class NumberBendsOption(enum.Enum):
        Two = 0
        Three = 1
        Four = 2
        Five = 3
        Six = 4
    

class PocketCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.PocketBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePocketBuilder(self) -> Tooling.PocketBuilder:
        ...
    def Tag(self) -> Tag: ...



class PocketBuilder(Builder):
    def __init__(self) -> None: ...
    def FindIntersection(self) -> None:
        ...
    def CheckStatus(self) -> None:
        ...
    def RemovePocket(self) -> None:
        ...
    def EditFalseBody(self) -> None:
        ...
    def DeleteFamilyToolFalse(self) -> None:
        ...
    def InitializeFamilyData(self) -> None:
        ...
    AssociationSetting: bool
    CreateSolidSetting: bool
    EntireComponentPattern: bool
    FsetName: str
    ModeSelection: Tooling.PocketBuilder.ModeType
    PreviewFalseBody: bool
    ReferenceSets: Tooling.PocketBuilder.RsetType
    RemoveToolComponent: bool
    SaveSetting: bool
    SelectTarget: SelectBodyList
    SelectTool: SelectNXObjectList
    SelectTypes: Tooling.PocketBuilder.ToolType
    ShowSetting: bool


    class ToolType(enum.Enum):
        Part = 0
        Solid = 1
    

    class RsetType(enum.Enum):
        False = 0
        True = 1
        Both = 2
        AddMaterial = 3
        NoChange = 4
    

    class ModeType(enum.Enum):
        Subtract = 0
        Add = 1
    

class PiercingInsertMiniToolsBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdatePosition(self) -> None:
        ...
    def DeletePiercingInsert(self) -> None:
        ...
    AssociationTool: Tooling.PiercingInsertMiniToolsBuilder.AssociationToolItems
    InsertsToDelete: SelectBodyList
    SelectAssociationInsert: SelectBodyList
    SelectAssociationScrap: SelectBodyList
    SelectScrapOrInsert: SelectFaceList


    class AssociationToolItems(enum.Enum):
        AddintoList = 0
        RemovefromList = 1
    

class PiercingInsertCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.PiercingInsertBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePiercingInsertBuilder(self) -> Tooling.PiercingInsertBuilder:
        ...
    def Tag(self) -> Tag: ...



class PiercingInsertBuilder(Builder):
    def __init__(self) -> None: ...
    def NormalLoadDie(self) -> None:
        ...
    def CreateUserDefinedInsertDatumPlane(self) -> None:
        ...
    def CreateUserDefinedDieInsert(self) -> None:
        ...
    def AddDieInsertPart(self) -> None:
        ...
    def DieEditOffsetValueTable(self) -> None:
        ...
    def NormalCreateCavityAndSlug(self) -> None:
        ...
    def NormalLoadStandardPunch(self) -> None:
        ...
    def PunchEditOffsetValueTable(self) -> None:
        ...
    def NormalCreateUdp(self) -> None:
        ...
    def AddStripperInsert(self) -> None:
        ...
    def UpdatePosition(self) -> None:
        ...
    def LinkButton(self) -> None:
        ...
    AssociationTool: Tooling.PiercingInsertBuilder.AssociationToolType
    ConceptDesign: bool
    DieInsertType: Tooling.PiercingInsertBuilder.DieInsertTypeItems
    DieOffsetValue: float
    DieSameOffsetValue: bool
    NewPartNames: str
    NormalBbpslug: Tooling.PiercingInsertBuilder.NormalBbpslugType
    NormalCavity: Tooling.PiercingInsertBuilder.NormalCavityType
    NormalClearance: float
    NormalClearanceOption: Tooling.PiercingInsertBuilder.NormalClearanceOptionType
    NormalDsslug: Tooling.PiercingInsertBuilder.NormalDsslugType
    NormalForEachScrap1: bool
    NormalForEachScrap2: bool
    NormalOffsetSide: Tooling.PiercingInsertBuilder.NormalOffsetSideType
    NormalOnePunchToggle: bool
    NormalPunchLength: str
    NormalRenameDialog: bool
    NormalSelectPierceDieInsert: SelectBodyList
    NormalSelectPiercePunch: SelectBodyList
    NormalSlugPara1: float
    NormalSlugPara2: float
    NormalSlugPara3: float
    NormalSlugPara4: float
    OffsetLinearDimension: Expression
    ParentPartName: str
    Position: Tooling.PiercingInsertBuilder.InsertPosition
    PunchOffsetValue: float
    PunchPocketClearanceForBP: float
    PunchPocketClearanceForPP: float
    PunchPocketClearanceForSP: float
    PunchPocketHeightInSP: float
    PunchPocketToggleForBP: bool
    PunchPocketToggleForPP: bool
    PunchPocketToggleForSP: bool
    PunchPocketTypeInBP: Tooling.PiercingInsertBuilder.PunchPocketTypeItemsBP
    PunchPocketTypeInPP: Tooling.PiercingInsertBuilder.PunchPocketTypeItemsPP
    PunchPocketTypeInSP: Tooling.PiercingInsertBuilder.PunchPocketTypeItemsSP
    PunchSameOffsetValue: bool
    SelectAssociationInsert: SelectBodyList
    SelectAssociationScrap: SelectBodyList
    SelectDieInsertForCavity: SelectBodyList
    SelectDieInsertOutline: Section
    SelectScrap: SelectBodyList
    SelectScrapOrInsert: SelectFaceList
    SelectUserDefinedDieInsertForEdit: SelectBodyList
    SettingWithoutFalseBody: bool
    SlugHoleHeightLinearDimension: Expression
    Type: Tooling.PiercingInsertBuilder.Types
    UserDefinedDieInsertClearance: float
    UserDefinedDieInsertHeight: Expression
    UserDefinedPunchEnd: Expression
    UserDefinedPunchPenetration: float
    UserDefinedPunchStart: Expression


    class Types(enum.Enum):
        DieInsert = 0
        DieCavityAndSlugHole = 1
        PunchInsert = 2
        Association = 3
        Delete = 4
    

    class PunchPocketTypeItemsSP(enum.Enum):
        Clearance = 0
        Fillet = 1
        Circle = 2
    

    class PunchPocketTypeItemsPP(enum.Enum):
        Clearance = 0
        Fillet = 1
        Circle = 2
    

    class PunchPocketTypeItemsBP(enum.Enum):
        Clearance = 0
        Fillet = 1
        Circle = 2
    

    class NormalUdpparentPartType(enum.Enum):
        PrjDie099 = 0
        PrjDb000 = 1
        PrjSub002 = 2
    

    class NormalOffsetSideType(enum.Enum):
        DieSide = 0
        PunchSide = 1
    

    class NormalDsslugType(enum.Enum):
        Fillet = 0
        Rectangle = 1
        Circle = 2
        Mickey = 3
        Clearance = 4
        SlotVer = 5
        SlotHor = 6
        None = 7
    

    class NormalClearanceOptionType(enum.Enum):
        Constant = 0
        Variable = 1
    

    class NormalCavityType(enum.Enum):
        TaperAngle = 0
        Step = 1
        RoundStep1 = 2
        RoundStep2 = 3
    

    class NormalBbpslugType(enum.Enum):
        Fillet = 0
        Rectangle = 1
        Circle = 2
        Mickey = 3
        Clearance = 4
        SlotVer = 5
        SlotHor = 6
        None = 7
    

    class InsertPosition(enum.Enum):
        Top = 0
        Bottom = 1
    

    class DieInsertTypeItems(enum.Enum):
        DieInsert = 0
        BackingInsert = 1
    

    class AssociationToolType(enum.Enum):
        AddIntoList = 0
        RemoveFromList = 1
        DeleteSelectedInserts = 2
    

class OpeningAreaData(Tooling.CostDataObject):
    def __init__(self) -> None: ...
    def AskIdenticalOpeningAreas(self, identicalObjects: typing.List[Tooling.OpeningAreaData]) -> None:
        ...


class OffsetDatumCsysBuilder(Builder):
    def __init__(self) -> None: ...
    def AddDatumCsys(self, refCsys: CoordinateSystem, refObject: NXObject, refExp: NXObject) -> None:
        ...
    def SetCsysName(self, olderName: str, newName: str) -> None:
        ...
    def SetReferenceObject(self, csysName: str, refObject: NXObject) -> None:
        ...
    def SetExpressionFormula(self, csysName: str, expFormula: str) -> None:
        ...
    def EditCsys(self, csysName: CoordinateSystem, refObject: NXObject, refCsys: CoordinateSystem) -> None:
        ...
    def DeleteCsys(self, csysName: str) -> None:
        ...
    def GetCsysByName(self, csysName: str) -> CoordinateSystem:
        ...
    def GetAllCsys(self, csysName: str) -> None:
        ...
    def SetAllCsys(self, csys: typing.List[CoordinateSystem], csysName: str, refExp: typing.List[NXObject]) -> None:
        ...


    class ReferenceType(enum.Enum):
        ReferenceObject = 0
        ReferenceExpression = 1
    

class OffsetCurve3DBuilder(Builder):
    def __init__(self) -> None: ...
    def GetAllReverseDirectionFlags(self, allReverseDirectionFlags: bool) -> None:
        """[Obsolete("Deprecated in NX10.0.0.   ")"""
        ...
    def SetAllReverseDirectionFlags(self, allReverseDirectionFlags: bool) -> None:
        """[Obsolete("Deprecated in NX10.0.0.   Please use NXOpen.Features.Offset3DCurveBuilder.FlipOffsetCurveDirection instead ")"""
        ...
    DistanceTolerance: float
    OffsetCurves: Section
    OffsetDistance: float
    OffsetViewDirection: Direction
    ReverseDirection: bool


class ObjectAttributeManagementCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ObjectAttributeManagementBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateObjectAttributeManagementBuilder(self) -> Tooling.ObjectAttributeManagementBuilder:
        ...
    def Tag(self) -> Tag: ...



class ObjectAttributeManagementBuilder(Builder):
    def __init__(self) -> None: ...
    def AddFromDataFileAttributeList(self) -> None:
        ...
    def NewAttribute(self) -> None:
        ...
    def CopyAttribute(self) -> None:
        ...
    def PasteAttribute(self) -> None:
        ...
    def DeleteAttribute(self) -> None:
        ...
    def UndoButton(self) -> None:
        ...
    def EditConfigurationFile(self) -> None:
        ...
    AttributeOfRootPart: bool
    AttributeTitles: str
    AttributeValues: str
    OccurenceOrPrototypeEnum: Tooling.ObjectAttributeManagementBuilder.OccurenceOrPrototype
    OccurenceOrPrototypeEnumAccordingToAttribute: Tooling.ObjectAttributeManagementBuilder.OccurenceOrPrototypeAccordingToAttribute
    SelectAttributeSpreadsheet: str
    SelectBody: SelectNXObjectList
    SelectBodyAccordingToAttribute: SelectNXObjectList
    SelectComponent: SelectNXObjectList
    SelectComponentAccordingToAttribute: SelectNXObjectList
    SelectFace: ScCollector
    SelectFaceAccordingToAttribute: ScCollector
    SelectionFilter: Tooling.ObjectAttributeManagementBuilder.FilterType
    SelectionFilterAccordingToAttribute: Tooling.ObjectAttributeManagementBuilder.FilterAccordingToAttributeType
    ShowTypeEnum: Tooling.ObjectAttributeManagementBuilder.ShowComponentsType
    ToggleListDependents: bool
    Type: Tooling.ObjectAttributeManagementBuilder.ShowType
    WizardType: int


    class ShowType(enum.Enum):
        ShowAttributeOfSelectedObject = 0
        ShowObjectAccordingToAttribute = 1
    

    class ShowComponentsType(enum.Enum):
        ShowAllComponents = 0
        OnlyShowComponentsWithAttribute = 1
        HideComponentsWithAttribute = 2
    

    class OccurenceOrPrototypeAccordingToAttribute(enum.Enum):
        AssignAttributesToOccurence = 0
        AssignAttributesToPrototype = 1
    

    class OccurenceOrPrototype(enum.Enum):
        AssignAttributesToOccurence = 0
        AssignAttributesToPrototype = 1
    

    class FilterType(enum.Enum):
        Part = 0
        Component = 1
        SolidBody = 2
        Face = 3
    

    class FilterAccordingToAttributeType(enum.Enum):
        Part = 0
        Component = 1
        SolidBody = 2
        Face = 3
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MWTraversePartingLinesCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MWTraversePartingLinesBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.MWTraversePartingLinesBuilder:
        ...
    def Tag(self) -> Tag: ...



class MWTraversePartingLinesBuilder(Builder):
    def __init__(self) -> None: ...
    def AssignTraverseLoopBuilder(self, traverseLoopBuilder: Tooling.TraverseLoopBuilder) -> None:
        ...


class MWSearchRegionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MWSearchRegionBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.MWSearchRegionBuilder:
        ...
    def Tag(self) -> Tag: ...



class MWSearchRegionBuilder(Builder):
    def __init__(self) -> None: ...
    def ChangeBoundaryFacesColor(self) -> None:
        ...
    def InitBuilderData(self) -> None:
        ...
    def DisplayProductBody(self) -> None:
        ...
    def TurnOffAllPartingLines(self) -> None:
        ...
    def UpdateRegion(self) -> None:
        ...
    BoundaryFacesColor: NXColor
    DifferentColorsAsBoundaryFacesOption: bool
    HighlightConnectingFacesScale: int
    MaximumNumberOfFacesSearched: int
    SelectBoundaryEdges: SelectEdgeList
    SelectBoundaryFaces: SelectFaceList
    SelectSeedFaces: SelectFaceList
    TranslucencyAsBoundaryFacesToggle: bool


class MWPartingManagerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MWPartingManagerBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.MWPartingManagerBuilder:
        ...
    def Tag(self) -> Tag: ...



class MWPartingManagerBuilder(Builder):
    def __init__(self) -> None: ...
    def InitModule(self) -> int:
        ...
    def InitPartingSettings(self) -> None:
        ...
    def PerformSyncTasks(self) -> None:
        ...
    def PerformSyncTasksOnExit(self) -> None:
        ...
    def SetUpdateLock(self) -> None:
        ...
    def ResetUpdateLock(self, doUpdate: int) -> None:
        ...
    def GetPartingManagerDataStatus(self) -> int:
        ...
    def SetPartingManagerDataStatus(self, pmDataStatus: int) -> None:
        ...
    def GetInPartingCommand(self) -> int:
        ...
    def SetInPartingCommand(self, inPartingCommand: int) -> None:
        ...
    def UpdatePartingNavigator(self) -> None:
        ...
    def RegisterUndoIds(self, registerType: int) -> None:
        ...
    def RegisterWtcPostUndoCallback(self, registerPostUNDO: int) -> None:
        ...
    def DeleteTransientMeshes(self, deleteMesh: int) -> None:
        ...


    class RegisterType(enum.Enum):
        Init = 0
        Current = 1
        Clear = 2
    

    class DataStatus(enum.Enum):
        NotFreed = 0
        Freed = 1
        ForceUpdate = 2
    

class MWMoldedPartValidationManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def CreateMWMoldedPartValidationBuilder(self) -> Tooling.MWMoldedPartValidationBuilder:
        ...
    def Tag(self) -> Tag: ...



class MWMoldedPartValidationBuilder(Builder):
    def __init__(self) -> None: ...
    def Calculate(self) -> None:
        ...
    def FaceSetAllFacesColor(self) -> None:
        ...
    def ProcessFaceSplit(self) -> None:
        ...
    def RegionSetRegionsColor(self) -> None:
        ...
    def UpdateEjectDirection(self) -> None:
        ...
    def InitMpvData(self, changeBody: int) -> None:
        ...
    def UpdateMpvData(self) -> None:
        ...
    def PerformModelPropertiesCalculation(self) -> None:
        ...
    def PerformSharpCornersCalculation(self) -> None:
        ...
    def UpdateSharpEdgesInformation(self) -> None:
        ...
    def UpdateSmallRadiusFacesInformation(self) -> None:
        ...
    def SetCalculationProductBody(self, calculationProductBody: Body) -> None:
        ...
    def ApplyAllDefaultParametersAfterInit(self) -> None:
        ...
    def GetFaceAnalysisFaces(self, allFaces: typing.List[Face], positiveFaces: typing.List[Face], smallDraftAnglePositiveFaces: typing.List[Face], verticalFaces: typing.List[Face], smallDraftAngleNegativeFaces: typing.List[Face], negativeFaces: typing.List[Face]) -> None:
        ...
    def GetCrossoverFacesAndUndercuts(self, crossoverFaces: typing.List[Face], undercutFaces: typing.List[Face], undercutEdges: typing.List[Edge], nUndercutAreas: int) -> None:
        ...
    def GetRegionAnalysisFaces(self, cavityRegionFaces: typing.List[Face], coreRegionFaces: typing.List[Face], undefinedRegionFaces: typing.List[Face], undefinedCrossoverRegionFaces: typing.List[Face], undefinedCrossoverVerticalFaces: typing.List[Face], undefinedUnknownRegionFaces: typing.List[Face], partingEdges: typing.List[Edge], nInternalLoopEdges: int, allInternalLoopEdges: typing.List[Edge], nIncompleteLoopEdges: int, allIncompleteLoopEdges: typing.List[Edge]) -> None:
        ...
    def GetClosestNXColorIDFromRGB(self, colorRGB: NXColor.Rgb) -> int:
        ...
    def GetAllColors(self, nxFaceColorIDs: int, faceColorRGBs: typing.List[NXColor.Rgb], nxRegionColorIDs: int, regionColorRGBs: typing.List[NXColor.Rgb]) -> None:
        ...
    def ChangeRegionsColor(self, intRGBValues: int) -> None:
        ...
    def ChangeRegionsTranslucency(self, intTranslucencyValues: int) -> None:
        ...
    def RetrieveRegionsTranslucency(self, intTranslucencyValues: int) -> None:
        ...
    def ChangeDraftFacesColor(self, intRGBValues: int) -> None:
        ...
    def UpdateDraftFacesInfoOnDraftAngleLimitChange(self, draftAngleLimit: float) -> None:
        ...
    def ExecuteApply(self) -> None:
        ...
    def HighlightBasedOnToggles(self) -> None:
        ...
    def DehighlightAll(self) -> None:
        ...
    def InitDraftAnalysis(self) -> None:
        ...
    def ResetDraftAnalysis(self, deleteDraftAnalysisAO: bool) -> None:
        ...
    def UpdateDraftAnalysisDisplay(self) -> None:
        ...
    def UpdateDraftAnalysisDisplayOnColorChange(self, intRGBValues: int) -> None:
        ...
    def UpdateDraftAnalysisDisplayOnDraftAngleLimitChange(self, draftAngleLimit: float) -> None:
        ...
    def InitMPVDraftAnalysis(self) -> None:
        ...
    def UpdateMPVDraftAnalysisDisplayOnColorChange(self, intRGBValues: int) -> None:
        ...
    def UpdateMPVDraftAnalysisDisplayOnDraftAngleLimitChange(self, draftAngleLimit: float) -> None:
        ...
    def UpdateMPVDraftAnalysisDisplayOnDrawDirectionChange(self, drawDirection: Vector3d) -> None:
        ...
    def GetMPVDraftAnalysisConvergentBodies(self, mpvDraftAnalysisConvergentBodies: typing.List[Body], bodyType: int) -> None:
        ...
    def GetOnOffStatesOfMPVDraftAnalysisConvergentBodies(self, onOffStates: int) -> None:
        ...
    def UpdateOnOffStateOfMPVDraftAnalysisConvergentBodies(self, onOffStates: int, option: int) -> None:
        ...
    def CheckAnalysisResultsAvailableAndUpToDate(self, analysisBody: Body, draftAnalysisResultsAvailable: int, draftAnalysisresultsUpToDate: int, regionAnalysisResultsAvailable: int, regionAnalysisresultsUpToDate: int) -> None:
        ...
    def GetCurrentAnalysisBodyAndParameters(self, analysisBody: Body, drawDirection: Vector3d, draftAngleLimit: float) -> None:
        ...
    def IdentifyAndGroupBodies(self, bodyTags: typing.List[Body], bodyResults: typing.List[Body], bodyNoResults: typing.List[Body], invalidBodies: typing.List[Body]) -> None:
        ...
    ActiveTabPage: int
    CalculationDrawDirection: Direction
    CalculationOption: Tooling.MWMoldedPartValidationBuilder.CalculateOption
    CalculationProductBody: SelectBody
    FaceAllFacesColor: NXColor
    FaceCrossoverFacesColor: NXColor
    FaceDraftAngleLimit: float
    FaceHighlightSelectedFaces: bool
    FaceNegativeFacesColor1: NXColor
    FaceNegativeFacesColor2: NXColor
    FaceNonSelectedFacesTranslucency: int
    FacePositiveFacesColor1: NXColor
    FacePositiveFacesColor2: NXColor
    FaceSelectAllFaces: bool
    FaceSelectCrossoverFaces: bool
    FaceSelectNegativeFaces1: bool
    FaceSelectNegativeFaces2: bool
    FaceSelectPositiveFaces1: bool
    FaceSelectPositiveFaces2: bool
    FaceSelectUndercutAreas: bool
    FaceSelectUndercutEdges: bool
    FaceSelectVerticalFaces: bool
    FaceSelectedFacesTranslucency: int
    FaceUndercutAreasColor: NXColor
    FaceUndercutEdgesColor: NXColor
    FaceVerticalFacesColor: NXColor
    InApplyStatus: int
    InformationCheckScope: Tooling.MWMoldedPartValidationBuilder.CheckScope
    InformationColorR01: NXColor
    InformationColorR02: NXColor
    InformationColorR03: NXColor
    InformationColorR04: NXColor
    InformationColorR05: NXColor
    InformationColorR06: NXColor
    InformationColorR07: NXColor
    InformationColorR08: NXColor
    InformationColorR09: NXColor
    InformationColorR10: NXColor
    InformationColorR11: NXColor
    InformationColorR12: NXColor
    InformationInspectFace: SelectFace
    InformationLowerLimit: float
    InformationLowerLimitR01: float
    InformationLowerLimitR02: float
    InformationLowerLimitR03: float
    InformationLowerLimitR04: float
    InformationLowerLimitR05: float
    InformationLowerLimitR06: float
    InformationLowerLimitR07: float
    InformationLowerLimitR08: float
    InformationLowerLimitR09: float
    InformationLowerLimitR10: float
    InformationLowerLimitR11: float
    InformationLowerLimitR12: float
    InformationRangeType: Tooling.MWMoldedPartValidationBuilder.RangeType
    InformationSharpAngleLimit: float
    InformationShowBoundaryEdges: bool
    InformationShowRangeR01: bool
    InformationShowRangeR02: bool
    InformationShowRangeR03: bool
    InformationShowRangeR04: bool
    InformationShowRangeR05: bool
    InformationShowRangeR06: bool
    InformationShowRangeR07: bool
    InformationShowRangeR08: bool
    InformationShowRangeR09: bool
    InformationShowRangeR10: bool
    InformationShowRangeR11: bool
    InformationShowRangeR12: bool
    InformationShowSharpEdges: bool
    InformationUpperLimit: float
    InformationUpperLimitR01: float
    InformationUpperLimitR02: float
    InformationUpperLimitR03: float
    InformationUpperLimitR04: float
    InformationUpperLimitR05: float
    InformationUpperLimitR06: float
    InformationUpperLimitR07: float
    InformationUpperLimitR08: float
    InformationUpperLimitR09: float
    InformationUpperLimitR10: float
    InformationUpperLimitR11: float
    InformationUpperLimitR12: float
    InformationUseSingleTolerance: bool
    RegionAssignToRegionOption: Tooling.MWMoldedPartValidationBuilder.AssignToRegion
    RegionCavityRegionColor: NXColor
    RegionCavityRegionTranslucency: int
    RegionCoreRegionColor: NXColor
    RegionCoreRegionTranslucency: int
    RegionFaces: SelectFaceList
    RegionSelectCrossoverRegionFaces: bool
    RegionSelectCrossoverVerticalFaces: bool
    RegionSelectUnknownFaces: bool
    RegionShowIncompleteLoops: bool
    RegionShowInternalLoops: bool
    RegionShowPartingEdges: bool
    RegionUndefinedRegionColor: NXColor


    class RangeType(enum.Enum):
        Uniform = 0
        Range = 1
        Plain = 2
    

    class CheckScope(enum.Enum):
        FaceProperties = 0
        ModelProperties = 1
        SharpCorners = 2
    

    class CalculateOption(enum.Enum):
        KeepExisting = 0
        EditRegionsOnly = 1
        ResetAll = 2
    

    class AssignToRegion(enum.Enum):
        CavityRegion = 0
        CoreRegion = 1
    

class MWLayoutCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.LayoutBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLayoutBuilder(self) -> Tooling.LayoutBuilder:
        ...
    def CreateLayoutRepositionBuilder(self) -> Tooling.LayoutRepositionBuilder:
        ...
    def Tag(self) -> Tag: ...



class MWDesignPartingSurfaceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MWDesignPartingSurfaceBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.MWDesignPartingSurfaceBuilder:
        ...
    def Tag(self) -> Tag: ...



class MWDesignPartingSurfaceBuilder(Builder):
    def __init__(self) -> None: ...
    def InitializeOnEntry(self) -> None:
        ...
    def DisplayObjectsOnEntry(self) -> None:
        ...
    def ChangePartingObjectType(self, partingObjectType: int) -> None:
        ...
    def PreCreateBoundedPlaneAndEnlargedSurface(self) -> None:
        ...
    def ClearPreCreatedBoundedPlaneAndEnlargedSurface(self, differentSegment: int) -> None:
        ...
    def ClearPreCreatedExtrudeAndSweptSurface(self, deleteSheet: int) -> None:
        ...
    def UpdateExtrudeDistanceExpression(self, extrudeDistance: float) -> None:
        ...
    def DeletePartingSurface(self, partingSheet: Body) -> None:
        ...
    def FinalizeCreatePartingSurface(self) -> None:
        ...
    def FlipTrimmedSheet(self) -> None:
        ...
    def CreateSurfaceData(self, faceTag: Face) -> None:
        ...
    def UpdatePreviewSurface(self) -> None:
        ...
    def UpdatePartingLines(self) -> None:
        ...
    def UpdateEditPartingLines(self) -> None:
        ...
    def UpdateTransitionPoints(self) -> None:
        ...
    def CheckSuppressParting(self) -> None:
        ...
    def UpdateExtrudeAndSweptSheets(self, directionChange: int) -> None:
        ...
    def DeleteAllPartingSurfaces(self) -> None:
        ...
    def AutoCreatePartingSurfaces(self) -> None:
        ...
    def UpdateAllSegmentsAutoCreateInfo(self) -> None:
        ...
    def UpdateSegmentAutoCreateInfo(self) -> None:
        ...
    def UpdateInApplyStatus(self, inApplyStatus: int) -> None:
        ...
    def CreateSectionForGuidedExtensionPreview(self) -> None:
        ...
    def UpdateBuilderPartingLinesHashTable(self) -> None:
        ...
    def VerifyExtendSheetMethod(self) -> None:
        ...
    def PreCreateExtendSheetSurface(self) -> None:
        ...
    def DeleteExtendSheetPreview(self, deleteSheet: int) -> None:
        ...
    def UpdateExtendSheetPreview(self, reverseSide: bool) -> None:
        ...
    def PreCreateRibbonSurface(self) -> None:
        ...
    def DeleteRibbonSurfacePreview(self, deleteSheet: int) -> None:
        ...
    def UpdateRibbonSurfacePreview(self) -> None:
        ...
    def FlipSide(self) -> None:
        ...
    def CreatePartingLinesByExistingRegions(self) -> None:
        ...
    def BridgeGapInPartingLinesLoop(self) -> Curve:
        ...
    AlternateMethod: bool
    CreateAsPartingSurface: bool
    CreateExtrudeSweptPreview: bool
    EditPartingLines: ScCollector
    EnlargeOtherFaceOption: bool
    ExtendDistance: Expression
    ExtrudeDirection: Direction
    ExtrudeDistance: float
    ExtrudeDraftAngle: float
    GuideOrPartingLine: SelectCurve
    PartingLines: SelectCurveList
    PrimaryEdges: SelectEdgeList
    ResizeAllDirections: bool
    SecondDirection: Direction
    SurfaceRange: GeometricUtilities.SurfaceRangeBuilder
    SurfaceTolerance: float
    SurfaceType: Tooling.MWDesignPartingSurfaceBuilder.PartingSurfaceType
    TransitionObjects: SelectCurveList
    TransitionSurfType: Tooling.MWDesignPartingSurfaceBuilder.TransitionSurfaceType
    TrimAndExtendFromRegion: Tooling.MWDesignPartingSurfaceBuilder.TrimAndExtendFromRegionType
    TrimWithGuideLines: bool
    UseDefaultKeepSide: bool


    class TrimAndExtendFromRegionType(enum.Enum):
        Cavity = 0
        Core = 1
        None = 2
    

    class TransitionSurfaceType(enum.Enum):
        Auto = 0
        BoundedPlane = 1
        Swept = 2
        Bridge = 3
    

    class PartingSurfaceType(enum.Enum):
        Extrude = 0
        Swept = 1
        BoundedPlane = 2
        EnlargedSurface = 3
        TrimandExtend = 4
        RibbonSurface = 5
        GuidedExtension = 6
    

    class ObjectType(enum.Enum):
        PartingSurface = 0
        PartingLine = 1
        GuideLine = 2
        TransitionObject = 3
    

class MWDesignGuideLinesCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MWDesignGuideLinesBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.MWDesignGuideLinesBuilder:
        ...
    def Tag(self) -> Tag: ...



class MWDesignGuideLinesBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteSelectedGuideLine(self) -> None:
        ...
    def DeleteAllGuideLines(self) -> None:
        ...
    def AutoCreateGuideLines(self) -> None:
        ...
    def CreateGuideLine(self, partingLineTag: Curve, closePoint: Point3d, length: float, created: int) -> Curve:
        ...
    def UpdateGuideLineDirection(self, directionType: Tooling.MWDesignGuideLinesBuilder.DirectionType, guideLine: Curve) -> None:
        ...
    def DeleteGuideLine(self, guideLine: Curve) -> None:
        ...
    def UpdateGuideLineDirectionAndLength(self, guideLine: Curve, guideLineVector: Vector3d, guideLinelength: float) -> None:
        ...
    GuideDirection: Tooling.MWDesignGuideLinesBuilder.DirectionType
    GuideLength: Expression
    GuideOrPartingLine: SelectCurve
    GuideVector: Direction
    SnapAngleLimit: float


    class DirectionType(enum.Enum):
        Normal = 0
        Tangential = 1
        SnaptoWCSAxis = 2
        Vector = 3
    

class MWDefineSheetsCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MWDefineSheetsBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.MWDefineSheetsBuilder:
        ...
    def Tag(self) -> Tag: ...



class MWDefineSheetsBuilder(Builder):
    def __init__(self) -> None: ...
    def SuppressPartingButton(self) -> None:
        ...
    def InitBuilderData(self) -> None:
        ...
    def UpdateBuilderData(self) -> None:
        ...
    def SaveBuilderData(self) -> None:
        ...
    def ResetBuilderData(self) -> None:
        ...
    def SetAllRegionUdosSelected(self, allRegionUDOsSelected: int) -> None:
        ...
    def SetSelectedRegions(self, regionNames: str) -> None:
        ...
    def DeleteExistingSheets(self) -> None:
        ...
    def PerformDisplayAndHighlight(self) -> None:
        ...
    def TurnOffAllSheets(self) -> None:
        ...
    def DisplayRegionOrSheetBody(self, onOff: int) -> None:
        ...
    def PerformDisplayForTypeChange(self) -> None:
        ...
    def CreateRegionSewnSheet(self, regionName: str) -> None:
        ...
    def SuppressRegionSheet(self, regionName: str) -> None:
        ...
    def ReversePartNormal(self, viewPart: BasePart) -> None:
        ...
    def SetDisplayedPart(self, displayedPart: BasePart) -> None:
        ...
    def SetWorkPart(self, workPart: BasePart) -> None:
        ...
    def CreateAssemblyNodeForRegionSheet(self, regionName: str) -> BasePart:
        ...
    def AutoCreateSelectedSheets(self) -> None:
        ...
    CheckGeometryToggle: bool
    CheckOverlappingToggle: bool
    DefineStep: Tooling.MWDefineSheetsBuilder.DefineStepType
    NoInteractionQueriesToggle: bool
    RenameComponentPartToggle: bool
    SelectProductBodies: SelectBodyList
    SelectSheetBodies: SelectBodyList
    SelectWorkpieceBody: SelectBody
    SewTolerance: float
    SplittingSheets: ScCollector
    Type: Tooling.MWDefineSheetsBuilder.Types


    class Types(enum.Enum):
        Region = 0
        SplitBody = 1
    

    class DefineStepType(enum.Enum):
        CutSolids = 0
        CavityandCore = 1
    

class MWDefineRegionsCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MWDefineRegionsBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.MWDefineRegionsBuilder:
        ...
    def Tag(self) -> Tag: ...



class MWDefineRegionsBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateNewRegionButton(self) -> None:
        ...
    def SearchRegionButton(self) -> None:
        ...
    def SetupRegionsInfo(self) -> None:
        ...
    def DisplayProductBody(self) -> None:
        ...
    def CreateNewRegion(self) -> str:
        ...
    def GetOrCreateEmptyRegion(self, created: int) -> str:
        ...
    def DeleteRegion(self, regionName: str) -> None:
        ...
    def SetCurrentRegion(self, regionName: str) -> None:
        ...
    def ChangeCurrentRegionName(self, regionName: str) -> int:
        ...
    def ChangeRegionFacesColor(self, regionName: str, allOrUndefined: int, color: int) -> None:
        ...
    def ChangeEntitiesColor(self, entities: typing.List[TaggedObject], color: int) -> None:
        ...
    def ChangeRegionLayer(self, regionName: str, layer: int) -> None:
        ...
    def UpdateUndefinedFaces(self, changeColor: int) -> None:
        ...
    def DeleteAllExistingRegions(self) -> None:
        ...
    def UpdateUnsewnBodiesNameAttribute(self, unsewFeatureTag: TaggedObject, cavityFaces: typing.List[Face]) -> None:
        ...
    def HookupRegionUdoAndBodyForCavityAndCore(self) -> None:
        ...
    CreatePartingLinesToggle: bool
    CreateRegionsToggle: bool
    FaceColor: NXColor
    SelectRegionFaces: ScCollector
    TranslucencyOption: Tooling.MWDefineRegionsBuilder.TranslucencyOptionType
    TranslucencyValueScale: int


    class TranslucencyOptionType(enum.Enum):
        SelectedFaces = 0
        OtherFaces = 1
    

class MWCopySheetsCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MWCopySheetsBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.MWCopySheetsBuilder:
        ...
    def Tag(self) -> Tag: ...



class MWCopySheetsBuilder(Builder):
    def __init__(self) -> None: ...
    ColorPicker: NXColor
    CopyAllSheetsToggle: bool
    Layer: int
    SheetsSelection: SelectBodyList
    Type: Tooling.MWCopySheetsBuilder.Types


    class Types(enum.Enum):
        PartingSurfaces = 0
        PatchedSurfaces = 1
        Both = 2
    

class MotionSimulationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MotionSimulationBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateMotionSimulationBuilder(self) -> Tooling.MotionSimulationBuilder:
        ...
    def Tag(self) -> Tag: ...



class MotionSimulationBuilder(Builder):
    def __init__(self) -> None: ...
    def MountKinematicComponents(self) -> None:
        ...
    def MountComponent(self, componentsArray: typing.List[NXObject]) -> None:
        ...
    def GetMountedBodyObjects(self, mountType: str, mountedBodyObjects: typing.List[NXObject]) -> None:
        ...
    def AddSafeDistanceAttribute(self, editEixstChecker: bool) -> None:
        ...
    def RemoveSafeDistanceAttibute(self, targetIndex: int) -> None:
        ...
    def EditTargetSafeDistance(self, selectedLabel: str, safeValue: float) -> None:
        ...
    def DeleteTargetSafeDistanceItem(self, labelString: str) -> None:
        ...
    AvoidMountChildren: bool
    CamDefinitionMethod: Tooling.MotionSimulationBuilder.CamDefinitionType
    Component: SelectBodyList
    ControlDataFile: str
    CrankRadius: Expression
    CsysVisibility: bool
    DiePitch: Expression
    DiePitch02: Expression
    EjectionStartAngle: float
    EjectorMoveOption: Tooling.MotionSimulationBuilder.EjectorMoveOptions
    ExportControlData: str
    HideMotionItem: bool
    IncludeBlank: bool
    IsDataFileValid: bool
    IsRemoveCurrentKinematicModel: bool
    KinematicModel: SelectBody
    KinematicModelName: str
    LiftHeight: Expression
    LiftHeight02: Expression
    MachineStroke: Expression
    ModelListSelectedNumber: int
    MoldOpenAngle: float
    MoldbaseStyle: Tooling.MotionSimulationBuilder.MoldbaseStyleType
    ReReadConfigData: bool
    RelativeMotion: bool
    RenameComponents: bool
    RenameRule: str
    SafeDisComponent: SelectBodyList
    SafeDisTargetComponent: SelectBodyList
    SafeDistance: float
    SelectedMountType: str
    StripTravel: Expression
    StripVector: Direction
    StrokeAngleStep: Expression
    StrokePerMinute: float
    TargetDirectory: str
    TransferEndAngle: Expression
    TransferStartAngle: Expression
    Type: Tooling.MotionSimulationBuilder.Types


    class Types(enum.Enum):
        AddKinematicModel = 0
        MountComponent = 1
        SafeDistanceConfig = 2
    

    class MoldbaseStyleType(enum.Enum):
        Two = 0
        Three = 1
    

    class EjectorMoveOptions(enum.Enum):
        After = 0
        While = 1
    

    class CamDefinitionType(enum.Enum):
        AutomaticalDefinedCam = 0
        UserDefinedCam = 1
    

class MoldwizardManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def CreateEjectorTableBuilder(self) -> Tooling.EjectorTableBuilder:
        ...
    def CreateBomListBuilder(self) -> Tooling.BomListBuilder:
        ...
    def CreateMoldFillingBuilder(self) -> Tooling.MoldFillingBuilder:
        ...
    def CreateBomListDataProvider(self) -> Tooling.BomListDataProvider:
        ...
    def CreateCopySolidBuilder(self) -> Tooling.CopySolidBuilder:
        ...
    def CreateMoldFeatureRecognitionBuilder(self) -> Tooling.MoldFeatureRecognitionBuilder:
        ...
    def CreateSheetMetalFeatureRecognitionBuilder(self) -> Tooling.SheetMetalFeatureRecognitionBuilder:
        ...
    def CreateCostFeatureDataProvider(self) -> Tooling.CostTableDataProvider:
        ...
    def CreateColorExpressionsBuilder(self) -> Tooling.ColorExpressionsBuilder:
        ...
    def CreateFeatureReferenceSetBuilder(self) -> Tooling.FeatureReferenceSetBuilder:
        ...
    def CreateReferenceCopyBuilder(self) -> Tooling.ReferenceCopyBuilder:
        ...
    def CreateMoldDesignReportBuilder(self) -> Tooling.CreateMoldDesignReportBuilder:
        ...
    def CreateDesignEjectorPinBuilder(self) -> Tooling.DesignEjectorPinBuilder:
        ...
    def CreateMoldInsertDesignBuilder(self) -> Tooling.MoldInsertDesignBuilder:
        ...
    def CreateVentingDesignBuilder(self) -> Tooling.VentingDesignBuilder:
        ...
    def CreateRasterImageBuilder(self, rasterImageTag: Display.RasterImage) -> Tooling.RasterImageBuilder:
        ...
    def CreateInsertBarcodeBuilder(self, pmiNoteTag: Annotations.SimpleDraftingAid) -> Tooling.InsertBarcodeBuilder:
        ...
    def CreateInsertQRBarCodeBuilder(self) -> Tooling.InsertQRBarCodeBuilder:
        ...
    def CreateInsertTextBuilder(self) -> Tooling.InsertTextBuilder:
        ...
    def CreateConformalOffsetBuilder(self) -> Tooling.ConformalOffsetBuilder:
        ...
    def CreateEditCoolingCurveBuilder(self) -> Tooling.EditCoolingCurveBuilder:
        ...
    def CreateConformalCircuitBuilder(self) -> Tooling.ConformalCircuitBuilder:
        ...
    def CreateStampingProcessRecognitionBuilder(self) -> Tooling.StampingProcessRecognitionBuilder:
        ...
    def Tag(self) -> Tag: ...



class MoldProcessCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MoldProcessBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateMoldProcessBuilder(self) -> Tooling.MoldProcessBuilder:
        ...
    def Tag(self) -> Tag: ...



class MoldProcessBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSelectedRecords(self, partNames: str, sketchNames: str) -> None:
        ...
    def GetStandardPartBatchData(self) -> Tooling.StandardPartBatchData:
        ...
    def SetStandardPartBatchData(self, batchData: Tooling.StandardPartBatchData) -> None:
        ...
    def FindMatchedLibraryOfConceptObject(self, conceptObject: NXObject) -> Tooling.StandardPartData:
        ...
    def SaveNameChangesToConceptObject(self, conceptObject: NXObject, assemblyName: str, assemblyPartNumber: str, assemblyItemType: str, childrenNames: str) -> None:
        ...
    def SaveCoolingConceptObjectHandles(self, conceptObject: NXObject, instanceObjects: typing.List[NXObject]) -> None:
        ...
    CompSelect: SelectPoint
    ConceptObjects: SelectNXObjectList
    Rename: bool


class MoldInsertDesignBuilder(Tooling.StandardPartBuilder):
    def __init__(self) -> None: ...
    def UpdateBoundingBodyOnOrientationChanged(self, boxMatrix: Matrix3x3) -> None:
        ...
    def GetCloneObject(self) -> Tooling.CloneObject:
        ...
    def SetCloneObject(self, cloneObject: Tooling.CloneObject) -> None:
        ...
    def CreateCloneObject(self) -> None:
        ...
    def RemoveInsertComponent(self) -> None:
        ...
    def EditInsertPartDimensions(self, addedPartOcc: Assemblies.Component) -> None:
        ...
    def GetInsertType(self) -> Tooling.MoldInsertDesignBuilder.InsertType:
        ...
    def SetInsertType(self, headType: Tooling.MoldInsertDesignBuilder.InsertType) -> None:
        ...
    def PopulateInsertDataToBuilder(self, addedPartOcc: Assemblies.Component) -> None:
        ...
    def AskInsertDataFromSelectedComponent(self, addedPartOcc: Assemblies.Component) -> None:
        ...
    def EditInsertComponentBasedOnSheetDataChange(self, addedPartOcc: Assemblies.Component) -> None:
        ...
    def MoveSideFlange(self) -> None:
        ...
    def OnExistingBodySelected(self) -> None:
        ...
    def SetBoundingBodyOrientation(self, position: Point3d, matrix: Matrix3x3) -> None:
        ...
    def UpdateInsertComponentOnOrientationChanged(self, matrix: Matrix3x3) -> None:
        ...
    def OnPositionPointSelected(self) -> None:
        ...
    def OnCuttingBodySelected(self) -> None:
        ...
    def OnBoundingBodyFaceChanged(self) -> None:
        ...
    def RestoreChangeInInsertComponent(self) -> None:
        ...
    def UpdateInsertBoundingBodyFromFeatureEdit(self, boxFeature: Features.ToolingBox) -> None:
        ...
    def PreviewSelectedInsertComponent(self) -> None:
        ...
    def OnHeadTypeChanged(self) -> bool:
        ...
    def AskFlangeTypeFromSheetData(self) -> int:
        ...
    def SetEditStatus(self, isInEdit: bool) -> None:
        ...
    def RestoreParameterValuesFromInsertPart(self, editingPartOcc: Assemblies.Component) -> None:
        ...
    def PreviewExtrudeBody(self, nBodies: int, bSolidBody: bool) -> None:
        ...
    def ReadInsertFlangeData(self, insertComponent: Assemblies.Component) -> None:
        ...
    def DeletePreviewBody(self) -> None:
        ...
    def ValidateExtrudeSection(self) -> int:
        ...
    def OnFirstSelectionForExtrudeSection(self, selObject: NXObject) -> Section:
        ...
    def CheckSectionOwningPart(self) -> None:
        ...
    Associative: bool
    BoundingBodyFaces: SelectFaceList
    CurrentEdge: Edge
    CuttingBody: SelectBody
    ExtrusionSection: Section
    FirstSelectionStatus: bool
    HeadType: Tooling.MoldInsertDesignBuilder.InsertHeadType
    PositionPoint: Point
    SelectExistingBody: SelectBody
    SketchFeature: Features.SketchFeature
    SplitBodyStatus: bool


    class InsertType(enum.Enum):
        Block = 0
        Cylinder = 1
    

    class InsertHeadType(enum.Enum):
        BoundingBody = 0
        ExistingSolid = 1
        Sketch = 2
        Standard = 3
    

class MoldInsertCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MoldInsertBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateMoldInsertBuilder(self) -> Tooling.MoldInsertBuilder:
        ...
    def Tag(self) -> Tag: ...



class MoldInsertBuilder(Builder):
    def __init__(self) -> None: ...
    MethodType: Tooling.MoldInsertBuilder.BooleanType
    Rename: bool
    SelectBody: SelectBodyList


    class BooleanType(enum.Enum):
        UniteSingleWorkpieces = 0
        SubtractOverallWorkpieces = 1
    

class MoldFillingBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteFill(self) -> None:
        ...
    def SetManipulatorPosition(self, matrix: Matrix3x3, position: Point3d) -> None:
        ...
    def SaveEditingFillComponentPosition(self, matrix: Matrix3x3, position: Point3d) -> None:
        ...
    def SetParameterTreeData(self, sheetData: Tooling.SpreadsheetData) -> None:
        ...
    def SetFillClientData(self, clientData: Tooling.StandardPartData) -> None:
        ...
    def EditComponentDimensions(self, addedPartOcc: Assemblies.Component) -> None:
        ...
    def AddFillingComponents(self) -> None:
        ...
    def SetActiveFillComponent(self, activePartOcc: Assemblies.Component) -> None:
        ...
    def GetDataFromSelectedFillComponent(self, sheetData: Tooling.SpreadsheetData) -> None:
        ...
    def RemoveAddedComponents(self) -> None:
        ...
    def GateLayoutAction(self) -> None:
        ...
    def CreateCloneObject(self) -> None:
        ...
    def PreviewSelectedFillComponent(self) -> None:
        ...
    def AskFillLibraryData(self, isFromMemberView: bool, libName: str, libPath: str) -> None:
        ...
    def SetClientDataWithSelectedItem(self, catalogName: str, descriptiveName: str) -> None:
        ...
    def GetCloneObject(self) -> Tooling.CloneObject:
        ...
    def SetCloneObject(self, cloneObject: Tooling.CloneObject) -> None:
        ...
    def SetParentAsWorkPart(self, sheetData: Tooling.SpreadsheetData) -> None:
        ...
    def GetLastFillComponent(self) -> Assemblies.Component:
        ...
    def SetLastFillComponent(self, lastFillComponent: Assemblies.Component) -> None:
        ...
    AddedGatesByRunner: Assemblies.SelectComponentList
    Constraint: bool
    FillComponent: Assemblies.SelectComponent
    InstallOptions: Tooling.MoldFillingBuilder.InstallOption
    IsBalanced: bool
    MoveAllGates: bool
    MoveOptions: Tooling.MoldFillingBuilder.MoveOption
    PositionObject: SelectNXObject
    PositionPoint: Point
    Rename: bool


    class MoveOption(enum.Enum):
        Move = 0
        CopyInstance = 1
        CopyPart = 2
    

    class InstallOption(enum.Enum):
        AddInstance = 0
        NewComponent = 1
    

class MoldFeatureRecognitionBuilder(Builder):
    def __init__(self) -> None: ...
    def AnalyzeMoldBody(self) -> None:
        ...
    def AnalyzeMoldBodyByMode(self, analyseMode: Tooling.MoldFeatureRecognitionBuilder.AnalysisModeType) -> None:
        ...
    def ExportResult(self) -> None:
        ...
    def SetProductOrientation(self, matrix: Matrix3x3) -> None:
        ...
    def GetProductOrientation(self) -> Matrix3x3:
        ...
    def ReleaseAllProductFeatureData(self) -> None:
        ...
    def FindMoldFeatures(self) -> None:
        ...
    def SetIsCoreCavityFaceChanged(self, status: bool) -> None:
        ...
    def AssignFeatureFaceColor(self, assignOrRestore: bool) -> None:
        ...
    def SetProductInformation(self) -> None:
        ...
    def SetFeatureFaceColorValue(self, colorId: NXColor) -> None:
        ...
    def ChangeColorSettingValue(self) -> None:
        ...
    def GetActivePage(self) -> int:
        ...
    def SetActivePage(self, activeTableIndex: int) -> None:
        ...
    def ValidateFeaturesZeroDimension(self, message: str) -> bool:
        ...
    def IsFeatureDataEmpty(self, costFeatureType: Tooling.MoldFeatureRecognitionBuilder.CostFeatureType, needCheckUserCreated: bool) -> bool:
        ...
    def GetMoldCostDataObject(self) -> TaggedObject:
        ...
    def SetRefineFactor(self, displayResolutionType: int) -> None:
        ...
    def UpdateFacetDisplay(self, highlightFacetType: int) -> None:
        ...
    def AskDefaultXmlFileName(self) -> str:
        ...
    def AskProductBodyOrientation(self, selBody: Body, workMatrix: Matrix3x3) -> Point3d:
        ...
    def DrawSliderDirection(self, costObject: TaggedObject) -> None:
        ...
    def EraseSliderDirection(self) -> None:
        ...
    def DeleteMoldingFeatures(self, costObjects: typing.List[Tooling.CostDataObject]) -> None:
        ...
    def AddMoldingFeature(self) -> Tooling.CostDataObject:
        ...
    def SplitUnderCut(self, selectedUndercut: Tooling.UnderCutData, newUndercuts: typing.List[Tooling.UnderCutData]) -> None:
        ...
    def GroupMoldingFeatures(self, costObject: typing.List[Tooling.CostDataObject]) -> Tooling.CostDataObject:
        ...
    def UngroupMoldingFeature(self, costObjects: typing.List[Tooling.CostDataObject], ungroupedObjects: typing.List[Tooling.CostDataObject]) -> None:
        ...
    def ShowBoundingBoxOfBody(self) -> None:
        ...
    def RefreshCostObjectComputedProperties(self, costObject: Tooling.CostDataObject) -> None:
        ...
    def CloseDisplay(self, originalMode: int) -> None:
        ...
    def ChangeSliderDirectionBasedOnBoundingBox(self, costObject: Tooling.CostDataObject, boxFeature: Features.ToolingBox) -> None:
        ...
    def CreateBoundingBox(self, costObject: Tooling.CostDataObject) -> Features.ToolingBox:
        ...
    def DeleteBoundingBoxFeature(self, boxFeature: Features.ToolingBox) -> None:
        ...
    def PopulateBoxDataToCostFeature(self, boxFeature: Features.ToolingBox, costObject: Tooling.CostDataObject) -> None:
        ...
    def AskCurrentActiveDataProvider(self) -> Tooling.CostTableDataProvider:
        ...
    def CollectUndercuts(self, pCostObjects: typing.List[Tooling.UnderCutData]) -> None:
        ...
    def UpdateProviderData(self, pDataProvider: Tooling.CostTableDataProvider, pCostObjects: typing.List[Tooling.CostDataObject]) -> None:
        ...
    def CollectOpeningAreas(self, pCostObjects: typing.List[Tooling.OpeningAreaData]) -> None:
        ...
    def CollectRibs(self, pCostObjects: typing.List[Tooling.RibsData]) -> None:
        ...
    def AskFacetsOfFaces(self, selectedFaces: typing.List[Face], facetsId: int) -> None:
        ...
    def AddFacetsToFeatureOrCreateNewOne(self, type: int, facetsId: int, costFeature: Tooling.CostDataObject) -> None:
        ...
    def RemoveFacetsFromAllCostObjects(self, type: int, facetsId: int) -> None:
        ...
    def AskCostFeatureFromSelectionAndPoint(self, selFace: NXObject, point: Point3d, minDistElem: int) -> Tooling.CostDataObject:
        ...
    def AskFeatureRelatedFacesWithChildren(self, costObjectTag: Tooling.CostDataObject, pFacesTags: typing.List[Face]) -> None:
        ...
    def PerformFacetAnalysis(self) -> None:
        ...
    def CreateConvergentBodyAndGetUndercutsData(self, undercuts: typing.List[Tooling.UnderCutData], undercutBodyNumberList: int, convergentBodyList: typing.List[Body], undercutParameterLength: int, allUndercutStringValueLists: str) -> None:
        ...
    def CreateConvergentBodyAndGetRibsData(self, ribs: typing.List[Tooling.RibsData], ribBodyNumberList: int, convergentBodyList: typing.List[Body], ribParameterLength: int, allRibsStringValueLists: str) -> None:
        ...
    def CreateConvergentBodyAndGetInsertsData(self, inserts: typing.List[Tooling.OpeningAreaData], insertBodyNumberList: int, convergentBodyList: typing.List[Body], insertParameterLength: int, allInsertStringValueLists: str) -> None:
        ...
    def SaveAnalysisResultToPart(self) -> None:
        ...
    def ClearExistingAnalysisResult(self) -> None:
        ...
    def CheckAnalysisResult(self, productBody: Body, drawingVector: Vector3d, hasAnalysisResult: bool, hasDifferentBody: bool, hasDifferentVector: bool) -> None:
        ...
    def AnalyzeMoldBodyByModeInCloudApp(self, analyseMode: Tooling.MoldFeatureRecognitionBuilder.AnalysisModeType) -> None:
        ...
    def CheckAnalysisStatus(self, productBody: Body, drawingVector: Vector3d, bFaceAnalyzed: bool, bUndercutAnalyzed: bool, bRibAnalyzed: bool, bOpeningAreaAnalyzed: bool, hasDifferentBody: bool, hasDifferentVector: bool) -> None:
        ...
    def CalculateWallThickness(self) -> None:
        ...
    AutoRibGrouping: bool
    BodyProjectArea: float
    BodySurfaceArea: float
    CostFeatureFacesColor: NXColor
    DisplayResolutionOptions: Tooling.MoldFeatureRecognitionBuilder.DisplayResolutionType
    DraftAngle: Expression
    MaximumRibLength: Expression
    MaximumRibThickness: Expression
    MaximumWallThickness: float
    MinimumWallThickness: float
    MinimumXDimension: float
    MinimumYDimension: float
    MinimumZDimension: float
    OpeningAreaDataProvider: Tooling.CostTableDataProvider
    OpeningFeatureFacesColor: NXColor
    PartFolderBrowser: str
    PartVolume: float
    RibFeatureFacesColor: NXColor
    RibsDataProvider: Tooling.CostTableDataProvider
    SaveAndExportStatus: bool
    SelectionBody: SelectBody
    TransparentMode: bool
    UndercutDataProvider: Tooling.CostTableDataProvider
    UndercutFeatureFacesColor: NXColor
    UndercutMinimumWidth: Expression
    UndercutToleranceAngle: Expression
    XDimension: float
    XmlFileName: str
    XmlFolderBrowser: str
    YDimension: float
    ZDimension: float


    class DisplayResolutionType(enum.Enum):
        Standard = 0
        Medium = 1
        Fine = 2
        ExtraFine = 3
    

    class CostFeatureType(enum.Enum):
        Undercut = 0
        Rib = 1
        Opening = 2
    

    class AnalysisModeType(enum.Enum):
        CostMoldFullAnalysis = 0
        CostMoldAnalysisWithoutWallThickness = 1
        CostMoldSplitFacesAndAnalysis = 2
        CostMoldFaceAnalysisOnly = 3
        CostMoldWallThicknessOnly = 4
        CostMoldUndercutsOnly = 5
        CostMoldRibsOnly = 6
        CostMoldOpeningsOnly = 7
        Nothing = 8
    

class MoldDesignCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MoldDesign]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFlowAnalysisBuilder(self) -> Tooling.FlowAnalysisBuilder:
        ...
    def CreateFlowDisplayBuilder(self, moldex3DResult: DisplayableObject) -> Tooling.FlowDisplayBuilder:
        ...
    def Tag(self) -> Tag: ...



class MoldDesign(Builder):
    def __init__(self) -> None: ...


class MoldCsysCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.MoldCsysBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateMoldCsysBuilder(self) -> Tooling.MoldCsysBuilder:
        ...
    def Tag(self) -> Tag: ...



class MoldCsysBuilder(Builder):
    def __init__(self) -> None: ...
    def CancelMoldCsys(self) -> None:
        ...
    def DestroyMoldCsys(self) -> None:
        ...
    def Initialize(self) -> None:
        ...
    def UpdateSelectedCsys(self, csysTag: CoordinateSystem) -> None:
        ...
    def OpenOriginalProdPartQuietly(self, displayMessage: bool, prodPart: NXObject, prodBody: NXObject) -> None:
        ...
    def UpdateBodyBox(self) -> None:
        ...
    def RepositionProductPart(self, csysMatrix: float) -> None:
        ...
    Lockx: bool
    Locky: bool
    Lockz: bool
    Prod: SelectFaceList
    Wcstype: Tooling.MoldCsysBuilder.Wcsposition


    class Wcsposition(enum.Enum):
        CurrentWcs = 0
        ProductBodyCenter = 1
        BoundaryFaceCenter = 2
    

class MoldCostProductData(Tooling.CostDataObject):
    def __init__(self) -> None: ...


class ManufacturingGeometryCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ManufacturingGeometryBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.ManufacturingGeometryBuilder:
        ...
    def CreateFaceAttributeBuilder(self) -> Tooling.FaceAttributeBuilder:
        ...
    def Tag(self) -> Tag: ...



class ManufacturingGeometryBuilder(Builder):
    def __init__(self) -> None: ...
    def GetFaceColor(self) -> int:
        ...
    def SetFaceColor(self, faceColor: int) -> None:
        ...
    def InitializeGeometry(self) -> None:
        ...
    def CreateNewSubNode(self, selNode: int) -> None:
        ...
    def InitializeContent(self, initializeWay: int) -> None:
        ...
    Face: ScCollector
    Translucency: int


class LsdynaKfileGeneratorBuilder(Builder):
    def __init__(self) -> None: ...
    def MeshObject(self) -> None:
        ...
    def CalculateMeshValue(self) -> None:
        ...
    def CreateLSDynaKFile(self, kFile: str) -> None:
        ...
    def AnalyzeFormability(self, kFile: str) -> None:
        ...
    def SetInputDynaFile(self, fileName: str) -> None:
        ...
    def SetOutputFile(self, outputFile: str) -> None:
        ...
    def SetOutputPath(self, outputPath: str) -> None:
        ...
    DataType: Tooling.LsdynaKfileGeneratorBuilder.MeshDataType
    ElementType: Tooling.LsdynaKfileGeneratorBuilder.MeshElementType
    InputDynaFile: str
    MaximumAngle: float
    MaximumDeviation: float
    MaximumElementSize: float
    MinimumElementSize: float
    OutputFile: str
    OutputPath: str
    OutputState: int
    Type: Tooling.LsdynaKfileGeneratorBuilder.OperTypes


    class OperTypes(enum.Enum):
        Mesh = 0
        Runsolver = 1
    

    class MeshElementType(enum.Enum):
        Triangle = 0
        Mixed = 1
    

    class MeshDataType(enum.Enum):
        LongBit = 0
        ShortBit = 1
    

class LsdynaGeometryPreparationBuilder(Builder):
    def __init__(self) -> None: ...
    def ExecuteRestorePosition(self) -> None:
        ...
    def ExecuteMovePosition(self) -> None:
        ...
    def GetPercentageForceArray(self, doublePercentageForceArray: float) -> None:
        ...
    def SetPercentageForceArray(self, doublePercentageForceArray: float) -> None:
        ...
    def SetDrawBeadCurves(self, drawBeadCurves: typing.List[Curve]) -> None:
        ...
    AutoPositionOption: bool
    BinderPosition: float
    BinderSheet: SelectBody
    BlankCurve: Section
    BlankOptionType: Tooling.LsdynaGeometryPreparationBuilder.BlankOption
    BlankPositionType: Tooling.LsdynaGeometryPreparationBuilder.BlankPosition
    BlankPositionValue: float
    BlankSheet: SelectBody
    BlankThickness: float
    ContactOffset: float
    ContactTypeOption: Tooling.LsdynaGeometryPreparationBuilder.ContactType
    DiePosition: float
    DieSheet: SelectBody
    DrawBeadCurves: SelectCurveList
    DrawBeadTypeOption: Tooling.LsdynaGeometryPreparationBuilder.DrawBeadType
    DrawTypeOption: Tooling.LsdynaGeometryPreparationBuilder.DrawType
    Friction: float
    MaterialName: str
    MaterialTypeOption: Tooling.LsdynaGeometryPreparationBuilder.MaterialType
    NormalForce: float
    PercentageForce: float
    ProcessBinder: float
    ProcessBinderOption: bool
    ProcessBinderType: Tooling.LsdynaGeometryPreparationBuilder.ProcessActionBinder
    ProcessDie: float
    ProcessDieOption: bool
    ProcessDieType: Tooling.LsdynaGeometryPreparationBuilder.ProcessActionDie
    ProcessPunch: float
    ProcessPunchOption: bool
    ProcessPunchType: Tooling.LsdynaGeometryPreparationBuilder.ProcessActionPunch
    ProcessTypeOption: Tooling.LsdynaGeometryPreparationBuilder.ProcessType
    PunchPosition: float
    PunchSheet: SelectBody
    RestrainForce: Expression
    TargetBinderType: Tooling.LsdynaGeometryPreparationBuilder.TargetBinder
    TargetDieType: Tooling.LsdynaGeometryPreparationBuilder.TargetDie
    TargetPunchType: Tooling.LsdynaGeometryPreparationBuilder.TargetPunch
    TensileStrength: float


    class TargetPunch(enum.Enum):
        Punch = 0
        Binder = 1
        Die = 2
    

    class TargetDie(enum.Enum):
        Punch = 0
        Binder = 1
        Die = 2
    

    class TargetBinder(enum.Enum):
        Punch = 0
        Binder = 1
        Die = 2
    

    class ProcessType(enum.Enum):
        Gravity = 0
        Closing = 1
        Drawing = 2
    

    class ProcessActionPunch(enum.Enum):
        Stationary = 0
        ClosureWith = 1
        FollowWith = 2
        Travel = 3
        UntilHome = 4
        Force = 5
    

    class ProcessActionDie(enum.Enum):
        Stationary = 0
        ClosureWith = 1
        FollowWith = 2
        Travel = 3
        UntilHome = 4
        Force = 5
    

    class ProcessActionBinder(enum.Enum):
        Stationary = 0
        ClosureWith = 1
        FollowWith = 2
        Travel = 3
        UntilHome = 4
        Force = 5
    

    class MaterialType(enum.Enum):
        NXMaterial = 0
        LSDynaMaterial = 1
    

    class DrawType(enum.Enum):
        SingleDraw = 0
        DoubleDraw = 1
    

    class DrawBeadType(enum.Enum):
        Round = 0
        Rectangle = 1
    

    class ContactType(enum.Enum):
        FormingOneWaySurfaceToSurface = 0
        FormingOneWaySurfaceToSurfaceSmooth = 1
        FormingSurfaceToSurface = 2
        FormingSurfaceToSurfaceSmooth = 3
        SurfaceToSurface = 4
        AutomaticSurfaceToSurface = 5
    

    class BlankPosition(enum.Enum):
        AboveBinder = 0
        AboveBinderandPunch = 1
    

    class BlankOption(enum.Enum):
        Sheet = 0
        Curve = 1
    

class LsdynaFormAnalysisResultDisplayBuilder(Builder):
    def __init__(self) -> None: ...
    def SetResultFileNames(self, resultFileNames: str) -> None:
        ...
    def ImportGeometries(self) -> None:
        ...
    def DisplayFormability(self) -> None:
        ...
    def DisplayStress(self) -> None:
        ...
    def DisplayStrain(self) -> None:
        ...
    def DisplayThickness(self) -> None:
        ...
    def DisplayThinning(self) -> None:
        ...
    AllowableThickening: float
    AllowableThinning: float
    EssentialThinning: float
    FormabilityStrainType: Tooling.LsdynaFormAnalysisResultDisplayBuilder.FormabilityStrainTypeName
    LimitOfFlc: float
    RValue: float
    ResultFileFolder: str
    SafetyMarginFromFlc: float
    ShowCracks: bool
    ShowInadequateStretch: bool
    ShowRiskOfCracks: bool
    ShowSevereThinning: bool
    ShowWrinkles: bool
    ShowWrinklingTendency: bool
    State: int
    StrainType: Tooling.LsdynaFormAnalysisResultDisplayBuilder.StrainTypeName
    StressType: Tooling.LsdynaFormAnalysisResultDisplayBuilder.StressTypeName


    class StressTypeName(enum.Enum):
        MaximumInplaneStress = 0
        MinimumInplaneStress = 1
    

    class StrainTypeName(enum.Enum):
        TopMajorPrincipalStrain = 0
        TopMinorPrincipalStrain = 1
        BottomMajorPrincipalStrain = 2
        BottomMinorPrincipalStrain = 3
    

    class FormabilityStrainTypeName(enum.Enum):
        TopPrincipalStrain = 0
        BottomPrincipalStrain = 1
    

class LetteringInsertBuilder(Builder):
    def __init__(self) -> None: ...
    def StandardInsert(self) -> None:
        ...
    def SelectFont(self, fontName: str, script: Tooling.LetteringInsertBuilder.ScriptOptions) -> None:
        ...
    def GetParentNames(self) -> str:
        ...
    def SetParentNames(self, parentNames: str) -> None:
        ...
    def GetSelectedFaceOccurrences(self, selectedFaceOccurrences: typing.List[TaggedObject]) -> None:
        ...
    def SetSelectedFaceOccurrences(self, selectedFaceOccurrences: typing.List[TaggedObject]) -> None:
        ...
    def PreparePDWStandardClientData(self) -> None:
        ...
    def PostProcessPDWStandardClientData(self) -> TaggedObject:
        ...
    BottomingPlateClearance: float
    BottomingPlateToggle: bool
    DiePlateClearance: float
    DiePlateToggle: bool
    DraftAngularDim: Expression
    EndDistanceLinearDim: Expression
    Font: str
    FontStyle: Tooling.LetteringInsertBuilder.FontStyleOptions
    Height: Expression
    InputLetter: str
    InsertInstanceTag: TaggedObject
    Length: Expression
    LetterDirection: Tooling.LetteringInsertBuilder.LetterDirectionOption
    OnlyAddLetteringStandardPartToggle: bool
    ParentPartName: str
    ParentPartNode: Tooling.LetteringInsertBuilder.ParentPartNodeOption
    PunchPlateClearance: float
    PunchPlateToggle: bool
    Script: Tooling.LetteringInsertBuilder.ScriptOptions
    SelectFace: ScCollector
    StartDistanceLinearDim: Expression
    StripperPlateClearance: float
    StripperPlateToggle: bool
    WizardType: int


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
    

    class ParentPartNodeOption(enum.Enum):
        NoParent = 0
    

    class LetterDirectionOption(enum.Enum):
        Up = 0
        Down = 1
    

    class FontStyleOptions(enum.Enum):
        Regular = 0
        Italic = 1
        Bold = 2
        BoldItalic = 3
    

class LayoutRepositionBuilder(Builder):
    def __init__(self) -> None: ...
    def AddCavity(self, selectedCavity: NXObject) -> None:
        ...
    def RepositionMove(self, copyOption: int) -> None:
        ...
    def RepositionRotate(self, type: int, copyOption: int) -> None:
        ...
    def RepositionPointToPoint(self, copyOption: int) -> None:
        ...
    def RepositionToOriginal(self) -> None:
        ...
    def RemoveOperation(self) -> None:
        ...
    def AddACavityToMoveCavities(self, cavityComponent: NXObject) -> None:
        ...
    def ClearMoveCavities(self) -> None:
        ...
    def AddACavityToCopyCavities(self, cavityComponent: NXObject) -> None:
        ...
    def ClearCopyCavities(self) -> None:
        ...
    DimX: Expression
    DimY: Expression
    PointFrom: Point
    PointTo: Point
    RepositionMethod: Tooling.LayoutRepositionBuilder.Method
    RepositionType: Tooling.LayoutRepositionBuilder.Type
    RotateAngle: Expression
    RotatePoint: Point
    SelectInstance: SelectNXObjectList


    class Type(enum.Enum):
        Move = 0
        Copy = 1
    

    class Method(enum.Enum):
        Rotate = 0
        Transform = 1
        PointToPoint = 2
    

class LayoutManagementCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.LayoutManagementBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLayoutManagementBuilder(self) -> Tooling.LayoutManagementBuilder:
        ...
    def Tag(self) -> Tag: ...



class LayoutManagementBuilder(Builder):
    def __init__(self) -> None: ...
    def AddObject(self) -> None:
        ...
    def RemoveObject(self) -> None:
        ...
    def MoveToStation(self) -> None:
        ...
    def AddStationAfter(self, currentStationPart: NXObject) -> None:
        ...
    def DeleteStationPart(self, stationPart: NXObject) -> None:
        ...
    def IncreaseStationParts(self) -> None:
        ...
    def DecreaseStationParts(self) -> None:
        ...
    def UpdateStation(self, stationPartOcc: NXObject, newStationName: str, newDistance: float) -> None:
        ...
    def CreateLayoutWithViews(self) -> None:
        ...
    def ExitStationManagement(self) -> None:
        ...
    def CreatePmiNote(self) -> None:
        ...
    def CreatePMIForNewStation(self) -> None:
        ...
    BodiesReposition: SelectBodyList
    MoveToStationEnum: Tooling.LayoutManagementBuilder.MoveToStationEnumeration
    NewStationPart: NXObject
    ReferencePoint: Point
    RepositionMotion: GeometricUtilities.ModlMotion
    SelectEntityAdd: SelectNXObjectList
    SelectEntityRemove: SelectNXObjectList
    SelectObject: SelectNXObjectList
    SpecifyDieTip: Direction
    StationDistance: float
    StationEnum: Tooling.LayoutManagementBuilder.StationItems
    StationNameStr: str
    StationNumber: int
    WizardType: Tooling.ToolingApplication


    class StationItems(enum.Enum):
        One = 0
        Two = 1
        Three = 2
    

    class MoveToStationEnumeration(enum.Enum):
        Op00 = 0
        Op10 = 1
        Op20 = 2
    

    class YrefNum(enum.Enum):
        Block = 0
        Move = 1
    

class LayoutBuilder(Builder):
    def __init__(self) -> None: ...
    def Layout(self) -> None:
        ...
    def Insertpocket(self) -> None:
        ...
    def Transform(self) -> None:
        ...
    def Remove(self) -> None:
        ...
    def Autocenter(self) -> None:
        ...
    def CreateLayout(self) -> None:
        ...
    def PutLayoutInfo(self) -> None:
        ...
    def RemoveCavitiesFromLayout(self) -> None:
        ...
    def AddACavity(self, aCavity: Assemblies.Component) -> None:
        ...
    def RemoveACavity(self, aCavity: Assemblies.Component) -> None:
        ...
    def ClearSelectedCavities(self) -> None:
        ...
    BalCavityNumber: Tooling.LayoutBuilder.BalNumber
    CirCavityNumber: int
    CirRadius: float
    CirRotateAngle: float
    CirStartAngle: float
    DimBalFirst: Expression
    DimBalSecond: Expression
    DimXdist: Expression
    DimYdist: Expression
    LayoutVector: Direction
    LinXnumber: int
    LinYnumber: int
    MwLayoutType: Tooling.LayoutBuilder.LayoutType
    RotatePoint: Point
    SelectCavity: SelectNXObjectList
    SubType: Tooling.LayoutBuilder.LayoutSubType
    Xref: Tooling.LayoutBuilder.XrefNum
    Yref: Tooling.LayoutBuilder.YrefNum


    class XrefNum(enum.Enum):
        Block = 0
        Move = 1
    

    class LayoutType(enum.Enum):
        Rectangle = 0
        Circular = 1
    

    class LayoutSubType(enum.Enum):
        Balance = 0
        Linear = 1
        Radial = 2
        Constant = 3
    

    class BalNumber(enum.Enum):
        Two = 0
        Four = 1
    

class IntermediateStageCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.IntermediateStageBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateIntermediateStageBuilder(self) -> Tooling.IntermediateStageBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Tooling.IntermediateStageBuilder:
        ...
    def Tag(self) -> Tag: ...



class IntermediateStageBuilder(Builder):
    def __init__(self) -> None: ...
    def DirectUnfoldProjectInitialize(self) -> NXObject:
        ...
    def UpdateStartStation(self, parentPart: Part) -> None:
        ...
    def UpdatePitchOrientation(self, parentPart: Part, originalPart: NXObject) -> None:
        ...
    def IncreaseIntermediateStages(self, parentPart: Part, originalPart: NXObject, numOldStage: int) -> None:
        ...
    def DecreaseIntermediateStages(self, parentPart: Part, originalPart: NXObject, numOldStage: int) -> None:
        ...
    def InsertIntermediateStages(self, parentPart: Part, originalPart: NXObject, selectPart: NXObject) -> None:
        ...
    def DeleteIntermediateStages(self, parentPart: Part, originalPart: NXObject, selectPart: NXObject) -> None:
        ...
    CreateCopyPart: bool
    DesignSequence: Tooling.IntermediateStageBuilder.DesignSequences
    DirectUnfoldParent: Part
    EditOption: Tooling.IntermediateStageBuilder.EditOptions
    IntermediateNamingRule: str
    IntermediateRename: bool
    IntermediateStage: Assemblies.SelectComponent
    LinkSheetBody: bool
    NumberIntermediate: int
    OrientPitch: Tooling.IntermediateStageBuilder.Orientations
    Pitch: float
    StartStation: int
    TopPartName: str


    class Orientations(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class EditOptions(enum.Enum):
        Insert = 0
        Delete = 1
    

    class DesignSequences(enum.Enum):
        PartToBlank = 0
        BlankToPart = 1
    

class InsertTextBuilder(Builder):
    def __init__(self) -> None: ...
    def GetScript(self) -> Features.TextBuilder.ScriptOptions:
        ...
    def SetScript(self, script: Features.TextBuilder.ScriptOptions) -> None:
        ...
    def UpdateTextPreview(self, udoTag: NXObject) -> None:
        ...
    def UpdateTextLocation(self, objectTag: NXObject, moveVector: Vector3d, currentHandle: int, angle: float) -> Group:
        ...
    def CreateNewTextUDO(self, faceTag: Face, attribute: str, udoTag: NXObject) -> str:
        ...
    def SetTextUDOAttributeName(self, udoTag: NXObject, attributeNmae: str) -> None:
        ...
    def SetTextUDODefaultText(self, udoTag: NXObject, text: str, previewText: bool) -> None:
        ...
    def SetTextUDOStartNumber(self, udoTag: NXObject, numberStr: str, previewText: bool) -> None:
        ...
    def UpdateTextUDOClientUIData(self, udoTag: NXObject, index: int) -> None:
        """[Obsolete("Deprecated in NX2007.0.0.  Use JA_TOOLING_INSERT_TEXT_BUILDER_UpdateTextUDOClientData instead.")"""
        ...
    def UpdateTextUDOClientData(self, index: int, previewText: bool) -> None:
        ...
    def AddOrRemoveUDOSelectedHole(self, udoTag: NXObject, holeEdge: Edge, isAdding: bool) -> None:
        ...
    def SetSelectedAttributesTreeNodes(self, nodeTags: typing.List[NXObject]) -> None:
        ...
    def GetTextAnchorPointMatrix(self, objectTag: NXObject, origin: Point3d) -> Matrix3x3:
        ...
    def DeleteTexts(self, holeEdges: typing.List[Edge]) -> None:
        ...
    def SetLastSelectedFace(self, faceTag: Face) -> None:
        ...
    def RecordFaceHolesData(self, faceTag: Face, recordAllHoles: bool, holeEdge: Edge, isAdding: bool) -> None:
        ...
    def SetEditFeatureGroup(self, featureGroup: NXObject) -> None:
        ...
    def ImplementInitFromUDO(self) -> None:
        ...
    def SetSingleTextUDO(self, udoTag: NXObject) -> None:
        ...
    def CleanUpRedundantData(self) -> None:
        ...
    BoundaryColor: NXColor
    BoundaryType: Tooling.InsertTextBuilder.TextBoundaryType
    BoundingDepth: Expression
    ComponentTextHeight: Expression
    CreateComponentText: bool
    CreateEmbossedText: bool
    CreateVShapeText: bool
    CsysMatrix: Matrix3x3
    CsysOrigin: Point3d
    FontHeight: Expression
    FontName: str
    InsertTextType: Tooling.InsertTextBuilder.InsertType
    LetteringDepth: Expression
    NumberingDirection: Tooling.InsertTextBuilder.NumberDirectionOption
    NumberingWidth: Expression
    Offset: Expression
    SelectFace: ScCollector
    SelectHoleEdges: ScCollector
    TextColor: NXColor
    TextLayer: int
    TextPosition: Tooling.InsertTextBuilder.TextPositionOption
    TextRule: str


    class TextPositionOption(enum.Enum):
        TopLeft = 0
        TopCenter = 1
        TopRight = 2
        MiddleLeft = 3
        MiddleRight = 4
        BottomLeft = 5
        BottomCenter = 6
        BottomRight = 7
    

    class TextBoundaryType(enum.Enum):
        None = 0
        Slot = 1
        Rectangle = 2
    

    class NumberDirectionOption(enum.Enum):
        AlongXAxis = 0
        AlongYAxis = 1
    

    class InsertType(enum.Enum):
        ThroughPoint = 0
        ThroughHole = 1
    

class InsertQRBarCodeBuilder(Builder):
    def __init__(self) -> None: ...
    def SetCodeType(self, codeType: Tooling.InsertQRBarCodeBuilder.Code) -> None:
        ...
    def SetQRCodeBuilder(self, qrCodeBuilder: Tooling.RasterImageBuilder) -> None:
        ...
    def SetBarCodeBuilder(self, barCodeBuilder: Tooling.InsertBarcodeBuilder) -> None:
        ...
    def GetTargetObjectForQRCode(self) -> Plane:
        ...
    def SetTargetObjectForQRCode(self, targetObj: Plane) -> None:
        ...
    def GetTargetObjectForBarCode(self) -> Plane:
        ...
    def SetTargetObjectForBarCode(self, targetObj: Plane) -> None:
        ...
    def DeleteBarCode(self) -> None:
        ...
    def DeleteQRCode(self) -> None:
        ...
    def GenerateQRCode(self) -> None:
        ...
    def EditBarCodeText(self) -> None:
        ...
    def GenerateBarCode(self) -> None:
        ...
    CodeRule: str


    class Code(enum.Enum):
        QRCode = 0
        BarCode = 1
    

class InsertEditToolsBuilder(Builder):
    def __init__(self) -> None: ...
    def ReparentComponent(self, componentName: str, parentName: str) -> None:
        ...
    def GetAllNeedReparentInsertGroups(self, insertTags: typing.List[NXObject]) -> None:
        ...
    def AskNewParentNameOfInsert(self, insertTag: NXObject) -> str:
        ...
    ControlPoint: Point
    CopySelectInsert: SelectBodyList
    DestinationPoint: Point
    InsertsToDelete: SelectBodyList
    ReparentSelectInsert: Assemblies.SelectComponentList
    ShanksToDelete: ScCollector
    Type: Tooling.InsertEditToolsBuilder.Types
    UpdateExpressionWithoutParentChange: bool


    class Types(enum.Enum):
        Copy = 0
        Delete = 1
        ChangeParent = 2
        UpdateAllInsertPosition = 3
    

class InsertBlockBuilder(Builder):
    def __init__(self) -> None: ...
    def StandardInsertBlock(self) -> None:
        ...
    def CreateUserDefinedInsertDatumPlane(self) -> None:
        ...
    def DeleteUnusedDatumAndSketch(self) -> None:
        ...
    def AddInsertBlockPart(self) -> None:
        ...
    def SetManipulatorToMatrixAndPosition(self, matrix: Matrix3x3, position: Point3d) -> None:
        ...
    def CalculateBoxSize(self) -> None:
        ...
    def CreateUserDefinedInsertBlock(self) -> None:
        ...
    BlockShimDistance: float
    BoundingBoxType: Tooling.InsertBlockBuilder.BoundingBoxTypeItems
    BoxPosition: Point3d
    ClearanceToggle: bool
    ConceptDesign: bool
    FacesSelect: SelectBodyList
    InsertBlockClearance: float
    InsertBlockType: Tooling.InsertBlockBuilder.InsertBlockTypeItems
    InsertMode: Tooling.InsertBlockBuilder.InsertModeItems
    InsertToDelete: Assemblies.SelectComponentList
    InsertToEdit: Assemblies.SelectComponentList
    InsertType: Tooling.InsertBlockBuilder.Types
    NewPartNames: str
    OffsetValueLinearDimensionNegativeX: Expression
    OffsetValueLinearDimensionNegativeY: Expression
    OffsetValueLinearDimensionNegativeZ: Expression
    OffsetValueLinearDimensionPositiveX: Expression
    OffsetValueLinearDimensionPositiveY: Expression
    OffsetValueLinearDimensionPositiveZ: Expression
    ParentPartName: str
    RadialOffset: Expression
    RenameDialog: bool
    SelectInsertBlockOutline: Section
    SelectVector: Direction
    StandardInsertBlockTag: TaggedObject
    UserDefBlockDatumPlane: TaggedObject
    UserDefinedInsertBlockHeight: Expression
    WithoutFalseBody: bool


    class Types(enum.Enum):
        InsertBlock = 0
        EditBlock = 1
        DeleteBlock = 2
    

    class InsertModeItems(enum.Enum):
        StandardBlock = 0
        SketchProfile = 1
        BoundingBox = 2
    

    class InsertBlockTypeItems(enum.Enum):
        PunchBlock = 0
        BottomingBlock = 1
        StripperBlock = 2
    

    class BoundingBoxTypeItems(enum.Enum):
        Block = 0
        Cylinder = 1
    

class InsertBarcodeBuilder(Builder):
    def __init__(self) -> None: ...
    def SetManipulatorOrigin(self, origin: Point3d) -> None:
        ...
    def SetManipulatorOrientation(self, orientation: Matrix3x3) -> None:
        ...
    def GetBarcodeTag(self) -> Annotations.SimpleDraftingAid:
        ...
    def SetBarcodeTag(self, barcodeTag: Annotations.SimpleDraftingAid) -> None:
        ...
    def IsMultipleBarcodes(self) -> bool:
        ...
    def SetIsMultipleBarcodes(self, isMultipleBarcodes: bool) -> None:
        ...
    def IsBarcodeQualified(self) -> bool:
        ...
    def SetBarcodeQualified(self, qualify: bool) -> None:
        ...
    def UpdateBarCode(self) -> None:
        ...
    def RotateBarCodeAroundZ(self, angle: float) -> None:
        ...
    BarcodeHeight: float
    Basepoint: Annotations.OriginBuilder.AlignmentPosition
    ColorPicker: int
    TargetObject: Plane


class InsertAuxiliaryCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.InsertAuxiliaryBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateInsertAuxiliaryBuilder(self) -> Tooling.InsertAuxiliaryBuilder:
        ...
    def Tag(self) -> Tag: ...



class InsertAuxiliaryBuilder(Builder):
    def __init__(self) -> None: ...
    def DesignMountHead(self) -> None:
        ...
    BlendRadius: float
    BottomPlateClearance: float
    CircDeleteAllComponents: bool
    CircularInsert: SelectBody
    CircularOperation: Tooling.InsertAuxiliaryBuilder.CircOperationTypes
    CircularVector: Direction
    ClearanceValue: float
    ControlPoint: Point
    CopySelectInsert: SelectBodyList
    CreateCurvesToDivideFace: Section
    DesignTool: Tooling.InsertAuxiliaryBuilder.DesignToolOption
    DestinationPoint: Point
    FaceForRamp: ScCollector
    FalseBodyHeight: Expression
    HeelFalseHeightClearance: float
    HeelHeight: float
    HeelLength: float
    HeelRadian: float
    HeelTypes: Tooling.InsertAuxiliaryBuilder.HeelTypesType
    HeelWidth: float
    InsertEdge: SelectEdge
    InsertShankFace: ScCollector
    InsertsToDelete: SelectBodyList
    MountPunchEdge: SelectEdge
    MountPunchFace: ScCollector
    OffsetAngle: float
    OffsetX: float
    OffsetY: float
    PointForRamp: Point
    Punch: SelectBody
    PunchEdge: SelectEdge
    PunchPlateClearance: float
    PunchShankFace: ScCollector
    PunchShankParaC: float
    PunchShankParaFL: float
    PunchShankParaL1: float
    PunchShankParaLength: float
    PunchShankParaPL: float
    PunchShankParaR: float
    PunchShankParaWidth: float
    RadiusForRamp: Expression
    RampShankHeight: Expression
    RampSteps: Tooling.InsertAuxiliaryBuilder.RampStepsType
    RectDeleteAllComponents: bool
    RectangularInsert: SelectBody
    RectangularOperation: Tooling.InsertAuxiliaryBuilder.RectOperationOption
    RectangularXVector: Direction
    RectangularYVector: Direction
    SelectFaceToDivide: SelectFace
    SelectInsertToDeleteRamp: SelectBody
    SelectRampFeature: SelectNXObjectList
    SelectShankProfile: Section
    ShankShape: Tooling.InsertAuxiliaryBuilder.ShankShapeTypes
    ShanksToDelete: ScCollector
    SketchToRevolve: Section
    StripperPlateClearance: float
    TotalAlongX: int
    TotalAlongY: int
    TotalNumber: int
    Type: Tooling.InsertAuxiliaryBuilder.Types
    UseBottomPlateClearance: bool
    UseClearance: bool
    UseFaceOrSketch: Tooling.InsertAuxiliaryBuilder.UseFaceOrSketchToRevolve
    UsePunchPlateClearance: bool
    UseStripperPlateClearance: bool
    VectorForRamp: Direction


    class UseFaceOrSketchToRevolve(enum.Enum):
        Face = 0
        Sketch = 1
    

    class Types(enum.Enum):
        InsertFlange = 0
        InsertRamp = 1
        InsertHeel = 2
        PunchMount = 3
        Tools = 4
    

    class ShankShapeTypes(enum.Enum):
        Flange = 0
        Ramp = 1
        Heel = 2
    

    class RectOperationOption(enum.Enum):
        Create = 0
        Edit = 1
        Delete = 2
    

    class RampStepsType(enum.Enum):
        AddMaterial = 0
        CreateCurvesAndDivideFace = 1
        CreateRamp = 2
        DeleteRamp = 3
    

    class HeelTypesType(enum.Enum):
        RType = 0
        CType = 1
    

    class DesignToolOption(enum.Enum):
        Copy = 0
        Array = 1
        Delete = 2
    

    class CircOperationTypes(enum.Enum):
        Create = 0
        Edit = 1
        Delete = 2
    

class InitProjectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.InitProjectBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.InitProjectBuilder:
        ...
    def Tag(self) -> Tag: ...



class InitProjectBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateProject(self, cloneObject: Tooling.CloneObject) -> Part:
        ...
    def CreateCloneObject(self, templatePartName: str) -> Tooling.CloneObject:
        ...
    def AskInstallingPartName(self) -> str:
        ...
    def CheckProductPartNodeExistence(self, bProdNodeExist: bool) -> str:
        ...
    def AddProductAssemblyNode(self, cloneObject: Tooling.CloneObject) -> Part:
        ...
    def AssignProjectAttributes(self, topPart: Part, prodPart: Part) -> None:
        ...
    def SetWorkPieceUdoClassId(self, udoID: int) -> None:
        ...
    def SetProjectPathAndName(self, path: str, projectName: str) -> None:
        ...
    def AskProductTemplatePartName(self) -> str:
        ...
    def PopulateFamilyMoldData(self, topPartName: str) -> None:
        ...
    def FamilyMoldPostProcess(self, plasticPartName: str, productBody: typing.List[Body], cloneObject: Tooling.CloneObject) -> None:
        ...
    def AskConfigurationNames(self) -> str:
        ...
    def AskShrinkageFromMaterial(self, materialName: str) -> str:
        ...
    def AskProjectData(self, type: int, attrNameList: str) -> str:
        ...
    def UpdateProjectAttribute(self, attributeName: str, attributeValue: str) -> None:
        ...
    def UpdateCurrentConfigData(self, configName: str) -> None:
        ...
    def SeparateObjects(self, selected: typing.List[NXObject], deselected: typing.List[NXObject]) -> None:
        ...
    def AskShrinkageFeature(self, bUpdate: bool) -> Features.Feature:
        ...
    BodySelect: SelectBodyList
    Configuration: Tooling.InitProjectBuilder.ConfigurationId
    ConfigurationName: str
    IsDragFromReuseLib: bool
    Material: Tooling.InitProjectBuilder.MaterialId
    MaterialName: str
    PathName: str
    ProjectName: str
    Rename: bool
    Shrinkage: str
    Unit: Tooling.InitProjectBuilder.UnitId


    class UnitId(enum.Enum):
        Millimeter = 0
        Inch = 1
    

    class MaterialId(enum.Enum):
        None = 0
        Nylon = 1
    

    class ConfigurationId(enum.Enum):
        Default = 0
        Orig = 1
    

class InitProjCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.InitProjBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateInitProjBuilder(self) -> Tooling.InitProjBuilder:
        ...
    def Tag(self) -> Tag: ...



class InitProjBuilder(Builder):
    def __init__(self) -> None: ...
    def ProjPathButton(self) -> None:
        ...
    def MatLibButton(self) -> None:
        ...
    def ProjTempBut(self) -> None:
        ...
    def InitNewProject(self, templateName: str) -> None:
        ...
    def InitInsertPartsToProject(self, partNames: str, radId: int) -> None:
        ...
    def OpenChangeMaterial(self) -> None:
        ...
    def OpenChangeThickness(self) -> None:
        ...
    def HideOriginalParts(self) -> None:
        ...
    def AskAttributeData(self, attrNameList: str) -> str:
        ...
    def UpdateProjectAttribute(self, attributeName: str, attributeValue: str) -> None:
        ...
    def AssignProjectAttributes(self, controlPart: Part) -> None:
        ...
    InsertStripTog: bool
    PartMatStr: str
    PartThickReal: float
    PartUnitStr: str
    PathName: str
    ProjPathStr: str
    ProjTempOpt: Tooling.InitProjBuilder.ProjTempOption
    ProjectName: str
    RenameDiaTog: bool
    StationaryFace: ScCollector
    UseSmfeatTog: bool


    class ProjTempOption(enum.Enum):
        Default = 0
    

class HoleTableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.HoleTableBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateHoleTableBuilder(self, holeTable: Annotations.Table) -> Tooling.HoleTableBuilder:
        ...
    def Tag(self) -> Tag: ...



class HoleTableBuilder(Annotations.HoleTableBuilder):
    def __init__(self) -> None: ...
    UseCustomTypeSymbol: bool


class HoleReportCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.HoleReportBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateHoleReportBuilder(self) -> Tooling.HoleReportBuilder:
        ...
    def Tag(self) -> Tag: ...



class HoleReportBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateOrdinateOrigin(self, quadrant: int, viewTag: TaggedObject, pointData: Point3d) -> TaggedObject:
        ...
    CreatedOrdinateOrigin: TaggedObject
    HoleTable: SelectEdgeList
    OrdinateOrigin: SelectPointList
    QuadrantType: Tooling.HoleReportBuilder.EnumQuadrantType
    SelectionType: Tooling.HoleReportBuilder.EnumSelectionType
    TableAddHole: SelectEdgeList
    TableHole: SelectEdgeList
    TableOrigin: Point
    TableView: Drawings.SelectDraftingViewList
    Type: Tooling.HoleReportBuilder.Types


    class Types(enum.Enum):
        CreateTable = 0
        UpdateTable = 1
    

    class EnumSelectionType(enum.Enum):
        ViewSelection = 0
        WindowSelection = 1
    

    class EnumQuadrantType(enum.Enum):
        PositiveQuadrantI = 0
        PositiveQuadrantIi = 1
        PositiveQuadrantIii = 2
        PositiveQuadrantIv = 3
        PositiveQuadrantAll = 4
    

class HoleManufacturingNoteCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.HoleManufacturingNoteBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateHoleManufacturingNoteBuilder(self) -> Tooling.HoleManufacturingNoteBuilder:
        ...
    def Tag(self) -> Tag: ...



class HoleManufacturingNoteBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateHoleIndexLabel(self, viewTag: NXObject, holeTypeIndex: str, faceTag: NXObject, holeDiameter: float, holePos: Point3d, holetype: str, reverseFlag: bool) -> NXObject:
        ...
    def CreateHoleManufacturingNoteAsNote(self, viewTag: NXObject, holeManufacturingNoteVector: str, point: Point3d) -> NXObject:
        ...
    def CycleObjectsInView(self, viewTag: NXObject, vseqNumber: int, isDrawing: bool, inObject: NXObject) -> NXObject:
        ...
    def ModifyStyle(self) -> None:
        ...
    CreatedHoleManufacturingNote: NXObject
    DefineByViewOrHolesEnum: Tooling.HoleManufacturingNoteBuilder.DefineByViewOrHoles
    HoleIndexColor: NXColor
    HoleIndexSize: float
    HoleIndexTypeEnum: Tooling.HoleManufacturingNoteBuilder.HoleIndexType
    HoleManufacturingNoteColor: NXColor
    HoleManufacturingNoteOrigin: Annotations.OriginBuilder
    HoleManufacturingNoteSize: float
    HoleManufacturingNoteStyle: Annotations.StyleBuilder
    SelectHoles: SelectNXObjectList
    SelectView: SelectNXObject
    UseDifferentSubIndexForSameDiameterHoles: bool
    WizardType: int


    class HoleIndexType(enum.Enum):
        UserDefinedAndNumber = 0
        Alphabetic = 1
        Numeric = 2
    

    class DefineByViewOrHoles(enum.Enum):
        View = 0
        Holes = 1
    

class HoleDatumSymbolBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateSymbolSizeInView(self) -> None:
        ...
    def CycleObjectsInView(self, viewTag: NXObject, vseqNumber: int, isDrawing: bool, inObject: NXObject) -> NXObject:
        ...
    AttributeTitles: str
    AttributeValues: str
    HoleDiameter: float
    HoleTolerance: float
    HoleType: Tooling.HoleDatumSymbolBuilder.SymbolType
    SelectHoles: SelectNXObjectList
    SelectHolesAccordingToAttribute: bool
    SelectSpreadsheet: str
    SelectView: Drawings.SelectDraftingViewList
    WizardType: int


    class SymbolType(enum.Enum):
        First = 0
        Second = 1
        Third = 2
        Fourth = 3
    

class HemFixerBuilder(Builder):
    def __init__(self) -> None: ...
    BendFace: ScCollector
    BendRadius: Expression
    FlangeFace: ScCollector


class GuidedExtensionManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def CreateBuilder(self) -> Tooling.GuidedExtensionBuilder:
        ...
    def Tag(self) -> Tag: ...



class GuidedExtensionBuilder(Builder):
    def __init__(self) -> None: ...
    def ResetAllSegments(self) -> None:
        ...
    def UpdateSheetEdges(self) -> None:
        ...
    def SetSelectedSegmentType(self, segmentType: Tooling.GuidedExtensionBuilder.SegmentType) -> None:
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
    def SetLastSelectedLoopIndex(self, lastSelectedLoopIndex: int) -> None:
        ...
    def SetReverseExtendDirection(self, reverseExtendDirection: bool) -> None:
        ...
    AngleTolerance: float
    CheckSurfaces: bool
    DistanceTolerance: float
    ExtendLength: Expression
    GuideLineAngle1: Expression
    GuideLineAngle2: Expression
    SegmentEdges: ScCollector
    SheetEdges: Section


    class SegmentType(enum.Enum):
        Normal = 0
        Transition = 1
        Bypass = 2
    

class GeneralInsertBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateDatum(self) -> None:
        ...
    def AddFromSpreadsheetAttributeList(self) -> None:
        ...
    def NewAttribute(self) -> None:
        ...
    def DeleteAttribute(self) -> None:
        ...
    def GetAttributeTitleName(self, titleName: str) -> None:
        ...
    def SetAttributeTitleName(self, titleName: str) -> None:
        ...
    def GetAttributeValueText(self, valueText: str) -> None:
        ...
    def SetAttributeValueText(self, valueText: str) -> None:
        ...
    def CreateUserDefinedInsert(self, refset: str) -> None:
        ...
    def CreateOffsetDatumPlane(self) -> None:
        ...
    BoxOffset: Expression
    Clearance: Expression
    GenerateType: Tooling.GeneralInsertBuilder.GenerateMethod
    Height: Expression
    InsertToDelete: Assemblies.SelectComponentList
    InsertToEdit: Assemblies.SelectComponent
    NegativeX: Expression
    NegativeY: Expression
    NegativeZ: Expression
    NormalRenameDialog: bool
    OrientationReferenceCSYS: Matrix3x3
    OuterProfile: Section
    ParentPart: Tooling.GeneralInsertBuilder.ParentOption
    ParentPartName: str
    PositiveX: Expression
    PositiveY: Expression
    PositiveZ: Expression
    Radius: Expression
    ReverseInsertDirection: bool
    SelectFace: SelectFaceList
    SettingWithoutFalseBody: bool
    StartPosition: Expression
    Type: Tooling.GeneralInsertBuilder.Types
    UserDefinedExtrudeDirection: Vector3d
    WizardType: int


    class Types(enum.Enum):
        CreateInsert = 0
        EditInsert = 1
        DeleteInsert = 2
    

    class ParentOption(enum.Enum):
        NoParent = 0
    

    class GenerateMethod(enum.Enum):
        BoundingBox = 0
        UserDefined = 1
    

class FreeformUnformBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreatePreviewFacets(self) -> None:
        ...
    AngleTolerance: float
    BaseCurve: Section
    BendCurve: Section
    BendFaces: ScCollector
    ControlCurve: Section
    DistanceTolerance: float
    FirstRegionLimitCurve: Section
    FirstRegionOffsetCurve: ScCollector
    FirstTargetCurve: ScCollector
    FirstTargetCurveOffset: Expression
    IterationCount: int
    KeepBaseLength: bool
    ModifyInputSheet: bool
    RadiusReductionPercent: Expression
    RegionToDeformOffset: Expression
    RotationAngle: Expression
    RotationAngleReverseDirection: bool
    RotationDistance: Expression
    RotationTargetCurve: Section
    SecondRegionLimitCurve: Section
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
    TargetCurveOffsetType: Features.GlobalShapingBuilder.OffsetMethod
    TargetPoint: Point
    TargetPointOffset: Expression
    TargetSheet: ScCollector
    TransitionOptions: Features.GlobalShapingBuilder.TransitionType
    TransitionShapeControl: float
    UnformType: Tooling.FreeformUnformBuilder.UnformTypes


    class UnformTypes(enum.Enum):
        ByCurve = 0
        OverBend = 1
    

    class RotationMethodType(enum.Enum):
        Angle = 0
        Distance = 1
    

    class RotationMethod(enum.Enum):
        Constant = 0
        LawControlled = 1
        CurveDefined = 2
    

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
    

class FormingSimulationResultDisplayBuilder(Builder):
    def __init__(self) -> None: ...
    def SetResultFileNames(self, resultFileNames: str) -> None:
        ...
    def ImportGeometries(self) -> None:
        ...
    def DisplayFormability(self) -> None:
        ...
    def DisplayStress(self) -> None:
        ...
    def DisplayStrain(self) -> None:
        ...
    def DisplayThickness(self) -> None:
        ...
    def DisplayThinning(self) -> None:
        ...
    def DisplaySpringback(self) -> None:
        ...
    FormabilityStrainType: Tooling.FormingSimulationResultDisplayBuilder.FormabilityStrainTypeName
    ResultFileFolder: str
    State: int
    StrainType: Tooling.FormingSimulationResultDisplayBuilder.StrainTypeName
    StressType: Tooling.FormingSimulationResultDisplayBuilder.StressTypeName


    class StressTypeName(enum.Enum):
        TopFirstPriStress = 0
        TopSecondPriStress = 1
        TopEquivalentStress = 2
        MidFirstPriStress = 3
        MidSecondPriStress = 4
        MidEquivalentStress = 5
        BottomFirstPriStress = 6
        BottomSecondPriStress = 7
        BottomEquivalentStress = 8
    

    class StrainTypeName(enum.Enum):
        TopFirstPriStrain = 0
        TopSecondPriStrain = 1
        TopEquivalentStrain = 2
        MidFirstPriStrain = 3
        MidSecondPriStrain = 4
        MidEquivalentStrain = 5
        BottomFirstPriStrain = 6
        BottomSecondPriStrain = 7
        BottomEquivalentStrain = 8
    

    class FormabilityStrainTypeName(enum.Enum):
        TopPrincipalStrain = 0
        MidPrincipalStrain = 1
        BottomPrincipalStrain = 2
    

class FormingInsertCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.FormingInsertBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFormingInsertBuilder(self) -> Tooling.FormingInsertBuilder:
        ...
    def Tag(self) -> Tag: ...



class FormingInsertBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateNewComponent(self, parentTag: TaggedObject, origin: Point3d) -> TaggedObject:
        ...
    def ReverseTrimDirection(self) -> None:
        ...
    def ExtractFormingRegion(self) -> None:
        ...
    def DeletePunchOrDieComponent(self) -> None:
        ...
    AngleToleranceValue: float
    BlankPosition: Tooling.FormingInsertBuilder.BlankPositions
    BlankProfile: Section
    BlankType: Tooling.FormingInsertBuilder.BlankTypes
    BottomPlateClearance: float
    BoundaryFaces: ScCollector
    DesignOption: Tooling.FormingInsertBuilder.DesignOptions
    DiePlateClearance: float
    HeightValue: Expression
    LowerValue: Expression
    ParentPart: Tooling.FormingInsertBuilder.ParentTypes
    ParentPartName: str
    PunchOrDieToEdit: SelectBody
    PunchPlateClearance: float
    RenameComponent: bool
    ReverseDirection: bool
    SameWithPlate: bool
    SeedFace: ScCollector
    SelectFormingFaces: ScCollector
    StripperPlateClearance: float
    TangentEdgeAngle: bool
    TraverseInteriorEdges: bool
    UseBottomPlateClearance: bool
    UseDiePlateClearance: bool
    UsePunchPlateClearance: bool
    UseStripperPlateClearance: bool


    class ParentTypes(enum.Enum):
        Control = 0
        DieBase = 1
        SubDie = 2
        Die = 3
    

    class DesignOptions(enum.Enum):
        FormingPunch = 0
        FormingDie = 1
    

    class BlankTypes(enum.Enum):
        Standard = 0
        UserDefined = 1
    

    class BlankPositions(enum.Enum):
        PunchPlate = 0
        StripperPlate = 1
        DiePlate = 2
    

class ForceCalculationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ForceCalculationBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateForceCalculationBuilder(self) -> Tooling.ForceCalculationBuilder:
        ...
    def Tag(self) -> Tag: ...



class ForceCalculationBuilder(Builder):
    def __init__(self) -> None: ...
    CalculationType: Tooling.ForceCalculationBuilder.CalculationTypes
    CuttingPerimeter: str
    DecimalPlaces: int
    ForceProcess: SelectFaceList
    GravityCenter: str
    HoldingForce: str
    Parameter: str
    ParameterText: str
    ProcessFace: ScCollector
    ProcessForce: str
    ProcessName: str
    ProcessType: Tooling.ForceCalculationBuilder.ProcessTypes
    TotalForce: str
    TotalForceCenter: str


    class ProcessTypes(enum.Enum):
        Catalog = 0
        AngularBlanking = 1
        AngularEmbossing = 2
        AngularPiercing = 3
        Bending = 4
        Blanking = 5
        Burring = 6
        CircularDrawing = 7
        Counterboring = 8
        Countersinking = 9
        CylindricalIroning = 10
        Flanging = 11
        Piercing = 12
        RoundEmbossing = 13
        SquareDrawing = 14
        UBending = 15
        VBending = 16
        VBendingTree = 17
        ZBending = 18
    

    class CalculationTypes(enum.Enum):
        Normal = 0
        Isolated = 1
    

class FlowDisplayBuilder(Builder):
    def __init__(self) -> None: ...
    def DisplayDynamicColorPlots(self) -> None:
        ...
    AirTrapOption: bool
    FolderBrowser: str
    NumberIntervals: int
    NumberSubMeshes: int
    ResultsOption: Tooling.FlowDisplayBuilder.AnalysisResults
    WeldLineOption: bool


    class AnalysisResults(enum.Enum):
        MeltFrontTime = 0
        GateContribution = 1
        PressureDrop = 2
        MeltFrontTemperature = 3
        MaxTemperature = 4
        AverageTemperature = 5
        FrozenLayerRatio = 6
        MaxCoolingTime = 7
    

class FlowAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    Description: str
    GatePoints: Section
    ProductBody: SelectBody


class FeatureReferenceSetBuilder(Builder):
    def __init__(self) -> None: ...
    def SetReferenceSet(self, referenceSet: str) -> None:
        ...
    SelectFeatures: Features.SelectFeatureList


class FastenerRemoveNodeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.FastenerRemoveNodeBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFastenerRemoveNodeBuilder(self) -> Tooling.FastenerRemoveNodeBuilder:
        ...
    def Tag(self) -> Tag: ...



class FastenerRemoveNodeBuilder(Builder):
    def __init__(self) -> None: ...
    def AddComponent(self, component: NXObject) -> None:
        ...
    def RemoveComponent(self, component: NXObject) -> None:
        ...


class FastenerAssyCustomizationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.FastenerAssyCustomizationBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.FastenerAssyCustomizationBuilder:
        ...
    def Tag(self) -> Tag: ...



class FastenerAssyCustomizationBuilder(Builder):
    def __init__(self) -> None: ...


class FastenerAssyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.FastenerAssy]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.FastenerAssy:
        ...
    def Tag(self) -> Tag: ...



class FastenerAssy(Builder):
    def __init__(self) -> None: ...
    def AddTopNode(self, point: Point3d, direction: Point3d, selObject: NXObject, index: int) -> NXObject:
        ...
    def SetHoleDiameter(self, diameter: float, index: int) -> None:
        ...
    def SetHoleDirection(self, direction: Point3d, index: int) -> None:
        ...
    def SetHoleSideCylindricalFaces(self, sideCylFace: NXObject, index: int) -> None:
        ...
    def SetCreatePocket(self, create: bool) -> None:
        ...
    def SetHoleFaces(self, holeFace: NXObject, index: int) -> None:
        ...
    def AddScrewArray(self, krxFile: str, lengthMatch: str, libPath: str, libName: str, fullPath: str, index: int, type: Tooling.FastenerAssy.StackTypeMethod) -> None:
        ...
    def AddParentNewPart(self, fileName: str, index: int, parentNode: bool) -> None:
        ...
    def SetItemName(self, partName: str, itemName: str) -> None:
        ...
    def SetHolePosition(self, position: Point3d, index: int) -> None:
        ...
    def SetHoleDefaultCylindricalFace(self, defaultCylFaces: NXObject, index: int) -> None:
        ...
    def SetHoleOriginPosition(self, originposition: Point3d, index: int) -> None:
        ...
    def SetHoleHeight(self, height: float, index: int) -> None:
        ...
    def SetHoleOriginHeight(self, originheight: float, index: int) -> None:
        ...
    def SetFastenerExtentLength(self, extentLength: float) -> None:
        ...
    def SetHoleOriginDiameter(self, originDiameter: float, index: int) -> None:
        ...
    def SetFastenerSelectionType(self, selectionType: Tooling.FastenerAssy.SelectionTypeMethod) -> None:
        ...
    def GetFastenerSelectionType(self) -> Tooling.FastenerAssy.SelectionTypeMethod:
        ...
    def SetHoleDatumCsys(self, datumCsys: NXObject, index: int) -> None:
        ...
    def UpdateFastenerLength(self, adjustLength: bool) -> None:
        ...
    def CreateSameAssemblyData(self, addedIndex: int, index: int) -> None:
        ...
    def EraseStackArray(self, parentIndex: int, inx: int, type: Tooling.FastenerAssy.StackTypeMethod) -> None:
        ...
    def EraseFastenerAssembly(self, parentInx: int, removeParent: bool, removeScrew: bool, removeStack: bool, removeArray: bool, removeBuilder: bool, initscrewBuilder: bool, initstackBuilder: bool, removeData: bool) -> None:
        ...
    def EraseFastenerSetupData(self) -> None:
        ...
    def CreateFastenerConstraints(self, index: int) -> None:
        ...
    def RemoveFastenerConstraints(self, index: int) -> None:
        ...
    def SetSidePlanarFaces(self, sidePlanarFace: NXObject, index: int) -> None:
        ...
    def SetDefaultPlanarFaces(self, defaultPlanarFace: NXObject, inx: int) -> None:
        ...
    def SetInstanceFeatureFaces(self, instanceFeature: NXObject, inx: int) -> None:
        ...
    def AdjustFastenerLength(self, parentIndex: int, childIndex: int, nodeType: Tooling.FastenerAssy.StackTypeMethod) -> None:
        ...
    def UpdateFastenerStacks(self, parentIndex: int, updateScrew: bool, updatePocket: bool) -> None:
        ...
    def UpdateHoleData(self, inx: int, originheight: float, originPoint: Point3d, threadhole: bool, blindhole: bool) -> None:
        ...
    def CreateReusablePocket(self, commit: bool) -> None:
        ...
    def DeleteReusablePocket(self) -> None:
        ...
    def SelectScrewSize(self, inx: int, diameter: float, origindiameter: float, selDiameter: bool) -> None:
        ...
    def CreateReusableBuilder(self, parentIndex: int, childIndex: int, nodeType: Tooling.FastenerAssy.StackTypeMethod) -> Tooling.AddReusablePart:
        ...
    def SubstituteFastenerStack(self, parentIndex: int, childIndex: int, nodeType: Tooling.FastenerAssy.StackTypeMethod, partFile: str, krxFile: str, libName: str, pathInLib: str, lengthMatch: str, fullPath: str) -> None:
        ...
    def SaveUdoData(self) -> None:
        ...
    def SetFastenerMode(self, modeMethod: Tooling.FastenerAssy.ModeMethod) -> None:
        ...
    def GetFastenerMode(self) -> Tooling.FastenerAssy.ModeMethod:
        ...
    def EraseAssemblyData(self, parentIndex: int) -> None:
        ...
    def UpdateHolePostion(self, parentIndex: int, dirOne: Point3d, tempPnt: Point3d, pointOne: Point3d, height: float, orignHeight: float, offSetDistance: float) -> None:
        ...
    def SetReuseBuilder(self, index: int, nodeType: Tooling.FastenerAssy.StackTypeMethod, childIndex: int, partOcc: Assemblies.Component) -> None:
        ...
    def RenameParentNode(self, index: int, newname: str) -> None:
        ...
    def CreateArrayHole(self, index: int) -> None:
        ...
    def DeleteArrayHole(self, index: int) -> None:
        ...
    def InitPocketBuilder(self) -> None:
        ...
    def UpdateTopBottomStacks(self, index: int, type: Tooling.FastenerAssy.SelectionObjectMethod, isSameFace: bool, face: NXObject) -> None:
        ...
    def ReadAssemblyConfigure(self, holeNum: int, partOcc: Assemblies.Component) -> None:
        ...
    def SetAssemblyExtentLength(self, index: int, extentLength: float) -> None:
        ...
    def UpdateDefaultStandard(self, index: int, standard: str, form: str, type: str) -> None:
        ...
    def RemoveSelectedHole(self) -> None:
        ...
    def AddRemovalHoleIndex(self, index: int) -> None:
        ...
    def UpdateStackPosition(self, parentIndex: int, childIndex: int, nodeType: Tooling.FastenerAssy.StackTypeMethod, deltaLength: float) -> None:
        ...
    def SetReusablePocketBuilder(self, pocketTag: Tooling.ReusablePocketBuilder) -> None:
        ...
    def GetReusablePocketBuilder(self) -> Tooling.ReusablePocketBuilder:
        ...
    def EraseFastenerAssemblyData(self, index: int) -> None:
        ...
    def SetBlindHole(self, inx: int, blindhole: bool) -> None:
        ...
    def CreatePatternComponent(self, createPattern: bool) -> None:
        ...
    def FindPositioningFeatureSet(self) -> Features.Feature:
        ...
    def SaveDropPointPosition(self, tempPnt: Point3d) -> None:
        ...
    def CreatePositioningFeatureOnPoint(self, selobj: NXObject, inputPosition: Point3d, centerFace: bool) -> None:
        ...
    def OffsetPositioningFeature(self, offsetValue: float) -> None:
        ...
    def SetOffsetExpression(self, offsetDistance: float) -> None:
        ...
    def GetReusableBuilderWorkPart(self) -> NXObject:
        ...
    def CreatePositioningFeatureByPoint(self, selobj: NXObject, inputPosition: Point3d, centerFace: bool) -> None:
        ...
    ComponentPatternBuilder: Assemblies.ComponentPatternBuilder
    PositioningFeature: Sketch


    class StackTypeMethod(enum.Enum):
        Screw = 0
        TopStack = 1
        BottomStack = 2
        RootNode = 3
        TopNode = 4
        BottomNode = 5
    

    class SelectionTypeMethod(enum.Enum):
        Hole = 0
        Position = 1
    

    class SelectionObjectMethod(enum.Enum):
        Top = 0
        Bottom = 1
    

    class ModeMethod(enum.Enum):
        Add = 1
        Edit = 2
    

    class HoleOperation(enum.Enum):
        Add = 0
        Remove = 1
    

class FastenerAssemConfigCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.FastenerAssemConfigBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.FastenerAssemConfigBuilder:
        ...
    def Tag(self) -> Tag: ...



class FastenerAssemConfigBuilder(Builder):
    def __init__(self) -> None: ...


class FamilyMoldCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.FamilyMoldBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFamilyMoldBuilder(self) -> Tooling.FamilyMoldBuilder:
        ...
    def Tag(self) -> Tag: ...



class FamilyMoldBuilder(Builder):
    def __init__(self) -> None: ...
    def AddItemToDeletedList(self, detetedItem: str) -> None:
        ...
    ItemIndex: int
    ListItem: str


class FaceSplitCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.FaceSplitBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFaceSplitBuilder(self) -> Tooling.FaceSplitBuilder:
        ...
    def Tag(self) -> Tag: ...



class FaceSplitBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateIsoclines(self, pFacesToDivide: typing.List[Face], outputCurves: typing.List[Curve]) -> None:
        ...
    def FindMoldUnsplitFace(self) -> None:
        ...
    def AddOrRemoveNewDividingObjects(self, createdFeture: Features.Feature, isAdding: bool) -> None:
        ...
    DivObjects: ScCollector
    DivideFaceBuilder: Features.DividefaceBuilder
    FaceToDivide: ScCollector
    Tolerance: float
    Type: Tooling.FaceSplitBuilder.FaceSplitType


    class FaceSplitType(enum.Enum):
        CurvesEdges = 0
        Plane = 1
        Intersection = 2
        Isocline = 3
    

class FaceColorManagementCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.FaceColorManagementBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFaceColorManagementBuilder(self) -> Tooling.FaceColorManagementBuilder:
        ...
    def Tag(self) -> Tag: ...



class FaceColorManagementBuilder(Builder):
    def __init__(self) -> None: ...
    def ShowFacesWithoutColorAttrirbute(self) -> None:
        ...
    def ShowFaceWithoutAnyManufacturingInformationButton(self) -> None:
        ...
    def ShowFaceWithSameManufacturingInformationButton(self) -> None:
        ...
    def EditColorSpreadsheet(self) -> None:
        ...
    def AssignAttributeToObject(self, objectTag: NXObject, attrTitle: str, attrValue: str) -> None:
        ...
    def AssignColorToObject(self, objectTag: NXObject, colorID: int) -> None:
        ...
    def RemoveAttributeOfObject(self, objectTag: NXObject, attrTitle: str) -> None:
        ...
    AngleNoseIgnorableSize: float
    FaceColor: NXColor
    FaceTranslucency: int
    HighlightSelectedFace: bool
    HoleTypeEnum: Tooling.FaceColorManagementBuilder.HoleTypeEnumValue
    IsAutoSelectHoleByType: bool
    IsShowFaceWithSameColorAttributeToggle: bool
    IsShowFaceWithoutColorAttributeToggle: bool
    OnlyCheckHoleFace: bool
    SelectColorSpreadsheet: str
    SelectCurve: ScCollector
    SelectFace: ScCollector
    SelectHoleAxis: Direction
    SelectSubHoleFaceAutomatically: bool
    WizardType: int


    class HoleTypeEnumValue(enum.Enum):
        ThroughHoles = 0
        BlindHoles = 1
        CounterboredHoles = 2
        CountersunkHoles = 3
        ThreadedHoles = 4
        ComboHoles = 5
        WireEDMStartHoles = 6
        CirclesinSketch = 7
    

class FaceAttributeBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteItem(self) -> None:
        ...


class EWMultiPositionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.EWMultiPositionBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateEwmultiPositionBuilder(self) -> Tooling.EWMultiPositionBuilder:
        ...
    def Tag(self) -> Tag: ...



class EWMultiPositionBuilder(Builder):
    def __init__(self) -> None: ...
    Head: SelectBodyList
    HeadSet: BodyList


class EWDraftingBuilder(Builder):
    def __init__(self) -> None: ...
    def SetEdmTemplateName(self, edmTemplateName: str) -> None:
        ...
    def SetCncTemplateName(self, cncTemplateName: str) -> None:
        ...
    def GetCloneObject(self, sheetType: Tooling.EWDraftingBuilder.NameOption) -> Tooling.CloneObject:
        ...
    def SetMasterModelPartName(self, masterPartName: str) -> None:
        ...
    def SetDeleteDrawingParts(self, partNames: str) -> None:
        ...
    BlankComps: Assemblies.SelectComponentList
    CncOption: bool
    CncSensitivity: bool
    CncTemplate: Tooling.EWDraftingBuilder.CNCTemplateOption
    DraftingMode: Tooling.EWDraftingBuilder.ModeOption
    DrawingType: Tooling.EWDraftingBuilder.DrawingOption
    EdmOption: bool
    EdmSensitivity: bool
    EdmTemplate: Tooling.EWDraftingBuilder.EDMTemplateOption
    HideCsys: bool
    IncludeFixture: bool
    IncludeOption: bool
    MasterModelCncPartName: str
    MasterModelEdmPartName: str
    NameRule: str
    OrdinateDimension: bool
    OutputPDF: bool
    OutputSameSheet: bool
    RenameComponent: bool
    SheetName: Tooling.EWDraftingBuilder.NameOption
    UseInstance: bool


    class NameOption(enum.Enum):
        Sh1 = 0
        Sh2 = 1
    

    class ModeOption(enum.Enum):
        Create = 0
        Add = 1
        Edit = 2
    

    class EDMTemplateOption(enum.Enum):
        EdmTemplate1 = 0
        EdmTemplate2 = 1
    

    class DrawingOption(enum.Enum):
        MasterModel = 0
        SelfContained = 1
    

    class CNCTemplateOption(enum.Enum):
        CncTemplate1 = 0
        CncTemplate2 = 1
    

class EnlargeSurfaceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.EnlargeSurfaceBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateEnlargeSurfaceBuilder(self) -> Tooling.EnlargeSurfaceBuilder:
        ...
    def Tag(self) -> Tag: ...



class EnlargeSurfaceBuilder(Builder):
    def __init__(self) -> None: ...
    def GetColorValue(self, redValue: float, greenValue: float, blueValue: float) -> None:
        ...
    def SetColorValue(self, redValue: float, greenValue: float, blueValue: float) -> None:
        ...
    def SetTargetFace(self, targetFace: Face) -> None:
        ...
    def SetRangeValue(self, rangeFace: Face, rangeValue: float) -> None:
        ...
    def AddSurfaceData(self, addFace: Face) -> None:
        ...
    def EraseSurfaceData(self, eraseFace: Face) -> None:
        ...
    def AddPlanarFaceData(self, planarFace: Face) -> None:
        ...
    def ErasePlanarFaceData(self, planarFace: Face) -> None:
        ...
    def CreatePreviewSurface(self) -> None:
        ...
    AsPatchSurface: bool
    BodyColor: NXColor
    BoundarySelection: SelectNXObjectList
    ChangeAllSizes: bool
    ConvertType: Tooling.EnlargeSurfaceBuilder.ConvertTypeOption
    CutToBoundary: bool
    DragData: bool
    RegionOption: Tooling.EnlargeSurfaceBuilder.KeepDiscardOption
    RegionSelection: RegionPointList
    ReselTargetData: bool
    SurfaceRange: GeometricUtilities.SurfaceRangeBuilder
    TargetSelection: ScCollector


    class KeepDiscardOption(enum.Enum):
        Keep = 0
        Discard = 1
    

    class ConvertTypeOption(enum.Enum):
        WithCopies = 0
        NoCopies = 1
    

class EmbossingAreaData(Tooling.CostDataObject):
    def __init__(self) -> None: ...


class ElectrodeInitializationBuilder(Builder):
    def __init__(self) -> None: ...
    def SetConfigurationData(self, configName: str, topPartName: str, msetPartName: str, workingPartName: str, subdir: str, cloneMethod: int) -> None:
        ...
    def SetMsetCsysMatrixOrigin(self, matrix: Matrix3x3, origin: Point3d) -> None:
        ...
    def SetMsetCsysOriginToFaceCenter(self) -> None:
        ...
    def CreateCloneObjectOfTopPart(self) -> Tooling.CloneObject:
        ...
    def CreateCloneObjectOfMsetPart(self) -> Tooling.CloneObject:
        ...
    def CreateCloneObjectOfWorkingPart(self) -> Tooling.CloneObject:
        ...
    def CreateProject(self, cloneObject: Tooling.CloneObject) -> None:
        ...
    def CreateMsetPart(self, cloneObject: Tooling.CloneObject) -> TaggedObject:
        ...
    def CreateWorkingPart(self, cloneObject: Tooling.CloneObject, msetPartTag: TaggedObject) -> TaggedObject:
        ...
    def DisposeCloneObject(self, cloneObject: Tooling.CloneObject) -> None:
        ...
    def InitLinkObjects(self, workingPartTag: TaggedObject) -> None:
        ...
    def GetWorkingPart(self, msetPartTag: TaggedObject) -> TaggedObject:
        ...
    def InitalizeProjectParameter(self, rootPartTag: NXObject) -> None:
        ...
    def BuildMemberPartName(self, type: Tooling.ElectrodeInitializationBuilder.Type) -> str:
        ...
    def SetCloneMethod(self, cloneMethod: int) -> None:
        ...
    def GetMsetPart(self, listIndex: int) -> TaggedObject:
        ...
    def RemoveSelectedMsetNode(self, msetPartTag: TaggedObject) -> None:
        ...
    def AnalyseInitProjectRegisterData(self, number: int) -> int:
        ...
    ActionType: Tooling.ElectrodeInitializationBuilder.Method
    CurrentMset: TaggedObject
    Face: SelectFace
    FaceList: SelectFaceList
    InputName: str
    PathBrowser: str
    Rename: bool
    Workpiece: SelectBody
    WorkpieceList: SelectBodyList


    class Type(enum.Enum):
        CloneTopPart = 0
        CloneMsetPart = 1
        CloneWorkingPart = 2
    

    class Method(enum.Enum):
        Original = 0
        NoWorkingPart = 1
        NoMsetPart = 2
        NoTemplate = 3
        OnlyTopPart = 4
        Number = 5
    

class ElectrodeEDMOutputBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateEwBlankAttributes(self) -> None:
        ...
    def GetAttributeTemplateName(self) -> str:
        ...
    def GetAttributeTemplateTitleNames(self, titleName: str) -> None:
        ...
    def SetAttributeTemplateName(self, attributeTemplateName: str) -> None:
        ...
    def CreateAttributeOutputFileName(self, blank: TaggedObject) -> None:
        ...
    def GetTemplateFileType(self) -> Tooling.ElectrodeEDMOutputBuilder.FileType:
        ...
    def SetTemplateFileType(self, attributeTemplateName: str) -> None:
        ...
    def PopulateAttributeTemplate(self, attributeTemplateFolder: str) -> None:
        ...
    def AnalyseAttributeTemplateData(self) -> None:
        ...
    AttributeTemplate: Tooling.ElectrodeEDMOutputBuilder.NameOption
    Blank: Assemblies.SelectComponentList
    InputName: str
    MultipleFile: bool
    NameRule: str
    OutputFileFolderNames: str
    ReplaceOption: bool
    TemplateFolderNames: str


    class NameOption(enum.Enum):
        Template1 = 0
        Template2 = 1
    

    class FileType(enum.Enum):
        Txt = 0
        Xml = 1
    

class ElectrodeDesignCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ElectrodeDesign]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateProjectBuilder(self) -> Tooling.ElectrodeInitializationBuilder:
        ...
    def CreateComponentBuilder(self) -> Tooling.ElectrodeComponentBuilder:
        ...
    def CreateBlankBuilder(self) -> Tooling.ElectrodeBlankBuilder:
        ...
    def CreateDeleteComponentBuilder(self) -> Tooling.ElectrodeDeleteBuilder:
        ...
    def CreateCheckingBuilder(self) -> Tooling.ElectrodeCheckingBuilder:
        ...
    def CreateEwdraftingBuilder(self) -> Tooling.EWDraftingBuilder:
        ...
    def CreateEDMOutputBuilder(self) -> Tooling.ElectrodeEDMOutputBuilder:
        ...
    def Tag(self) -> Tag: ...



class ElectrodeDesign(Builder):
    def __init__(self) -> None: ...


class ElectrodeDeleteBuilder(Builder):
    def __init__(self) -> None: ...
    Component: Assemblies.SelectComponentList
    Head: Features.SelectFeatureList
    KeepSize: bool
    RoundPosition: bool
    Type: Tooling.ElectrodeDeleteBuilder.Types


    class Types(enum.Enum):
        SparkingBody = 0
        Component = 1
    

class ElectrodeCopyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ElectrodeCopyBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateElectrodeCopyBuilder(self) -> Tooling.ElectrodeCopyBuilder:
        ...
    def Tag(self) -> Tag: ...



class ElectrodeCopyBuilder(Builder):
    def __init__(self) -> None: ...
    def SetBlankPartName(self, blankPartName: str) -> None:
        ...
    def CopyElectrode(self, copyType: Tooling.ElectrodeCopyBuilder.Copy, eleBody: NXObject, fromface: NXObject, toface: NXObject) -> NXObject:
        ...
    def UpdateParameterData(self, blankBuilderTag: TaggedObject, partTag: TaggedObject, paraNames: str) -> str:
        ...
    def SetInstallationMethod(self, installationMethod: Tooling.ElectrodeCopyBuilder.CloneMethod) -> None:
        ...
    Angle: Expression
    AngularAxis: Axis
    BooleanTool: GeometricUtilities.BooleanToolBuilder
    CloneObject: Tooling.CloneObject
    CopyInstance: bool
    DefNum: int
    ElectrodeBlankBuilder: TaggedObject
    ManipulatorMatrix: Matrix3x3
    ManipulatorOrigin: Point3d
    MirrorPlane: SelectDatumPlaneList
    Rename: bool
    SelToFace: SelectFaceList
    SelType: Tooling.ElectrodeCopyBuilder.Copy
    SelectElectrode: SelectBodyList
    SelectFromCsys: CoordinateSystem
    SelectFromFace: SelectFaceList
    SelectToCsys: CoordinateSystem
    TransformMotionType: Tooling.ElectrodeCopyBuilder.TransformMotionTypes


    class TransformMotionTypes(enum.Enum):
        FaceToFace = 0
        CSYSToCSYS = 1
        Rotation = 2
        Dynamic = 3
    

    class Copy(enum.Enum):
        Transform = 0
        Mirror = 1
    

    class CloneMethod(enum.Enum):
        UseLogFile = 0
        InternalClone = 1
        PartRename = 2
        SaveAs = 3
    

class ElectrodeComponentBuilder(Builder):
    def __init__(self) -> None: ...
    def SetTemplatePartName(self, templatePartName: str) -> None:
        ...
    def SetTemplateDataName(self, templateDataName: str) -> None:
        ...
    def InstallComponentPart(self, templateData: Tooling.SpreadsheetData, libraryName: str, catalogName: str, classificationName: str, titleName: str) -> NXObject:
        ...
    ChuckType: Tooling.ElectrodeComponentBuilder.Chuck
    ComponentMatrix: Matrix3x3
    Face: SelectFace
    Fixture: Assemblies.SelectComponent
    MateCsys: NXObject
    Parent: Assemblies.SelectComponent
    ReferPart: bool
    ReferenceCenter: Point3d
    Rename: bool
    StandardData: str
    StandardPart: str


    class Chuck(enum.Enum):
        Unknown = -1
        Holder = 0
        Pallet = 1
    

class ElectrodeCheckingBuilder(Builder):
    def __init__(self) -> None: ...
    Electrode: Assemblies.SelectComponentList
    ElectrodeNameFilter: str
    InterSolid: bool
    MapFaceColor: bool
    SameParent: bool
    SaveResultsInPart: bool
    TouchArea: bool
    TouchAreaTolerance: Expression
    TouchBody: bool
    Workpiece: Assemblies.SelectComponentList
    WorkpieceNameFilter: str


class ElectrodeBlankBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateBlankData(self, registerPath: str, dataPath: str, modelPath: str, bitmapPath: str, material: str, paraNames: str, paraValues: str) -> None:
        ...
    def CreateCloneObject(self, applicationType: int, installationMethod: int, partToBeInstalled: str, folderToSaveParts: str, projectName: str) -> Tooling.CloneObject:
        ...
    def UpdateDisplayName(self, displayName: str) -> None:
        ...
    Angle: Expression
    Blank: Assemblies.SelectComponent
    BlankMatrix: Matrix3x3
    BlendRadius: Expression
    CrossLinesRatio: float
    ExtensionHeight: Expression
    HeadBodies: SelectBodyList
    JointFace: SelectFace
    JointMethod: Tooling.ElectrodeBlankBuilder.JointObject
    KeepSize: bool
    KeepZValueInSameMSet: bool
    Material: Tooling.ElectrodeBlankBuilder.BlankMaterial
    MsetPart: TaggedObject
    MultiPositionBuilder: TaggedObject
    ReferenceCenter: Point3d
    ReferencePointPrecision: float
    Rename: bool
    ReusablePartBuilder: TaggedObject
    RotationAngle: Expression
    RoundCrossLinesPosition: bool
    Shape: Tooling.ElectrodeBlankBuilder.BlankShape
    UniteBodies: bool
    XRefValue: Expression
    YRefValue: Expression
    ZRefValue: Expression


    class JointObject(enum.Enum):
        Extrude = 0
        Offset = 1
        None = 2
    

    class BlankShape(enum.Enum):
        Block = 0
        Cylinder = 1
        Undercut = 2
    

    class BlankMaterial(enum.Enum):
        Copper = 0
        Graphite = 1
    

class EjectorTableData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def CollectEjectors(self, parent: NXObject) -> None:
        ...


class EjectorTableBuilder(Builder):
    def __init__(self) -> None: ...
    def AssignEjectorType(self) -> None:
        ...
    def RemoveEjectorType(self) -> None:
        ...
    def NewEjectorTableData(self) -> Tooling.EjectorTableData:
        ...
    def GetEjectorTableData(self) -> Tooling.EjectorTableData:
        ...
    DestinationFolder: str
    EjectorDrawingType: Tooling.EjectorTableBuilder.DrawingType
    EjectorPinType: Tooling.EjectorTableBuilder.EjectorType
    EjectorPins: Assemblies.SelectComponentList
    MasterModelPartName: str
    NameRule: str
    RenameComponent: bool
    TemplateName: str
    WorkingPart: NXObject


    class EjectorType(enum.Enum):
        All = 0
        Straight = 1
        Shoulder = 2
        Blade = 3
        Sleeve = 4
        Other = 5
    

    class DrawingType(enum.Enum):
        MasterModel = 0
        SelfContained = 1
    

class EjectorRecords(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetCurrentRecordIndex(self) -> int:
        ...
    def SetCurrentRecordIndex(self, index: int) -> None:
        ...
    def AddSingleDesignRecord(self, designRecord: Tooling.EjectorDesignData) -> None:
        ...
    def InsertDesignRecord(self, designRecord: Tooling.EjectorDesignData, index: int) -> None:
        ...
    def GetSingleDesignRecord(self, index: int) -> Tooling.EjectorDesignData:
        ...
    def AddSingleEditRecord(self, editRecord: Tooling.EjectorDesignData) -> None:
        ...
    def InsertEditRecord(self, editRecord: Tooling.EjectorDesignData, index: int) -> None:
        ...
    def GetSingleEditRecord(self, index: int) -> Tooling.EjectorDesignData:
        ...
    def GetCurrentDesignRecord(self) -> Tooling.EjectorDesignData:
        ...
    def ClearDesignRecords(self) -> None:
        ...
    def ClearEditRecords(self) -> None:
        ...
    def EraseDesignRecord(self, index: int) -> None:
        ...


class EjectorPostProcessingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.EjectorPostProcessingBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateEjectorPostProcessingBuilder(self) -> Tooling.EjectorPostProcessingBuilder:
        ...
    def Tag(self) -> Tag: ...



class EjectorPostProcessingBuilder(Builder):
    def __init__(self) -> None: ...
    def SetTrimDataDetails(self, surfaceType: int, targets: typing.List[NXObject], tools: typing.List[NXObject]) -> None:
        ...
    ActionType: Tooling.EjectorPostProcessingBuilder.TrimMethod
    FitDistance: Expression
    ForceFitDistance: bool
    OffsetValue: Expression
    PrecisionValue: float
    TargetComponents: SelectNXObjectList
    ToolFace: ScCollector
    ToolSheetBody: SelectBody
    TrimPart: Tooling.EjectorPostProcessingBuilder.TrimPartName
    TrimSurface: Tooling.EjectorPostProcessingBuilder.TrimSufaceName


    class TrimSufaceName(enum.Enum):
        Face = 0
        SheetBody = 1
    

    class TrimPartName(enum.Enum):
        Notrimpart = 0
    

    class TrimMethod(enum.Enum):
        AdjustLength = 0
        SheetTrim = 1
        Untrim = 2
    

class EjectorDesignData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetSymbolTemplateFile(self, symbolFile: str) -> None:
        ...


class EditCoolingCurveBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdatePointSelectedCurve(self, pointNumber: int, selectedCurveTag: TaggedObject) -> None:
        ...
    def UpdateOutputCurve(self, pointNumber: int) -> None:
        ...
    def UpdateTrimLength(self, pointNumber: int, trimLength: float, trimPoint: Point3d) -> None:
        ...
    def UpdateOutputCurveAfterMoveHandle(self) -> None:
        ...
    def UpdateStartDistanceExpStr(self, startDistance: str) -> None:
        ...
    def UpdateEndDistanceExpStr(self, endDistance: str) -> None:
        ...
    Associative: bool
    CurveSmoothRates: int
    EndDistance: Expression
    ExtendMethod: Tooling.EditCoolingCurveBuilder.ExtensionMethod
    FirstPoint: Point
    ManipulatorOldOrigin: Point3d
    ManipulatorOldOriginAvailable: bool
    ManipulatorOrigin: Point3d
    OriginalCurveLayer: int
    OriginalCurveOperation: Tooling.EditCoolingCurveBuilder.OriginalCurveOperationType
    ReverseFirstPointTrimSide: bool
    ReverseSecondPointTrimSide: bool
    SecondPoint: Point
    StartDistance: Expression
    TangentShapeControlScaleValue: float
    Type: Tooling.EditCoolingCurveBuilder.Types


    class Types(enum.Enum):
        Trim = 0
        Extend = 1
        Divide = 2
        Bridge = 3
        Move = 4
        Drag = 5
    

    class OriginalCurveOperationType(enum.Enum):
        None = 0
        Hide = 1
        MovetoLayer = 2
        Delete = 3
    

    class ExtensionMethod(enum.Enum):
        Natural = 0
        Linear = 1
        Circular = 2
    

class EdgePatchCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.EdgePatchBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.EdgePatchBuilder:
        ...
    def Tag(self) -> Tag: ...



class EdgePatchBuilder(Builder):
    def __init__(self) -> None: ...
    def DirectionReverse(self) -> None:
        ...
    def GetBodyColor(self, redValue: float, greenValue: float, blueValue: float) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use Tooling.EdgePatchBuilder.BodyColor instead.")"""
        ...
    def SetBodyColor(self, redValue: float, greenValue: float, blueValue: float) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use Tooling.EdgePatchBuilder.BodyColor instead.")"""
        ...
    def FindFaceHoles(self, referFaces: Face) -> Tooling.EdgePatchBuilder.PatchStatus:
        ...
    def FindBodyHoles(self, body: Body) -> None:
        ...
    def FindEdgesPatch(self, edges: typing.List[NXObject]) -> Tooling.EdgePatchBuilder.PatchStatus:
        ...
    def EditReferenceFace(self, index: int, addFaces: typing.List[Face], removeFaces: typing.List[Face]) -> None:
        ...
    def DeleteOneLoopList(self, index: int) -> None:
        ...
    def SetSelectedItems(self, selectedItems: int) -> None:
        ...
    def SetTolerance(self, tolerance: float) -> None:
        ...
    def SetGiveFailedMessage(self, giveMessage: int) -> None:
        ...
    def DestroyMemory(self) -> None:
        ...
    def ClearList(self, type: int) -> None:
        ...
    def SetDeletedList(self, items: int) -> None:
        ...
    def MakeMoldWizardFills(self, tolerance: float, edges: typing.List[NXObject], origFaces: typing.List[Face]) -> None:
        ...
    AllowPatch: bool
    Body: SelectBody
    BodyColor: NXColor
    ConvertType: Tooling.EdgePatchBuilder.ConvertTypeOption
    Face: ScCollector
    Loops: ScCollector
    PatchSurface: bool
    ReferenceFace: ScCollector
    SelType: Tooling.EdgePatchBuilder.SelectTypes


    class SelectTypes(enum.Enum):
        Face = 0
        Body = 1
        Traverse = 2
    

    class PatchStatus(enum.Enum):
        NoLoopExisted = 0
        OneLoopExisted = 1
        MultiLoopsExisted = 2
        SomeLoopsExisted = 3
        LoopNotPatched = 4
        PatchedAndSomeSuppressed = 5
        PatchedAndAllSuppressed = 6
        PatchedAndNoSuppressed = 7
    

    class ConvertTypeOption(enum.Enum):
        WithCopies = 0
        NoCopies = 1
    

class DrawingSheetNameBuilder(Builder):
    def __init__(self) -> None: ...
    DrawingSheetName: str


class DrawingAreaData(Tooling.CostDataObject):
    def __init__(self) -> None: ...


class DirectUnfoldCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.DirectUnfoldBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDirectUnfoldBuilder(self) -> Tooling.DirectUnfoldBuilder:
        ...
    def CreateDirectUnbendBuilder(self) -> Tooling.DirectUnbendBuilder:
        ...
    def Tag(self) -> Tag: ...



class DirectUnfoldBuilder(Builder):
    def __init__(self) -> None: ...
    def LoadDatabase(self) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  This functionality is no longer supported.")"""
        ...
    def KByMaterial(self) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  This functionality is no longer supported.")"""
        ...
    def ConvertToSheetMetal(self, baseBody: NXObject) -> None:
        ...
    def MergeBends(self, mergeBendsFaces: typing.List[NXObject]) -> None:
        ...
    def DefinePreBends(self, selBends: typing.List[NXObject]) -> None:
        ...
    def DeleteBends(self, bendFaces: typing.List[NXObject]) -> None:
        ...
    def CreateResizeNeutralFactorForBody(self, baseBody: NXObject) -> None:
        ...
    def EditResizeNeutralFactorForBends(self, newKFactor: float, bendUDO: typing.List[NXObject]) -> None:
        ...
    def GetAllBendsUDO(self, baseBody: NXObject) -> typing.List[NXObject]:
        ...
    def SetCurrentBody(self, currentBody: NXObject) -> None:
        ...
    AdditionalBendFaces: ScCollector
    Angle1: float
    Angle2: float
    Angle3: float
    Angle4: float
    Angle5: float
    Angle6: float
    CurBodies: Tooling.DirectUnfoldBuilder.BodyList
    DefineNeutralFactor: Tooling.DefineNeutralFactorBuilder
    DesignSequence: int
    DevLength: float
    EditOption: int
    InterNamingRule: str
    InterRenameComp: bool
    InterStage: Assemblies.SelectComponent
    KFactor: str
    Materials: Tooling.DirectUnfoldBuilder.MatType
    NumBends: Tooling.DirectUnfoldBuilder.Bend
    NumInter: int
    OrientPitch: int
    Pitch: float
    SelPlanarFaces: SelectFaceList
    SelectBend: SelectFaceList
    SelectStartEdge: SelectEdgeList
    StartStation: int
    UnfoldType: Tooling.DirectUnfoldBuilder.Types


    class Types(enum.Enum):
        Convert = 0
        MergeBends = 1
        DefinePreBends = 2
        DeleteBends = 3
    

    class MatType(enum.Enum):
        Steel = 0
    

    class BodyList(enum.Enum):
        None = 0
    

    class Bend(enum.Enum):
        Two = 0
        Three = 1
        Four = 2
        Five = 3
        Six = 4
    

class DirectUnbendBuilder(Builder):
    def __init__(self) -> None: ...
    AlterResult: bool
    BaseBody: Body
    BendAngle1: float
    BendAngle2: float
    BendAngle3: float
    BendAngle4: float
    BendAngle5: float
    BendAngle6: float
    BendDevLength: float
    BendNeutralFactor: float
    BendNumPrebends: Tooling.DirectUnfoldBuilder.Bend
    KeepRadFixed: bool
    OverbendAngle: float
    RefObject: SelectEdgeList
    ResizeRadius: bool
    SelBend: SelectFaceList
    Type: Tooling.DirectUnbendBuilder.Bendtypes
    WorkPart: Assemblies.SelectComponent


    class Bendtypes(enum.Enum):
        Unbend = 0
        Rebend = 1
        Prebend = 2
        Overbend = 3
    

class DieInsertBuilder(Builder):
    def __init__(self) -> None: ...
    def StandardDieInsert(self) -> None:
        ...
    def CreateUserDefinedInsertDatumPlane(self) -> None:
        ...
    def AddDieInsertPart(self) -> None:
        ...
    def CreateUserDefinedDieInsert(self) -> None:
        ...
    def SetManipulatorToMatrixAndPosition(self, matrix: Matrix3x3, position: Point3d) -> None:
        ...
    def CalculateBoxSize(self) -> None:
        ...
    BoundingBoxType: Tooling.DieInsertBuilder.BoundingBoxTypeItems
    BoxPosition: Point3d
    ClearanceToggle: bool
    ConceptDesign: bool
    DieInsertType: Tooling.DieInsertBuilder.DieInsertTypeItems
    DieShimDistance: float
    DieStandardInsertInstance: TaggedObject
    InsertMode: Tooling.DieInsertBuilder.InsertModeItems
    NewPartNames: str
    OffsetValueLinearDimensionNegativeX: Expression
    OffsetValueLinearDimensionNegativeY: Expression
    OffsetValueLinearDimensionNegativeZ: Expression
    OffsetValueLinearDimensionPositiveX: Expression
    OffsetValueLinearDimensionPositiveY: Expression
    OffsetValueLinearDimensionPositiveZ: Expression
    ParentPartName: str
    Position: Tooling.DieInsertBuilder.PositionItems
    RadialOffset: Expression
    RenameDialog: bool
    SelectDieInsertOutline: Section
    SelectScrap: SelectBodyList
    SelectUserDefinedDieInsertForEdit: SelectBodyList
    SelectVector: Direction
    UserDefinedDieInsertClearance: float
    UserDefinedDieInsertHeight: Expression
    WithoutFalseBody: bool


    class PositionItems(enum.Enum):
        Top = 0
        Bottom = 1
    

    class InsertModeItems(enum.Enum):
        StandardInsert = 0
        SketchProfile = 1
        BoundingBox = 2
    

    class DieInsertTypeItems(enum.Enum):
        DieInsert = 0
        BackingInsert = 1
    

    class BoundingBoxTypeItems(enum.Enum):
        Block = 0
        Cylinder = 1
    

class DieEngTrimTaskBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SwitchTrimSide(self) -> None:
        ...
    def SetMatchCutNotchOffset(self, notchOffset: float) -> None:
        ...
    def SetMatchCutFirstRadius(self, firstRadius: float) -> None:
        ...
    def SetMatchCutSecondRadius(self, secondRadius: float) -> None:
        ...
    def SetMatchCutThirdRadius(self, thirdRadius: float) -> None:
        ...
    def SetMatchCutOffsetLength(self, offsetLength: float) -> None:
        ...
    def SetMatchCutAngle(self, angle: float) -> None:
        ...
    def SetMatchCutScrapCutterLength(self, scrapCutterLength: float) -> None:
        ...
    def SetMatchCutOffsetFromPlane(self, offsetFromPlane: float) -> None:
        ...
    def SetUsePlaneOffset(self, useOffset: bool) -> None:
        ...
    CamType: Tooling.DieEngTrimTaskBuilder.TrimTaskCamType
    CreateScrap: bool
    EndPlaneSelected: bool
    FinishOperation: bool
    LayoutFlange: bool
    MatchCut: Tooling.DieEngTrimTaskBuilder.TrimTaskMatchCutType
    SelectCamDirection: Direction
    SelectDieTip: Features.SelectFeature
    SelectEndPlane: Plane
    SelectScrapCutters: SelectIBasePlaneList
    SelectStartPlane: Plane
    SelectTrimBounds: ScCollector
    StartPlaneSelected: bool
    TrimDirection: bool
    TrimNewDieFace: bool
    TrimTolerance: float


    class TrimTaskMatchCutType(enum.Enum):
        None = 0
        Start = 1
        End = 2
        Both = 3
    

    class TrimTaskCamType(enum.Enum):
        AerialCam = 0
        BaseMountedCam = 1
        Direct = 2
    

class DieEngTrimAngleCheckBuilder(Builder):
    def __init__(self) -> None: ...
    def GetJoinedSelectedCurves(self, joinedSelectedCurves: typing.List[Curve]) -> None:
        ...
    def SetJoinedSelectedCurves(self, joinedSelectedCurves: typing.List[Curve]) -> None:
        ...
    def GetTrimSideTags(self, trimSideTags: typing.List[Direction]) -> None:
        ...
    def SetTrimSideTags(self, trimSideTags: typing.List[Direction]) -> None:
        ...
    def JoinCurvesAndEdges(self, inputCrvs: typing.List[ICurve], distTol: float, outputCrvs: typing.List[ICurve]) -> None:
        ...
    AutoFit: bool
    CheckPointSpacing: Expression
    DirectionOption: Tooling.DieEngTrimAngleCheckBuilder.DirectionOptions
    ElevationAngle: Expression
    HideSafeZone: bool
    LineScale: float
    MaxAngle: Expression
    MinAngle: Expression
    PlaneAngle: Expression
    TrimmingCurves: ScCollector
    TrimmingDirection: Direction
    TrimmingFaces: ScCollector


    class DirectionOptions(enum.Enum):
        ByVector = 0
        ByAngles = 1
    

class DieEngTrimAngleCheck(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class DieEngStampingOutputBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def DefineSpringback(self) -> None:
        ...
    def SetProperty(self) -> None:
        ...
    SewTolerance: float
    SourceBody: SelectBodyList
    SpringbackMethod: Tooling.DieEngStampingOutputBuilder.SpringbackMethodType
    TargetBody: SelectBody


    class SpringbackMethodType(enum.Enum):
        None = 0
        UniformMembraneExpansion = 1
        OvercrownbyFunction = 2
        OvercrownbySurface = 3
    

    class DisplayProductType(enum.Enum):
        OriginalProduct = 0
        NewProduct = 1
        Both = 2
    

class DieEngStampingCarryoverBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    DieTip: Features.SelectFeature
    GenerateOptimizeToggle: bool
    GenerateOriginalToggle: bool
    StampingOutput: SelectBodyList


class DieEngProcessUpdateManagerBuilder(Builder):
    def __init__(self) -> None: ...
    Type: Tooling.DieEngProcessUpdateManagerBuilder.Types


    class Types(enum.Enum):
        TrimTask = 0
        PierceTask = 1
    

class DieEngLineupBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ObjectProperties(self) -> None:
        ...
    def MoreDetails(self) -> None:
        ...
    Product: SelectNXObjectList
    ReorientProperties: bool
    UpdatePressInformation: bool


class DieEngFormTaskBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetDetails(self) -> str:
        ...
    def SetDetails(self, details: str) -> None:
        ...
    CamDirection: Direction
    DieTip: Features.SelectFeature
    FinishOperation: bool
    PointInRegion: Point
    RegionBounds: ScCollector
    ShapeDetail: SelectDisplayableObjectList


class DieEngDieTipBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ObjectProperties(self) -> None:
        ...
    def MoreDetails(self) -> None:
        ...
    ChangeTipOrientations: bool
    ChangeTipOrigin: bool
    GenerateOutline: bool
    InheritTip: bool
    Origin: Point
    Product: SelectBody
    ReferenceData: SelectNXObjectList
    StampingOperation: SelectNXObject
    SyncOrigin: int
    Thickness: float
    ThicknessType: Tooling.DieEngDieTipBuilder.MaterialThicknessType
    WithoutWorkflow: bool


    class MaterialThicknessType(enum.Enum):
        Uniform = 0
        Variable = 1
    

class DieEngDefineProductOrientationBuilder(Builder):
    def __init__(self) -> None: ...
    def GetReason(self) -> str:
        ...
    def SetReason(self, reason: str) -> None:
        ...
    def ButtonNew(self) -> None:
        ...
    def ButtonCut(self) -> None:
        ...
    def ButtonCopy(self) -> None:
        ...
    def ButtonPaste(self) -> None:
        ...
    def ButtonCopyTip(self) -> None:
        ...
    def ButtonView(self) -> None:
        ...
    def ButtonApplyOptimal(self) -> None:
        ...
    AngleAbout: Direction
    AngleIncrement: float
    AngleValue: float
    AngleValueOptimal: float
    ChooseOptimalMethod: Tooling.DieEngDefineProductOrientationBuilder.OptimalMethod
    ColorDepthPass: NXColor
    ColorDraftAngleFailure: NXColor
    ColorDraftAnglePass: NXColor
    ColorDraftAngleWarning: NXColor
    ColorFailure: NXColor
    ColorWarning: NXColor
    DoublePassTranslucency: float
    DraftAngleScale: float
    FacetQualityOptions: Tooling.DieEngDefineProductOrientationBuilder.FacetQualityOption
    FailureShowIsocline: bool
    FailureValue: float
    FromPoint: Point
    FromVector: Direction
    LimitShading: bool
    NameCSYS: str
    OptimalHoleAxis: ScCollector
    OptimalPoint1: Point
    OptimalPoint2: Point
    OptimalPoint3: Point
    PointInRegion: Point
    PointInRegion1: Point
    ProductCSYS: CoordinateSystem
    ReverseNormal: bool
    ReverseSheetNormal: bool
    ToPoint: Point
    ToVector: Direction
    TrimProfile: ScCollector
    TrimWallAngleScale: float
    ViewRegionBounds: ScCollector
    VisualizeDepth: bool
    VisualizeDraft: bool
    VisualizeDraftOptions: Tooling.DieEngDefineProductOrientationBuilder.ViewDraftOptions
    WarningShowIsocline: bool
    WarningValue: float


    class ViewDraftOptions(enum.Enum):
        None = 0
        ComputeTrimAngles = 1
        ComputeWallAngles = 2
    

    class OptimalMethod(enum.Enum):
        MinimizeBackdraft = 0
        MinimizeDrawDepth = 1
        NormaltoFace = 2
        AxisofHole = 3
        ThreePoints = 4
    

    class FacetQualityOption(enum.Enum):
        Coarse = 0
        Normal = 1
        Fine = 2
        ExtraFine = 3
        UltraFine = 4
    

class DieDesPierceInsertBuilder(Builder):
    def __init__(self) -> None: ...
    BoudaryCurveSelection: ScCollector
    ClearanceCoefficient: float
    DiePenetration: float
    DownToleranceForLength: float
    DownToleranceForWidth: float
    PunchPenetration: float
    ThicknessDirectionOption: Tooling.DieDesPierceInsertBuilder.Direction
    ThicknessValue: float
    ToleranceCoefficient: float
    UpToleranceForLength: float
    UpToleranceForWidth: float


    class HoleShapeTypes(enum.Enum):
        Circular = 0
        Oblong = 1
        Square = 2
        Rectangular = 3
        RoundedRectangular = 4
        ChordRectangular = 5
        Hexagonal = 6
        Other = 7
    

    class Direction(enum.Enum):
        Upper = 0
        Lower = 1
    

class DieDesignTrimPostBuilder(Builder):
    def __init__(self) -> None: ...
    def SeedPointInfo(self, seedPoint: float, seedTangent: float) -> None:
        ...
    BasePlane: Plane
    BeltThickness: float
    BoundaryCurves: Section
    CAMRelief: float
    CamDirection: Direction
    MachineAllowance: float
    Product: SelectBody
    Profiles: SelectNXObjectList
    ProfilesDirection: bool
    UseApproxSheetBody: bool


class DieDesignSettingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.DieDesignSettingBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDieDesignSettingBuilder(self) -> Tooling.DieDesignSettingBuilder:
        ...
    def Tag(self) -> Tag: ...



class DieDesignSettingBuilder(Builder):
    def __init__(self) -> None: ...
    def SetParameters(self, paraNames: str, paraValues: str) -> None:
        ...
    RoundoffInsertXYPosition: bool


class DieDesignLowerBinderBuilder(Builder):
    def __init__(self) -> None: ...
    BasePlane: Plane
    BinderProfiles: SelectNXObjectList
    BinderRelief: float
    BlankProfile: SelectNXObjectList
    BlankProfileOffset: float
    CoreDirection: int
    DeckProfile: SelectNXObjectList
    IsApproxSheetBody: bool
    IsExactBinderProfiles: bool
    LowerDeckThickness: float
    MachineAllowance: float
    OffsetValue: float
    OutWallThickness: float
    OutterWallProfile: SelectNXObjectList
    SheetBody: SelectBody
    UpperDeckOffsetSheet: SelectBody
    UpperDeckRelief: float
    UpperDeckReliefSheet: SelectBody
    UpperDeckThickness: float
    WallThickness: float


class DieDesDrawPunchBuilder(Builder):
    def __init__(self) -> None: ...
    ApproximateSheetbodyOption: bool
    BasePlane: Plane
    BaseThickness: float
    BaseWidth: float
    BeltThickness: float
    CoreDrawPunchOption: bool
    DeckThickness: float
    ExactSheetbodyOption: bool
    FlangeProfile: Section
    MachiningAllowance: float
    MainWallCenterLine: Section
    PunchCurve: SelectNXObjectList
    ReliefAngle: float
    ReliefDistance: float
    SheetBody: SelectBody
    SheetBodyDeck: SelectBody
    TfeatureSet: Features.Feature
    WallThickness: float


class DieDesDrawDieBuilder(Builder):
    def __init__(self) -> None: ...
    ApproximateSheetbodyOption: bool
    BasePlane: Plane
    BaseThickness: float
    BinderEdgeOffset: float
    BlankCurve: SelectNXObjectList
    CoreDrawDieOption: bool
    DeckEdgeOffset: float
    DeckFlangeThickness: float
    DeckThickness: float
    ExactSheetbodyOption: bool
    FlangeCurve: SelectNXObjectList
    FlangeOffset: float
    MachiningAllowance: float
    PunchCurve: SelectNXObjectList
    SheetBody: SelectBody
    TfeatureSet: Features.Feature
    WallThickness: float


class DieCavityAndSlugHoleBuilder(Builder):
    def __init__(self) -> None: ...
    def DieEditOffsetValueTable(self) -> None:
        ...
    def NormalCreateCavityAndSlug(self) -> None:
        ...
    AngleDiePlateTwo: float
    DieInsertStack: Tooling.DieCavityAndSlugHoleBuilder.DieInsertStackType
    DieOffsetValue: float
    DiePlateThree: float
    DiePlateTwo: float
    DieSameOffsetValue: bool
    ForEachScrapDiePlateThree: bool
    ForEachScrapDiePlateTwo: bool
    NewPartNames: str
    NormalBottomBackPlateSlug: Tooling.DieCavityAndSlugHoleBuilder.BottomPlateSlugItems
    NormalCavity: Tooling.DieCavityAndSlugHoleBuilder.CavityTypeItems
    NormalClearance: float
    NormalClearanceOption: Tooling.DieCavityAndSlugHoleBuilder.ClearanceOptionItems
    NormalDieShoeSlug: Tooling.DieCavityAndSlugHoleBuilder.DieShoeSlugTypeItems
    NormalForEachScrap1: bool
    NormalForEachScrap2: bool
    NormalOffsetSide: Tooling.DieCavityAndSlugHoleBuilder.OffsetSideOptionItems
    NormalRenameDialog: bool
    NormalSelectPierceDieInsert: SelectBodyList
    NormalSlugInDiePlateThree: Tooling.DieCavityAndSlugHoleBuilder.DiePlateThreeSlugType
    NormalSlugInDiePlateTwo: Tooling.DieCavityAndSlugHoleBuilder.DiePlateTwoSlugType
    NormalSlugParameter1: float
    NormalSlugParameter2: float
    NormalSlugParameter3: float
    NormalSlugParameter4: float
    OffsetLinearDimension: Expression
    ParentPartName: str
    Position: Tooling.DieCavityAndSlugHoleBuilder.InsertPositionItems
    SelectOffsetSpreadsheet: str
    SelectScrap: SelectBodyList
    SelectSketch: SelectSketch
    ShimHeight: float
    ShimOffset: float
    SlugHoleHeightLinearDimension: Expression
    SlugPreviousParameterA: float
    SlugPreviousParameterC1: float
    SlugPreviousParameterC2: float
    SpacerAngle: float
    SpacerOffset: float
    WaferHeight: float


    class OffsetSideOptionItems(enum.Enum):
        DieSide = 0
        PunchSide = 1
    

    class InsertPositionItems(enum.Enum):
        Top = 0
        Bottom = 1
    

    class DieShoeSlugTypeItems(enum.Enum):
        Fillet = 0
        Rectangle = 1
        Circle = 2
        Mickey = 3
        Clearance = 4
        SlotVer = 5
        SlotHor = 6
        None = 7
    

    class DiePlateTwoSlugType(enum.Enum):
        Fillet = 0
        Rectangle = 1
        Circle = 2
        Mickey = 3
        Clearance = 4
        Slotver = 5
        Slothor = 6
        None = 7
    

    class DiePlateThreeSlugType(enum.Enum):
        Fillet = 0
        Rectangle = 1
        Circle = 2
        Mickey = 3
        Cleanrance = 4
        Slotver = 5
        Slothor = 6
        None = 7
    

    class DieInsertStackType(enum.Enum):
        One = 0
        Two = 1
        Three = 2
    

    class ClearanceOptionItems(enum.Enum):
        Constant = 0
        Variable = 1
    

    class CavityTypeItems(enum.Enum):
        TaperAngle = 0
        Step = 1
        RoundStep1 = 2
        RoundStep2 = 3
    

    class BottomPlateSlugItems(enum.Enum):
        Fillet = 0
        Rectangle = 1
        Circle = 2
        Mickey = 3
        Clearance = 4
        SlotVer = 5
        SlotHor = 6
        None = 7
    

class DieBaseCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.DieBaseBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDieBaseBuilder(self) -> Tooling.DieBaseBuilder:
        ...
    def Tag(self) -> Tag: ...



class DieBaseBuilder(Builder):
    def __init__(self) -> None: ...
    def PickArea(self) -> None:
        ...
    def RefPoint(self) -> None:
        ...
    def DieBaseReg(self) -> None:
        ...
    def DieBaseData(self) -> None:
        ...
    def PickSplitLocation(self) -> None:
        ...
    def PickLocation(self) -> None:
        ...
    def DeleteSelectedDieBase(self) -> None:
        ...
    AdjustedPlateLength: float
    AlongDirection: Tooling.DieBaseBuilder.AlongDirectionOpt
    Catalog: Tooling.DieBaseBuilder.CatalogOpt
    CatalogName: str
    Close: float
    CreateSplittingCurves: Section
    DbEdgeDistance: float
    DbRefPointX: float
    DbRefPointY: float
    DesignToolOpt: Tooling.DieBaseBuilder.DesignToolOption
    DieBase: SelectBody
    DieBaseOrSubDieBase: SelectBodyList
    DieBaseToDelete: SelectBodyList
    DieBaseType: Tooling.DieBaseBuilder.DieBaseTypeOpt
    FirstLength: float
    GapFirst: float
    GapSecond: float
    IsLaunchFromReuseLibrary: bool
    LoadDBOnly: bool
    NewDieBaseName: str
    OpenDist: float
    ParentNode: Tooling.DieBaseBuilder.ParentNodeOpt
    ParentPartName: str
    PlateLength: float
    PlateTypeName: str
    PlateWidth: float
    PlatesNumber: Tooling.DieBaseBuilder.PlatesNumberOpt
    Rename: bool
    SecondLength: float
    SelectPlateToSplit: SelectPart
    SelectSubDieBase: SelectPart
    SelectSubDieBaseSketch: SelectSketchList
    SplitGap: float
    SplitSubSingle: Tooling.DieBaseBuilder.SplitMethod
    StandardOrUserDefined: Tooling.DieBaseBuilder.SplitOption
    StripTravelDistance: float
    Type: Tooling.DieBaseBuilder.Types
    UpdateDieBasePosition: bool
    XDistanceFirst: float
    XDistanceSecond: float
    YDistanceFirst: float
    YDistanceSecond: float


    class Types(enum.Enum):
        StandardDieBase = 0
        CustomizeDieBase = 1
        DesignTools = 2
    

    class SplitOption(enum.Enum):
        Standard = 0
        UserDefined = 1
    

    class SplitMethod(enum.Enum):
        WholeSubDiebase = 0
        SinglePlate = 1
    

    class PlatesNumberOpt(enum.Enum):
        PlateFive = 0
        PlateEight = 1
        PlateNine = 2
        PlateTen = 3
        PlateTwelve = 4
    

    class ParentNodeOpt(enum.Enum):
        Control = 0
        Die = 1
        SubFirst = 2
        SubSecond = 3
        DieBaseFirst = 4
    

    class DieBaseTypeOpt(enum.Enum):
        Pdw = 0
        SingleDie = 1
        CompoundDie = 2
        DrawDie = 3
    

    class DesignToolOption(enum.Enum):
        Split = 0
        Merge = 1
        Align = 2
        Adjust = 3
        Save = 4
        Delete = 5
    

    class CatalogOpt(enum.Enum):
        Dme = 0
        Futaba = 1
    

    class AlongDirectionOpt(enum.Enum):
        AlongXDirection = 0
        AlongYDirection = 1
    

class DesignTrimToolCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.DesignTrimToolBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDesignTrimToolBuilder(self) -> Tooling.DesignTrimToolBuilder:
        ...
    def Tag(self) -> Tag: ...



class DesignTrimToolBuilder(Builder):
    def __init__(self) -> None: ...
    def SetTrimDataDetails(self, trimPart: NXObject, sourceObjectOcc: NXObject, currentTrimSurfaceName: str, previousTrimSurfaceName: str) -> None:
        ...
    def CreateNewComponent(self, partName: str, instanceName: str) -> Assemblies.Component:
        ...
    def CreateDefaultSheet(self, surfaceName: str, trimPart: NXObject, sheetType: int, layer: int) -> NXObject:
        ...
    NewSurfaceLayer: int
    SourceObject: SelectNXObject


class DesignEjectorPinBuilder(Builder):
    def __init__(self) -> None: ...
    def GetEjectorRecords(self) -> Tooling.EjectorRecords:
        ...
    def SetEjectorRecords(self, ejectorRecords: Tooling.EjectorRecords) -> None:
        ...
    def GetReferenceSet(self) -> str:
        ...
    def SetReferenceSet(self, referenceSet: str) -> None:
        ...
    def GetEjectorClientData(self) -> Tooling.StandardPartData:
        ...
    def SetEjectorClientData(self, standardClientData: Tooling.StandardPartData) -> None:
        ...
    def GetParameterTreeData(self) -> Tooling.SpreadsheetData:
        ...
    def SetParameterTreeData(self, sheetData: Tooling.SpreadsheetData) -> None:
        ...
    def GetSelectedEjectorComponent(self) -> NXObject:
        ...
    def XAlignment(self) -> None:
        ...
    def YAlignment(self) -> None:
        ...
    def SearchSleeve(self, maxPinDia: str) -> None:
        ...
    def GetSymbolAngle(self, symbolTag: Annotations.PmiCustomSymbol) -> float:
        ...
    def DeleteConceptEjector(self, singleRecord: Tooling.EjectorDesignData) -> None:
        ...
    def DeleteEjector(self) -> None:
        ...
    def DeleteDumbDesignPoints(self) -> None:
        ...
    def ReadEjectorClientDataFromLibrary(self, isFromMemberView: bool, dataType: int, libName: str, libPath: str) -> None:
        ...
    def ResetStandardClientData(self, singleRecord: Tooling.EjectorDesignData) -> None:
        ...
    def RepositionEjector(self, singleRecord: Tooling.EjectorDesignData, fileName: str, refsetName: str) -> None:
        ...
    def GetAddInstanceInformation(self, pinLength: str, sleeveLength: str, pinType: int, beyondRange: bool, isSleeve: bool, updateTemplateData: bool) -> bool:
        ...
    def AddEjectorPart(self, conceptRecord: Tooling.ConceptStandardPartRecord, destinationCsys: float, pinType: int, pinLength: str, sleeveLength: str, isRecommended: bool, ejectorCsys: float) -> Annotations.PmiCustomSymbol:
        ...
    def AddInstanceOfExistingEjector(self, destinationCsys: float, pinType: int, pinLength: str, sleeveLength: str, isRecommended: bool, ejectorCsys: float, isPointDeleted: bool) -> Annotations.PmiCustomSymbol:
        ...
    def UpdateDataOfInstance(self) -> None:
        ...
    def FindPinMaxDiameter(self) -> str:
        ...
    def SetParentParts(self, bAnalyze: bool) -> None:
        ...
    def RestoreParameterOfInstance(self) -> None:
        ...
    def EditConceptEjector(self) -> None:
        ...
    def SetEditRecords(self) -> Annotations.PmiCustomSymbol:
        ...
    def CreatePoint(self, createNewPoint: bool, coordinates: float, conceptObjectLayer: int) -> Point:
        ...
    def GetInstallPointMatrix(self, pointTag: NXObject, matrix: Matrix3x3) -> Point3d:
        ...
    def UpdateLengthForConceptEjector(self) -> None:
        ...
    def GetMoveVector(self, pointTag: NXObject, origin: Point3d) -> Vector3d:
        ...
    def ResetPointsCoordinates(self, pointTag: NXObject, matrix: Matrix3x3, moveVector: Vector3d, currentHandle: int, gesture: int, moveType: int, snapDistance: float, angle: float) -> Point3d:
        ...
    def UpdateSpreadsheetDataWithObject(self, objectWithParameters: NXObject, isConcpetObject: bool, designData: Tooling.EjectorDesignData, sheetData: Tooling.SpreadsheetData) -> None:
        ...
    def UpdateComponentData(self, nativeDataPath: str, partOcc: NXObject, sheetData: Tooling.SpreadsheetData) -> None:
        ...
    CalculateLength: bool
    CreateComponentType: Tooling.DesignEjectorPinBuilder.ComponentType
    DefinitionType: Tooling.DesignEjectorPinBuilder.DefineType
    EjectorPoints: SelectNXObjectList
    EjectorType: Tooling.DesignEjectorPinBuilder.EjectorPinType
    InsertPoint: TaggedObject
    ParentIndex: int
    ReferencePoint: TaggedObject
    Rename: bool
    SleevePoints: SelectNXObjectList
    UseSymbol: bool


    class EjectorPinType(enum.Enum):
        Straight = 0
        Shoulder = 1
        Blade = 2
        Sleeve = 3
    

    class DefineType(enum.Enum):
        Insert = 0
        Edit = 1
    

    class ComponentType(enum.Enum):
        Instance = 0
        NewPart = 1
    

class DefineNeutralFactorBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BendDevelopedLength: float
    NeutralFactor: str
    NeutralFactorFormula: Tooling.DefineNeutralFactorBuilder.FormulaOptions
    PartMaterial: str


    class FormulaOptions(enum.Enum):
        General = 0
        BendAllowance = 1
    

class DefineLifterBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteGenericLifter(self, lifterName: str) -> None:
        ...
    def DeleteLifterOnLifter(self, lifterName: str) -> None:
        ...
    LifterBodies: SelectDisplayableObjectList
    LifterDriveBodies: SelectDisplayableObjectList
    LifterDriveVector: Direction
    LifterName: str
    LifterOnBodies: SelectDisplayableObjectList
    LifterOnDriveVector: Direction
    LifterOnLifterVector: Direction
    LifterOnName: str
    LifterVector: Direction
    MainLifterBodies: SelectDisplayableObjectList
    MainLifterDriveBodies: SelectDisplayableObjectList
    MainLifterDriveVector: Direction
    MainLifterVector: Direction
    Type: Tooling.DefineLifterBuilder.Types


    class Types(enum.Enum):
        GenericLifter = 0
        LifteronLifter = 1
    

class DefineCamBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteLinearCam(self, camName: str) -> None:
        ...
    def DeleteRotaryCam(self, camName: str) -> None:
        ...
    def DeleteRockerCam(self, camName: str) -> None:
        ...
    def DeleteCushion(self, cushionName: str) -> None:
        ...
    CamName: str
    CushionBody: SelectDisplayableObjectList
    CushionDirection: Direction
    CushionName: str
    LinearBackstopOffset: Expression
    LinearCamBodies: SelectDisplayableObjectList
    LinearDirection: Direction
    LinearDriveBodies: SelectDisplayableObjectList
    MotionDistance: float
    PredefinedHydraulicOption: Tooling.DefineCamBuilder.PredefinedHydraulicOptions
    PressStartAngle: float
    PressStopAngle: float
    ReturnStartAngle: float
    ReturnStopAngle: float
    RockerAxisBackstopOffset: Expression
    RockerAxisDirection: Axis
    RockerCamBodies: SelectDisplayableObjectList
    RockerCamDirection: Direction
    RockerCamRockerBodies: SelectDisplayableObjectList
    RockerDriveBodies: SelectDisplayableObjectList
    RotaryBackstopOffset: Expression
    RotaryCamBodies: SelectDisplayableObjectList
    RotaryDirection: Axis
    RotaryDriveBodies: SelectDisplayableObjectList
    Type: Tooling.DefineCamBuilder.Types


    class Types(enum.Enum):
        LinearCam = 0
        RotaryCam = 1
        RockerCam = 2
        CushionProgram = 3
    

    class PredefinedHydraulicOptions(enum.Enum):
        None = 0
        BeforeMoldOpen = 1
        BeforeEjection = 2
    

class CutoutAreaData(Tooling.CostDataObject):
    def __init__(self) -> None: ...


class CreateMoldDesignReportBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSlideValues(self) -> str:
        ...
    def SetSlideValues(self, slideName: str) -> None:
        ...
    def GetReportedSlides(self) -> str:
        ...
    def SetReportedSlides(self, reportedSlideName: str) -> None:
        ...
    def GetComment(self) -> str:
        ...
    def SetComment(self, comment: str) -> None:
        ...
    def OpenPowerPointFile(self) -> None:
        ...
    def GetCurrentSlideName(self, currentIndex: int) -> str:
        ...
    def ParseReportFile(self) -> None:
        ...
    def GetLocalizedSlideNames(self) -> str:
        ...
    def SetLocalizedSlideNames(self, localizedSlideNames: str) -> None:
        ...
    AddPictureType: Tooling.CreateMoldDesignReportBuilder.ImageType
    FileName: str
    ImageCapture: Gateway.ImageCaptureBuilder
    ImageFileName: str
    NavNodeTag: TaggedObject
    OutputLocation: str
    ReadOnlyStatus: bool
    SlideSelection: int


    class ImageType(enum.Enum):
        Append = 0
        Replace = 1
    

class CreateBoxCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.CreateBoxBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBoxBuilder(self, boxFrec: NXObject) -> Tooling.CreateBoxBuilder:
        ...
    def Tag(self) -> Tag: ...



class CreateBoxBuilder(Builder):
    def __init__(self) -> None: ...
    def SetBoxMatrixAndPosition(self, matrix: Matrix3x3, position: Point3d) -> None:
        ...
    def ConvertFrecToBuilderData(self, featTag: NXObject) -> None:
        ...
    def SetBoxColorValue(self, value: Point3d) -> None:
        ...
    def SetBoxCsysPosition(self, value: Point3d) -> None:
        ...
    def GetBoxCsysPosition(self) -> Point3d:
        ...
    def SetSelectedOccs(self, selections: typing.List[NXObject], deselections: typing.List[NXObject]) -> None:
        ...
    def GetBoxFeatTag(self) -> NXObject:
        ...
    BoxColor: int
    Clearance: Expression
    Objects: ScCollector
    OffsetNegativeX: Expression
    OffsetNegativeY: Expression
    OffsetNegativeZ: Expression
    OffsetPositiveX: Expression
    OffsetPositiveY: Expression
    OffsetPositiveZ: Expression
    Type: Tooling.CreateBoxBuilder.BoxType
    XValue: Expression
    YValue: Expression
    ZValue: Expression


    class BoxType(enum.Enum):
        General = 0
        Bounding = 1
    

class CostTableDataProvider(TaggedObject):
    def __init__(self) -> None: ...
    def SetRowObjectInMap(self, rowIndex: int, costObject: Tooling.CostDataObject) -> None:
        ...
    def AskRowObjectInMap(self, rowIndex: int) -> Tooling.CostDataObject:
        ...
    def ClearRowObjectMap(self) -> None:
        ...
    def SetString(self, rows: int, column: int, stringData: str) -> bool:
        ...
    def SetString(self, rows: int, column: int, stringData: str) -> bool:
        ...
    def GetString(self, row: int, column: int) -> str:
        ...
    def SetInteger(self, rows: int, column: int, integerData: int) -> bool:
        ...
    def SetInteger(self, rows: int, column: int, integerData: int) -> bool:
        ...
    def GetInteger(self, row: int, column: int, isUnassigned: bool) -> int:
        ...
    def SetDouble(self, rows: int, column: int, doubleData: float) -> bool:
        ...
    def SetDouble(self, rows: int, column: int, doubleData: float) -> bool:
        ...
    def GetDouble(self, row: int, column: int, isUnassigned: bool) -> float:
        ...
    def SetBoolean(self, rows: int, column: int, booleanData: bool) -> bool:
        ...
    def SetBoolean(self, rows: int, column: int, booleanData: bool) -> bool:
        ...
    def GetBoolean(self, row: int, column: int) -> bool:
        ...
    def UnsetValue(self, row: int, column: int) -> bool:
        ...
    def UnsetValue(self, rows: int, column: int) -> bool:
        ...
    def Destroy(self) -> None:
        ...
    ColumnCount: int
    RowCount: int


class CostDataObject(TaggedObject):
    def __init__(self) -> None: ...
    def AskCostObjects(self, objectType: int, objectSubtype: int, costObjects: typing.List[Tooling.CostDataObject]) -> None:
        ...
    def AskFeatureRelatedFacetsWithChildren(self, pFacetIds: int) -> None:
        ...
    def AskCostObjectParameterValues(self, costObjectStringValueList: str) -> None:
        ...


class CornerDesignCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.CornerDesignBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCornerDesignBuilder(self) -> Tooling.CornerDesignBuilder:
        ...
    def Tag(self) -> Tag: ...



class CornerDesignBuilder(Builder):
    def __init__(self) -> None: ...
    ChamferAngle: Expression
    CornerType: Tooling.CornerDesignBuilder.CornerTypeOpt
    FirstVectorForBunnyEar: Direction
    Offset: Expression
    RadiusDia: Expression
    SecondVectorForBunnyEar: Direction
    SelectCorner: Features.SelectFeatureList
    SelectEdge: SelectEdgeList
    SelectFrom: Tooling.CornerDesignBuilder.SelectFromOpt
    Type: Tooling.CornerDesignBuilder.Types


    class Types(enum.Enum):
        Create = 0
        Edit = 1
        Delete = 2
    

    class SelectFromOpt(enum.Enum):
        Both = 0
        PartBody = 1
        PocketBody = 2
    

    class CornerTypeOpt(enum.Enum):
        Chamfer = 0
        Fillet = 1
        Mickey = 2
        BunnyEar = 3
    

class CopySolidBuilder(Builder):
    def __init__(self) -> None: ...
    def GetParentFromConfigurationRecord(self) -> str:
        ...
    def UpdateCloneItemsName(self) -> None:
        ...
    def SetTemplateAttribute(self, templateName: str, attributeName: str, attributeValue: str, deleteAttr: bool) -> None:
        ...
    def ClearPartItems(self) -> None:
        ...
    def SetIsDefinedParent(self, isDefinedParent: bool) -> None:
        ...
    def UpdateClonePartItems(self, updateType: Tooling.CopySolidBuilder.PartItemUpdateType) -> None:
        ...
    Associative: bool
    CloneObject: Tooling.CloneObject
    CopyDestinationSelection: Tooling.CopySolidBuilder.CopyDestinationType
    DestinationComponent: Assemblies.SelectComponent
    FixAtCurrentTimestamp: bool
    MultipleComponents: bool
    OriginalBodyLayer: int
    OriginalBodyOperation: Tooling.CopySolidBuilder.OriginalOperationOption
    SelectBodies: SelectBodyList
    SelectParentPartOcc: Assemblies.SelectComponent
    TemplateNameListValue: str
    WizardType: Tooling.ToolingApplication


    class PartItemUpdateType(enum.Enum):
        Restore = 0
        Rebuild = 1
    

    class OriginalOperationOption(enum.Enum):
        None = 0
        Hide = 1
        MoveToLayer = 2
        Delete = 3
    

    class CopyDestinationType(enum.Enum):
        NewComponent = 0
        NewComponentFromAttribute = 1
        ExistingComponent = 2
    

class CoolingPatternCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.CoolingPatternBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCoolingPatternBuilder(self) -> Tooling.CoolingPatternBuilder:
        ...
    def Tag(self) -> Tag: ...



class CoolingPatternBuilder(Builder):
    def __init__(self) -> None: ...
    ChannelDiameter: float
    ChannelGuide: Section
    Diameter: Expression
    DiameterListValue: str


class CoolingFittingData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddFittingPoints(self, fittingPoint: Point) -> None:
        ...
    def RemoveFittingPoint(self, fittingPoint: Point) -> None:
        ...
    def ClearFittingPoints(self) -> None:
        ...


class CoolingExtendCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.CoolingExtendBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCoolingExtendBuilder(self) -> Tooling.CoolingExtendBuilder:
        ...
    def Tag(self) -> Tag: ...



class CoolingExtendBuilder(Builder):
    def __init__(self) -> None: ...
    AdjustBoundaryChannel: bool
    BoundaryChannelExtension: float
    ExtendChannel: SelectBodyList
    ExtensionValue: Expression
    LimitBody: SelectBody
    RemoveParameter: bool
    ReverseDirection: bool
    RoundTip: bool
    TipAngle: float
    TipAngleValue: Expression
    TipEndType: Tooling.CoolingExtendBuilder.TipEndTypes


    class TipEndTypes(enum.Enum):
        None = 0
        Angle = 1
        Round = 2
    

class CoolingDefineChannelCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.CoolingDefineChannelBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCoolingDefineChannelBuilder(self) -> Tooling.CoolingDefineChannelBuilder:
        ...
    def Tag(self) -> Tag: ...



class CoolingDefineChannelBuilder(Builder):
    def __init__(self) -> None: ...
    def SetBoundaryBody(self, body: Body) -> None:
        ...
    def AutoGetBoundaryBody(self) -> None:
        ...
    def SetAutoSelectBoundary(self, autoSelectBoundary: bool) -> None:
        ...
    def SetNXVersionNumber(self, version: int) -> None:
        ...
    def SetChannelCreationParameters(self, channelTipVector: Vector3d, channelStartPt: Point3d, channelEndPt: Point3d, tipLocation: Point3d) -> None:
        ...
    def SetBoundaryClosePointsToChannel(self, closeToTipEnd: Point3d, closeToHandle: Point3d) -> None:
        ...
    AdjustBoundaryChannel: bool
    AdjustChannelStart: bool
    ChannelDiameter: float
    ChannelType: Tooling.CoolingDefineChannelBuilder.Types
    Diameter: Expression
    DiameterListValue: str
    DistanceToBoundary: Expression
    ExtensionSolution: Tooling.CoolingDefineChannelBuilder.ExtensionTypes
    LimitBody: SelectBody
    Motion: GeometricUtilities.ModlMotion
    RemoveParameter: bool
    StartPoint: Point
    TipAngle: Expression
    TipEndType: Tooling.CoolingDefineChannelBuilder.TipEndTypes
    Type: Tooling.CoolingDefineChannelBuilder.Types


    class Types(enum.Enum):
        Channel = 0
        Baffle = 1
    

    class TipEndTypes(enum.Enum):
        None = 0
        Angle = 1
        Round = 2
    

    class ExtensionTypes(enum.Enum):
        NoExtension = 0
        AlongExtrusionDirection = 1
        AlongReverseExtrusionDirection = 2
        AlongBothDirections = 3
    

class CoolingConnectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.CoolingConnectBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCoolingConnectBuilder(self) -> Tooling.CoolingConnectBuilder:
        ...
    def Tag(self) -> Tag: ...



class CoolingConnectBuilder(Builder):
    def __init__(self) -> None: ...
    ConnectVector: Direction
    DefineConnectVector: bool
    DefineStartPoint: bool
    FirstChannel: SelectBody
    SecondChannel: SelectBody
    StartPoint: Point


class ConformalOffsetBuilder(Builder):
    def __init__(self) -> None: ...
    def GenerateIntersectionPlanes(self) -> None:
        ...
    def CreateConformalCurves(self) -> None:
        ...
    def AdjustSmoothCorner(self) -> None:
        ...
    def UpdateTubesStatus(self) -> None:
        ...
    def DeleteOffsetBodiesCreatedFromExtractedFacesFeatures(self, numFromEnd: int) -> None:
        ...
    def UpdateCheckingOffsetFeatures(self) -> None:
        ...
    def SetPreviewOn(self, previewEnabled: bool) -> None:
        ...
    def SetUpdateFacetBody(self, isUpdateFacetBody: bool) -> None:
        ...
    def SetUpdateChanged(self, isUpdateChanged: bool) -> None:
        ...
    def SetIsAdjustSmoothCorner(self, isAdjustSmoothCorner: bool) -> None:
        ...
    def PreviewBodies(self) -> None:
        ...
    def UpdateSelectionAfterMoveHandle(self, profiles: typing.List[Point]) -> None:
        ...
    def SetBackUpMovePoint(self, backPoint: Point) -> None:
        ...
    Associative: bool
    BooleanTool: GeometricUtilities.BooleanToolBuilder
    ConncetType: Tooling.ConformalOffsetBuilder.ConnectType
    CoolingDiameter: Expression
    CornerAngleLimit: Expression
    CreateBodyMethod: int
    CurveSmoothRates: int
    DistanceToFace: Expression
    ManipulatorOrigin: Point3d
    OffsetBody: SelectBodyList
    OffsetCheck: bool
    OffsetFaces: ScCollector
    OriginalCurveLayer: int
    OriginalCurveOperation: Tooling.ConformalOffsetBuilder.OriginalCurveOperationType
    PlaneInterval: Expression
    PlaneNum: int
    PlaneStartValue: Expression
    ProjectDirection: Direction
    ProjectDirectionMethod: Features.ProjectCurveBuilder.DirectionType
    ProjectGuideLines: Section
    ReverseDirection: bool
    ReversePlaneDirection: bool
    SampleDistance: Expression
    SelectExistingCurves: Section
    SelectReferObjects: ScCollector
    ShowTubes: bool
    Tolerance: float
    Type: Tooling.ConformalOffsetBuilder.Action


    class OriginalCurveOperationType(enum.Enum):
        None = 0
        Hide = 1
        MovetoLayer = 2
        Delete = 3
    

    class CreateType(enum.Enum):
        New = 0
        Existing = 1
        None = 2
    

    class ConnectType(enum.Enum):
        Default = 0
        Connect = 1
        Enclose = 2
    

    class Action(enum.Enum):
        ExistingCurves = 0
        Intersection = 1
        Projection = 2
        SpecifyPoint = 3
        Automatic = 4
        None = 5
    

class ConformalCoolingManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def CreateBuilder(self) -> Tooling.ConformalCoolingBuilder:
        ...
    def Tag(self) -> Tag: ...



class ConformalCoolingBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateOffsetConvergentBody(self) -> None:
        ...
    def CreateConvergentBody(self) -> None:
        ...
    def GetInApplyStatus(self) -> bool:
        ...
    def SetInApplyStatus(self, inApplyStatus: bool) -> None:
        ...
    def InitConformalCoolingFacetsData(self, changingBody: bool) -> None:
        ...
    def UpdateFacetsDisplay(self) -> None:
        ...
    def GetInUnitTest(self) -> bool:
        ...
    def SetInUnitTest(self, inUnitTest: bool) -> None:
        ...
    AllFaces: bool
    ConformalCoolingBody: ScCollector
    DisplayColor: NXColor
    DisplayEntity: Tooling.ConformalCoolingBuilder.DisplayEntityType
    DisplayMode: Tooling.ConformalCoolingBuilder.DisplayModeType
    DisplayResolution: Tooling.ConformalCoolingBuilder.DisplayResolutionOption
    DisplayTranslucency: int
    DynamicPointOnFace: SelectFace
    FacesToDisplay: ScCollector
    OffsetDistance: float
    SaveConvergentBody: bool


    class DisplayResolutionOption(enum.Enum):
        Standard = 0
        Fine = 1
        ExtraFine = 2
        SuperFine = 3
        UltraFine = 4
    

    class DisplayModeType(enum.Enum):
        Wireframe = 0
        Colorfill = 1
        Both = 2
    

    class DisplayEntityType(enum.Enum):
        Facet = 0
        BoundaryCube = 1
        OffsetLayerCube = 2
        InnerCube = 3
    

class ConformalCircuitBuilder(Builder):
    def __init__(self) -> None: ...
    def SetCircuitNodeName(self, index: int, nodeName: str) -> None:
        ...
    def InitializeConformalCircuitData(self) -> None:
        ...
    def UpdateConformalCircuitData(self, type: Tooling.ConformalCircuitBuilder.CircuitNodeAction, deleteNodes: str) -> None:
        ...
    def AdjustSmoothCorner(self, nodeName: str) -> None:
        ...
    def UpdateTubesStatus(self, nodeName: str) -> None:
        ...
    def UpdateConformalCurveSection(self, curve: typing.List[Curve]) -> None:
        ...
    def RemoveSingleCurveObjectFromACircuitData(self, objectTag: NXObject) -> None:
        ...
    def SetShowChannelFlag(self, nodeName: str, checkedFlag: bool) -> None:
        ...
    def InitializeNodeOfConformalCircuitData(self) -> None:
        ...
    Associative: bool
    ConformalCurve: Section
    CoolingDiameter: Expression
    CornerAngleLimit: Expression
    CurveSmoothRates: int
    OriginalCurveLayer: int
    OriginalCurveOperation: Tooling.ConformalCircuitBuilder.OriginalCurveOperationType
    SampleDistance: Expression
    SmoothCurve: bool


    class OriginalCurveOperationType(enum.Enum):
        None = 0
        Hide = 1
        MovetoLayer = 2
        Delete = 3
    

    class CircuitNodeAction(enum.Enum):
        Remove = 0
        Hide = 1
        Show = 2
        ShowOnly = 3
        Add = 4
        Update = 5
        All = 6
        Diameter = 7
        None = 8
    

class ConcurrentDesignManagementBuilder(Builder):
    def __init__(self) -> None: ...
    DesignTasks: str
    DesignerName: str
    ProjectLeader: str
    SelectComponent: Assemblies.SelectComponent
    SelectedDesignerIndex: int
    SetAsMyDefaultTask: bool
    TaskDescription: str
    Type: Tooling.ConcurrentDesignManagementBuilder.Types
    UpdateOptions: Tooling.ConcurrentDesignManagementBuilder.UpdateTypes
    UserName: str


    class UpdateTypes(enum.Enum):
        SaveMyComponents = 0
        UpdateOtherComponents = 1
    

    class Types(enum.Enum):
        DesignerLogin = 0
        TaskAssignment = 1
        SaveAndUpdate = 2
    

class ConceptStandardPartRecord(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def UpdateValues(self, entity: NXObject) -> None:
        ...
    def AddConceptObject(self, specifiedPoint: Point3d, positionMatrix: Matrix3x3) -> NXObject:
        ...


class ConceptPositionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ConceptPositionBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateConceptPositionBuilder(self) -> Tooling.ConceptPositionBuilder:
        ...
    def Tag(self) -> Tag: ...



class ConceptPositionBuilder(Builder):
    def __init__(self) -> None: ...
    def GetAttributeData(self) -> Tooling.ConceptStandardPartRecord:
        ...
    def SetAttributeData(self, conceptRecord: Tooling.ConceptStandardPartRecord) -> None:
        ...
    def GetSelectedPoints(self, selectedPoints: typing.List[Point]) -> None:
        ...
    def AddToSelectedPoints(self, point: Point) -> None:
        ...
    def InsertSymbol(self, attachPoint: Point) -> None:
        ...
    def AddLinkFeature(self, sketch: NXObject) -> typing.List[Point]:
        ...
    def Clear(self) -> None:
        ...
    LocatedPoint: Point
    PartPosition: Section


class ConceptDieBaseBuilder(Builder):
    def __init__(self) -> None: ...
    def GetExpressionValue(self, expName: str) -> str:
        ...
    def SetExpressionValue(self, expName: str, expressionValue: str) -> None:
        ...
    def SetBasePointYValue(self) -> None:
        ...
    DistanceToDieBaseEdge: float
    IndexStringList: str
    LengthPL: float
    ReferencePoint: Point
    SelectConceptDieBaseSpreadsheet: str
    SubDieBaseNumber: int
    UpdateDieBasePositionAccordingToStrip: bool
    WidthPW: float
    WizardType: int
    XEndDistance: float
    XStartDistance: float
    YDistanceFirst: float
    YDistanceSecond: float


class CompDrawingBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateAll(self) -> None:
        ...
    def DeleteDrawing(self, pName: str, dFile: str, dName: str, templateName: str) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Tooling.CompDrawingBuilder.DeleteCompDrawing instead.")"""
        ...
    def OpenDrawing(self, pName: str, dFile: str, dName: str, templateName: str) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Tooling.CompDrawingBuilder.OpenCompDrawing instead.")"""
        ...
    def EditDrawing(self, pName: str, dFile: str, dName: str, templateName: str) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Tooling.CompDrawingBuilder.EditCompDrawing instead.")"""
        ...
    def InitConstructor(self) -> None:
        ...
    def DeleteCompSheet(self, component: NXObject, componentPartName: str, drawingFileName: str, drawingName: str, templateName: str) -> None:
        ...
    def OpenCompDrawing(self, component: NXObject, componentPartName: str, drawingFileName: str, drawingName: str, templateName: str) -> None:
        ...
    def EditCompDrawing(self, component: NXObject, componentPartName: str, drawingFileName: str, drawingName: str, templateName: str, oldSheetName: str) -> None:
        ...
    def DeleteCompDrawing(self, component: NXObject, componentPartName: str, drawingFileName: str, drawingName: str, templateName: str) -> None:
        ...
    def SetDisplayState(self, displayState: int, layout: str, drawingTag: NXObject) -> None:
        ...
    def AssignAttribute(self, objectTag: NXObject, attributeTitle: str, attributeValue: str) -> None:
        ...
    def CreateComponentDrawing(self, component: NXObject, componentPartName: str, drawingFileName: str, drawingName: str, templateName: str, attributeTitles: str, attributeValues: str, viewScale: float, referenceSet: Tooling.CompDrawingBuilder.ReferenceSet, renderingStyle: Tooling.CompDrawingBuilder.RenderingStyleOption) -> None:
        ...
    def ChangeRenderingStyle(self, styleOption: Tooling.CompDrawingBuilder.RenderingStyleOption) -> None:
        ...
    def ChangeReferenceSet(self, compTag: NXObject) -> None:
        ...
    def ChangeViewScale(self, scale: float) -> None:
        ...
    def AddComponentSheet(self, component: NXObject, componentPartName: str, drawingFileName: str, drawingName: str, templateName: str, viewScale: float, referenceSet: Tooling.CompDrawingBuilder.ReferenceSet, renderingStyle: Tooling.CompDrawingBuilder.RenderingStyleOption) -> None:
        ...
    def UpdateCompDrawing(self, drawing: NXObject, component: NXObject, componentPartName: str, drawingFileName: str, drawingName: str, templateName: str) -> None:
        ...
    def IgnoreComponents(self, component: NXObject) -> None:
        ...
    Component: Assemblies.SelectComponent
    ComponentType: Tooling.CompDrawingBuilder.ComponentTypeSelection
    DestinationFolder: str
    DoubleViewScale: float
    DrawingFileNamingRule: str
    DrawingFilter: Tooling.CompDrawingBuilder.DrawingType
    DrawingSheetNamingRule: str
    EnumReferenceSet: Tooling.CompDrawingBuilder.ReferenceSet
    EnumRenderingStyle: Tooling.CompDrawingBuilder.RenderingStyleOption
    Filter: Tooling.CompDrawingBuilder.FilterSelection
    IsKeepDrawingOpen: bool
    Margin: int
    MarginForView: float
    Projection: Tooling.CompDrawingBuilder.ProjectionType
    WizardType: int


    class RenderingStyleOption(enum.Enum):
        FullyShaded = 0
        PartiallyShaded = 1
        Wireframe = 2
        NoChange = 3
    

    class ReferenceSet(enum.Enum):
        Model = 0
        True = 1
        EntirePart = 2
        False = 3
        NoChange = 4
    

    class ProjectionType(enum.Enum):
        FirstAngleProjection = 0
        ThirdAngleProjection = 1
    

    class FilterSelection(enum.Enum):
        Type = 0
        Drawing = 1
        All = 2
    

    class DrawingType(enum.Enum):
        None = 0
        NonMaster = 1
        SelfContained = 2
    

    class ComponentTypeSelection(enum.Enum):
        All = 0
    

class ColorExpressionsBuilder(Builder):
    def __init__(self) -> None: ...
    def SetCurrentUDO(self, udo: UserDefinedObjects.UserDefinedObject) -> None:
        ...
    def DeleteCurrentUDO(self) -> None:
        ...
    def BlockCurrentUDO(self, blocked: bool) -> None:
        ...
    ColorName: str
    ColorPicker: NXColor
    SelectFaces: ScCollector


class ClonePart(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    IsClone: bool
    NewItemId: str
    NewItemType: str
    NewMfkId: str
    NewPartName: str
    NewRevisionId: str
    PartName: str


class CloneObject(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddAssembly(self, assemName: str) -> None:
        ...
    def AddAssembly(self, part: Part) -> None:
        ...
    def CreateClonePartItem(self, partName: str) -> Tooling.ClonePart:
        ...
    def Commit(self) -> str:
        ...
    def FindClonePartItem(self, partName: str) -> Tooling.ClonePart:
        ...
    def FindClonePartItemByIndex(self, index: int) -> Tooling.ClonePart:
        ...
    def AddAssociatedPart(self, clonedPartName: str, fileType: Tooling.ToolingCloneparttype) -> None:
        ...
    def SetNextNumber(self, nextNumber: int) -> None:
        ...
    def BuildClonePartItems(self, clonedPartItems: typing.List[Tooling.ClonePart]) -> None:
        ...
    def BuildAllClonePartItems(self) -> None:
        ...
    def BuildAllClonePartItems(self, newWorkPart: Part) -> None:
        ...
    def BuildAllConceptPartItems(self) -> None:
        ...
    def SaveCloneStartNumber(self) -> None:
        ...
    def SetProjectName(self, projName: str) -> None:
        ...
    def SetNameRule(self, nameRule: str) -> None:
        ...
    def SyncPartNumber(self) -> None:
        ...
    def RestorePartNumber(self) -> None:
        ...
    def SetKeepItemType(self, keepItemType: bool) -> None:
        ...
    def SetDefaultItemType(self, defaultItemType: str) -> None:
        ...
    def SetDefaultNameRule(self, nameRule: str) -> None:
        ...
    def SetUseMappingTemplate(self, bUseMappingTemplate: bool) -> None:
        ...
    def SetCurrentNameMappingTemplate(self, mappingTemplate: str) -> None:
        ...
    def SetEnableVersionControl(self, bVersionControl: bool) -> None:
        ...
    def AddDrawingPart(self, drawingPart: str, masterPart: str, bDefinedInMap: bool) -> None:
        ...
    def BuildDrawingRelations(self, partNames: str) -> None:
        ...
    def SetCheckSymbolName(self, checkSymbolName: bool) -> None:
        ...
    CloneMethod: Tooling.ToolingClonemethod
    OutputFolder: str


class ClearanceManagementCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ClearanceManagementBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateClearanceManagementBuilder(self) -> Tooling.ClearanceManagementBuilder:
        ...
    def Tag(self) -> Tag: ...



class ClearanceManagementBuilder(Builder):
    def __init__(self) -> None: ...
    def SetParameters(self, paraNames: str, paraValues: str) -> None:
        ...
    IsHighLightFacesWithSameClearance: bool
    PlateClearanceEighth: float
    PlateClearanceFifth: float
    PlateClearanceFirst: float
    PlateClearanceFourth: float
    PlateClearanceNinth: float
    PlateClearanceSecond: float
    PlateClearanceSeventh: float
    PlateClearanceSixth: float
    PlateClearanceTenth: float
    PlateClearanceThird: float
    SelectFace: ScCollector
    SelectPart: SelectBody
    ShowPartAndClearanceHoleOnly: bool
    SpecifyClearanceDataFile: str
    ToolPartOrTargetPart: Tooling.ClearanceManagementBuilder.Selection
    TypeAssignOrCheck: Tooling.ClearanceManagementBuilder.Type
    UsePlateClearanceEighth: bool
    UsePlateClearanceFifth: bool
    UsePlateClearanceFirst: bool
    UsePlateClearanceFourth: bool
    UsePlateClearanceNinth: bool
    UsePlateClearanceSecond: bool
    UsePlateClearanceSeventh: bool
    UsePlateClearanceSixth: bool
    UsePlateClearanceTenth: bool
    UsePlateClearanceThird: bool


    class Type(enum.Enum):
        AssignClearances = 0
        CheckClearances = 1
    

    class Selection(enum.Enum):
        ToolPart = 0
        TargetPart = 1
    

class ChannelFittingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ChannelFittingBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateChannelFittingBuilder(self) -> Tooling.ChannelFittingBuilder:
        ...
    def Tag(self) -> Tag: ...



class ChannelFittingBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateCoolingFittingData(self) -> Tooling.CoolingFittingData:
        ...
    def GetCoolingFittingData(self) -> Tooling.CoolingFittingData:
        ...
    def CreateFittingPoints(self) -> None:
        ...
    def SetCoolingNodeInfo(self) -> None:
        ...
    def SetExistingFittingPointDataDetails(self, fittingPts: typing.List[Point], channelDiameters: str, currentNames: str, currentTypes: str, currentFitTypes: str, baffleLengths: str, fittingPointModified: bool, partNumbersTc: str) -> None:
        ...
    def ProcessPoint(self, editPoint: Point, newWcsMtx: Matrix3x3) -> None:
        ...
    def SetChannelType(self, channelType: str) -> None:
        ...
    def CalculateManualBaffleLength(self, edit: bool, fittingPoint: Point) -> None:
        ...
    def AddInstance(self, coolingPart: Assemblies.Component, fittingPoint: Point) -> None:
        ...
    BottomClearance: Expression
    BoundaryBody: SelectBodyList
    CoolingStandardPart: SelectNXObject
    FittingPoint: Point
    ParentChannel: SelectBodyList
    SearchBoundaryBodies: bool
    TopClearance: Expression
    UseSymbol: bool


class ChannelAdjustCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.ChannelAdjustBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateChannelAdjustBuilder(self) -> Tooling.ChannelAdjustBuilder:
        ...
    def Tag(self) -> Tag: ...



class ChannelAdjustBuilder(Builder):
    def __init__(self) -> None: ...
    def SetManipulatorOriginValue(self, moveOrigin: Point3d) -> None:
        ...
    def SetModifyManipulatorOrigin(self, modified: bool) -> None:
        ...
    AdjustMethod: Tooling.ChannelAdjustBuilder.AdjustType
    AdjustVector: Direction
    AlongAxialDir: bool
    BaffleComponent: Assemblies.SelectComponentList
    BoundaryBody: SelectBodyList
    CopyOriginal: bool
    Diameter: Expression
    DiameterListValue: str
    Distance: Expression
    ReferenceFace: ScCollector
    RepositionMethod: Tooling.ChannelAdjustBuilder.VectorMethod
    TargetChannel: SelectBodyList


    class VectorMethod(enum.Enum):
        Along = 0
        Perpendicular = 1
    

    class MoveType(enum.Enum):
        MoveOriginal = 0
        CopyOriginal = 1
    

    class AdjustType(enum.Enum):
        Distance = 0
        BaffleLength = 1
        BaffleComponentLength = 2
        AdjustDiameter = 3
    

class ChangeoverManagementBuilder(Builder):
    def __init__(self) -> None: ...
    def UseArrangement(self) -> None:
        ...
    def RenameArrangement(self) -> None:
        ...
    def DeleteArrangement(self, removeComponents: bool) -> None:
        ...
    def AddToChangeover(self) -> None:
        ...
    def RemoveFromChangeover(self) -> None:
        ...
    AddComponentsExclusively: bool
    ChangeoverName: str
    ClonedProductName: str
    NewChangeoverName: str
    RenameComponent: bool
    SelectComponents: Assemblies.SelectComponentList
    SelectProduct: Assemblies.SelectComponent
    SelectedArrangementName: str
    Type: Tooling.ChangeoverManagementBuilder.Types


    class Types(enum.Enum):
        Create = 0
        Manage = 1
    

class ChamferingInsertBuilder(Builder):
    def __init__(self) -> None: ...
    def StandardInsert(self) -> None:
        ...
    def UpdateInsertPartData(self) -> None:
        ...
    def PreparePDWStandardClientData(self) -> None:
        ...
    def PostProcessPDWStandardClientData(self) -> TaggedObject:
        ...
    def GetParentNames(self) -> str:
        ...
    def SetParentNames(self, parentNames: str) -> None:
        ...
    def GetSelectedFaceOccurrences(self, selectedFaceOccurrences: typing.List[TaggedObject]) -> None:
        ...
    def SetSelectedFaceOccurrences(self, selectedFaceOccurrences: typing.List[TaggedObject]) -> None:
        ...
    BottomingPlateClearance: float
    BottomingPlateToggle: bool
    DiePlateClearance: float
    DiePlateToggle: bool
    FaceEdgeType: Tooling.ChamferingInsertBuilder.FaceEdgeTypeOption
    InsertInstanceTag: TaggedObject
    InsertType: Tooling.ChamferingInsertBuilder.InsertTypeOption
    ParentPartName: str
    ParentPartNode: Tooling.ChamferingInsertBuilder.ParentPartNodeOption
    PunchPlateClearance: float
    PunchPlateToggle: bool
    RenameComponent: bool
    SelectFace: ScCollector
    StripperPlateClearance: float
    StripperPlateToggle: bool
    WizardType: int


    class ParentPartNodeOption(enum.Enum):
        NoParent = 0
    

    class InsertTypeOption(enum.Enum):
        Up = 0
        Down = 1
        All = 2
    

    class FaceEdgeTypeOption(enum.Enum):
        StraightChamfer = 0
        InnerCircle = 1
        InnerProfile = 2
    

class CAMDataManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateBlendCurve3dBuilder(self) -> Tooling.BlendCurve3DBuilder:
        ...
    def CreateOffsetCurve3dBuilder(self) -> Tooling.OffsetCurve3DBuilder:
        """[Obsolete("Deprecated in NX10.0.0.   Please use Features.CurveFeatureCollection.CreateOffset3dCurveBuilder instead ")"""
        ...
    def Tag(self) -> Tag: ...



class CalculateAreaCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.CalculateAreaBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.CalculateAreaBuilder:
        ...
    def Tag(self) -> Tag: ...



class CalculateAreaBuilder(Builder):
    def __init__(self) -> None: ...
    AngularAccuracy: Expression
    ApproximationTolerance: Expression
    CreateSheet: bool
    DimTolerance: Expression
    PlaneDefine: NXObject
    SelectionTarget: SelectBodyList
    SheetMethod: Tooling.CalculateAreaBuilder.SheetMethodType
    ToggleSideArea: bool


    class SheetMethodType(enum.Enum):
        Curve = 0
        Mesh = 1
    

class CaeReuseLibrary(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
    def CreateReusableObject(self) -> Tooling.ReusableObject:
        ...
    def ExportBeamSectionToLibrary(self, reuseLibraryName: str, reusableObject: Tooling.ReusableObject) -> None:
        ...
    def ImportBeamSectionFromLibrary(self, reuseLibraryName: str) -> CAE.BeamSection:
        ...
    def UpdateDescription(self, descriptiveName: str, reuseLibraryName: str, previewImageFile: str) -> None:
        ...
    def Tag(self) -> Tag: ...



class BurringInsertCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.BurringInsertBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBurringInsertBuilder(self) -> Tooling.BurringInsertBuilder:
        ...
    def Tag(self) -> Tag: ...



class BurringInsertBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateNewComponent(self, parentTag: TaggedObject, origin: Point3d) -> TaggedObject:
        ...
    def RevolveSketchedCurve(self) -> None:
        ...
    def DeletePunchOrDieComponent(self) -> None:
        ...
    ArcRadius: Expression
    BlankProfile: Section
    BurringDirection: Tooling.BurringInsertBuilder.BurringDirections
    BurringPunchType: Tooling.BurringInsertBuilder.BurringPunchTypes
    CircularOrNonCircular: Tooling.BurringInsertBuilder.CircularOrNonCircularType
    DesignOption: Tooling.BurringInsertBuilder.DesignOptions
    EndValue: Expression
    ParentPart: Tooling.BurringInsertBuilder.ParentTypes
    ParentPartName: str
    PlateClearanceFirst: float
    PlateClearanceSecond: float
    PlateClearanceThird: float
    PunchHeadHeight: Expression
    PunchOrDieToEdit: SelectBody
    RenameComponent: bool
    SelectFaces: ScCollector
    StartValue: Expression
    UsePlateClearanceFirst: bool
    UsePlateClearanceSecond: bool
    UsePlateClearanceThird: bool


    class ParentTypes(enum.Enum):
        Control = 0
        DieBase = 1
        SubDie = 2
        Die = 3
    

    class DesignOptions(enum.Enum):
        BurringPunch = 0
        BurringDie = 1
    

    class CircularOrNonCircularType(enum.Enum):
        Circular = 0
        NonCircular = 1
    

    class BurringPunchTypes(enum.Enum):
        First = 0
        Second = 1
        Third = 2
    

    class BurringDirections(enum.Enum):
        BurringUpwards = 0
        BurringDownwards = 1
    

class BomListDataProvider(TaggedObject):
    def __init__(self) -> None: ...
    def SetString(self, rows: int, column: int, stringData: str) -> bool:
        ...
    def SetString(self, rows: int, column: int, stringData: str) -> bool:
        ...
    def GetString(self, row: int, column: int) -> str:
        ...
    def SetInteger(self, rows: int, column: int, integerData: int) -> bool:
        ...
    def SetInteger(self, rows: int, column: int, integerData: int) -> bool:
        ...
    def GetInteger(self, row: int, column: int, isUnassigned: bool) -> int:
        ...
    def SetDouble(self, rows: int, column: int, doubleData: float) -> bool:
        ...
    def SetDouble(self, rows: int, column: int, doubleData: float) -> bool:
        ...
    def GetDouble(self, row: int, column: int, isUnassigned: bool) -> float:
        ...
    def SetBoolean(self, rows: int, column: int, booleanData: bool) -> bool:
        ...
    def SetBoolean(self, rows: int, column: int, booleanData: bool) -> bool:
        ...
    def GetBoolean(self, row: int, column: int) -> bool:
        ...
    def UnsetValue(self, row: int, column: int) -> bool:
        ...
    def UnsetValue(self, rows: int, column: int) -> bool:
        ...
    def Destroy(self) -> None:
        ...
    ColumnCount: int
    RowCount: int


    class ExportedStatus(enum.Enum):
        Null = 0
        Partial = 1
        All = 2
    

class BomListBuilder(Builder):
    def __init__(self) -> None: ...
    def GetLastTemplateName(self) -> str:
        ...
    def SetLastTemplateName(self, lastTemplateName: str) -> None:
        ...
    def UpdateEwBlankAttributes(self) -> None:
        ...
    def ParseBomTemplate(self) -> None:
        ...
    def PopulateBomListData(self) -> None:
        ...
    def AddBomData(self, partOccs: typing.List[Assemblies.Component], dataStrings: str) -> None:
        ...
    def ShowComponents(self, rowID: int, partOccs: typing.List[Assemblies.Component]) -> None:
        ...
    def ShowRows(self, rowIDs: int) -> None:
        ...
    def IgnoreComponents(self, rowID: int, partOccs: typing.List[Assemblies.Component]) -> None:
        ...
    def IgnoreRows(self, rowIDs: int) -> None:
        ...
    def SortColumn(self, columnID: int, order: Tooling.BomListBuilder.BomListSortOption) -> None:
        ...
    def CreatePartsList(self, columnWidths: int, point: Point3d) -> DisplayableObject:
        ...
    def GetColumnLabel(self, columnID: int) -> str:
        ...
    def GetColumnAttribute(self, columnID: int) -> str:
        ...
    def GetPartOccs(self, rowID: int) -> typing.List[Assemblies.Component]:
        ...
    def GetRows(self, bomListType: Tooling.BomListBuilder.BomListTypes) -> int:
        """[Obsolete("Deprecated in NX11.0.0.  Use Tooling.BomListDataProvider.RowCount instead.")"""
        ...
    def GetAttributeStrings(self) -> str:
        """[Obsolete("Deprecated in NX11.0.0.  Use Tooling.BomListBuilder.GetColumnAttribute instead.")"""
        ...
    def GetColumn(self, attrString: str) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use Tooling.BomListBuilder.GetColumnAttribute instead.")"""
        ...
    def ModifyBomData(self, rowNumber: int, columnNumber: int, userString: str) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use Tooling.BomListDataProvider.SetString instead.")"""
        ...
    def StoreBomListData(self) -> None:
        ...
    def CheckBlankAttributes(self) -> None:
        ...
    BomListDataProvider: Tooling.BomListDataProvider
    BomListType: Tooling.BomListBuilder.BomListTypes
    BomTemplate: str
    SelectComponents: Assemblies.SelectComponentList
    SortingBasedOnModify: bool
    SortingMethod: bool


    class BomListTypes(enum.Enum):
        BomList = 0
        HideList = 1
    

    class BomListSortOption(enum.Enum):
        Unsorted = 0
        Ascending = 1
        Descending = 2
    

    class BomListDecimalDelimiter(enum.Enum):
        Dot = 0
        Comma = 1
    

class BlendCurve3DBuilder(Builder):
    def __init__(self) -> None: ...
    def SaveFilletCurves(self) -> None:
        ...
    def CreateBlendCurves(self) -> typing.List[Curve]:
        ...
    def DeleteBlendCurves(self, blendCurves: typing.List[Curve]) -> None:
        ...
    BlendCurveOption: Tooling.BlendCurve3DBuilder.BlendCurveOptions
    CornerFillet: ScCollector
    CurveBlend: ScCollector
    DistanceTolerance: float
    InputCurves: Tooling.BlendCurve3DBuilder.InputCurvesOption
    MinimalRadius: float
    ReferenceDirection: Direction
    ReverseSide: bool


    class InputCurvesOption(enum.Enum):
        Keep = 0
        Hide = 1
        Delete = 2
    

    class BlendCurveOptions(enum.Enum):
        BestFit = 0
        Variable = 1
        Vector = 2
        CurrentView = 3
    

class BlankNestingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.BlankNestingBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBlankNestingBuilder(self) -> Tooling.BlankNestingBuilder:
        ...
    def Tag(self) -> Tag: ...



class BlankNestingBuilder(Builder):
    def __init__(self) -> None: ...
    def LayoutCalculation(self) -> None:
        ...
    AngleResult: float
    AngleResultExp: Expression
    AngleStep: float
    AngleStepExp: Expression
    BlankArea: float
    BlankAreaExp: Expression
    BoundarySegment: int
    HeightStep: float
    IsReNest: bool
    LayoutType: Tooling.BlankNestingBuilder.LayoutTypeSpecification
    MinimumDistance: float
    MinimumDistanceExp: Expression
    PitchResult: float
    PitchResultExp: Expression
    SelectObject: ScCollector
    StripWidthResult: float
    StripWidthResultExp: Expression
    Utilization: float
    WebDistance: float
    WebDistanceExp: Expression


    class LayoutTypeSpecification(enum.Enum):
        Rectangle = 0
        Parallelogram = 1
        Trapezoid = 2
        OneUp = 3
        TwoUp = 4
        TwoPair = 5
    

class BlankLayoutCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.BlankLayoutBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBlankLayoutBuilder(self) -> Tooling.BlankLayoutBuilder:
        ...
    def Tag(self) -> Tag: ...



class BlankLayoutBuilder(Builder):
    def __init__(self) -> None: ...
    def RepositionBottom(self) -> None:
        ...
    def RepositionLeftDistance(self) -> None:
        ...
    def RepositionLeftRightSide(self) -> None:
        ...
    def RepositionPitch(self) -> None:
        ...
    def RepositionRightDistance(self) -> None:
        ...
    def RepositionRotate(self) -> None:
        ...
    def RepositionSideWeb(self) -> None:
        ...
    def RepositionTop(self) -> None:
        ...
    def RepositionWidth(self) -> None:
        ...
    def RepositionShiftX(self) -> None:
        ...
    def RepositionShiftY(self) -> None:
        ...
    def UpdateBlankLayout(self) -> None:
        ...
    def SetBoundingBox(self) -> None:
        ...
    def SetItemValue(self) -> None:
        ...
    def SetMaterialUtilization(self) -> None:
        ...
    def InsertBlank(self, blankName: str) -> None:
        ...
    BasePoint: Point
    Blank: SelectBody
    BlankNameStr: str
    Bottom: float
    LeftDistance: float
    LeftRightSide: Tooling.BlankLayoutBuilder.LeftRightSideOption
    LockPitch: bool
    LockPitchAndWidth: bool
    LockRotate: bool
    LockShiftX: bool
    LockShiftY: bool
    LockWidth: bool
    MaterialUtilization: str
    MinimumSpaceSize: bool
    MinimumSpaceSizeValue: str
    Pitch: float
    RightDistance: float
    Rotate: float
    SideWeb: Tooling.BlankLayoutBuilder.SideWebOption
    SnapSize: Tooling.BlankLayoutBuilder.SnapSizeOption
    ThreeBlanks: bool
    Top: float
    Type: Tooling.BlankLayoutBuilder.Types
    Width: float
    XShift: float
    YShift: float


    class Types(enum.Enum):
        CreateLayout = 0
        AddBlank = 1
        CopyBlank = 2
        RemoveBlank = 3
        SetBasePoint = 4
        FlipBlank = 5
    

    class SnapSizeOption(enum.Enum):
        Tenth = 0
        Fifth = 1
        Half = 2
        One = 3
        Two = 4
        Five = 5
        Ten = 6
    

    class SideWebOption(enum.Enum):
        Average = 0
        Bottom = 1
        Top = 2
    

    class LeftRightSideOption(enum.Enum):
        Average = 0
        Left = 1
        Right = 2
    

class BlankGeneratorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.BlankGeneratorBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBlankGeneratorBuilder(self) -> Tooling.BlankGeneratorBuilder:
        ...
    def Tag(self) -> Tag: ...



class BlankGeneratorBuilder(Builder):
    def __init__(self) -> None: ...
    def ImportBlank(self) -> None:
        ...
    def ImportBlankPart(self, blankFullName: str) -> NXObject:
        ...
    def SelectBlank(self) -> None:
        ...
    def UnformSheet(self) -> None:
        ...
    def UpdateBlank(self) -> None:
        ...
    def UpdateBlankPart(self, blankFullName: str) -> NXObject:
        ...
    def RemoveBlank(self) -> None:
        ...
    BlankNumber: str
    BlankPart: TaggedObject
    CreateBlankOption: Tooling.BlankGeneratorBuilder.CreateBlankType
    CreatedByInsert: bool
    DatumFace: SelectFace
    DisplayPartImport: TaggedObject
    DisplayPartSelect: TaggedObject
    EditBlankOption: Tooling.BlankGeneratorBuilder.EditBlankType
    InsertNewBlank: TaggedObject
    SheetMetalPartName: str
    StationaryFace: SelectFace
    Type: Tooling.BlankGeneratorBuilder.Types
    WorkPart: TaggedObject


    class Types(enum.Enum):
        CreateBlank = 0
        EditBlank = 1
    

    class EditBlankType(enum.Enum):
        Update = 0
        Remove = 1
    

    class CreateBlankType(enum.Enum):
        Import = 0
        Select = 1
        Unform = 2
    

class BendOperationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.BendOperationBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBendOperationBuilder(self) -> Tooling.BendOperationBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Tooling.BendOperationBuilder:
        ...
    def Tag(self) -> Tag: ...



class BendOperationBuilder(Builder):
    def __init__(self) -> None: ...
    AlternateResult: bool
    BaseBody: Body
    BendAngle1: float
    BendAngle2: float
    BendAngle3: float
    BendAngle4: float
    BendAngle5: float
    BendDevLength: float
    BendNeutralFactor: float
    BendNumPrebends: Tooling.BendOperationBuilder.Prebend
    DefineNeutralFactor: Tooling.DefineNeutralFactorBuilder
    FixTabFlangePosition: bool
    KeepRadiusFixed: bool
    OverbendAngle: float
    OverbendOption: Tooling.BendOperationBuilder.OverbendOptions
    OverbendRadius: float
    ReferObject: SelectEdgeList
    ResizeRadius: bool
    RestorePosition: bool
    SelectedBend: SelectFaceList
    Type: Tooling.BendOperationBuilder.Types
    WorkPart: Assemblies.SelectComponent


    class Types(enum.Enum):
        Unbend = 0
        Rebend = 1
        Prebend = 2
        Overbend = 3
    

    class Prebend(enum.Enum):
        Two = 0
        Three = 1
        Four = 2
        Five = 3
        Six = 4
    

    class OverbendOptions(enum.Enum):
        ResizeBendAngle = 0
        ResizeBendRadius = 1
    

class BendInsertDesignCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.BendInsertDesignBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBendInsertDesignBuilder(self) -> Tooling.BendInsertDesignBuilder:
        ...
    def Tag(self) -> Tag: ...



class BendInsertDesignBuilder(Builder):
    def __init__(self) -> None: ...
    def SetFaces(self, faceOccs: typing.List[Face]) -> None:
        ...
    def AddInsertComponent(self) -> None:
        ...
    BendFace: ScCollector
    BendType: Tooling.BendInsertDesignBuilder.BendTypeOption
    BendingDirection: Tooling.BendInsertDesignBuilder.BendingDirectionOption
    BlankPosition: Tooling.BendInsertDesignBuilder.BlankPositions
    BottomPlateClearance: float
    CompositeInsert: bool
    ConceptDesign: bool
    DiePlateClearance: float
    Extend: Expression
    ExtrudeEnd: Expression
    ExtrudeEnd1: Expression
    ExtrudeSketch: Section
    ExtrudeStart: Expression
    ExtrudeStart1: Expression
    ExtrudeTolerance: float
    FalseBody: bool
    FlipTrimDirection: bool
    InsertComponent: Assemblies.SelectComponentList
    InsertToEdit: Assemblies.SelectComponentList
    InsertType: Tooling.BendInsertDesignBuilder.InsertTypeOption
    IntersectPlane: Plane
    IsAutoDatum: bool
    NewPartName: str
    ParentNode: Tooling.BendInsertDesignBuilder.ParentOption
    ParentPartName: str
    PunchPlateClearance: float
    ReName: bool
    StripperPlateClearance: float
    Type: Tooling.BendInsertDesignBuilder.Types
    UseBottomPlateClearance: bool
    UseDiePlateClearance: bool
    UsePunchPlateClearance: bool
    UseStripperPlateClearance: bool


    class Types(enum.Enum):
        Standard = 0
        UserDefined = 1
        Delete = 2
    

    class ParentOption(enum.Enum):
        Sub = 0
    

    class InsertTypeOption(enum.Enum):
        Punch = 0
        Die = 1
    

    class BlankPositions(enum.Enum):
        PunchPlate = 0
        StripperPlate = 1
    

    class BendTypeOption(enum.Enum):
        Sbend = 0
        Abend = 1
        Zbend = 2
        Vbend = 3
        Uzbend = 4
    

    class BendingDirectionOption(enum.Enum):
        Up = 0
        Down = 1
    

class BendingAreaData(Tooling.CostDataObject):
    def __init__(self) -> None: ...


class BackingPadBuilder(Builder):
    def __init__(self) -> None: ...
    def WaveFaces(self) -> None:
        ...
    def DeleteWavedFaces(self) -> None:
        ...
    OffsetValueLinearDimension: Expression
    OffsetValueLinearDimensionNegativeX: Expression
    OffsetValueLinearDimensionNegativeY: Expression
    OffsetValueLinearDimensionPositiveX: Expression
    OffsetValueLinearDimensionPositiveY: Expression
    PadBoolean: GeometricUtilities.BooleanOperation
    PadHeightLinearDimension: Expression
    PreviousWorkPart: Part
    SelectComponent: Assemblies.SelectComponent
    SelectCurve: Section
    SelectFaces: SelectFaceList
    SelectPad: Features.SelectFeatureList
    Type: Tooling.BackingPadBuilder.Types


    class Types(enum.Enum):
        KfBoundBox = 0
        UserDefined = 1
        DeletePad = 2
    

class AutoDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateOrdinateOrigin(self, viewTag: NXObject, pointData: Point3d) -> NXObject:
        ...
    def CreateOrdinateOriginMargins(self, ordinateOrigin: NXObject, viewTag: NXObject) -> None:
        ...
    def CycleObjectsInView(self, viewTag: NXObject, vseqNumber: int, isDrawing: bool, inObject: NXObject) -> NXObject:
        ...
    CreateXDimensions: bool
    CreateYDimensions: bool
    CreatedOrdinateOrigin: NXObject
    DimensionCharacterSize: float
    DimensionColor: NXColor
    Dimensions: Annotations.SelectOrdinateDimensionList
    FirstMargin: NXObject
    FourthMargin: NXObject
    InnerDimensionOffsetValue: float
    MaxDistanceToOuterMargin: float
    ObjectToDimension: SelectNXObjectList
    OffsetValueForMargin: float
    OrdinateDimensionStyle: Annotations.StyleBuilder
    OrdinateView: NXObject
    OriginPoint: SelectNXObject
    SecondMargin: NXObject
    SelectHolesAutomatically: bool
    TextAngle: float
    TextFont: Tooling.AutoDimensionBuilder.TextFontType
    TextOrientation: Tooling.AutoDimensionBuilder.TextOrientationType
    ThirdMargin: NXObject
    Tolerance: Tooling.AutoDimensionBuilder.ToleranceType
    ToleranceCharacterSize: float
    ToleranceColor: NXColor
    ToleranceLowerValue: float
    ToleranceUpperValue: float
    ToleranceValue: float
    Type: Tooling.AutoDimensionBuilder.MainType
    ValuePrecision: Tooling.AutoDimensionBuilder.ValuePrecisionType


    class ValuePrecisionType(enum.Enum):
        NominalMinusX = 0
        NominalMinusXDotx = 1
        NominalMinusXDotxx = 2
        NominalMinusXDotxxx = 3
        NominalMinusXDotxxxx = 4
        NominalMinusXDotxxxxx = 5
        NominalMinusXDotxxxxxx = 6
    

    class ToleranceType(enum.Enum):
        NoTolerance = 0
        EqualBilateralTolerance = 1
        BilateralTolerance = 2
        UnilateralPlus = 3
        UnilateralMinus = 4
    

    class TextOrientationType(enum.Enum):
        Horizontal = 0
        Aligned = 1
        TextOverDimensionLine = 2
        TextAtAngle = 3
        Perpendicular = 4
    

    class TextFontType(enum.Enum):
        First = 0
        Second = 1
        Third = 2
        Fourth = 3
        Fifth = 4
    

    class MainType(enum.Enum):
        CreateOrdinateDimension = 0
        EditOrdinateDimension = 1
    

class AutoDieGroup(TaggedObject):
    def __init__(self) -> None: ...


class AutoDieCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.AutoDieGroup]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDieDesDrawPunchBuilder(self, featureSet: Features.Feature) -> Tooling.DieDesDrawPunchBuilder:
        ...
    def CreateDieDesDrawDieBuilder(self, featureSet: Features.Feature) -> Tooling.DieDesDrawDieBuilder:
        ...
    def CreateDieEngFormTaskBuilder(self, dieEngFormTask: Features.Feature) -> Tooling.DieEngFormTaskBuilder:
        ...
    def CreateDieDesPierceInsertBuilder(self) -> Tooling.DieDesPierceInsertBuilder:
        ...
    def CreateDieEngTrimAngleCheckBuilder(self, dieEngTrimAngleCheck: GeometricAnalysis.AnalysisObject) -> Tooling.DieEngTrimAngleCheckBuilder:
        ...
    def CreateLsdynaGeometryPreparationBuilder(self) -> Tooling.LsdynaGeometryPreparationBuilder:
        ...
    def CreateLsdynaKfileGeneratorBuilder(self) -> Tooling.LsdynaKfileGeneratorBuilder:
        ...
    def CreateLsdynaFormAnalysisResultDisplayBuilder(self) -> Tooling.LsdynaFormAnalysisResultDisplayBuilder:
        ...
    def CreateDieDesignLowerBinderBuilder(self, frec: Features.Feature) -> Tooling.DieDesignLowerBinderBuilder:
        ...
    def CreateDieDesignTrimPostBuilder(self, frec: Features.Feature) -> Tooling.DieDesignTrimPostBuilder:
        ...
    def CreateDieEngStampingCarryoverBuilder(self, dieEngStampingCarryover: Features.BodyFeature) -> Tooling.DieEngStampingCarryoverBuilder:
        ...
    def CreateDieEngStampingOutputBuilder(self, frec: Features.BodyFeature) -> Tooling.DieEngStampingOutputBuilder:
        ...
    def CreateDieEngTrimTaskBuilder(self, frec: Features.BodyFeature) -> Tooling.DieEngTrimTaskBuilder:
        ...
    def CreateDieEngProcessUpdateManagerBuilder(self, frec: Features.BodyFeature) -> Tooling.DieEngProcessUpdateManagerBuilder:
        ...
    def CreateSetPressModelBuilder(self) -> Tooling.SetPressModelBuilder:
        ...
    def CreateSpindleSliderBuilder(self) -> Tooling.SpindleSliderBuilder:
        ...
    def CreateDieEngDieTipBuilder(self, frec: Features.Feature) -> Tooling.DieEngDieTipBuilder:
        ...
    def CreateDieEngLineUpBuilder(self, frec: Features.BodyFeature) -> Tooling.DieEngLineupBuilder:
        ...
    def CreateDieEngDefineProductOrientationBuilder(self, featureSet: Features.Feature) -> Tooling.DieEngDefineProductOrientationBuilder:
        ...
    def Tag(self) -> Tag: ...



class AssignPatchCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.AssignPatchBuilder]:
        ...
    def __init__(self, owner: Tooling.ToolingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.AssignPatchBuilder:
        ...
    def CreateBuilderByPartingOrPatchType(self) -> Tooling.AssignPatchBuilder:
        ...
    def Tag(self) -> Tag: ...



class AssignPatchBuilder(Builder):
    def __init__(self) -> None: ...
    def GetPatchColor(self, redValue: float, greenValue: float, blueValue: float) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use Tooling.AssignPatchBuilder.PatchColor instead.")"""
        ...
    def SetPatchColor(self, redValue: float, greenValue: float, blueValue: float) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use Tooling.AssignPatchBuilder.PatchColor instead.")"""
        ...
    def AddSelectFace(self, addFace: Body) -> None:
        ...
    def InitOnEnter(self) -> None:
        ...
    def UpdateInitialCandidates(self) -> None:
        ...
    def PrepareAllRemovingSheets(self, sheets: typing.List[Body]) -> None:
        ...
    def ClearAddingCandidates(self) -> None:
        ...
    ConvertType: Tooling.AssignPatchBuilder.ConvertTypeOption
    KeepSheet: bool
    PartingColor: NXColor
    PatchColor: NXColor
    PatchSurfaces: SelectBodyList
    Type: Tooling.AssignPatchBuilder.Types


    class Types(enum.Enum):
        PatchSurface = 0
        PartingSurface = 1
    

    class ConvertTypeOption(enum.Enum):
        WithCopies = 0
        NoCopies = 1
    

class AssemblyDrawingBuilder(Builder):
    def __init__(self) -> None: ...
    def NewMasterModelFile(self, masterModelFileName: str) -> None:
        ...
    def OpenMasterModelFile(self, masterModelFileName: str) -> None:
        ...
    def DeleteSheet(self, selectedSheetName: str) -> None:
        ...
    def AddSectionView(self) -> None:
        ...
    def AddView(self, viewTag: NXObject, attrName: str, componentType: str) -> None:
        ...
    def RetrieveSheet(self, selectedSheetName: str) -> None:
        ...
    def CreateDrawing(self, sheetName: str, templateName: str) -> None:
        ...
    def EditDrawing(self, sheetName: str, templateName: str) -> None:
        ...
    def AssignAttr(self, selectdObjs: typing.List[NXObject], attrName: str, attrValue: str) -> None:
        ...
    def CreateView(self, viewName: str, viewScale: float) -> None:
        ...
    def DeleteView(self, viewName: str) -> None:
        ...
    def CreateSectionView(self, viewName: str, parentView: NXObject, stepDirection: float, arrowdirection: float, pointX: float, pointY: float, pointZ: float, segmentType: int, attrName: str, attrValueList: str) -> None:
        ...
    def CreateViewToShowComponents(self, viewName: str) -> NXObject:
        ...
    def UpdateEventForShowOnlyTrue(self, attributeNames: str, attributeValues: str, allComps: typing.List[NXObject]) -> None:
        ...
    def UpdateEventForShowOnly(self, attributeNames: str, attributeValues: str, allComps: typing.List[NXObject]) -> None:
        ...
    def UpdateEventForBlankComponetsWithAttributes(self, attributeNames: str, attributeValues: str, allComps: typing.List[NXObject]) -> None:
        ...
    def UnhighlightOccOfSelectedPartOccs(self, attributeNames: str, attributeValues: str, indexAttributeName: int, indexAttributeValue: int, partOccTag: NXObject, unhighlight: bool) -> None:
        ...
    def UseArrangement(self) -> None:
        ...
    def PopulateBomListData(self) -> None:
        ...
    def CreateDrawing(self, sheetName: str, templateName: str, sheetsNumber: int) -> None:
        ...
    def CreatePartsList(self, columnWidths: int, point: Point3d) -> DisplayableObject:
        ...
    BomListDataProvider: Tooling.BomListDataProvider
    BomTemplate: str
    DeleteButtonClicked: bool
    DoubleViewScale: float
    EnumAttributeName: Tooling.AssemblyDrawingBuilder.AttributeNames
    EnumAttributeValue: Tooling.AssemblyDrawingBuilder.AttributeValues
    EnumDrawingType: Tooling.AssemblyDrawingBuilder.DrawingTypes
    EnumSheets: Tooling.AssemblyDrawingBuilder.DrawingCreateOrEdit
    ModelViewToUse: Tooling.AssemblyDrawingBuilder.ModelViewToUseValue
    NewArrangementName: str
    ScaleModified: bool
    SectionViewButtonClicked: bool
    SelectedArrangementName: str
    SheetsNumber: Tooling.AssemblyDrawingBuilder.SheetsNum
    StringFilterRule: str
    StringNameRule: str
    StringSheetName: str
    TgShowA: bool
    TgShowB: bool
    TgShowC: bool
    ToggleBlankComponentsWithAttribute: bool
    ToggleCreateFourSheets: bool
    ToggleListDependents: bool
    ToggleShowOnly: bool
    Type: Tooling.AssemblyDrawingBuilder.Types
    ViewLocation: Point
    ViewOption: Tooling.AssemblyDrawingBuilder.ViewOptionValue
    ViewScale: float
    WizardType: int


    class ViewOptionValue(enum.Enum):
        DefaultView = 0
        BaseViewTool = 1
    

    class Types(enum.Enum):
        Visibility = 0
        Drawing = 1
        View = 2
    

    class SheetsNum(enum.Enum):
        One = 0
        Two = 1
        Three = 2
        Four = 3
    

    class ModelViewToUseValue(enum.Enum):
        Top = 0
        Front = 1
        Right = 2
        Back = 3
        Bottom = 4
        Left = 5
        Isometric = 6
        Trimetric = 7
    

    class DrawingTypes(enum.Enum):
        MasterModel = 0
        SelfContained = 1
    

    class DrawingCreateOrEdit(enum.Enum):
        CreateNew = 0
        Sh1 = 1
    

    class BomListTypes(enum.Enum):
        BomList = 0
        HideList = 1
    

    class BomListSortOption(enum.Enum):
        Unsorted = 0
        Ascending = 1
        Descending = 2
    

    class AttributeValues(enum.Enum):
        A = 0
        B = 1
        Hide = 2
    

    class AttributeNames(enum.Enum):
        MwSide = 0
        MwComponentName = 1
    

class AddReusablePartCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Tooling.AddReusablePart]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Tooling.AddReusablePart:
        ...
    def Tag(self) -> Tag: ...



class AddReusablePart(Builder):
    def __init__(self) -> None: ...
    def CreateCloneObject(self, applicationType: Tooling.ToolingApplication, assemName: str) -> Tooling.CloneObject:
        ...
    def GetInitialPosition(self) -> Point3d:
        ...
    def SetInitialPosition(self, dropLocation: Point3d) -> None:
        ...
    def GetSpreadsheetData(self) -> Tooling.SpreadsheetData:
        ...
    def SetSpreadsheetData(self, spreadsheetData: Tooling.SpreadsheetData) -> None:
        ...
    def GetParentPart(self) -> Part:
        ...
    def SetParentPart(self, part: Part) -> None:
        ...
    def GetAttachedGeometry(self) -> NXObject:
        ...
    def SetAttachedGeometry(self, part: NXObject) -> None:
        ...
    def SaveLibraryPath(self, libName: str, libpath: str) -> None:
        ...
    def LoadReusableComponent(self, krxFile: str) -> None:
        ...
    def SetComponentProperties(self, referenceSetName: str, componentName: str, layer: int) -> None:
        ...
    def UpdateReusableComponent(self) -> None:
        ...
    def UpdatePartData(self) -> None:
        ...
    def ConstructParametersData(self) -> None:
        ...
    def AffirmReusableComponent(self) -> None:
        ...
    def CreateReusableConstraints(self, index: int) -> None:
        ...
    def DeleteReusableConstraints(self) -> None:
        ...
    def ReverseComponentDirection(self, inputPosition: Point3d, inputDirection: Point3d, length: float, outputPosition: Point3d, outputDirection: Point3d) -> NXObject:
        ...
    def CreateReusablePocket(self, commit: bool) -> None:
        ...
    def DeleteReusablePocket(self) -> None:
        ...
    def CreateComponents(self, count: int, selobj: NXObject) -> None:
        ...
    def DeleteComponents(self, count: int) -> None:
        ...
    def AddHoleInstance(self, inputDirection: Point3d, inputPostion: Point3d) -> None:
        ...
    def AddHoleInstanceForCsys(self, inputDirection: Point3d, inputPostion: Point3d, selCsys: NXObject) -> None:
        ...
    def ReversePreviewComponent(self, rememberDir: Point3d) -> None:
        ...
    def RemoveOldInstance(self, index: int) -> None:
        ...
    def AddNewInstance(self, partOcc: Assemblies.Component, index: int) -> None:
        ...
    def EditReusableComponent(self, partOcc: Assemblies.Component) -> None:
        ...
    def AddPartOccurance(self, partOcc: Assemblies.Component) -> None:
        ...
    def AddComponentProperty(self, compName: str, refsetName: str, layer: int) -> None:
        ...
    def InsertReusableComponent(self, instIndex: int, needTransform: bool) -> None:
        ...
    def AddComponentMode(self, modeMethod: Tooling.AddReusablePart.ModeMethod) -> None:
        ...
    def SetCloneObject(self, cloneObject: Tooling.CloneObject) -> None:
        ...
    def GetCloneObject(self) -> Tooling.CloneObject:
        ...
    def AddClonePartName(self, clonedpartname: str) -> None:
        ...
    def SubtituteReusableComponent(self, substituteInstance: bool) -> None:
        ...
    def RemoveDesignElement(self) -> None:
        ...
    def MoveReusableComponent(self, translation: Vector3d, rotation: Matrix3x3, index: int) -> None:
        ...
    def RemoveReusableComponent(self, index: int) -> None:
        ...
    def SetSearchGeometry(self, isTrunOn: bool) -> None:
        ...
    def DestroyReusableBuilder(self) -> None:
        ...
    def RecordReusableComponent(self, fileName: str) -> None:
        ...
    def UpdateReusablePocket(self) -> None:
        ...
    def GetDesignElement(self) -> typing.List[Assemblies.Component]:
        ...
    def SetReusablePocketBuilder(self, pocketTag: Tooling.ReusablePocketBuilder) -> None:
        ...
    def GetReusablePocketBuilder(self) -> Tooling.ReusablePocketBuilder:
        ...
    def SetEnablePreview(self, isTrunOn: bool) -> None:
        ...
    def SetReplaceTemplate(self, replaceTemplate: Part) -> None:
        ...
    def SetComponentToReplace(self, index: int, replaceComponent: Assemblies.Component) -> None:
        ...
    def ReplaceReusableComponent(self) -> None:
        ...
    def RemoveFamilyInstance(self, part: Part) -> None:
        ...
    def CreatePatternComponent(self, createPattern: bool) -> None:
        ...
    def FindPositioningFeatureSet(self) -> Features.Feature:
        ...
    def SetComponentHandleToPoint(self) -> None:
        ...
    def UpdateCadenasParameter(self, paraName: str, paraValue: str) -> None:
        ...
    def ModifyParametersByRow(self, index: int) -> None:
        ...
    def AddCriteriaToInstance(self, hasCriteria: bool, expStr: str, addValue: str) -> None:
        ...
    def UpdatePocketBody(self, createPattern: bool, updatePocketBody: Tooling.AddReusablePart.PocketBodyMethod) -> None:
        ...
    def CreatePositioningFeatureOnPoint(self, selobj: NXObject, inputPosition: Point3d, centerFace: bool) -> None:
        ...
    def SavePositioningOriginPlacement(self, positionOffSet: str, placementOriginIndex: int) -> None:
        ...
    def UpdatePositioningOffset(self, positionOffSet: str) -> None:
        ...
    def SetUpdateComponentName(self, updateComponentName: bool) -> None:
        ...
    def UpdateParametersByConfiguration(self) -> None:
        ...
    def CreatePositioningFeatureByPoint(self, selobj: NXObject, inputPosition: Point3d, centerFace: bool) -> None:
        ...
    def DeleteReusableCompIdentity(self, partOcc: Assemblies.Component) -> None:
        ...
    def AffirmReusableComponents(self) -> typing.List[Assemblies.Component]:
        ...
    def UpdateTemplateInfo(self, replacementPartTag: Part, replacedPartOcc: Assemblies.Component) -> None:
        ...
    def SetWaveLink(self) -> None:
        ...
    def RenamePart(self, partName: str) -> None:
        ...
    def SetStructureDesignerPart(self, isStructureDesigner: bool) -> None:
        ...
    def ReverseDirection(self) -> None:
        ...
    def AssignStructureDesignerAttributes(self) -> None:
        ...
    def UpdateToolingSymbolicThread(self) -> None:
        ...
    def UndelayComponentToUpdate(self, obj: Part) -> None:
        ...
    def DelayComponents(self, objs: typing.List[TaggedObject]) -> None:
        ...
    ComponentPatternBuilder: Assemblies.ComponentPatternBuilder
    ComponentType: Tooling.AddReusablePart.ComponentMode
    PositionMode: Tooling.AddReusablePart.PositionMethod
    PositioningFeature: Sketch


    class PositionMethod(enum.Enum):
        Invalid = -1
        Absolute = 0
        Mate = 1
        Reposition = 2
        Wcs = 3
        Position = 4
        Point = 15
        InferredOny = 16
        Routing = 17
    

    class PocketBodyMethod(enum.Enum):
        None = 1
        Update = 2
        Delete = 3
    

    class ModeMethod(enum.Enum):
        Add = 1
        Edit = 2
    

    class ComponentMode(enum.Enum):
        Normal = 1
        Cadenas = 3
    

class AddCommentBuilder(Builder):
    def __init__(self) -> None: ...
    CommentString: str
    CompletionPercentage: int


