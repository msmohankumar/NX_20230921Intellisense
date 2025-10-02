from ...NXOpen import *
from ..Validate import *

import typing
import enum

class XmlComparator(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CompareXmlFiles(self, workXmlFile: str, masterXmlFile: str, compareOptions: Validate.XmlComparator.Options) -> Validate.XmlComparator.Result:
        ...
    def Tag(self) -> Tag: ...



    class Result(enum.Enum):
        Identical = 0
        Different = 1
    

    class XmlComparatorOptions():
        FilterFile: str
        ReportFile: str
        LogFile: str
        IgnoreNamespaces: bool
        IgnoreUnmatchedNodes: bool
        IgnoreComments: bool
        IgnoreCdata: bool
        IgnorePI: bool
        def ToString(self) -> str:
            ...
    

    class XmlComparator_Options():
        filterFile: int
        reportFile: int
        logFile: int
        ignoreNamespaces: bool
        ignoreUnmatchedNodes: bool
        ignoreComments: bool
        ignoreCdata: bool
        ignorePI: bool
    

class ValidatorOptions(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AutoDisplayResults: Validate.ValidatorOptions.ResultsDisplayModeTypes
    ExcludeNonOwnerParts: bool
    ExcludeReadonlyParts: bool
    GenerateCheckFlag: bool
    GenerateLogFile: bool
    LogFileDirectory: str
    LogFileMode: Validate.ValidatorOptions.LogModeTypes
    ResultsAutoUpdate: bool
    SavePartFile: Validate.ValidatorOptions.SaveModeTypes
    SaveResultInPart: bool
    SaveResultInTeamcenter: Validate.ValidatorOptions.SaveModeTypes
    SkipChecking: bool
    SkipCheckingDontLoadPart: bool
    SkipOverriddenResultOption: bool
    StopOnError: bool
    StopOnWarning: bool
    TreatWarningAsFail: bool


    class SaveModeTypes(enum.Enum):
        DoNotSave = 0
        SaveIfPassed = 1
        AlwaysSave = 2
    

    class ResultsDisplayModeTypes(enum.Enum):
        AlwaysDisplay = 0
        DisplayIfNotPass = 1
        DoNotDisplay = 2
    

    class LogModeTypes(enum.Enum):
        LogPerSession = 0
        LogPerPart = 1
    

class Validator(TaggedObject):
    def __init__(self) -> None: ...
    def Commit(self) -> Validation.Result:
        ...
    def GetLastErrorListFromCommit(self) -> ErrorList:
        ...
    def AppendPartNode(self, fileName: str) -> None:
        ...
    def AppendPartNode(self, partObject: Part) -> None:
        ...
    def AppendPartNodes(self, fileNames: str) -> None:
        ...
    def AppendPartNodes(self, partObject: typing.List[Part]) -> None:
        ...
    def ErasePartNode(self, index: int) -> None:
        ...
    def ClearPartNodes(self) -> None:
        ...
    def FindPartNode(self, index: int) -> Validate.PartNode:
        ...
    def GetPartNodes(self, partNodes: typing.List[Validate.PartNode]) -> None:
        ...
    def AppendCheckerNode(self, className: str) -> None:
        ...
    def AppendCheckerNodes(self, classNames: str) -> None:
        ...
    def EraseCheckerNode(self, delNdx: int) -> None:
        ...
    def ClearCheckerNodes(self) -> None:
        ...
    def FindCheckerNode(self, index: int) -> Validate.CheckerNode:
        ...
    def GetCheckerNodes(self, checkerNode: typing.List[Validate.CheckerNode]) -> None:
        ...
    ValidatorOptions: Validate.ValidatorOptions


class ValidationManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateValidator(self, name: str) -> Validate.Validator:
        ...
    def CreateParser(self, name: str) -> Validate.Parser:
        ...
    def FindValidator(self, name: str, validators: typing.List[Validate.Validator]) -> None:
        ...
    def DeleteValidator(self, validator: Validate.Validator) -> None:
        ...
    def DeleteParser(self, parser: Validate.Parser) -> None:
        ...
    def FindParser(self, name: str, parsers: typing.List[Validate.Parser]) -> None:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: int, options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: int, options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: bool, options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: bool, options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: float, options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: float, options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: str, options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: str, options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: Point3d, options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: typing.List[Point3d], options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: Vector3d, options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineParameter(self, parameterID: str, parameterValue: typing.List[Vector3d], options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineNXObjectParameter(self, parameterID: str, parameterValue: NXObject, options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def DefineNXObjectParameters(self, parameterID: str, parameterValue: typing.List[NXObject], options: Validate.ValidationManager.ParameterOptions) -> Validate.Parameter:
        ...
    def CreateCheckerDefinition(self, classID: str, displayName: str, category: str, parameters: typing.List[Validate.Parameter], doCheck: Validate.ValidationManager.DoCheckHandler) -> Validate.CheckerDefinition:
        ...
    def DeleteCheckerDefinition(self, checkerDefinition: Validate.CheckerDefinition) -> None:
        ...
    def Tag(self) -> Tag: ...



    class ValidationManagerParameterOptions():
        Label: str
        Group: str
        Modifiable: bool
        def ToString(self) -> str:
            ...
        def __init__(self, Label: str, Group: str, Modifiable: bool) -> None: ...
    

    

    

    class ValidationManager_ParameterOptions():
        label: int
        group: int
        modifiable: bool
    

    

class SelectionAndPlacementBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetTargets(self) -> typing.List[TaggedObject]:
        ...
    def SetTargets(self, targets: typing.List[TaggedObject]) -> None:
        ...
    def Validate(self) -> bool:
        ...
    DrawOrientation: Matrix3x3
    DrawOrigin: Point3d


class ResultObject(NXObject):
    def __init__(self) -> None: ...
    def CreateOverrideBuilder(self, overrideRequest: Validate.Override) -> Validate.OverrideBuilder:
        ...
    def DeleteOverride(self) -> None:
        ...
    def AskAttribute(self, name: str) -> NXObject.AttributeInformation:
        ...
    def AskAttributes(self, name: str, attributes: typing.List[NXObject.AttributeInformation]) -> None:
        ...
    CategoryName: str
    ClassName: str
    Disabled: bool
    Object: NXObject
    OutOfDate: bool
    Override: Validate.Override
    Status: Validation.Result
    TotalObjectsCount: int
    Type: Validate.ResultObject.ResultTypes


    class ResultTypes(enum.Enum):
        Part = 0
        Profile = 1
        Test = 2
        Object = 3
        ObjectSet = 4
    

class RequirementCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Validate.Requirement]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateRequirementBuilder(self, requirement: Validate.Requirement) -> Validate.RequirementBuilder:
        ...
    def FindObject(self, id: str) -> Validate.Requirement:
        ...
    def LoadFromExternalSource(self, sourceType: Validate.RequirementCollection.SourceTypeOptions, source: str, revision: str, project: str) -> None:
        ...
    def RefreshFromExternalSource(self, requirementTags: typing.List[Validate.Requirement]) -> None:
        ...
    def Tag(self) -> Tag: ...

    RevisionRule: str


    class SourceTypeOptions(enum.Enum):
        LocalFile = 0
        TeamcenterFile = 1
        Teamcenter = 2
        MeasurableAttribute = 3
    

class RequirementCheckCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Validate.RequirementCheck]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateRequirementCheck(self) -> Validate.RequirementCheck:
        ...
    def Tag(self) -> Tag: ...



class RequirementCheck(Validation):
    def __init__(self) -> None: ...
    def SetFormula(self, formula: str) -> None:
        ...
    CheckName: str
    Formula: str
    ParentRequirement: Validate.Requirement
    SaveResultsToTeamcenterOption: Validate.RequirementCheck.SaveResultsToTeamcenterOptions


    class SaveResultsToTeamcenterOptions(enum.Enum):
        DoNotSave = 0
        SaveIfPassed = 1
        AlwaysSave = 2
    

class RequirementBuilder(Builder):
    def __init__(self) -> None: ...
    def GetValidValues(self) -> str:
        ...
    def SetValidValues(self, validValues: str) -> None:
        ...
    def GetRequirementDescription(self) -> str:
        ...
    def SetRequirementDescription(self, requirementDescription: str) -> None:
        ...
    DataTypeOption: Validate.RequirementBuilder.DataTypeOptions
    DefinitionMethodOption: Validate.RequirementBuilder.DefinitionMethodOptions
    DoubleSidedMaximumValue: str
    DoubleSidedMinimumValue: str
    Formula: str
    Name: str
    RelationalOperatorOption: Validate.RequirementBuilder.RelationalOperatorOptions
    RelationalOperatorOptionOnMaximumValue: Validate.RequirementBuilder.RelationalOperatorOptions
    RelationalOperatorOptionOnMinimumValue: Validate.RequirementBuilder.RelationalOperatorOptions
    RequirementTolerance: float
    RequirementTypeOption: Validate.RequirementBuilder.RequirementTypeOptions
    SeverityOption: Validate.RequirementBuilder.SeverityOptions
    SingleSidedValue: str


    class SeverityOptions(enum.Enum):
        Error = 0
        Warning = 1
        Information = 2
    

    class RequirementTypeOptions(enum.Enum):
        ValidationLimit = 0
        DesignLimit = 1
    

    class RelationalOperatorOptions(enum.Enum):
        Equal = 0
        NotEqual = 1
        LessThan = 2
        LessThanOrEqual = 3
        GreaterThan = 4
        GreaterThanOrEqual = 5
    

    class DefinitionMethodOptions(enum.Enum):
        SingleSidedComparison = 0
        DoubleSidedComparison = 1
        SetOfValues = 2
        Formula = 3
    

    class DataTypeOptions(enum.Enum):
        Number = 0
        String = 1
        Boolean = 2
        Integer = 3
        Point = 4
    

class Requirement(NXObject):
    def __init__(self) -> None: ...
    def NewCheck(self, name: str, formula: str) -> Validate.RequirementCheck:
        ...
    def Delete(self) -> None:
        ...
    def RefreshFromExternalSource(self) -> None:
        ...


class PorosityAnalysisResult(Validate.AnalysisResult):
    def __init__(self) -> None: ...


class PersistentResultCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Validate.PersistentResult]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class PersistentResult(NXObject):
    def __init__(self) -> None: ...
    def AddTrackingObjects(self, key: str, objects: typing.List[TaggedObject]) -> None:
        ...
    def GetTrackingObjects(self, key: str) -> typing.List[TaggedObject]:
        ...
    CheckerClassId: str
    ErrorLevel: Validation.Result
    UpToDateStatus: bool


class PBFPrintTimeParameter(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    HatchSpacing: Expression
    IslandLength: Expression
    LayerThickness: Expression
    RecoatingTime: Expression
    SkyWritingTime: Expression
    TravelSpeed: Expression


class PartOrientationAnalysisResult(Validate.AnalysisResult):
    def __init__(self) -> None: ...
    def GetNumOfOptimumOrientations(self) -> int:
        ...
    def GetOptimumOrientation(self, optimumOrientationIndex: int, origin: Point3d, orientation: Vector3d, checkerValues: typing.List[Validate.PartOrientationAnalysisResult.CheckerValues]) -> None:
        ...
    def GetMinimumOrientation(self, checkerIndex: Validate.PartOrientationAnalysisResult.CheckerIndex, origin: Point3d, orientation: Vector3d, checkerValues: typing.List[Validate.PartOrientationAnalysisResult.CheckerValues]) -> None:
        ...


    class PartOrientationAnalysisResultCheckerValues():
        MCheckerIndex: Validate.PartOrientationAnalysisResult.CheckerIndex
        MCheckerMinValue: float
        MCheckerValue: float
        MCheckerMaxValue: float
        def ToString(self) -> str:
            ...
    

    class CheckerIndex(enum.Enum):
        Minimum = 0
        SurfaceArea = 0
        SupportVolume = 1
        PrintTime = 2
        Overheat = 3
        Maximum = 4
    

class PartNode(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    FileName: str
    PartObject: Part


class Parser(TaggedObject):
    def __init__(self) -> None: ...
    def Commit(self) -> None:
        ...
    def GetPartResultObjects(self, partResultObject: typing.List[Validate.ResultObject]) -> None:
        ...
    def GetProfileResultObjects(self, profileResultObject: typing.List[Validate.ResultObject]) -> None:
        ...
    def GetProfileResultObjects(self, resultObject: Validate.ResultObject, profileResultObject: typing.List[Validate.ResultObject]) -> None:
        ...
    def GetTestResultObjects(self, testResultObject: typing.List[Validate.ResultObject]) -> None:
        ...
    def GetTestResultObjects(self, resultObject: Validate.ResultObject, testResultObject: typing.List[Validate.ResultObject]) -> None:
        ...
    def GetObjectSetResultObjects(self, resultObject: Validate.ResultObject, objectSetResultObject: typing.List[Validate.ResultObject]) -> None:
        ...
    def GetObjectResultObjects(self, resultObject: Validate.ResultObject, objectResultObject: typing.List[Validate.ResultObject]) -> None:
        ...
    def DeleteResultObject(self, resultObject: Validate.ResultObject) -> ErrorList:
        ...
    def DeleteResult(self, resultObject: Validate.ResultObject) -> int:
        ...
    def ClearResultObjects(self) -> None:
        ...
    DataSource: Validate.Parser.DataSourceTypes
    MaxDisplayObjects: int


    class DataSourceTypes(enum.Enum):
        MostRecentRun = 0
        ResultFromPart = 1
        ResultFromTeamcenter = 2
        ResultFromNXChecks = 3
        ResultFromLogFile = 4
    

class Parameter(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def IsList(self) -> bool:
        ...
    def GetBooleanValue(self) -> bool:
        ...
    def GetBooleanValues(self) -> bool:
        ...
    def SetBooleanValue(self, data: bool) -> None:
        ...
    def SetBooleanValues(self, data: bool) -> None:
        ...
    def GetIntValue(self) -> int:
        ...
    def GetIntValues(self) -> int:
        ...
    def SetIntValue(self, data: int) -> None:
        ...
    def SetIntValues(self, data: int) -> None:
        ...
    def GetDoubleValue(self) -> float:
        ...
    def GetDoubleValues(self) -> float:
        ...
    def SetDoubleValue(self, data: float) -> None:
        ...
    def SetDoubleValues(self, data: float) -> None:
        ...
    def GetStringValue(self) -> str:
        ...
    def GetStringValues(self) -> str:
        ...
    def SetStringValue(self, data: str) -> None:
        ...
    def SetStringValues(self, data: str) -> None:
        ...
    def GetPoint3dValue(self) -> Point3d:
        ...
    def GetPoint3dValues(self) -> typing.List[Point3d]:
        ...
    def SetPoint3dValue(self, data: Point3d) -> None:
        ...
    def SetPoint3dValues(self, data: typing.List[Point3d]) -> None:
        ...
    def GetVector3dValue(self) -> Vector3d:
        ...
    def GetVector3dValues(self) -> typing.List[Vector3d]:
        ...
    def SetVector3dValue(self, data: Vector3d) -> None:
        ...
    def SetVector3dValues(self, data: typing.List[Vector3d]) -> None:
        ...
    def GetNXObjectValue(self) -> NXObject:
        ...
    def GetNXObjectValues(self) -> typing.List[NXObject]:
        ...
    def SetNXObjectValue(self, data: NXObject) -> None:
        ...
    def SetNXObjectValues(self, data: typing.List[NXObject]) -> None:
        ...
    Title: str
    Type: RuleManager.RuleType


class OverrideBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDetailReason(self) -> str:
        ...
    def SetDetailReason(self, detailReason: str) -> None:
        ...
    def GetDecisionComments(self) -> str:
        ...
    def SetDecisionComments(self, decisionComments: str) -> None:
        ...
    Category: str
    DecisionAction: Validate.OverrideBuilder.DecisionActions
    DecisionUser: str
    Reason: str
    RequestType: Validate.OverrideBuilder.RequestTypes
    ToState: Validate.OverrideBuilder.ToStates


    class ToStates(enum.Enum):
        Passed = 0
        Failed = 1
    

    class RequestTypes(enum.Enum):
        Permanent = 0
        Temporary = 1
    

    class DecisionActions(enum.Enum):
        Approved = 0
        Rejected = 1
        Pending = 2
    

class Override(NXObject):
    def __init__(self) -> None: ...


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MJFPrintTimeParameter(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    LayerPrintTime: Expression
    LayerThickness: Expression


class Logger(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def LogResult(self, result: Validation.Result, message: str) -> None:
        ...
    def LogNXObject(self, result: Validation.Result, anObject: NXObject) -> None:
        ...
    def LogNXObject(self, result: Validation.Result, anObject: NXObject, message: str) -> None:
        ...
    def LogNXObject(self, result: Validation.Result, anObject: NXObject, message: str, objectName: str, referencePoints: typing.List[Point3d], referenceVectors: typing.List[Vector3d]) -> None:
        ...
    def LogNXObjectSet(self, name: str, message: str) -> Validate.Logger:
        ...
    def LogBooleanAttribute(self, title: str, booleanValue: bool) -> None:
        ...
    def LogIntegerAttribute(self, title: str, integerValue: int) -> None:
        ...
    def LogRealAttribute(self, title: str, realValue: float) -> None:
        ...
    def LogStringAttribute(self, title: str, stringValue: str) -> None:
        ...
    def LogBooleanAttributes(self, title: str, attrs: bool) -> None:
        ...
    def LogIntegerAttributes(self, title: str, attrs: int) -> None:
        ...
    def LogRealAttributes(self, title: str, attrs: float) -> None:
        ...
    def LogStringAttributes(self, title: str, attrs: str) -> None:
        ...


class LinkedParameterReqDialogBuilder(Builder):
    def __init__(self) -> None: ...
    def AppendMeasurableAttribute(self, logicalItemId: str, logicalItemRevId: str, mesAttrName: str, mesAttrRevId: str) -> None:
        ...


class KeyPerformanceInterfaceCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetKeyPerformanceInterfaceCollection(self, owner: Session) -> Validate.KeyPerformanceInterfaceCollection:
        ...
    def CreateLinkedParameterRequirementsBuilder(self, part: Part) -> Validate.LinkedParameterReqDialogBuilder:
        ...
    def RefreshLinkedParameterRequirements(self, part: Part, requirementTags: typing.List[Validate.Requirement], refreshToLatest: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class FDMPrintTimeParameter(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    LayerThickness: Expression
    NozzleDiameter: Expression
    TravelSpeed: Expression


class CheckWhollyEnclosedVolumeBuilder(Builder):
    def __init__(self) -> None: ...
    AutomaticUpdate: bool
    DisplayResolutionBuilder: GeometricUtilities.DisplayResolutionBuilder
    PreviewState: bool
    SelectionAndPlacement: Validate.SelectionAndPlacementBuilder
    WhollyEnclosedVolumeColor: NXColor


class CheckTrappedSupportsBuilder(Builder):
    def __init__(self) -> None: ...
    Angle: float
    AutomaticUpdate: bool
    DisplayResolutionBuilder: GeometricUtilities.DisplayResolutionBuilder
    NonTrappedSupportAreasColor: NXColor
    PreviewState: bool
    SelectionAndPlacement: Validate.SelectionAndPlacementBuilder
    ShowOnlyFailArea: bool
    TrappedArea: float
    TrappedSupportAreasColor: NXColor


class CheckThermalDistortionBuilder(Builder):
    def __init__(self) -> None: ...
    def Update(self) -> None:
        ...
    def CheckJobStatus(self) -> None:
        ...
    def CreatePrintCsys(self) -> None:
        ...
    def OrientPartToMinimumThermalDistortion(self) -> None:
        ...
    BuildPlateTemperature: Expression
    BuildPlateThickness: Expression
    CheckerCreationTime: str
    CriticalAngle: Expression
    DisplayResolutionBuilder: GeometricUtilities.DisplayResolutionBuilder
    ElementSize: Expression
    FilePathKey: str
    JobID: str
    JobStatus: Validate.CheckThermalDistortionBuilder.JobStatusType
    LayerThickness: Expression
    MaterialEnum: int
    NumberOfLasers: Expression
    PartMaterial: str
    PrinterDiameter: Expression
    PrinterHeight: Expression
    PrinterLength: Expression
    PrinterName: str
    PrinterShape: Validate.CheckThermalDistortionBuilder.PrinterShapeTypes
    PrinterWidth: Expression
    SelectionAndPlacement: Validate.SelectionAndPlacementBuilder
    StressRelief: bool
    UserID: str


    class PrinterShapeTypes(enum.Enum):
        Block = 0
        Cylinder = 1
    

    class JobStatusType(enum.Enum):
        Queued = 0
        Processing = 1
        Completed = 2
        Error = 3
        Unknown = 4
    

class CheckPrintTimeBuilder(Builder):
    def __init__(self) -> None: ...
    def Update(self) -> None:
        ...
    AutomaticUpdate: bool
    FDMPrintTimeParameter: Validate.FDMPrintTimeParameter
    MJFPrintTimeParameter: Validate.MJFPrintTimeParameter
    PBFPrintTimeParameter: Validate.PBFPrintTimeParameter
    PrintTime: float
    Printer: Validate.CheckPrintTimeBuilder.PrinterType
    SelectionAndPlacement: Validate.SelectionAndPlacementBuilder


    class PrinterType(enum.Enum):
        PowderBedFusion = 0
        MultiJetFusion = 1
        FusedDepositionModeling = 2
    

class CheckPorosityBuilder(Builder):
    def __init__(self) -> None: ...
    def RemoveColorLegend(self) -> None:
        ...
    def MakeColorLegend(self) -> None:
        ...
    def AddGeometricConstraintPoint(self, face: Face, point: Point) -> None:
        ...
    def SetGeometricConstraintPoint(self, face: Face, point: Point) -> None:
        ...
    def DeleteGeometricConstraintPoint(self, point: Point) -> None:
        ...
    def ClearGeometricConstraintPoints(self) -> None:
        ...
    AboveLimit: float
    AboveTarget: float
    AutomaticUpdate: bool
    Average: float
    BelowLimit: float
    BelowTarget: float
    ColorMapDisplayOptionType: Validate.CheckPorosityBuilder.ColorMapDisplayOptionTypes
    GeometricConstraintDataManager: Features.GeometricConstraintDataManager
    Maximum: float
    MaximumPorosity: float
    Median: float
    Minimum: float
    MinimumPorosity: float
    PreviewState: bool
    SelectionAndPlacement: Validate.SelectionAndPlacementBuilder
    TargetPorosity: float
    VoxelSize: Expression
    WithinLimit: float


    class ColorMapDisplayOptionTypes(enum.Enum):
        All = 0
        WithinLimits = 1
        OutsideLimits = 2
        AboveTarget = 3
        BelowTarget = 4
    

class CheckPartOrientationBuilder(Builder):
    def __init__(self) -> None: ...
    def CalculateCheck(self, checkerValues: typing.List[Validate.PartOrientationAnalysisResult.CheckerValues]) -> None:
        ...
    def StartCalculation(self) -> None:
        ...
    def OrientToMinimum(self, checkerIndex: Validate.PartOrientationAnalysisResult.CheckerIndex) -> None:
        ...
    def GetNumOfOptimumOrientations(self) -> int:
        ...
    def OptimumSolution(self, orientationIndex: int) -> None:
        ...
    def GetOptimumOrientation(self, optimumOrientationIndex: int, origin: Point3d, orientation: Vector3d, checkerValues: typing.List[Validate.PartOrientationAnalysisResult.CheckerValues]) -> None:
        ...
    def GetMinimumOrientation(self, checkerIndex: Validate.PartOrientationAnalysisResult.CheckerIndex, origin: Point3d, orientation: Vector3d, checkerValues: typing.List[Validate.PartOrientationAnalysisResult.CheckerValues]) -> None:
        ...
    def RemoveAllSolutions(self) -> None:
        ...
    def GetPartOrientationResult(self) -> Validate.PartOrientationAnalysisResult:
        ...
    Accuracy: Validate.CheckPartOrientationBuilder.AccuracyLevel
    FDMPrintTimeParameter: Validate.FDMPrintTimeParameter
    MJFPrintTimeParameter: Validate.MJFPrintTimeParameter
    MaxOverhangAngleForOverHeating: Expression
    MaxOverhangAngleForVolume: Expression
    PBFPrintTimeParameter: Validate.PBFPrintTimeParameter
    Printer: Validate.CheckPrintTimeBuilder.PrinterType
    SelectionAndPlacement: Validate.SelectionAndPlacementBuilder
    ValidateOverheating: bool
    ValidatePrintTime: bool
    ValidateSupportVolume: bool
    ValidateSurfaceArea: bool
    WeightOverheating: int
    WeightPrintTime: int
    WeightSupportVolume: int
    WeightSurfaceArea: int


    class AccuracyLevel(enum.Enum):
        Coarse = 1
        Low = 2
        Medium = 3
        High = 4
        VeryHigh = 5
    

class CheckOverheatingBuilder(Builder):
    def __init__(self) -> None: ...
    def Update(self) -> None:
        ...
    AutomaticUpdate: bool
    DisplayResolution: GeometricUtilities.DisplayResolutionBuilder
    MaximumOverhangAngle: Expression
    NonOverheatingColor: NXColor
    OverheatingArea: float
    OverheatingColor: NXColor
    SelectionAndPlacement: Validate.SelectionAndPlacementBuilder
    ShowOnlyOverheatingAreas: bool


class CheckModelWithinPrintableVolumeBuilder(Builder):
    def __init__(self) -> None: ...
    AutomaticUpdate: bool
    CloseToPrintableVolumeColor: NXColor
    DisplayResolutionBuilder: GeometricUtilities.DisplayResolutionBuilder
    DistanceTolerance: float
    OutOfPrintableVolumeColor: NXColor
    PreviewState: bool
    PrinterDiameter: float
    PrinterHeight: float
    PrinterLength: float
    PrinterName: str
    PrinterOrientation: Matrix3x3
    PrinterOrigin: Point3d
    PrinterShapeType: Validate.CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes
    PrinterWidth: float
    SelectionAndPlacement: Validate.SelectionAndPlacementBuilder
    ShowType: Validate.CheckModelWithinPrintableVolumeBuilder.ShowTypes
    WithinPrintableVolumeColor: NXColor


    class ShowTypes(enum.Enum):
        Printer = 0
        Product = 1
        Both = 2
    

    class PrinterShapeTypes(enum.Enum):
        Block = 0
        Cylinder = 1
    

class CheckMinimumWallThicknessBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDynamicResult(self, selectedFace: Face, dynamicPnt: Point3d, thickness: float, direction: Vector3d, closestPnt: Point3d) -> bool:
        ...
    AutomaticUpdate: bool
    DisplayResolutionBuilder: GeometricUtilities.DisplayResolutionBuilder
    FailureArea: float
    LessThanMinThicknessColor: NXColor
    MoreThanMinThicknessColor: NXColor
    PreviewState: bool
    SelectionAndPlacement: Validate.SelectionAndPlacementBuilder
    ShowOnlyFailArea: bool
    Thickness: float


class CheckMinimumRadiusBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDynamicResult(self, selectedFace: Face, dynamicPnt: Point3d) -> float:
        ...
    AutomaticUpdate: bool
    CurvatureType: Validate.CheckMinimumRadiusBuilder.CurvatureTypes
    DisplayResolutionBuilder: GeometricUtilities.DisplayResolutionBuilder
    ExcludeConvex: bool
    FailureArea: float
    LessThanMinimumRadiusColor: NXColor
    MinimumRadius: float
    MoreThanMinimumRadiusColor: NXColor
    PreviewState: bool
    SelectionAndPlacement: Validate.SelectionAndPlacementBuilder
    ShowOnlyFailArea: bool


    class CurvatureTypes(enum.Enum):
        Radius = 0
        Sectional = 1
    

class CheckMaximumOverhangAngleBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTargets(self) -> typing.List[Body]:
        """[Obsolete("Deprecated in NX1899.0.0.  Use  NXOpen.Validate.SelectionAndPlacementBuilder.GetTargets ")"""
        ...
    def SetTargets(self, targets: typing.List[Body]) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use  NXOpen.Validate.SelectionAndPlacementBuilder.SetTargets ")"""
        ...
    def Update(self) -> None:
        ...
    Angle: float
    AutomaticUpdate: bool
    DisplayResolutionBuilder: GeometricUtilities.DisplayResolutionBuilder
    DrawOrientation: Matrix3x3
    DrawOrigin: Point3d
    ExceedExtendToleranceColor: NXColor
    ExtendedAngularTolerance: float
    LessThanMaxAngleColor: NXColor
    MoreThanMaxAngleColor: NXColor
    OverhangArea: float
    PreviewState: bool
    SelectionAndPlacement: Validate.SelectionAndPlacementBuilder
    ShowOnlyExceedingOverhangAngles: bool
    ShowOnlyFailArea: bool


class CheckerNode(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetChildCheckerInstanceNames(self) -> str:
        ...
    def GetChildCheckerEnabledFlags(self, childCheckerInstances: str) -> bool:
        ...
    def SetChildCheckerEnabledFlags(self, childCheckerInstances: str, enableFlags: bool) -> None:
        ...
    def GetChildCheckerEnabledFlag(self, childCheckerInstance: str) -> bool:
        ...
    def SetChildCheckerEnabledFlag(self, childCheckerInstance: str, enableFlag: bool) -> None:
        ...
    def GetParameter(self, parameterTitle: str) -> Validate.Parameter:
        ...
    def GetParameters(self) -> typing.List[Validate.Parameter]:
        ...
    def AskLogger(self) -> Validate.Logger:
        ...
    AttributeCustomizedFormulas: str
    ClassName: str


class CheckerDefinition(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetDocumentationHandler(self, document: Validate.CheckerDefinition.DocumentationHandler) -> None:
        ...
    def SetCustomizationHandler(self, customize: Validate.CheckerDefinition.CustomizationHandler) -> None:
        ...


    

    

    

    

    

    

class CheckChannelRatioBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTableData(self, tableData: typing.List[Validate.CheckChannelRatioBuilder.TableData]) -> None:
        ...
    def SetTableData(self, tableData: typing.List[Validate.CheckChannelRatioBuilder.TableData]) -> None:
        ...
    def GetFaces(self) -> typing.List[Face]:
        ...
    def SetFaces(self, faces: typing.List[Face]) -> None:
        ...
    def GetBodies(self) -> typing.List[Body]:
        ...
    def SetBodies(self, bodies: typing.List[Body]) -> None:
        ...
    def SetNeedRegenerateFacets(self, needRegenerateFacets: bool) -> None:
        ...
    AutomaticUpdate: bool
    DisplayResolution: GeometricUtilities.DisplayResolutionBuilder
    FailedSegmentsColor: NXColor
    MaximumWidth: float
    MinimumRatio: float
    Orientation: Matrix3x3
    Origin: Point3d
    PassedSegmentsColor: NXColor
    PreviewState: bool
    SegmentLength: float
    ShowOnlyFailedSegments: bool


    class CheckChannelRatioBuilderTableData():
        Angle: float
        MinimumDiameter: float
        def ToString(self) -> str:
            ...
        def __init__(self, Angle: float, MinimumDiameter: float) -> None: ...
    

class AnalysisResultCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Validate.AnalysisResult]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateCheckMaximumOverhangAngleBuilder(self, persistentResult: Validate.AnalysisResult) -> Validate.CheckMaximumOverhangAngleBuilder:
        ...
    def CreateCheckMinimumRadiusBuilder(self, persistentResult: Validate.AnalysisResult) -> Validate.CheckMinimumRadiusBuilder:
        ...
    def CreateCheckMinimumWallThicknessBuilder(self, persistentResult: Validate.AnalysisResult) -> Validate.CheckMinimumWallThicknessBuilder:
        ...
    def CreateCheckTrappedSupportsBuilder(self, persistentResult: Validate.AnalysisResult) -> Validate.CheckTrappedSupportsBuilder:
        ...
    def CreateCheckModelWithinPrintableVolumeBuilder(self, persistentResult: Validate.AnalysisResult) -> Validate.CheckModelWithinPrintableVolumeBuilder:
        ...
    def CreateCheckWhollyEnclosedVolumeBuilder(self, persistentResult: Validate.AnalysisResult) -> Validate.CheckWhollyEnclosedVolumeBuilder:
        ...
    def EvaluateAll(self, analysisResults: typing.List[Validate.AnalysisResult]) -> None:
        ...
    def DeactivateAll(self, analysisResults: typing.List[Validate.AnalysisResult]) -> None:
        ...
    def FindAllAnalysisResults(self) -> typing.List[Validate.AnalysisResult]:
        ...
    def FindObject(self, sid: str) -> Validate.AnalysisResult:
        ...
    def CreateCheckPrintTimeBuilder(self, persistentResult: Validate.AnalysisResult) -> Validate.CheckPrintTimeBuilder:
        ...
    def CreateCheckOverheatingBuilder(self, persistentResult: Validate.AnalysisResult) -> Validate.CheckOverheatingBuilder:
        ...
    def CreateCheckPartOrientationBuilder(self, persistentResult: Validate.PartOrientationAnalysisResult) -> Validate.CheckPartOrientationBuilder:
        ...
    def FindAllAnalysisResultsOfType(self, analysisType: Validate.AnalysisResultCollection.AnalysisResultType) -> typing.List[Validate.AnalysisResult]:
        ...
    def GetAnalysisResultValue(self, persistentResult: Validate.AnalysisResult) -> float:
        ...
    def CreateCheckPorosityBuilder(self, persistentResult: Validate.AnalysisResult) -> Validate.CheckPorosityBuilder:
        ...
    def CreateCheckChannelRatioBuilder(self, persistentResult: Validate.AnalysisResult) -> Validate.CheckChannelRatioBuilder:
        ...
    def CreateCheckThermalDistortionBuilder(self, persistentResult: Validate.AnalysisResult) -> Validate.CheckThermalDistortionBuilder:
        ...
    def Tag(self) -> Tag: ...



    class AnalysisResultType(enum.Enum):
        MaximumOverhangAngle = 0
        PrintTime = 1
        Overheating = 2
    

class AnalysisResult(Validate.PersistentResult):
    def __init__(self) -> None: ...
    def Evaluate(self) -> None:
        ...
    def Deactivate(self) -> None:
        ...
    def Activate(self) -> None:
        ...
    ActiveStatus: bool


