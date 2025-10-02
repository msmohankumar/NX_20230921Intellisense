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
    def Tag(self) -> Tag: ...



class ResultObject(NXObject):
    def __init__(self) -> None: ...
    def CreateOverrideBuilder(self, overrideRequest: Validate.Override) -> Validate.OverrideBuilder:
        ...
    def DeleteOverride(self) -> None:
        ...
    CategoryName: str
    ClassName: str
    Disabled: bool
    Name: str
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
    AttributeCustomizedFormulas: str
    ClassName: str


