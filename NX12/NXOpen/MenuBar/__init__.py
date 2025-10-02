from ...NXOpen import *
from ..MenuBar import *

import typing
import enum

class MenuButtonEvent(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetMenuAncestors(self) -> str:
        ...
    ActiveButton: MenuBar.MenuButton
    ApplicationId: int
    MenuBarName: str


class MenuButton(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    ButtonId: int
    ButtonName: str
    ButtonSensitivity: MenuBar.MenuButton.SensitivityStatus
    ButtonType: MenuBar.MenuButton.Type
    ButtonTypeName: str
    ToggleStatus: MenuBar.MenuButton.Toggle


    class Type(enum.Enum):
        CascadeButton = 0
        PushButton = 1
        ToggleButton = 2
        Separator = 3
        ApplicationButton = 4
        NullButton = 5
    

    class Toggle(enum.Enum):
        On = 0
        Off = 1
    

    class SensitivityStatus(enum.Enum):
        Sensitive = 0
        Insensitive = 1
    

class MenuBarManager(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def AddMenuAction(self, name: str, actionCallback: MenuBar.MenuBarManager.ActionCallback) -> None:
        ...
    def GetButtonFromName(self, name: str) -> MenuBar.MenuButton:
        ...
    def RegisterApplication(self, name: str, initializeCallback: MenuBar.MenuBarManager.InitializeMenuApplication, enterCallback: MenuBar.MenuBarManager.EnterMenuApplication, exitCallback: MenuBar.MenuBarManager.ExitMenuApplication, supportsDrawings: bool, supportsDesignInContext: bool, supportsUndo: bool) -> int:
        ...
    def ApplicationSwitchRequest(self, applicationName: str) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.Session.ApplicationSwitchImmediate instead.")"""
        ...
    def RegisterConfigureContextMenuCallback(self, name: str, description: str, configurePopupMenu: MenuBar.MenuBarManager.ConfigureContextMenu) -> int:
        ...
    def UnregisterConfigureContextMenuCallback(self, id: int) -> None:
        ...
    def Tag(self) -> Tag: ...



    

    

    

    

    class CallbackStatus(enum.Enum):
        Continue = 0
        Cancel = 1
        OverrideStandard = 2
        Warning = 3
        Error = 4
    

    

class ContextMenuProperties(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Context: str
    Location: str


class ContextMenuEntry(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    EntryType: MenuBar.ContextMenuEntry.Type
    IsDefault: bool
    IsHidden: bool
    IsSensitive: bool
    Label: str
    Name: str


    class Type(enum.Enum):
        Submenu = 0
        PushButton = 1
        ToggleButton = 2
        Separator = 3
        Label = 4
    

class ContextMenu(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetEntry(self, index: int) -> MenuBar.ContextMenuEntry:
        ...
    def GetSubmenu(self, index: int) -> MenuBar.ContextMenu:
        ...
    def HasEntryWithName(self, name: str) -> bool:
        ...
    def GetEntryWithName(self, name: str) -> MenuBar.ContextMenuEntry:
        ...
    def GetIndexOfEntry(self, entry: MenuBar.ContextMenuEntry) -> int:
        ...
    def AddMenuButton(self, button: MenuBar.MenuButton, index: int) -> MenuBar.ContextMenuEntry:
        ...
    def AddSeparator(self, index: int) -> None:
        ...
    def AddMenuLabel(self, label: str, index: int) -> MenuBar.ContextMenuEntry:
        ...
    def AddSubmenu(self, label: str, index: int) -> MenuBar.ContextMenu:
        ...
    def SetDefaultEntry(self, entry: MenuBar.ContextMenuEntry) -> None:
        ...
    def HideEntry(self, entry: MenuBar.ContextMenuEntry) -> None:
        ...
    def MoveEntry(self, entry: MenuBar.ContextMenuEntry, index: int) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    NumberOfEntries: int


