from ...NXOpen import *
from ..VisualReporting import *

import typing
import enum

class VisualReportManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateVisualReportBuilder(self, visualReport: VisualReporting.VisualReport) -> VisualReporting.VisualReportBuilder:
        ...
    def Open(self, filename: str) -> VisualReporting.VisualReport:
        ...
    def Unload(self, visualReport: VisualReporting.VisualReport) -> None:
        ...
    def OpenReports(self, folders: str, names: str) -> typing.List[VisualReporting.VisualReport]:
        ...
    def ActivateCurrentVisualReport(self) -> None:
        ...
    def DeactivateCurrentVisualReport(self) -> None:
        ...
    def MergeReports(self, visualReports: typing.List[VisualReporting.VisualReport], mergedReportName: str, mergedReportDescription: str) -> VisualReporting.VisualReport:
        ...
    def CreateSpecifyDateBuilder(self) -> VisualReporting.SpecifyDateBuilder:
        ...
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReporting.VisualReport.ScopeTypeOption, objectTypes: typing.List[VisualReporting.VisualReport.ObjectTypeOption], dataType: VisualReporting.Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getStringTypePropertyValue: VisualReporting.VisualReportManager.GetStringTypePropertyValue) -> None:
        ...
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReporting.VisualReport.ScopeTypeOption, objectTypes: typing.List[VisualReporting.VisualReport.ObjectTypeOption], dataType: VisualReporting.Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getIntegerTypePropertyValue: VisualReporting.VisualReportManager.GetIntegerTypePropertyValue) -> None:
        ...
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReporting.VisualReport.ScopeTypeOption, objectTypes: typing.List[VisualReporting.VisualReport.ObjectTypeOption], dataType: VisualReporting.Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getRealTypePropertyValue: VisualReporting.VisualReportManager.GetRealTypePropertyValue) -> None:
        ...
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReporting.VisualReport.ScopeTypeOption, objectTypes: typing.List[VisualReporting.VisualReport.ObjectTypeOption], dataType: VisualReporting.Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getBooleanTypePropertyValue: VisualReporting.VisualReportManager.GetBooleanTypePropertyValue) -> None:
        ...
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReporting.VisualReport.ScopeTypeOption, objectTypes: typing.List[VisualReporting.VisualReport.ObjectTypeOption], dataType: VisualReporting.Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getDateTypePropertyValue: VisualReporting.VisualReportManager.GetDateTypePropertyValue) -> None:
        ...
    def UnregisterProperty(self, propertyKey: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    VisualReports: VisualReporting.VisualReportCollection
    VisualReportExplorer: VisualReporting.VisualReportExplorer
    Current: VisualReporting.VisualReport


    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

class VisualReportExplorer(Utilities.NXRemotableObject):
    def __init__(self, owner: VisualReporting.VisualReportManager) -> None: ...
    def ReportOnObjects(self, nxObjects: typing.List[NXObject], reportOnObjectsOption: VisualReporting.VisualReportExplorer.ReportOnObjectsOption) -> None:
        ...
    def RemoveReportObjects(self, nxObjects: typing.List[NXObject]) -> None:
        ...
    def ClearReportObjects(self) -> None:
        ...
    def ResetReportObjects(self) -> None:
        ...
    def GetExploringGroup(self) -> VisualReporting.GroupLabel:
        ...
    def SetGroupToExplore(self, groupLabel: VisualReporting.GroupLabel) -> None:
        ...
    def ReportDown(self, reportOnObjectsOption: VisualReporting.VisualReportExplorer.ReportOnObjectsOption) -> VisualReporting.VisualReportExplorer.ReportDownStatus:
        ...
    def ReportDown(self, nxObjects: typing.List[NXObject], reportOnObjectsOption: VisualReporting.VisualReportExplorer.ReportOnObjectsOption) -> VisualReporting.VisualReportExplorer.ReportDownStatus:
        ...
    def ReportOnChildren(self, nxObjects: typing.List[NXObject], reportOnObjectsOption: VisualReporting.VisualReportExplorer.ReportOnObjectsOption) -> None:
        ...
    def ReportOnParents(self, nxObjects: typing.List[NXObject], reportOnObjectsOption: VisualReporting.VisualReportExplorer.ReportOnObjectsOption) -> None:
        ...
    def Tag(self) -> Tag: ...

    ExploreReport: VisualReporting.VisualReportExplorer.ExploreReportOption


    class ReportOnObjectsOption(enum.Enum):
        Replace = 0
        Add = 1
    

    class ReportDownStatus(enum.Enum):
        None = 0
        End = 1
        More = 2
    

    class ExploreReportOption(enum.Enum):
        Off = 0
        On = 1
    

class VisualReportCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[VisualReporting.VisualReport]:
        ...
    def __init__(self, owner: VisualReporting.VisualReportManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> VisualReporting.VisualReport:
        ...
    def Tag(self) -> Tag: ...



class VisualReportBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateVisualReport(self) -> VisualReporting.VisualReport:
        ...
    def EditVisualReport(self, visualReport: VisualReporting.VisualReport) -> None:
        ...
    def CommitAsCopy(self) -> VisualReporting.VisualReport:
        ...
    def EnableUnmatchedGroupOfVisualReport(self, enableUnmatchedGroup: bool) -> None:
        ...
    def GetRule(self, index: int) -> VisualReporting.Rule:
        ...
    def GetRules(self) -> typing.List[VisualReporting.Rule]:
        ...
    def GetClassifiersOfRule(self, rule: VisualReporting.Rule) -> typing.List[VisualReporting.Classifier]:
        ...
    def GetActiveClassifierOfRule(self, rule: VisualReporting.Rule) -> VisualReporting.Classifier:
        ...
    def SetActiveClassifierOfRule(self, rule: VisualReporting.Rule, activeClassifier: VisualReporting.Classifier) -> None:
        ...
    def GetReferencePropertiesOfReportingProperty(self, properties: typing.List[VisualReporting.Property], usages: typing.List[VisualReporting.VisualReportBuilder.PropertyUsageOption]) -> None:
        ...
    def SetReferencePropertiesOfReportingProperty(self, properties: typing.List[VisualReporting.Property], usages: typing.List[VisualReporting.VisualReportBuilder.PropertyUsageOption]) -> None:
        ...
    def GetPropertyOfCondition(self, condition: VisualReporting.Condition) -> VisualReporting.Property:
        ...
    def SetPropertyOfCondition(self, condition: VisualReporting.Condition, property: VisualReporting.Property) -> None:
        ...
    def RemovePropertyFromCondition(self, condition: VisualReporting.Condition) -> None:
        ...
    def GetOperatorTypeOfCondition(self, condition: VisualReporting.Condition) -> VisualReporting.Condition.OperatorOption:
        ...
    def SetOperatorTypeOfCondition(self, condition: VisualReporting.Condition, operatorType: VisualReporting.Condition.OperatorOption) -> None:
        ...
    def GetValueOfCondition(self, condition: VisualReporting.Condition) -> str:
        ...
    def SetValueOfCondition(self, condition: VisualReporting.Condition, value: str) -> None:
        ...
    def GetPropertyForComparison(self, condition: VisualReporting.Condition) -> VisualReporting.Property:
        ...
    def SetPropertyForComparison(self, condition: VisualReporting.Condition, property: VisualReporting.Property) -> None:
        ...
    def AddChildToCondition(self, condition: VisualReporting.Condition, childCondition: VisualReporting.Condition) -> None:
        ...
    def RemoveChildFromCondition(self, condition: VisualReporting.Condition, childCondition: VisualReporting.Condition) -> None:
        ...
    def GetHasUserSpecifiedValueForCondition(self, condition: VisualReporting.Condition) -> bool:
        ...
    def SetHasUserSpecifiedValueForCondition(self, condition: VisualReporting.Condition, isUserSpecified: bool) -> None:
        ...
    def GetUserPromptOfCondition(self, condition: VisualReporting.Condition) -> str:
        ...
    def SetUserPromptOfCondition(self, condition: VisualReporting.Condition, userPrompt: str) -> None:
        ...
    def GetDescriptionOfCondition(self, condition: VisualReporting.Condition) -> str:
        ...
    def SetDescriptionOfCondition(self, condition: VisualReporting.Condition, description: str) -> None:
        ...
    def GetClassifierTypeOfRule(self, rule: VisualReporting.Rule) -> VisualReporting.Classifier.TypeOption:
        ...
    def SetClassifierTypeOfRule(self, rule: VisualReporting.Rule, classifierType: VisualReporting.Classifier.TypeOption) -> VisualReporting.Classifier:
        ...
    def GetReportingPropertyOfRule(self, rule: VisualReporting.Rule) -> VisualReporting.Property:
        ...
    def SetReportingPropertyOfRule(self, rule: VisualReporting.Rule, reportingProperty: VisualReporting.Property) -> None:
        ...
    def GetReportingDatatypeOfRule(self, rule: VisualReporting.Rule) -> VisualReporting.Property.DatatypeOption:
        ...
    def SetReportingDatatypeOfRule(self, rule: VisualReporting.Rule, datatype: VisualReporting.Property.DatatypeOption) -> None:
        ...
    def RemoveFilterConditionFromRule(self, rule: VisualReporting.Rule) -> None:
        ...
    def GetFilterConditionOfRule(self, rule: VisualReporting.Rule) -> VisualReporting.Condition:
        ...
    def SetFilterConditionOfRule(self, rule: VisualReporting.Rule, filterCondition: VisualReporting.Condition) -> None:
        ...
    def GetManualGroupingForRule(self, rule: VisualReporting.Rule) -> bool:
        ...
    def SetManualGroupingForRule(self, rule: VisualReporting.Rule, isManualGrouping: bool) -> None:
        ...
    def GetGroupingMethodOfRule(self, rule: VisualReporting.Rule) -> VisualReporting.Classifier.GroupingMethodOption:
        ...
    def SetGroupingMethodOfRule(self, rule: VisualReporting.Rule, groupingMethod: VisualReporting.Classifier.GroupingMethodOption) -> None:
        ...
    def GetRangeMethodOfRule(self, rule: VisualReporting.Rule) -> VisualReporting.Classifier.RangeMethodOption:
        ...
    def SetRangeMethodOfRule(self, rule: VisualReporting.Rule, rangeMethod: VisualReporting.Classifier.RangeMethodOption) -> None:
        ...
    def GetToleranceOfRule(self, rule: VisualReporting.Rule) -> float:
        ...
    def SetToleranceOfRule(self, rule: VisualReporting.Rule, tolerance: float) -> None:
        ...
    def GetAllGroupLabelsOfRule(self, rule: VisualReporting.Rule) -> typing.List[VisualReporting.GroupLabel]:
        ...
    def GetManualGroupLabelOfRule(self, rule: VisualReporting.Rule, index: int) -> VisualReporting.GroupLabel:
        ...
    def GetManualGroupLabelsOfRule(self, rule: VisualReporting.Rule) -> typing.List[VisualReporting.GroupLabel]:
        ...
    def DeleteGroupLabel(self, rule: VisualReporting.Rule, groupLabel: VisualReporting.GroupLabel) -> None:
        ...
    def UnsetUserNameOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel) -> None:
        ...
    def GetUserNameOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel) -> str:
        ...
    def SetUserNameOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel, name: str) -> None:
        ...
    def GetLowerBoundOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel) -> str:
        ...
    def SetLowerBoundOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel, lowerBound: str) -> None:
        ...
    def GetUpperBoundOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel) -> str:
        ...
    def SetUpperBoundOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel, upperBound: str) -> None:
        ...
    def GetValueOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel) -> str:
        ...
    def SetValueOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel, value: str) -> None:
        ...
    def GetDisplayStyleForGroupLabel(self, groupLabel: VisualReporting.GroupLabel) -> VisualReporting.GroupLabel.DisplayStyleOption:
        ...
    def SetDisplayStyleForGroupLabel(self, groupLabel: VisualReporting.GroupLabel, displayStyle: VisualReporting.GroupLabel.DisplayStyleOption) -> None:
        ...
    def GetColorOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel) -> NXColor.Rgb:
        ...
    def SetColorOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel, color: NXColor.Rgb) -> None:
        ...
    def GetBitmapNameOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel) -> str:
        ...
    def SetBitmapNameOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel, bitmapName: str) -> None:
        ...
    def GetCustomMessageOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel) -> str:
        ...
    def SetCustomMessageOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel, customMessage: str) -> None:
        ...
    def CreateProperty(self, propertyType: VisualReporting.Property.TypeOption) -> VisualReporting.Property:
        ...
    def CreateProperty(self, propertyId: str) -> VisualReporting.Property:
        ...
    def DeleteProperty(self, property: VisualReporting.Property) -> None:
        ...
    def CreateAndCondition(self) -> VisualReporting.Condition:
        ...
    def CreateOrCondition(self) -> VisualReporting.Condition:
        ...
    def CreateNotCondition(self) -> VisualReporting.Condition:
        ...
    def CreateStringCondition(self, property: VisualReporting.Property, value: str, operatorType: VisualReporting.Condition.OperatorOption) -> VisualReporting.Condition:
        ...
    def CreateIntegerCondition(self, property: VisualReporting.Property, value: int, operatorType: VisualReporting.Condition.OperatorOption) -> VisualReporting.Condition:
        ...
    def CreateRealCondition(self, property: VisualReporting.Property, value: float, operatorType: VisualReporting.Condition.OperatorOption, tolerance: float) -> VisualReporting.Condition:
        ...
    def CreateBooleanCondition(self, property: VisualReporting.Property, value: bool, operatorType: VisualReporting.Condition.OperatorOption) -> VisualReporting.Condition:
        ...
    def CreateNullCondition(self, property: VisualReporting.Property, value: bool, operatorType: VisualReporting.Condition.OperatorOption) -> VisualReporting.Condition:
        ...
    def CreateDateCondition(self, property: VisualReporting.Property, value: str, operatorType: VisualReporting.Condition.OperatorOption) -> VisualReporting.Condition:
        ...
    def GetParentCondition(self, condition: VisualReporting.Condition) -> VisualReporting.Condition:
        ...
    def IsChildCondition(self, condition: VisualReporting.Condition, childCondition: VisualReporting.Condition) -> bool:
        ...
    def GetChildCondition(self, condition: VisualReporting.Condition, index: int) -> VisualReporting.Condition:
        ...
    def GetChildConditions(self, condition: VisualReporting.Condition) -> typing.List[VisualReporting.Condition]:
        ...
    def CreateGroupLabel(self, name: str, rule: VisualReporting.Rule, afterGroupLabel: VisualReporting.GroupLabel) -> VisualReporting.GroupLabel:
        ...
    def SetPropertySpecification(self, property: VisualReporting.Property, key: str) -> None:
        ...
    def SetPropertySpecification(self, property: VisualReporting.Property, key: str, name: str) -> None:
        ...
    def GetPropertySpecification(self, property: VisualReporting.Property, propertyType: VisualReporting.Property.TypeOption, key: str, name: str) -> None:
        ...
    def GetReferencePropertiesOfReport(self, properties: typing.List[VisualReporting.Property], usages: typing.List[VisualReporting.VisualReportBuilder.PropertyUsageOption], notUsed: int) -> None:
        ...
    def SetReferencePropertiesOfReport(self, properties: typing.List[VisualReporting.Property], usages: typing.List[VisualReporting.VisualReportBuilder.PropertyUsageOption]) -> None:
        ...
    def Save(self) -> None:
        ...
    def GetTagPriorityOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel) -> VisualReporting.GroupLabel.TagPriorityOption:
        ...
    def SetTagPriorityOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel, tagPriority: VisualReporting.GroupLabel.TagPriorityOption) -> None:
        ...
    def GetErrorLevelOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel) -> Validation.Result:
        ...
    def SetErrorLevelOfGroupLabel(self, groupLabel: VisualReporting.GroupLabel, errorLevel: Validation.Result) -> None:
        ...
    def DeleteChildCondition(self, condition: VisualReporting.Condition, childCondition: VisualReporting.Condition) -> None:
        ...
    def GetDateGroupMethodOfRule(self, rule: VisualReporting.Rule) -> VisualReporting.Classifier.DateGroupMethodOption:
        ...
    def SetDateGroupMethodOfRule(self, rule: VisualReporting.Rule, dateGroupMethod: VisualReporting.Classifier.DateGroupMethodOption) -> None:
        ...
    def GetObjectTypesOfVisualReport(self) -> typing.List[VisualReporting.VisualReport.ObjectTypeOption]:
        ...
    def SetObjectTypesOfVisualReport(self, objectTypes: typing.List[VisualReporting.VisualReport.ObjectTypeOption]) -> None:
        ...
    BitmapNameOfReport: str
    BitmapNameOfReportingProperty: str
    CustomMessageOfReport: str
    CustomMessageOfReportingProperty: str
    DescriptionOfVisualReport: str
    DescriptiveCategoryOfVisualReport: str
    DestinationTeamcenterFolder: str
    FilenameOfVisualReport: str
    KeywordsOfVisualReport: str
    ReportContextOfVisualReport: VisualReporting.VisualReport.ReportContextOption
    ReportNameOfVisualReport: str
    ReportingObjectTypeOfVisualReport: VisualReporting.VisualReport.ReportingObjectTypeOption
    ReportingStyleOfVisualReport: VisualReporting.VisualReport.ReportingStyleOption
    SaveDestination: VisualReporting.VisualReport.SaveDestinationOption
    ScopeTypeOfVisualReport: VisualReporting.VisualReport.ScopeTypeOption


    class PropertyUsageOption(enum.Enum):
        Tooltip = 0
        InfoView = 1
        TooltipAndInfoView = 2
    

class VisualReport(NXObject):
    def __init__(self) -> None: ...
    def Save(self) -> None:
        ...
    def GetRule(self, index: int) -> VisualReporting.Rule:
        ...
    def GetRules(self) -> typing.List[VisualReporting.Rule]:
        ...
    def GetResultCategories(self) -> typing.List[VisualReporting.ResultCategory]:
        ...
    def GetGroupLabelsOfResultCategory(self, category: VisualReporting.ResultCategory) -> typing.List[VisualReporting.GroupLabel]:
        ...
    def GetGroupLabels(self) -> typing.List[VisualReporting.GroupLabel]:
        ...
    def GetObjectsInGroup(self, groupLabel: VisualReporting.GroupLabel) -> typing.List[NXObject]:
        ...
    def GetKeywords(self) -> str:
        ...
    def SetKeywords(self, keywords: str) -> None:
        ...
    def RemoveResultCategory(self, theCategory: VisualReporting.ResultCategory) -> None:
        ...
    def GetAllDefinedProperties(self) -> typing.List[VisualReporting.Property]:
        ...
    def GetPropertyValueOfObject(self, property: VisualReporting.Property, groupLabel: VisualReporting.GroupLabel, nxObject: NXObject) -> str:
        ...
    def GetObjectTypes(self) -> typing.List[VisualReporting.VisualReport.ObjectTypeOption]:
        ...
    BitmapName: str
    CustomMessage: str
    Description: str
    DescriptiveCategory: str
    DestinationTeamcenterFolder: str
    Filename: str
    IsUnmatchedGroupEnabled: bool
    ReportContext: VisualReporting.VisualReport.ReportContextOption
    ReportingObjectType: VisualReporting.VisualReport.ReportingObjectTypeOption
    ReportingStyle: VisualReporting.VisualReport.ReportingStyleOption
    SaveDestination: VisualReporting.VisualReport.SaveDestinationOption
    ScopeType: VisualReporting.VisualReport.ScopeTypeOption
    UnmatchedGroupLabel: VisualReporting.GroupLabel
    UnmatchedResultCategory: VisualReporting.UnmatchedResultCategory


    class ScopeTypeOption(enum.Enum):
        Component = 0
        SubPart = 1
    

    class SaveDestinationOption(enum.Enum):
        Local = 0
        Teamcenter = 1
    

    class ReportingStyleOption(enum.Enum):
        ColorObject = 0
        TagObject = 1
        ColorAndTagObject = 2
    

    class ReportingObjectTypeOption(enum.Enum):
        Part = 0
        Component = 1
        Inferred = 2
    

    class ReportContextOption(enum.Enum):
        Assembly = 0
        WorkPart = 1
    

    class ObjectTypeOption(enum.Enum):
        Body = 0
        Face = 1
    

class UnmatchedResultCategory(NXObject):
    def __init__(self) -> None: ...


class SpecifyDateBuilder(Builder):
    def __init__(self) -> None: ...
    Date: DateBuilder
    DateString: str
    RelativeDateString: str


class Rule(NXObject):
    def __init__(self) -> None: ...
    def GetClassifiers(self) -> typing.List[VisualReporting.Classifier]:
        ...
    def GetIsSmartGroupDateEnabled(self, classifier: VisualReporting.Classifier) -> bool:
        ...
    def SetIsSmartGroupDateEnabled(self, classifier: VisualReporting.Classifier, isSmartGroupDateEnabled: bool) -> None:
        ...
    ActiveClassifier: VisualReporting.Classifier
    FilterCondition: VisualReporting.Condition


class ResultCategory(NXObject):
    def __init__(self) -> None: ...
    BitmapName: str
    CustomMessage: str


class Property(NXObject):
    def __init__(self) -> None: ...
    BitmapName: str
    CustomMessage: str
    PropertyType: VisualReporting.Property.TypeOption
    SystemDatatype: VisualReporting.Property.DatatypeOption


    class TypeOption(enum.Enum):
        ArrangementSpecificPositionProperty = 0
        AttributeProperty = 1
        ComponentGroupProperty = 2
        ComponentNameProperty = 3
        DescriptivePartNameProperty = 4
        LoadStateProperty = 5
        MassKgProperty = 6
        MassLbProperty = 7
        ModifiedProperty = 8
        MultiCadProperty = 9
        PartNameProperty = 10
        PartUnitsProperty = 11
        PiecePartProperty = 12
        PositionProperty = 13
        PositionControlProperty = 14
        ReadOnlyProperty = 15
        ReferenceSetProperty = 16
        RootPartProperty = 17
        SuppressionControlProperty = 18
        WeightStatusProperty = 19
        TeamcenterProperty = 20
        ServerProperty = 21
        DegreesOfFreedomProperty = 22
        RuleEvaluationResultProperty = 23
        CheckMateResultProperty = 24
        LastModifiedDateProperty = 25
        RequirementsValidationStatusProperty = 26
        RepresentationProperty = 27
        LastModifiedUserProperty = 28
        ComponentProperty = 29
        MassGmProperty = 30
        PartFamilyMemberProperty = 31
        LinkedPartProperty = 32
        ProductTemplateProperty = 33
        BodyDensityProperty = 34
        BodyMassProperty = 35
        BodyRadiusGyrationProperty = 36
        BodySurfaceAreaProperty = 37
        BodyTypeProperty = 38
        BodyVolumeProperty = 39
        BodyWeightProperty = 40
        FaceAreaProperty = 41
        FaceTypeProperty = 42
        FaceMinRadiusProperty = 43
        FacePerimeterProperty = 44
        FacePMIFCFProperty = 45
        FacePMIFCFCharacteristicsProperty = 46
        FacePMIFCFCharFormTolProperty = 47
        FacePMIFCFCharLocationTolProperty = 48
        FacePMIFCFCharOrientationTolProperty = 49
        FacePMIFCFCharProfileTolProperty = 50
        FacePMIFCFCharRunoutTolProperty = 51
        FacePMIDatumFeatureProperty = 52
        FacePMIDatumTargetProperty = 53
        ObjectAttributeProperty = 54
        ObjectCreatedByUserProperty = 55
        ObjectCreatedDateProperty = 56
        ObjectCreatedVersionProperty = 57
        ObjectRefByWaveLinkProperty = 58
        ObjectWaveLinkedProperty = 59
        ObjectModifiedByUserProperty = 60
        ObjectModifiedDateProperty = 61
        ObjectModifiedVersionProperty = 62
        PartitionMembershipProperty = 63
        ComponentAddedDateProperty = 64
        TeamcenterObjectProperty = 65
        ComponentPatternTypeProperty = 66
        ObjectNameProperty = 67
        NXOpenProperty = 68
        SheetMetalBendAngleProperty = 69
        SheetMetalBendRadiusProperty = 70
        SheetMetalFaceTypeAllProperty = 71
        SheetMetalFaceTypeBendProperty = 72
        SheetMetalFaceTypeDeformProperty = 73
        SheetMetalFaceTypeWebProperty = 74
        SheetMetalNeutralFactorProperty = 75
        SheetMetalBodyTypeProperty = 76
        FeatureFailureProperty = 77
        MassIssueProperty = 78
        MassUpdateToggleStatusProperty = 79
        LastSavedVersionProperty = 80
        FlexiblePrintedCircuitDesignFaceTypeTopAndBottomProperty = 81
    

    class DatatypeOption(enum.Enum):
        String = 0
        Integer = 1
        Real = 2
        Boolean = 3
        Unknown = 4
        Null = 5
        Date = 6
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class GroupLabel(NXObject):
    def __init__(self) -> None: ...
    BitmapName: str
    Color: NXColor.Rgb
    CustomMessage: str
    DisplayStyle: VisualReporting.GroupLabel.DisplayStyleOption
    ErrorLevel: Validation.Result
    IsManual: bool
    IsNameUserSpecified: bool
    LowerBound: str
    TagPriority: VisualReporting.GroupLabel.TagPriorityOption
    UpperBound: str
    Value: str


    class TagPriorityOption(enum.Enum):
        Low = 0
        Medium = 1
        High = 2
    

    class DisplayStyleOption(enum.Enum):
        DeEmphasis = 0
        SpecifiedColor = 1
        OriginalColor = 2
        AutomaticColor = 3
    

class Condition(NXObject):
    def __init__(self) -> None: ...
    def IsChildCondition(self, childCondition: VisualReporting.Condition) -> bool:
        ...
    def GetChildCondition(self, index: int) -> VisualReporting.Condition:
        ...
    def GetChildConditions(self) -> typing.List[VisualReporting.Condition]:
        ...
    Datatype: VisualReporting.Property.DatatypeOption
    Description: str
    HasUserSpecifiedValue: bool
    OperatorType: VisualReporting.Condition.OperatorOption
    ParentCondition: VisualReporting.Condition
    Property: VisualReporting.Property
    Type: VisualReporting.Condition.TypeOption
    UserPrompt: str
    Value: str


    class TypeOption(enum.Enum):
        AndCondition = 0
        OrCondition = 1
        NotCondition = 2
        ValueCondition = 3
    

    class OperatorOption(enum.Enum):
        EqualOperator = 0
        LessThanOperator = 1
        NotLessThanOperator = 2
        GreaterThanOperator = 3
        NotGreaterThanOperator = 4
        NotEqualOperator = 5
        RegularExpressionOperator = 6
        ContainsOperator = 7
        DoesNotContainOperator = 8
        OnOrBeforeOperator = 9
        OnOrAfterOperator = 10
    

class Classifier(NXObject):
    def __init__(self) -> None: ...


    class TypeOption(enum.Enum):
        Simple = 0
        Value = 1
        Range = 2
    

    class RangeMethodOption(enum.Enum):
        Number = 0
        Percentage = 1
    

    class GroupingMethodOption(enum.Enum):
        Manual = 0
        Automatic = 1
        SemiAutomatic = 2
    

    class DateGroupMethodOption(enum.Enum):
        Day = 0
        Week = 1
        Month = 2
        Year = 3
    

