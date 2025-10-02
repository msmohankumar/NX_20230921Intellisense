from ....NXOpen import *
from ...CAE import *
from ..ModelCheck import *

import typing
import enum

class TestValueTypes(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...


    class Validator(enum.Enum):
        None = 0
        GreatThan = 1
        GreatThanOrEqual = 2
        SmallThan = 3
        SmallThanOrEqual = 4
    

    class TestType(enum.Enum):
        JacobianZero = 0
        JacobianRatio = 1
        JacobianSign = 2
        Volume = 3
        AxisymmetricY = 4
        AxisymmetricX = 5
        AspectRatio = 6
        SkewAngle = 7
        InteriorAngleMinimum = 8
        InteriorAngleMaximum = 9
        Taper = 10
        WarpFactor = 11
        FaceWarpCoefficient = 12
        EdgePointLengthRatio = 13
        EdgePointIncludedAngle = 14
        LengthRatioOffset = 15
        ParallelDeviation = 16
        ShapeFactor = 17
        Twist = 18
        LengthMinimum = 19
        LengthMaximum = 20
        TetCollapse = 21
        WarpageAngle = 22
        CohesiveElement = 23
        LaminateTaperRatio = 24
        LaminateThicknessRatio = 25
        Area = 26
    

    class Result(enum.Enum):
        Passed = 0
        Failed = 1
        Exception = 2
        NotApply = 3
        Warned = 4
    

    class TestValueTypesElementReference():
        ElementTypeName: str
        ElementPropertyName: str
        ElementPropertyValue: int
        def ToString(self) -> str:
            ...
        def __init__(self, ElementTypeName: str, ElementPropertyName: str, ElementPropertyValue: int) -> None: ...
    

    class CriteriaType(enum.Enum):
        Warning = 0
        Error = 1
    

    class TestValueTypes_ElementReference():
        elementTypeName: int
        elementPropertyName: int
        elementPropertyValue: int
    

class TestResult(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def HasTestValue(self) -> bool:
        ...
    TestType: CAE.ModelCheck.TestValueTypes.TestType
    TestValue: float
    ValidatedTestResult: CAE.ModelCheck.TestValueTypes.Result


class SolidElementFaceNormalBuilder(Builder):
    def __init__(self) -> None: ...
    def DisplayNormals(self) -> None:
        ...
    def ReorientLeftHandedElements(self) -> None:
        ...
    def CreateGroupOfLeftHandedElements(self) -> None:
        ...
    NegativeFaceColor: int
    PositiveFaceColor: int
    SelectionList: SelectTaggedObjectList
    CheckScopeOption: CAE.ModelCheck.CheckScope


class ReverseShellElementNormalBuilder(Builder):
    def __init__(self) -> None: ...
    def DisplayNormals(self) -> None:
        ...
    def ReverseNormals(self) -> typing.List[CAE.FEElement]:
        ...
    def CreateInconsistentElementEdgeGroup(self) -> CAE.CaeGroup:
        ...
    def CreateElementGroupOfSubdomains(self, ppSubdomainGroupTag: typing.List[NXObject]) -> None:
        ...
    DisplayType: CAE.ModelCheck.ReverseShellElementNormalBuilder.DisplayTypeValue
    NegativeFaceColor: int
    PositiveFaceColor: int
    SelectionList: SelectTaggedObjectList
    CheckScopeOption: CAE.ModelCheck.CheckScope


    class DisplayTypeValue(enum.Enum):
        Arrows = 0
        SolidFaceColors = 1
    

class ReverseBeamElementDirectionBuilder(Builder):
    def __init__(self) -> None: ...
    def DisplayDirections(self) -> None:
        ...
    def ReverseDirections(self) -> typing.List[CAE.FEElement]:
        ...
    SelectionList: SelectTaggedObjectList
    CheckScopeOption: CAE.ModelCheck.CheckScope


class QualityTestValue(NXObject):
    def __init__(self) -> None: ...
    def GetElementSpecificTestByIndex(self, index: int) -> CAE.ModelCheck.ElementSpecificTestValue:
        ...
    def GetTestType(self) -> CAE.ModelCheck.TestValueTypes.TestType:
        ...
    def GetValidator(self) -> CAE.ModelCheck.TestValueTypes.Validator:
        ...
    def HasCriteriaValue(self) -> bool:
        ...
    def GetCriteriaValue(self, criteriaType: CAE.ModelCheck.TestValueTypes.CriteriaType, criteriaValue: float) -> Unit:
        ...
    def SetCriteriaValue(self, criteriaType: CAE.ModelCheck.TestValueTypes.CriteriaType, criteriaValue: float, unit: Unit) -> None:
        ...
    def SetCriteriaValue(self, criteriaType: CAE.ModelCheck.TestValueTypes.CriteriaType, criteriaValue: str, unit: Unit) -> None:
        ...
    def GetIsSolverSpecificTest(self, isSystemTest: bool) -> bool:
        ...
    def GetElementReferences(self) -> typing.List[CAE.ModelCheck.TestValueTypes.ElementReference]:
        ...
    def ResetToCustomerDefault(self) -> None:
        ...
    ElementSpecificTestCount: int
    DoTest: bool


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class ModelSetupCheckBuilder(Builder):
    def __init__(self) -> None: ...
    def DoCheck(self) -> int:
        ...
    CheckAllComponents: bool
    CheckLabelConflicts: bool
    CheckUnconnectedComponent: bool
    IsDetailedMessage: bool
    ReportFileName: str


class ITestValue():
    def GetTestType(self) -> CAE.ModelCheck.TestValueTypes.TestType:
        ...
    def GetValidator(self) -> CAE.ModelCheck.TestValueTypes.Validator:
        ...
    def HasCriteriaValue(self) -> bool:
        ...
    def GetCriteriaValue(self, criteriaType: CAE.ModelCheck.TestValueTypes.CriteriaType, criteriaValue: float) -> Unit:
        ...
    def SetCriteriaValue(self, criteriaType: CAE.ModelCheck.TestValueTypes.CriteriaType, criteriaValue: float, unit: Unit) -> None:
        ...
    def SetCriteriaValue(self, criteriaType: CAE.ModelCheck.TestValueTypes.CriteriaType, criteriaValue: str, unit: Unit) -> None:
        ...
    def GetIsSolverSpecificTest(self, isSystemTest: bool) -> bool:
        ...
    def GetElementReferences(self) -> typing.List[CAE.ModelCheck.TestValueTypes.ElementReference]:
        ...
    def ResetToCustomerDefault(self) -> None:
        ...
    DoTest: bool


class ISelectionBuilder():
    CheckScopeOption: CAE.ModelCheck.CheckScope


class IElementQualityChecker(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetElementSize(self, pElem: CAE.FEElement, pMinSize: float, pMazSize: float, pAvgSize: float) -> None:
        ...
    def GetAspectRatio(self, pElem: CAE.FEElement) -> float:
        ...
    def GetCohesiveElementRatio(self, pElem: CAE.FEElement) -> float:
        ...
    def GetSkew(self, pElem: CAE.FEElement) -> float:
        ...
    def GetTaper(self, pElem: CAE.FEElement) -> float:
        ...
    def GetWarp(self, pElem: CAE.FEElement) -> float:
        ...
    def GetInteriorAngle(self, pElem: CAE.FEElement, pMinAngle: float, pMaxAngle: float) -> None:
        ...
    def GetJacobian(self, pElem: CAE.FEElement, pJacobianZero: float, pJacobianRatio: float, pJacobianSign: bool) -> None:
        ...
    def GetCollapse(self, pElem: CAE.FEElement) -> float:
        ...
    def GetTwist(self, pElem: CAE.FEElement) -> float:
        ...
    def GetEdgePointLengthRatioAndAngle(self, pElem: CAE.FEElement, pRatioValue: float, pAngleValue: float) -> None:
        ...
    def GetVolume(self, pElem: CAE.FEElement) -> float:
        ...
    def GetOffsetLengthRatio(self, pElem: CAE.FEElement) -> float:
        ...
    def GetConsistDistance(self, pElem: CAE.FEElement) -> float:
        ...
    def GetAxisRadius(self, pElem: CAE.FEElement) -> float:
        ...
    def GetParallelDeviation(self, pElem: CAE.FEElement) -> float:
        ...
    def GetShapeFactor(self, pElem: CAE.FEElement) -> float:
        ...
    def GetLaminateRatio(self, pElem: CAE.FEElement, matMatrix: Matrix3x3, stackAxis: int, totalPlyThick: float, lamEdgeRatio: float, lamThickRatio: float) -> None:
        ...
    def GetArea(self, pElem: CAE.FEElement) -> float:
        ...
    def FreeResource(self) -> None:
        ...


class FaceClearanceCheckBuilder(Builder):
    def __init__(self) -> None: ...
    def DoCheck(self) -> CAE.CaeGroup:
        ...
    Clearance: Expression


class ElementTestResult(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetTestResults(self) -> typing.List[CAE.ModelCheck.TestResult]:
        ...
    def GetTestElement(self) -> CAE.FEElement:
        ...
    OverallResult: CAE.ModelCheck.TestValueTypes.Result


class ElementSpecificTestValue(NXObject):
    def __init__(self) -> None: ...
    def GetTestType(self) -> CAE.ModelCheck.TestValueTypes.TestType:
        ...
    def GetValidator(self) -> CAE.ModelCheck.TestValueTypes.Validator:
        ...
    def HasCriteriaValue(self) -> bool:
        ...
    def GetCriteriaValue(self, criteriaType: CAE.ModelCheck.TestValueTypes.CriteriaType, criteriaValue: float) -> Unit:
        ...
    def SetCriteriaValue(self, criteriaType: CAE.ModelCheck.TestValueTypes.CriteriaType, criteriaValue: float, unit: Unit) -> None:
        ...
    def SetCriteriaValue(self, criteriaType: CAE.ModelCheck.TestValueTypes.CriteriaType, criteriaValue: str, unit: Unit) -> None:
        ...
    def GetIsSolverSpecificTest(self, isSystemTest: bool) -> bool:
        ...
    def GetElementReferences(self) -> typing.List[CAE.ModelCheck.TestValueTypes.ElementReference]:
        ...
    def ResetToCustomerDefault(self) -> None:
        ...
    DoTest: bool


class ElementQualitySettingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ModelCheck.ElementQualitySetting]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def GetElementQualitySetting(self, solverName: str) -> CAE.ModelCheck.ElementQualitySetting:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.ModelCheck.ElementQualitySetting:
        ...
    def Tag(self) -> Tag: ...



class ElementQualitySetting(NXObject):
    def __init__(self) -> None: ...
    def GetTestValueByIndex(self, index: int) -> CAE.ModelCheck.QualityTestValue:
        ...
    def GetTestValueByType(self, testType: CAE.ModelCheck.TestValueTypes.TestType) -> CAE.ModelCheck.QualityTestValue:
        ...
    def GetQualityValue(self, descriptorName: str) -> CAE.ModelCheck.ITestValue:
        ...
    def LocateTestDescriptorName(self, element: CAE.FEElement, testType: CAE.ModelCheck.TestValueTypes.TestType, useElemSpecific: bool) -> str:
        ...
    def ResetToCustomerDefault(self) -> None:
        ...
    LimitValueOption: CAE.ModelCheck.ElementQualitySetting.LimitValue
    TestValueCount: int
    UseElementSpecificValue: bool


    class LimitValue(enum.Enum):
        WarningAndErrorLimit = 0
        ErrorLimitOnly = 1
    

class ElementQualityCheckResults(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetTestSummary(self) -> typing.List[CAE.ModelCheck.ElementQualityCheckResults.TestSummary]:
        ...
    def GetElementTestResultByIndex(self, index: int) -> CAE.ModelCheck.ElementTestResult:
        ...
    ElementTestCount: int


    class ElementQualityCheckResultsTestSummary():
        TestType: CAE.ModelCheck.TestValueTypes.TestType
        WorstTestValue: float
        HasTestValue: bool
        TestCount: int
        ErrorCount: int
        WarnedCount: int
        def ToString(self) -> str:
            ...
    

class ElementQualityCheckBuilder(Builder):
    def __init__(self) -> None: ...
    def ExecuteCheck(self) -> CAE.ModelCheck.ElementQualityCheckResults:
        ...
    def WriteResultsToFile(self, outputFile: str, eqcResults: CAE.ModelCheck.ElementQualityCheckResults) -> None:
        ...
    def AttemptFixFailingElements(self, testTypes: typing.List[CAE.ModelCheck.TestValueTypes.TestType]) -> None:
        ...
    ElementReportFormat: CAE.ModelCheck.ElementQualityCheckBuilder.ReportFormat
    ElementsOutputOption: CAE.ModelCheck.ElementQualityCheckBuilder.OutputElements
    FailedElementsColor: NXColor
    NumberFormat: CAE.NumberFormat
    SelectionList: SelectTaggedObjectList
    ShowFailedElementsLabel: bool
    WarningElementsColor: NXColor
    CheckScopeOption: CAE.ModelCheck.CheckScope


    class ReportFormat(enum.Enum):
        None = 0
        Failed = 1
        Warning = 2
        FailedAndWarning = 3
        All = 4
    

    class OutputElements(enum.Enum):
        None = 0
        Failed = 1
        Warning = 2
        FailedAndWarning = 3
    

class ElementMaterialOrientationCheckBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCheckOrientation(self, orientationType: CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType) -> bool:
        ...
    def SetCheckOrientation(self, orientationType: CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType, checkOrientation: bool) -> None:
        ...
    def GetOrientationColor(self, orientationType: CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType) -> NXColor:
        ...
    def SetOrientationColor(self, orientationType: CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType, color: NXColor) -> None:
        ...
    def DoCheck(self, orientationType: typing.List[CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType], elements: typing.List[CAE.FEElement]) -> typing.List[Vector3d]:
        ...
    def GetArrowheadDisplayType(self) -> CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType:
        ...
    def SetArrowheadDisplayType(self, displayType: CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType) -> None:
        ...
    def GetSolidElementDisplayType(self) -> CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType:
        ...
    def SetSolidElementDisplayType(self, displayType: CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType) -> None:
        ...
    def GetCheckTranslucency(self) -> bool:
        ...
    def SetCheckTranslucency(self, checkOrientation: bool) -> None:
        ...
    def GetTranslucencyValue(self) -> int:
        ...
    def SetTranslucencyValue(self, translucencyValue: int) -> None:
        ...
    def GetArrowShowThrough(self) -> bool:
        ...
    def SetArrowShowThrough(self, arrowShowThrough: bool) -> None:
        ...
    SelectionList: SelectTaggedObjectList
    CheckScopeOption: CAE.ModelCheck.CheckScope


    class MaterialOrientationType(enum.Enum):
        Shell = 0
        SolidFirstDirection = 1
        SolidSecondDirection = 2
        SolidThirdDirection = 3
    

    class MaterialOrientationSolidElementDisplayType(enum.Enum):
        SolidAllElements = 0
        SolidExteriorElements = 1
    

    class MaterialOrientationArrowheadType(enum.Enum):
        ShowArrowHead = 0
        HideArrowHead = 1
    

class ElementEdgeCheckBuilder(Builder):
    def __init__(self) -> None: ...
    def HideInputMeshes(self, hideInputMeshes: bool) -> None:
        ...
    def ExecuteCheck(self, freeEdges: typing.List[CAE.FEElemEdge], nonManifoldEdges: typing.List[CAE.FEElemEdge]) -> None:
        ...
    def DoCheck(self, freeEdges: typing.List[CAE.FEElemEdge], nonManifoldEdges: typing.List[CAE.FEElemEdge], assoElems: typing.List[CAE.FEElement], outputGroup: CAE.CaeGroup) -> None:
        ...
    CheckFreeEdges: bool
    CheckNonManifoldEdges: bool
    ComputationScope: CAE.ModelCheck.ElementEdgeCheckBuilder.Scope
    FreeEdgeDisplayStyle: CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle
    NonManifoldEdgeDisplayStyle: CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle
    SelectionList: SelectTaggedObjectList
    CheckScopeOption: CAE.ModelCheck.CheckScope


    class Scope(enum.Enum):
        EntireModel = 0
        VisibleModel = 1
        SelectedModels = 2
    

    class ElementEdgeCheckBuilderEdgeDisplayStyle():
        Font: DisplayableObject.ObjectFont
        Width: DisplayableObject.ObjectWidth
        Color: NXColor
        def ToString(self) -> str:
            ...
        def __init__(self, Font: DisplayableObject.ObjectFont, Width: DisplayableObject.ObjectWidth, Color: NXColor) -> None: ...
    

    class ElementEdgeCheckBuilder_EdgeDisplayStyle():
        font: DisplayableObject.ObjectFont
        width: DisplayableObject.ObjectWidth
        color: int
    

class DuplicateNodesCheckBuilder(Builder):
    def __init__(self) -> None: ...
    def IdentifyDuplicateNodes(self) -> None:
        ...
    def GetDuplicateNodes(self, groupIndex: int) -> typing.List[CAE.FENode]:
        ...
    def MergeDuplicateNodes(self) -> None:
        ...
    DisplaySettingsData: CAE.ModelCheck.DuplicateNodesCheckBuilder.DisplaySettings
    DuplicateNodeGroupsCount: int
    IgnoreNodesConnectedToTinyEdges: bool
    IgnoreNodesInSameMesh: bool
    ListingType: CAE.ModelCheck.DuplicateNodesCheckBuilder.ListOption
    MergeOccurrenceNodes: bool
    Preference: CAE.ModelCheck.DuplicateNodesCheckBuilder.MergePreference
    SelectPreferenceNodesList: CAE.SelectFENodeList
    SelectionList: SelectTaggedObjectList
    Tolerance: Expression
    CheckScopeOption: CAE.ModelCheck.CheckScope


    class MergePreference(enum.Enum):
        None = 0
        KeepHighLabel = 1
        KeepLowLabel = 2
        KeepSelected = 3
        RemoveSelected = 4
    

    class ListOption(enum.Enum):
        All = 0
        Mergeable = 1
        Unmergeable = 2
    

    class DuplicateNodesCheckBuilderDisplaySettings():
        ShowDuplicateNodes: bool
        ShowMergedNodeLabels: bool
        ShowRetainedNodeLabels: bool
        KeepNodesColor: NXColor
        MergeNodesColor: NXColor
        UnableToMergeNodesColor: NXColor
        def ToString(self) -> str:
            ...
    

    class DuplicateNodesCheckBuilder_DisplaySettings():
        showDuplicateNodes: bool
        showMergedNodeLabels: bool
        showRetainedNodeLabels: bool
        keepNodesColor: int
        mergeNodesColor: int
        unableToMergeNodesColor: int
    

class DuplicateElementsCheckBuilder(Builder):
    def __init__(self) -> None: ...
    def IdentifyDuplicateElements(self) -> None:
        ...
    def GetDuplicateElements(self, groupIndex: int) -> typing.List[CAE.FEElement]:
        ...
    def DeleteDuplicateElements(self) -> None:
        ...
    DisplaySettingsData: CAE.ModelCheck.DuplicateElementsCheckBuilder.DisplaySettings
    DuplicateElementGroupsCount: int
    Preference: CAE.ModelCheck.DuplicateElementsCheckBuilder.DeletePreference
    PreferenceElements: CAE.SelectElementsBuilder
    SelectionList: SelectTaggedObjectList
    CheckScopeOption: CAE.ModelCheck.CheckScope


    class DuplicateElementsCheckBuilderDisplaySettings():
        ShowDuplicateElements: bool
        ShowElementLabels: bool
        ElementsColor: NXColor
        ElementsWidth: DisplayableObject.ObjectWidth
        def ToString(self) -> str:
            ...
    

    class DeletePreference(enum.Enum):
        KeepHighLabel = 0
        KeepLowLabel = 1
        KeepSelected = 2
        RemoveSelected = 3
    

    class DuplicateElementsCheckBuilder_DisplaySettings():
        showDuplicateElements: bool
        showElementLabels: bool
        elementsColor: int
        elementsWidth: DisplayableObject.ObjectWidth
    

class CorrectBeamElementsBuilder(Builder):
    def __init__(self) -> None: ...
    def IdentifyFailedElements(self, failedElement: typing.List[CAE.FEElement]) -> None:
        ...
    def DeleteDanglingNodesInElements(self, failedElement: typing.List[CAE.FEElement]) -> None:
        ...
    def DeleteFailedElements(self, failedElement: typing.List[CAE.FEElement]) -> None:
        ...
    def CorrectFailedElements(self, failedElement: CAE.FEElement, nodeToReplace: CAE.FENode, replacementNode: CAE.FENode) -> None:
        ...
    ElemCheckOption: CAE.ModelCheck.CorrectBeamElementsBuilder.ElementToCheck
    ElementSelection: CAE.SelectElementsBuilder
    NodeToReplace: CAE.SelectFENodeList
    ReplacementNode: CAE.SelectFENodeList
    CheckScopeOption: CAE.ModelCheck.CheckScope


    class ElementToCheck(enum.Enum):
        Displayed = 0
        Selected = 1
    

class CheckScope(enum.Enum):
    Displayed = 0
    Selected = 1


class AlignShellElementNormalBuilder(Builder):
    def __init__(self) -> None: ...
    def FindAllVisibleConnectedElements(self) -> typing.List[CAE.FEElement]:
        ...
    def DisplayNormals(self) -> None:
        ...
    def AlignNormals(self) -> typing.List[CAE.FEElement]:
        ...
    ElementConnectScope: CAE.ModelCheck.AlignShellElementNormalBuilder.ConnectedElementScope
    ElementSelectionList: SelectTaggedObjectList
    OrientMethod: CAE.ModelCheck.AlignShellElementNormalBuilder.OrientMethodType
    ReverseSeedNormal: bool
    SeedElement: CAE.FEElement
    UserSpecifiedConnectElements: CAE.SelectElementsBuilder
    CheckScopeOption: CAE.ModelCheck.CheckScope


    class OrientMethodType(enum.Enum):
        UsingSeedElement = 0
        Automatic = 1
    

    class ConnectedElementScope(enum.Enum):
        SeedMesh = 0
        AllVisible = 1
        UserSpecified = 2
    

class AlignShellElementFirstEdgeBuilder(Builder):
    def __init__(self) -> None: ...
    def DisplayFirstEdges(self) -> None:
        ...
    Direction: bool
    ElemSelectionMethod: CAE.ModelCheck.AlignShellElementFirstEdgeBuilder.ElemSelectionMode
    Elements: CAE.SelectElementsBuilder
    SeedEdge: CAE.SelectElementsBuilder


    class ElemSelectionMode(enum.Enum):
        ConnectedElementsinSeedMesh = 0
        AllVisibleConnectedShellElements = 1
        SelectedConnectedElements = 2
    

class AlignBeamElementDirectionBuilder(Builder):
    def __init__(self) -> None: ...
    def FindAllVisibleConnectedElements(self) -> typing.List[CAE.FEElement]:
        ...
    def DisplayDirections(self) -> None:
        ...
    def AlignDirections(self) -> typing.List[CAE.FEElement]:
        ...
    ElementConnectScope: CAE.ModelCheck.AlignBeamElementDirectionBuilder.ConnectedElementScope
    ReverseSeedDirection: bool
    SeedElement: CAE.FEElement
    UserSpecifiedConnectElements: CAE.SelectElementsBuilder


    class ConnectedElementScope(enum.Enum):
        SeedMesh = 0
        AllVisible = 1
        UserSpecified = 2
    

