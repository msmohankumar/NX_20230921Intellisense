from ...NXOpen import *
from ..BlockStyler import *

import typing
import enum

class Wizard(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def CreateStepSubNode(self, step: int, text: str, bitmap: str, showCheckBox: bool, checkBoxChecked: bool) -> int:
        ...
    def RemoveStepSubNode(self, subNodeId: int) -> None:
        ...
    def CreateMenu(self) -> BlockStyler.TreeListMenu:
        ...
    def SetMenu(self, menu: BlockStyler.TreeListMenu) -> None:
        ...
    def SetStepNotifyPreHandler(self, cb: BlockStyler.Wizard.StepNotifyPreCallback) -> None:
        ...
    def SetStepNotifyPostHandler(self, cb: BlockStyler.Wizard.StepNotifyPostCallback) -> None:
        ...
    def SetIsStepOkayHandler(self, cb: BlockStyler.Wizard.IsStepOkayCallback) -> None:
        ...
    def SetOnSubNodeHandler(self, cb: BlockStyler.Wizard.OnSubNodeCallback) -> None:
        ...
    def SetOnMenuHandler(self, cb: BlockStyler.Wizard.OnMenuCallback) -> None:
        ...
    def SetOnMenuSelectionHandler(self, cb: BlockStyler.Wizard.OnMenuSelectionCallback) -> None:
        ...
    def GetStepBannerBitmaps(self) -> str:
        ...
    def SetStepBannerBitmaps(self, bitmaps: str) -> None:
        ...
    def GetStepBitmaps(self) -> str:
        ...
    def SetStepBitmaps(self, bitmaps: str) -> None:
        ...
    def GetStepCues(self) -> str:
        ...
    def SetStepCues(self, cues: str) -> None:
        ...
    def GetStepText(self) -> str:
        ...
    def SetStepText(self, text: str) -> None:
        ...
    CurrentStep: int
    HighQualityBitmap: bool
    Localize: bool
    Members: BlockStyler.PropertyList
    ShowTaskNavigator: bool


    class TaskNavigatorItem(enum.Enum):
        Step = 0
        SubNode = 1
        Background = 2
    

    class SubNodeAction(enum.Enum):
        Select = 0
        Deselect = 1
        Check = 2
        Uncheck = 3
    

    

    

    

    

    

    

class UIBlock(TaggedObject):
    def __init__(self) -> None: ...
    def GetProperties(self) -> BlockStyler.PropertyList:
        ...
    def Focus(self) -> None:
        ...
    Enable: bool
    Expanded: bool
    Group: bool
    Label: str
    Name: str
    Show: bool
    Type: str


class TreeListMenu(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def AddMenuItem(self, menuItemID: int, menuItemText: str) -> None:
        ...
    def AddMenuItem(self, menuItemID: int, menuItemText: str, icon: str) -> None:
        ...
    def AddSeperator(self) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use BlockStyler.TreeListMenu.AddSeparator instead.")"""
        ...
    def AddSeparator(self) -> None:
        ...
    def SetSubMenu(self, menuItemID: int, subMenu: BlockStyler.TreeListMenu) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    def GetItemChecked(self, menuItemID: int) -> bool:
        ...
    def SetItemChecked(self, menuItemID: int, checkedStatusStatus: bool) -> None:
        ...
    def GetItemDisable(self, menuItemID: int) -> bool:
        ...
    def SetItemDisable(self, menuItemID: int, disableStatus: bool) -> None:
        ...
    def GetItemDefault(self, menuItemID: int) -> bool:
        ...
    def SetItemDefault(self, menuItemID: int, defaultStatus: bool) -> None:
        ...
    def GetItemHidden(self, menuItemID: int) -> bool:
        ...
    def SetItemHidden(self, menuItemID: int, hiddenStatus: bool) -> None:
        ...
    def GetItemDialogLaunching(self, menuItemID: int) -> bool:
        ...
    def SetItemDialogLaunching(self, menuItemID: int, dialogLaunchingStaus: bool) -> None:
        ...
    def GetItemIcon(self, menuItemID: int) -> str:
        ...
    def SetItemIcon(self, menuItemID: int, icon: str) -> None:
        ...
    def GetItemText(self, menuItemID: int) -> str:
        ...
    def SetItemText(self, menuItemID: int, text: str) -> None:
        ...


class Tree(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def CreateNode(self, displayText: str) -> BlockStyler.Node:
        ...
    def InsertNode(self, newNode: BlockStyler.Node, parentNode: BlockStyler.Node, afterNode: BlockStyler.Node, nodeInsertOption: BlockStyler.Tree.NodeInsertOption) -> None:
        ...
    def DeleteNode(self, node: BlockStyler.Node) -> None:
        ...
    def SelectNode(self, node: BlockStyler.Node, isSelect: bool, isOtherNodeAffected: bool) -> None:
        ...
    def SelectNodes(self, node: typing.List[BlockStyler.Node], isSelect: bool, isOtherNodeAffected: bool) -> None:
        ...
    def InsertColumn(self, columnID: int, columnTitle: str, columnWidth: int) -> int:
        ...
    def GetColumnTitle(self, columnID: int) -> str:
        ...
    def SetColumnTitle(self, columnID: int, columnHeaderTitle: str) -> None:
        ...
    def GetColumnId(self, columnPosition: int) -> int:
        ...
    def GetColumnPosition(self, columnID: int) -> int:
        ...
    def GetColumnWidth(self, columnID: int) -> int:
        ...
    def SetColumnWidth(self, columnID: int, columnWidth: int) -> None:
        ...
    def GetColumnSortOption(self, columnID: int) -> BlockStyler.Tree.ColumnSortOption:
        ...
    def SetColumnSortOption(self, columnID: int, sortOption: BlockStyler.Tree.ColumnSortOption) -> None:
        ...
    def GetColumnSortable(self, columnID: int) -> bool:
        ...
    def SetColumnSortable(self, columnID: int, isSortable: bool) -> None:
        ...
    def GetColumnVisible(self, columnID: int) -> bool:
        ...
    def SetColumnVisible(self, columnID: int, isVisible: bool) -> None:
        ...
    def GetColumnDisplayType(self, columnID: int) -> BlockStyler.Tree.ColumnDisplay:
        ...
    def SetColumnDisplayType(self, columnID: int, displayType: BlockStyler.Tree.ColumnDisplay) -> None:
        ...
    def GetColumnResizePolicy(self, columnID: int) -> BlockStyler.Tree.ColumnResizePolicy:
        ...
    def SetColumnResizePolicy(self, columnID: int, resizePolicy: BlockStyler.Tree.ColumnResizePolicy) -> None:
        ...
    def SetPreSelectionTimeOut(self, timeOut: float) -> None:
        ...
    def GetSelectedNodes(self) -> typing.List[BlockStyler.Node]:
        ...
    def Redraw(self, redraw: bool) -> None:
        ...
    def SetOnExpandHandler(self, cb: BlockStyler.Tree.OnExpandCallback) -> None:
        ...
    def SetOnInsertColumnHandler(self, cb: BlockStyler.Tree.OnInsertColumnCallback) -> None:
        ...
    def SetStateIconNameHandler(self, cb: BlockStyler.Tree.StateIconNameCallback) -> None:
        ...
    def SetOnInsertNodeHandler(self, cb: BlockStyler.Tree.OnInsertNodeCallback) -> None:
        ...
    def SetOnPreSelectHandler(self, cb: BlockStyler.Tree.OnPreSelectCallback) -> None:
        ...
    def SetOnDeleteNodeHandler(self, cb: BlockStyler.Tree.OnDeleteNodeCallback) -> None:
        ...
    def SetOnSelectHandler(self, cb: BlockStyler.Tree.OnSelectCallback) -> None:
        ...
    def SetOnStateChangeHandler(self, cb: BlockStyler.Tree.OnStateChangeCallback) -> None:
        ...
    def SetToolTipTextHandler(self, cb: BlockStyler.Tree.ToolTipTextCallback) -> None:
        ...
    def SetColumnSortHandler(self, cb: BlockStyler.Tree.ColumnSortCallback) -> None:
        ...
    def SetOnBeginLabelEditHandler(self, cb: BlockStyler.Tree.OnBeginLabelEditCallback) -> None:
        ...
    def SetOnEndLabelEditHandler(self, cb: BlockStyler.Tree.OnEndLabelEditCallback) -> None:
        ...
    def SetAskEditControlHandler(self, cb: BlockStyler.Tree.AskEditControlCallback) -> None:
        ...
    def SetEditOptions(self, stringArray: str, defaultIndex: int) -> None:
        ...
    def SetOnEditOptionSelectedHandler(self, cb: BlockStyler.Tree.OnEditOptionSelectedCallback) -> None:
        ...
    def SetOnMenuHandler(self, cb: BlockStyler.Tree.OnMenuCallback) -> None:
        ...
    def SetOnMenuSelectionHandler(self, cb: BlockStyler.Tree.OnMenuSelectionCallback) -> None:
        ...
    def SetIsDragAllowedHandler(self, cb: BlockStyler.Tree.IsDragAllowedCallback) -> None:
        ...
    def SetIsDropAllowedHandler(self, cb: BlockStyler.Tree.IsDropAllowedCallback) -> None:
        ...
    def SetOnDropHandler(self, cb: BlockStyler.Tree.OnDropCallback) -> None:
        ...
    def SetOnDropMenuHandler(self, cb: BlockStyler.Tree.OnDropMenuCallback) -> None:
        ...
    def SetOnDefaultActionHandler(self, cb: BlockStyler.Tree.OnDefaultActionCallback) -> None:
        ...
    def CreateMenu(self) -> BlockStyler.TreeListMenu:
        ...
    def SetMenu(self, menu: BlockStyler.TreeListMenu) -> None:
        ...
    def CopyNode(self, sourceNode: BlockStyler.Node) -> BlockStyler.Node:
        ...
    def GetSelectionModeMembers(self) -> str:
        ...
    CanStretchHeight: bool
    CanStretchWidth: bool
    FirstSelectedNode: BlockStyler.Node
    Height: int
    Localize: bool
    MaximumHeight: int
    MaximumWidth: int
    MinimumHeight: int
    MinimumWidth: int
    NumberOfColumns: int
    RootNode: BlockStyler.Node
    ScrollFrozenColumn: int
    ScrollLineNumber: int
    SelectionModeAsString: str
    ShowExpandCollapseMarker: bool
    ShowHeader: bool
    ShowMultipleColumns: bool
    ShowToolTips: bool
    SortRootNodes: bool
    Width: int


    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    class NodeInsertOption(enum.Enum):
        First = 0
        Last = 1
        Sort = 2
        AlwaysFirst = 3
        AlwaysLast = 4
    

    

    

    class EndLabelEditState(enum.Enum):
        AcceptText = 0
        RejectText = 1
    

    class EditControlOption(enum.Enum):
        Accept = 0
        Reject = 1
    

    class ControlType(enum.Enum):
        None = 0
        ComboBox = 1
        ListBox = 2
    

    class ColumnSortOption(enum.Enum):
        Unsorted = 0
        Ascending = 1
        Descending = 2
    

    

    class ColumnResizePolicy(enum.Enum):
        ConstantWidth = 0
        ResizeWithContents = 1
        ResizeWithTree = 2
    

    class ColumnDisplay(enum.Enum):
        Text = 0
        Icon = 1
    

    class BeginLabelEditState(enum.Enum):
        Allow = 0
        Disallow = 1
    

    

class Toggle(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    BalloonTooltipLayoutAsString: str
    BalloonTooltipOffImage: str
    BalloonTooltipOffText: str
    BalloonTooltipOnImage: str
    BalloonTooltipOnText: str
    Bitmap: str
    BitmapOnly: bool
    Localize: bool
    RetainValue: bool
    Value: bool


class TextColorFontWidth(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetColorValue(self) -> int:
        ...
    def SetColorValue(self, colorValueVector: int) -> None:
        ...
    def IsNxFont(self) -> bool:
        ...
    AvailableFontTypesAsString: str
    FontValue: str
    LayoutAsString: str
    StandardFontStyle: str
    WidthValueAsString: str


class Table(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    HasColumnLabels: bool
    HighQualityBitmap: bool
    Localize: bool
    Members: BlockStyler.PropertyList
    NumberOfColumns: int
    RetainValue: bool


class TabControl(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetHiddenTabPages(self) -> int:
        ...
    def SetHiddenTabPages(self, hiddenTabs: int) -> None:
        ...
    ActivePage: int
    HighQualityBitmap: bool
    Localize: bool
    Members: BlockStyler.PropertyList
    RetainValue: bool
    TabsPerRow: int


class SuperSection(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetInterpartSelectionMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    def GetDefaultCurveRulesMembers(self) -> str:
        ...
    AllowConvergentObject: bool
    AllowInferredCurveSelection: bool
    AllowStopAtIntersectionFollowFillet: bool
    AngularTolerance: float
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    BlendVirtualCurveOverlay: bool
    ChainWithinFeature: bool
    CreateInterpartLink: bool
    Cue: str
    CurveRules: int
    DefaultCurveRulesAsString: str
    EntityType: int
    FollowFillet: bool
    InferredCurveSelection: bool
    InterpartSelectionAsString: str
    LabelString: str
    PointOverlay: bool
    ShowFlowDirectionAndOriginCurve: bool
    SketchOnPath: bool
    SmartUpdateOptionAsString: str
    SnapPointTypesEnabled: int
    SnapPointTypesOnByDefault: int
    StepStatusAsString: str
    StopAtIntersection: bool
    ToolTip: str


class SuperPoint(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetInterpartSelectionMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    def GetDefaultCurveRulesMembers(self) -> str:
        ...
    AllowConvergentObject: bool
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    BlendVirtualCurveOverlay: bool
    CreateInterpartLink: bool
    Cue: str
    CurveRules: int
    DefaultCurveRulesAsString: str
    EntityType: int
    InterpartSelectionAsString: str
    LabelString: str
    PointOverlay: bool
    ShowFlowDirectionAndOriginCurve: bool
    SketchOnPath: bool
    SnapPointTypesEnabled: int
    SnapPointTypesOnByDefault: int
    StepStatusAsString: str
    ToolTip: str


class StringBlock(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetBalloonTooltipImages(self) -> str:
        ...
    def SetBalloonTooltipImages(self, imageStrings: str) -> None:
        ...
    def GetBalloonTooltipTexts(self) -> str:
        ...
    def SetBalloonTooltipTexts(self, tooltipTextArray: str) -> None:
        ...
    def GetListItems(self) -> str:
        ...
    def SetListItems(self, itemStrings: str) -> None:
        ...
    def GetPresentationStyleMembers(self) -> str:
        ...
    def GetWidthMembers(self) -> str:
        ...
    def SetKeystrokeCallback(self, cb: BlockStyler.StringBlock.KeystrokeCallback) -> None:
        ...
    AllowInternationalTextInput: bool
    BalloonTooltipLayoutAsString: str
    Bitmap: str
    IsPassword: bool
    Localize: bool
    MaxTextLength: int
    PresentationStyleAsString: str
    ReadOnlyString: bool
    RetainValue: bool
    Tooltip: str
    Value: str
    WideValue: str
    WidthAsString: str


    

class SpecifyVector(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetInterpartSelectionMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    CreateInterpartLink: bool
    DoubleSide: bool
    EnableFacetSelection: bool
    EnableReverseDirection: bool
    InterpartSelectionAsString: str
    Is2DMode: bool
    LabelString: str
    Point: Point3d
    ShowShortcuts: bool
    SnapPointTypesOnByDefault: int
    StepStatusAsString: str
    Vector: Vector3d


class SpecifyPoint(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetInterpartSelectionMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    CreateInterpartLink: bool
    EnableFacetSelection: bool
    InterpartSelectionAsString: str
    LabelString: str
    Point: Point3d
    ShowShortcuts: bool
    SnapPointTypesEnabled: int
    SnapPointTypesOnByDefault: int
    StepStatusAsString: str


class SpecifyPlane(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    def GetInterpartSelectionMembers(self) -> str:
        ...
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    CreateInterpartLink: bool
    CurrentStepStatusAsString: str
    InterpartSelectionAsString: str
    LabelString: str
    ShowShortcuts: bool
    StepStatusAsString: str


class SpecifyOrientation(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    EnableDoubleClickFlip: bool
    EnableFacetSelection: bool
    HasOriginGwif: bool
    IsOriginSpecified: bool
    IsWCSCoordinates: bool
    Origin: Point3d
    SnapPointTypesOnByDefault: int
    VisibleManipulatorHandles: int
    XAxis: Vector3d
    YAxis: Vector3d


class SpecifyLocation(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetStepStatusMembers(self) -> str:
        ...
    AutomaticProgression: bool
    CursorLocation: Point3d
    DisplayTemporaryPoint: bool
    LabelString: str
    StepStatusAsString: str


class SpecifyCSYS(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetInterpartSelectionMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    def GetOutputTypeMembers(self) -> str:
        ...
    def GetSmartUpdteOptionMembers(self) -> str:
        """[Obsolete("Deprecated in NX9.0.1.  Use BlockStyler.SpecifyCSYS.GetSmartUpdateOptionMembers instead")"""
        ...
    def GetSmartUpdateOptionMembers(self) -> str:
        ...
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    CreateInterpartLink: bool
    InterpartSelectionAsString: str
    LabelString: str
    OutputTypeAsString: str
    ShowShortcuts: bool
    SmartUpdateOptionAsString: str
    SmartUpdteOptionAsString: str
    StepStatusAsString: str


class SpecifyAxis(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    BalloonTooltipLayoutAsString: str
    BalloonTooltipPointImage: str
    BalloonTooltipPointText: str
    BalloonTooltipVectorImage: str
    BalloonTooltipVectorText: str
    StepStatusAsString: str


class SnapBlockDialog(BlockStyler.BlockDialog):
    def __init__(self, ptr: int) -> None: ...
    def Add(self, itemType: str, itemTitle: str, itemValue: str) -> str:
        ...
    def AddItem(self, itemType: str, itemID: str) -> None:
        ...
    def FreeResource(self) -> None:
        ...


class SetList(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def SetSeed(self, dlxFile: str) -> None:
        ...
    def SetAddHandler(self, cb: BlockStyler.SetList.AddCallback) -> None:
        ...
    def SetDeleteHandler(self, cb: BlockStyler.SetList.DeleteCallback) -> None:
        ...
    def SetReorderObserver(self, cb: BlockStyler.SetList.ReorderCallback) -> None:
        ...
    def AddNewSet(self, copyPropertiesAndSelect: bool) -> BlockStyler.UIBlock:
        ...
    def Delete(self, uicomp: BlockStyler.UIBlock) -> None:
        ...
    def Swap(self, uicomp1: BlockStyler.UIBlock, uicomp2: BlockStyler.UIBlock) -> None:
        ...
    def InsertNewSet(self, location: BlockStyler.UIBlock, insertBeforeOrAfter: BlockStyler.SetList.InsertionLocation, copyPropertiesAndSelect: bool) -> BlockStyler.UIBlock:
        ...
    def SetItemText(self, item: BlockStyler.UIBlock, strings: str) -> None:
        ...
    def GetItemText(self, item: BlockStyler.UIBlock) -> str:
        ...
    def FindUpdated(self) -> BlockStyler.UIBlock:
        ...
    def GetSelected(self) -> typing.List[BlockStyler.UIBlock]:
        ...
    def SetSelected(self, items: typing.List[BlockStyler.UIBlock]) -> None:
        ...
    def GetItems(self) -> typing.List[BlockStyler.UIBlock]:
        ...
    def GetColumnLabels(self) -> str:
        ...
    def SetColumnLabels(self, labels: str) -> None:
        ...
    def GetColumnWidths(self) -> int:
        ...
    def SetColumnWidths(self, width: int) -> None:
        ...
    def GetLayoutMembers(self) -> str:
        ...
    AddNewSetLabel: str
    DefaultColumnWidth: int
    IsAddButtonSensitive: bool
    LayoutAsString: str
    ListExpanded: bool
    ListHideGroup: bool
    MaximumHeight: int
    MinimumHeight: int
    MultipleEdit: bool
    NumberColumnString: str
    NumberOfColumns: int
    ResizeHeightWithDialog: bool
    SeedDlxFile: str
    ShowAddNewSet: bool
    ShowColumnHeadings: bool
    ShowRemove: bool
    ShowReorderControls: bool


    

    class InsertionLocation(enum.Enum):
        Before = 0
        After = 1
    

    

    

class Separator(BlockStyler.UIBlock):
    def __init__(self) -> None: ...


class SelectPartFromList(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...


class SelectObject(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetInterpartSelectionMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetSelectModeMembers(self) -> str:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    def GetLastDeselectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def GetLastSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def GetMaximumScopeMembers(self) -> str:
        ...
    def SetSelectionFilter(self, maskAction: Selection.SelectionAction, maskTriples: typing.List[Selection.MaskTriple]) -> None:
        ...
    def AddFilter(self, filterTypes: int) -> None:
        ...
    def AddFilter(self, filterTypes: BlockStyler.SelectObject.FilterType) -> None:
        ...
    def AddFilter(self, type: int, subType: int, solidBodyType: int) -> None:
        ...
    def ResetFilter(self) -> None:
        ...
    AllowConvergentObject: bool
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    BlendVirtualCurveOverlay: bool
    CreateInterpartLink: bool
    Cue: str
    InterpartSelectionAsString: str
    LabelString: str
    MaximumScopeAsString: str
    PickPoint: Point3d
    PointOverlay: bool
    SelectModeAsString: str
    SmartUpdateOptionAsString: str
    SnapPointTypesEnabled: int
    SnapPointTypesOnByDefault: int
    StepStatusAsString: str
    ToolTip: str


    class FilterType(enum.Enum):
        Features = 1
        Faces = 2
        Edges = 4
        CurvesAndEdges = 8
        Components = 16
        SolidBodies = 32
        SheetBodies = 64
    

class SelectNode(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetSelectModeMembers(self) -> str:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    AutomaticProgression: bool
    Bitmap: str
    Cue: str
    LabelString: str
    SelectModeAsString: str
    ShowSelection: bool
    StepStatusAsString: str


class SelectFeature(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetSelectModeMembers(self) -> str:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    BlendVirtualCurveOverlay: bool
    Cue: str
    LabelString: str
    SelectModeAsString: str
    StepStatusAsString: str
    ToolTip: str


class SelectFacetRegion(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    def GetLastDeselectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def GetLastSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    Cue: str
    EnabledFacetCollectionRules: int
    FacetCollector: FacetCollector
    LabelString: str
    SelectedFacetCollectionRule: int
    StepStatusAsString: str
    SupportedFacetTypes: int
    ToolTip: str


class SelectElement(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    def GetSelectedObjectsSubIDs(self) -> int:
        ...
    def SetSelectedObjectsSubIDs(self, idVector: int) -> None:
        ...
    def GetSelectModeMembers(self) -> str:
        ...
    def GetSelectSubTypeMembers(self) -> str:
        ...
    AutomaticProgression: bool
    Bitmap: str
    Cue: str
    LabelString: str
    SelectModeAsString: str
    SelectSubTypeAsString: str
    ShowSelection: bool
    StepStatusAsString: str


class SectionBuilder(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetInterpartSelectionMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    def GetDefaultCurveRulesMembers(self) -> str:
        ...
    AllowConvergentObject: bool
    AllowInferredCurveSelection: bool
    AllowStopAtIntersectionFollowFillet: bool
    AngularTolerance: float
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    BlendVirtualCurveOverlay: bool
    ChainWithinFeature: bool
    CreateInterpartLink: bool
    Cue: str
    CurveRules: int
    DefaultCurveRulesAsString: str
    EntityType: int
    FollowFillet: bool
    InferredCurveSelection: bool
    InterpartSelectionAsString: str
    LabelString: str
    PointOverlay: bool
    ShowFlowDirectionAndOriginCurve: bool
    SmartUpdateOptionAsString: str
    SnapPointTypesEnabled: int
    SnapPointTypesOnByDefault: int
    StepStatusAsString: str
    StopAtIntersection: bool
    ToolTip: str


class ScrolledWindow(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    Height: int
    Members: BlockStyler.PropertyList
    ResizeHeightWithDialog: bool
    Width: int


class RGBColorPicker(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Localize: bool
    RetainValue: bool
    Value: int


class ReverseDirection(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    Direction: Vector3d
    Flip: bool
    Origin: Point3d


class RadiusDimension(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    AdaptiveScaleLimits: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    ExpressionObject: TaggedObject
    Formula: str
    HandleOrientation: Vector3d
    HandleOrigin: Point3d
    LineIncrement: float
    MaxInclusive: bool
    MaximumValue: float
    MinInclusive: bool
    MinimumValue: float
    PageIncrement: float
    ShowFocusHandle: bool
    ShowHandle: bool
    SnapPointTypesOnByDefault: int
    Units: TaggedObject
    Value: float
    WithScale: bool


class PropertyList(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetPropertyNames(self) -> str:
        ...
    def GetPropertyType(self, propertyName: str) -> BlockStyler.PropertyList.PropertyType:
        ...
    def GetPropertyType(self, propertyIndex: int) -> BlockStyler.PropertyList.PropertyType:
        ...
    def SetInteger(self, propertyName: str, value: int) -> None:
        ...
    def GetInteger(self, propertyName: str) -> int:
        ...
    def GetInteger(self, propertyIndex: int) -> int:
        ...
    def SetLogical(self, propertyName: str, value: bool) -> None:
        ...
    def GetLogical(self, propertyName: str) -> bool:
        ...
    def GetLogical(self, propertyIndex: int) -> bool:
        ...
    def SetDouble(self, propertyName: str, value: float) -> None:
        ...
    def GetDouble(self, propertyName: str) -> float:
        ...
    def GetDouble(self, propertyIndex: int) -> float:
        ...
    def SetString(self, propertyName: str, value: str) -> None:
        ...
    def GetString(self, propertyName: str) -> str:
        ...
    def GetString(self, propertyIndex: int) -> str:
        ...
    def SetEnumAsString(self, propertyName: str, value: str) -> None:
        ...
    def GetEnumAsString(self, propertyName: str) -> str:
        ...
    def GetEnumAsString(self, propertyIndex: int) -> str:
        ...
    def SetEnum(self, propertyName: str, value: int) -> None:
        ...
    def GetEnum(self, propertyName: str) -> int:
        ...
    def GetEnum(self, propertyIndex: int) -> int:
        ...
    def SetEnumMembers(self, propertyName: str, stringArray: str) -> None:
        ...
    def GetEnumMembers(self, propertyName: str) -> str:
        ...
    def GetEnumMembers(self, propertyIndex: int) -> str:
        ...
    def SetStrings(self, propertyName: str, stringArray: str) -> None:
        ...
    def GetStrings(self, propertyName: str) -> str:
        ...
    def GetStrings(self, propertyIndex: int) -> str:
        ...
    def GetUIBlock(self, propertyName: str) -> BlockStyler.UIBlock:
        ...
    def GetUIBlock(self, propertyIndex: int) -> BlockStyler.UIBlock:
        ...
    def SetPoint(self, propertyName: str, pointSc: Point3d) -> None:
        ...
    def GetPoint(self, propertyName: str) -> Point3d:
        ...
    def GetPoint(self, propertyIndex: int) -> Point3d:
        ...
    def SetVector(self, propertyName: str, vector: Vector3d) -> None:
        ...
    def GetVector(self, propertyName: str) -> Vector3d:
        ...
    def GetVector(self, propertyIndex: int) -> Vector3d:
        ...
    def SetBits(self, propertyName: str, bitsSc: int) -> None:
        ...
    def GetBits(self, propertyName: str) -> int:
        ...
    def GetBits(self, propertyIndex: int) -> int:
        ...
    def SetTaggedObject(self, propertyName: str, taggedSc: TaggedObject) -> None:
        ...
    def GetTaggedObject(self, propertyName: str) -> TaggedObject:
        ...
    def GetTaggedObject(self, propertyIndex: int) -> TaggedObject:
        ...
    def GetIntegerVector(self, propertyName: str) -> int:
        ...
    def SetIntegerVector(self, propertyName: str, intVector: int) -> None:
        ...
    def GetIntegerVector(self, propertyIndex: int) -> int:
        ...
    def GetDoubleVector(self, propertyName: str) -> float:
        ...
    def SetDoubleVector(self, propertyName: str, doubleVector: float) -> None:
        ...
    def GetDoubleVector(self, propertyIndex: int) -> float:
        ...
    def GetTaggedObjectVector(self, propertyName: str) -> typing.List[TaggedObject]:
        ...
    def SetTaggedObjectVector(self, propertyName: str, tagVector: typing.List[TaggedObject]) -> None:
        ...
    def GetTaggedObjectVector(self, propertyIndex: int) -> typing.List[TaggedObject]:
        ...
    def GetIntegerMatrix(self, propertyName: str, nRows: int, nColumns: int) -> int:
        ...
    def SetIntegerMatrix(self, propertyName: str, nRows: int, nColumns: int, matrixValue: int) -> None:
        ...
    def GetIntegerMatrix(self, propertyIndex: int, nRows: int, nColumns: int) -> int:
        ...
    def GetDoubleMatrix(self, propertyName: str, nRows: int, nColumns: int) -> float:
        ...
    def SetDoubleMatrix(self, propertyName: str, nRows: int, nColumns: int, matrixValue: float) -> None:
        ...
    def GetDoubleMatrix(self, propertyIndex: int, nRows: int, nColumns: int) -> float:
        ...
    def GetFile(self, propertyName: str) -> str:
        ...
    def SetFile(self, propertyName: str, value: str) -> None:
        ...
    def GetFile(self, propertyIndex: int) -> str:
        ...
    def GetArray(self, propertyName: str) -> BlockStyler.PropertyList:
        ...
    def GetArray(self, propertyIndex: int) -> BlockStyler.PropertyList:
        ...
    def SetSelectionFilter(self, propertyName: str, maskAction: Selection.SelectionAction, maskTriples: typing.List[Selection.MaskTriple]) -> None:
        ...
    Length: int
    Mode: BlockStyler.PropertyList.ListMode


    class PropertyType(enum.Enum):
        String = 0
        Double = 1
        Logical = 2
        Integer = 3
        Enum = 4
        Strings = 5
        UIBlock = 6
        Point = 7
        Vector = 8
        Bits = 9
        TaggedObject = 10
        Array = 11
        IntegerMatrix2d = 12
        DoubleMatrix2d = 13
        TaggedObjectMatrix2d = 14
        IntegerVector = 15
        DoubleVector = 16
        TaggedObjectVector = 17
        File = 18
        SelectionFilter = 19
        Undefined = 20
    

    class ListMode(enum.Enum):
        Indexed = 0
        Named = 1
    

class OrientXpress(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetDirectionMembers(self) -> str:
        ...
    def GetPlaneMembers(self) -> str:
        ...
    def GetReferenceMembers(self) -> str:
        ...
    DirectionAsString: str
    PlaneAsString: str
    ReferenceAsString: str
    ReferenceCsys: TaggedObject
    ShowAxisSubBlock: bool
    ShowPlaneSubBlock: bool
    ShowReferenceSubBlock: bool
    ShowSceneControl: bool
    ShowXAxis: bool
    ShowXYPlane: bool
    ShowXZPlane: bool
    ShowYAxis: bool
    ShowYZPlane: bool
    ShowZAxis: bool


class OnPathDimension(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetLocationOptionMembers(self) -> str:
        ...
    AdaptiveScaleLimits: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    ExpressionObject: TaggedObject
    Formula: str
    LineIncrement: float
    LocationOptionAsString: str
    MaxInclusive: bool
    MaximumValue: float
    MinInclusive: bool
    MinimumValue: float
    OptionMask: int
    OptionMenuTitle: str
    PageIncrement: float
    Path: TaggedObject
    ShowFocusHandle: bool
    SnapPointTypesOnByDefault: int
    Units: TaggedObject
    Value: float
    WithScale: bool


class ObjectColorPicker(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetValue(self) -> int:
        ...
    def SetValue(self, valueVector: int) -> None:
        ...
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Localize: bool
    NumberSelectable: int
    RetainValue: bool


class Node(TaggedObject):
    def __init__(self) -> None: ...
    def ScrollTo(self, columnID: int, visibleOption: BlockStyler.Node.Scroll) -> None:
        ...
    def Expand(self, expandOption: BlockStyler.Node.ExpandOption) -> None:
        ...
    def GetState(self) -> int:
        ...
    def SetState(self, state: int) -> None:
        ...
    def GetColumnDisplayText(self, columnID: int) -> str:
        ...
    def SetColumnDisplayText(self, columnID: int, columnDisplayText: str) -> None:
        ...
    def GetNodeData(self) -> DataContainer:
        ...
    CrossSelection: bool
    DisplayIcon: str
    DisplayText: str
    FirstChildNode: BlockStyler.Node
    ForegroundColor: int
    IsExpanded: bool
    IsInserted: bool
    IsSelected: bool
    NextNode: BlockStyler.Node
    NextSelectedNode: BlockStyler.Node
    NextSiblingNode: BlockStyler.Node
    ParentNode: BlockStyler.Node
    PreviousNode: BlockStyler.Node
    PreviousSelectedNode: BlockStyler.Node
    PreviousSiblingNode: BlockStyler.Node
    SelectedIcon: str


    class Scroll(enum.Enum):
        Center = 0
        LeastScroll = 1
        MostScroll = 2
    

    class ExpandOption(enum.Enum):
        Collapse = 0
        Expand = 1
        Toggle = 2
    

    class DropType(enum.Enum):
        None = 0
        On = 1
        Before = 2
        After = 3
        BeforeAndAfter = 4
    

    class DragType(enum.Enum):
        None = 0
        All = 1
    

class MultilineString(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetValue(self) -> str:
        ...
    def SetValue(self, valueString: str) -> None:
        ...
    Height: int
    Localize: bool
    MaximumCharactersAccepted: int
    MaximumHeight: int
    MinimumHeight: int
    ResizeHeightWithDialog: bool
    RetainValue: bool
    ValuesConcatenated: str
    Width: int


class Microposition(BlockStyler.UIBlock):
    def __init__(self) -> None: ...


class ListBox(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def SetAddHandler(self, cb: BlockStyler.ListBox.AddCallback) -> None:
        ...
    def SetDeleteHandler(self, cb: BlockStyler.ListBox.DeleteCallback) -> None:
        ...
    def GetListItems(self) -> str:
        ...
    def SetListItems(self, items: str) -> None:
        ...
    def GetSelectedItems(self) -> int:
        ...
    def SetSelectedItems(self, selectedItems: int) -> None:
        ...
    def GetSelectedItemStrings(self) -> str:
        ...
    def SetSelectedItemStrings(self, strings: str) -> None:
        ...
    def GetSelectedItemBooleans(self) -> int:
        ...
    def SetSelectedItemBooleans(self, items: int) -> None:
        ...
    AllowDeselectForSingleSelect: bool
    Height: int
    IsAddButtonSensitive: bool
    IsDeleteButtonSensitive: bool
    Localize: bool
    MaximumHeight: int
    MaximumStringLength: int
    MinimumHeight: int
    ResizeHeightWithDialog: bool
    SelectedItemIndex: int
    SelectedItemString: str
    ShowAddButton: bool
    ShowDeleteButton: bool
    ShowMoveUpDownButtons: bool
    SingleSelect: bool


    

    

class LineWidth(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    AllowDefaultWidth: bool
    AllowNoChangeWidth: bool
    LabelVisibility: bool
    LineWidthValue: int
    ShowDefaultAsOriginal: bool


class LineFont(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    AvailableOptions: int
    ShowOptionLabels: bool
    ValueAsString: str


class LineColorFontWidth(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetColorValue(self) -> int:
        ...
    def SetColorValue(self, colorValueVector: int) -> None:
        ...
    HideSubBlocksAsString: str
    LabelString: str
    LayoutAsString: str
    LineFontAvailableOptions: int
    LineFontValueAsString: str
    LineWidthShowDefault: bool
    LineWidthShowDefaultAsOriginal: bool
    LineWidthShowNoChange: bool
    LineWidthUseWideLines: bool
    ShowLabel: bool


class LinearDimension(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    AdaptiveScaleLimits: bool
    AutoReverseDuringDrag: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    ExpressionObject: TaggedObject
    Formula: str
    HandleOrientation: Vector3d
    HandleOrigin: Point3d
    LineIncrement: float
    MaxInclusive: bool
    MaximumValue: float
    MinInclusive: bool
    MinimumValue: float
    PageIncrement: float
    ShowFocusHandle: bool
    ShowHandle: bool
    SnapPointTypesOnByDefault: int
    Units: TaggedObject
    Value: float
    WithScale: bool


class LayerBlock(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    LayerOption: int
    LayerValue: int
    ShowMaintainLayerOption: bool
    ShowOriginalLayerOption: bool
    ShowUserDefinedLayerOption: bool
    ShowWorkLayerOption: bool


class Label(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    DisplayBitmapLabel: bool
    HighQualityBitmap: bool
    Localize: bool
    Tooltip: str
    WordWrap: bool


class IntegerTable(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetMaximumValues(self, nRows: int, nColumns: int) -> int:
        ...
    def SetMaximumValues(self, nRows: int, nColumns: int, matrixValue: int) -> None:
        ...
    def GetMinimumValues(self, nRows: int, nColumns: int) -> int:
        ...
    def SetMinimumValues(self, nRows: int, nColumns: int, matrixValue: int) -> None:
        ...
    def GetValues(self, nRows: int, nColumns: int) -> int:
        ...
    def SetValues(self, nRows: int, nColumns: int, matrixValue: int) -> None:
        ...
    def GetRowTitles(self) -> str:
        ...
    def SetRowTitles(self, rowTitle: str) -> None:
        ...
    ColumnTitles: str
    Increment: float
    RetainValue: bool
    Spin: bool
    WrapSpin: bool


class IntegerBlock(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetComboOptions(self) -> int:
        ...
    def SetComboOptions(self, optionValue: int) -> None:
        ...
    def GetPresentationStyleMembers(self) -> str:
        ...
    AdaptiveScaleLimits: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    Increment: float
    LineIncrement: float
    Localize: bool
    MaxInclusive: bool
    MaximumValue: int
    MinInclusive: bool
    MinimumValue: int
    PageIncrement: float
    PresentationStyleAsString: str
    ReadOnlyValue: bool
    RetainValue: bool
    ScaleLimits: bool
    ScaleMaxLimitLabel: str
    ScaleMinLimitLabel: str
    ShowScaleValue: bool
    TitleVisibility: bool
    Value: int
    WrapSpin: bool


class Group(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    Column: int
    Localize: bool
    Members: BlockStyler.PropertyList


class FolderSelection(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    Path: str
    RetainStringValue: bool


class FileSelection(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    Filter: str
    Path: str
    RetainStringValue: bool


class FaceCollector(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetInterpartSelectionMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetSelectModeMembers(self) -> str:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    def GetDefaultFaceRulesMembers(self) -> str:
        ...
    AllowConvergentObject: bool
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    BlendVirtualCurveOverlay: bool
    CreateInterpartLink: bool
    Cue: str
    DefaultFaceRulesAsString: str
    EntityType: int
    FaceRules: int
    InterpartSelectionAsString: str
    LabelString: str
    MaximumScopeAsString: str
    PopupMenuEnabled: bool
    SelectModeAsString: str
    StepStatusAsString: str
    ToolTip: str


class ExpressionBlock(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetDimensionalityMembers(self) -> str:
        ...
    AdaptiveScaleLimits: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    DimensionalityAsString: str
    ExpressionObject: TaggedObject
    Formula: str
    HasUnitsMenu: bool
    LineIncrement: float
    MaxInclusive: bool
    MaximumValue: float
    MinInclusive: bool
    MinimumValue: float
    PageIncrement: float
    RetainValue: bool
    Units: TaggedObject
    Value: float
    WithScale: bool


class Explorer(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def SetChildMembers(self, parentMember: BlockStyler.UIBlock, childMembers: typing.List[BlockStyler.UIBlock]) -> None:
        ...
    def SetNotifyNodeSelectedPreHandler(self, cb: BlockStyler.Explorer.NotifyNodeSelectedPreCallback) -> None:
        ...
    def SetNotifyNodeSelectedPostHandler(self, cb: BlockStyler.Explorer.NotifyNodeSelectedPostCallback) -> None:
        ...
    CurrentNode: int
    Localize: bool
    Members: BlockStyler.PropertyList
    TreeWidth: int


    

    

class Enumeration(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipImages(self) -> str:
        ...
    def SetBalloonTooltipImages(self, imageStrings: str) -> None:
        ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetBalloonTooltipTexts(self) -> str:
        ...
    def SetBalloonTooltipTexts(self, tooltipTextArray: str) -> None:
        ...
    def GetBitmaps(self) -> str:
        ...
    def SetBitmaps(self, bitmapsStrings: str) -> None:
        ...
    def GetEnumSensitivity(self) -> int:
        ...
    def SetEnumSensitivity(self, valueVector: int) -> None:
        ...
    def GetEnumVisibility(self) -> int:
        ...
    def SetEnumVisibility(self, valueVector: int) -> None:
        ...
    def GetInitialShortcuts(self) -> int:
        ...
    def SetInitialShortcuts(self, valueVector: int) -> None:
        ...
    def GetLayoutMembers(self) -> str:
        ...
    def GetPresentationStyleMembers(self) -> str:
        ...
    def GetEnumMembers(self) -> str:
        ...
    def SetEnumMembers(self, memberStrings: str) -> None:
        ...
    AllowShortcuts: bool
    BalloonTooltipLayoutAsString: str
    BorderVisibility: bool
    HighQualityBitmap: bool
    IconsOnly: bool
    LabelVisibility: bool
    LayoutAsString: str
    Localize: bool
    NumberOfColumns: int
    PackedColumns: bool
    PresentationStyleAsString: str
    RetainValue: bool
    ValueAsString: str


class DrawingArea(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    Height: int
    Image: str
    Width: int


class DoubleTable(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetMaximumValues(self, nRows: int, nColumns: int) -> float:
        ...
    def SetMaximumValues(self, nRows: int, nColumns: int, matrixValue: float) -> None:
        ...
    def GetMinimumValues(self, nRows: int, nColumns: int) -> float:
        ...
    def SetMinimumValues(self, nRows: int, nColumns: int, matrixValue: float) -> None:
        ...
    def GetValues(self, nRows: int, nColumns: int) -> float:
        ...
    def SetValues(self, nRows: int, nColumns: int, matrixValue: float) -> None:
        ...
    def GetRowTitles(self) -> str:
        ...
    def SetRowTitles(self, rowTitle: str) -> None:
        ...
    CellWidth: int
    ColumnTitles: str
    Increment: float
    RetainValue: bool
    Spin: bool
    WrapSpin: bool


class DoubleBlock(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetComboOptions(self) -> float:
        ...
    def SetComboOptions(self, optionValue: float) -> None:
        ...
    def GetPresentationStyleMembers(self) -> str:
        ...
    AdaptiveScaleLimits: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    Increment: float
    LineIncrement: float
    Localize: bool
    MaxInclusive: bool
    MaximumValue: float
    MinInclusive: bool
    MinimumValue: float
    PageIncrement: float
    PresentationStyleAsString: str
    ReadOnlyValue: bool
    RetainValue: bool
    ScaleLimits: bool
    ScaleMaxLimitLabel: str
    ScaleMinLimitLabel: str
    ShowScaleValue: bool
    TitleVisibility: bool
    Value: float
    WrapSpin: bool


class CurveCollector(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetInterpartSelectionMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetSelectModeMembers(self) -> str:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    def GetDefaultCurveRulesMembers(self) -> str:
        ...
    AllowConvergentObject: bool
    AllowInferredCurveSelection: bool
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    BlendVirtualCurveOverlay: bool
    CreateInterpartLink: bool
    Cue: str
    CurveRules: int
    DefaultCurveRulesAsString: str
    EntityType: int
    InferredCurveSelection: bool
    InterpartSelectionAsString: str
    LabelString: str
    MaximumScopeAsString: str
    PopupMenuEnabled: bool
    SelectModeAsString: str
    StepStatusAsString: str
    ToolTip: str


class CompositeBlock(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def FindBlock(self, blockName: str) -> BlockStyler.UIBlock:
        ...
    def GetBlocks(self) -> typing.List[BlockStyler.UIBlock]:
        ...
    def GetDialogSizingMembers(self) -> str:
        ...
    def GetNavigationStyleMembers(self) -> str:
        ...
    Cue: str
    DialogSizing: int
    DialogSizingAsString: str
    LastUpdated: BlockStyler.UIBlock
    NavigationStyle: int
    NavigationStyleAsString: str


class ChooseExpression(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetExpressionSortTypeMembers(self) -> str:
        ...
    def GetExpressionTypeIndexMembers(self) -> str:
        ...
    ExpressionSortTypeAsString: str
    ExpressionTypeIndexAsString: str
    SelectedExpression: TaggedObject


class Button(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    HighQualityBitmap: bool
    Localize: bool
    Tooltip: str


class BodyCollector(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    def GetInterpartSelectionMembers(self) -> str:
        ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetSelectedObjects(self, objectVector: typing.List[TaggedObject]) -> None:
        ...
    def GetSelectModeMembers(self) -> str:
        ...
    def GetStepStatusMembers(self) -> str:
        ...
    def GetDefaultBodyRulesMembers(self) -> str:
        ...
    AllowConvergentObject: bool
    AutomaticProgression: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    Bitmap: str
    BlendVirtualCurveOverlay: bool
    BodyRules: int
    CreateInterpartLink: bool
    Cue: str
    DefaultBodyRulesAsString: str
    EntityType: int
    IncludeSheetBodies: bool
    InterpartSelectionAsString: str
    LabelString: str
    MaximumScopeAsString: str
    PopupMenuEnabled: bool
    SelectModeAsString: str
    StepStatusAsString: str
    ToolTip: str


class BlockDialog(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def AddUpdateHandler(self, cb: BlockStyler.BlockDialog.Update) -> None:
        ...
    def AddEnableOKButtonHandler(self, cb: BlockStyler.BlockDialog.EnableOKButton) -> None:
        ...
    def AddFilterHandler(self, cb: BlockStyler.BlockDialog.Filter) -> None:
        ...
    def AddOkHandler(self, okCb: BlockStyler.BlockDialog.Ok) -> None:
        ...
    def AddApplyHandler(self, applyCb: BlockStyler.BlockDialog.Apply) -> None:
        ...
    def AddCancelHandler(self, cancelCb: BlockStyler.BlockDialog.Cancel) -> None:
        ...
    def AddCloseHandler(self, closeCb: BlockStyler.BlockDialog.Close) -> None:
        ...
    def AddInitializeHandler(self, cb: BlockStyler.BlockDialog.Initialize) -> None:
        ...
    def AddDialogShownHandler(self, cb: BlockStyler.BlockDialog.DialogShown) -> None:
        ...
    def Show(self) -> Selection.Response:
        ...
    def Show(self, dialogMode: BlockStyler.BlockDialog.DialogMode) -> Selection.Response:
        ...
    def PerformApply(self) -> None:
        ...
    def PerformOK(self) -> None:
        ...
    def PerformOK_Deferred(self, Handle: int) -> None:
        ...
    def PerformCancel(self) -> None:
        ...
    def PerformCancel_Deferred(self, Handle: int) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    def AddFocusNotifyHandler(self, cb: BlockStyler.BlockDialog.FocusNotify) -> None:
        ...
    def AddKeyboardFocusNotifyHandler(self, cb: BlockStyler.BlockDialog.KeyboardFocusNotify) -> None:
        ...
    def RegisterUserDefinedUIBlock(self, blockDialog: BlockStyler.BlockDialog, blockId: str) -> None:
        ...
    def GetBlockProperties(self, blockName: str) -> BlockStyler.PropertyList:
        ...
    TopBlock: BlockStyler.CompositeBlock


    

    

    

    

    

    

    

    

    class DialogMode(enum.Enum):
        Create = 0
        Edit = 1
    

    

    

    

class AngularDimension(BlockStyler.UIBlock):
    def __init__(self) -> None: ...
    def GetBalloonTooltipLayoutMembers(self) -> str:
        ...
    AdaptiveScaleLimits: bool
    BalloonTooltipImage: str
    BalloonTooltipLayoutAsString: str
    BalloonTooltipText: str
    ExpressionObject: TaggedObject
    Formula: str
    HandleFixedSizeFlag: bool
    HandleOrigin: Point3d
    HandleRadius: float
    HandleRadiusOffset: float
    HandleXAxis: Vector3d
    HandleZAxis: Vector3d
    LineIncrement: float
    MaxInclusive: bool
    MaximumValue: float
    MinInclusive: bool
    MinRadius: float
    MinimumValue: float
    PageIncrement: float
    ShowFocusHandle: bool
    ShowHandle: bool
    SnapPointTypesOnByDefault: int
    Units: TaggedObject
    Value: float
    WithScale: bool


