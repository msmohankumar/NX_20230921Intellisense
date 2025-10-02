from ...NXOpen import *
from ..UIStyler import *

import typing
import enum

class WideString(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.WideString.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetFocus(self) -> None:
        ...
    ItemValue: str
    Sensitivity: bool
    Visibility: bool


    

class ToolPalette(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.ToolPalette.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        ...
    def GetSensitivity(self) -> bool:
        ...
    def SetDefault(self, dialogId: int) -> None:
        ...
    ItemValue: int
    Visibility: bool


    

class Toggle(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddValueChangedHandler(self, valuechangedevent: UIStyler.Toggle.ValueChanged, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        ...
    def GetSensitivity(self) -> bool:
        ...
    def SetFocus(self) -> None:
        ...
    def SetDefaultAction(self) -> None:
        ...
    ItemValue: bool
    Visibility: bool


    

class TabControl(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddSwitchHandler(self, switchevent: UIStyler.TabControl.SwitchHandler, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetFocus(self) -> None:
        ...
    PageSwitchData: UIStyler.PageSwitchData
    Sensitivity: bool
    Visibility: bool


    

class StylerItem(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetItemType(self) -> UIStyler.StylerItem.ItemType:
        ...
    def InitializeAttachment(self) -> UIStyler.Attachment:
        ...
    def SetAttachment(self, attachment: UIStyler.Attachment) -> None:
        ...
    def IsEqualTo(self, itemToCompare: UIStyler.StylerItem) -> bool:
        ...


    class ItemType(enum.Enum):
        InvalidType = -1
        ActionButton = 0
        Dialog = 1
        RadioBox = 2
        Real = 3
        ScaleReal = 4
        Bitmap = 5
        RowColumn = 6
        ButtonLayout = 7
        ScrolledWindow = 8
        ColorTool = 9
        SelectionBox = 10
        Separator = 11
        SingleSelectionList = 12
        String = 13
        BeginGroup = 14
        Integer = 15
        ScaleInteger = 16
        MultiList = 17
        Label = 18
        MultiLineText = 19
        TabControl = 20
        OptionMenu = 21
        Toggle = 22
        OptionToggle = 23
        ToolPalette = 24
        WideString = 25
        PropertyPage = 26
        CollapsibleGroup = 27
    

class StylerEvent(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetStylerItem(self) -> UIStyler.StylerItem:
        ...
    def GetReason(self) -> UIStyler.StylerEvent.Reason:
        ...


    class Reason(enum.Enum):
        NoReason = -1
        ActivateReason = 0
        ValueChangedReason = 1
        DragReason = 2
        DoubleClickReason = 3
        OkReason = 4
        ApplyReason = 5
        BackReason = 6
        CancelReason = 7
        ConstructReason = 8
        DestructReason = 9
        FileopReason = 10
        SwitchReason = 11
        FileOperationReason = 12
        ExitFileOperationReason = 13
    

    class Miscellaneous(enum.Enum):
        NoSubIndex = -1
        OkIndex = 0
        ApplyIndex = 1
        BackIndex = 2
        CancelIndex = 3
    

    class Indicator(enum.Enum):
        NoValue = -1
        StringValue = 0
        StringPointerValue = 1
        IntegerValue = 2
        IntegerPointerValue = 3
        RealValue = 4
        RealPointerValue = 5
        SelectionValue = 6
        OptionToggleValue = 7
    

class Styler(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def CreateStylerDialog(self, dialogName: str) -> UIStyler.Dialog:
        ...
    def Tag(self) -> Tag: ...



class StringItem(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.StringItem.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetBitmap(self, strBitmap: str) -> None:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetSensitivity(self, type: bool) -> None:
        ...
    def GetSensitivity(self) -> bool:
        ...
    def SetFocus(self) -> None:
        ...
    ItemValue: str
    Visibility: bool


    

class SingleSelectList(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.SingleSelectList.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddDoubleClickHandler(self, doubleclickevent: UIStyler.SingleSelectList.DoubleClick, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetSelected(self, subIndex: int) -> None:
        ...
    def SetListItems(self, itemVal: str) -> None:
        ...
    def GetListItems(self) -> str:
        ...
    def SetFocus(self) -> None:
        ...
    def DeselectSubItem(self, subItemIndex: int) -> None:
        ...
    def InsertSubItem(self, subitemIndex: int, multiEntries: str) -> None:
        ...
    def Append(self, multiEntries: str) -> None:
        ...
    def DeleteSubItem(self, subItemIndex: int) -> None:
        ...
    def ShowSubItem(self, subItemIndex: int) -> None:
        ...
    def GetSelectedIndexValue(self) -> int:
        ...
    def GetSelectedString(self) -> str:
        ...
    def HasSelected(self) -> bool:
        ...
    Sensitivity: bool
    Visibility: bool


    

    

class Separator(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    Visibility: bool


class SelectionBox(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.SelectionBox.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddDoubleClickHandler(self, doubleclickevent: UIStyler.SelectionBox.DoubleClick, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetListItems(self, values: str) -> None:
        ...
    def GetListItems(self) -> str:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetFocus(self) -> None:
        ...
    def DeselectSubItem(self, subItemIndex: int) -> None:
        ...
    def InsertSubItem(self, subitemIndex: int, multiEntries: str) -> None:
        ...
    def Append(self, multiEntries: str) -> None:
        ...
    def DeleteSubItem(self, subItemIndex: int) -> None:
        ...
    def ShowSubItem(self, subItemIndex: int) -> None:
        ...
    def SetValue(self, value: int) -> None:
        ...
    def GetSelectedIndexValue(self) -> int:
        ...
    def GetSelectedString(self) -> str:
        ...
    Sensitivity: bool
    Visibility: bool


    

    

class ScrolledWindow(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    Sensitivity: bool
    Visibility: bool


class RowColumn(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    Sensitivity: bool
    Visibility: bool


class RealScale(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddValueChangedHandler(self, valuechangedevent: UIStyler.RealScale.ValueChanged, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddDragHandler(self, dragevent: UIStyler.RealScale.Drag, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetLimits(self, minimumValue: float, maximumValue: float) -> None:
        ...
    def SetLabels(self, minimumLabel: str, maximumLabel: str) -> None:
        ...
    def SetDecimalPrecision(self, digits: int) -> None:
        ...
    ItemValue: float
    Sensitivity: bool
    Visibility: bool


    

    

class RealItem(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.RealItem.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetBitmap(self, strBitmap: str) -> None:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetFocus(self) -> None:
        ...
    ItemValue: float
    Sensitivity: bool
    Visibility: bool


    

class RadioBox(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddValueChangedHandler(self, valuechangedevent: UIStyler.RadioBox.ValueChanged, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        ...
    def GetSensitivity(self) -> bool:
        ...
    def SetDefaultAction(self) -> None:
        ...
    ItemValue: int
    Visibility: bool


    

class PushButton(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.PushButton.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetBitmap(self, bitmap: str) -> None:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetFocus(self) -> None:
        ...
    def SetDefaultAction(self) -> None:
        ...
    Sensitivity: bool
    Visibility: bool


    

class PropertyPage(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetFocus(self) -> None:
        ...
    Sensitivity: bool
    Visibility: bool


class PageSwitchData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    ActivatedPage: int
    DeactivatedPage: int


class OptionToggle(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.OptionToggle.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddValueChangedHandler(self, valuechangedevent: UIStyler.OptionToggle.ValueChanged, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetBitmaps(self, bitmaps: str) -> None:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetItems(self, strListArray: str) -> None:
        ...
    def GetItems(self) -> str:
        ...
    def SetItemValue(self, subitemIndex: int, setCheck: bool) -> None:
        ...
    def GetItemValue(self, setCheck: bool) -> int:
        ...
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        ...
    def GetSensitivity(self) -> bool:
        ...
    def SetDefaultAction(self) -> None:
        ...
    Visibility: bool


    

    

class OptionMenu(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.OptionMenu.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetBitmap(self, bitmaps: str) -> None:
        ...
    def GetBitmap(self) -> str:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetItems(self, strListArray: str) -> None:
        ...
    def GetItems(self) -> str:
        ...
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        ...
    def GetSensitivity(self) -> bool:
        ...
    ItemValue: int
    Visibility: bool


    

class MultiTextBox(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetItemValues(self, values: str) -> None:
        ...
    def GetItemValues(self) -> str:
        ...
    def SetFocus(self) -> None:
        ...
    Sensitivity: bool
    Visibility: bool


class MultiSelectList(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.MultiSelectList.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddDoubleClickHandler(self, doubleclickevent: UIStyler.MultiSelectList.DoubleClick, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetListItems(self, itemVal: str) -> None:
        ...
    def GetListItems(self) -> str:
        ...
    def SetSelected(self, subIndex: int) -> None:
        ...
    def SetAllSelected(self) -> None:
        ...
    def GetAllIndicesSelected(self) -> int:
        ...
    def GetAllNameSelected(self) -> str:
        ...
    def Focus(self) -> None:
        ...
    def Deselect(self, subItemIndex: int) -> None:
        ...
    def InsertSubitems(self, subitemIndex: int, multiEntries: str) -> None:
        ...
    def Append(self, multiEntries: str) -> None:
        ...
    def DeleteSubitem(self, subItemIndex: int) -> None:
        ...
    def ShowSubItem(self, subItemIndex: int) -> None:
        ...
    Sensitivity: bool
    Visibility: bool


    

    

class LabelItem(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def SetBitmap(self, bitmapFile: str) -> None:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    Sensitivity: bool
    Visibility: bool


class IntegerScale(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddValueChangedHandler(self, valuechangedevent: UIStyler.IntegerScale.ValueChanged, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddDragHandler(self, dragevent: UIStyler.IntegerScale.Drag, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetLimits(self, minimumValue: int, maximumValue: int) -> None:
        ...
    def SetLabels(self, minimumLabel: str, maximumLabel: str) -> None:
        ...
    ItemValue: int
    Sensitivity: bool
    Visibility: bool


    

    

class IntegerItem(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.IntegerItem.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetBitmap(self, bitmap: str) -> None:
        ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    def SetFocus(self) -> None:
        ...
    ItemValue: int
    Sensitivity: bool
    Visibility: bool


    

class GroupBox(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    Sensitivity: bool
    Visibility: bool


class FileOperationData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    State: UIStyler.FileOperationData.FileOperationState
    Type: UIStyler.FileOperationData.FileOperationType


    class FileOperationType(enum.Enum):
        New = 0
        Open = 1
        Save = 2
        SaveAs = 3
        SaveAll = 4
        Close = 5
        Quit = 6
        SaveAndExit = 7
        ChangePart = 8
        Execute = 9
        Reopen = 10
        SaveAllAndClose = 11
        SaveAndClose = 12
        SaveAsAndClose = 13
    

    class FileOperationState(enum.Enum):
        Enter = 0
        Exit = 1
    

class DialogState(enum.Enum):
    ContinueDialog = 0
    ExitDialog = 1


class DialogResponse(enum.Enum):
    PickResponse = 1
    Ok = 2
    Cancel = 3
    Back = 4
    Apply = 5
    Help = 6
    ObjectSelected = 7
    ObjectSelectedByName = 8
    CbTerminate = 9


class DialogItem(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddConstructHandler(self, constructevent: UIStyler.DialogItem.Construct, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddDestructHandler(self, destructevent: UIStyler.DialogItem.Destruct, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddOkayHandler(self, okayevent: UIStyler.DialogItem.Okay, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddApplyHandler(self, applyevent: UIStyler.DialogItem.Apply, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddPageSwitchHandler(self, switchevent: UIStyler.DialogItem.PageSwitch, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddBackHandler(self, backevent: UIStyler.DialogItem.Back, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddCancelHandler(self, cancelevent: UIStyler.DialogItem.Cancel, isDialogLaunchingEvent: bool) -> None:
        ...
    def AddFileOperationHandler(self, fileoperationevent: UIStyler.DialogItem.FileOperation, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetTitle(self, strLabel: str) -> None:
        ...
    def SetSensitivity(self, type: bool) -> None:
        ...
    def SetNavigationSensitivity(self, subItemIndex: UIStyler.DialogItem.DialogItemIndex, type: bool) -> None:
        ...
    def SetResize(self, type: bool) -> None:
        ...
    def SetWidth(self, width: int) -> None:
        ...
    def GetSelectionHandle(self) -> SelectionHandle:
        ...
    FileOperationData: UIStyler.FileOperationData


    

    

    

    class DialogItemIndex(enum.Enum):
        Ok = 0
        Apply = 1
        Back = 2
        Cancel = 3
    

    

    

    

    

    

class DialogIndex(enum.Enum):
    NoSubIndex = -1


class Dialog(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetDialogIndex(self, itemIdentifier: str) -> UIStyler.DialogItem:
        ...
    def GetPushButton(self, itemIdentifier: str) -> UIStyler.PushButton:
        ...
    def GetBitmap(self, itemIdentifier: str) -> UIStyler.BitMap:
        ...
    def GetButtonLayout(self, itemIdentifier: str) -> UIStyler.ButtonLayout:
        ...
    def GetColorTool(self, itemIdentifier: str) -> UIStyler.ColorTool:
        ...
    def GetGroupBox(self, itemIdentifier: str) -> UIStyler.GroupBox:
        ...
    def GetIntegerItem(self, itemIdentifier: str) -> UIStyler.IntegerItem:
        ...
    def GetIntegerScale(self, itemIdentifier: str) -> UIStyler.IntegerScale:
        ...
    def GetMultiSelectList(self, itemIdentifier: str) -> UIStyler.MultiSelectList:
        ...
    def GetMultiTextBox(self, itemIdentifier: str) -> UIStyler.MultiTextBox:
        ...
    def GetOptionMenu(self, itemIdentifier: str) -> UIStyler.OptionMenu:
        ...
    def GetOptionToggle(self, itemIdentifier: str) -> UIStyler.OptionToggle:
        ...
    def GetPropertyPage(self, itemIdentifier: str) -> UIStyler.PropertyPage:
        ...
    def GetRadioBox(self, itemIdentifier: str) -> UIStyler.RadioBox:
        ...
    def GetRealItem(self, itemIdentifier: str) -> UIStyler.RealItem:
        ...
    def GetRealScale(self, itemIdentifier: str) -> UIStyler.RealScale:
        ...
    def GetRowColumn(self, itemIdentifier: str) -> UIStyler.RowColumn:
        ...
    def GetScrolledWindow(self, itemIdentifier: str) -> UIStyler.ScrolledWindow:
        ...
    def GetSelectionBox(self, itemIdentifier: str) -> UIStyler.SelectionBox:
        ...
    def GetSeparator(self, itemIdentifier: str) -> UIStyler.Separator:
        ...
    def GetSingleSelectList(self, itemIdentifier: str) -> UIStyler.SingleSelectList:
        ...
    def GetStringItem(self, itemIdentifier: str) -> UIStyler.StringItem:
        ...
    def GetTabControl(self, itemIdentifier: str) -> UIStyler.TabControl:
        ...
    def GetToggle(self, itemIdentifier: str) -> UIStyler.Toggle:
        ...
    def GetToolPalette(self, itemIdentifier: str) -> UIStyler.ToolPalette:
        ...
    def GetLabelItem(self, itemIdentifier: str) -> UIStyler.LabelItem:
        ...
    def GetCollapsibleGroup(self, itemIdentifier: str) -> UIStyler.CollapsibleGroup:
        ...
    def GetWideString(self, itemIdentifier: str) -> UIStyler.WideString:
        ...
    def GetStylerItem(self, itemIdentifier: str, type: UIStyler.Dialog.ItemType) -> UIStyler.StylerItem:
        ...
    def GetDialogItemUsingSelectionHandle(self, select: SelectionHandle) -> UIStyler.StylerItem:
        ...
    def Show(self) -> UIStyler.DialogResponse:
        ...
    def RegisterWithUiMenu(self, isTopDialog: bool) -> None:
        ...


    class ItemType(enum.Enum):
        PushButton = 0
        DialogItem = 1
        RadioBox = 2
        RealItem = 3
        RealScale = 4
        Bitmap = 5
        RowColumn = 6
        ButtonLayout = 7
        ScrolledWindow = 8
        ColorTool = 9
        SelectionBox = 10
        Separator = 11
        SingleSelectList = 12
        StringItem = 13
        GroupBox = 14
        IntegerItem = 15
        IntegerScale = 16
        MultiSelectList = 17
        LabelItem = 18
        MultiTextBox = 19
        TabControl = 20
        OptionMenu = 21
        Toggle = 22
        OptionToggle = 23
        ToolPalette = 24
        WideString = 25
        PropertyPage = 26
        CollapsibleGroup = 27
    

class ColorTool(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddValueChangedHandler(self, valuechangedevent: UIStyler.ColorTool.ValueChanged, isDialogLaunchingEvent: bool) -> None:
        ...
    ItemValue: int
    Sensitivity: bool
    Visibility: bool


    

class CollapsibleGroup(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def SetLabel(self, strLabel: str) -> None:
        ...
    CollapseState: bool
    Visibility: bool


class ButtonLayout(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def AddActivateHandler(self, activateevent: UIStyler.ButtonLayout.Activate, isDialogLaunchingEvent: bool) -> None:
        ...
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        ...
    def GetSensitivity(self) -> bool:
        ...
    def GetSelectedIndexValue(self) -> int:
        ...
    def SetDefaultAction(self) -> None:
        ...
    Visibility: bool


    

class BitMap(UIStyler.StylerItem):
    def __init__(self, ptr: int) -> None: ...
    def SetBitmap(self, bitmap: str) -> None:
        ...


class Attachment(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetCenter(self, isCenter: bool) -> None:
        ...
    def SetAttachTypeTop(self, attachTypeTop: UIStyler.Attachment.AttachType) -> None:
        ...
    def SetAttachTypeLeft(self, attachTypeLeft: UIStyler.Attachment.AttachType) -> None:
        ...
    def SetAttachTypeRight(self, attachTypeRight: UIStyler.Attachment.AttachType) -> None:
        ...
    def SetTopOffset(self, offsetTop: int) -> None:
        ...
    def SetLeftOffset(self, offsetLeft: int) -> None:
        ...
    def SetRightOffset(self, offsetRight: int) -> None:
        ...
    def SetTopDialogItem(self, topItemIdentifire: str) -> None:
        ...
    def SetLeftDialogItem(self, leftItemIdentifire: str) -> None:
        ...
    def SetRightDialogItem(self, rightItemIdentifire: str) -> None:
        ...


    class AttachType(enum.Enum):
        Dialog = 0
        Default = 1
        None = 2
        NoChange = 3
        Item = 4
    

