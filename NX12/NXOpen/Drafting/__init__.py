from ...NXOpen import *
from ..Drafting import *

import typing
import enum

class SpecifyRuleBuilder(Builder):
    def __init__(self) -> None: ...
    Note: Annotations.Note
    Rule: str


class SmashDrawingViewBuilder(Builder):
    def __init__(self) -> None: ...
    SelectView: Drawings.SelectDraftingView


class SettingsManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreatePreferencesBuilder(self) -> Drafting.PreferencesBuilder:
        ...
    def CreateAnnotationEditSettingsBuilder(self, objects: typing.List[DisplayableObject]) -> Annotations.EditSettingsBuilder:
        ...
    def CreateDrawingEditSectionLineSettingsBuilder(self, sectionLines: typing.List[Drawings.SectionLine]) -> Drawings.EditSectionLineSettingsBuilder:
        ...
    def CreateDrawingEditViewSettingsBuilder(self, views: typing.List[View]) -> Drawings.EditViewSettingsBuilder:
        ...
    def CreateLayout2dEditComponentSettingsBuilder(self, components: typing.List[Layout2d.Component]) -> Layout2d.EditComponentSettingsBuilder:
        ...
    def CreateDrawingEditViewLabelSettingsBuilder(self, viewLabels: typing.List[DisplayableObject]) -> Drawings.EditViewLabelSettingsBuilder:
        ...
    def CreateTableEditSettingsBuilder(self, objects: typing.List[DisplayableObject]) -> Annotations.TableEditSettingsBuilder:
        ...
    def ProcessForMutipleObjectsSettings(self, editSettingsBuilders: typing.List[Drafting.BaseEditSettingsBuilder]) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use Drafting.SettingsManager.ProcessForMultipleObjectsSettings instead.")"""
        ...
    def ProcessForMultipleObjectsSettings(self, editSettingsBuilders: typing.List[Drafting.BaseEditSettingsBuilder]) -> None:
        ...
    def Tag(self) -> Tag: ...



class RulesBuilder(Builder):
    def __init__(self) -> None: ...
    DimensionRule: str
    NoteRule: str
    SymbolRule: str


class PrimaryContentItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Drafting.PrimaryContentItemBuilder]) -> None:
        ...
    def Append(self, object: Drafting.PrimaryContentItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Drafting.PrimaryContentItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Drafting.PrimaryContentItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Drafting.PrimaryContentItemBuilder) -> None:
        ...
    def Erase(self, obj: Drafting.PrimaryContentItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Drafting.PrimaryContentItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Drafting.PrimaryContentItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Drafting.PrimaryContentItemBuilder, object2: Drafting.PrimaryContentItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Drafting.PrimaryContentItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PrimaryContentItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Content: Assemblies.SelectComponentList
    GeometryTemplate: str


class PreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObjects(self, selectedObject: NXObject) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    AnnotationStyle: Annotations.StyleBuilder
    AssemblyCreationSettingsBuilder: Layout2d.AssemblyCreationSettingsBuilder
    AutomationBooklet: Drawings.AutomationBookletBuilder
    AutomationRule: Drafting.AutomationRuleBuilder
    AutomationTemplateRegion: Drawings.AutomationTemplateRegionBuilder
    BendTable: Annotations.BendTableSettingsBuilder
    BorderAndZoneStyle: Drawings.BorderAndZoneStyleBuilder
    CommonWorkflow: Annotations.CommonWorkflowBuilder
    Component2dSettings: Layout2d.ComponentSettingsBlockBuilder
    CreateComponentFrom3DSettingsBuilder: Layout2d.CreateComponentFrom3DSettingsBuilder
    DimensionWorkflow: Annotations.DimensionWorkflowBuilder
    DrawingFormatTitle: Annotations.DrawingFormatTitleBuilder
    DrawingFormatsheet: Drawings.DrawingFormatSheetBuilder
    FramebarGeneral: Annotations.ShipDraftingFramebarGeneralBuilder
    GeneralLayoutPreferencesBuilder: Layout2d.GeneralPreferencesBuilder
    HoleTableContent: Annotations.HoleTableSettingsContentBuilder
    HoleTableFormat: Annotations.HoleTableSettingsFormatBuilder
    HoleTableHoleFilters: Annotations.HoleTableSettingsHoleFiltersBuilder
    HoleTableLabel: Annotations.HoleTableSettingsLabelBuilder
    HoleTableWorkflow: Annotations.HoleTableSettingsWorkflowBuilder
    PartsList: Annotations.PartsListBuilder
    RetainedAnnotations: Annotations.RetainedAnnotationsBuilder
    SymbolWorkflow: Annotations.SymbolWorkflowBuilder
    TableCellStyle: Annotations.TableCellStyleBuilder
    TableSection: Annotations.TableSectionStyleBuilder
    TabularNoteStyle: Annotations.TabularNoteStyleBuilder
    TrackDrawingChangesGeneral: Drawings.TrackDrawingChangesGeneralBuilder
    TrackDrawingChangesReportFilter: Drawings.TrackDrawingChangesReportFilterBuilder
    ViewBreak: Drawings.ViewBreakBuilder
    ViewCommonViewLabel: Drawings.ViewCommonViewLabelBuilder
    ViewDetailLabel: Drawings.ViewDetailLabelBuilder
    ViewLabel: Drawings.ViewLabelBuilder
    ViewProjectedLabel: Drawings.ViewProjectedLabelBuilder
    ViewSectionLabel: Drawings.ViewSectionLabelBuilder
    ViewSectionLine: Drawings.ViewSectionLineBuilder
    ViewStyle: Drawings.ViewStyleBuilder
    ViewWorkflow: Drawings.ViewWorkflowBuilder
    VisualDrawingCompare: Drawings.VisualDrawingComparePrefsBuilder
    Workflow: Drawings.GeneralWorkFlowBuilder


class MoveToDrawingViewBuilder(Builder):
    def __init__(self) -> None: ...
    SelectObjects: SelectTaggedObjectList
    SelectPoint: Point
    TwoDOrientation: Drawings.View2dOrientBuilder
    ViewScale: Drawings.ViewScaleBuilder
    ViewStyle: Drawings.ViewStyleBuilder
    XCoordinate: float
    YCoordinate: float


class DrawingCreationWizardBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSummary(self) -> str:
        ...
    def SetSummary(self, summary: str) -> None:
        ...
    def SetObjectCreateBuilder(self, objectCreateBuilder: PDM.ObjectCreateBuilder) -> None:
        ...
    ApplyTemplateToAll: bool
    Attributes: Drafting.AttributeItemBuilderList
    DetailID: str
    Discipline: str
    DrawingStyle: str
    ExcludedContent: Assemblies.SelectComponentList
    Folder: str
    IntroductoryTemplate: str
    Name: str
    Number: str
    PrimaryContent: Drafting.PrimaryContentItemBuilderList
    References: SelectNXObjectList
    Revision: str
    SecondaryContent: Assemblies.SelectComponentList


class DrawingAutomationWizard(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Builder: Drafting.DrawingCreationWizardBuilder
    ContinueProcessing: bool
    ErrorCode: int
    Part: Part


class DraftingApplicationManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateCutCopyPasteBuilder(self) -> Drafting.CutCopyPasteBuilder:
        ...
    def CreateMoveToDrawingViewBuilder(self) -> Drafting.MoveToDrawingViewBuilder:
        ...
    def CreateSmashDrawingViewBuilder(self) -> Drafting.SmashDrawingViewBuilder:
        ...
    def Tag(self) -> Tag: ...

    TitleBlocks: Annotations.TitleBlockCollection


class DistributeAnnotationsBuilder(Builder):
    def __init__(self) -> None: ...
    Views: Drawings.SelectDraftingViewList


class CutCopyPasteLeaderBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetMoveOnCommit(self, rot: Matrix3x3, trans: Vector3d) -> None:
        ...
    def Validate(self) -> bool:
        ...
    DestinationView: View
    IsLeaderSelection: bool
    LeaderSelection: SelectTaggedObject
    ReassociateLeader: bool
    Selection: SelectTaggedObject


class CutCopyPasteBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDefaultToPoint(self) -> Point3d:
        ...
    def SetDefaultToPoint(self, dropLocation: Point3d) -> None:
        ...
    def SetMoveOnCommit(self, rot: Matrix3x3, trans: Vector3d) -> None:
        ...
    def InitPaste(self) -> None:
        ...
    CutCopyPasteLeader: Drafting.CutCopyPasteLeaderBuilder
    DestinationView: View
    ObjectsToCopy: SelectTaggedObjectList
    Originals: Drafting.CutCopyPasteBuilder.TypeOperation
    OutputObjects: SelectTaggedObjectList
    PasteType: Drafting.CutCopyPasteBuilder.TypePaste
    PlaneToRestrictMotion: Plane
    Transform: GeometricUtilities.ModlMotion


    class TypePaste(enum.Enum):
        Transform = 0
        Tracking = 1
    

    class TypeOperation(enum.Enum):
        Copy = 0
        Cut = 1
    

class BaseEditSettingsBuilder(Builder):
    def __init__(self) -> None: ...


class AutomationRuleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetRulesList(self) -> str:
        ...
    def SetRulesList(self, rules: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AllowInsideGeometry: bool
    EqualDimensionTolerance: float
    HideFeetAndInchMarks: bool
    Increment: float
    LowerThreshold: float
    MaximumGapToGeometry: float
    MinimumGapBetweenAnnotations: float
    MinimumGapToGeometry: float
    ReferenceGeometryGapTolerance: float
    RoundFeetAndInches: bool
    UseFeetInchesAndFraction: bool


class AutomationPreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    def GetRulesList(self) -> str:
        ...
    def SetRulesList(self, rules: str) -> None:
        ...
    AllowFeetInchFractionForDimensionGreaterThan: bool
    AllowInchFractionToNearest: bool
    AnnotationInsideGeometry: bool
    DisplayRegion: bool
    DisplayRegionLabel: bool
    DistanceBetweenAnnotations: float
    EqualDimensionCompareTolerance: float
    FeetInchFractionForDimensionGreaterThan: float
    HideFeetInchMark: bool
    InchFractionToNearest: float
    MaximumDistanceToGeometry: float
    MinimumDistanceToGeometry: float
    ReferenceGeometrySearchDistance: float
    RegionColor: NXColor
    RegionFont: Preferences.PartDrafting.FontType
    RegionWidth: Preferences.PartDrafting.WidthType
    SecondaryContentHiddenLineColor: NXColor
    SecondaryContentHiddenLineFont: Preferences.PartDrafting.FontType
    SecondaryContentHiddenLineWidth: Preferences.PartDrafting.WidthType
    SecondaryContentVisibleLineColor: NXColor
    SecondaryContentVisibleLineFont: Preferences.PartDrafting.FontType
    SecondaryContentVisibleLineWidth: Preferences.PartDrafting.WidthType


class AutomationManager(Utilities.NXRemotableObject):
    def __init__(self, owner: DraftingManager) -> None: ...
    def CreatePrimaryContentItemBuilder(self) -> Drafting.PrimaryContentItemBuilder:
        ...
    def CreateAttributeItemBuilder(self) -> Drafting.AttributeItemBuilder:
        ...
    def CreateDrawingCreationWizardBuilder(self, isEditing: bool) -> Drafting.DrawingCreationWizardBuilder:
        ...
    def CreateDrawingCreationWizardBuilderFromRule(self, className: str) -> Drafting.DrawingCreationWizardBuilder:
        ...
    def CreatePreferencesBuilder(self) -> Drafting.AutomationPreferencesBuilder:
        ...
    def CreateAnnotateViewsBuilder(self) -> Drafting.AnnotateViewsBuilder:
        ...
    def CreateRulesBuilder(self) -> Drafting.RulesBuilder:
        ...
    def CreateSpecifyRuleBuilder(self) -> Drafting.SpecifyRuleBuilder:
        ...
    def CreateDistributeAnnotationsBuilder(self) -> Drafting.DistributeAnnotationsBuilder:
        ...
    def GetRemainingPartsOfBooklet(self, remainingParts: typing.List[Part], remainingPartFileSpecs: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    DrawingRegions: Drawings.DrawingRegionCollection


class AttributeItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Drafting.AttributeItemBuilder]) -> None:
        ...
    def Append(self, object: Drafting.AttributeItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Drafting.AttributeItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Drafting.AttributeItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Drafting.AttributeItemBuilder) -> None:
        ...
    def Erase(self, obj: Drafting.AttributeItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Drafting.AttributeItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Drafting.AttributeItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Drafting.AttributeItemBuilder, object2: Drafting.AttributeItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Drafting.AttributeItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class AttributeItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Title: str
    Value: str


class AnnotateViewsBuilder(Builder):
    def __init__(self) -> None: ...
    ExistingAutomaticAnnotationOption: Drafting.AnnotateViewsBuilder.ExistingAutomaticAnnotation
    Views: Drawings.SelectDraftingViewList


    class ExistingAutomaticAnnotation(enum.Enum):
        Delete = 0
        Preserve = 1
    

